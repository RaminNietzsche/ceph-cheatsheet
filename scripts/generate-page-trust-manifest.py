#!/usr/bin/env python3
"""Build page trust manifest (human-reviewed vs auto-generated) for site UI."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import ROOT, docs_en_file, nav_path_to_en_file, source_key_from_en_path  # noqa: E402

MKDOCS = ROOT / "mkdocs.yml"
DOCS = ROOT / "docs"
REVIEW_FILE = Path(__file__).resolve().parent / "data" / "content-review.yaml"
DEFAULT_OUT = ROOT / "docs" / "javascripts" / "page-trust-data.js"

LOCALES = ("en", "fa", "zh")

AUTO_GENERATED_PREFIXES = (
    "cheatsheet/config/",
    "cheatsheet/guides/rgw-config/",
    "cheatsheet/guides/osd-config/",
    "cheatsheet/guides/mon-config/",
    "cheatsheet/guides/mgr-config/",
    "cheatsheet/guides/mds-config/",
    "cheatsheet/guides/mds-client-config/",
    "cheatsheet/guides/global-config/",
    "cheatsheet/guides/roles/",
    "cheatsheet/guides/scales/",
)

AUTO_GENERATED_EXACT = frozenset(
    {
        "cheatsheet/OVERVIEW",
        "version",
        "license",
    }
)

UI_STRINGS = {
    "en": {
        "badgeHuman": "Human reviewed",
        "badgeAuto": "Auto-generated",
        "toastHumanTitle": "Human-reviewed content",
        "toastHumanBody": "This page was fully reviewed by a real person for content quality.",
        "toastAutoTitle": "Auto-generated content",
        "toastAutoBody": "This page was produced automatically. It may contain errors; content accuracy is not guaranteed.",
        "toastDismiss": "Dismiss",
    },
    "fa": {
        "badgeHuman": "بررسی انسانی",
        "badgeAuto": "تولید خودکار",
        "toastHumanTitle": "محتوای بررسی‌شده",
        "toastHumanBody": "این صفحه قبلاً توسط یک فرد واقعی به‌صورت کامل از نظر محتوایی بررسی شده است.",
        "toastAutoTitle": "محتوای تولیدشدهٔ خودکار",
        "toastAutoBody": "این صفحه به‌صورت خودکار تولید شده است. ممکن است از نظر محتوا دچار مشکل باشد و صحت آن تضمین نمی‌شود.",
        "toastDismiss": "بستن",
    },
    "zh": {
        "badgeHuman": "人工审核",
        "badgeAuto": "自动生成",
        "toastHumanTitle": "人工审核内容",
        "toastHumanBody": "本页已由专人完整审核，内容质量经过人工确认。",
        "toastAutoTitle": "自动生成内容",
        "toastAutoBody": "本页为自动生成，可能存在内容问题，不保证准确性。",
        "toastDismiss": "关闭",
    },
}


def load_review_manifest() -> dict[str, dict]:
    if not REVIEW_FILE.exists():
        return {}
    data = yaml.safe_load(REVIEW_FILE.read_text(encoding="utf-8")) or {}
    return {k: v for k, v in data.items() if isinstance(v, dict) and not str(k).startswith("#")}


def extract_nav_block(text: str) -> str:
    match = re.search(r"^nav:\s*\n", text, re.MULTILINE)
    if not match:
        raise SystemExit("nav: section not found in mkdocs.yml")
    return text[match.start() :]


def parse_nav_entries(nav_yaml: str) -> list[tuple[str, str]]:
    data = yaml.safe_load(nav_yaml)
    items = data.get("nav") if isinstance(data, dict) else data
    if items is None:
        raise SystemExit("Could not parse nav structure")

    rows: list[tuple[str, str]] = []

    def walk(node, trail: list[str]) -> None:
        if isinstance(node, list):
            for child in node:
                walk(child, trail)
        elif isinstance(node, dict):
            for _title, value in node.items():
                if isinstance(value, str) and value.endswith(".md"):
                    rows.append((value, value))
                else:
                    walk(value, trail)

    walk(items, [])
    return rows


def resolve_source_path(nav_path: str) -> str | None:
    candidate = nav_path_to_en_file(nav_path)
    if not candidate.exists():
        return None
    return source_key_from_en_path(candidate)


def nav_path_to_url(nav_path: str) -> str:
    """MkDocs directory URL path (no locale prefix, no trailing slash)."""
    stem = nav_path[:-3] if nav_path.endswith(".md") else nav_path
    if stem == "index":
        return "/"
    if stem.endswith("/index"):
        stem = stem[: -len("/index")]
    return stem if stem else "/"


def has_generated_frontmatter(path: Path) -> bool:
    if not path.exists():
        return False
    head = path.read_text(encoding="utf-8", errors="replace")[:800]
    if not head.startswith("---"):
        return False
    end = head.find("\n---", 3)
    if end < 0:
        return False
    block = head[3:end]
    return re.search(r"^generated:\s*", block, re.MULTILINE) is not None


def is_auto_generated(source_key: str) -> bool:
    if source_key in AUTO_GENERATED_EXACT:
        return True
    if any(source_key.startswith(prefix) for prefix in AUTO_GENERATED_PREFIXES):
        return True
    path = docs_en_file(source_key)
    if has_generated_frontmatter(path):
        return True
    return False


def human_review_for_locale(entry: dict, locale: str) -> bool | None:
    if entry.get("reviewed") is True:
        return True
    if entry.get("reviewed") is False:
        return False
    if locale in entry:
        val = entry[locale]
        if val is True:
            return True
        if val is False:
            return False
    return None


def trust_for_page(source_key: str, locale: str, manifest: dict[str, dict]) -> str | None:
    entry = manifest.get(source_key, {})
    reviewed = human_review_for_locale(entry, locale)
    if reviewed is True:
        return "human-reviewed"
    if is_auto_generated(source_key):
        return "auto-generated"
    return None


def build_manifest() -> dict:
    review = load_review_manifest()
    nav_text = extract_nav_block(MKDOCS.read_text(encoding="utf-8"))
    entries = parse_nav_entries(nav_text)

    pages: dict[str, dict[str, str]] = {}
    url_to_source: dict[str, str] = {}

    for nav_path in {nav for _, nav in entries}:
        source_key = resolve_source_path(nav_path)
        if not source_key:
            continue

        url = nav_path_to_url(nav_path)
        url_to_source[url] = source_key
        if url != "/":
            url_to_source[url.rstrip("/") or "/"] = source_key

        locale_status: dict[str, str] = {}
        for locale in LOCALES:
            status = trust_for_page(source_key, locale, review)
            if status:
                locale_status[locale] = status
        if locale_status:
            pages[source_key] = locale_status

    return {
        "version": 1,
        "strings": UI_STRINGS,
        "pages": pages,
        "urlToSource": url_to_source,
    }


def write_js(path: Path, manifest: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"))
    path.write_text(f"window.PAGE_TRUST = {payload};\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUT,
        help="Output JS path (default: docs/javascripts/page-trust-data.js)",
    )
    args = parser.parse_args()

    if not MKDOCS.exists():
        print(f"Missing {MKDOCS}", file=sys.stderr)
        return 1

    manifest = build_manifest()
    write_js(args.output, manifest)

    human = sum(
        1
        for locs in manifest["pages"].values()
        for status in locs.values()
        if status == "human-reviewed"
    )
    auto = sum(
        1
        for locs in manifest["pages"].values()
        for status in locs.values()
        if status == "auto-generated"
    )
    print(f"Wrote {args.output}")
    print(f"  Pages with trust labels: {len(manifest['pages'])}")
    print(f"  Human-reviewed (locale entries): {human}")
    print(f"  Auto-generated (locale entries): {auto}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
