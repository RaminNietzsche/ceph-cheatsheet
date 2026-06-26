# Access & object logging

راهنمای عمیق پیکربندی RGW — 4 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_log_http_headers](#rgw_log_http_headers) | `(empty)` | Basic | عملکرد |
| [rgw_log_nonexistent_bucket](#rgw_log_nonexistent_bucket) | `False` | Advanced | سیاست |
| [rgw_log_object_name](#rgw_log_object_name) | `%Y-%m-%d-%H-%i-%n` | Advanced | عملکرد |
| [rgw_log_object_name_utc](#rgw_log_object_name_utc) | `False` | Advanced | سیاست |

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

### rgw_log_http_headers

| | |
|---|---|
| نوع | Str · default `(empty)` · **Basic** |
| جدول | [rgw.md#SP_rgw_log_http_headers](../../../config/rgw/rgw.md#SP_rgw_log_http_headers) |

**کارکرد:** List of HTTP headers to log A comma delimited list of HTTP headers to log when seen, ignores case (e.g., http_x_forwarded_for).

**زمان استفاده:** رفتار اصلی RGW — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_log_http_headers <value>
ceph config get client.rgw rgw_log_http_headers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_http_headers
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_log_nonexistent_bucket

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_log_nonexistent_bucket](../../../config/rgw/rgw.md#SP_rgw_log_nonexistent_bucket) |

**کارکرد:** Should RGW log operations on bucket that does not exist This config option applies to the ops log. When this option is set, the ops log will log operations that are sent to non existing buckets. These operations inherently fail, and do not correspond to a specific user.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`rgw_enable_ops_log`](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log)

**مثال:**

```bash
ceph config set client.rgw rgw_log_nonexistent_bucket true
ceph config get client.rgw rgw_log_nonexistent_bucket
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_log_object_name

| | |
|---|---|
| نوع | Str · default `%Y-%m-%d-%H-%i-%n` · **Advanced** |
| جدول | [rgw.md#SP_rgw_log_object_name](../../../config/rgw/rgw.md#SP_rgw_log_object_name) |

**کارکرد:** Ops log object name format Defines the format of the RADOS objects names that ops log uses to store ops log data

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`rgw_enable_ops_log`](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log)

**مثال:**

```bash
ceph config set client.rgw rgw_log_object_name "%Y-%m-%d-%H-%i-%n"
ceph config get client.rgw rgw_log_object_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `%Y-%m-%d-%H-%i-%n`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_object_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_log_object_name_utc

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_log_object_name_utc](../../../config/rgw/rgw.md#SP_rgw_log_object_name_utc) |

**کارکرد:** Should ops log object name based on UTC If set, the names of the RADOS objects that hold the ops log data will be based on UTC time zone. If not set, it will use the local time zone.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_log_object_name_utc true
ceph config get client.rgw rgw_log_object_name_utc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
