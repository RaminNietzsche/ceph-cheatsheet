# Swift API

RGW config deep dive — 11 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_swift_account_in_url](#rgw_swift_account_in_url) | `False` | Advanced |
| [rgw_swift_auth_entry](#rgw_swift_auth_entry) | `auth` | Advanced |
| [rgw_swift_auth_url](#rgw_swift_auth_url) | `(empty)` | Advanced |
| [rgw_swift_custom_header](#rgw_swift_custom_header) | `(empty)` | Advanced |
| [rgw_swift_enforce_content_length](#rgw_swift_enforce_content_length) | `False` | Advanced |
| [rgw_swift_need_stats](#rgw_swift_need_stats) | `True` | Advanced |
| [rgw_swift_tenant_name](#rgw_swift_tenant_name) | `(empty)` | Advanced |
| [rgw_swift_token_expiration](#rgw_swift_token_expiration) | `1_day` | Advanced |
| [rgw_swift_url](#rgw_swift_url) | `(empty)` | Advanced |
| [rgw_swift_url_prefix](#rgw_swift_url_prefix) | `swift` | Advanced |
| [rgw_swift_versioning_enabled](#rgw_swift_versioning_enabled) | `False` | Advanced |

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

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`False`) if the integration is unused.

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

**Finding optimal value:** Start from upstream default (`auth`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

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

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `False`.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

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

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`(empty)`) if the integration is unused.

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

**Finding optimal value:** Start from upstream default (`swift`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Enable when the feature is required; otherwise keep default (`False`) to minimize background threads and memory.

---


[← RGW config overview](OVERVIEW.md)
