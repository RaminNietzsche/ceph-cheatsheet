# HTTP compatibility

راهنمای عمیق پیکربندی RGW — 17 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_content_length_compat](#rgw_content_length_compat) | `False` | Advanced | سیاست |
| [rgw_cross_domain_policy](#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Advanced | عملکرد |
| [rgw_defer_to_bucket_acls](#rgw_defer_to_bucket_acls) | `(empty)` | Advanced | عملکرد |
| [rgw_enforce_swift_acls](#rgw_enforce_swift_acls) | `True` | Advanced | سیاست |
| [rgw_extended_http_attrs](#rgw_extended_http_attrs) | `(empty)` | Advanced | عملکرد |
| [rgw_ignore_get_invalid_range](#rgw_ignore_get_invalid_range) | `False` | Advanced | سیاست |
| [rgw_print_continue](#rgw_print_continue) | `True` | Advanced | سیاست |
| [rgw_print_prohibited_content_length](#rgw_print_prohibited_content_length) | `False` | Advanced | سیاست |
| [rgw_relaxed_region_enforcement](#rgw_relaxed_region_enforcement) | `False` | Advanced | سیاست |
| [rgw_relaxed_s3_bucket_names](#rgw_relaxed_s3_bucket_names) | `False` | Advanced | سیاست |
| [rgw_relaxed_topic_names](#rgw_relaxed_topic_names) | `False` | Advanced | سیاست |
| [rgw_remote_addr_param](#rgw_remote_addr_param) | `REMOTE_ADDR` | Advanced | عملکرد |
| [rgw_request_uri](#rgw_request_uri) | `(empty)` | Dev | اتصال |
| [rgw_resolve_cname](#rgw_resolve_cname) | `False` | Advanced | سیاست |
| [rgw_service_provider_name](#rgw_service_provider_name) | `(empty)` | Advanced | عملکرد |
| [rgw_trust_forwarded_https](#rgw_trust_forwarded_https) | `False` | Advanced | سیاست |
| [rgw_verify_ssl](#rgw_verify_ssl) | `True` | Advanced | سیاست |

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

### rgw_content_length_compat

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_content_length_compat](../../../config/rgw/rgw.md#SP_rgw_content_length_compat) |

**کارکرد:** Multiple content length headers compatibility Try to handle requests with ambiguous multiple content length headers (Content-Length, Http-Content-Length).

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

**کارکرد:** RGW handle cross domain policy Returned cross domain policy when accessing the crossdomain.xml resource (Swift compatibility).

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

**کارکرد:** Bucket ACLs override object ACLs If not empty, a string that selects that mode of operation. 'recurse' will use bucket's ACL for the authorization. 'full-control' will allow users that users that have full control permission on the bucket have access to the object.

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

**کارکرد:** RGW enforce swift acls Should RGW enforce special Swift-only ACLs. Swift has a special ACL that gives permission to access all objects in a container.

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

**کارکرد:** RGW support extended HTTP attrs Add new set of attributes that could be set on an object. These extra attributes can be set through HTTP header fields when putting the objects. If set, these attributes will return as HTTP fields when doing GET/HEAD on the object.

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

**کارکرد:** Treat invalid (e.g., negative) range request as full Treat invalid (e.g., negative) range request as request for the full object (AWS compatibility)

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

**کارکرد:** RGW support of 100-continue Should RGW explicitly send 100 (continue) responses. This is mainly relevant when using FastCGI, as some FastCGI modules do not fully support this feature.

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

**کارکرد:** RGW RFC-7230 compatibility Specifies whether RGW violates RFC 7230 and sends Content-Length with 204 or 304 statuses.

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

**کارکرد:** Disable region constraint enforcement Enable requests such as bucket creation to succeed irrespective of region restrictions (Jewel compat).

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

**کارکرد:** RGW enable relaxed S3 bucket names RGW enable relaxed S3 bucket name rules for US region buckets.

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

**کارکرد:** RGW enable relaxed topic names RGW enable relaxed topic names to allow changing existing topics that were created before validation rules were implemented. This also allows re-creating topics that were deleted, but match names that are already used externally (e.g. in Kafka)

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

**کارکرد:** HTTP header that holds the remote address in incoming requests. RGW will use this header to extract requests origin. When RGW runs behind a reverse proxy, the remote address header will point at the proxy's address and not at the originator's address. Therefore it is sometimes possible to have the proxy add the originator's address in a separate HTTP header, which will allow RGW to log it correctly.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`rgw_enable_ops_log`](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log)

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

**کارکرد:** Support vanity domain names via CNAME If true, RGW will query DNS when detecting that it's serving a request that was sent to a host in another domain. If a CNAME record is configured for that domain it will use it instead. This gives user to have the ability of creating a unique domain of their own to point at data in their bucket.

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

**کارکرد:** Service provider name which is contained in http response headers As S3 or other cloud storage providers do, http response headers should contain the name of the provider. This name will be placed in http header 'Server'.

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

**کارکرد:** Trust Forwarded and X-Forwarded-Proto headers When a proxy in front of radosgw is used for ssl termination, radosgw does not know whether incoming http connections are secure. Enable this option to trust the Forwarded and X-Forwarded-Proto headers sent by the proxy when determining whether the connection is secure. This is required for some features, such as server side encryption. (Never enable this setting if you do not have a trusted proxy in front of radosgw, or else malicious users will be able to set these headers in any request.)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`rgw_crypt_require_ssl`](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl)

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

**کارکرد:** Should RGW verify SSL when connecting to a remote HTTP server RGW can send requests to other RGW servers (e.g., in multi-site sync work). This configurable selects whether RGW should verify the certificate for the remote peer and host.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`rgw_keystone_verify_ssl`](../../../config/rgw/rgw.md#SP_rgw_keystone_verify_ssl)

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
