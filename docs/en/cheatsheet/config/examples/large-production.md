# Large production example

**12+ nodes**, many OSDs, strict SLAs, performance tuning.

## Focus areas

```ini
[global]
osd_pool_default_pg_autoscale_mode = on

public_network = 10.10.0.0/16
cluster_network = 10.20.0.0/16

# Full/nearfull — tune to operational policy
mon_osd_full_ratio = 0.95
mon_osd_nearfull_ratio = 0.85
```

## OSD scheduling (mClock)

```ini
[osd]
osd_op_queue = mclock_scheduler
osd_mclock_profile = balanced
osd_mclock_max_capacity_iops_hdd = 315
osd_mclock_max_capacity_iops_ssd = 20000
```

Use device classes in CRUSH for NVMe vs HDD pools.

## Recovery throttling (business hours)

```ini
[osd]
osd_max_backfills = 1
osd_recovery_max_active = 3
osd_recovery_sleep = 0.1
osd_max_scrubs = 1
```

## Scrub windows

```ini
[osd]
osd_scrub_begin_hour = 2
osd_scrub_end_hour = 6
osd_deep_scrub_interval = 604800
```

## RGW at scale

Deploy many stateless `radosgw` instances behind a load balancer. Enable ops log and Prometheus export. See [RGW optimized example](rgw-optimized.md) and [Large production guide](../../guides/scales/large-production.md).

## Rationale

| Option | Risk if wrong |
|--------|----------------|
| `osd_mclock_profile` | Client latency vs recovery speed trade-off |
| Low `osd_max_backfills` | Slower rebuild after disk failure |
| Network misconfiguration | Recovery saturates public network |

[← Examples overview](OVERVIEW.md)
