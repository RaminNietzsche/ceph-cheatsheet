# API limits & policies

RGW config deep dive — 6 options. [← RGW config overview](OVERVIEW.md) · [Curated batch 1](../rgw-config-options.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | Policy |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | Policy |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | Policy |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | Policy |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | Policy |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced | Policy |

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

### rgw_acl_grants_max_num

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_acl_grants_max_num](../../config/rgw/rgw.md#SP_rgw_acl_grants_max_num) |

**What it does:** The maximum number of ACL grants in a single request.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_acl_grants_max_num 100
ceph config get client.rgw rgw_acl_grants_max_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_admin_entry

| | |
|---|---|
| Type | Str · default `admin` · **Advanced** |
| Table | [rgw.md#SP_rgw_admin_entry](../../config/rgw/rgw.md#SP_rgw_admin_entry) |

**What it does:** Path prefix to be used for accessing RGW RESTful admin API.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_admin_entry admin
ceph config get client.rgw rgw_admin_entry
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`admin`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_cors_rules_max_num

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_cors_rules_max_num](../../config/rgw/rgw.md#SP_rgw_cors_rules_max_num) |

**What it does:** The maximum number of CORS rules in a single request.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_cors_rules_max_num 100
ceph config get client.rgw rgw_cors_rules_max_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_policy_reject_invalid_principals

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [rgw.md#SP_rgw_policy_reject_invalid_principals](../../config/rgw/rgw.md#SP_rgw_policy_reject_invalid_principals) |

**What it does:** Whether to reject policies with invalid principals

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_policy_reject_invalid_principals True
ceph config get client.rgw rgw_policy_reject_invalid_principals
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_topic_require_publish_policy

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [rgw.md#SP_rgw_topic_require_publish_policy](../../config/rgw/rgw.md#SP_rgw_topic_require_publish_policy) |

**What it does:** Whether to validate user permissions to publish notifications to topics.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_topic_require_publish_policy False
ceph config get client.rgw rgw_topic_require_publish_policy
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_website_routing_rules_max_num

| | |
|---|---|
| Type | Int · default `50` · **Advanced** |
| Table | [rgw.md#SP_rgw_website_routing_rules_max_num](../../config/rgw/rgw.md#SP_rgw_website_routing_rules_max_num) |

**What it does:** The maximum number of website routing rules in a single request.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_website_routing_rules_max_num 50
ceph config get client.rgw rgw_website_routing_rules_max_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `50` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW config overview](OVERVIEW.md)
