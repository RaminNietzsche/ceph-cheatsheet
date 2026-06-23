# ceph-cheatsheet — extended reference

## Subsystems (`config/`)

global, osd, mon, mgr, mds, mds-client, rgw, rbd, rbd-mirror, cephfs-mirror, crimson, immutable-object-cache, ceph-exporter

## Roles → CLI / config

| Role | CLI | Config |
|------|-----|--------|
| Cluster admin | `cli/cluster.md`, `cli/cephadm.md`, `cli/config.md` | `config/mon`, `config/mgr`, `config/global/auth.md` |
| Storage operator | `cli/osd-pool.md`, `cli/rados.md` | `config/osd`, `config/global/osd.md` |
| RGW admin | `cli/rgw.md` | `config/rgw/` |
| CephFS admin | `cli/cephfs.md` | `config/mds`, `config/mds-client` |

## Scales → guides

| Scale | Guide | Focus |
|-------|-------|-------|
| Lab | `guides/scales/lab.md` | Minimal mon/osd |
| Small production | `guides/scales/small-production.md` | replica 3, pg autoscale |
| Large production | `guides/scales/large-production.md` | mclock, scrub |
| Multisite | `guides/scales/multisite.md` | rgw zones, mirror |

---

## Scripts (complete)

**Canonical guide:** [`scripts/README.md`](../../scripts/README.md) — every script, CLI flags, CI order, workflows, troubleshooting.

Below is a short index; see README for full detail.

### Layout & validation

| Script | Purpose |
|--------|---------|
| `setup-docs-layout.py` | Create/verify `docs/` symlinks |
| `restructure-site-locales.py` | Post-build: `site/{en,fa,zh}/` + root redirect |
| `fix-html-hrefs.py` | Strip `.md` from hub HTML `href`s |

### Sync & index

| Script | Purpose |
|--------|---------|
| `sync-docs-index.py` | `REFERENCE.md` → `cheatsheet/OVERVIEW.md`; `VERSION`/`LICENSE` → `docs/version.md`, `docs/license.md` |
| `sync-i18n-pages.py` | fa/zh for HAND_PAGES (`cli/`, selected `guides/`, `docs/index`) |
| `sync-i18n-config.py` | fa/zh for `config/OVERVIEW.md` only |
| `sync-rgw-from-docs-extended.py` | `arch/rgw/` from upstream docs-extended |
| `sync-architecture-docs.py` | Legacy arch sync helper |

### Generators

| Script | Output |
|--------|--------|
| `generate-config.py` | `config/` tables from Ceph YAML |
| `split-index.py` | `config/<sub>/INDEX.md` from readme |
| `generate-rgw-guide.py` | `guides/rgw-config/` + mkdocs rgw-nav |
| `generate-config-guide.py` | `guides/*-config/` + mkdocs osd/mon/… nav |
| `generate-role-scale-guides.py` | `guides/roles/`, `guides/scales/` |

### Orchestration & inventory

| Script | Purpose |
|--------|---------|
| `regenerate-docs.py` | Full pipeline (layout → generators → i18n → fix-hrefs) |
| `generate-content-inventory.py` | 6-column en/fa/zh status CSV + markdown |

### Search shell

| Script | Purpose |
|--------|---------|
| `lookup-config.sh` | One config option |
| `search-config.sh` | Search config tables |
| `search-all.sh` | cli + config + guides |
| `search-fuzzy.sh` | Interactive (fzf) |

### Libraries

| Module | Role |
|--------|------|
| `i18n.py` | `t()`, `locale_path()`, `write_localized()` |
| `config_guide_lib.py` | Shared config-guide generator logic |
| `subsystem_enrichments.py` | Hand-tuned option blurbs |
| `rgw_docs_extended.py` | docs-extended sync helpers |

---

## Locale files

| Path | Content |
|------|---------|
| `scripts/locales/strings.yaml` | UI labels, `upstream_table_note`, `fallback_page_note` |
| `scripts/locales/pages/*.yaml` | Hand-page fa/zh bodies |
| `scripts/data/content-review.yaml` | Human review flags for inventory |

### HAND_PAGES (`sync-i18n-pages.py`)

`docs/index`, `docs/version`, `docs/compatibility`, `docs/license`, `config/OVERVIEW`, `cli/*`, `guides/OVERVIEW`, `guides/quickstart`, `guides/getting-started`, `guides/i18n-glossary`, `guides/troubleshooting-guide`, `guides/config-lookup`, `guides/contributing`

**Not in HAND_PAGES** (manual hubs): `cheatsheet/index`, `arch/index`, `dev/index`

---

## MkDocs & CI

- Config: `mkdocs.yml` — `docs_dir: docs`, i18n plugin (en/fa/zh suffix)
- Workflow: `.github/workflows/docs.yml`
- Build order: layout → sync-index → generators → i18n → fix-hrefs → validate → mkdocs build → **restructure-site-locales**
- Deploy: GitHub Pages → proxied at `http://blog.ceph-s3.ir/`
- Published layout: `site/index.html` redirects to `site/en/`; `fa/` and `zh/` are siblings

### docs/ symlink map

```
docs/cheatsheet/cli      → ../../cli
docs/cheatsheet/config   → ../../config
docs/cheatsheet/guides   → ../../guides
docs/cheatsheet/index.md → ../../cheatsheet/index.md
docs/arch                → ../arch
docs/dev                 → ../dev
```

---

## Hub page conventions

- Wrapper: `<div class="hub-page hub-page--section hub-page--{cheatsheet|arch|dev}">`
- Nav: `hub-nav`, locale switcher, `hub-nav__hub-link` → `/` or `/fa/` or `/zh/`
- Hero visuals: cheatsheet=terminal, arch=pipeline, dev=terminal+phase-track
- Inner docs: `internal-ergonomics.css`, `readability.css`

---

## Content inventory columns

1. Full nav breadcrumb title
2. Content status (complete / needs more)
3. EN complete (yes / partial / missing)
4. FA complete
5. ZH complete
6. Human reviewed (`content-review.yaml`)

Output: `reports/content-inventory.csv`, `reports/content-inventory.md`
