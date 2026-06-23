# مقیاس Lab / توسعه

<span class="badge badge-scale-lab">آزمایشگاه / توسعه</span> ۱–۳ نود، تست و یادگیری — **نه برای دادهٔ عملیاتی**.

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
| Replication | `size=2` با `--single-host-defaults` |
| PG | autoscale؛ pool کوچک |
| حافظه OSD | `osd_memory_target` پایین‌تر |
| Scrub | interval بلندتر |

```bash
./scripts/lookup-config.sh osd_memory_target
```

## راهنمای نقش

| نقش | راهنما |
|------|--------|
| Cluster | [cluster-admin.md](../roles/cluster-admin.md) |
| Storage | [storage-operator.md](../roles/storage-operator.md) |

[← نمای کلی راهنما](../OVERVIEW.md)
