#!/usr/bin/env python3
"""Sync docs/index.md and auxiliary pages from repo sources for MkDocs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCE = ROOT / "REFERENCE.md"
DOCS = ROOT / "docs"
INDEX = DOCS / "index.md"
VERSION_SRC = ROOT / "VERSION"
LICENSE_SRC = ROOT / "LICENSE"


def sync_index() -> None:
    if not REFERENCE.exists():
        raise SystemExit(f"Missing {REFERENCE}")
    text = REFERENCE.read_text(encoding="utf-8")
    text = text.replace("[`VERSION`](VERSION)", "[VERSION](version.md)")
    text = text.replace(
        "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](LICENSE)",
        "[README](https://github.com/RaminNietzsche/ceph-cheatsheet) · [License](license.md)",
    )
    DOCS.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(text, encoding="utf-8")
    print(f"Synced {INDEX} from {REFERENCE}")


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
    sync_index()
    sync_version_page()
    sync_license_page()


if __name__ == "__main__":
    main()
