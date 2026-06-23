#!/usr/bin/env python3
"""Keep README.md, README.fa.md, and README.zh.md in sync."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import ROOT, write_localized  # noqa: E402

README_BASE = ROOT / "README.md"
README_KEY = "README"
LOCALE_FILE = Path(__file__).resolve().parent / "locales" / "pages" / "readme.yaml"

LANG_BAR = {
    "en": "**Languages:** English · [فارسی](README.fa.md) · [中文](README.zh.md)",
    "fa": "**زبان‌ها:** [English](README.md) · فارسی · [中文](README.zh.md)",
    "zh": "**语言：** [English](README.md) · [فارسی](README.fa.md) · 中文",
}

HEADING_RE = re.compile(r"^##\s+", re.MULTILINE)


def load_translations() -> dict[str, str]:
    if not LOCALE_FILE.exists():
        raise SystemExit(f"Missing {LOCALE_FILE}")
    data = yaml.safe_load(LOCALE_FILE.read_text(encoding="utf-8")) or {}
    entry = data.get(README_KEY)
    if not isinstance(entry, dict):
        raise SystemExit(f"{LOCALE_FILE}: missing key {README_KEY!r}")
    missing = [loc for loc in ("fa", "zh") if not (entry.get(loc) or "").strip()]
    if missing:
        raise SystemExit(f"{LOCALE_FILE}: {README_KEY} missing translation(s): {', '.join(missing)}")
    return {loc: entry[loc].strip() + "\n" for loc in ("fa", "zh")}


def strip_language_bar(body: str) -> str:
    lines = body.splitlines()
    if not lines:
        return body
    # Remove optional language line near top (after title)
    out: list[str] = []
    skipped_bar = False
    for i, line in enumerate(lines):
        if not skipped_bar and (
            line.startswith("**Languages:**")
            or line.startswith("**زبان‌ها:**")
            or line.startswith("**语言：**")
        ):
            skipped_bar = True
            continue
        if skipped_bar and line.strip() == "":
            continue
        if skipped_bar:
            skipped_bar = False
        out.append(line)
    text = "\n".join(out)
    if text and not text.endswith("\n"):
        text += "\n"
    return text


def ensure_en_language_bar(en_body: str) -> str:
    body = strip_language_bar(en_body)
    lines = body.splitlines()
    if not lines:
        return LANG_BAR["en"] + "\n\n"
    # Insert language bar after first heading line (# title)
    insert_at = 1
    if len(lines) > 1 and lines[1].strip() == "":
        insert_at = 2
    bar_block = [lines[0], "", LANG_BAR["en"], ""]
    rest = lines[1:] if insert_at == 1 else lines[2:]
    while rest and rest[0].strip() == "":
        rest = rest[1:]
    return "\n".join(bar_block + rest) + ("\n" if not body.endswith("\n\n") else "")


def count_h2(text: str) -> int:
    return len(HEADING_RE.findall(text))


def validate_structure(en: str, fa: str, zh: str) -> None:
    en_h2 = count_h2(en)
    fa_h2 = count_h2(fa)
    zh_h2 = count_h2(zh)
    if not (en_h2 == fa_h2 == zh_h2):
        raise SystemExit(
            f"README heading mismatch: en={en_h2} fa={fa_h2} zh={zh_h2} "
            "(each locale must have the same ## sections)"
        )


def sync_readme() -> None:
    if not README_BASE.exists():
        raise SystemExit(f"Missing {README_BASE}")

    translations = load_translations()
    raw_en = README_BASE.read_text(encoding="utf-8")
    en_body = ensure_en_language_bar(raw_en)

    contents = {
        "en": en_body,
        "fa": translations["fa"],
        "zh": translations["zh"],
    }
    validate_structure(contents["en"], contents["fa"], contents["zh"])
    write_localized(README_BASE, contents)
    print(f"Synced README.md, README.fa.md, README.zh.md from {LOCALE_FILE.name}")


def main() -> int:
    sync_readme()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
