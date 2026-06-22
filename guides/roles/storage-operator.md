# Storage Operator

Manage OSDs, pools, placement groups, CRUSH, recovery, and scrub.

## Daily commands

```bash
ceph osd stat
ceph osd tree
ceph osd df tree
ceph pg stat
ceph pg dump_stuck
ceph df detail
```

See [OSD & pools CLI](../../cli/osd-pool.md) and [RADOS CLI](../../cli/rados.md).

## Configuration

| Area | Config index |
|------|--------------|
| OSD daemon | [config/osd/INDEX.md](../../config/osd/INDEX.md) |
| Global OSD / bluestore | [config/global/osd.md](../../config/global/osd.md), [bluestore.md](../../config/global/bluestore.md) |
| PG autoscale | `osd_pool_default_pg_autoscale_mode`, `mon_target_pg_per_osd` |
| Recovery / scrub | `osd_max_scrubs`, `osd_recovery_*`, `osd_deep_scrub_*` |

Look up any option:

```bash
./scripts/lookup-config.sh osd_max_scrubs
```

## Common workflows

**OSD maintenance:**

```bash
ceph osd safe-to-destroy 5
ceph osd out 5
# stop osd, replace disk, redeploy
ceph osd in 5
```

**Create replicated pool:**

```bash
ceph osd pool create mypool 128 128 replicated
ceph osd pool application enable mypool rbd
ceph osd pool autoscale-status
```

**Rebalance:**

```bash
ceph osd reweight-by-utilization
ceph osd crush reweight osd.5 0.95
```

## Scale notes

- [Small production](../scales/small-production.md) — autoscale on, 3x replication
- [Large production](../scales/large-production.md) — mclock profiles, device classes
- [Lab](../scales/lab.md) — lower osd memory, fewer PGs

## Troubleshooting

Degraded PGs, backfill throttling, nearfull — [cli/troubleshooting.md](../../cli/troubleshooting.md)

[← Guides overview](../OVERVIEW.md)
