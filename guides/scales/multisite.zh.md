> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

# Multisite Scale

<span class="badge badge-scale-multi">Multisite</span> Multiple datacenters or regions — RGW zones, optional RBD / CephFS mirroring.

## Patterns

| Use case | Components |
|----------|------------|
| S3 geo-distribution | RGW realm → zonegroup → zones, `period update` |
| Block DR | RBD mirroring (pool or image mode) |
| CephFS DR | cephfs-mirror snapshot sync |

## RGW multisite

```bash
radosgw-admin realm list
radosgw-admin zone list
radosgw-admin period update --commit
radosgw-admin sync status
```

CLI: [cli/rgw.md](../../cli/rgw.md)  
Config: [config/rgw/INDEX.md](../../config/rgw/INDEX.md) — search `rgw_zone`, `rgw_data_log`

```bash
./scripts/search-config.sh -s rgw zone
```

## RBD mirror

```bash
rbd mirror pool enable rbd image
rbd mirror pool status rbd
rbd mirror image promote rbd/image --force
```

Config: [config/rbd-mirror/INDEX.md](../../config/rbd-mirror/INDEX.md)

## CephFS mirror

```bash
ceph fs snapshot mirror enable myfs
ceph fs snapshot mirror info myfs
```

Config: [config/cephfs-mirror/INDEX.md](../../config/cephfs-mirror/INDEX.md)

## Role guides

[RGW admin](../roles/rgw-admin.md) · [CephFS admin](../roles/cephfs-admin.md)

## Caveats

- Latency between sites affects RGW metadata sync and RBD journal lag
- Test failover (`promote`) in maintenance windows
- Separate pools per site for erasure + multisite requires careful planning

[← Guides overview](../OVERVIEW.md)
