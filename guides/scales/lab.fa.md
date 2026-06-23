# مقیاس آزمایشگاه / توسعه

<span class="badge badge-scale-lab">آزمایشگاه / توسعه</span> ۱–۳ نود، تست، یادگیری و CI — **نه برای دادهٔ عملیاتی**.

## اهداف

- حداقل منابع، تکرار سریع
- پذیرش single point of failure
- durability شل‌تر فقط در شبکه lab ایزوله

## چیدمان پیشنهادی

```bash
cephadm bootstrap --mon-ip <ip> --single-host-defaults
ceph orch apply mon --placement="1"
ceph orch apply mgr --placement="1"
ceph orch apply osd --all-available-devices
```

## تنظیم

| حوزه | رویکرد lab |
|------|------------|
| Replication | `size=2` با `--single-host-defaults` روی یک host |
| PG | autoscale روشن؛ pool کوچک |
| حافظه OSD | `osd_memory_target` پایین‌تر اگر RAM محدود است |
| Scrub | interval بلندتر برای کاهش فشار دیسک |

```bash
./scripts/lookup-config.sh osd_memory_target
./scripts/lookup-config.sh osd_pool_default_pg_autoscale_mode
```

## راهنمای نقش

| نقش | راهنما |
|------|--------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| Storage | [storage-operator.md](../roles/storage-operator.md) |
| RGW (اختیاری) | [rgw-admin.md](../roles/rgw-admin.md) |
| CephFS (اختیاری) | [cephfs-admin.md](../roles/cephfs-admin.md) |

## مرجع سریع CLI

[cli/cluster.md](../../cli/cluster.md) · [cli/osd-pool.md](../../cli/osd-pool.md)

[← نمای کلی راهنما](../OVERVIEW.md)
