# HTTP compatibility

RGW config deep dive — 17 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
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

### rgw_content_length_compat

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_content_length_compat](../../../config/rgw/rgw.md#SP_rgw_content_length_compat) |

**What it does:** Multiple content length headers compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_content_length_compat true
ceph config get client.rgw rgw_content_length_compat
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_cross_domain_policy

| | |
|---|---|
| Type | Str · default `<allow-access-from domain="*" secure="false" />` · **Advanced** |
| Table | [rgw.md#SP_rgw_cross_domain_policy](../../../config/rgw/rgw.md#SP_rgw_cross_domain_policy) |

**What it does:** RGW handle cross domain policy

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_cross_domain_policy "<allow-access-from domain="*" secure="false" />"
ceph config get client.rgw rgw_cross_domain_policy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `<allow-access-from domain="*" secure="false" />`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_cross_domain_policy
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_defer_to_bucket_acls

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_defer_to_bucket_acls](../../../config/rgw/rgw.md#SP_rgw_defer_to_bucket_acls) |

**What it does:** Bucket ACLs override object ACLs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_defer_to_bucket_acls <value>
ceph config get client.rgw rgw_defer_to_bucket_acls
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_defer_to_bucket_acls
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_enforce_swift_acls

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enforce_swift_acls](../../../config/rgw/rgw.md#SP_rgw_enforce_swift_acls) |

**What it does:** RGW enforce swift acls

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enforce_swift_acls false
ceph config get client.rgw rgw_enforce_swift_acls
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_extended_http_attrs

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_extended_http_attrs](../../../config/rgw/rgw.md#SP_rgw_extended_http_attrs) |

**What it does:** RGW support extended HTTP attrs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_extended_http_attrs <value>
ceph config get client.rgw rgw_extended_http_attrs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_extended_http_attrs
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_ignore_get_invalid_range

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_ignore_get_invalid_range](../../../config/rgw/rgw.md#SP_rgw_ignore_get_invalid_range) |

**What it does:** Treat invalid (e.g., negative) range request as full

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_ignore_get_invalid_range true
ceph config get client.rgw rgw_ignore_get_invalid_range
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_continue

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_print_continue](../../../config/rgw/rgw.md#SP_rgw_print_continue) |

**What it does:** RGW support of 100-continue

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_print_continue false
ceph config get client.rgw rgw_print_continue
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_prohibited_content_length

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_print_prohibited_content_length](../../../config/rgw/rgw.md#SP_rgw_print_prohibited_content_length) |

**What it does:** RGW RFC-7230 compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_print_prohibited_content_length true
ceph config get client.rgw rgw_print_prohibited_content_length
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_region_enforcement

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_relaxed_region_enforcement](../../../config/rgw/rgw.md#SP_rgw_relaxed_region_enforcement) |

**What it does:** Disable region constraint enforcement

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_region_enforcement true
ceph config get client.rgw rgw_relaxed_region_enforcement
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_s3_bucket_names

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_relaxed_s3_bucket_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_s3_bucket_names) |

**What it does:** RGW enable relaxed S3 bucket names

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_s3_bucket_names true
ceph config get client.rgw rgw_relaxed_s3_bucket_names
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_topic_names

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_relaxed_topic_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_topic_names) |

**What it does:** RGW enable relaxed topic names

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_topic_names true
ceph config get client.rgw rgw_relaxed_topic_names
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_remote_addr_param

| | |
|---|---|
| Type | Str · default `REMOTE_ADDR` · **Advanced** |
| Table | [rgw.md#SP_rgw_remote_addr_param](../../../config/rgw/rgw.md#SP_rgw_remote_addr_param) |

**What it does:** HTTP header that holds the remote address in incoming requests.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_remote_addr_param REMOTE_ADDR
ceph config get client.rgw rgw_remote_addr_param
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `REMOTE_ADDR`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_remote_addr_param
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_request_uri

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_request_uri](../../../config/rgw/rgw.md#SP_rgw_request_uri) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_request_uri "https://service.example.com/"
ceph config get client.rgw rgw_request_uri
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
ceph config get client.rgw rgw_request_uri
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_resolve_cname

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_resolve_cname](../../../config/rgw/rgw.md#SP_rgw_resolve_cname) |

**What it does:** Support vanity domain names via CNAME

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_resolve_cname true
ceph config get client.rgw rgw_resolve_cname
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_service_provider_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_service_provider_name](../../../config/rgw/rgw.md#SP_rgw_service_provider_name) |

**What it does:** Service provider name which is contained in http response headers

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_service_provider_name <value>
ceph config get client.rgw rgw_service_provider_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_service_provider_name
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_trust_forwarded_https

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_trust_forwarded_https](../../../config/rgw/rgw.md#SP_rgw_trust_forwarded_https) |

**What it does:** Trust Forwarded and X-Forwarded-Proto headers

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_trust_forwarded_https true
ceph config get client.rgw rgw_trust_forwarded_https
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_verify_ssl

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_verify_ssl) |

**What it does:** Should RGW verify SSL when connecting to a remote HTTP server

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_verify_ssl false
ceph config get client.rgw rgw_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← RGW config overview](../OVERVIEW.md)
