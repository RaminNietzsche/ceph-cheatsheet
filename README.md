# ceph-cheatsheet

**Languages:** English · [فارسی](README.fa.md) · [中文](README.zh.md)

**Simple, complete offline reference** for Ceph — organized by **role**, **scale**, CLI, and config.

**Release:** [v2026.06.1](https://github.com/RaminNietzsche/ceph-cheatsheet/releases/tag/v2026.06.1) · **Site:** [blog.ceph-s3.ir](http://blog.ceph-s3.ir/)

→ **[Open the reference](docs/en/cheatsheet/OVERVIEW.md)** · **[Getting started](docs/en/cheatsheet/guides/getting-started.md)**

| Layer | Content |
|-------|---------|
| [Getting started](docs/en/cheatsheet/guides/getting-started.md) | Glossary, learning paths, tools |
| [Roles](docs/en/cheatsheet/guides/OVERVIEW.md#by-role) | Cluster admin, storage operator, RGW, CephFS |
| [Scales](docs/en/cheatsheet/guides/OVERVIEW.md#by-scale) | Lab, small/large production, multisite |
| [Config examples](docs/en/cheatsheet/config/examples/OVERVIEW.md) | Production ceph.conf fragments |
| [Troubleshooting](docs/en/cheatsheet/guides/troubleshooting-guide.md) | PG, OSD, RGW, MON, performance |
| [CLI](docs/en/cheatsheet/cli/OVERVIEW.md) | `ceph`, `rbd`, `rados`, `radosgw-admin`, `cephadm` |
| [Config](docs/en/cheatsheet/config/OVERVIEW.md) | **2122** options from upstream Ceph YAML |
| [Architecture](docs/en/arch/rgw/OVERVIEW.md) | RGW deep dives (docs-extended) |

**Online:** [blog.ceph-s3.ir/cheatsheet](http://blog.ceph-s3.ir/cheatsheet/)

## Quick tools

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-all.sh scrub
./scripts/search-fuzzy.sh          # interactive (needs fzf)
```

## For contributors / agents

- Rules: `.cursor/rules/` · layout: `scripts/LAYOUT.md`
- Skill: `.cursor/skills/ceph-cheatsheet/SKILL.md` · [reference](.cursor/skills/ceph-cheatsheet/reference.md)
- [Contributing guide](docs/en/cheatsheet/guides/contributing.md)
- [AGENTS.md](AGENTS.md)

## Regenerate config & docs (en + fa + zh)

```bash
pip install -r scripts/requirements.txt
make help          # list all targets
make all           # deps + upstream config + full site build
make serve         # mkdocs dev server
```

Or step by step:

```bash
make setup
python3 scripts/generate-config.py --ref main   # or: make config
make docs                                       # full pipeline + build
make serve-site                                 # preview production layout
```

Script details: [`scripts/README.md`](scripts/README.md)

The site uses **mkdocs-static-i18n** (`docs_structure: folder`): `docs/en/`, `docs/fa/` (RTL), `docs/zh/`. Generators and `sync-i18n-*.py` keep all three trees in sync on every run.

## License

GPL-3.0 — see [LICENSE](LICENSE).
