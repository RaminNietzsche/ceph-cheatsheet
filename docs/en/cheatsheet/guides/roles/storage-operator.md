# Storage Operator

<span class="badge badge-role-storage">Storage operator</span> Manage OSDs, pools, placement groups, CRUSH, recovery, and scrub.

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
| OSD daemon | [config/osd/INDEX.md](../../config/osd/INDEX.md) · [OSD deep dive](../osd-config/OVERVIEW.md) |
| Global / bluestore | [config/global/osd.md](../../config/global/osd.md), [bluestore.md](../../config/global/bluestore.md) |
| Recovery & scrub | [osd-config/recovery](../osd-config/recovery/recovery.md), [scrub](../osd-config/scrub/scrub.md) |
| mClock | [osd-config/mclock](../osd-config/mclock/mclock.md) — `osd_mclock_profile` |

Look up any option:

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd recovery
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

| Scale | Focus |
|-------|--------|
| [Lab](../scales/lab.md) | Lower `osd_memory_target`, fewer PGs |
| [Small production](../scales/small-production.md) | Autoscale on, replica 3 |
| [Large production](../scales/large-production.md) | mClock, device classes, scrub windows |
| [Multisite](../scales/multisite.md) | CRUSH per site; pool layout for DR |

## Troubleshooting

Degraded PGs, backfill throttling, nearfull — [cli/troubleshooting.md](../../cli/troubleshooting.md)

[← Guides overview](../OVERVIEW.md)
