#!/usr/bin/env python3
"""Build page trust manifest from reports/content-inventory.csv for site UI."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_inventory_lib import (  # noqa: E402
    PROGRESS_STRINGS,
    TRUST_AUTO,
    TRUST_HUMAN,
    TRUST_UNREVIEWED,
    aggregate_sections,
    nav_path_to_url,
    read_inventory_csv,
    trust_status_for,
)
from repo_paths import REPORTS, ROOT  # noqa: E402

DEFAULT_CSV = REPORTS / "content-inventory.csv"
DEFAULT_OUT = ROOT / "docs" / "javascripts" / "page-trust-data.js"

LOCALES = ("en", "fa", "zh")

UI_STRINGS = {
    "en": {
        "badgeHuman": "Human reviewed",
        "badgeAuto": "Auto-generated",
        "toastHumanTitle": "Human-reviewed content",
        "toastHumanBody": "This page was fully reviewed by a real person for content quality.",
        "toastAutoTitle": "Auto-generated content",
        "toastAutoBody": "This page was produced automatically. It may contain errors; content accuracy is not guaranteed.",
        "toastDismiss": "Dismiss",
        "badgeUnreviewed": "Not human-reviewed",
        "toastUnreviewedTitle": "Not yet human-reviewed",
        "toastUnreviewedBody": "This page is published but has not been fully verified by a human reviewer.",
    },
    "fa": {
        "badgeHuman": "بررسی انسانی",
        "badgeAuto": "تولید خودکار",
        "toastHumanTitle": "محتوای بررسی‌شده",
        "toastHumanBody": "این صفحه قبلاً توسط یک فرد واقعی به‌صورت کامل از نظر محتوایی بررسی شده است.",
        "toastAutoTitle": "محتوای تولیدشدهٔ خودکار",
        "toastAutoBody": "این صفحه به‌صورت خودکار تولید شده است. ممکن است از نظر محتوا دچار مشکل باشد و صحت آن تضمین نمی‌شود.",
        "toastDismiss": "بستن",
        "badgeUnreviewed": "بررسی انسانی نشده",
        "toastUnreviewedTitle": "هنوز بررسی انسانی نشده",
        "toastUnreviewedBody": "این صفحه منتشر شده اما هنوز به‌طور کامل توسط یک بررسی‌کنندهٔ انسانی تأیید نشده است.",
    },
    "zh": {
        "badgeHuman": "人工审核",
        "badgeAuto": "自动生成",
        "toastHumanTitle": "人工审核内容",
        "toastHumanBody": "本页已由专人完整审核，内容质量经过人工确认。",
        "toastAutoTitle": "自动生成内容",
        "toastAutoBody": "本页为自动生成，可能存在内容问题，不保证准确性。",
        "toastDismiss": "关闭",
        "badgeUnreviewed": "未人工审核",
        "toastUnreviewedTitle": "尚未人工审核",
        "toastUnreviewedBody": "本页已发布，但尚未经专人完整审核确认。",
    },
}


def build_manifest(csv_path: Path) -> dict:
    rows = read_inventory_csv(csv_path)
    pages: dict[str, dict[str, str]] = {}
    url_to_source: dict[str, str] = {}

    for row in rows:
        if not row.source_key or not row.nav_path:
            continue

        trust = row.trust_status or trust_status_for(row.human_review, row.source_key)
        pages[row.source_key] = {locale: trust for locale in LOCALES}

        url = nav_path_to_url(row.nav_path)
        url_to_source[url] = row.source_key
        if url != "/":
            url_to_source[url.rstrip("/") or "/"] = row.source_key

    return {
        "version": 2,
        "source": str(csv_path.relative_to(ROOT)),
        "strings": UI_STRINGS,
        "progressStrings": PROGRESS_STRINGS,
        "pages": pages,
        "urlToSource": url_to_source,
        "sections": aggregate_sections(rows),
    }


def verify_manifest(manifest: dict) -> list[str]:
    errors: list[str] = []
    pages = manifest.get("pages") or {}
    url_map = manifest.get("urlToSource") or {}

    for source_key, locales in pages.items():
        if not locales:
            errors.append(f"missing locale trust labels: {source_key}")
        for locale in LOCALES:
            status = locales.get(locale)
            if status not in {TRUST_HUMAN, TRUST_AUTO, TRUST_UNREVIEWED}:
                errors.append(f"invalid trust status for {source_key}/{locale}: {status!r}")

    for url, source_key in url_map.items():
        if source_key not in pages:
            errors.append(f"urlToSource points to missing page entry: {url} -> {source_key}")

    if not pages:
        errors.append("no pages loaded from inventory CSV")
    return errors


def write_js(path: Path, manifest: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"))
    path.write_text(f"window.PAGE_TRUST = {payload};\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help="Content inventory CSV (default: reports/content-inventory.csv)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUT,
        help="Output JS path (default: docs/javascripts/page-trust-data.js)",
    )
    args = parser.parse_args()

    if not args.csv.exists():
        print(f"Missing {args.csv}; run generate-content-inventory.py first", file=sys.stderr)
        return 1

    try:
        manifest = build_manifest(args.csv)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    gaps = verify_manifest(manifest)
    if gaps:
        print("page-trust manifest gaps:", file=sys.stderr)
        for gap in gaps[:20]:
            print(f"  - {gap}", file=sys.stderr)
        if len(gaps) > 20:
            print(f"  ... and {len(gaps) - 20} more", file=sys.stderr)
        return 1

    write_js(args.output, manifest)

    human = sum(
        1
        for locs in manifest["pages"].values()
        for status in locs.values()
        if status == TRUST_HUMAN
    )
    auto = sum(
        1
        for locs in manifest["pages"].values()
        for status in locs.values()
        if status == TRUST_AUTO
    )
    unreviewed = sum(
        1
        for locs in manifest["pages"].values()
        for status in locs.values()
        if status == TRUST_UNREVIEWED
    )
    print(f"Wrote {args.output} from {args.csv.relative_to(ROOT)}")
    print(f"  Pages with trust labels: {len(manifest['pages'])}")
    print(f"  Human-reviewed (locale entries): {human}")
    print(f"  Auto-generated (locale entries): {auto}")
    print(f"  Unreviewed (locale entries): {unreviewed}")
    for section, stats in (manifest.get("sections") or {}).items():
        total = stats.get("total") or 0
        if not total:
            continue
        print(
            f"  Section {section}: {total} pages, "
            f"EN {100 * stats['enComplete'] / total:.0f}%, "
            f"FA {100 * stats['faComplete'] / total:.0f}%, "
            f"ZH {100 * stats['zhComplete'] / total:.0f}%, "
            f"reviewed {100 * stats['humanReviewed'] / total:.0f}%"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
