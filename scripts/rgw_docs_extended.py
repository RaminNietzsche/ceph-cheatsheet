#!/usr/bin/env python3
"""Shared helpers for syncing dev-code/rgw/docs-extended into docs/fa/arch/rgw/."""

from __future__ import annotations

import os
import re
from pathlib import Path

from repo_paths import DOCS_EN, DOCS_FA, DOCS_ZH, ROOT

DEFAULT_SRC = ROOT / "dev-code" / "rgw" / "docs-extended" / "pages"
OUT_FA = DOCS_FA / "arch" / "rgw"

SKIP_PARTS = frozenset({"appendix", "assets"})

SNIPPET_BLOCK = re.compile(
    r'```(?:\w+ title="[^"]*")?\s*\n--8<-- "([^"]+)"\s*\n```',
    re.MULTILINE,
)
SNIPPET_INLINE = re.compile(r'--8<-- "([^"]+)"')
GITHUB = "https://github.com/ceph/ceph/blob/main/src/rgw/"

LINK_REPLACEMENTS: tuple[tuple[str, str], ...] = (
    ("../../cheatsheet/guides/roles/rgw-admin.md", "../../../cheatsheet/guides/roles/rgw-admin.md"),
    ("../../cheatsheet/cli/troubleshooting.md", "../../../cheatsheet/cli/troubleshooting.md"),
    ("../guides/deployment-implementation-guide.md", "../guides/deployment-implementation-guide.md"),
    ("../guides/development-convention.md", "../guides/development-convention.md"),
    ("../guides/source-code-in-docs.md", "../guides/source-code-in-docs.md"),
    ("../appendix/generated/symbol-index.md", "https://github.com/ceph/ceph/tree/main/src/rgw/docs-extended/pages/appendix/generated/symbol-index.md"),
    ("../appendix/generated/import-graph.md", "https://github.com/ceph/ceph/tree/main/src/rgw/docs-extended/pages/appendix/generated/import-graph.md"),
)


def source_root() -> Path:
    if env := os.environ.get("DEV_CODE_RGW_PAGES"):
        return Path(env)
    if DEFAULT_SRC.is_dir():
        return DEFAULT_SRC
    raise SystemExit(
        "RGW docs source not found. Clone or symlink dev-code/rgw/docs-extended "
        "(see dev-code/ in .gitignore) or set DEV_CODE_RGW_PAGES."
    )


def github_link(ref: str) -> str:
    path, *lines = ref.split(":")
    anchor = ""
    if len(lines) >= 2:
        anchor = f"#L{lines[0]}-L{lines[1]}"
    elif len(lines) == 1:
        anchor = f"#L{lines[0]}"
    return f"{GITHUB}{path}{anchor}"


def process(text: str) -> str:
    def block(match: re.Match[str]) -> str:
        ref = match.group(1)
        path = ref.split(":")[0]
        return f"\n> **Source:** [`{path}`]({github_link(ref)})\n"

    text = SNIPPET_BLOCK.sub(block, text)
    text = SNIPPET_INLINE.sub(
        lambda m: f"[`{m.group(1).split(':')[0]}`]({github_link(m.group(1))})",
        text,
    )
    for old, new in LINK_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def should_skip(path: Path, src: Path) -> bool:
    rel_parts = path.relative_to(src).parts
    if not rel_parts:
        return True
    if rel_parts[0] in SKIP_PARTS:
        return True
    if "generated" in rel_parts:
        return True
    return False


def dest_for(src: Path, rel: Path) -> Path:
    if rel.as_posix() == "index.md":
        return OUT_FA / "OVERVIEW.md"
    return OUT_FA / rel


def needs_locale_stubs(rel: Path) -> bool:
    parts = rel.parts
    return parts and parts[0] in {"guides", "learning-program"}


def title_from_fa(body: str, fallback: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def stub_body(title: str, locale: str, back: str) -> str:
    if locale == "en":
        return (
            f"# {title}\n\n"
            "Persian deep-dive synced from upstream `docs-extended`. "
            "Switch to **فارسی** locale for the full text.\n\n"
            f"{back}\n"
        )
    return (
        f"# {title}\n\n"
        "完整波斯语内容来自 upstream `docs-extended`。请切换到 **فارسی** 语言查看全文。\n\n"
        f"{back}\n"
    )


def back_link_for(rel: Path) -> str:
    if rel.parts[0] == "guides":
        return "[← RGW overview](../OVERVIEW.md)"
    if len(rel.parts) > 1 and rel.parts[1] == "phase-0":
        return "[← Phase 0](index.md) · [Learning program](../index.md)"
    return "[← Learning program](index.md)"


def write_locale_stubs(rel: Path, fa_body: str) -> None:
    fallback = rel.stem.replace("-", " ").replace("_", " ").title()
    title = title_from_fa(fa_body, fallback)
    back = back_link_for(rel)
    for locale, root in (("en", DOCS_EN), ("zh", DOCS_ZH)):
        path = root / "arch" / "rgw" / rel.parent / f"{rel.stem}.md"
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(stub_body(title, locale, back), encoding="utf-8")


def collect_sources(src: Path) -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for path in sorted(src.rglob("*.md")):
        if should_skip(path, src):
            continue
        rel = path.relative_to(src)
        pairs.append((path, dest_for(path, rel)))
    return pairs
