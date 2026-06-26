# Encryption & KMS

راهنمای عمیق پیکربندی RGW — 43 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_barbican_url](#rgw_barbican_url) | `(empty)` | Advanced | اتصال |
| [rgw_crypt_default_encryption_key](#rgw_crypt_default_encryption_key) | `(empty)` | Dev | عملکرد |
| [rgw_crypt_kmip_addr](#rgw_crypt_kmip_addr) | `(empty)` | Advanced | اتصال |
| [rgw_crypt_kmip_ca_path](#rgw_crypt_kmip_ca_path) | `(empty)` | Advanced | ظرفیت |
| [rgw_crypt_kmip_client_cert](#rgw_crypt_kmip_client_cert) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_kmip_client_key](#rgw_crypt_kmip_client_key) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_kmip_kms_key_template](#rgw_crypt_kmip_kms_key_template) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_kmip_password](#rgw_crypt_kmip_password) | `(empty)` | Advanced | سیاست |
| [rgw_crypt_kmip_s3_key_template](#rgw_crypt_kmip_s3_key_template) | `$keyid` | Advanced | عملکرد |
| [rgw_crypt_kmip_username](#rgw_crypt_kmip_username) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_require_ssl](#rgw_crypt_require_ssl) | `True` | Advanced | سیاست |
| [rgw_crypt_s3_kms_backend](#rgw_crypt_s3_kms_backend) | `barbican` | Advanced | معماری |
| [rgw_crypt_s3_kms_cache_enabled](#rgw_crypt_s3_kms_cache_enabled) | `True` | Advanced | سیاست |
| [rgw_crypt_s3_kms_cache_max_size](#rgw_crypt_s3_kms_cache_max_size) | `128` | Advanced | سیاست |
| [rgw_crypt_s3_kms_cache_negative_ttl](#rgw_crypt_s3_kms_cache_negative_ttl) | `120` | Advanced | عملکرد |
| [rgw_crypt_s3_kms_cache_positive_ttl](#rgw_crypt_s3_kms_cache_positive_ttl) | `60` | Advanced | عملکرد |
| [rgw_crypt_s3_kms_cache_transient_error_ttl](#rgw_crypt_s3_kms_cache_transient_error_ttl) | `10` | Advanced | عملکرد |
| [rgw_crypt_s3_kms_encryption_keys](#rgw_crypt_s3_kms_encryption_keys) | `(empty)` | Dev | عملکرد |
| [rgw_crypt_s3_kms_testing_delay](#rgw_crypt_s3_kms_testing_delay) | `0` | Dev | عملکرد |
| [rgw_crypt_sse_algorithm](#rgw_crypt_sse_algorithm) | `aes-256-cbc` | Advanced | معماری |
| [rgw_crypt_sse_s3_backend](#rgw_crypt_sse_s3_backend) | `vault` | Advanced | معماری |
| [rgw_crypt_sse_s3_key_template](#rgw_crypt_sse_s3_key_template) | `%bucket_id` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_addr](#rgw_crypt_sse_s3_vault_addr) | `(empty)` | Advanced | اتصال |
| [rgw_crypt_sse_s3_vault_auth](#rgw_crypt_sse_s3_vault_auth) | `token` | Advanced | معماری |
| [rgw_crypt_sse_s3_vault_namespace](#rgw_crypt_sse_s3_vault_namespace) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_prefix](#rgw_crypt_sse_s3_vault_prefix) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_secret_engine](#rgw_crypt_sse_s3_vault_secret_engine) | `transit` | Advanced | سیاست |
| [rgw_crypt_sse_s3_vault_ssl_cacert](#rgw_crypt_sse_s3_vault_ssl_cacert) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_ssl_clientcert](#rgw_crypt_sse_s3_vault_ssl_clientcert) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_ssl_clientkey](#rgw_crypt_sse_s3_vault_ssl_clientkey) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_sse_s3_vault_token_file](#rgw_crypt_sse_s3_vault_token_file) | `(empty)` | Advanced | ظرفیت |
| [rgw_crypt_sse_s3_vault_verify_ssl](#rgw_crypt_sse_s3_vault_verify_ssl) | `True` | Advanced | سیاست |
| [rgw_crypt_suppress_logs](#rgw_crypt_suppress_logs) | `True` | Advanced | سیاست |
| [rgw_crypt_vault_addr](#rgw_crypt_vault_addr) | `(empty)` | Advanced | اتصال |
| [rgw_crypt_vault_auth](#rgw_crypt_vault_auth) | `token` | Advanced | معماری |
| [rgw_crypt_vault_namespace](#rgw_crypt_vault_namespace) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_vault_prefix](#rgw_crypt_vault_prefix) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_vault_secret_engine](#rgw_crypt_vault_secret_engine) | `transit` | Advanced | سیاست |
| [rgw_crypt_vault_ssl_cacert](#rgw_crypt_vault_ssl_cacert) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_vault_ssl_clientcert](#rgw_crypt_vault_ssl_clientcert) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_vault_ssl_clientkey](#rgw_crypt_vault_ssl_clientkey) | `(empty)` | Advanced | عملکرد |
| [rgw_crypt_vault_token_file](#rgw_crypt_vault_token_file) | `(empty)` | Advanced | ظرفیت |
| [rgw_crypt_vault_verify_ssl](#rgw_crypt_vault_verify_ssl) | `True` | Advanced | سیاست |

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

### rgw_barbican_url

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_barbican_url](../../../config/rgw/rgw.md#SP_rgw_barbican_url) |

**کارکرد:** Base URL of the **OpenStack Barbican** key manager for **SSE-KMS** server-side encryption.

**زمان استفاده:** Store encryption keys in Barbican instead of on-cluster secrets. Requires Keystone credentials for Barbican access.

**گزینه‌های مرتبط:**

- `rgw_crypt_s3_kms_backend` = `barbican`
- `rgw_keystone_barbican_*`, `rgw_crypt_s3_kms_cache_*`

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

See [Ceph RGW config ref — Barbican](https://docs.ceph.com/en/latest/radosgw/config-ref/#barbican-settings).

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_barbican_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_default_encryption_key

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_crypt_default_encryption_key](../../../config/rgw/rgw.md#SP_rgw_crypt_default_encryption_key) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_default_encryption_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_default_encryption_key
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_default_encryption_key
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_addr) |

**کارکرد:** kmip server address

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_addr "kmip.example.com:5696"
ceph config get client.rgw rgw_crypt_kmip_addr
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
ceph config get client.rgw rgw_crypt_kmip_addr
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_ca_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_ca_path](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_ca_path) |

**کارکرد:** ca for kmip servers

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_ca_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_crypt_kmip_ca_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_crypt_kmip_ca_path)
iostat -x 5  # disk saturation
```

---

### rgw_crypt_kmip_client_cert

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_client_cert](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_cert) |

**کارکرد:** connect using client certificate

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_cert <value>
ceph config get client.rgw rgw_crypt_kmip_client_cert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_kmip_client_cert
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_client_key

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_client_key](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_key) |

**کارکرد:** connect using client certificate

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_client_key
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_kmip_client_key
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_kms_key_template

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_kms_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_kms_key_template) |

**کارکرد:** sse-kms; kmip key names

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_kms_key_template <value>
ceph config get client.rgw rgw_crypt_kmip_kms_key_template
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_kmip_kms_key_template
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_password

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_password](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_password) |

**کارکرد:** optional w/ username

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_password "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_password
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_kmip_s3_key_template

| | |
|---|---|
| نوع | Str · default `$keyid` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_s3_key_template) |

**کارکرد:** sse-s3; kmip key template

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_s3_key_template $keyid
ceph config get client.rgw rgw_crypt_kmip_s3_key_template
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `$keyid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_kmip_s3_key_template
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_kmip_username

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_kmip_username](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_username) |

**کارکرد:** when authenticating via username

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_kmip_username <value>
ceph config get client.rgw rgw_crypt_kmip_username
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_kmip_username
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_require_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_require_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl) |

**کارکرد:** Requests including encryption key headers must be sent over ssl

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_require_ssl false
ceph config get client.rgw rgw_crypt_require_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_s3_kms_backend

| | |
|---|---|
| نوع | Str · enum: ["barbican", "vault", "testing", "kmip"] · default `barbican` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_backend) |

**کارکرد:** Where the SSE-KMS encryption keys are stored. Supported KMS systems are OpenStack Barbican ('barbican', the default) and HashiCorp Vault ('vault').

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config get client.rgw rgw_crypt_s3_kms_backend
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["barbican", "vault", "testing", "kmip"].
2. Default `barbican` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_s3_kms_cache_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled) |

**کارکرد:** Enable caching of encryption keys for SSE-KMS.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_enabled false
ceph config get client.rgw rgw_crypt_s3_kms_cache_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_s3_kms_cache_max_size

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_cache_max_size](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_max_size) |

**کارکرد:** Maximum number of SSE-KMS secrets cached. Each key consumes 32 byte (AES-256) + overhead in memory

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**گزینه‌های مرتبط:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_max_size 128
ceph config get client.rgw rgw_crypt_s3_kms_cache_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_crypt_s3_kms_cache_negative_ttl

| | |
|---|---|
| نوع | Uint · default `120` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl) |

**کارکرد:** Time in seconds after which the KMS cache evicts permanent look-up errors (e.g key does not exist).

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**گزینه‌های مرتبط:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_negative_ttl 120
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `120`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_cache_positive_ttl

| | |
|---|---|
| نوع | Uint · default `60` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl) |

**کارکرد:** Time in seconds after which the KMS cache evicts successful lookups.

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**گزینه‌های مرتبط:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_positive_ttl 60
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `60`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `10`, max `3600`.

---

### rgw_crypt_s3_kms_cache_transient_error_ttl

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl) |

**کارکرد:** Time in seconds after which the KMS cache evicts entries representing transient errors (timeouts, temporary outages, misconfiguration, etc).

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**گزینه‌های مرتبط:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl 10
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_encryption_keys

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_encryption_keys](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_encryption_keys) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_encryption_keys <value>
ceph config get client.rgw rgw_crypt_s3_kms_encryption_keys
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_encryption_keys
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_s3_kms_testing_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [rgw.md#SP_rgw_crypt_s3_kms_testing_delay](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_testing_delay) |

**کارکرد:** Add delay in milliseconds to the 'testing' KMS key retrieval.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_testing_delay 0
ceph config get client.rgw rgw_crypt_s3_kms_testing_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_testing_delay
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_algorithm

| | |
|---|---|
| نوع | Str · enum: ["aes-256-cbc", "aes-256-gcm"] · default `aes-256-cbc` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_algorithm](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_algorithm) |

**کارکرد:** Default encryption algorithm for server-side encryption Specifies the default AES encryption algorithm to use for new objects encrypted with SSE-C, SSE-KMS, SSE-S3, or RGW-AUTO modes. Valid values are aes-256-cbc (legacy, compatible with older RGW versions) and aes-256-gcm (recommended, provides authenticated encryption). Existing encrypted objects are always decrypted using the algorithm specified in their metadata, regardless of this setting.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`rgw_crypt_require_ssl`](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl)

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_algorithm "aes-256-cbc"
ceph config get client.rgw rgw_crypt_sse_algorithm
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["aes-256-cbc", "aes-256-gcm"].
2. Default `aes-256-cbc` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_backend

| | |
|---|---|
| نوع | Str · enum: ["vault"] · default `vault` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_backend) |

**کارکرد:** Where the SSE-S3 encryption keys are stored. The only valid choice here is HashiCorp Vault ('vault').

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_backend vault
ceph config get client.rgw rgw_crypt_sse_s3_backend
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["vault"].
2. Default `vault` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_key_template

| | |
|---|---|
| نوع | Str · default `%bucket_id` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_key_template) |

**کارکرد:** template for per-bucket SSE-S3 keys in Vault. This is the template for per-bucket sse-s3 keys. This string may include ``%bucket_id`` which will be expanded out to the bucket marker, a unique uuid assigned to that bucket. It could contain ``%owner_id``, which will expand out to the owner's id. Any other use of % is reserved and should not be used. If the template contains ``%bucket_id``, associated bucket keys will be automatically removed when the bucket is removed.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_key_template %bucket_id
ceph config get client.rgw rgw_crypt_sse_s3_key_template
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `%bucket_id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_key_template
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_addr) |

**کارکرد:** SSE-S3 Vault server base address.

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_sse_s3_vault_addr
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
ceph config get client.rgw rgw_crypt_sse_s3_vault_addr
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_auth

| | |
|---|---|
| نوع | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_auth) |

**کارکرد:** Type of authentication method to be used with SSE-S3 and Vault.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_auth token
ceph config get client.rgw rgw_crypt_sse_s3_vault_auth
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_vault_namespace

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_namespace) |

**کارکرد:** Vault Namespace to be used to select your tenant

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_namespace <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_namespace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_vault_namespace
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_prefix

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_prefix) |

**کارکرد:** SSE-S3 Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_prefix <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_prefix
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_vault_prefix
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_secret_engine

| | |
|---|---|
| نوع | Str · default `transit` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine) |

**کارکرد:** Vault Secret Engine to be used to retrieve encryption keys.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_sse_s3_vault_secret_engine
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_sse_s3_vault_ssl_cacert

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert) |

**کارکرد:** Path for custom ca certificate for accessing vault server

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_cacert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_cacert
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_ssl_clientcert

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert) |

**کارکرد:** Path for custom client certificate for accessing vault server

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_ssl_clientkey

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey) |

**کارکرد:** Path for private key required for client cert

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_sse_s3_vault_token_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_token_file) |

**کارکرد:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_sse_s3_vault_token_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_crypt_sse_s3_vault_token_file)
iostat -x 5  # disk saturation
```

---

### rgw_crypt_sse_s3_vault_verify_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl) |

**کارکرد:** Should RGW verify the vault server SSL certificate.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_sse_s3_vault_verify_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_suppress_logs

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_suppress_logs](../../../config/rgw/rgw.md#SP_rgw_crypt_suppress_logs) |

**کارکرد:** Suppress logs that might print client key

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_suppress_logs false
ceph config get client.rgw rgw_crypt_suppress_logs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_vault_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_addr) |

**کارکرد:** Vault server base address.

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر قابلیت استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_vault_addr
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
ceph config get client.rgw rgw_crypt_vault_addr
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_auth

| | |
|---|---|
| نوع | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_auth) |

**کارکرد:** Type of authentication method to be used with Vault.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_auth token
ceph config get client.rgw rgw_crypt_vault_auth
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_vault_namespace

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_namespace) |

**کارکرد:** Vault Namespace to be used to select your tenant

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_namespace <value>
ceph config get client.rgw rgw_crypt_vault_namespace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_vault_namespace
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_prefix

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_prefix) |

**کارکرد:** Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_prefix <value>
ceph config get client.rgw rgw_crypt_vault_prefix
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_vault_prefix
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_secret_engine

| | |
|---|---|
| نوع | Str · default `transit` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_secret_engine) |

**کارکرد:** Vault Secret Engine to be used to retrieve encryption keys.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_vault_secret_engine
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_vault_ssl_cacert

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_cacert) |

**کارکرد:** Path for custom ca certificate for accessing vault server

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_cacert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_vault_ssl_cacert
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_ssl_clientcert

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientcert) |

**کارکرد:** Path for custom client certificate for accessing vault server

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientcert
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_vault_ssl_clientcert
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_ssl_clientkey

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientkey) |

**کارکرد:** Path for private key required for client cert

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientkey
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_crypt_vault_ssl_clientkey
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_crypt_vault_token_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_token_file) |

**کارکرد:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_vault_token_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_crypt_vault_token_file)
iostat -x 5  # disk saturation
```

---

### rgw_crypt_vault_verify_ssl

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_crypt_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_verify_ssl) |

**کارکرد:** Should RGW verify the vault server SSL certificate.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_crypt_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_vault_verify_ssl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
