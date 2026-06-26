"""Regression tests for config table parsing."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config_guide_lib import parse_table, related_options  # noqa: E402
from repo_paths import CONFIG  # noqa: E402


def test_parse_table_reads_see_also_column():
    opts = parse_table(CONFIG / "osd" / "osd.md")
    opt = next(o for o in opts if o.name == "osd_max_backfills")
    refs = related_options(opt)
    assert "osd_mclock_override_recovery_settings" in refs
    assert opt.see_also_raw.startswith("[[")


def test_parse_table_reads_long_desc_not_validator():
    opts = parse_table(CONFIG / "osd" / "osd.md")
    opt = next(o for o in opts if o.name == "osd_max_write_size")
    assert "clients from doing very large writes" in opt.long_desc
    assert "std::" not in opt.long_desc


def test_parse_table_reads_flags_column():
    opts = parse_table(CONFIG / "osd" / "osd.md")
    opt = next(o for o in opts if o.name == "osd_mclock_profile")
    assert opt.flags == "RUNTIME"


def test_parse_table_reads_tags_column_when_present():
    opts = parse_table(CONFIG / "osd" / "osd.md")
    assert all(hasattr(o, "tags") for o in opts)
