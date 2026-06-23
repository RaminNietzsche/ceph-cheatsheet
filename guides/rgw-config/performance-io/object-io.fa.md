# Object read/write windows

deep dive پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_get_obj_max_req_size](#rgw_get_obj_max_req_size) | `4_M` | Advanced | Policy |
| [rgw_get_obj_window_size](#rgw_get_obj_window_size) | `16_M` | Advanced | Performance |
| [rgw_put_obj_max_window_size](#rgw_put_obj_max_window_size) | `64_M` | Advanced | Performance |
| [rgw_put_obj_min_window_size](#rgw_put_obj_min_window_size) | `16_M` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Architecture** | backend، توپولوژی multisite — نه sweep عددی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_get_obj_max_req_size

| | |
|---|---|
| نوع | Size · default `4_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_get_obj_max_req_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_max_req_size) |

**کارکرد:** RGW object read chunk size

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_get_obj_max_req_size 4_M
ceph config get client.rgw rgw_get_obj_max_req_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `4_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_get_obj_window_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_get_obj_window_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_window_size) |

**کارکرد:** RGW object read window size

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_get_obj_window_size 16_M
ceph config get client.rgw rgw_get_obj_window_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_get_obj_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_max_window_size

| | |
|---|---|
| نوع | Size · default `64_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_put_obj_max_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_max_window_size) |

**کارکرد:** The maximum RADOS write window size (in bytes).

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_put_obj_max_window_size 64_M
ceph config get client.rgw rgw_put_obj_max_window_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `64_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_max_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_min_window_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_put_obj_min_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_min_window_size) |

**کارکرد:** The minimum RADOS write window size (in bytes).

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_put_obj_min_window_size 16_M
ceph config get client.rgw rgw_put_obj_min_window_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**سیگنال‌ها:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_min_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
