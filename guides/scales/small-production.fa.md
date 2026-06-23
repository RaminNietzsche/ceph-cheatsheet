# محیط عملیاتی کوچک

<span class="badge badge-scale-small">محیط عملیاتی کوچک</span> معمولاً **۳–۱۲ نود**، یک مرکز داده، replica **3**، مدیریت با cephadm.

## چک‌لیست معماری

- [ ] ۳ monitor روی hostهای جدا
- [ ] ۲ manager (active + standby)
- [ ] OSD: یک OSD به ازای هر دیسک؛ در صورت امکان شبکه mon/osd جدا
- [ ] PG autoscale **روشن** برای همه poolها
- [ ] برچسب `application` روی pool (rbd، rgw، cephfs)

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

راهنمای عمیق: [OSD](../osd-config/OVERVIEW.md) · [MON](../mon-config/OVERVIEW.md) · [MGR](../mgr-config/TUNING.md)

## ظرفیت

```bash
ceph df detail
ceph osd df tree
```

حدود **۷۰٪** قابل استفاده قبل از `nearfull`؛ فضای headroom برای backfill هنگام تعویض OSD بگذارید.

## ارتقا

ارتقای rolling با cephadm — [cli/cephadm.md](../../cli/cephadm.md)

[← نمای کلی راهنما](../OVERVIEW.md)

## RGW در محیط عملیاتی کوچک

از [معماری استقرار](../../../arch/rgw/architecture/deployment-architecture.md):

- [ ] حداقل ۲ نمونه `radosgw` پشت load balancer
- [ ] `rgw_frontends` (Beast) + TLS عمومی یا termination در LB
- [ ] `rgw_enable_apis` محدود به APIهای لازم
- [ ] یک zone؛ realm/zonegroup اگر multisite بعداً برنامه‌ریزی شده
- [ ] ops log و export متریک mgr

```bash
ceph orch apply rgw prod --placement="2 host1 host2" --port=8080
ceph config set client.rgw rgw_enable_apis "s3"
```
