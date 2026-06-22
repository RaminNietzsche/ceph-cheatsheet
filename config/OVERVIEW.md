# Ceph Configuration Reference

Browse by subsystem. Each section has an option index and detailed tables.

| Subsystem | Description | Options |
|-----------|-------------|---------|
| [global](global/INDEX.md) | Auth, storage backends, logging, networking, debug | [index](global/INDEX.md) |
| [osd](osd/INDEX.md) | Object Storage Daemon — recovery, scrub, mclock | [index](osd/INDEX.md) |
| [mon](mon/INDEX.md) | Monitor — cluster map, paxos | [index](mon/INDEX.md) |
| [mgr](mgr/INDEX.md) | Manager — modules, cephadm | [index](mgr/INDEX.md) |
| [mds](mds/INDEX.md) | CephFS metadata server | [index](mds/INDEX.md) |
| [mds-client](mds-client/INDEX.md) | CephFS client / FUSE | [index](mds-client/INDEX.md) |
| [rgw](rgw/INDEX.md) | RADOS Gateway — S3, multisite, encryption | [index](rgw/INDEX.md) |
| [rbd](rbd/INDEX.md) | RADOS Block Device — images, cache, features | [index](rbd/INDEX.md) |
| [rbd-mirror](rbd-mirror/INDEX.md) | RBD asynchronous mirroring | [index](rbd-mirror/INDEX.md) |
| [cephfs-mirror](cephfs-mirror/INDEX.md) | CephFS mirroring | [index](cephfs-mirror/INDEX.md) |
| [crimson](crimson/INDEX.md) | Crimson OSD / Seastore (experimental) | [index](crimson/INDEX.md) |
| [immutable-object-cache](immutable-object-cache/INDEX.md) | Immutable object cache | [index](immutable-object-cache/INDEX.md) |
| [ceph-exporter](ceph-exporter/INDEX.md) | Prometheus ceph-exporter metrics | [index](ceph-exporter/INDEX.md) |

## Search

From the repo root:

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## Full master index

The complete cross-subsystem index lives in [`readme.md`](readme.md).  
Run `python3 scripts/split-index.py` to regenerate per-subsystem `INDEX.md` files after editing it.

[← Back to main reference](../index.md)
