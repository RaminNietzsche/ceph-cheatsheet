# مقیاس Small Production

<span class="badge badge-scale-small">محیط عملیاتی کوچک</span> معمولاً **۳–۱۲ نود**، یک مرکز داده، replica **3**، cephadm.

## چک‌لیست معماری

- [ ] ۳ monitor روی host جدا
- [ ] ۲ manager (active + standby)
- [ ] یک OSD به ازای هر دیسک
- [ ] PG autoscale **روشن**
- [ ] برچسب `application` روی pool

## عملیات روزانه

[quickstart.md](../quickstart.md) و راهنمای نقش:

| نقش | راهنما |
|------|--------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| Storage | [storage-operator.md](../roles/storage-operator.md) |
| RGW | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS | [cephfs-admin.md](../roles/cephfs-admin.md) |

## پیکربندی کلیدی

```bash
ceph config get mon osd_pool_default_pg_autoscale_mode
ceph config get mgr mon_target_pg_per_osd
ceph osd pool autoscale-status
```

Deep dive: [OSD](../osd-config/OVERVIEW.md) · [MON](../mon-config/OVERVIEW.md)

## ظرفیت

```bash
ceph df detail
ceph osd df tree
```

حدود **۷۰٪** قابل استفاده قبل از `nearfull`.

[← نمای کلی راهنما](../OVERVIEW.md)
