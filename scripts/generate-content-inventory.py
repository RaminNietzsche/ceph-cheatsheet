#!/usr/bin/env python3
"""Build a 6-column inventory of all MkDocs nav pages across en/fa/zh."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_inventory_lib import (  # noqa: E402
    CSV_COLUMNS,
    LABEL_NO,
    LABEL_NO_INCOMPLETE,
    LABEL_NO_MISSING,
    LABEL_UNKNOWN,
    LABEL_YES,
    STATUS_COMPLETE,
    STATUS_MISSING_EMPTY,
    STATUS_MISSING_NAV,
    STATUS_NEEDS_PLACEHOLDER,
    STATUS_NEEDS_SHORT,
    STATUS_NEEDS_TODO,
    aggregate_sections,
    trust_status_for,
)
from repo_paths import REPORTS, ROOT, locale_file, nav_path_to_en_file, source_key_from_en_path  # noqa: E402

REVIEW_FILE = Path(__file__).resolve().parent / "data" / "content-review.yaml"
STRINGS_FILE = Path(__file__).resolve().parent / "locales" / "strings.yaml"
MKDOCS = ROOT / "mkdocs.yml"
DOCS = ROOT / "docs"
REVIEW_AUTO_MARKER = "# --- auto-added by generate-content-inventory.py ---"

LOCALES = ("en", "fa", "zh")

# Content-quality signals
STUB_PATTERNS = (
    r"coming\s+soon",
    r"\*\*status:\*\*\s*coming\s+soon",
    r"^#\s+todo\b",
    r"placeholder\s+page",
    r"not\s+written\s+yet",
)
NEEDS_MORE_PATTERNS = (
    r"\bTODO\b",
    r"\bFIXME\b",
    r"\bTBD\b",
    r"needs?\s+more\s+(detail|explanation|work)",
    r"نیاز\s+به\s+توضیح",
    r"待补充",
)

COLUMNS = CSV_COLUMNS


@dataclass
class LocaleStatus:
    exists: bool
    label: str


@dataclass
class PageRow:
    title: str
    nav_path: str
    source_rel: str
    content_status: str
    en: LocaleStatus
    fa: LocaleStatus
    zh: LocaleStatus
    human_review: str
    source_key: str = ""
    trust_status: str = ""


def load_i18n_notes() -> dict[str, dict[str, str]]:
    if not STRINGS_FILE.exists():
        return {"fallback_page_note": {}, "upstream_table_note": {}}
    data = yaml.safe_load(STRINGS_FILE.read_text(encoding="utf-8")) or {}
    return {
        "fallback_page_note": data.get("fallback_page_note") or {},
        "upstream_table_note": data.get("upstream_table_note") or {},
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
    """Return (breadcrumb title, docs-relative .md path)."""
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
            for title, value in node.items():
                new_trail = trail + [str(title)]
                if isinstance(value, str) and value.endswith(".md"):
                    rows.append((" / ".join(new_trail), value))
                else:
                    walk(value, new_trail)

    walk(items, [])
    return rows


def resolve_source_path(nav_path: str) -> Path | None:
    """Map MkDocs nav path to docs/en/… source file."""
    candidate = nav_path_to_en_file(nav_path)
    if not candidate.exists():
        return None
    return candidate


def locale_path(base: Path, locale: str) -> Path:
    return locale_file(base, locale)


def strip_i18n_prefix(body: str, notes: dict[str, dict[str, str]], locale: str) -> str:
    text = body.lstrip()
    for key in ("fallback_page_note", "upstream_table_note"):
        note = (notes.get(key) or {}).get(locale, "").strip()
        if note and text.startswith(note):
            text = text[len(note) :].lstrip()
    # Generic blockquote notes at top
    while text.startswith(">"):
        line, _, rest = text.partition("\n")
        text = rest.lstrip()
    return text


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text


def is_english_mirror(en_body: str, loc_body: str, notes: dict) -> bool:
    en_norm = normalize_text(en_body)
    loc_core = normalize_text(strip_i18n_prefix(loc_body, notes, "fa"))
    if not loc_core:
        return False
    if en_norm == loc_core:
        return True
    # Mostly English copy with tiny diff
    if len(en_norm) > 80 and en_norm in loc_core:
        return True
    ratio = len(loc_core) / max(len(en_norm), 1)
    if ratio > 0.85 and loc_core[:200] == en_norm[:200]:
        return True
    return False


def has_marker(text: str, patterns: tuple[str, ...]) -> bool:
    flags = re.IGNORECASE | re.MULTILINE
    return any(re.search(p, text, flags) for p in patterns)


def assess_content_depth(en_body: str) -> str:
    if not en_body.strip():
        return STATUS_MISSING_EMPTY
    if has_marker(en_body, STUB_PATTERNS):
        return STATUS_NEEDS_PLACEHOLDER
    stripped = strip_i18n_prefix(en_body, {}, "en")
    if len(stripped.strip()) < 120:
        return STATUS_NEEDS_SHORT
    if has_marker(en_body, NEEDS_MORE_PATTERNS):
        return STATUS_NEEDS_TODO
    return STATUS_COMPLETE


def assess_locale(
    base: Path,
    locale: str,
    en_body: str,
    notes: dict[str, dict[str, str]],
) -> LocaleStatus:
    path = locale_path(base, locale)
    if not path.exists():
        return LocaleStatus(False, LABEL_NO_MISSING)

    body = path.read_text(encoding="utf-8", errors="replace")
    if locale == "en":
        if len(body.strip()) < 40:
            return LocaleStatus(True, LABEL_NO_INCOMPLETE)
        if has_marker(body, STUB_PATTERNS):
            return LocaleStatus(True, LABEL_NO_INCOMPLETE)
        return LocaleStatus(True, LABEL_YES)

    fallback = (notes.get("fallback_page_note") or {}).get(locale, "")
    upstream = (notes.get("upstream_table_note") or {}).get(locale, "")
    if fallback and fallback.strip() in body:
        return LocaleStatus(True, LABEL_NO_INCOMPLETE)
    if upstream and upstream.strip() in body:
        return LocaleStatus(True, LABEL_NO_INCOMPLETE)
    if is_english_mirror(en_body, body, notes):
        return LocaleStatus(True, LABEL_NO_INCOMPLETE)

    core = strip_i18n_prefix(body, notes, locale)
    if len(core.strip()) < 80:
        return LocaleStatus(True, LABEL_NO_INCOMPLETE)

    return LocaleStatus(True, LABEL_YES)


def human_review_label(source_key: str, manifest: dict[str, dict]) -> str:
    entry = manifest.get(source_key, {})
    if entry.get("reviewed") is True:
        return LABEL_YES
    if entry.get("reviewed") is False:
        return LABEL_NO
    locale_flags = [entry.get(loc) for loc in LOCALES if loc in entry]
    if locale_flags:
        if all(v is True for v in locale_flags):
            return LABEL_YES
        if any(v is False for v in locale_flags):
            return LABEL_NO
    return LABEL_UNKNOWN


def build_rows(include_missing_nav: bool = True) -> list[PageRow]:
    notes = load_i18n_notes()
    manifest = load_review_manifest()
    nav_text = extract_nav_block(MKDOCS.read_text(encoding="utf-8"))
    entries = parse_nav_entries(nav_text)

    rows: list[PageRow] = []
    for title, nav_path in entries:
        rel = resolve_source_path(nav_path)
        if rel is None:
            if not include_missing_nav:
                continue
            rows.append(
                PageRow(
                    title=title,
                    nav_path=nav_path,
                    source_rel="",
                    content_status=STATUS_MISSING_NAV,
                    en=LocaleStatus(False, LABEL_NO_MISSING),
                    fa=LocaleStatus(False, LABEL_NO_MISSING),
                    zh=LocaleStatus(False, LABEL_NO_MISSING),
                    human_review=LABEL_UNKNOWN,
                    source_key="",
                    trust_status="",
                )
            )
            continue

        base = rel
        en_body = base.read_text(encoding="utf-8", errors="replace") if base.exists() else ""
        source_key = source_key_from_en_path(base)

        human = human_review_label(source_key, manifest)
        rows.append(
            PageRow(
                title=title,
                nav_path=nav_path,
                source_rel=str(base.relative_to(ROOT)),
                content_status=assess_content_depth(en_body),
                en=assess_locale(base, "en", en_body, notes),
                fa=assess_locale(base, "fa", en_body, notes),
                zh=assess_locale(base, "zh", en_body, notes),
                human_review=human,
                source_key=source_key,
                trust_status=trust_status_for(human, source_key),
            )
        )

    return rows


def write_csv(path: Path, rows: list[PageRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMNS)
        for row in rows:
            writer.writerow(
                [
                    row.title,
                    row.content_status,
                    row.en.label,
                    row.fa.label,
                    row.zh.label,
                    row.human_review,
                    row.source_key,
                    row.nav_path,
                    row.trust_status,
                ]
            )


def write_markdown(path: Path, rows: list[PageRow]) -> None:
    from content_inventory_lib import InventoryRow, aggregate_sections

    path.parent.mkdir(parents=True, exist_ok=True)
    n = len(rows)
    en_yes = sum(1 for r in rows if r.en.label == LABEL_YES)
    fa_yes = sum(1 for r in rows if r.fa.label == LABEL_YES)
    zh_yes = sum(1 for r in rows if r.zh.label == LABEL_YES)
    reviewed = sum(1 for r in rows if r.human_review == LABEL_YES)

    inventory_rows = [
        InventoryRow(
            title=r.title,
            content_status=r.content_status,
            en=r.en.label,
            fa=r.fa.label,
            zh=r.zh.label,
            human_review=r.human_review,
            source_key=r.source_key,
            nav_path=r.nav_path,
            trust_status=r.trust_status,
        )
        for r in rows
    ]
    section_stats = aggregate_sections(inventory_rows)

    lines = [
        "# Documentation content inventory (en / fa / zh)",
        "",
        f"Nav pages: **{n}**",
        "",
        "## Summary",
        "",
        "| Metric | Count | Percent |",
        "| --- | ---: | ---: |",
        f"| EN complete | {en_yes} | {100*en_yes/n:.1f}% |",
        f"| FA complete | {fa_yes} | {100*fa_yes/n:.1f}% |",
        f"| ZH complete | {zh_yes} | {100*zh_yes/n:.1f}% |",
        f"| Human reviewed | {reviewed} | {100*reviewed/n:.1f}% |",
        "",
        "## Section progress",
        "",
        "| Section | Pages | EN | FA | ZH | Human review | Content complete |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for section, stats in section_stats.items():
        total = stats["total"] or 1
        lines.append(
            "| "
            + " | ".join(
                [
                    section.title(),
                    str(stats["total"]),
                    f"{100 * stats['enComplete'] / total:.1f}%",
                    f"{100 * stats['faComplete'] / total:.1f}%",
                    f"{100 * stats['zhComplete'] / total:.1f}%",
                    f"{100 * stats['humanReviewed'] / total:.1f}%",
                    f"{100 * stats['contentComplete'] / total:.1f}%",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "Generated by: `python3 scripts/generate-content-inventory.py`",
            "",
            "Edit `scripts/data/content-review.yaml` for the **Human review** column.",
            "Page trust toasts read from this report via `generate-page-trust-manifest.py`.",
            "",
            "## Pages",
            "",
            "| " + " | ".join(COLUMNS) + " |",
            "| " + " | ".join(["---"] * len(COLUMNS)) + " |",
        ]
    )
    for row in rows:
        cells = [
            row.title.replace("|", "\\|"),
            row.content_status,
            row.en.label,
            row.fa.label,
            row.zh.label,
            row.human_review,
            row.source_key,
            row.nav_path,
            row.trust_status,
        ]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def source_key_from_row(row: PageRow) -> str | None:
    if row.source_key:
        return row.source_key
    if not row.source_rel:
        return None
    rel = Path(row.source_rel)
    parts = rel.parts
    if "en" in parts:
        idx = parts.index("en")
        return str(Path(*parts[idx + 1 :]).with_suffix(""))
    return str(rel.with_suffix(""))


def sync_review_manifest(rows: list[PageRow]) -> list[str]:
    """Append nav pages missing from content-review.yaml (reviewed: false)."""
    manifest = load_review_manifest()
    new_keys = sorted(
        key
        for row in rows
        if (key := source_key_from_row(row)) and key not in manifest
    )
    if not new_keys:
        return []

    text = REVIEW_FILE.read_text(encoding="utf-8") if REVIEW_FILE.exists() else ""
    if not text.endswith("\n"):
        text += "\n"
    if REVIEW_AUTO_MARKER not in text:
        text += f"\n{REVIEW_AUTO_MARKER}\n"

    for key in new_keys:
        text += f"{key}:\n  reviewed: false\n"

    REVIEW_FILE.write_text(text, encoding="utf-8")
    return new_keys


def print_summary(rows: list[PageRow]) -> None:
    n = len(rows)
    en_yes = sum(1 for r in rows if r.en.label == LABEL_YES)
    fa_yes = sum(1 for r in rows if r.fa.label == LABEL_YES)
    zh_yes = sum(1 for r in rows if r.zh.label == LABEL_YES)
    reviewed = sum(1 for r in rows if r.human_review == LABEL_YES)
    needs_work = sum(1 for r in rows if r.content_status.startswith("Needs more detail"))
    print(f"Pages: {n}")
    print(f"  EN complete: {en_yes} ({100*en_yes/n:.1f}%)")
    print(f"  FA complete: {fa_yes} ({100*fa_yes/n:.1f}%)")
    print(f"  ZH complete: {zh_yes} ({100*zh_yes/n:.1f}%)")
    print(f"  Human reviewed: {reviewed} ({100*reviewed/n:.1f}%)")
    print(f"  Needs more explanation (EN): {needs_work}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=REPORTS / "content-inventory.csv",
        help="CSV output path (UTF-8 BOM)",
    )
    parser.add_argument(
        "--md",
        type=Path,
        default=REPORTS / "content-inventory.md",
        help="Markdown table output path",
    )
    parser.add_argument("--no-csv", action="store_true")
    parser.add_argument("--no-md", action="store_true")
    parser.add_argument(
        "--sync-review",
        action="store_true",
        help="Append new nav pages to scripts/data/content-review.yaml with reviewed: false",
    )
    args = parser.parse_args()

    if not MKDOCS.exists():
        print(f"Missing {MKDOCS}", file=sys.stderr)
        return 1

    rows = build_rows()
    if args.sync_review:
        added = sync_review_manifest(rows)
        if added:
            print(f"Added {len(added)} page(s) to {REVIEW_FILE.relative_to(ROOT)}")
            manifest = load_review_manifest()
            for row in rows:
                key = source_key_from_row(row)
                if key:
                    row.human_review = human_review_label(key, manifest)
                    row.trust_status = trust_status_for(row.human_review, key)
    if not args.no_csv:
        write_csv(args.csv, rows)
        print(f"Wrote {args.csv}")
    if not args.no_md:
        write_markdown(args.md, rows)
        print(f"Wrote {args.md}")
    print_summary(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
