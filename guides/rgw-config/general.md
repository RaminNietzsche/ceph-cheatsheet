# General RGW options

RGW config deep dive — 54 options. [← RGW config overview](OVERVIEW.md) · [Curated batch 1](../rgw-config-options.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | Policy |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | Policy |
| [rgw_asio_assert_yielding](#rgw_asio_assert_yielding) | `False` | Dev | Dev |
| [rgw_barbican_url](#rgw_barbican_url) | `(empty)` | Advanced | Connectivity |
| [rgw_beast_enable_async](#rgw_beast_enable_async) | `True` | Dev | Policy |
| [rgw_content_length_compat](#rgw_content_length_compat) | `False` | Advanced | Policy |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | Policy |
| [rgw_cross_domain_policy](#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Advanced | Performance |
| [rgw_data](#rgw_data) | `/var/lib/ceph/radosgw/$cluster-$id` | Advanced | Performance |
| [rgw_dedup_min_obj_size_for_dedup](#rgw_dedup_min_obj_size_for_dedup) | `64_K` | Advanced | Performance |
| [rgw_dedup_split_obj_head](#rgw_dedup_split_obj_head) | `True` | Advanced | Policy |
| [rgw_default_realm_info_oid](#rgw_default_realm_info_oid) | `default.realm` | Advanced | Performance |
| [rgw_default_region_info_oid](#rgw_default_region_info_oid) | `default.region` | Advanced | Performance |
| [rgw_default_zone_info_oid](#rgw_default_zone_info_oid) | `default.zone` | Advanced | Performance |
| [rgw_default_zonegroup_info_oid](#rgw_default_zonegroup_info_oid) | `default.zonegroup` | Advanced | Performance |
| [rgw_defer_to_bucket_acls](#rgw_defer_to_bucket_acls) | `(empty)` | Advanced | Performance |
| [rgw_enforce_swift_acls](#rgw_enforce_swift_acls) | `True` | Advanced | Policy |
| [rgw_expose_bucket](#rgw_expose_bucket) | `False` | Advanced | Policy |
| [rgw_extended_http_attrs](#rgw_extended_http_attrs) | `(empty)` | Advanced | Performance |
| [rgw_filter](#rgw_filter) | `none` | Advanced | Architecture |
| [rgw_graceful_stop](#rgw_graceful_stop) | `False` | Advanced | Policy |
| [rgw_healthcheck_disabling_path](#rgw_healthcheck_disabling_path) | `(empty)` | Dev | Capacity |
| [rgw_ignore_get_invalid_range](#rgw_ignore_get_invalid_range) | `False` | Advanced | Policy |
| [rgw_json_config](#rgw_json_config) | `/var/lib/ceph/radosgw/config.json` | Advanced | Performance |
| [rgw_lifecycle_work_time](#rgw_lifecycle_work_time) | `00:00-06:00` | Advanced | Performance |
| [rgw_mime_types_file](#rgw_mime_types_file) | `/etc/mime.types` | Basic | Capacity |
| [rgw_mp_lock_max_time](#rgw_mp_lock_max_time) | `10_min` | Advanced | Policy |
| [rgw_numa_node](#rgw_numa_node) | `-1` | Advanced | Policy |
| [rgw_op_tracing](#rgw_op_tracing) | `False` | Advanced | Policy |
| [rgw_override_bucket_index_max_shards](#rgw_override_bucket_index_max_shards) | `0` | Dev | Policy |
| [rgw_parquet_buffer_size](#rgw_parquet_buffer_size) | `16_M` | Advanced | Performance |
| [rgw_pending_bucket_index_op_expiration](#rgw_pending_bucket_index_op_expiration) | `120` | Advanced | Performance |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | Policy |
| [rgw_print_continue](#rgw_print_continue) | `True` | Advanced | Policy |
| [rgw_print_prohibited_content_length](#rgw_print_prohibited_content_length) | `False` | Advanced | Policy |
| [rgw_rados_pool_autoscale_bias](#rgw_rados_pool_autoscale_bias) | `4` | Advanced | Performance |
| [rgw_rados_pool_recovery_priority](#rgw_rados_pool_recovery_priority) | `5` | Advanced | Performance |
| [rgw_rados_tracing](#rgw_rados_tracing) | `False` | Advanced | Policy |
| [rgw_relaxed_region_enforcement](#rgw_relaxed_region_enforcement) | `False` | Advanced | Policy |
| [rgw_relaxed_s3_bucket_names](#rgw_relaxed_s3_bucket_names) | `False` | Advanced | Policy |
| [rgw_relaxed_topic_names](#rgw_relaxed_topic_names) | `False` | Advanced | Policy |
| [rgw_remote_addr_param](#rgw_remote_addr_param) | `REMOTE_ADDR` | Advanced | Performance |
| [rgw_request_uri](#rgw_request_uri) | `(empty)` | Dev | Connectivity |
| [rgw_resolve_cname](#rgw_resolve_cname) | `False` | Advanced | Policy |
| [rgw_restore_lock_max_time](#rgw_restore_lock_max_time) | `90` | Dev | Policy |
| [rgw_safe_max_objects_per_shard](#rgw_safe_max_objects_per_shard) | `102400` | Advanced | Policy |
| [rgw_script_uri](#rgw_script_uri) | `(empty)` | Dev | Connectivity |
| [rgw_service_provider_name](#rgw_service_provider_name) | `(empty)` | Advanced | Performance |
| [rgw_shard_warning_threshold](#rgw_shard_warning_threshold) | `90` | Advanced | Performance |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | Policy |
| [rgw_trust_forwarded_https](#rgw_trust_forwarded_https) | `False` | Advanced | Policy |
| [rgw_use_opa_authz](#rgw_use_opa_authz) | `False` | Advanced | Policy |
| [rgw_verify_ssl](#rgw_verify_ssl) | `True` | Advanced | Policy |
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

### rgw_asio_assert_yielding

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_asio_assert_yielding](../../config/rgw/rgw.md#SP_rgw_asio_assert_yielding) |

**What it does:** Trigger an assertion failure if an operation would block an asio thread

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_asio_assert_yielding False
ceph config get client.rgw rgw_asio_assert_yielding
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_barbican_url

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_barbican_url](../../config/rgw/rgw.md#SP_rgw_barbican_url) |

**What it does:** URL to barbican server.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw rgw_barbican_url <value>
ceph config get client.rgw rgw_barbican_url
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_barbican_url
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_beast_enable_async

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rgw.md#SP_rgw_beast_enable_async](../../config/rgw/rgw.md#SP_rgw_beast_enable_async) |

**What it does:** Enable async request processing under beast using coroutines

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_beast_enable_async True
ceph config get client.rgw rgw_beast_enable_async
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_content_length_compat

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_content_length_compat](../../config/rgw/rgw.md#SP_rgw_content_length_compat) |

**What it does:** Multiple content length headers compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_content_length_compat False
ceph config get client.rgw rgw_content_length_compat
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

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

### rgw_cross_domain_policy

| | |
|---|---|
| Type | Str · default `<allow-access-from domain="*" secure="false" />` · **Advanced** |
| Table | [rgw.md#SP_rgw_cross_domain_policy](../../config/rgw/rgw.md#SP_rgw_cross_domain_policy) |

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

### rgw_data

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw/$cluster-$id` · **Advanced** |
| Table | [rgw.md#SP_rgw_data](../../config/rgw/rgw.md#SP_rgw_data) |

**What it does:** Alternative location for RGW configuration.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_data "/var/lib/ceph/radosgw/$cluster-$id"
ceph config get client.rgw rgw_data
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_min_obj_size_for_dedup

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [rgw.md#SP_rgw_dedup_min_obj_size_for_dedup](../../config/rgw/rgw.md#SP_rgw_dedup_min_obj_size_for_dedup) |

**What it does:** The minimum RGW object size for dedup (0 means no minimum size for dedup).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dedup_min_obj_size_for_dedup 64_K
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_split_obj_head

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_dedup_split_obj_head](../../config/rgw/rgw.md#SP_rgw_dedup_split_obj_head) |

**What it does:** Enables the split-head functionality

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_dedup_split_obj_head True
ceph config get client.rgw rgw_dedup_split_obj_head
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_default_realm_info_oid

| | |
|---|---|
| Type | Str · default `default.realm` · **Advanced** |
| Table | [rgw.md#SP_rgw_default_realm_info_oid](../../config/rgw/rgw.md#SP_rgw_default_realm_info_oid) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_default_realm_info_oid default.realm
ceph config get client.rgw rgw_default_realm_info_oid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default.realm`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_realm_info_oid
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_default_region_info_oid

| | |
|---|---|
| Type | Str · default `default.region` · **Advanced** |
| Table | [rgw.md#SP_rgw_default_region_info_oid](../../config/rgw/rgw.md#SP_rgw_default_region_info_oid) |

**What it does:** Default region info object id

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_default_region_info_oid default.region
ceph config get client.rgw rgw_default_region_info_oid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default.region`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_region_info_oid
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zone_info_oid

| | |
|---|---|
| Type | Str · default `default.zone` · **Advanced** |
| Table | [rgw.md#SP_rgw_default_zone_info_oid](../../config/rgw/rgw.md#SP_rgw_default_zone_info_oid) |

**What it does:** Default zone info object id

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_default_zone_info_oid default.zone
ceph config get client.rgw rgw_default_zone_info_oid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default.zone`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zone_info_oid
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zonegroup_info_oid

| | |
|---|---|
| Type | Str · default `default.zonegroup` · **Advanced** |
| Table | [rgw.md#SP_rgw_default_zonegroup_info_oid](../../config/rgw/rgw.md#SP_rgw_default_zonegroup_info_oid) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_default_zonegroup_info_oid default.zonegroup
ceph config get client.rgw rgw_default_zonegroup_info_oid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default.zonegroup`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zonegroup_info_oid
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_defer_to_bucket_acls

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_defer_to_bucket_acls](../../config/rgw/rgw.md#SP_rgw_defer_to_bucket_acls) |

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
| Table | [rgw.md#SP_rgw_enforce_swift_acls](../../config/rgw/rgw.md#SP_rgw_enforce_swift_acls) |

**What it does:** RGW enforce swift acls

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enforce_swift_acls True
ceph config get client.rgw rgw_enforce_swift_acls
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_expose_bucket

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_expose_bucket](../../config/rgw/rgw.md#SP_rgw_expose_bucket) |

**What it does:** Send Bucket HTTP header with the response

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_expose_bucket False
ceph config get client.rgw rgw_expose_bucket
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_extended_http_attrs

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_extended_http_attrs](../../config/rgw/rgw.md#SP_rgw_extended_http_attrs) |

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

### rgw_filter

| | |
|---|---|
| Type | Str · default `none` · **Advanced** |
| Table | [rgw.md#SP_rgw_filter](../../config/rgw/rgw.md#SP_rgw_filter) |

**What it does:** experimental Option to set a filter

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_filter none
ceph config get client.rgw rgw_filter
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["none", "base", "d4n"].
2. Default `none` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_graceful_stop

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_graceful_stop](../../config/rgw/rgw.md#SP_rgw_graceful_stop) |

**What it does:** Delay the shutdown until all outstanding requests have completed

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_graceful_stop False
ceph config get client.rgw rgw_graceful_stop
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_healthcheck_disabling_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_healthcheck_disabling_path](../../config/rgw/rgw.md#SP_rgw_healthcheck_disabling_path) |

**What it does:** Swift health check api can be disabled if a file can be accessed in this path.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_healthcheck_disabling_path <value>
ceph config get client.rgw rgw_healthcheck_disabling_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_healthcheck_disabling_path)
iostat -x 5  # disk saturation
```

---

### rgw_ignore_get_invalid_range

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_ignore_get_invalid_range](../../config/rgw/rgw.md#SP_rgw_ignore_get_invalid_range) |

**What it does:** Treat invalid (e.g., negative) range request as full

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_ignore_get_invalid_range False
ceph config get client.rgw rgw_ignore_get_invalid_range
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_json_config

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw/config.json` · **Advanced** |
| Table | [rgw.md#SP_rgw_json_config](../../config/rgw/rgw.md#SP_rgw_json_config) |

**What it does:** Path to a json file that contains the static zone and zonegroup configuration. Requires rgw_config_store=json.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_json_config "/var/lib/ceph/radosgw/config.json"
ceph config get client.rgw rgw_json_config
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/config.json`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_json_config
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_lifecycle_work_time

| | |
|---|---|
| Type | Str · default `00:00-06:00` · **Advanced** |
| Table | [rgw.md#SP_rgw_lifecycle_work_time](../../config/rgw/rgw.md#SP_rgw_lifecycle_work_time) |

**What it does:** Lifecycle allowed work time

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_lifecycle_work_time 00:00-06:00
ceph config get client.rgw rgw_lifecycle_work_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `00:00-06:00`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lifecycle_work_time
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_mime_types_file

| | |
|---|---|
| Type | Str · default `/etc/mime.types` · **Basic** |
| Table | [rgw.md#SP_rgw_mime_types_file](../../config/rgw/rgw.md#SP_rgw_mime_types_file) |

**What it does:** Path to local mime types file

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_mime_types_file "/etc/mime.types"
ceph config get client.rgw rgw_mime_types_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/etc/mime.types`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_mime_types_file)
iostat -x 5  # disk saturation
```

---

### rgw_mp_lock_max_time

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_mp_lock_max_time](../../config/rgw/rgw.md#SP_rgw_mp_lock_max_time) |

**What it does:** Multipart upload max completion time

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_mp_lock_max_time 10_min
ceph config get client.rgw rgw_mp_lock_max_time
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `10_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**Bounds:** min `2_min`, max `—`.

---

### rgw_numa_node

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_numa_node](../../config/rgw/rgw.md#SP_rgw_numa_node) |

**What it does:** set the RGW daemon's CPU affinity to a NUMA node (-1 for none)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_numa_node -1
ceph config get client.rgw rgw_numa_node
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_op_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_op_tracing](../../config/rgw/rgw.md#SP_rgw_op_tracing) |

**What it does:** Enables LTTng-UST operator tracepoints.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_op_tracing False
ceph config get client.rgw rgw_op_tracing
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_override_bucket_index_max_shards

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_override_bucket_index_max_shards](../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards) |

**What it does:** The default number of bucket index shards for newly-created buckets. This value overrides bucket_index_max_shards stored in the zone. Setting this value in the zone is preferred, because it applies globally to all radosgw daemons running in the zone.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_override_bucket_index_max_shards 0
ceph config get client.rgw rgw_override_bucket_index_max_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_parquet_buffer_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_parquet_buffer_size](../../config/rgw/rgw.md#SP_rgw_parquet_buffer_size) |

**What it does:** the Maximum parquet buffer size, a limit to memory consumption for parquet reading operations.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_parquet_buffer_size 16_M
ceph config get client.rgw rgw_parquet_buffer_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_parquet_buffer_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_pending_bucket_index_op_expiration

| | |
|---|---|
| Type | Uint · default `120` · **Advanced** |
| Table | [rgw.md#SP_rgw_pending_bucket_index_op_expiration](../../config/rgw/rgw.md#SP_rgw_pending_bucket_index_op_expiration) |

**What it does:** Number of seconds a pending operation can remain in bucket index shard.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_pending_bucket_index_op_expiration 120
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

### rgw_print_continue

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_print_continue](../../config/rgw/rgw.md#SP_rgw_print_continue) |

**What it does:** RGW support of 100-continue

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_print_continue True
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
| Table | [rgw.md#SP_rgw_print_prohibited_content_length](../../config/rgw/rgw.md#SP_rgw_print_prohibited_content_length) |

**What it does:** RGW RFC-7230 compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_print_prohibited_content_length False
ceph config get client.rgw rgw_print_prohibited_content_length
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_rados_pool_autoscale_bias

| | |
|---|---|
| Type | Float · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_rados_pool_autoscale_bias](../../config/rgw/rgw.md#SP_rgw_rados_pool_autoscale_bias) |

**What it does:** pg_autoscale_bias value for RGW metadata (omap-heavy) pools

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_rados_pool_autoscale_bias 4
ceph config get client.rgw rgw_rados_pool_autoscale_bias
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_autoscale_bias
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0.01`, max `100000`.

---

### rgw_rados_pool_recovery_priority

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rgw.md#SP_rgw_rados_pool_recovery_priority](../../config/rgw/rgw.md#SP_rgw_rados_pool_recovery_priority) |

**What it does:** recovery_priority value for RGW metadata (omap-heavy) pools

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_rados_pool_recovery_priority 5
ceph config get client.rgw rgw_rados_pool_recovery_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_recovery_priority
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `-10`, max `10`.

---

### rgw_rados_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rados_tracing](../../config/rgw/rgw.md#SP_rgw_rados_tracing) |

**What it does:** Enables LTTng-UST tracepoints.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rados_tracing False
ceph config get client.rgw rgw_rados_tracing
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
| Table | [rgw.md#SP_rgw_relaxed_region_enforcement](../../config/rgw/rgw.md#SP_rgw_relaxed_region_enforcement) |

**What it does:** Disable region constraint enforcement

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_region_enforcement False
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
| Table | [rgw.md#SP_rgw_relaxed_s3_bucket_names](../../config/rgw/rgw.md#SP_rgw_relaxed_s3_bucket_names) |

**What it does:** RGW enable relaxed S3 bucket names

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_s3_bucket_names False
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
| Table | [rgw.md#SP_rgw_relaxed_topic_names](../../config/rgw/rgw.md#SP_rgw_relaxed_topic_names) |

**What it does:** RGW enable relaxed topic names

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_relaxed_topic_names False
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
| Table | [rgw.md#SP_rgw_remote_addr_param](../../config/rgw/rgw.md#SP_rgw_remote_addr_param) |

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
| Table | [rgw.md#SP_rgw_request_uri](../../config/rgw/rgw.md#SP_rgw_request_uri) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_request_uri <value>
ceph config get client.rgw rgw_request_uri
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
| Table | [rgw.md#SP_rgw_resolve_cname](../../config/rgw/rgw.md#SP_rgw_resolve_cname) |

**What it does:** Support vanity domain names via CNAME

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_resolve_cname False
ceph config get client.rgw rgw_resolve_cname
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_restore_lock_max_time

| | |
|---|---|
| Type | Int · default `90` · **Dev** |
| Table | [rgw.md#SP_rgw_restore_lock_max_time](../../config/rgw/rgw.md#SP_rgw_restore_lock_max_time) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_restore_lock_max_time 90
ceph config get client.rgw rgw_restore_lock_max_time
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `90` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_safe_max_objects_per_shard

| | |
|---|---|
| Type | Int · default `102400` · **Advanced** |
| Table | [rgw.md#SP_rgw_safe_max_objects_per_shard](../../config/rgw/rgw.md#SP_rgw_safe_max_objects_per_shard) |

**What it does:** Safe number of objects per shard

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_safe_max_objects_per_shard 102400
ceph config get client.rgw rgw_safe_max_objects_per_shard
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `102400` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_script_uri

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_script_uri](../../config/rgw/rgw.md#SP_rgw_script_uri) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_script_uri <value>
ceph config get client.rgw rgw_script_uri
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_script_uri
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_service_provider_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_service_provider_name](../../config/rgw/rgw.md#SP_rgw_service_provider_name) |

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

### rgw_shard_warning_threshold

| | |
|---|---|
| Type | Float · default `90` · **Advanced** |
| Table | [rgw.md#SP_rgw_shard_warning_threshold](../../config/rgw/rgw.md#SP_rgw_shard_warning_threshold) |

**What it does:** Warn about max objects per shard

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_shard_warning_threshold 90
ceph config get client.rgw rgw_shard_warning_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `90`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_shard_warning_threshold
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

### rgw_trust_forwarded_https

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_trust_forwarded_https](../../config/rgw/rgw.md#SP_rgw_trust_forwarded_https) |

**What it does:** Trust Forwarded and X-Forwarded-Proto headers

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_trust_forwarded_https False
ceph config get client.rgw rgw_trust_forwarded_https
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_use_opa_authz

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_use_opa_authz](../../config/rgw/rgw.md#SP_rgw_use_opa_authz) |

**What it does:** Should OPA be used to authorize client requests.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_use_opa_authz False
ceph config get client.rgw rgw_use_opa_authz
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
| Table | [rgw.md#SP_rgw_verify_ssl](../../config/rgw/rgw.md#SP_rgw_verify_ssl) |

**What it does:** Should RGW verify SSL when connecting to a remote HTTP server

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_verify_ssl True
ceph config get client.rgw rgw_verify_ssl
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`True` for most security options).
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
