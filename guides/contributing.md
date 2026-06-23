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
cli/              Manual — command cheatsheets
guides/roles/     Manual — by operator role
guides/scales/    Manual — by cluster size
config/           Generated — do not hand-edit tables
REFERENCE.md      Hub — sync to docs/index.md
```

## Workflows

**Update config from upstream Ceph:**

```bash
python3 scripts/generate-config.py --ref main
python3 scripts/generate-rgw-guide.py
```

The RGW guide generator reads `config/rgw/*.md` and writes `guides/rgw-config/` (441 options, step-by-step tuning in 44 topic files + `TUNING.md`). Re-run after config regeneration; update `mkdocs.yml` nav if new topic groups are added.

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
