> **یادداشت:** متن این صفحه هنوز به فارسی ترجمه نشده است؛ نسخهٔ انگلیسی در ادامه آمده است.

# Contributing to the Reference

How this repository is structured, maintained, and extended.

## Cursor rules

Project rules in `.cursor/rules/`:

| Rule | Applies to |
|------|------------|
| `documentation.mdc` | `cli/`, `guides/`, REFERENCE.md |
| `config-generation.mdc` | `config/`, generate scripts |
| `no-cursor-coauthor.mdc` | All commits |

All rules live under `.cursor/rules/` in the repository root.

## Cursor skill

`.cursor/skills/ceph-cheatsheet/SKILL.md` — agent workflow for regenerate, search, mkdocs, and adding content.

## Content types

```
cli/                    Manual — command cheatsheets
guides/roles/           Manual — by operator role
guides/scales/          Manual — by cluster size
guides/rgw-config/      Generated — RGW options by nav category (see below)
config/                 Generated — do not hand-edit tables
docs/                   MkDocs shell — sync index from REFERENCE.md
REFERENCE.md            Hub — sync to docs/index.md
```

## Workflows

**Update config from upstream Ceph:**

```bash
python3 scripts/generate-config.py --ref main
python3 scripts/generate-role-scale-guides.py   # roles + scales (en/fa/zh)
python3 scripts/generate-rgw-guide.py
python3 scripts/generate-config-guide.py all   # OSD, MON, MGR, MDS, global, …
python3 scripts/sync-i18n-config.py            # fa/zh config tables
python3 scripts/sync-i18n-pages.py             # fa/zh hand-written pages
python3 scripts/sync-docs-index.py
```

All generators write **English** (`.md`) plus **Persian** (`.fa.md`) and **Chinese** (`.zh.md`) variants. Template strings live in `scripts/locales/strings.yaml`; hand-page translations in `scripts/locales/pages/`.

The RGW guide generator reads `config/rgw/*.md`, writes topic files under
`guides/rgw-config/<category>/`, and patches `mkdocs.yml` between `# rgw-nav:start` /
`# rgw-nav:end`.

`generate-config-guide.py` does the same for other subsystems (profiles in that
script; nav markers `# osd-nav:start` / … inside `# config-guides-nav:start` in
`mkdocs.yml`). Hand-tuned text for hot OSD/MON options lives in
`scripts/subsystem_enrichments.py`. RGW and global flat guide URLs redirect via
`mkdocs-redirects` (patched by the generators). Re-run both generators after config regeneration.

**Edit prose (CLI, guides, REFERENCE):**

1. Edit files
2. `python3 scripts/sync-docs-index.py`
3. `mkdocs serve` to preview

**CI:** push to `main` → `.github/workflows/docs.yml` builds and deploys Pages.

## Adding a new CLI page

1. Create `cli/mytopic.md` per documentation rule
2. Link from `cli/OVERVIEW.md`, `REFERENCE.md`, `mkdocs.yml`
3. Cross-link from relevant role/scale guide

## Adding a role or scale guide

1. Create under `guides/roles/` or `guides/scales/`
2. Update `guides/OVERVIEW.md` and `REFERENCE.md`
3. Sync docs index and mkdocs nav

[← Guides overview](OVERVIEW.md)
