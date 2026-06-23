#!/usr/bin/env python3
"""Sync role and scale guide translations (fa/zh) from locales/pages/roles-scales.yaml."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from i18n import write_localized  # noqa: E402
from repo_paths import docs_en_file  # noqa: E402

LOCALE_FILE = Path(__file__).resolve().parent / "locales" / "pages" / "roles-scales.yaml"
RGW_ENRICH_FILE = (
    Path(__file__).resolve().parent / "locales" / "pages" / "rgw-from-docs-extended.yaml"
)

ROLE_SCALE_PAGES: tuple[str, ...] = (
    "cheatsheet/guides/roles/cluster-admin",
    "cheatsheet/guides/roles/storage-operator",
    "cheatsheet/guides/roles/rgw-admin",
    "cheatsheet/guides/roles/cephfs-admin",
    "cheatsheet/guides/scales/lab",
    "cheatsheet/guides/scales/small-production",
    "cheatsheet/guides/scales/large-production",
    "cheatsheet/guides/scales/multisite",
)


def load_yaml_pages(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: dict[str, dict[str, str]] = {}
    for rel in ROLE_SCALE_PAGES:
        entry = data.get(rel)
        if not isinstance(entry, dict):
            continue
        for loc in ("en", "fa", "zh"):
            if entry.get(loc):
                out.setdefault(rel, {})[loc] = entry[loc].strip() + "\n"
    return out


def load_translations() -> dict[str, dict[str, str]]:
    if not LOCALE_FILE.exists():
        raise SystemExit(f"Missing {LOCALE_FILE}")
    base = load_yaml_pages(LOCALE_FILE)
    enrich = load_yaml_pages(RGW_ENRICH_FILE)
    out: dict[str, dict[str, str]] = {}
    for rel in ROLE_SCALE_PAGES:
        merged: dict[str, str] = {}
        for loc in ("en", "fa", "zh"):
            parts = [
                base.get(rel, {}).get(loc, ""),
                enrich.get(rel, {}).get(loc, ""),
            ]
            body = "\n\n".join(p.strip() for p in parts if p.strip())
            if body:
                merged[loc] = body + "\n"
        if merged:
            out[rel] = merged
        elif rel not in base:
            print(f"warning: no translations for {rel}", file=sys.stderr)
    return out


def sync_page(rel: str, locales: dict[str, str]) -> None:
    en_path = docs_en_file(rel)
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
