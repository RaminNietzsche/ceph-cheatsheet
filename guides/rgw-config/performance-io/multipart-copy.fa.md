# Multipart & copy

deep dive پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_copy_obj_progress](#rgw_copy_obj_progress) | `True` | Advanced | Policy |
| [rgw_copy_obj_progress_every_bytes](#rgw_copy_obj_progress_every_bytes) | `1_M` | Advanced | Performance |
| [rgw_multipart_min_part_size](#rgw_multipart_min_part_size) | `5_M` | Advanced | Performance |
| [rgw_multipart_part_upload_limit](#rgw_multipart_part_upload_limit) | `10000` | Advanced | Policy |

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

### rgw_copy_obj_progress

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_copy_obj_progress](../../../config/rgw/rgw.md#SP_rgw_copy_obj_progress) |

**کارکرد:** Send progress report through copy operation

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_copy_obj_progress false
ceph config get client.rgw rgw_copy_obj_progress
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_copy_obj_progress_every_bytes

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_copy_obj_progress_every_bytes](../../../config/rgw/rgw.md#SP_rgw_copy_obj_progress_every_bytes) |

**کارکرد:** Send copy-object progress info after these many bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_copy_obj_progress_every_bytes 1_M
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_min_part_size

| | |
|---|---|
| نوع | Size · default `5_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_multipart_min_part_size](../../../config/rgw/rgw.md#SP_rgw_multipart_min_part_size) |

**کارکرد:** Minimum S3 multipart-upload part size

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_multipart_min_part_size 5_M
ceph config get client.rgw rgw_multipart_min_part_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_multipart_min_part_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_part_upload_limit

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [rgw.md#SP_rgw_multipart_part_upload_limit](../../../config/rgw/rgw.md#SP_rgw_multipart_part_upload_limit) |

**کارکرد:** Max number of parts in multipart upload

**زمان استفاده:** وقتی کلاینت‌ها به محدودیت اندازه/concurrency می‌رسند یا برای محافظت از منابع کلاستر.

**مثال:**

```bash
ceph config set client.rgw rgw_multipart_part_upload_limit 10000
ceph config get client.rgw rgw_multipart_part_upload_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`10000`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
