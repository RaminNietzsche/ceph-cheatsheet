# Swift API

RGW config deep dive — 11 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_swift_account_in_url

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_account_in_url](../../config/rgw/rgw.md#SP_rgw_swift_account_in_url) |

**What it does:** Swift account encoded in URL

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_swift_account_in_url False
ceph config get client.rgw rgw_swift_account_in_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`False`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_account_in_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_auth_entry

| | |
|---|---|
| Type | Str · default `auth` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_auth_entry](../../config/rgw/rgw.md#SP_rgw_swift_auth_entry) |

**What it does:** Swift auth URL prefix

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_swift_auth_entry auth
ceph config get client.rgw rgw_swift_auth_entry
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`auth`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_swift_auth_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_auth_url](../../config/rgw/rgw.md#SP_rgw_swift_auth_url) |

**What it does:** Swift auth URL

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_swift_auth_url <value>
ceph config get client.rgw rgw_swift_auth_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_auth_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_custom_header

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_custom_header](../../config/rgw/rgw.md#SP_rgw_swift_custom_header) |

**What it does:** Enable swift custom header

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_swift_custom_header <value>
ceph config get client.rgw rgw_swift_custom_header
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_custom_header
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_enforce_content_length

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_enforce_content_length](../../config/rgw/rgw.md#SP_rgw_swift_enforce_content_length) |

**What it does:** Send content length when listing containers (Swift)

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_swift_enforce_content_length False
ceph config get client.rgw rgw_swift_enforce_content_length
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_need_stats

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_need_stats](../../config/rgw/rgw.md#SP_rgw_swift_need_stats) |

**What it does:** Enable stats on bucket listing in Swift

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_swift_need_stats True
ceph config get client.rgw rgw_swift_need_stats
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_tenant_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_tenant_name](../../config/rgw/rgw.md#SP_rgw_swift_tenant_name) |

**What it does:** Swift tenant name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_swift_tenant_name <value>
ceph config get client.rgw rgw_swift_tenant_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_tenant_name
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_token_expiration

| | |
|---|---|
| Type | Int · default `1_day` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_token_expiration](../../config/rgw/rgw.md#SP_rgw_swift_token_expiration) |

**What it does:** Expiration time (in seconds) for token generated through RGW Swift auth.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_swift_token_expiration 1_day
ceph config get client.rgw rgw_swift_token_expiration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_day`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_token_expiration
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_url](../../config/rgw/rgw.md#SP_rgw_swift_url) |

**What it does:** Swift-auth storage URL

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_swift_url <value>
ceph config get client.rgw rgw_swift_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url_prefix

| | |
|---|---|
| Type | Str · default `swift` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_url_prefix](../../config/rgw/rgw.md#SP_rgw_swift_url_prefix) |

**What it does:** Swift URL prefix

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_swift_url_prefix swift
ceph config get client.rgw rgw_swift_url_prefix
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `swift`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_url_prefix
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_versioning_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_swift_versioning_enabled](../../config/rgw/rgw.md#SP_rgw_swift_versioning_enabled) |

**What it does:** Enable Swift versioning

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_swift_versioning_enabled False
ceph config get client.rgw rgw_swift_versioning_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](OVERVIEW.md)
