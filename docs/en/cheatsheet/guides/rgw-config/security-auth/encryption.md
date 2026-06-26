# Encryption & KMS

RGW config deep dive — 43 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_barbican_url](#rgw_barbican_url) | `(empty)` | Advanced | Connectivity |
| [rgw_crypt_default_encryption_key](#rgw_crypt_default_encryption_key) | `(empty)` | Dev | Performance |
| [rgw_crypt_kmip_addr](#rgw_crypt_kmip_addr) | `(empty)` | Advanced | Connectivity |
| [rgw_crypt_kmip_ca_path](#rgw_crypt_kmip_ca_path) | `(empty)` | Advanced | Capacity |
| [rgw_crypt_kmip_client_cert](#rgw_crypt_kmip_client_cert) | `(empty)` | Advanced | Performance |
| [rgw_crypt_kmip_client_key](#rgw_crypt_kmip_client_key) | `(empty)` | Advanced | Performance |
| [rgw_crypt_kmip_kms_key_template](#rgw_crypt_kmip_kms_key_template) | `(empty)` | Advanced | Performance |
| [rgw_crypt_kmip_password](#rgw_crypt_kmip_password) | `(empty)` | Advanced | Policy |
| [rgw_crypt_kmip_s3_key_template](#rgw_crypt_kmip_s3_key_template) | `$keyid` | Advanced | Performance |
| [rgw_crypt_kmip_username](#rgw_crypt_kmip_username) | `(empty)` | Advanced | Performance |
| [rgw_crypt_require_ssl](#rgw_crypt_require_ssl) | `True` | Advanced | Policy |
| [rgw_crypt_s3_kms_backend](#rgw_crypt_s3_kms_backend) | `barbican` | Advanced | Architecture |
| [rgw_crypt_s3_kms_cache_enabled](#rgw_crypt_s3_kms_cache_enabled) | `True` | Advanced | Policy |
| [rgw_crypt_s3_kms_cache_max_size](#rgw_crypt_s3_kms_cache_max_size) | `128` | Advanced | Policy |
| [rgw_crypt_s3_kms_cache_negative_ttl](#rgw_crypt_s3_kms_cache_negative_ttl) | `120` | Advanced | Performance |
| [rgw_crypt_s3_kms_cache_positive_ttl](#rgw_crypt_s3_kms_cache_positive_ttl) | `60` | Advanced | Performance |
| [rgw_crypt_s3_kms_cache_transient_error_ttl](#rgw_crypt_s3_kms_cache_transient_error_ttl) | `10` | Advanced | Performance |
| [rgw_crypt_s3_kms_encryption_keys](#rgw_crypt_s3_kms_encryption_keys) | `(empty)` | Dev | Performance |
| [rgw_crypt_s3_kms_testing_delay](#rgw_crypt_s3_kms_testing_delay) | `0` | Dev | Performance |
| [rgw_crypt_sse_algorithm](#rgw_crypt_sse_algorithm) | `aes-256-cbc` | Advanced | Architecture |
| [rgw_crypt_sse_s3_backend](#rgw_crypt_sse_s3_backend) | `vault` | Advanced | Architecture |
| [rgw_crypt_sse_s3_key_template](#rgw_crypt_sse_s3_key_template) | `%bucket_id` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_addr](#rgw_crypt_sse_s3_vault_addr) | `(empty)` | Advanced | Connectivity |
| [rgw_crypt_sse_s3_vault_auth](#rgw_crypt_sse_s3_vault_auth) | `token` | Advanced | Architecture |
| [rgw_crypt_sse_s3_vault_namespace](#rgw_crypt_sse_s3_vault_namespace) | `(empty)` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_prefix](#rgw_crypt_sse_s3_vault_prefix) | `(empty)` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_secret_engine](#rgw_crypt_sse_s3_vault_secret_engine) | `transit` | Advanced | Policy |
| [rgw_crypt_sse_s3_vault_ssl_cacert](#rgw_crypt_sse_s3_vault_ssl_cacert) | `(empty)` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_ssl_clientcert](#rgw_crypt_sse_s3_vault_ssl_clientcert) | `(empty)` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_ssl_clientkey](#rgw_crypt_sse_s3_vault_ssl_clientkey) | `(empty)` | Advanced | Performance |
| [rgw_crypt_sse_s3_vault_token_file](#rgw_crypt_sse_s3_vault_token_file) | `(empty)` | Advanced | Capacity |
| [rgw_crypt_sse_s3_vault_verify_ssl](#rgw_crypt_sse_s3_vault_verify_ssl) | `True` | Advanced | Policy |
| [rgw_crypt_suppress_logs](#rgw_crypt_suppress_logs) | `True` | Advanced | Policy |
| [rgw_crypt_vault_addr](#rgw_crypt_vault_addr) | `(empty)` | Advanced | Connectivity |
| [rgw_crypt_vault_auth](#rgw_crypt_vault_auth) | `token` | Advanced | Architecture |
| [rgw_crypt_vault_namespace](#rgw_crypt_vault_namespace) | `(empty)` | Advanced | Performance |
| [rgw_crypt_vault_prefix](#rgw_crypt_vault_prefix) | `(empty)` | Advanced | Performance |
| [rgw_crypt_vault_secret_engine](#rgw_crypt_vault_secret_engine) | `transit` | Advanced | Policy |
| [rgw_crypt_vault_ssl_cacert](#rgw_crypt_vault_ssl_cacert) | `(empty)` | Advanced | Performance |
| [rgw_crypt_vault_ssl_clientcert](#rgw_crypt_vault_ssl_clientcert) | `(empty)` | Advanced | Performance |
| [rgw_crypt_vault_ssl_clientkey](#rgw_crypt_vault_ssl_clientkey) | `(empty)` | Advanced | Performance |
| [rgw_crypt_vault_token_file](#rgw_crypt_vault_token_file) | `(empty)` | Advanced | Capacity |
| [rgw_crypt_vault_verify_ssl](#rgw_crypt_vault_verify_ssl) | `True` | Advanced | Policy |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_barbican_url](../../../config/rgw/rgw.md#SP_rgw_barbican_url) |

**What it does:** Base URL of the **OpenStack Barbican** key manager for **SSE-KMS** server-side encryption.

**When to use:** Store encryption keys in Barbican instead of on-cluster secrets. Requires Keystone credentials for Barbican access.

**Related options:**

- `rgw_crypt_s3_kms_backend` = `barbican`
- `rgw_keystone_barbican_*`, `rgw_crypt_s3_kms_cache_*`

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

See [Ceph RGW config ref — Barbican](https://docs.ceph.com/en/latest/radosgw/config-ref/#barbican-settings).

**Finding optimal value:**

**Tuning model:** Connectivity

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
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_default_encryption_key](../../../config/rgw/rgw.md#SP_rgw_crypt_default_encryption_key) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_default_encryption_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_default_encryption_key
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_addr) |

**What it does:** kmip server address

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_addr "kmip.example.com:5696"
ceph config get client.rgw rgw_crypt_kmip_addr
# curl -k <url>  # from each RGW node
```

**Finding optimal value:**

**Tuning model:** Connectivity

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_ca_path](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_ca_path) |

**What it does:** ca for kmip servers

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_ca_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_crypt_kmip_ca_path
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_client_cert](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_cert) |

**What it does:** connect using client certificate

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_cert <value>
ceph config get client.rgw rgw_crypt_kmip_client_cert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_client_key](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_key) |

**What it does:** connect using client certificate

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_client_key
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_kms_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_kms_key_template) |

**What it does:** sse-kms; kmip key names

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_kms_key_template <value>
ceph config get client.rgw rgw_crypt_kmip_kms_key_template
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_password](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_password) |

**What it does:** optional w/ username

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_password "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_password
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_kmip_s3_key_template

| | |
|---|---|
| Type | Str · default `$keyid` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_s3_key_template) |

**What it does:** sse-s3; kmip key template

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_s3_key_template $keyid
ceph config get client.rgw rgw_crypt_kmip_s3_key_template
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `$keyid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_username](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_username) |

**What it does:** when authenticating via username

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_username <value>
ceph config get client.rgw rgw_crypt_kmip_username
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_require_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl) |

**What it does:** Requests including encryption key headers must be sent over ssl

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_require_ssl false
ceph config get client.rgw rgw_crypt_require_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_s3_kms_backend

| | |
|---|---|
| Type | Str · enum: ["barbican", "vault", "testing", "kmip"] · default `barbican` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_backend) |

**What it does:** Where the SSE-KMS encryption keys are stored. Supported KMS systems are OpenStack Barbican ('barbican', the default) and HashiCorp Vault ('vault').

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config get client.rgw rgw_crypt_s3_kms_backend
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["barbican", "vault", "testing", "kmip"].
2. Default `barbican` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_s3_kms_cache_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled) |

**What it does:** Enable caching of encryption keys for SSE-KMS.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_enabled false
ceph config get client.rgw rgw_crypt_s3_kms_cache_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_s3_kms_cache_max_size

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_max_size](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_max_size) |

**What it does:** Maximum number of SSE-KMS secrets cached. Each key consumes 32 byte (AES-256) + overhead in memory

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Related options:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_max_size 128
ceph config get client.rgw rgw_crypt_s3_kms_cache_max_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_crypt_s3_kms_cache_negative_ttl

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts permanent look-up errors (e.g key does not exist).

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Related options:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_negative_ttl 120
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `120`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_cache_positive_ttl

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts successful lookups.

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Related options:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_positive_ttl 60
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `60`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `10`, max `3600`.

---

### rgw_crypt_s3_kms_cache_transient_error_ttl

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts entries representing transient errors (timeouts, temporary outages, misconfiguration, etc).

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Related options:**

- [`rgw_crypt_s3_kms_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled)

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl 10
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_encryption_keys

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_encryption_keys](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_encryption_keys) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_encryption_keys <value>
ceph config get client.rgw rgw_crypt_s3_kms_encryption_keys
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_testing_delay](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_testing_delay) |

**What it does:** Add delay in milliseconds to the 'testing' KMS key retrieval.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_testing_delay 0
ceph config get client.rgw rgw_crypt_s3_kms_testing_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · enum: ["aes-256-cbc", "aes-256-gcm"] · default `aes-256-cbc` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_algorithm](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_algorithm) |

**What it does:** Default encryption algorithm for server-side encryption Specifies the default AES encryption algorithm to use for new objects encrypted with SSE-C, SSE-KMS, SSE-S3, or RGW-AUTO modes. Valid values are aes-256-cbc (legacy, compatible with older RGW versions) and aes-256-gcm (recommended, provides authenticated encryption). Existing encrypted objects are always decrypted using the algorithm specified in their metadata, regardless of this setting.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_crypt_require_ssl`](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl)

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_algorithm "aes-256-cbc"
ceph config get client.rgw rgw_crypt_sse_algorithm
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["aes-256-cbc", "aes-256-gcm"].
2. Default `aes-256-cbc` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_backend

| | |
|---|---|
| Type | Str · enum: ["vault"] · default `vault` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_backend) |

**What it does:** Where the SSE-S3 encryption keys are stored. The only valid choice here is HashiCorp Vault ('vault').

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_backend vault
ceph config get client.rgw rgw_crypt_sse_s3_backend
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["vault"].
2. Default `vault` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_key_template

| | |
|---|---|
| Type | Str · default `%bucket_id` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_key_template) |

**What it does:** template for per-bucket SSE-S3 keys in Vault. This is the template for per-bucket sse-s3 keys. This string may include ``%bucket_id`` which will be expanded out to the bucket marker, a unique uuid assigned to that bucket. It could contain ``%owner_id``, which will expand out to the owner's id. Any other use of % is reserved and should not be used. If the template contains ``%bucket_id``, associated bucket keys will be automatically removed when the bucket is removed.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_key_template %bucket_id
ceph config get client.rgw rgw_crypt_sse_s3_key_template
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `%bucket_id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_addr) |

**What it does:** SSE-S3 Vault server base address.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_sse_s3_vault_addr
# curl -k <url>  # from each RGW node
```

**Finding optimal value:**

**Tuning model:** Connectivity

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
| Type | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_auth) |

**What it does:** Type of authentication method to be used with SSE-S3 and Vault.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_auth token
ceph config get client.rgw rgw_crypt_sse_s3_vault_auth
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_vault_namespace

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_namespace) |

**What it does:** Vault Namespace to be used to select your tenant

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_namespace <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_namespace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_prefix) |

**What it does:** SSE-S3 Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_prefix <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_prefix
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `transit` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine) |

**What it does:** Vault Secret Engine to be used to retrieve encryption keys.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_sse_s3_vault_secret_engine
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_sse_s3_vault_ssl_cacert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert) |

**What it does:** Path for custom ca certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_cacert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert) |

**What it does:** Path for custom client certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey) |

**What it does:** Path for private key required for client cert

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_token_file) |

**What it does:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_sse_s3_vault_token_file
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl) |

**What it does:** Should RGW verify the vault server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_sse_s3_vault_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_suppress_logs

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_suppress_logs](../../../config/rgw/rgw.md#SP_rgw_crypt_suppress_logs) |

**What it does:** Suppress logs that might print client key

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_suppress_logs false
ceph config get client.rgw rgw_crypt_suppress_logs
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_vault_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_addr) |

**What it does:** Vault server base address.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_vault_addr
# curl -k <url>  # from each RGW node
```

**Finding optimal value:**

**Tuning model:** Connectivity

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
| Type | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_auth) |

**What it does:** Type of authentication method to be used with Vault.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_auth token
ceph config get client.rgw rgw_crypt_vault_auth
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_vault_namespace

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_namespace) |

**What it does:** Vault Namespace to be used to select your tenant

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_namespace <value>
ceph config get client.rgw rgw_crypt_vault_namespace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_prefix) |

**What it does:** Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_prefix <value>
ceph config get client.rgw rgw_crypt_vault_prefix
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `transit` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_secret_engine) |

**What it does:** Vault Secret Engine to be used to retrieve encryption keys.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_vault_secret_engine
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_vault_ssl_cacert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_cacert) |

**What it does:** Path for custom ca certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_cacert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientcert) |

**What it does:** Path for custom client certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientcert
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientkey) |

**What it does:** Path for private key required for client cert

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientkey
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_token_file) |

**What it does:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_vault_token_file
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_verify_ssl) |

**What it does:** Should RGW verify the vault server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_vault_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← RGW config overview](../OVERVIEW.md)
