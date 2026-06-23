# ceph-cheatsheet — extended reference

## Subsystems (config/)

global, osd, mon, mgr, mds, mds-client, rgw, rbd, rbd-mirror, cephfs-mirror, crimson, immutable-object-cache, ceph-exporter

## Roles → CLI / config mapping

| Role | CLI | Config |
|------|-----|--------|
| Cluster admin | cli/cluster.md, cli/cephadm.md, cli/config.md | config/mon, config/mgr, config/global/auth.md |
| Storage operator | cli/osd-pool.md, cli/rados.md | config/osd, config/global/osd.md, config/global/bluestore.md |
| RGW admin | cli/rgw.md | config/rgw/ |
| CephFS admin | cli/cephfs.md | config/mds, config/mds-client |

## Scales → focus areas

| Scale | Guides | Key config topics |
|-------|--------|-------------------|
| Lab | guides/scales/lab.md | Minimal mon/osd, single host |
| Small production | guides/scales/small-production.md | replica 3, pg autoscale |
| Large production | guides/scales/large-production.md | mclock, capacity, scrub |
| Multisite | guides/scales/multisite.md | rgw zones, rbd-mirror, cephfs-mirror |

## Scripts

| Script | Purpose |
|--------|---------|
| `generate-config.py` | Pull upstream YAML → markdown |
| `split-index.py` | Split readme.md → per-subsystem INDEX.md |
| `sync-docs-index.py` | REFERENCE.md → docs/index.md |
| `lookup-config.sh` | Pretty-print one option |
| `search-config.sh` | Search config tables |
| `search-all.sh` | Search cli + config + guides |

## CI / Pages

- Workflow: `.github/workflows/docs.yml`
- Site URL: `http://blog.ceph-s3.ir/cheatsheet/`
- `mkdocs.yml` → `docs_dir: docs` (symlinks to cli, config, guides)
