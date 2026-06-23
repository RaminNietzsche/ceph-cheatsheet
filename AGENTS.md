# Agent instructions

**ceph-cheatsheet** — Ceph CLI/config reference, RGW architecture, and MkDocs hub (en/fa/zh).

## Before editing

1. Read `.cursor/skills/ceph-cheatsheet/SKILL.md`
2. Apply matching rule from `.cursor/rules/`:
   - `documentation.mdc` — prose under `docs/{en,fa,zh}/`
   - `config-generation.mdc` — `docs/en/cheatsheet/config/` and generators
   - `mkdocs-site.mdc` — `docs/`, `mkdocs.yml`, locale folders
   - `i18n.mdc` — `docs/{en,fa,zh}/`, locale YAML
   - `doc-locale-parity.mdc` — **mandatory en/fa/zh parity** when any doc locale changes
   - `readme-i18n.mdc` — root `README.md` / `README.fa.md` / `README.zh.md`
3. Never hand-edit generated `docs/en/cheatsheet/config/` tables — use `scripts/generate-config.py`

## Site map

| Layer | Path (English) | URL |
|-------|----------------|-----|
| Root hub | `docs/en/index.md` | `/` |
| Cheatsheet | `docs/en/cheatsheet/` | `/cheatsheet/` |
| Architecture | `docs/en/arch/` | `/arch/` |
| Develop | `docs/en/dev/` | `/dev/` |
| Legacy table | `REFERENCE.md` → `docs/en/cheatsheet/OVERVIEW.md` | nav optional |

Persian and Chinese: same paths under `docs/fa/` and `docs/zh/`.

## Regenerate everything

```bash
make all              # install + setup + config + full build
make docs             # generators + mkdocs + restructure (no upstream fetch)
make validate         # nav + symlinks check
make serve            # mkdocs serve (dev)
make serve-site       # static site/ (production URLs)
```

See `make help` and [`scripts/README.md`](scripts/README.md).

## Key scripts

| Task | Command |
|------|---------|
| Verify docs layout | `python3 scripts/setup-docs-layout.py` |
| Sync OVERVIEW/version/license | `python3 scripts/sync-docs-index.py` |
| fa/zh hand pages | `python3 scripts/sync-i18n-pages.py` |
| Root README (en/fa/zh) | `make readme` — edit `README.md` + `scripts/locales/pages/readme.yaml` |
| Content status table | `python3 scripts/generate-content-inventory.py` (see `.cursor/rules/content-inventory.mdc`) |
| Page trust badges / toasts | `python3 scripts/generate-page-trust-manifest.py` |
| Search | `./scripts/lookup-config.sh <opt>` · `./scripts/search-all.sh <term>` |

**Full scripts reference:** [`scripts/README.md`](scripts/README.md)

## Section hub homepages

Edit `docs/en/cheatsheet/index.md`, `docs/en/arch/index.md`, `docs/en/dev/index.md` (+ fa/zh) — **not** overwritten by sync. Keep identical structure across locales; use `/fa/…` absolute locale links.

## Human review tracking

Edit `scripts/data/content-review.yaml`, then run `generate-content-inventory.py` and `generate-page-trust-manifest.py`.

## Live site

http://blog.ceph-s3.ir/ (redirects to `/en/`) · `/fa/` · `/zh/`

## Commits

No `Co-authored-by: Cursor` in commit messages.
