# ceph-cheatsheet

**Simple, complete offline reference** for Ceph administrators — CLI commands, configuration options, and guides.

→ **[Open the reference (REFERENCE.md)](REFERENCE.md)**

| Section | Content |
|---------|---------|
| [CLI](cli/OVERVIEW.md) | Essential `ceph`, `rbd`, `rados`, `radosgw-admin`, `cephadm` commands |
| [Config](config/OVERVIEW.md) | **2122** options from upstream Ceph YAML (auto-generated) |
| [Guides](guides/quickstart.md) | Daily workflow, config lookup how-to |

**Browse online:** enable GitHub Pages (Settings → Pages → GitHub Actions), or run `mkdocs serve` locally.

## Quick tools

```bash
# Look up one config option (readable summary)
./scripts/lookup-config.sh osd_max_scrubs

# Search everything
./scripts/search-all.sh scrub

# Search config only
./scripts/search-config.sh -s rgw cache
```

## Project layout

```
ceph-cheatsheet/
├── REFERENCE.md            ← main entry point
├── cli/                    ← command reference
├── config/                 ← config option tables (generated)
├── guides/                 ← how-to guides
├── scripts/                ← search, lookup, regenerate
├── mkdocs.yml              ← static site config
└── VERSION                 ← upstream Ceph ref + date
```

## Regenerate config from upstream

```bash
pip install -r scripts/requirements.txt
python3 scripts/generate-config.py --ref main   # or reef, squid, …
```

After editing [`REFERENCE.md`](REFERENCE.md), sync the MkDocs home page:

```bash
python3 scripts/sync-docs-index.py
```

```bash
pip install -r scripts/requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build          # output in site/
```

## Source

Config options are generated from [ceph/ceph](https://github.com/ceph/ceph) `src/common/options/*.yaml.in`.  
CLI content is curated for common admin tasks. See [`VERSION`](VERSION) for the current upstream ref.

## License

GPL-3.0 — see [LICENSE](LICENSE).
