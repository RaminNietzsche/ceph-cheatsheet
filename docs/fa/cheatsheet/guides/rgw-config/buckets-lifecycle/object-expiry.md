# Object expiry hints

راهنمای عمیق پیکربندی RGW — 2 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_objexp_chunk_size](#rgw_objexp_chunk_size) | `100` | Dev | عملکرد |
| [rgw_objexp_hints_num_shards](#rgw_objexp_hints_num_shards) | `127` | Advanced | سیاست |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری API، محدودیت tenant |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه pool |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **معماری** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_objexp_chunk_size

| | |
|---|---|
| نوع | Uint · default `100` · **Dev** |
| جدول | [rgw.md#SP_rgw_objexp_chunk_size](../../../config/rgw/rgw.md#SP_rgw_objexp_chunk_size) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_objexp_chunk_size 100
ceph config get client.rgw rgw_objexp_chunk_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `100` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_objexp_chunk_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_hints_num_shards

| | |
|---|---|
| نوع | Uint · default `127` · **Advanced** |
| جدول | [rgw.md#SP_rgw_objexp_hints_num_shards](../../../config/rgw/rgw.md#SP_rgw_objexp_hints_num_shards) |

**کارکرد:** Number of object expirer data shards The number of shards the (Swift) object expirer will store its data on.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_objexp_hints_num_shards 127
ceph config get client.rgw rgw_objexp_hints_num_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `127` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
