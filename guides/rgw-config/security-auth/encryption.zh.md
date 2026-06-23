# Encryption & KMS

RGW 配置深度指南 — 43 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
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

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、API 兼容性、租户限制 |
| **Capacity** | 磁盘布局、路径、池容量 |
| **Performance** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **Connectivity** | 最近且稳定的外部端点 |
| **Architecture** | 后端、多站点拓扑 — 非数值扫描 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_barbican_url](../../../config/rgw/rgw.md#SP_rgw_barbican_url) |

**作用：** Base URL of the **OpenStack Barbican** key manager for **SSE-KMS** server-side encryption.

**何时使用：** Store encryption keys in Barbican instead of on-cluster secrets. Requires Keystone credentials for Barbican access.

**相关选项：**

- `rgw_crypt_s3_kms_backend` = `barbican`
- `rgw_keystone_barbican_*`, `rgw_crypt_s3_kms_cache_*`

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

See [Ceph RGW config ref — Barbican](https://docs.ceph.com/en/latest/radosgw/config-ref/#barbican-settings).

**寻找最优值：**

**调优模型：** Connectivity

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
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_crypt_default_encryption_key](../../../config/rgw/rgw.md#SP_rgw_crypt_default_encryption_key) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_default_encryption_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_default_encryption_key
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_addr) |

**作用：** kmip server address

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_addr "kmip.example.com:5696"
ceph config get client.rgw rgw_crypt_kmip_addr
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_ca_path](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_ca_path) |

**作用：** ca for kmip servers

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_ca_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_crypt_kmip_ca_path
```

**寻找最优值：**

**调优模型：** Capacity

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_client_cert](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_cert) |

**作用：** connect using client certificate

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_cert <value>
ceph config get client.rgw rgw_crypt_kmip_client_cert
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_client_key](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_key) |

**作用：** connect using client certificate

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_key "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_client_key
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_kms_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_kms_key_template) |

**作用：** sse-kms; kmip key names

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_kms_key_template <value>
ceph config get client.rgw rgw_crypt_kmip_kms_key_template
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_password](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_password) |

**作用：** optional w/ username

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_password "<from-secrets-manager>"
ceph config get client.rgw rgw_crypt_kmip_password
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_kmip_s3_key_template

| | |
|---|---|
| 类型 | Str · default `$keyid` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_s3_key_template) |

**作用：** sse-s3; kmip key template

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_s3_key_template $keyid
ceph config get client.rgw rgw_crypt_kmip_s3_key_template
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `$keyid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_kmip_username](../../../config/rgw/rgw.md#SP_rgw_crypt_kmip_username) |

**作用：** when authenticating via username

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_kmip_username <value>
ceph config get client.rgw rgw_crypt_kmip_username
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_require_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl) |

**作用：** Requests including encryption key headers must be sent over ssl

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_require_ssl false
ceph config get client.rgw rgw_crypt_require_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_s3_kms_backend

| | |
|---|---|
| 类型 | Str · enum: ["barbican", "vault", "testing", "kmip"] · default `barbican` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_backend) |

**作用：** Where the SSE-KMS encryption keys are stored. Supported KMS systems are OpenStack Barbican ('barbican', the default) and HashiCorp Vault ('vault').

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config get client.rgw rgw_crypt_s3_kms_backend
ceph config set client.rgw rgw_barbican_url https://barbican.example.com:9311/
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["barbican", "vault", "testing", "kmip"].
2. Default `barbican` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_s3_kms_cache_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled) |

**作用：** Enable caching of encryption keys for SSE-KMS.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_enabled false
ceph config get client.rgw rgw_crypt_s3_kms_cache_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_s3_kms_cache_max_size

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_cache_max_size](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_max_size) |

**作用：** Maximum number of SSE-KMS secrets cached. Each key consumes 32 byte (AES-256) + overhead in memory

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_max_size 128
ceph config get client.rgw rgw_crypt_s3_kms_cache_max_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_crypt_s3_kms_cache_negative_ttl

| | |
|---|---|
| 类型 | Uint · default `120` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl) |

**作用：** Time in seconds after which the KMS cache evicts permanent look-up errors (e.g key does not exist).

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_negative_ttl 120
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `120`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_cache_positive_ttl

| | |
|---|---|
| 类型 | Uint · default `60` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl) |

**作用：** Time in seconds after which the KMS cache evicts successful lookups.

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_positive_ttl 60
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `60`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `10`, max `3600`.

---

### rgw_crypt_s3_kms_cache_transient_error_ttl

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl) |

**作用：** Time in seconds after which the KMS cache evicts entries representing transient errors (timeouts, temporary outages, misconfiguration, etc).

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl 10
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0`, max `3600`.

---

### rgw_crypt_s3_kms_encryption_keys

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_encryption_keys](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_encryption_keys) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_encryption_keys <value>
ceph config get client.rgw rgw_crypt_s3_kms_encryption_keys
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_crypt_s3_kms_testing_delay](../../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_testing_delay) |

**作用：** Add delay in milliseconds to the 'testing' KMS key retrieval.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_testing_delay 0
ceph config get client.rgw rgw_crypt_s3_kms_testing_delay
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · enum: ["aes-256-cbc", "aes-256-gcm"] · default `aes-256-cbc` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_algorithm](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_algorithm) |

**作用：** Default encryption algorithm for server-side encryption

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_algorithm "aes-256-cbc"
ceph config get client.rgw rgw_crypt_sse_algorithm
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["aes-256-cbc", "aes-256-gcm"].
2. Default `aes-256-cbc` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_backend

| | |
|---|---|
| 类型 | Str · enum: ["vault"] · default `vault` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_backend](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_backend) |

**作用：** Where the SSE-S3 encryption keys are stored. The only valid choice here is HashiCorp Vault ('vault').

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_backend vault
ceph config get client.rgw rgw_crypt_sse_s3_backend
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["vault"].
2. Default `vault` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_key_template

| | |
|---|---|
| 类型 | Str · default `%bucket_id` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_key_template](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_key_template) |

**作用：** template for per-bucket SSE-S3 keys in Vault.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_key_template %bucket_id
ceph config get client.rgw rgw_crypt_sse_s3_key_template
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `%bucket_id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_addr) |

**作用：** SSE-S3 Vault server base address.

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_sse_s3_vault_addr
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

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
| 类型 | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_auth) |

**作用：** Type of authentication method to be used with SSE-S3 and Vault.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_auth token
ceph config get client.rgw rgw_crypt_sse_s3_vault_auth
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_sse_s3_vault_namespace

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_namespace) |

**作用：** Vault Namespace to be used to select your tenant

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_namespace <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_namespace
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_prefix) |

**作用：** SSE-S3 Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_prefix <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_prefix
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `transit` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine) |

**作用：** Vault Secret Engine to be used to retrieve encryption keys.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_sse_s3_vault_secret_engine
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_sse_s3_vault_ssl_cacert

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert) |

**作用：** Path for custom ca certificate for accessing vault server

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_cacert
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert) |

**作用：** Path for custom client certificate for accessing vault server

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey) |

**作用：** Path for private key required for client cert

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_token_file) |

**作用：** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_sse_s3_vault_token_file
```

**寻找最优值：**

**调优模型：** Capacity

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl) |

**作用：** Should RGW verify the vault server SSL certificate.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_sse_s3_vault_verify_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_crypt_suppress_logs

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_suppress_logs](../../../config/rgw/rgw.md#SP_rgw_crypt_suppress_logs) |

**作用：** Suppress logs that might print client key

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_suppress_logs false
ceph config get client.rgw rgw_crypt_suppress_logs
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_crypt_vault_addr

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_addr](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_addr) |

**作用：** Vault server base address.

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_addr "192.0.2.10:7480"
ceph config get client.rgw rgw_crypt_vault_addr
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

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
| 类型 | Str · enum: ["token", "agent"] · default `token` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_auth](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_auth) |

**作用：** Type of authentication method to be used with Vault.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_auth token
ceph config get client.rgw rgw_crypt_vault_auth
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["token", "agent"].
2. Default `token` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_crypt_vault_namespace

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_namespace](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_namespace) |

**作用：** Vault Namespace to be used to select your tenant

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_namespace <value>
ceph config get client.rgw rgw_crypt_vault_namespace
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_prefix](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_prefix) |

**作用：** Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_prefix <value>
ceph config get client.rgw rgw_crypt_vault_prefix
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `transit` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_secret_engine](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_secret_engine) |

**作用：** Vault Secret Engine to be used to retrieve encryption keys.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_vault_secret_engine
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_crypt_vault_ssl_cacert

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_ssl_cacert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_cacert) |

**作用：** Path for custom ca certificate for accessing vault server

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_cacert
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_ssl_clientcert](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientcert) |

**作用：** Path for custom client certificate for accessing vault server

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientcert
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_ssl_clientkey](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientkey) |

**作用：** Path for private key required for client cert

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientkey
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_token_file](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_token_file) |

**作用：** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_token_file "/etc/ceph/rgw-vault-token"
ceph config get client.rgw rgw_crypt_vault_token_file
```

**寻找最优值：**

**调优模型：** Capacity

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_crypt_vault_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_crypt_vault_verify_ssl) |

**作用：** Should RGW verify the vault server SSL certificate.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_crypt_vault_verify_ssl false
ceph config get client.rgw rgw_crypt_vault_verify_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← RGW 配置概览](../OVERVIEW.md)
