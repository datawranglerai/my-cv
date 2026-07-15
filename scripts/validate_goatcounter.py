#!/usr/bin/env python3
"""Validate the CV's GoatCounter link-tracking contract."""

import base64
import hashlib
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
GOATCOUNTER_SCRIPT = ROOT / "vendor" / "goatcounter" / "count.js"
OUTGOING_SCHEMES = {"http", "https", "mailto", "tel"}


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[tuple[int, dict[str, str | None]]] = []
        self.ids: set[str] = set()
        self.scripts: list[tuple[int, dict[str, str | None]]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        line = self.getpos()[0]

        if element_id := attributes.get("id"):
            self.ids.add(element_id)
        if tag == "a":
            self.anchors.append((line, attributes))
        elif tag == "script":
            self.scripts.append((line, attributes))


def main() -> int:
    parser = DocumentParser()
    parser.feed(INDEX.read_text(encoding="utf-8"))
    errors: list[str] = []

    goatcounter_scripts = [
        (line, attrs)
        for line, attrs in parser.scripts
        if attrs.get("data-goatcounter")
    ]
    if len(goatcounter_scripts) != 1:
        errors.append(f"expected one GoatCounter script, found {len(goatcounter_scripts)}")
    else:
        line, script = goatcounter_scripts[0]
        required = {
            "src": "vendor/goatcounter/count.js",
            "data-goatcounter": "https://datawranglerai.goatcounter.com/count",
            "crossorigin": "anonymous",
        }
        for attribute, expected in required.items():
            if script.get(attribute) != expected:
                errors.append(
                    f"line {line}: expected {attribute}={expected!r}, "
                    f"found {script.get(attribute)!r}"
                )
        if "defer" not in script:
            errors.append(f"line {line}: GoatCounter must load with defer")
        if "async" in script:
            errors.append(f"line {line}: GoatCounter must not load with async")
        if not GOATCOUNTER_SCRIPT.is_file():
            errors.append(f"line {line}: vendored GoatCounter script is missing")
        else:
            script_bytes = GOATCOUNTER_SCRIPT.read_bytes()
            digest = base64.b64encode(hashlib.sha384(script_bytes).digest()).decode("ascii")
            expected_integrity = f"sha384-{digest}"
            if script.get("integrity") != expected_integrity:
                errors.append(
                    f"line {line}: GoatCounter integrity must be {expected_integrity!r}"
                )
            if b"goatcounterNoSession" not in script_bytes:
                errors.append(
                    f"line {line}: vendored GoatCounter script lacks raw-click support"
                )

    tracked_events: list[tuple[int, str]] = []
    for line, anchor in parser.anchors:
        href = anchor.get("href") or ""
        scheme = urlparse(href).scheme.lower()
        if scheme in OUTGOING_SCHEMES:
            event = anchor.get("data-goatcounter-click") or ""
            if not event:
                errors.append(f"line {line}: outgoing link {href!r} is not tracked")
            elif event.startswith("/"):
                errors.append(f"line {line}: event {event!r} must not start with '/'")
            else:
                tracked_events.append((line, event))
            if anchor.get("data-goatcounter-no-session") != "1":
                errors.append(f"line {line}: outgoing link {href!r} does not count every click")
        elif href.startswith("#") and href[1:] not in parser.ids:
            errors.append(f"line {line}: fragment {href!r} has no matching element")

    counts = Counter(event for _, event in tracked_events)
    for event, count in counts.items():
        if count > 1:
            lines = [str(line) for line, value in tracked_events if value == event]
            errors.append(f"event {event!r} is duplicated on lines {', '.join(lines)}")

    if errors:
        print("GoatCounter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"GoatCounter validation passed: {len(tracked_events)} outgoing links "
        "have unique raw-click events."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
