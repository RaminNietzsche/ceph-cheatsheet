#!/usr/bin/env python3
"""Internationalization helpers for generated and synced documentation."""

from __future__ import annotations

import contextvars
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
LOCALES_DIR = Path(__file__).resolve().parent / "locales"
STRINGS_FILE = LOCALES_DIR / "strings.yaml"

LOCALES: tuple[str, ...] = ("en", "fa", "zh")
DEFAULT_LOCALE = "en"
ALT_LOCALES: tuple[str, ...] = ("fa", "zh")

_current_locale = contextvars.ContextVar("doc_locale", default=DEFAULT_LOCALE)

_STRINGS: dict[str, dict[str, str]] | None = None
_LABEL_ORDER: list[str] | None = None


def load_strings() -> dict[str, dict[str, str]]:
    global _STRINGS, _LABEL_ORDER
    if _STRINGS is None:
        data = yaml.safe_load(STRINGS_FILE.read_text(encoding="utf-8")) or {}
        _STRINGS = {k: v for k, v in data.items() if isinstance(v, dict)}
        _LABEL_ORDER = sorted(
            (k for k, v in _STRINGS.items() if k.startswith("label_")),
            key=lambda k: len(_STRINGS[k]["en"]),
            reverse=True,
        )
    return _STRINGS


def set_locale(locale: str) -> None:
    if locale not in LOCALES:
        raise ValueError(f"Unsupported locale: {locale}")
    _current_locale.set(locale)


def get_locale() -> str:
    return _current_locale.get()


def t(key: str, **kwargs: Any) -> str:
    strings = load_strings()
    locale = get_locale()
    entry = strings.get(key)
    if not entry:
        raise KeyError(f"Missing i18n key: {key}")
    text = entry.get(locale) or entry.get(DEFAULT_LOCALE, "")
    if kwargs:
        return text.format(**kwargs)
    return text


def model_label(model: str) -> str:
    key = f"model_{model.lower()}"
    strings = load_strings()
    if key in strings:
        return t(key)
    return model


def locale_path(base: Path, locale: str) -> Path:
    """Map guides/foo/bar.md → bar.fa.md / bar.zh.md (English keeps bar.md)."""
    if locale == DEFAULT_LOCALE:
        return base
    return base.parent / f"{base.stem}.{locale}.md"


def all_locale_paths(base: Path) -> list[Path]:
    return [locale_path(base, loc) for loc in LOCALES]


def write_localized(base: Path, contents: dict[str, str]) -> None:
    base.parent.mkdir(parents=True, exist_ok=True)
    for locale in LOCALES:
        path = locale_path(base, locale)
        path.write_text(contents[locale], encoding="utf-8")


def render_all_locales(render_fn, *args, **kwargs) -> dict[str, str]:
    out: dict[str, str] = {}
    for locale in LOCALES:
        set_locale(locale)
        out[locale] = render_fn(*args, **kwargs)
    set_locale(DEFAULT_LOCALE)
    return out


def apply_inline_labels(text: str, locale: str) -> str:
    """Replace remaining English markdown labels in generated prose."""
    if locale == DEFAULT_LOCALE:
        return text
    strings = load_strings()
    order = _LABEL_ORDER or []
    for key in order:
        en = strings[key]["en"]
        translated = strings[key].get(locale, en)
        text = text.replace(en, translated)
    return text


def wrap_upstream_table(en_body: str, locale: str) -> str:
    if locale == DEFAULT_LOCALE:
        return en_body
    note = t("upstream_table_note")
    return f"{note}\n\n{en_body}"


def enrich_field(
    enrichments: dict[str, dict[str, str]],
    opt_name: str,
    field: str,
    locale_enrichments: dict[str, dict[str, dict[str, str]]] | None = None,
) -> str | None:
    locale = get_locale()
    if locale_enrichments and locale in locale_enrichments:
        localized = locale_enrichments[locale].get(opt_name, {}).get(field)
        if localized:
            return localized
    return enrichments.get(opt_name, {}).get(field)


def cleanup_stale_markdown(directory: Path, keep_bases: set[Path]) -> None:
    """Remove *.md not in keep set (all locale variants of kept bases are kept)."""
    keep_all: set[Path] = set()
    for base in keep_bases:
        keep_all.update(all_locale_paths(base))
    for path in directory.rglob("*.md"):
        if path not in keep_all:
            path.unlink()
            print(f"Removed stale {path.relative_to(ROOT)}")
