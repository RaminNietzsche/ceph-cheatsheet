---
name: ceph-cheatsheet
description: >-
  Maintain ceph-cheatsheet: Ceph CLI/config reference, RGW architecture docs,
  MkDocs hub (en/fa/zh), section homepages, generators, and CI. Use when editing
  cli/, guides/, config/, arch/, dev/, docs/, mkdocs.yml, scripts/, i18n,
  hub pages, content inventory, or GitHub Pages workflow.
---

# ceph-cheatsheet Maintenance

Read `.cursor/rules/` before editing. Extended detail: [reference.md](reference.md).

## Site structure

| Section | Source | URL |
|---------|--------|-----|
| Hub | `docs/index.md` | `/` |
| Cheatsheet | `cheatsheet/`, `cli/`, `config/`, `guides/` | `/cheatsheet/` |
| Architecture | `arch/` | `/arch/` |
| Develop | `dev/` | `/dev/` |

`docs/` holds symlinks — run `setup-docs-layout.py` after clone.

## One-command regen

```bash
pip install -r scripts/requirements.txt
python3 scripts/regenerate-docs.py
python3 scripts/validate-docs-paths.py
mkdocs serve
```

## Common tasks

### Config from upstream

```bash
python3 scripts/generate-config.py --ref main
python3 scripts/regenerate-docs.py
```

### Search locally

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
./scripts/search-fuzzy.sh
```

### Content inventory (en/fa/zh + human review)

```bash
python3 scripts/generate-content-inventory.py
# edit scripts/content-review.yaml for human-reviewed pages
```

### Edit section hub homepage

1. Edit `cheatsheet/index.md`, `arch/index.md`, or `dev/index.md` (+ `.fa.md`, `.zh.md`)
2. Keep **same HTML skeleton** across all three locales
3. Use site-root locale links (`/fa/cheatsheet/`, not `../fa/`)
4. Run `fix-html-hrefs.py` and `validate-docs-paths.py`

**Never** let `sync-docs-index.py` overwrite section `index.md` — it only syncs `cheatsheet/OVERVIEW.md`, `docs/version.md`, `docs/license.md`.

### Add CLI page

1. Create `cli/<topic>.md` per `documentation.mdc`
2. Add to `cli/OVERVIEW.md` and `mkdocs.yml` nav
3. Add translation keys in `scripts/locales/pages/cli.yaml` if needed
4. Run `sync-i18n-pages.py`

### Add role/scale guide

1. Edit `guides/roles/` or `guides/scales/` (or run `generate-role-scale-guides.py`)
2. Update `guides/OVERVIEW.md` and `REFERENCE.md` if hub links change
3. Run `sync-docs-index.py` for `cheatsheet/OVERVIEW.md` only

## Rules index

| Rule | Scope |
|------|-------|
| `documentation.mdc` | Prose, linking, CLI style |
| `config-generation.mdc` | `config/`, generators |
| `mkdocs-site.mdc` | `docs/`, hubs, CI, symlinks |
| `i18n.mdc` | `.fa.md`, `.zh.md`, locale YAML |
| `no-cursor-coauthor.mdc` | Commits (workspace) |

## CSS / JS for hubs

- `docs/stylesheets/hub.css` — section accents (cyan / indigo / emerald)
- `docs/stylesheets/internal-ergonomics.css` — inner doc pages
- `docs/javascripts/hub.js` — scroll, reveal, pipeline step animation (arch)
