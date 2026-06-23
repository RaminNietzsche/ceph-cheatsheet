# Core runtime

RGW config deep dive — 16 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_data](#rgw_data) | `/var/lib/ceph/radosgw/$cluster-$id` | Advanced | Performance |
| [rgw_dedup_min_obj_size_for_dedup](#rgw_dedup_min_obj_size_for_dedup) | `64_K` | Advanced | Performance |
| [rgw_dedup_split_obj_head](#rgw_dedup_split_obj_head) | `True` | Advanced | Policy |
| [rgw_expose_bucket](#rgw_expose_bucket) | `False` | Advanced | Policy |
| [rgw_filter](#rgw_filter) | `none` | Advanced | Architecture |
| [rgw_graceful_stop](#rgw_graceful_stop) | `False` | Advanced | Policy |
| [rgw_healthcheck_disabling_path](#rgw_healthcheck_disabling_path) | `(empty)` | Dev | Capacity |
| [rgw_json_config](#rgw_json_config) | `/var/lib/ceph/radosgw/config.json` | Advanced | Performance |
| [rgw_mime_types_file](#rgw_mime_types_file) | `/etc/mime.types` | Basic | Capacity |
| [rgw_numa_node](#rgw_numa_node) | `-1` | Advanced | Policy |
| [rgw_op_tracing](#rgw_op_tracing) | `False` | Advanced | Policy |
| [rgw_parquet_buffer_size](#rgw_parquet_buffer_size) | `16_M` | Advanced | Performance |
| [rgw_rados_pool_autoscale_bias](#rgw_rados_pool_autoscale_bias) | `4` | Advanced | Performance |
| [rgw_rados_pool_recovery_priority](#rgw_rados_pool_recovery_priority) | `5` | Advanced | Performance |
| [rgw_rados_tracing](#rgw_rados_tracing) | `False` | Advanced | Policy |
| [rgw_script_uri](#rgw_script_uri) | `(empty)` | Dev | Connectivity |

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

### rgw_data

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw/$cluster-$id` · **Advanced** |
| Table | [rgw.md#SP_rgw_data](../../../config/rgw/rgw.md#SP_rgw_data) |

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
| Table | [rgw.md#SP_rgw_dedup_min_obj_size_for_dedup](../../../config/rgw/rgw.md#SP_rgw_dedup_min_obj_size_for_dedup) |

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
| Table | [rgw.md#SP_rgw_dedup_split_obj_head](../../../config/rgw/rgw.md#SP_rgw_dedup_split_obj_head) |

**What it does:** Enables the split-head functionality

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_dedup_split_obj_head false
ceph config get client.rgw rgw_dedup_split_obj_head
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
| Table | [rgw.md#SP_rgw_expose_bucket](../../../config/rgw/rgw.md#SP_rgw_expose_bucket) |

**What it does:** Send Bucket HTTP header with the response

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_expose_bucket true
ceph config get client.rgw rgw_expose_bucket
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_filter

| | |
|---|---|
| Type | Str · enum: ["none", "base", "d4n"] · default `none` · **Advanced** |
| Table | [rgw.md#SP_rgw_filter](../../../config/rgw/rgw.md#SP_rgw_filter) |

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
| Table | [rgw.md#SP_rgw_graceful_stop](../../../config/rgw/rgw.md#SP_rgw_graceful_stop) |

**What it does:** Delay the shutdown until all outstanding requests have completed

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_graceful_stop true
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
| Table | [rgw.md#SP_rgw_healthcheck_disabling_path](../../../config/rgw/rgw.md#SP_rgw_healthcheck_disabling_path) |

**What it does:** Swift health check api can be disabled if a file can be accessed in this path.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_healthcheck_disabling_path "/var/lib/ceph/radosgw"
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

### rgw_json_config

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw/config.json` · **Advanced** |
| Table | [rgw.md#SP_rgw_json_config](../../../config/rgw/rgw.md#SP_rgw_json_config) |

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

### rgw_mime_types_file

| | |
|---|---|
| Type | Str · default `/etc/mime.types` · **Basic** |
| Table | [rgw.md#SP_rgw_mime_types_file](../../../config/rgw/rgw.md#SP_rgw_mime_types_file) |

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

### rgw_numa_node

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_numa_node](../../../config/rgw/rgw.md#SP_rgw_numa_node) |

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
| Table | [rgw.md#SP_rgw_op_tracing](../../../config/rgw/rgw.md#SP_rgw_op_tracing) |

**What it does:** Enables LTTng-UST operator tracepoints.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_op_tracing true
ceph config get client.rgw rgw_op_tracing
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_parquet_buffer_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_parquet_buffer_size](../../../config/rgw/rgw.md#SP_rgw_parquet_buffer_size) |

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

### rgw_rados_pool_autoscale_bias

| | |
|---|---|
| Type | Float · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_rados_pool_autoscale_bias](../../../config/rgw/rgw.md#SP_rgw_rados_pool_autoscale_bias) |

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
| Table | [rgw.md#SP_rgw_rados_pool_recovery_priority](../../../config/rgw/rgw.md#SP_rgw_rados_pool_recovery_priority) |

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
| Table | [rgw.md#SP_rgw_rados_tracing](../../../config/rgw/rgw.md#SP_rgw_rados_tracing) |

**What it does:** Enables LTTng-UST tracepoints.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rados_tracing true
ceph config get client.rgw rgw_rados_tracing
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_script_uri

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_script_uri](../../../config/rgw/rgw.md#SP_rgw_script_uri) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_script_uri "https://service.example.com/"
ceph config get client.rgw rgw_script_uri
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
ceph config get client.rgw rgw_script_uri
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
