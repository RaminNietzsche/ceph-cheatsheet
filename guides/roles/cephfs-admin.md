# CephFS Admin

Manage Ceph file systems, metadata servers (MDS), subvolumes, and mirroring.

## Daily commands

```bash
ceph fs ls
ceph fs status myfs
ceph mds stat
ceph orch ps --service-type mds
```

See [CephFS CLI](../../cli/cephfs.md).

## Configuration

| Area | Config index |
|------|--------------|
| MDS daemon | [config/mds/INDEX.md](../../config/mds/INDEX.md) |
| Client / FUSE | [config/mds-client/INDEX.md](../../config/mds-client/INDEX.md) |
| CephFS mirror | [config/cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md) |

Key options: `mds_cache_memory_limit`, `mds_max_file_size`, client mount flags.

```bash
./scripts/lookup-config.sh mds_cache_memory_limit
```

## Common workflows

**Create file system:**

```bash
ceph osd pool create cephfs-metadata 32 32
ceph osd pool create cephfs-data 128 128
ceph fs new myfs cephfs-metadata cephfs-data
ceph orch apply mds myfs --placement="2"
```

**Subvolume:**

```bash
ceph fs subvolume create myfs vol1 --size 10737418240
ceph fs subvolume info myfs vol1
```

**Enable snapshot mirroring:**

```bash
ceph fs snapshot mirror enable myfs
```

## Scale notes

- [Lab](../scales/lab.md) — 1 MDS, small cache
- [Small production](../scales/small-production.md) — 2 active MDS for HA
- [Multisite](../scales/multisite.md) — cephfs-mirror

[← Guides overview](../OVERVIEW.md)
