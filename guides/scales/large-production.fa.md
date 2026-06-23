# مقیاس Large Production

<span class="badge badge-scale-large">Large production</span> **۱۲+ نود**، OSD زیاد، SLA سخت، شبکه جدا، تنظیم performance.

## حوزه‌های تمرکز

| حوزه | اقدام |
|------|--------|
| زمان‌بندی | `osd_mclock_profile`، device class |
| PG | autoscale + `mon_target_pg_per_osd` |
| Scrub | `osd_max_scrubs`، پنجره deep-scrub |
| شبکه | public / cluster — [public.md](../../config/global/public.md) |
| CRUSH | rule هر rack / DC |

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
./scripts/lookup-config.sh osd_mclock_profile
./scripts/lookup-config.sh osd_max_scrubs
```

Deep dive: [OSD](../osd-config/OVERVIEW.md) · [recovery](../osd-config/recovery/recovery.md)

## محدود کردن recovery

```bash
ceph config set osd osd_max_backfills 1
ceph config set osd osd_recovery_max_active 3
```

[← نمای کلی راهنما](../OVERVIEW.md)
