#!/usr/bin/env python3
"""Sync auxiliary MkDocs pages (version, license, cheatsheet OVERVIEW legacy)."""

from __future__ import annotations

from pathlib import Path

from repo_paths import CHEATSHEET, DOCS_EN

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "REFERENCE.md"
OVERVIEW = CHEATSHEET / "OVERVIEW.md"
VERSION_SRC = ROOT / "VERSION"
LICENSE_SRC = ROOT / "LICENSE"


def rewrite_cheatsheet_paths(text: str) -> str:
    """REFERENCE paths assume repo root; OVERVIEW is served at /cheatsheet/."""
    replacements = [
        ("[`VERSION`](VERSION)", "[VERSION](../../version.md)"),
        (
            "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](LICENSE)",
            "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](../../license.md)",
        ),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    if "[← Home]" not in text:
        text = "[← Home](../../index.md)\n\n" + text
    return text


def sync_cheatsheet_overview() -> None:
    """Legacy reference table — do not overwrite cheatsheet/index.md (section hub)."""
    if not REFERENCE.exists():
        raise SystemExit(f"Missing {REFERENCE}")
    text = rewrite_cheatsheet_paths(REFERENCE.read_text(encoding="utf-8"))
    CHEATSHEET.mkdir(parents=True, exist_ok=True)
    OVERVIEW.write_text(text, encoding="utf-8")
    print(f"Synced {OVERVIEW} from {REFERENCE}")


def sync_version_page() -> None:
    if not VERSION_SRC.exists():
        raise SystemExit(f"Missing {VERSION_SRC}")
    body = VERSION_SRC.read_text(encoding="utf-8").strip()
    DOCS_EN.mkdir(parents=True, exist_ok=True)
    (DOCS_EN / "version.md").write_text(
        "# Upstream source\n\n"
        "Config tables are generated from Ceph upstream YAML.\n\n"
        f"```yaml\n{body}\n```\n",
        encoding="utf-8",
    )
    print(f"Synced {DOCS_EN / 'version.md'} from {VERSION_SRC}")


def sync_license_page() -> None:
    if not LICENSE_SRC.exists():
        raise SystemExit(f"Missing {LICENSE_SRC}")
    text = LICENSE_SRC.read_text(encoding="utf-8")
    DOCS_EN.mkdir(parents=True, exist_ok=True)
    (DOCS_EN / "license.md").write_text(
        "# License\n\n"
        "This project is licensed under GPL-3.0.\n\n"
        f"```text\n{text.strip()}\n```\n",
        encoding="utf-8",
    )
    print(f"Synced {DOCS_EN / 'license.md'} from {LICENSE_SRC}")


def main() -> None:
    sync_cheatsheet_overview()
    sync_version_page()
    sync_license_page()


if __name__ == "__main__":
    main()
