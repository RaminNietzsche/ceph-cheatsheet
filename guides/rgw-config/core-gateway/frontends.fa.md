# Frontends & HTTP stack

deep dive پیکربندی RGW — 6 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_asio_assert_yielding](#rgw_asio_assert_yielding) | `False` | Dev | Dev |
| [rgw_beast_enable_async](#rgw_beast_enable_async) | `True` | Dev | Policy |
| [rgw_dns_name](#rgw_dns_name) | `(empty)` | Advanced | Performance |
| [rgw_dns_s3website_name](#rgw_dns_s3website_name) | `(empty)` | Advanced | Performance |
| [rgw_frontend_defaults](#rgw_frontend_defaults) | `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` | Advanced | Performance |
| [rgw_frontends](#rgw_frontends) | `beast port=7480` | Basic | Performance |

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

### rgw_asio_assert_yielding

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rgw.md#SP_rgw_asio_assert_yielding](../../../config/rgw/rgw.md#SP_rgw_asio_assert_yielding) |

**کارکرد:** Triggers an assertion if code on an asio/beast thread would block instead of yielding to coroutines. Development aid for finding blocking calls.

**زمان استفاده:** RGW development/debugging only — keep `false` in production.

**گزینه‌های مرتبط:**

- `rgw_beast_enable_async`

**مثال:**

```bash
ceph config set client.rgw rgw_asio_assert_yielding true
ceph config get client.rgw rgw_asio_assert_yielding
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**سیگنال‌ها:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_beast_enable_async

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [rgw.md#SP_rgw_beast_enable_async](../../../config/rgw/rgw.md#SP_rgw_beast_enable_async) |

**کارکرد:** When `true`, the Beast HTTP frontend processes requests with **coroutines**, allowing multiple concurrent requests per thread.

**زمان استفاده:** Leave `true` for production throughput. Set `false` only when debugging request flow.

**مثال:**

```bash
ceph config set client.rgw rgw_beast_enable_async false
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dns_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dns_name](../../../config/rgw/rgw.md#SP_rgw_dns_name) |

**کارکرد:** The host names that RGW uses.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_dns_name "s3.example.com"
ceph config get client.rgw rgw_dns_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dns_s3website_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dns_s3website_name](../../../config/rgw/rgw.md#SP_rgw_dns_s3website_name) |

**کارکرد:** The host name that RGW uses for static websites (S3)

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_dns_s3website_name "website.s3.example.com"
ceph config get client.rgw rgw_dns_s3website_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_s3website_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_frontend_defaults

| | |
|---|---|
| نوع | Str · default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` · **Advanced** |
| جدول | [rgw.md#SP_rgw_frontend_defaults](../../../config/rgw/rgw.md#SP_rgw_frontend_defaults) |

**کارکرد:** RGW frontends default configuration

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_frontend_defaults "beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key"
ceph config get client.rgw rgw_frontend_defaults
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontend_defaults
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_frontends

| | |
|---|---|
| نوع | Str · default `beast port=7480` · **Basic** |
| جدول | [rgw.md#SP_rgw_frontends](../../../config/rgw/rgw.md#SP_rgw_frontends) |

**کارکرد:** RGW frontends configuration

**زمان استفاده:** رفتار اصلی RGW — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_frontends "beast port=7480"
ceph config get client.rgw rgw_frontends
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `beast port=7480`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontends
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
