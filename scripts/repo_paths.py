"""Canonical repository paths — single source of truth for layout."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
DATA = SCRIPTS / "data"
REPORTS = ROOT / "reports"
DOCS = ROOT / "docs"

LOCALES: tuple[str, ...] = ("en", "fa", "zh")
DOCS_EN = DOCS / "en"
DOCS_FA = DOCS / "fa"
DOCS_ZH = DOCS / "zh"

CHEATSHEET = DOCS_EN / "cheatsheet"
CLI = CHEATSHEET / "cli"
CONFIG = CHEATSHEET / "config"
GUIDES = CHEATSHEET / "guides"

ARCH = DOCS_EN / "arch"
DEV = DOCS_EN / "dev"

# MkDocs nav prefix (URL segment under each locale)
CHEATSHEET_NAV = "cheatsheet"

# Shared MkDocs assets (language-agnostic)
DOCS_STYLESHEETS = DOCS / "stylesheets"
DOCS_JAVASCRIPTS = DOCS / "javascripts"

# Legacy root paths (pre-migration); used only by migrate-to-docs-locale-folders.py
LEGACY_CHEATSHEET = ROOT / "cheatsheet"
LEGACY_ARCH = ROOT / "arch"
LEGACY_DEV = ROOT / "dev"


def docs_locale_root(locale: str) -> Path:
    if locale not in LOCALES:
        raise ValueError(f"Unsupported locale: {locale}")
    return DOCS / locale


def docs_en_file(rel: str) -> Path:
    """Map logical key (no .md) to docs/en/{rel}.md — e.g. cheatsheet/cli/cluster."""
    return DOCS_EN / f"{rel}.md"


def locale_file(en_path: Path, locale: str) -> Path:
    """Map docs/en/.../page.md → docs/{locale}/.../page.md."""
    if locale == "en":
        return en_path
    rel = en_path.relative_to(DOCS_EN)
    return DOCS / locale / rel


def source_key_from_en_path(en_path: Path) -> str:
    """docs/en/cheatsheet/cli/cluster.md → cheatsheet/cli/cluster."""
    return str(en_path.relative_to(DOCS_EN).with_suffix(""))


def nav_path_to_en_file(nav_path: str) -> Path:
    """MkDocs nav entry → docs/en/{nav_path}."""
    return DOCS_EN / nav_path
