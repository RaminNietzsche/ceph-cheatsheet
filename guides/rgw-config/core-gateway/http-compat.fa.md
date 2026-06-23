# HTTP compatibility

راهنمای عمیق پیکربندی RGW — 17 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_content_length_compat](#rgw_content_length_compat) | `False` | Advanced | Policy |
| [rgw_cross_domain_policy](#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Advanced | Performance |
| [rgw_defer_to_bucket_acls](#rgw_defer_to_bucket_acls) | `(empty)` | Advanced | Performance |
| [rgw_enforce_swift_acls](#rgw_enforce_swift_acls) | `True` | Advanced | Policy |
| [rgw_extended_http_attrs](#rgw_extended_http_attrs) | `(empty)` | Advanced | Performance |
| [rgw_ignore_get_invalid_range](#rgw_ignore_get_invalid_range) | `False` | Advanced | Policy |
| [rgw_print_continue](#rgw_print_continue) | `True` | Advanced | Policy |
| [rgw_print_prohibited_content_length](#rgw_print_prohibited_content_length) | `False` | Advanced | Policy |
| [rgw_relaxed_region_enforcement](#rgw_relaxed_region_enforcement) | `False` | Advanced | Policy |
| [rgw_relaxed_s3_bucket_names](#rgw_relaxed_s3_bucket_names) | `False` | Advanced | Policy |
| [rgw_relaxed_topic_names](#rgw_relaxed_topic_names) | `False` | Advanced | Policy |
| [rgw_remote_addr_param](#rgw_remote_addr_param) | `REMOTE_ADDR` | Advanced | Performance |
| [rgw_request_uri](#rgw_request_uri) | `(empty)` | Dev | Connectivity |
| [rgw_resolve_cname](#rgw_resolve_cname) | `False` | Advanced | Policy |
| [rgw_service_provider_name](#rgw_service_provider_name) | `(empty)` | Advanced | Performance |
| [rgw_trust_forwarded_https](#rgw_trust_forwarded_https) | `False` | Advanced | Policy |
| [rgw_verify_ssl](#rgw_verify_ssl) | `True` | Advanced | Policy |

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

### rgw_content_length_compat

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_content_length_compat](../../../config/rgw/rgw.md#SP_rgw_content_length_compat) |

**کارکرد:** Multiple content length headers compatibility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_content_length_compat true
ceph config get client.rgw rgw_content_length_compat
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_cross_domain_policy

| | |
|---|---|
| نوع | Str · default `<allow-access-from domain="*" secure="false" />` · **Advanced** |
| جدول | [rgw.md#SP_rgw_cross_domain_policy](../../../config/rgw/rgw.md#SP_rgw_cross_domain_policy) |

**کارکرد:** RGW handle cross domain policy

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_cross_domain_policy "<allow-access-from domain="*" secure="false" />"
ceph config get client.rgw rgw_cross_domain_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `<allow-access-from domain="*" secure="false" />`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_cross_domain_policy
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_defer_to_bucket_acls

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_defer_to_bucket_acls](../../../config/rgw/rgw.md#SP_rgw_defer_to_bucket_acls) |

**کارکرد:** Bucket ACLs override object ACLs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_defer_to_bucket_acls <value>
ceph config get client.rgw rgw_defer_to_bucket_acls
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_defer_to_bucket_acls
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_enforce_swift_acls

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_enforce_swift_acls](../../../config/rgw/rgw.md#SP_rgw_enforce_swift_acls) |

**کارکرد:** RGW enforce swift acls

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_enforce_swift_acls false
ceph config get client.rgw rgw_enforce_swift_acls
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_extended_http_attrs

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_extended_http_attrs](../../../config/rgw/rgw.md#SP_rgw_extended_http_attrs) |

**کارکرد:** RGW support extended HTTP attrs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_extended_http_attrs <value>
ceph config get client.rgw rgw_extended_http_attrs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_extended_http_attrs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ignore_get_invalid_range

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_ignore_get_invalid_range](../../../config/rgw/rgw.md#SP_rgw_ignore_get_invalid_range) |

**کارکرد:** Treat invalid (e.g., negative) range request as full

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_ignore_get_invalid_range true
ceph config get client.rgw rgw_ignore_get_invalid_range
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_continue

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_print_continue](../../../config/rgw/rgw.md#SP_rgw_print_continue) |

**کارکرد:** RGW support of 100-continue

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_print_continue false
ceph config get client.rgw rgw_print_continue
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_prohibited_content_length

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_print_prohibited_content_length](../../../config/rgw/rgw.md#SP_rgw_print_prohibited_content_length) |

**کارکرد:** RGW RFC-7230 compatibility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_print_prohibited_content_length true
ceph config get client.rgw rgw_print_prohibited_content_length
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_region_enforcement

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_relaxed_region_enforcement](../../../config/rgw/rgw.md#SP_rgw_relaxed_region_enforcement) |

**کارکرد:** Disable region constraint enforcement

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_relaxed_region_enforcement true
ceph config get client.rgw rgw_relaxed_region_enforcement
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_s3_bucket_names

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_relaxed_s3_bucket_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_s3_bucket_names) |

**کارکرد:** RGW enable relaxed S3 bucket names

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_relaxed_s3_bucket_names true
ceph config get client.rgw rgw_relaxed_s3_bucket_names
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_topic_names

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_relaxed_topic_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_topic_names) |

**کارکرد:** RGW enable relaxed topic names

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_relaxed_topic_names true
ceph config get client.rgw rgw_relaxed_topic_names
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_remote_addr_param

| | |
|---|---|
| نوع | Str · default `REMOTE_ADDR` · **Advanced** |
| جدول | [rgw.md#SP_rgw_remote_addr_param](../../../config/rgw/rgw.md#SP_rgw_remote_addr_param) |

**کارکرد:** HTTP header that holds the remote address in incoming requests.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_remote_addr_param REMOTE_ADDR
ceph config get client.rgw rgw_remote_addr_param
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `REMOTE_ADDR`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_remote_addr_param
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_request_uri

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_request_uri](../../../config/rgw/rgw.md#SP_rgw_request_uri) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_request_uri "https://service.example.com/"
ceph config get client.rgw rgw_request_uri
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
ceph config get client.rgw rgw_request_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_resolve_cname

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_resolve_cname](../../../config/rgw/rgw.md#SP_rgw_resolve_cname) |

**کارکرد:** Support vanity domain names via CNAME

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_resolve_cname true
ceph config get client.rgw rgw_resolve_cname
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_service_provider_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_service_provider_name](../../../config/rgw/rgw.md#SP_rgw_service_provider_name) |

**کارکرد:** Service provider name which is contained in http response headers

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_service_provider_name <value>
ceph config get client.rgw rgw_service_provider_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_service_provider_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_trust_forwarded_https

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_trust_forwarded_https](../../../config/rgw/rgw.md#SP_rgw_trust_forwarded_https) |

**کارکرد:** Trust Forwarded and X-Forwarded-Proto headers

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_trust_forwarded_https true
ceph config get client.rgw rgw_trust_forwarded_https
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_verify_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_verify_ssl) |

**کارکرد:** Should RGW verify SSL when connecting to a remote HTTP server

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_verify_ssl false
ceph config get client.rgw rgw_verify_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
