# ceph-cheatsheet

**Simple, complete offline reference** for Ceph — organized by **role**, **scale**, CLI, and config.

→ **[Open the reference (REFERENCE.md)](REFERENCE.md)**

| Layer | Content |
|-------|---------|
| [Roles](guides/OVERVIEW.md#by-role) | Cluster admin, storage operator, RGW, CephFS |
| [Scales](guides/OVERVIEW.md#by-scale) | Lab, small/large production, multisite |
| [CLI](cli/OVERVIEW.md) | `ceph`, `rbd`, `rados`, `radosgw-admin`, `cephadm` |
| [Config](config/OVERVIEW.md) | **2122** options from upstream Ceph YAML |
| [Config deep dives](guides/OVERVIEW.md#general) | RGW, OSD, MON, MGR, MDS, Global — tuning + examples |

**Online:** [blog.ceph-s3.ir/cheatsheet](http://blog.ceph-s3.ir/cheatsheet/)

## Quick tools

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
```

## For contributors / agents

- Rules: `.cursor/rules/`
- Skill: `.cursor/skills/ceph-cheatsheet/SKILL.md`
- [Contributing guide](guides/contributing.md)
- [AGENTS.md](AGENTS.md)

## Regenerate config & docs (en + fa + zh)

```bash
pip install -r scripts/requirements.txt
python3 scripts/generate-config.py --ref main
python3 scripts/regenerate-docs.py
mkdocs serve
```

The site uses **mkdocs-static-i18n**: English (`.md`), Persian (`.fa.md`, RTL), Chinese (`.zh.md`). Generators and `sync-i18n-*.py` keep all three in sync on every run.

## License

GPL-3.0 — see [LICENSE](LICENSE).
