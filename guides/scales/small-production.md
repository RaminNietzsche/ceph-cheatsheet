# Small Production Scale

Typically **3–12 nodes**, one datacenter, replica **3**, cephadm-managed.

## Architecture checklist

- [ ] 3 monitors on separate hosts
- [ ] 2 manager daemons (active + standby)
- [ ] OSDs: 1 per disk, separate mon/osd networks if possible
- [ ] PG autoscale **on** for all pools
- [ ] Pool `application` tag set (rbd, rgw, cephfs)

## Daily operations

Follow [quickstart.md](../quickstart.md) and role-specific guides:

| Role | Guide |
|------|-------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| OSD/pools | [storage-operator.md](../roles/storage-operator.md) |

## Key config defaults to verify

```bash
ceph config get mon osd_pool_default_pg_autoscale_mode
ceph config get mgr mon_target_pg_per_osd
ceph osd pool autoscale-status
```

Common options:

- `mon_target_pg_per_osd` — [config/mgr/mon.md](../../config/mgr/mon.md)
- `osd_pool_default_pg_autoscale_mode` — [config/global/osd.md](../../config/global/osd.md)
- `osd_mclock_profile` — `balanced` or `high_client_ops` for mixed workloads

## Capacity planning

```bash
ceph df detail
ceph osd df tree
```

Plan for **~70% usable** before `nearfull` warnings; leave headroom for backfill during OSD replacement.

## Upgrades

Use cephadm rolling upgrade — [cli/cephadm.md](../../cli/cephadm.md)

[← Guides overview](../OVERVIEW.md)
