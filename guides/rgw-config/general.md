# General RGW options

RGW config deep dive — 50 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_config_store](#rgw_config_store) | `rados` | Advanced |
| [rgw_content_length_compat](#rgw_content_length_compat) | `False` | Advanced |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced |
| [rgw_cross_domain_policy](#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Advanced |
| [rgw_data](#rgw_data) | `/var/lib/ceph/radosgw/$cluster-$id` | Advanced |
| [rgw_dedup_min_obj_size_for_dedup](#rgw_dedup_min_obj_size_for_dedup) | `64_K` | Advanced |
| [rgw_dedup_split_obj_head](#rgw_dedup_split_obj_head) | `True` | Advanced |
| [rgw_default_realm_info_oid](#rgw_default_realm_info_oid) | `default.realm` | Advanced |
| [rgw_default_region_info_oid](#rgw_default_region_info_oid) | `default.region` | Advanced |
| [rgw_default_zone_info_oid](#rgw_default_zone_info_oid) | `default.zone` | Advanced |
| [rgw_default_zonegroup_info_oid](#rgw_default_zonegroup_info_oid) | `default.zonegroup` | Advanced |
| [rgw_defer_to_bucket_acls](#rgw_defer_to_bucket_acls) | `(empty)` | Advanced |
| [rgw_enforce_swift_acls](#rgw_enforce_swift_acls) | `True` | Advanced |
| [rgw_expose_bucket](#rgw_expose_bucket) | `False` | Advanced |
| [rgw_extended_http_attrs](#rgw_extended_http_attrs) | `(empty)` | Advanced |
| [rgw_filter](#rgw_filter) | `none` | Advanced |
| [rgw_graceful_stop](#rgw_graceful_stop) | `False` | Advanced |
| [rgw_healthcheck_disabling_path](#rgw_healthcheck_disabling_path) | `(empty)` | Dev |
| [rgw_ignore_get_invalid_range](#rgw_ignore_get_invalid_range) | `False` | Advanced |
| [rgw_json_config](#rgw_json_config) | `/var/lib/ceph/radosgw/config.json` | Advanced |
| [rgw_lifecycle_work_time](#rgw_lifecycle_work_time) | `00:00-06:00` | Advanced |
| [rgw_mime_types_file](#rgw_mime_types_file) | `/etc/mime.types` | Basic |
| [rgw_mp_lock_max_time](#rgw_mp_lock_max_time) | `10_min` | Advanced |
| [rgw_numa_node](#rgw_numa_node) | `-1` | Advanced |
| [rgw_op_tracing](#rgw_op_tracing) | `False` | Advanced |
| [rgw_override_bucket_index_max_shards](#rgw_override_bucket_index_max_shards) | `0` | Dev |
| [rgw_parquet_buffer_size](#rgw_parquet_buffer_size) | `16_M` | Advanced |
| [rgw_pending_bucket_index_op_expiration](#rgw_pending_bucket_index_op_expiration) | `120` | Advanced |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic |
| [rgw_print_continue](#rgw_print_continue) | `True` | Advanced |
| [rgw_print_prohibited_content_length](#rgw_print_prohibited_content_length) | `False` | Advanced |
| [rgw_rados_pool_autoscale_bias](#rgw_rados_pool_autoscale_bias) | `4` | Advanced |
| [rgw_rados_pool_recovery_priority](#rgw_rados_pool_recovery_priority) | `5` | Advanced |
| [rgw_rados_tracing](#rgw_rados_tracing) | `False` | Advanced |
| [rgw_relaxed_region_enforcement](#rgw_relaxed_region_enforcement) | `False` | Advanced |
| [rgw_relaxed_s3_bucket_names](#rgw_relaxed_s3_bucket_names) | `False` | Advanced |
| [rgw_relaxed_topic_names](#rgw_relaxed_topic_names) | `False` | Advanced |
| [rgw_remote_addr_param](#rgw_remote_addr_param) | `REMOTE_ADDR` | Advanced |
| [rgw_request_uri](#rgw_request_uri) | `(empty)` | Dev |
| [rgw_resolve_cname](#rgw_resolve_cname) | `False` | Advanced |
| [rgw_restore_lock_max_time](#rgw_restore_lock_max_time) | `90` | Dev |
| [rgw_safe_max_objects_per_shard](#rgw_safe_max_objects_per_shard) | `102400` | Advanced |
| [rgw_script_uri](#rgw_script_uri) | `(empty)` | Dev |
| [rgw_service_provider_name](#rgw_service_provider_name) | `(empty)` | Advanced |
| [rgw_shard_warning_threshold](#rgw_shard_warning_threshold) | `90` | Advanced |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic |
| [rgw_trust_forwarded_https](#rgw_trust_forwarded_https) | `False` | Advanced |
| [rgw_use_opa_authz](#rgw_use_opa_authz) | `False` | Advanced |
| [rgw_verify_ssl](#rgw_verify_ssl) | `True` | Advanced |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced |

---

### rgw_config_store

| | |
|---|---|
| Type | Str · default `rados` · **Advanced** |
| Table | [rgw.md#SP_rgw_config_store](../../config/rgw/rgw.md#SP_rgw_config_store) |

**What it does:** Configuration storage backend

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_config_store rados
ceph config get client.rgw rgw_config_store
```

**Finding optimal value:** Choose from valid values ["rados", "dbstore", "json"]. Default `rados` is optimal unless your backend or integration requires another value.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`100`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Start from upstream default (`<allow-access-from domain="*" secure="false" />`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`/var/lib/ceph/radosgw/$cluster-$id`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`64_K`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`default.realm`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`default.region`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`default.zone`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`default.zonegroup`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Choose from valid values ["none", "base", "d4n"]. Default `none` is optimal unless your backend or integration requires another value.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`/var/lib/ceph/radosgw/config.json`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`00:00-06:00`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/etc/mime.types`) is fine when that path is on a separate volume.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`10_min`) matches S3 compatibility for most workloads. Valid range: min=2_min, max=—.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`-1`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Start from upstream default (`16_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`120`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`4`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`5`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `False`.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Start from upstream default (`REMOTE_ADDR`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Keep the upstream default (`90`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`102400`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`90`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `False`.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

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

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `True`.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`50`) matches S3 compatibility for most workloads.

---


[← RGW config overview](OVERVIEW.md)
