# Changelog

All notable changes to this project are documented here.

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [v2026.06.2] — 2026-06-23

### Fixed

- **Critical:** `parse_table()` in `config_guide_lib.py` mapped `see_also`, `long_desc`, and `Tags` to wrong CSV columns — related-option links and long descriptions in generated config guides were broken.
- `lookup-config.sh`, `search-config.sh`, and `search-all.sh` work without ripgrep (`grep` fallback).
- `search-config.sh` name mode searches config option anchors (`SP_<name>`) instead of fragile line-1 filtering.
- Root hub pages for FA/ZH now match EN layout (hero + three portal cards).
- `site_url` uses HTTPS for canonical URLs and sitemap.
- CI runs `pytest` on script parsers; RGW sync step is conditional (no silent `continue-on-error`).

### Changed

- Pinned Python dependencies in `scripts/requirements.txt`.
- `generate-rgw-guide.py` reuses `parse_table()` from `config_guide_lib.py` (no duplicate parser).

## [v2026.06.1] — 2026-06-23

### Added

- Page trust toasts driven from `reports/content-inventory.csv` (human-reviewed / auto-generated / unreviewed).
- Section progress bars on Cheatsheet, Arch, and Dev homepages.
- Inventory CSV columns: source key, nav path, trust status; section summary in `content-inventory.md`.
- Makefile `.venv` support for local builds.

## [v2026.06] — 2026-06-23

### Added

- First release of **Ceph Docs Hub** — cheatsheet, RGW architecture, and developer docs in en/fa/zh.
- Hub at [blog.ceph-s3.ir](https://blog.ceph-s3.ir/).
- 2122+ config options, RGW learning program, role/scale guides, fuzzy search script.
