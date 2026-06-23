# Small Production Scale

<span class="badge badge-scale-small">Small production</span> Typically **3–12 nodes**, one datacenter, replica **3**, cephadm-managed.

## Architecture checklist

- [ ] 3 monitors on separate hosts
- [ ] 2 manager daemons (active + standby)
- [ ] OSDs: one per disk; separate mon/osd networks if possible
- [ ] PG autoscale **on** for all pools
- [ ] Pool `application` tag set (rbd, rgw, cephfs)

## Daily operations

Follow [quickstart.md](../quickstart.md) and role guides:

| Role | Guide |
|------|-------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| OSD / pools | [storage-operator.md](../roles/storage-operator.md) |
| RGW | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS | [cephfs-admin.md](../roles/cephfs-admin.md) |

## Key config to verify

```bash
ceph config get mon osd_pool_default_pg_autoscale_mode
ceph config get mgr mon_target_pg_per_osd
ceph osd pool autoscale-status
```

Deep dives: [OSD](../osd-config/OVERVIEW.md) · [MON](../mon-config/OVERVIEW.md) · [MGR](../mgr-config/TUNING.md)

## Capacity planning

```bash
ceph df detail
ceph osd df tree
```

Plan for **~70% usable** before `nearfull`; leave headroom for backfill during OSD replacement.

## Upgrades

Rolling upgrade via cephadm — [cli/cephadm.md](../../cli/cephadm.md)

[← Guides overview](../OVERVIEW.md)
