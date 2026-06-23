# Contributing to the Reference

How this repository is structured, maintained, and extended.

## Cursor rules

Project rules in `.cursor/rules/`:

| Rule | Applies to |
|------|------------|
| `documentation.mdc` | `cli/`, `guides/`, `arch/`, `dev/`, `cheatsheet/`, hub pages |
| `config-generation.mdc` | `config/`, generate scripts |
| `mkdocs-site.mdc` | `docs/`, `mkdocs.yml`, symlinks, CI |
| `i18n.mdc` | `.fa.md`, `.zh.md`, `scripts/locales/` |
| `doc-locale-parity.mdc` | en/fa/zh trio must stay equivalent on every doc edit |
| `readme-i18n.mdc` | Root `README.md`, `README.fa.md`, `README.zh.md` |
| `no-cursor-coauthor.mdc` | All commits |

All rules live under `.cursor/rules/` in the repository root.

## Cursor skill

`.cursor/skills/ceph-cheatsheet/SKILL.md` — agent workflow for regenerate, search, mkdocs, and adding content.

## Content types

```
docs/index.md           Root hub (HTML) — en/fa/zh
cheatsheet/index.md     Cheatsheet section home — en/fa/zh (manual)
arch/index.md           Architecture section home — en/fa/zh (manual)
dev/index.md            Develop section home — en/fa/zh (manual)
cli/                    Manual — command cheatsheets
guides/roles/           Manual / generated — by operator role
guides/scales/          Manual / generated — by cluster size
guides/rgw-config/      Generated — RGW options by nav category
guides/*-config/        Generated — OSD, MON, MGR, … deep dives
arch/rgw/               Synced + learning program
config/                 Generated — do not hand-edit tables
docs/                   MkDocs shell — symlinks via setup-docs-layout.py
REFERENCE.md            Legacy hub table → cheatsheet/OVERVIEW.md
```

## Workflows

**Full scripts reference:** [`scripts/README.md`](../scripts/README.md) (every script, flags, CI order, troubleshooting).

**Update config from upstream Ceph:**

```bash
python3 scripts/setup-docs-layout.py
python3 scripts/generate-config.py --ref main
python3 scripts/regenerate-docs.py
python3 scripts/validate-docs-paths.py
```

`regenerate-docs.py` runs: layout → docs-extended sync → role/scale guides → RGW/config guides → i18n → sync-docs-index → sync-i18n-pages → fix-html-hrefs.

**Content inventory (en/fa/zh status):**

```bash
python3 scripts/generate-content-inventory.py
# human review: edit scripts/data/content-review.yaml
```

**Root README (en / fa / zh):**

Edit `README.md` (English) and matching sections in `scripts/locales/pages/readme.yaml`, then:

```bash
make readme
```

Commit `README.md`, `README.fa.md`, `README.zh.md`, and `readme.yaml` together. CI fails if they drift. See `.cursor/rules/readme-i18n.mdc`.

**i18n overview:**

All generators write **English** (`.md`) plus **Persian** (`.fa.md`) and **Chinese** (`.zh.md`) variants. Template strings live in `scripts/locales/strings.yaml`; hand-page translations in `scripts/locales/pages/`.

The RGW guide generator reads `config/rgw/*.md`, writes topic files under
`guides/rgw-config/<category>/`, and patches `mkdocs.yml` between `# rgw-nav:start` /
`# rgw-nav:end`.

`generate-config-guide.py` does the same for other subsystems (profiles in that
script; nav markers `# osd-nav:start` / … inside `# config-guides-nav:start` in
`mkdocs.yml`). Hand-tuned text for hot OSD/MON options lives in
`scripts/subsystem_enrichments.py`. RGW and global flat guide URLs redirect via
`mkdocs-redirects` (patched by the generators). Re-run both generators after config regeneration.

**Edit prose (CLI, guides, section hubs):**

1. Edit source files (and `.fa.md`/`.zh.md` or locale YAML as needed)
2. `python3 scripts/sync-i18n-pages.py` for HAND_PAGES sources
3. `python3 scripts/fix-html-hrefs.py` if hub HTML changed
4. `python3 scripts/validate-docs-paths.py`
5. `mkdocs serve` to preview

**CI:** push to `main` → `.github/workflows/docs.yml` (layout, generators, validate, build, deploy).

## Adding a new CLI page

1. Create `cli/mytopic.md` per documentation rule
2. Link from `cli/OVERVIEW.md`, `REFERENCE.md`, `mkdocs.yml`
3. Cross-link from relevant role/scale guide

## Adding a role or scale guide

1. Create under `guides/roles/` or `guides/scales/`
2. Update `guides/OVERVIEW.md` and `REFERENCE.md`
3. Sync docs index and mkdocs nav

[← Guides overview](OVERVIEW.md)
