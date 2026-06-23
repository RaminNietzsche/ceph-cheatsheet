#!/usr/bin/env python3
"""Sync role and scale guide translations (fa/zh) from locales/pages/roles-scales.yaml."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import ROOT, write_localized  # noqa: E402

LOCALE_FILE = Path(__file__).resolve().parent / "locales" / "pages" / "roles-scales.yaml"

ROLE_SCALE_PAGES: tuple[str, ...] = (
    "guides/roles/cluster-admin",
    "guides/roles/storage-operator",
    "guides/roles/rgw-admin",
    "guides/roles/cephfs-admin",
    "guides/scales/lab",
    "guides/scales/small-production",
    "guides/scales/large-production",
    "guides/scales/multisite",
)


def load_translations() -> dict[str, dict[str, str]]:
    if not LOCALE_FILE.exists():
        raise SystemExit(f"Missing {LOCALE_FILE}")
    data = yaml.safe_load(LOCALE_FILE.read_text(encoding="utf-8")) or {}
    out: dict[str, dict[str, str]] = {}
    for rel in ROLE_SCALE_PAGES:
        entry = data.get(rel)
        if not isinstance(entry, dict):
            print(f"warning: no translations for {rel}", file=sys.stderr)
            continue
        for loc in ("en", "fa", "zh"):
            if entry.get(loc):
                out.setdefault(rel, {})[loc] = entry[loc].strip() + "\n"
    return out


def sync_page(rel: str, locales: dict[str, str]) -> None:
    en_path = ROOT / f"{rel}.md"
    if "en" in locales:
        en_path.write_text(locales["en"], encoding="utf-8")
    elif not en_path.exists():
        raise SystemExit(f"Missing English source: {en_path}")
    en_body = en_path.read_text(encoding="utf-8")
    contents = {
        "en": locales.get("en", en_body),
        "fa": locales.get("fa", ""),
        "zh": locales.get("zh", ""),
    }
    if not contents["fa"] or not contents["zh"]:
        raise SystemExit(f"Incomplete fa/zh for {rel} — update {LOCALE_FILE}")
    write_localized(en_path, contents)


def main() -> int:
    translations = load_translations()
    for rel in ROLE_SCALE_PAGES:
        sync_page(rel, translations.get(rel, {}))
    print(f"Synced {len(ROLE_SCALE_PAGES)} role/scale guides (en/fa/zh)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
