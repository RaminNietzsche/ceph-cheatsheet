#!/usr/bin/env python3
"""Sync cheatsheet hub and auxiliary pages from repo sources for MkDocs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "REFERENCE.md"
CHEATSHEET_OVERVIEW = ROOT / "cheatsheet" / "OVERVIEW.md"
DOCS = ROOT / "docs"
VERSION_SRC = ROOT / "VERSION"
LICENSE_SRC = ROOT / "LICENSE"


def rewrite_cheatsheet_paths(text: str) -> str:
    """Paths in REFERENCE assume docs root; cheatsheet hub lives one level deeper."""
    replacements = [
        ("[`VERSION`](VERSION)", "[VERSION](../version.md)"),
        (
            "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](LICENSE)",
            "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](../license.md)",
        ),
        ("](guides/", "](../guides/"),
        ("](cli/", "](../cli/"),
        ("](config/", "](../config/"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    if "[← Home]" not in text:
        text = "[← Home](../index.md)\n\n" + text
    return text


def sync_cheatsheet_overview() -> None:
    if not REFERENCE.exists():
        raise SystemExit(f"Missing {REFERENCE}")
    text = rewrite_cheatsheet_paths(REFERENCE.read_text(encoding="utf-8"))
    CHEATSHEET_OVERVIEW.parent.mkdir(parents=True, exist_ok=True)
    CHEATSHEET_OVERVIEW.write_text(text, encoding="utf-8")
    print(f"Synced {CHEATSHEET_OVERVIEW} from {REFERENCE}")


def sync_version_page() -> None:
    if not VERSION_SRC.exists():
        raise SystemExit(f"Missing {VERSION_SRC}")
    body = VERSION_SRC.read_text(encoding="utf-8").strip()
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "version.md").write_text(
        "# Upstream source\n\n"
        "Config tables are generated from Ceph upstream YAML.\n\n"
        f"```yaml\n{body}\n```\n",
        encoding="utf-8",
    )
    print(f"Synced {DOCS / 'version.md'} from {VERSION_SRC}")


def sync_license_page() -> None:
    if not LICENSE_SRC.exists():
        raise SystemExit(f"Missing {LICENSE_SRC}")
    text = LICENSE_SRC.read_text(encoding="utf-8")
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "license.md").write_text(
        "# License\n\n"
        "This project is licensed under GPL-3.0.\n\n"
        f"```text\n{text.strip()}\n```\n",
        encoding="utf-8",
    )
    print(f"Synced {DOCS / 'license.md'} from {LICENSE_SRC}")


def main() -> None:
    sync_cheatsheet_overview()
    sync_version_page()
    sync_license_page()


if __name__ == "__main__":
    main()
