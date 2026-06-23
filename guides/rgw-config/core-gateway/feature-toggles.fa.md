# Feature toggles

راهنمای عمیق پیکربندی RGW — 10 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_disable_s3select](#rgw_disable_s3select) | `False` | Advanced | Policy |
| [rgw_enable_apis](#rgw_enable_apis) | `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` | Advanced | Performance |
| [rgw_enable_gc_threads](#rgw_enable_gc_threads) | `True` | Advanced | Policy |
| [rgw_enable_jwks_url_verification](#rgw_enable_jwks_url_verification) | `False` | Advanced | Policy |
| [rgw_enable_lc_threads](#rgw_enable_lc_threads) | `True` | Advanced | Policy |
| [rgw_enable_mdsearch](#rgw_enable_mdsearch) | `True` | Basic | Policy |
| [rgw_enable_ops_log](#rgw_enable_ops_log) | `False` | Advanced | Policy |
| [rgw_enable_restore_threads](#rgw_enable_restore_threads) | `True` | Advanced | Policy |
| [rgw_enable_static_website](#rgw_enable_static_website) | `False` | Basic | Policy |
| [rgw_enable_usage_log](#rgw_enable_usage_log) | `False` | Advanced | Policy |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Architecture** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_disable_s3select

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_disable_s3select](../../../config/rgw/rgw.md#SP_rgw_disable_s3select) |

**کارکرد:** disable the s3select operation; RGW will report an error and will return ERR_INVALID_REQUEST.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_disable_s3select true
ceph config get client.rgw rgw_disable_s3select
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_apis

| | |
|---|---|
| نوع | Str · default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_apis](../../../config/rgw/rgw.md#SP_rgw_enable_apis) |

**کارکرد:** A list of RESTful APIs for RGW to enable

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_apis "s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications"
ceph config get client.rgw rgw_enable_apis
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_enable_apis
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_enable_gc_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_gc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_gc_threads) |

**کارکرد:** Enables the garbage collection maintenance thread.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_gc_threads false
ceph config get client.rgw rgw_enable_gc_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_jwks_url_verification

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_jwks_url_verification](../../../config/rgw/rgw.md#SP_rgw_enable_jwks_url_verification) |

**کارکرد:** Enable JWKS url verification for AWS compliance

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_jwks_url_verification true
ceph config get client.rgw rgw_enable_jwks_url_verification
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_lc_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_lc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_lc_threads) |

**کارکرد:** Enables the lifecycle maintenance thread. This is required on at least one RGW daemon for each zone.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_lc_threads false
ceph config get client.rgw rgw_enable_lc_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_mdsearch

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [rgw.md#SP_rgw_enable_mdsearch](../../../config/rgw/rgw.md#SP_rgw_enable_mdsearch) |

**کارکرد:** Enable elastic metadata search APIs

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_mdsearch false
ceph config get client.rgw rgw_enable_mdsearch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_ops_log

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_ops_log](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log) |

**کارکرد:** Enable ops log

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_ops_log true
ceph config get client.rgw rgw_enable_ops_log
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_restore_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_restore_threads](../../../config/rgw/rgw.md#SP_rgw_enable_restore_threads) |

**کارکرد:** Enables the objects' restore maintenance thread.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_restore_threads false
ceph config get client.rgw rgw_enable_restore_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_static_website

| | |
|---|---|
| نوع | Bool · default `False` · **Basic** |
| جدول | [rgw.md#SP_rgw_enable_static_website](../../../config/rgw/rgw.md#SP_rgw_enable_static_website) |

**کارکرد:** Enable static website APIs

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_static_website true
ceph config get client.rgw rgw_enable_static_website
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_usage_log

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enable_usage_log](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log) |

**کارکرد:** Enable the usage log

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enable_usage_log true
ceph config get client.rgw rgw_enable_usage_log
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
