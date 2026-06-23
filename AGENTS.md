# Agent instructions

This repository is **ceph-cheatsheet** — an offline Ceph CLI and config reference.

## Before editing

1. Read `.cursor/skills/ceph-cheatsheet/SKILL.md`
2. Follow `.cursor/rules/documentation.mdc` for markdown in `cli/` and `guides/`
3. Never hand-edit generated files in `config/` — use `scripts/generate-config.py`

## Documentation model

| Layer | Path | Organization |
|-------|------|--------------|
| Hub | `REFERENCE.md` | Entry point |
| CLI | `cli/` | By subsystem / tool |
| Config | `config/` | By Ceph subsystem (generated) |
| Guides | `guides/roles/`, `guides/scales/`, `guides/rgw-config/` | By operator role, cluster scale, RGW tuning |

## After changing REFERENCE.md

```bash
python3 scripts/sync-docs-index.py
```

## Search tools

```bash
./scripts/lookup-config.sh <option>
./scripts/search-all.sh <term>
```

## Site

- MkDocs: `mkdocs serve`
- Live: https://blog.raminnietzsche.ir/ceph-cheatsheet/
