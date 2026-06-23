#!/usr/bin/env python3
"""Sync fa/zh markdown for hand-written docs (cli/, guides prose, docs/)."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import set_locale, t, write_localized  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

PAGES_DIR = Path(__file__).resolve().parent / "locales" / "pages"

# English sources relative to repo root (without .md suffix for pairing).
HAND_PAGES: tuple[str, ...] = (
    "docs/index",
    "docs/version",
    "docs/license",
    "config/OVERVIEW",
    "cli/OVERVIEW",
    "cli/cluster",
    "cli/config",
    "cli/osd-pool",
    "cli/rados",
    "cli/rbd",
    "cli/rgw",
    "cli/cephfs",
    "cli/cephadm",
    "cli/troubleshooting",
    "guides/OVERVIEW",
    "guides/quickstart",
    "guides/config-lookup",
    "guides/contributing",
)


def load_page_translations() -> dict[str, dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    if not PAGES_DIR.exists():
        return merged
    for path in sorted(PAGES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for rel, locales in data.items():
            if isinstance(locales, dict):
                merged[rel] = {k: v for k, v in locales.items() if k in ("fa", "zh") and v}
    return merged


def fallback_translation(en_path: Path, locale: str) -> str:
    body = en_path.read_text(encoding="utf-8")
    set_locale(locale)
    note = t("upstream_table_note") or ""
    set_locale("en")
    if note:
        return f"{note}\n\n{body}"
    return body


def sync_page(rel: str, translations: dict[str, dict[str, str]]) -> None:
    en_path = ROOT / f"{rel}.md"
    if not en_path.exists():
        print(f"warning: missing {en_path}", file=sys.stderr)
        return
    en_body = en_path.read_text(encoding="utf-8")
    page_tr = translations.get(rel, {})
    contents = {
        "en": en_body,
        "fa": page_tr.get("fa") or fallback_translation(en_path, "fa"),
        "zh": page_tr.get("zh") or fallback_translation(en_path, "zh"),
    }
    write_localized(en_path, contents)


def main() -> None:
    translations = load_page_translations()
    for rel in HAND_PAGES:
        sync_page(rel, translations)
    print(f"Synced i18n for {len(HAND_PAGES)} hand-written page(s)")


if __name__ == "__main__":
    main()
