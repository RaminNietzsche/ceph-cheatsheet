# محیط عملیاتی بزرگ

<span class="badge badge-scale-large">محیط عملیاتی بزرگ</span> **۱۲+ نود**، OSD زیاد، SLA سخت‌گیرانه، شبکهٔ جدا، تنظیم عملکرد.

## حوزه‌های تمرکز

| حوزه | اقدام |
|------|--------|
| زمان‌بندی | `osd_mclock_profile`، device class (ssd/hdd/nvme) |
| PG | autoscale + `mon_target_pg_per_osd`؛ از OSD داغ پرهیز کنید |
| Scrub | `osd_max_scrubs`، پنجره deep-scrub |
| شبکه | `public_network` / `cluster_network` — [public.md](../../config/global/public.md) |
| failure domain | قوانین CRUSH برای هر rack / مرکز داده |

## دستورات

```bash
ceph osd crush class ls
ceph osd crush tree
ceph osd perf
ceph osd reweight-by-utilization 0.05
ceph osd ok-to-stop osd.0 osd.1 osd.2
```

## پیکربندی

```bash
./scripts/search-config.sh -s osd mclock
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
./scripts/lookup-config.sh mon_osd_full_ratio
```

راهنمای عمیق: [OSD](../osd-config/OVERVIEW.md) · [recovery](../osd-config/recovery/recovery.md) · [scrub](../osd-config/scrub/scrub.md)

## محدود کردن recovery (ساعات کاری)

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

## راهنمای نقش

[storage-operator.md](../roles/storage-operator.md) · [cluster-admin.md](../roles/cluster-admin.md)

[← نمای کلی راهنما](../OVERVIEW.md)

## RGW در محیط عملیاتی بزرگ

چند gateway بدون state در لبه، RADOS مشترک، شبکه public و cluster جدا در صورت امکان.

| موضوع | اقدام |
|-------|--------|
| زمان‌بندی / fairness | [معماری dmclock](../../../arch/rgw/architecture/dmclock-architecture.md) |
| محدودیت کلاینت | [Rate limit](../../../arch/rgw/architecture/rate-limit-architecture.md) |
| رصدپذیری | ops log، `rgw_perf_counters`، health check — [رصدپذیری](../../../arch/rgw/architecture/observability-overview.md) |
| شکاف‌های HA | [محدودیت‌های HA](../../../arch/rgw/architecture/critical-gaps-and-ha-limitations.md) |

پایش: `l_rgw_qlen` پایدار، `ERR_RATE_LIMITED`، lag multisite، شکست GC/reshard.
