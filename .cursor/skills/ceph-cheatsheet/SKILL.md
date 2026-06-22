---
name: ceph-cheatsheet
description: Maintain and extend the ceph-cheatsheet reference (CLI, guides by role/scale, config from upstream YAML, MkDocs site). Use when editing cli/, guides/, config/, running generate-config.py, lookup-config.sh, mkdocs, or GitHub Pages workflow.
---

# ceph-cheatsheet Maintenance

## Project map

| Path | Content | Update method |
|------|---------|---------------|
| `REFERENCE.md` | Main hub | Manual → run `sync-docs-index.py` |
| `cli/` | CLI commands | Manual |
| `guides/roles/` | By operator role | Manual |
| `guides/scales/` | By cluster scale | Manual |
| `config/` | 2122+ options | `generate-config.py` only |
| `docs/` | MkDocs symlinks + `index.md` | Sync from REFERENCE |

## Common tasks

### Regenerate config from Ceph upstream

```bash
python3 scripts/generate-config.py --ref main
```

### Look up / search

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
./scripts/search-config.sh -s rgw cache
```

### Preview site

```bash
pip install -r scripts/requirements.txt
python3 scripts/sync-docs-index.py
mkdocs serve
```

## Adding CLI content

1. Edit or create `cli/<topic>.md` following `.cursor/rules/documentation.mdc`
2. Add entry to `cli/OVERVIEW.md` and `mkdocs.yml` nav if new file
3. Link related config: `../config/<subsystem>/INDEX.md`

## Adding role or scale guides

1. Edit `guides/roles/*.md` or `guides/scales/*.md`
2. Update `guides/OVERVIEW.md` and `REFERENCE.md`
3. Run `sync-docs-index.py`; update `mkdocs.yml` nav if needed

## Rules

Read before editing:

- `.cursor/rules/documentation.mdc` — prose and linking
- `.cursor/rules/config-generation.mdc` — never hand-edit generated tables

## Details

See [reference.md](reference.md) for subsystem list, mkdocs layout, and CI workflow.
