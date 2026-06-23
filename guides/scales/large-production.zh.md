> **说明：** 下表中的选项说明来自 upstream Ceph（英文）。

# Large Production Scale

<span class="badge badge-scale-large">Large production</span> **12+ nodes**, many OSDs, strict SLAs, separate networks, performance tuning.

## Focus areas

| Area | Actions |
|------|---------|
| Scheduling | `osd_mclock_profile`, device classes (ssd/hdd/nvme) |
| PG balance | Autoscale + monitor `mon_target_pg_per_osd`, avoid hot OSDs |
| Scrub | Tune `osd_max_scrubs`, deep-scrub windows, no overlap with peak I/O |
| Networks | `public_network` / `cluster_network` — [config/global/public.md](../../config/global/public.md) |
| Failure domains | CRUSH rules per rack/datacenter |

## Commands

```bash
ceph osd crush class ls
ceph osd crush tree
ceph osd perf
ceph pg dump | awk '/active/ {print $1}' | sort | uniq -c
ceph osd reweight-by-utilization 0.05
```

## Config to review

```bash
./scripts/search-config.sh -s osd mclock
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
./scripts/lookup-config.sh mon_osd_full_ratio
```

Indexes: [config/osd/INDEX.md](../../config/osd/INDEX.md), [config/global/bluestore.md](../../config/global/bluestore.md)

## OSD maintenance at scale

Always use safety checks before bulk operations:

```bash
ceph osd ok-to-stop osd.0 osd.1 osd.2
ceph osd safe-to-destroy 12
```

Throttle recovery during business hours:

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

## Role guides

[storage-operator.md](../roles/storage-operator.md) · [cluster-admin.md](../roles/cluster-admin.md)

[← Guides overview](../OVERVIEW.md)
