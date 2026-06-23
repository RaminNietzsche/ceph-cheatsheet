# Swift API

deep dive پیکربندی RGW — 11 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_swift_account_in_url](#rgw_swift_account_in_url) | `False` | Advanced | Connectivity |
| [rgw_swift_auth_entry](#rgw_swift_auth_entry) | `auth` | Advanced | Policy |
| [rgw_swift_auth_url](#rgw_swift_auth_url) | `(empty)` | Advanced | Connectivity |
| [rgw_swift_custom_header](#rgw_swift_custom_header) | `(empty)` | Advanced | Performance |
| [rgw_swift_enforce_content_length](#rgw_swift_enforce_content_length) | `False` | Advanced | Policy |
| [rgw_swift_need_stats](#rgw_swift_need_stats) | `True` | Advanced | Policy |
| [rgw_swift_tenant_name](#rgw_swift_tenant_name) | `(empty)` | Advanced | Performance |
| [rgw_swift_token_expiration](#rgw_swift_token_expiration) | `1_day` | Advanced | Performance |
| [rgw_swift_url](#rgw_swift_url) | `(empty)` | Advanced | Connectivity |
| [rgw_swift_url_prefix](#rgw_swift_url_prefix) | `swift` | Advanced | Performance |
| [rgw_swift_versioning_enabled](#rgw_swift_versioning_enabled) | `False` | Advanced | Policy |

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

### rgw_swift_account_in_url

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_account_in_url](../../../config/rgw/rgw.md#SP_rgw_swift_account_in_url) |

**کارکرد:** Swift account encoded in URL

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_account_in_url true
ceph config get client.rgw rgw_swift_account_in_url
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`False`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_account_in_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_auth_entry

| | |
|---|---|
| نوع | Str · default `auth` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_auth_entry](../../../config/rgw/rgw.md#SP_rgw_swift_auth_entry) |

**کارکرد:** Swift auth URL prefix

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_auth_entry auth
ceph config get client.rgw rgw_swift_auth_entry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Upstream default (`auth`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_swift_auth_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_auth_url](../../../config/rgw/rgw.md#SP_rgw_swift_auth_url) |

**کارکرد:** Swift auth URL

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_auth_url "https://swift.example.com/auth/v1.0"
ceph config get client.rgw rgw_swift_auth_url
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_auth_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_custom_header

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_custom_header](../../../config/rgw/rgw.md#SP_rgw_swift_custom_header) |

**کارکرد:** Enable swift custom header

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_custom_header <value>
ceph config get client.rgw rgw_swift_custom_header
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_custom_header
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_enforce_content_length

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_enforce_content_length](../../../config/rgw/rgw.md#SP_rgw_swift_enforce_content_length) |

**کارکرد:** Send content length when listing containers (Swift)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_enforce_content_length true
ceph config get client.rgw rgw_swift_enforce_content_length
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_need_stats

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_need_stats](../../../config/rgw/rgw.md#SP_rgw_swift_need_stats) |

**کارکرد:** Enable stats on bucket listing in Swift

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_need_stats false
ceph config get client.rgw rgw_swift_need_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_tenant_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_tenant_name](../../../config/rgw/rgw.md#SP_rgw_swift_tenant_name) |

**کارکرد:** Swift tenant name

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_tenant_name <value>
ceph config get client.rgw rgw_swift_tenant_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_tenant_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_token_expiration

| | |
|---|---|
| نوع | Int · default `1_day` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_token_expiration](../../../config/rgw/rgw.md#SP_rgw_swift_token_expiration) |

**کارکرد:** Expiration time (in seconds) for token generated through RGW Swift auth.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_token_expiration 1_day
ceph config get client.rgw rgw_swift_token_expiration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1_day`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_token_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_url](../../../config/rgw/rgw.md#SP_rgw_swift_url) |

**کارکرد:** Swift-auth storage URL

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_url "https://swift.example.com/auth/v1.0"
ceph config get client.rgw rgw_swift_url
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url_prefix

| | |
|---|---|
| نوع | Str · default `swift` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_url_prefix](../../../config/rgw/rgw.md#SP_rgw_swift_url_prefix) |

**کارکرد:** Swift URL prefix

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_url_prefix swift
ceph config get client.rgw rgw_swift_url_prefix
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `swift`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_url_prefix
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_versioning_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_swift_versioning_enabled](../../../config/rgw/rgw.md#SP_rgw_swift_versioning_enabled) |

**کارکرد:** Enable Swift versioning

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_swift_versioning_enabled true
ceph config get client.rgw rgw_swift_versioning_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
