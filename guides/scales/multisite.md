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
radosgw-admin sync status
radosgw-admin period update --commit
ceph config get client.rgw rgw_zone
```

CLI: [cli/rgw.md](../../cli/rgw.md)  
Config: [config/rgw/INDEX.md](../../config/rgw/INDEX.md)  
Deep dives: [multisite-zones.md](../rgw-config/multisite/multisite-zones.md) · [multisite-sync.md](../rgw-config/multisite/multisite-sync.md)

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

| Role | Guide |
|------|-------|
| RGW multisite | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS DR | [cephfs-admin.md](../roles/cephfs-admin.md) |
| Cluster / mon | [cluster-admin.md](../roles/cluster-admin.md) |

## Caveats

- Latency between sites affects RGW sync and RBD journal lag
- Test failover (`promote`) in maintenance windows
- Plan CRUSH and pools per site for erasure + multisite

[← Guides overview](../OVERVIEW.md)

## RGW multisite model (docs-extended)

From [deployment architecture](../../../arch/rgw/architecture/deployment-architecture.md) and [runtime topology](../../../arch/rgw/architecture/runtime-topology.md):

| Object | Role |
|--------|------|
| **Realm** | Configuration namespace |
| **Period** | Epoch version of config |
| **Zone** | Geographic site with local pools |
| **Sync** | Metadata log + data sync over HTTP between zones (`RGWRESTConn`) |

Each zone runs its own RGW fleet; instances are stateless — coordination via RADOS and multisite, not shared memory.

Module deep dive: [Multisite module](../../../arch/rgw/modules/multisite.md) · Learning path: [Phase 7 — Multisite](../../../arch/rgw/learning-program/08-phase-7-multisite.md)
