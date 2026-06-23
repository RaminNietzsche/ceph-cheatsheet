# Encryption and KMS

RGW config deep dive — 42 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_crypt_default_encryption_key](#rgw_crypt_default_encryption_key) | `(empty)` | Dev |
| [rgw_crypt_kmip_addr](#rgw_crypt_kmip_addr) | `(empty)` | Advanced |
| [rgw_crypt_kmip_ca_path](#rgw_crypt_kmip_ca_path) | `(empty)` | Advanced |
| [rgw_crypt_kmip_client_cert](#rgw_crypt_kmip_client_cert) | `(empty)` | Advanced |
| [rgw_crypt_kmip_client_key](#rgw_crypt_kmip_client_key) | `(empty)` | Advanced |
| [rgw_crypt_kmip_kms_key_template](#rgw_crypt_kmip_kms_key_template) | `(empty)` | Advanced |
| [rgw_crypt_kmip_password](#rgw_crypt_kmip_password) | `(empty)` | Advanced |
| [rgw_crypt_kmip_s3_key_template](#rgw_crypt_kmip_s3_key_template) | `$keyid` | Advanced |
| [rgw_crypt_kmip_username](#rgw_crypt_kmip_username) | `(empty)` | Advanced |
| [rgw_crypt_require_ssl](#rgw_crypt_require_ssl) | `True` | Advanced |
| [rgw_crypt_s3_kms_backend](#rgw_crypt_s3_kms_backend) | `barbican` | Advanced |
| [rgw_crypt_s3_kms_cache_enabled](#rgw_crypt_s3_kms_cache_enabled) | `True` | Advanced |
| [rgw_crypt_s3_kms_cache_max_size](#rgw_crypt_s3_kms_cache_max_size) | `128` | Advanced |
| [rgw_crypt_s3_kms_cache_negative_ttl](#rgw_crypt_s3_kms_cache_negative_ttl) | `120` | Advanced |
| [rgw_crypt_s3_kms_cache_positive_ttl](#rgw_crypt_s3_kms_cache_positive_ttl) | `60` | Advanced |
| [rgw_crypt_s3_kms_cache_transient_error_ttl](#rgw_crypt_s3_kms_cache_transient_error_ttl) | `10` | Advanced |
| [rgw_crypt_s3_kms_encryption_keys](#rgw_crypt_s3_kms_encryption_keys) | `(empty)` | Dev |
| [rgw_crypt_s3_kms_testing_delay](#rgw_crypt_s3_kms_testing_delay) | `0` | Dev |
| [rgw_crypt_sse_algorithm](#rgw_crypt_sse_algorithm) | `aes-256-cbc` | Advanced |
| [rgw_crypt_sse_s3_backend](#rgw_crypt_sse_s3_backend) | `vault` | Advanced |
| [rgw_crypt_sse_s3_key_template](#rgw_crypt_sse_s3_key_template) | `%bucket_id` | Advanced |
| [rgw_crypt_sse_s3_vault_addr](#rgw_crypt_sse_s3_vault_addr) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_auth](#rgw_crypt_sse_s3_vault_auth) | `token` | Advanced |
| [rgw_crypt_sse_s3_vault_namespace](#rgw_crypt_sse_s3_vault_namespace) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_prefix](#rgw_crypt_sse_s3_vault_prefix) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_secret_engine](#rgw_crypt_sse_s3_vault_secret_engine) | `transit` | Advanced |
| [rgw_crypt_sse_s3_vault_ssl_cacert](#rgw_crypt_sse_s3_vault_ssl_cacert) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_ssl_clientcert](#rgw_crypt_sse_s3_vault_ssl_clientcert) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_ssl_clientkey](#rgw_crypt_sse_s3_vault_ssl_clientkey) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_token_file](#rgw_crypt_sse_s3_vault_token_file) | `(empty)` | Advanced |
| [rgw_crypt_sse_s3_vault_verify_ssl](#rgw_crypt_sse_s3_vault_verify_ssl) | `True` | Advanced |
| [rgw_crypt_suppress_logs](#rgw_crypt_suppress_logs) | `True` | Advanced |
| [rgw_crypt_vault_addr](#rgw_crypt_vault_addr) | `(empty)` | Advanced |
| [rgw_crypt_vault_auth](#rgw_crypt_vault_auth) | `token` | Advanced |
| [rgw_crypt_vault_namespace](#rgw_crypt_vault_namespace) | `(empty)` | Advanced |
| [rgw_crypt_vault_prefix](#rgw_crypt_vault_prefix) | `(empty)` | Advanced |
| [rgw_crypt_vault_secret_engine](#rgw_crypt_vault_secret_engine) | `transit` | Advanced |
| [rgw_crypt_vault_ssl_cacert](#rgw_crypt_vault_ssl_cacert) | `(empty)` | Advanced |
| [rgw_crypt_vault_ssl_clientcert](#rgw_crypt_vault_ssl_clientcert) | `(empty)` | Advanced |
| [rgw_crypt_vault_ssl_clientkey](#rgw_crypt_vault_ssl_clientkey) | `(empty)` | Advanced |
| [rgw_crypt_vault_token_file](#rgw_crypt_vault_token_file) | `(empty)` | Advanced |
| [rgw_crypt_vault_verify_ssl](#rgw_crypt_vault_verify_ssl) | `True` | Advanced |

---

### rgw_crypt_default_encryption_key

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_default_encryption_key](../../config/rgw/rgw.md#SP_rgw_crypt_default_encryption_key) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_default_encryption_key <value>
ceph config get client.rgw rgw_crypt_default_encryption_key
```

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_crypt_kmip_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_addr](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_addr) |

**What it does:** kmip server address

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_addr <value>
ceph config get client.rgw rgw_crypt_kmip_addr
```

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

---

### rgw_crypt_kmip_ca_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_ca_path](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_ca_path) |

**What it does:** ca for kmip servers

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_ca_path <value>
ceph config get client.rgw rgw_crypt_kmip_ca_path
```

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`(empty)`) is fine when that path is on a separate volume.

---

### rgw_crypt_kmip_client_cert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_client_cert](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_cert) |

**What it does:** connect using client certificate

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_cert <value>
ceph config get client.rgw rgw_crypt_kmip_client_cert
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_kmip_client_key

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_client_key](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_client_key) |

**What it does:** connect using client certificate

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_client_key <value>
ceph config get client.rgw rgw_crypt_kmip_client_key
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_kmip_kms_key_template

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_kms_key_template](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_kms_key_template) |

**What it does:** sse-kms; kmip key names

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_kms_key_template <value>
ceph config get client.rgw rgw_crypt_kmip_kms_key_template
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_kmip_password

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_password](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_password) |

**What it does:** optional w/ username

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_password <value>
ceph config get client.rgw rgw_crypt_kmip_password
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_kmip_s3_key_template

| | |
|---|---|
| Type | Str · default `$keyid` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_s3_key_template](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_s3_key_template) |

**What it does:** sse-s3; kmip key template

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_s3_key_template $keyid
ceph config get client.rgw rgw_crypt_kmip_s3_key_template
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_kmip_username

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_kmip_username](../../config/rgw/rgw.md#SP_rgw_crypt_kmip_username) |

**What it does:** when authenticating via username

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_kmip_username <value>
ceph config get client.rgw rgw_crypt_kmip_username
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_require_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_require_ssl](../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl) |

**What it does:** Requests including encryption key headers must be sent over ssl

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_require_ssl True
ceph config get client.rgw rgw_crypt_require_ssl
```

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

---

### rgw_crypt_s3_kms_backend

| | |
|---|---|
| Type | Str · default `barbican` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_backend](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_backend) |

**What it does:** Where the SSE-KMS encryption keys are stored. Supported KMS systems are OpenStack Barbican ('barbican', the default) and HashiCorp Vault ('vault').

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_backend barbican
ceph config get client.rgw rgw_crypt_s3_kms_backend
```

**Finding optimal value:** Choose from valid values ["barbican", "vault", "testing", "kmip"]. Default `barbican` is optimal unless your backend or integration requires another value.

---

### rgw_crypt_s3_kms_cache_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_enabled](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_enabled) |

**What it does:** Enable caching of encryption keys for SSE-KMS.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_enabled True
ceph config get client.rgw rgw_crypt_s3_kms_cache_enabled
```

**Finding optimal value:** Enable only when the related metrics or correctness path needs it. Default (`True`) is usually optimal for standard deployments.

---

### rgw_crypt_s3_kms_cache_max_size

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_max_size](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_max_size) |

**What it does:** Maximum number of SSE-KMS secrets cached. Each key consumes 32 byte (AES-256) + overhead in memory

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_max_size 128
ceph config get client.rgw rgw_crypt_s3_kms_cache_max_size
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`128`) while watching RGW RSS.

---

### rgw_crypt_s3_kms_cache_negative_ttl

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_negative_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts permanent look-up errors (e.g key does not exist).

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_negative_ttl 120
ceph config get client.rgw rgw_crypt_s3_kms_cache_negative_ttl
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`120`) while watching RGW RSS. Valid range: min=0, max=3600.

---

### rgw_crypt_s3_kms_cache_positive_ttl

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_positive_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts successful lookups.

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_positive_ttl 60
ceph config get client.rgw rgw_crypt_s3_kms_cache_positive_ttl
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`60`) while watching RGW RSS. Valid range: min=10, max=3600.

---

### rgw_crypt_s3_kms_cache_transient_error_ttl

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_cache_transient_error_ttl) |

**What it does:** Time in seconds after which the KMS cache evicts entries representing transient errors (timeouts, temporary outages, misconfiguration, etc).

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl 10
ceph config get client.rgw rgw_crypt_s3_kms_cache_transient_error_ttl
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`10`) while watching RGW RSS. Valid range: min=0, max=3600.

---

### rgw_crypt_s3_kms_encryption_keys

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_encryption_keys](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_encryption_keys) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_encryption_keys <value>
ceph config get client.rgw rgw_crypt_s3_kms_encryption_keys
```

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_crypt_s3_kms_testing_delay

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_crypt_s3_kms_testing_delay](../../config/rgw/rgw.md#SP_rgw_crypt_s3_kms_testing_delay) |

**What it does:** Add delay in milliseconds to the 'testing' KMS key retrieval.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_s3_kms_testing_delay 0
ceph config get client.rgw rgw_crypt_s3_kms_testing_delay
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_crypt_sse_algorithm

| | |
|---|---|
| Type | Str · default `aes-256-cbc` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_algorithm](../../config/rgw/rgw.md#SP_rgw_crypt_sse_algorithm) |

**What it does:** Default encryption algorithm for server-side encryption

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_algorithm aes-256-cbc
ceph config get client.rgw rgw_crypt_sse_algorithm
```

**Finding optimal value:** Choose from valid values ["aes-256-cbc", "aes-256-gcm"]. Default `aes-256-cbc` is optimal unless your backend or integration requires another value.

---

### rgw_crypt_sse_s3_backend

| | |
|---|---|
| Type | Str · default `vault` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_backend](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_backend) |

**What it does:** Where the SSE-S3 encryption keys are stored. The only valid choice here is HashiCorp Vault ('vault').

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_backend vault
ceph config get client.rgw rgw_crypt_sse_s3_backend
```

**Finding optimal value:** Choose from valid values ["vault"]. Default `vault` is optimal unless your backend or integration requires another value.

---

### rgw_crypt_sse_s3_key_template

| | |
|---|---|
| Type | Str · default `%bucket_id` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_key_template](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_key_template) |

**What it does:** template for per-bucket SSE-S3 keys in Vault.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_key_template %bucket_id
ceph config get client.rgw rgw_crypt_sse_s3_key_template
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_sse_s3_vault_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_addr](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_addr) |

**What it does:** SSE-S3 Vault server base address.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_addr <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_addr
```

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

---

### rgw_crypt_sse_s3_vault_auth

| | |
|---|---|
| Type | Str · default `token` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_auth](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_auth) |

**What it does:** Type of authentication method to be used with SSE-S3 and Vault.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_auth token
ceph config get client.rgw rgw_crypt_sse_s3_vault_auth
```

**Finding optimal value:** Choose from valid values ["token", "agent"]. Default `token` is optimal unless your backend or integration requires another value.

---

### rgw_crypt_sse_s3_vault_namespace

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_namespace](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_namespace) |

**What it does:** Vault Namespace to be used to select your tenant

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_namespace <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_namespace
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_sse_s3_vault_prefix

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_prefix](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_prefix) |

**What it does:** SSE-S3 Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_prefix <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_prefix
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_sse_s3_vault_secret_engine

| | |
|---|---|
| Type | Str · default `transit` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_secret_engine) |

**What it does:** Vault Secret Engine to be used to retrieve encryption keys.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_sse_s3_vault_secret_engine
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_sse_s3_vault_ssl_cacert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_cacert) |

**What it does:** Path for custom ca certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_cacert
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_sse_s3_vault_ssl_clientcert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientcert) |

**What it does:** Path for custom client certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientcert
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_sse_s3_vault_ssl_clientkey

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_ssl_clientkey) |

**What it does:** Path for private key required for client cert

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_ssl_clientkey
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_sse_s3_vault_token_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_token_file](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_token_file) |

**What it does:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_token_file <value>
ceph config get client.rgw rgw_crypt_sse_s3_vault_token_file
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_sse_s3_vault_verify_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl](../../config/rgw/rgw.md#SP_rgw_crypt_sse_s3_vault_verify_ssl) |

**What it does:** Should RGW verify the vault server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_sse_s3_vault_verify_ssl True
ceph config get client.rgw rgw_crypt_sse_s3_vault_verify_ssl
```

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

---

### rgw_crypt_suppress_logs

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_suppress_logs](../../config/rgw/rgw.md#SP_rgw_crypt_suppress_logs) |

**What it does:** Suppress logs that might print client key

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_suppress_logs True
ceph config get client.rgw rgw_crypt_suppress_logs
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgw_crypt_vault_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_addr](../../config/rgw/rgw.md#SP_rgw_crypt_vault_addr) |

**What it does:** Vault server base address.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_addr <value>
ceph config get client.rgw rgw_crypt_vault_addr
```

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

---

### rgw_crypt_vault_auth

| | |
|---|---|
| Type | Str · default `token` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_auth](../../config/rgw/rgw.md#SP_rgw_crypt_vault_auth) |

**What it does:** Type of authentication method to be used with Vault.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_auth token
ceph config get client.rgw rgw_crypt_vault_auth
```

**Finding optimal value:** Choose from valid values ["token", "agent"]. Default `token` is optimal unless your backend or integration requires another value.

---

### rgw_crypt_vault_namespace

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_namespace](../../config/rgw/rgw.md#SP_rgw_crypt_vault_namespace) |

**What it does:** Vault Namespace to be used to select your tenant

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_namespace <value>
ceph config get client.rgw rgw_crypt_vault_namespace
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_vault_prefix

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_prefix](../../config/rgw/rgw.md#SP_rgw_crypt_vault_prefix) |

**What it does:** Vault secret URL prefix, which can be used to restrict access to a particular subset of the Vault secret space.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_prefix <value>
ceph config get client.rgw rgw_crypt_vault_prefix
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_vault_secret_engine

| | |
|---|---|
| Type | Str · default `transit` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_secret_engine](../../config/rgw/rgw.md#SP_rgw_crypt_vault_secret_engine) |

**What it does:** Vault Secret Engine to be used to retrieve encryption keys.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_secret_engine transit
ceph config get client.rgw rgw_crypt_vault_secret_engine
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_vault_ssl_cacert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_cacert](../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_cacert) |

**What it does:** Path for custom ca certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_cacert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_cacert
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_vault_ssl_clientcert

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_clientcert](../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientcert) |

**What it does:** Path for custom client certificate for accessing vault server

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientcert <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientcert
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_crypt_vault_ssl_clientkey

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_ssl_clientkey](../../config/rgw/rgw.md#SP_rgw_crypt_vault_ssl_clientkey) |

**What it does:** Path for private key required for client cert

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_ssl_clientkey <value>
ceph config get client.rgw rgw_crypt_vault_ssl_clientkey
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_vault_token_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_token_file](../../config/rgw/rgw.md#SP_rgw_crypt_vault_token_file) |

**What it does:** If authentication method is 'token', provide a path to the token file, which for security reasons should readable only by Rados Gateway.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_token_file <value>
ceph config get client.rgw rgw_crypt_vault_token_file
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_crypt_vault_verify_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_crypt_vault_verify_ssl](../../config/rgw/rgw.md#SP_rgw_crypt_vault_verify_ssl) |

**What it does:** Should RGW verify the vault server SSL certificate.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_crypt_vault_verify_ssl True
ceph config get client.rgw rgw_crypt_vault_verify_ssl
```

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

---


[← RGW config overview](OVERVIEW.md)
