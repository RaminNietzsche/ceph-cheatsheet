# مسئول ذخیره‌سازی

<span class="badge badge-role-storage">مسئول ذخیره‌سازی</span> — مدیریت OSD، pool، PG، CRUSH، recovery و scrub.

## دستورات روزانه

```bash
ceph osd stat
ceph osd tree
ceph osd df tree
ceph pg stat
ceph pg dump_stuck
ceph df detail
```

[CLI OSD و pool](../../cli/osd-pool.md) · [CLI RADOS](../../cli/rados.md)

## پیکربندی

| حوزه | فهرست پیکربندی |
|------|-------|
| دیمن OSD | [config/osd/INDEX.md](../../config/osd/INDEX.md) · [راهنمای عمیق OSD](../osd-config/OVERVIEW.md) |
| Global / bluestore | [osd.md](../../config/global/osd.md)، [bluestore.md](../../config/global/bluestore.md) |
| بازیابی و scrub | [recovery](../osd-config/recovery/recovery.md)، [scrub](../osd-config/scrub/scrub.md) |
| mClock | [mclock](../osd-config/mclock/mclock.md) — `osd_mclock_profile` |

جستجوی هر گزینه:

```bash
./scripts/lookup-config.sh osd_max_scrubs
./scripts/search-config.sh -s osd recovery
```

## روندهای کاری رایج

**نگهداری OSD:**

```bash
ceph osd safe-to-destroy 5
ceph osd out 5
ceph osd in 5
```

**ایجاد pool:**

```bash
ceph osd pool create mypool 128 128 replicated
ceph osd pool application enable mypool rbd
ceph osd pool autoscale-status
```

**تعادل مجدد (rebalance):**

```bash
ceph osd reweight-by-utilization
ceph osd crush reweight osd.5 0.95
```

## یادداشت مقیاس

| مقیاس | تمرکز |
|-------|--------|
| [آزمایشگاه](../scales/lab.md) | `osd_memory_target` پایین‌تر، PG کمتر |
| [محیط عملیاتی کوچک](../scales/small-production.md) | autoscale روشن، replica 3 |
| [محیط عملیاتی بزرگ](../scales/large-production.md) | mClock، device class، پنجره scrub |
| [چندسایته](../scales/multisite.md) | CRUSH هر سایت؛ چیدمان pool برای DR |

## عیب‌یابی

PGهای degraded، محدودسازی backfill، nearfull — [cli/troubleshooting.md](../../cli/troubleshooting.md)

[← نمای کلی راهنما](../OVERVIEW.md)
