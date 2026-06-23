"""Shared helpers for content inventory CSV and page-trust manifest."""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path

from repo_paths import ROOT, docs_en_file

LABEL_YES = "Yes"
LABEL_NO = "No"
LABEL_NO_INCOMPLETE = "No (incomplete)"
LABEL_NO_MISSING = "No (missing)"
LABEL_UNKNOWN = "Unknown"
STATUS_COMPLETE = "Complete"
STATUS_MISSING_EMPTY = "Missing / empty"
STATUS_NEEDS_PLACEHOLDER = "Needs more detail (placeholder)"
STATUS_NEEDS_SHORT = "Needs more detail (short text)"
STATUS_NEEDS_TODO = "Needs more detail (TODO/FIXME)"
STATUS_MISSING_NAV = "Missing (nav file not found)"
TRUST_HUMAN = "human-reviewed"
TRUST_AUTO = "auto-generated"
TRUST_UNREVIEWED = "unreviewed"

SECTION_KEYS = ("cheatsheet", "arch", "dev")

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

CSV_COLUMNS = (
    "Section / chapter title",
    "Content status",
    "EN complete",
    "FA complete",
    "ZH complete",
    "Human review",
    "Source key",
    "Nav path",
    "Trust status",
)


@dataclass
class InventoryRow:
    title: str
    content_status: str
    en: str
    fa: str
    zh: str
    human_review: str
    source_key: str
    nav_path: str
    trust_status: str


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
    if not source_key:
        return False
    if source_key in AUTO_GENERATED_EXACT:
        return True
    if any(source_key.startswith(prefix) for prefix in AUTO_GENERATED_PREFIXES):
        return True
    path = docs_en_file(source_key)
    if has_generated_frontmatter(path):
        return True
    return False


def trust_status_for(human_review: str, source_key: str) -> str:
    if human_review == LABEL_YES:
        return TRUST_HUMAN
    if is_auto_generated(source_key):
        return TRUST_AUTO
    return TRUST_UNREVIEWED


def nav_path_to_url(nav_path: str) -> str:
    stem = nav_path[:-3] if nav_path.endswith(".md") else nav_path
    if stem == "index":
        return "/"
    if stem.endswith("/index"):
        stem = stem[: -len("/index")]
    return stem if stem else "/"


def section_for_source_key(source_key: str) -> str | None:
    if not source_key:
        return None
    for section in SECTION_KEYS:
        if source_key == section or source_key.startswith(f"{section}/"):
            return section
    return None


def locale_complete(label: str) -> bool:
    return label == LABEL_YES


def aggregate_sections(rows: list[InventoryRow]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {
        section: {
            "total": 0,
            "enComplete": 0,
            "faComplete": 0,
            "zhComplete": 0,
            "humanReviewed": 0,
            "contentComplete": 0,
        }
        for section in SECTION_KEYS
    }
    for row in rows:
        section = section_for_source_key(row.source_key)
        if not section:
            continue
        bucket = stats[section]
        bucket["total"] += 1
        if locale_complete(row.en):
            bucket["enComplete"] += 1
        if locale_complete(row.fa):
            bucket["faComplete"] += 1
        if locale_complete(row.zh):
            bucket["zhComplete"] += 1
        if row.human_review == LABEL_YES:
            bucket["humanReviewed"] += 1
        if row.content_status == STATUS_COMPLETE:
            bucket["contentComplete"] += 1
    return stats


def read_inventory_csv(path: Path) -> list[InventoryRow]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        if "Source key" not in fieldnames:
            raise ValueError(
                f"{path} is missing Source key column; run generate-content-inventory.py"
            )
        rows: list[InventoryRow] = []
        for raw in reader:
            source_key = (raw.get("Source key") or "").strip()
            human_review = (raw.get("Human review") or "").strip()
            trust = (raw.get("Trust status") or "").strip()
            if not trust and source_key:
                trust = trust_status_for(human_review, source_key)
            rows.append(
                InventoryRow(
                    title=(raw.get("Section / chapter title") or "").strip(),
                    content_status=(raw.get("Content status") or "").strip(),
                    en=(raw.get("EN complete") or "").strip(),
                    fa=(raw.get("FA complete") or "").strip(),
                    zh=(raw.get("ZH complete") or "").strip(),
                    human_review=human_review,
                    source_key=source_key,
                    nav_path=(raw.get("Nav path") or "").strip(),
                    trust_status=trust,
                )
            )
        return rows


PROGRESS_STRINGS = {
    "en": {
        "title": "Documentation progress",
        "enComplete": "EN complete",
        "faComplete": "FA complete",
        "zhComplete": "ZH complete",
        "humanReview": "Human reviewed",
        "contentComplete": "Content complete",
        "pages": "pages",
    },
    "fa": {
        "title": "پیشرفت مستندات",
        "enComplete": "تکمیل EN",
        "faComplete": "تکمیل FA",
        "zhComplete": "تکمیل ZH",
        "humanReview": "بررسی انسانی",
        "contentComplete": "محتوای کامل",
        "pages": "صفحه",
    },
    "zh": {
        "title": "文档进度",
        "enComplete": "英文完成",
        "faComplete": "波斯语完成",
        "zhComplete": "中文完成",
        "humanReview": "人工审核",
        "contentComplete": "内容完整",
        "pages": "页",
    },
}
