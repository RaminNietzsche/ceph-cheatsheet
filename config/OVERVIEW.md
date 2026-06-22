# Ceph Configuration Reference

Browse by subsystem. Each section has an option index and detailed tables.

| Subsystem | Description | Options |
|-----------|-------------|---------|
| [global](global/) | Auth, storage backends, logging, networking, debug | [index](global/INDEX.md) |
| [osd](osd/) | Object Storage Daemon — recovery, scrub, mclock | [index](osd/INDEX.md) |
| [mon](mon/) | Monitor — cluster map, paxos | [index](mon/INDEX.md) |
| [mgr](mgr/) | Manager — modules, cephadm | [index](mgr/INDEX.md) |
| [mds](mds/) | CephFS metadata server | [index](mds/INDEX.md) |
| [mds-client](mds-client/) | CephFS client / FUSE | [index](mds-client/INDEX.md) |
| [rgw](rgw/) | RADOS Gateway — S3, multisite, encryption | [index](rgw/INDEX.md) |
| [rbd](rbd/) | RADOS Block Device — images, cache, features | [index](rbd/INDEX.md) |
| [rbd-mirror](rbd-mirror/) | RBD asynchronous mirroring | [index](rbd-mirror/INDEX.md) |
| [cephfs-mirror](cephfs-mirror/) | CephFS mirroring | [index](cephfs-mirror/INDEX.md) |
| [crimson](crimson/) | Crimson OSD / Seastore (experimental) | [index](crimson/INDEX.md) |
| [immutable-object-cache](immutable-object-cache/) | Immutable object cache | [index](immutable-object-cache/INDEX.md) |
| [ceph-exporter](ceph-exporter/) | Prometheus ceph-exporter metrics | [index](ceph-exporter/INDEX.md) |

## Search

From the repo root:

```bash
./scripts/search-config.sh <option-or-keyword>
./scripts/search-config.sh -s osd scrub
```

## Full master index

The complete cross-subsystem index lives in [`readme.md`](readme.md).  
Run `python3 scripts/split-index.py` to regenerate per-subsystem `INDEX.md` files after editing it.

[← Back to main reference](../REFERENCE.md)
