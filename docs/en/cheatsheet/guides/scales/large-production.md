# Large Production Scale

<span class="badge badge-scale-large">Large production</span> **12+ nodes**, many OSDs, strict SLAs, separate networks, performance tuning.

## Focus areas

| Area | Actions |
|------|---------|
| Scheduling | `osd_mclock_profile`, device classes (ssd/hdd/nvme) |
| PG balance | Autoscale + `mon_target_pg_per_osd`; avoid hot OSDs |
| Scrub | `osd_max_scrubs`, deep-scrub windows |
| Networks | `public_network` / `cluster_network` — [global/public.md](../../config/global/public.md) |
| Failure domains | CRUSH rules per rack / datacenter |

## Commands

```bash
ceph osd crush class ls
ceph osd crush tree
ceph osd perf
ceph osd reweight-by-utilization 0.05
ceph osd ok-to-stop osd.0 osd.1 osd.2
```

## Config to review

```bash
./scripts/search-config.sh -s osd mclock
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
./scripts/lookup-config.sh mon_osd_full_ratio
```

Deep dives: [OSD](../osd-config/OVERVIEW.md) · [recovery](../osd-config/recovery/recovery.md) · [scrub](../osd-config/scrub/scrub.md)

## Throttle recovery (business hours)

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

## Role guides

[storage-operator.md](../roles/storage-operator.md) · [cluster-admin.md](../roles/cluster-admin.md)

[← Guides overview](../OVERVIEW.md)

## RGW at large production scale

Multiple stateless gateways, shared RADOS, separate public vs cluster networks when possible.

| Concern | Action |
|---------|--------|
| Scheduling / fairness | [dmclock architecture](../../../arch/rgw/architecture/dmclock-architecture.md) |
| Client throttling | [Rate limits](../../../arch/rgw/architecture/rate-limit-architecture.md) |
| Observability | ops log, `rgw_perf_counters`, health check — [observability](../../../arch/rgw/architecture/observability-overview.md) |
| HA gaps | [Critical gaps & HA limitations](../../../arch/rgw/architecture/critical-gaps-and-ha-limitations.md) |

Watch: sustained `l_rgw_qlen`, high `ERR_RATE_LIMITED`, multisite sync lag, GC/reshard failures in driver logs.
