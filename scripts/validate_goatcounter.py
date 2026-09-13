#!/usr/bin/env python3
"""Validate GoatCounter tracking on every generated page."""

import argparse
import base64
import hashlib
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
OUTGOING_SCHEMES = {"http", "https", "mailto", "tel"}
SCRIPT_PATH = "/vendor/goatcounter/count.js"
ENDPOINT = "https://datawranglerai.goatcounter.com/count"


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
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


def validate_page(path: Path, script_bytes: bytes, integrity: str) -> list[str]:
    parser = DocumentParser()
    parser.feed(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    goatcounter_scripts = [
        (line, attrs)
        for line, attrs in parser.scripts
        if attrs.get("data-goatcounter") is not None
        or (attrs.get("src") or "").endswith(SCRIPT_PATH)
    ]
    if len(goatcounter_scripts) != 1:
        errors.append(f"expected one GoatCounter script, found {len(goatcounter_scripts)}")
    else:
        line, script = goatcounter_scripts[0]
        required = {
            "src": SCRIPT_PATH,
            "data-goatcounter": ENDPOINT,
            "crossorigin": "anonymous",
            "integrity": integrity,
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
        if b"goatcounterNoSession" not in script_bytes:
            errors.append(f"line {line}: vendored GoatCounter script lacks raw-click support")

    tracked_events: list[tuple[int, str]] = []
    for line, anchor in parser.anchors:
        href = anchor.get("href") or ""
        if urlparse(href).scheme.lower() in OUTGOING_SCHEMES:
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
    return errors


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        "--site-dir", type=Path, default=ROOT / "dist", help="built site directory"
    )
    args = argument_parser.parse_args()
    site_dir = args.site_dir.resolve()
    if not site_dir.is_dir():
        print(f"GoatCounter validation failed: built site directory is missing: {site_dir}")
        return 1
    pages = sorted(site_dir.rglob("*.html"))
    if not pages:
        print(f"GoatCounter validation failed: no HTML pages found in {site_dir}")
        return 1

    vendored_script = ROOT / "public" / "vendor" / "goatcounter" / "count.js"
    if not vendored_script.is_file():
        print(f"GoatCounter validation failed: vendored script is missing: {vendored_script}")
        return 1
    script_bytes = vendored_script.read_bytes()
    digest = base64.b64encode(hashlib.sha384(script_bytes).digest()).decode("ascii")
    integrity = f"sha384-{digest}"
    errors: list[str] = []
    built_script = site_dir / "vendor" / "goatcounter" / "count.js"
    if not built_script.is_file() or built_script.read_bytes() != script_bytes:
        errors.append("built GoatCounter script is missing or differs from public/vendor copy")
    for page in pages:
        errors.extend(f"{page.relative_to(site_dir)}: {error}" for error in validate_page(page, script_bytes, integrity))

    if errors:
        print("GoatCounter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"GoatCounter validation passed: {len(pages)} pages have tracked outgoing links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
