#!/usr/bin/env python3
"""Validate generated routes, links, indexing policy, and CV content."""

import argparse
import html
import json
import re
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "tests" / "fixtures" / "cv_baseline.json"
DOMAIN = "jameswolman.dev"
PROJECT_SLUGS = (
    "aime",
    "where-was-i",
    "redspace-mapping",
    "upstream",
    "declassified-reclassified",
    "talk-data-to-me",
    "self-host-n8n-on-gcr",
)
EXPECTED_PAGES = (
    "index.html",
    "portfolio/index.html",
    *(f"portfolio/projects/{slug}/index.html" for slug in PROJECT_SLUGS),
    "404.html",
)


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFC", html.unescape(value))
    value = re.sub(r"\s+", " ", value).strip()
    return re.sub(r"\s+([,.;:!?])", r"\1", value)


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.main_count = 0
        self.h1_count = 0
        self.meta: list[dict[str, str | None]] = []
        self.references: list[tuple[int, str, str]] = []
        self.links: list[dict[str, str]] = []
        self._main_depth = 0
        self._section_stack: list[str | None] = []
        self._footer_depth = 0
        self._current_link: dict[str, object] | None = None
        self.hero_parts: list[str] = []
        self.section_parts: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        line = self.getpos()[0]
        if element_id := attributes.get("id"):
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag == "main":
            self.main_count += 1
            self._main_depth += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "section" and self._main_depth:
            section_id = attributes.get("id")
            self._section_stack.append(section_id)
            if section_id:
                self.section_parts.setdefault(section_id, [])
        elif tag == "footer" and self._main_depth:
            self._footer_depth += 1

        if tag == "meta":
            self.meta.append(attributes)
        if tag == "a":
            href = attributes.get("href") or ""
            self.references.append((line, "link", href))
            self._current_link = {"href": href, "parts": []}
        for attribute in ("src", "poster"):
            if value := attributes.get(attribute):
                self.references.append((line, "asset", value))
        if tag == "link" and (href := attributes.get("href")):
            self.references.append((line, "asset", href))
        if srcset := attributes.get("srcset"):
            for candidate in srcset.split(","):
                source = candidate.strip().split(" ", 1)[0]
                if source:
                    self.references.append((line, "asset", source))

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._current_link:
            self.links.append({
                "href": str(self._current_link["href"]),
                "label": normalize(" ".join(self._current_link["parts"])),
            })
            self._current_link = None
        if tag == "section" and self._main_depth and self._section_stack:
            self._section_stack.pop()
        elif tag == "footer" and self._main_depth:
            self._footer_depth -= 1
        elif tag == "main":
            self._main_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._current_link:
            self._current_link["parts"].append(data)
        if not self._main_depth or self._footer_depth:
            return
        section_id = self._section_stack[-1] if self._section_stack else None
        if section_id:
            self.section_parts[section_id].append(data)
        else:
            self.hero_parts.append(data)


def parse_page(path: Path) -> DocumentParser:
    parser = DocumentParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve_reference(page: Path, site_dir: Path, reference: str) -> tuple[Path, str] | None:
    if not reference or reference.startswith(("data:", "blob:", "javascript:")):
        return None
    page_url = "/" + page.relative_to(site_dir).as_posix()
    if page_url.endswith("index.html"):
        page_url = page_url[: -len("index.html")]
    absolute = urlparse(urljoin(f"https://{DOMAIN}{page_url}", reference))
    if absolute.scheme not in {"http", "https"} or absolute.hostname != DOMAIN:
        return None
    relative = unquote(absolute.path).lstrip("/")
    target = (site_dir / relative).resolve()
    if not target.is_relative_to(site_dir):
        return target, unquote(absolute.fragment)
    if absolute.path.endswith("/") or not target.suffix:
        target = target / "index.html"
    return target, unquote(absolute.fragment)


def first_missing_token(expected: str, actual: str) -> str | None:
    actual_words = iter(normalize(actual).split())
    for word in normalize(expected).split():
        if not any(candidate == word for candidate in actual_words):
            return word
    return None


def validate_cv(parser: DocumentParser, baseline: dict[str, object]) -> list[str]:
    errors: list[str] = []
    hero = normalize(" ".join(parser.hero_parts))
    if missing := first_missing_token(str(baseline["hero"]), hero):
        errors.append(f"CV hero text changed or disappeared near {missing!r}")
    for section_id, expected in baseline["sections"].items():
        if section_id not in parser.ids:
            errors.append(f"CV section ID {section_id!r} is missing")
        elif missing := first_missing_token(expected, " ".join(parser.section_parts.get(section_id, []))):
            errors.append(f"CV section {section_id!r} text changed or disappeared near {missing!r}")
    for expected_link in baseline["outgoing_links"]:
        if not any(
            link["href"] == expected_link["href"]
            and expected_link["label"] in link["label"]
            for link in parser.links
        ):
            errors.append(
                f"CV outgoing link changed or disappeared: "
                f"{expected_link['label']!r} ({expected_link['href']})"
            )
    return errors


def validate_robots(path: Path) -> list[str]:
    if not path.is_file():
        return ["robots.txt is missing"]
    groups: list[tuple[list[str], list[tuple[str, str]]]] = []
    agents: list[str] = []
    rules: list[tuple[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.partition("#")[0].strip()
        if not line or ":" not in line:
            continue
        key, value = (part.strip().lower() for part in line.split(":", 1))
        if key == "user-agent":
            if rules:
                groups.append((agents, rules))
                agents, rules = [], []
            agents.append(value)
        elif agents:
            rules.append((key, value))
    if agents:
        groups.append((agents, rules))
    generic = [rules for agents, rules in groups if "*" in agents]
    if not generic:
        return ["robots.txt has no generic User-agent: * group"]
    if any(value for rules in generic for key, value in rules if key == "disallow"):
        return ["generic robots.txt rules disallow crawling; noindex must be readable"]
    return []


def main() -> int:
    argument_parser = argparse.ArgumentParser(description=__doc__)
    argument_parser.add_argument(
        "--site-dir", type=Path, default=ROOT / "dist", help="built site directory"
    )
    args = argument_parser.parse_args()
    site_dir = args.site_dir.resolve()
    if not site_dir.is_dir():
        print(f"Site validation failed: built site directory is missing: {site_dir}")
        return 1
    if not BASELINE.is_file():
        print(f"Site validation failed: CV baseline fixture is missing: {BASELINE}")
        return 1
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    errors: list[str] = []
    for relative in EXPECTED_PAGES:
        if not (site_dir / relative).is_file():
            errors.append(f"expected route is missing: {relative}")
    cname = site_dir / "CNAME"
    if not cname.is_file() or cname.read_text(encoding="utf-8").strip() != DOMAIN:
        errors.append(f"CNAME must contain exactly {DOMAIN!r}")
    errors.extend(validate_robots(site_dir / "robots.txt"))

    pages = {path: parse_page(path) for path in site_dir.rglob("*.html")}
    for page, parser in pages.items():
        name = page.relative_to(site_dir).as_posix()
        if parser.main_count != 1 or parser.h1_count != 1:
            errors.append(f"{name}: expected one main and one h1, found {parser.main_count} and {parser.h1_count}")
        if parser.duplicate_ids:
            errors.append(f"{name}: duplicate IDs: {', '.join(sorted(parser.duplicate_ids))}")
        robots = [
            meta.get("content") or ""
            for meta in parser.meta
            if (meta.get("name") or "").lower() == "robots"
        ]
        if not any("noindex" in re.split(r"[,\s]+", content.lower()) for content in robots):
            errors.append(f"{name}: robots meta must include noindex")
        for line, kind, reference in parser.references:
            resolved = resolve_reference(page, site_dir, reference)
            if resolved is None:
                continue
            target, fragment = resolved
            if not target.is_relative_to(site_dir) or not target.is_file():
                errors.append(f"{name}:{line}: {kind} target {reference!r} is missing")
            elif fragment and target.suffix == ".html":
                target_parser = pages.get(target)
                if target_parser is None or fragment not in target_parser.ids:
                    errors.append(f"{name}:{line}: fragment {reference!r} has no matching ID")

    for stylesheet in site_dir.rglob("*.css"):
        css = stylesheet.read_text(encoding="utf-8")
        for match in re.finditer(r"url\(\s*(['\"]?)(.*?)\1\s*\)", css):
            reference = match.group(2)
            if not reference.startswith("/"):
                continue
            resolved = resolve_reference(stylesheet, site_dir, reference)
            if resolved is None or not resolved[0].is_file():
                errors.append(
                    f"{stylesheet.relative_to(site_dir)}: root asset {reference!r} is missing"
                )

    cv_page = site_dir / "index.html"
    if cv_page in pages:
        errors.extend(f"index.html: {error}" for error in validate_cv(pages[cv_page], baseline))
    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site validation passed: {len(pages)} HTML pages and all required routes, links, and CV content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
