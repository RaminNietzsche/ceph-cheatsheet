#!/usr/bin/env python3
"""Restructure MkDocs output: site/{en,fa,zh}/ + root index.html → en/."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SITE = ROOT / "site"

LOCALE_DIRS = frozenset({"en", "fa", "zh"})
SHARED_AT_ROOT = frozenset({"assets", "stylesheets", "javascripts", "search"})
ROOT_KEEP = frozenset({"sitemap.xml", "sitemap.xml.gz"})

REDIRECT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ceph Docs Hub</title>
  <meta http-equiv="refresh" content="0; url=en/">
  <link rel="canonical" href="en/">
  <script>location.replace("en/");</script>
</head>
<body>
  <p>Redirecting to <a href="en/">English documentation</a>…</p>
</body>
</html>
"""

# Absolute site paths: English at root → under /en/
ABS_EN_REPLACEMENTS: tuple[tuple[str, str], ...] = (
    (r'href="/cheatsheet/', 'href="/en/cheatsheet/'),
    (r'href="/arch/', 'href="/en/arch/'),
    (r'href="/dev/', 'href="/en/dev/'),
    (r'href="/compatibility/', 'href="/en/compatibility/'),
    (r'href="/license/', 'href="/en/license/'),
    (r'href="/version/', 'href="/en/version/'),
    (r'href="/readability-guide/', 'href="/en/readability-guide/'),
    (r'href="/guides/', 'href="/en/guides/'),
    (r'href="/"', 'href="/en/"'),
)

CANONICAL_RE = re.compile(
    r'(<link rel="canonical" href=")(https?://[^/]+)((?:/[^"]*)?)(")',
    re.IGNORECASE,
)


def depth_from_site(html_path: Path, site_dir: Path) -> int:
    return len(html_path.parent.relative_to(site_dir).parts)


def prefix_to_root(site_dir: Path, html_path: Path) -> str:
    return "../" * depth_from_site(html_path, site_dir)


def fix_relative_assets(text: str, html_path: Path, site_dir: Path) -> str:
    """Ensure assets/stylesheets/javascripts resolve to site root shared dirs."""
    prefix = prefix_to_root(site_dir, html_path)

    def repl_attr(match: re.Match[str]) -> str:
        attr, path = match.group(1), match.group(2)
        if path.startswith(("http://", "https://", "//", "/")):
            return match.group(0)
        clean = path
        while clean.startswith("../"):
            clean = clean[3:]
        return f'{attr}="{prefix}{clean}"'

    for folder in ("assets/", "stylesheets/", "javascripts/"):
        text = re.sub(
            rf'((?:href|src))="([^"]*{re.escape(folder)}[^"]*)"',
            repl_attr,
            text,
        )
    return text


def fix_absolute_en_urls(text: str) -> str:
    for old, new in ABS_EN_REPLACEMENTS:
        if old == new:
            continue
        text = text.replace(old, new)
    return text


def bump_base_path(base: str) -> str:
    """Add one site-root segment (English moved under en/)."""
    if base in (".", "./"):
        return ".."
    if base.endswith("/"):
        return base + ".."
    return f"../{base}"


def fix_config_base(text: str, html_path: Path, site_dir: Path) -> str:
    """MkDocs Material resolves search_index.json from __config.base — bump en/ pages."""
    try:
        rel = html_path.relative_to(site_dir)
    except ValueError:
        return text
    if not rel.parts or rel.parts[0] != "en":
        return text

    marker = '<script id="__config" type="application/json">'
    start = text.find(marker)
    if start < 0:
        return text
    end = text.find("</script>", start)
    if end < 0:
        return text

    payload = text[start + len(marker) : end]
    try:
        config = json.loads(payload)
    except json.JSONDecodeError:
        return text

    if "base" in config:
        config["base"] = bump_base_path(str(config["base"]))
        if isinstance(config.get("search"), str) and config["search"]:
            search_path = config["search"]
            if not search_path.startswith(("http://", "https://", "//", "/")):
                config["search"] = bump_base_path(search_path)

    updated = marker + json.dumps(config, separators=(",", ": ")) + "</script>"
    return text[:start] + updated + text[end + len("</script>") :]


def fix_canonical_urls(text: str, html_path: Path, site_dir: Path) -> str:
    rel_parts = html_path.parent.relative_to(site_dir).parts
    if not rel_parts or rel_parts[0] not in LOCALE_DIRS:
        return text
    locale = rel_parts[0]

    def repl(match: re.Match[str]) -> str:
        start, host, path, end = match.group(1), match.group(2), match.group(3), match.group(4)
        path = path or ""
        if path.startswith("/fa") or path.startswith("/zh"):
            return match.group(0)
        if path.startswith("/en"):
            return match.group(0)
        if locale == "en":
            new_path = "/en" + (path if path.startswith("/") else "/" + path)
            return f"{start}{host}{new_path}{end}"
        return match.group(0)

    return CANONICAL_RE.sub(repl, text)


def patch_html_file(path: Path, site_dir: Path) -> bool:
    original = path.read_text(encoding="utf-8", errors="replace")
    updated = original
    updated = fix_relative_assets(updated, path, site_dir)
    updated = fix_config_base(updated, path, site_dir)
    updated = fix_absolute_en_urls(updated)
    updated = fix_canonical_urls(updated, path, site_dir)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def patch_sitemap(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    # Insert /en after host for URLs that are not already /fa/ or /zh/ or /en/
    def repl_loc(m: re.Match[str]) -> str:
        url = m.group(1)
        if "/fa/" in url or "/zh/" in url or "/en/" in url:
            return f"<loc>{url}</loc>"
        # root URL
        if re.search(r"https?://[^/]+/?$", url):
            return f"<loc>{url.rstrip('/')}/en/</loc>"
        return f"<loc>{re.sub(r'(https?://[^/]+)/', r'\\1/en/', url, count=1)}</loc>"

    text = re.sub(r"<loc>(.*?)</loc>", repl_loc, text)
    path.write_text(text, encoding="utf-8")


def move_english_to_en(site_dir: Path) -> list[str]:
    en_dir = site_dir / "en"
    en_dir.mkdir(exist_ok=True)
    moved: list[str] = []

    root_index = site_dir / "index.html"
    if root_index.is_file():
        shutil.move(str(root_index), str(en_dir / "index.html"))
        moved.append("index.html")

    for child in list(site_dir.iterdir()):
        name = child.name
        if name in LOCALE_DIRS or name in SHARED_AT_ROOT or name in ROOT_KEEP:
            continue
        dest = en_dir / name
        if dest.exists():
            if dest.is_dir():
                shutil.rmtree(dest)
            else:
                dest.unlink()
        shutil.move(str(child), str(dest))
        moved.append(name)
    return moved


def restructure(site_dir: Path) -> int:
    if not site_dir.is_dir():
        print(f"error: site directory missing: {site_dir}", file=sys.stderr)
        return 1

    moved = move_english_to_en(site_dir)
    (site_dir / "index.html").write_text(REDIRECT_HTML, encoding="utf-8")

    patched = 0
    for html in site_dir.rglob("*.html"):
        if patch_html_file(html, site_dir):
            patched += 1

    for name in ("sitemap.xml",):
        patch_sitemap(site_dir / name)

    print(f"restructure-site-locales: moved {len(moved)} item(s) → en/")
    print(f"  moved: {', '.join(sorted(moved)) or '(none)'}")
    print(f"  patched {patched} HTML file(s); root index.html → en/")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--site-dir",
        type=Path,
        default=DEFAULT_SITE,
        help="MkDocs output directory (default: site/)",
    )
    args = parser.parse_args()
    return restructure(args.site_dir.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
