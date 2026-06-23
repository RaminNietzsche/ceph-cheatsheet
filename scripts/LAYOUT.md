# Repository layout

Canonical paths (see `scripts/repo_paths.py`):

```
ceph-cheatsheet/
├── docs/                 # MkDocs docs_dir — all content by locale
│   ├── en/               # English (canonical)
│   │   ├── index.md      # Site root hub
│   │   ├── cheatsheet/   # CLI, config, guides
│   │   ├── arch/         # RGW architecture & learning
│   │   └── dev/          # Develop section hub
│   ├── fa/               # Persian (RTL) — same tree as en/
│   ├── zh/               # Chinese — same tree as en/
│   ├── stylesheets/      # Shared theme CSS
│   └── javascripts/      # Shared JS (hub, page-trust, …)
├── reports/              # Generated content-inventory (CSV + MD)
├── scripts/
│   ├── data/             # content-review.yaml
│   ├── locales/          # i18n strings + hand-page translations
│   └── upstream/         # Ceph option YAML inputs
├── mkdocs.yml
├── REFERENCE.md          # Legacy hub table → synced to docs/en/cheatsheet/OVERVIEW.md
└── site/                 # Build output (gitignored)
```

After clone: `python3 scripts/setup-docs-layout.py` then `make docs`.

Published URLs: `/` → `/en/` · `/fa/` · `/zh/` · content under `/en/cheatsheet/`, etc.

**i18n:** mkdocs-static-i18n `docs_structure: folder` — one `docs/{locale}/` tree per language (no `.fa.md` / `.zh.md` suffixes).

**Migration from old layout:** `python3 scripts/migrate-to-docs-locale-folders.py --remove-legacy` (one-time).

**Scripts guide:** [`README.md`](README.md)
