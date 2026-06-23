# Core runtime

RGW 配置深度指南 — 16 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
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

### rgw_data

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/radosgw/$cluster-$id` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_data](../../../config/rgw/rgw.md#SP_rgw_data) |

**作用：** Alternative location for RGW configuration.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_data "/var/lib/ceph/radosgw/$cluster-$id"
ceph config get client.rgw rgw_data
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_min_obj_size_for_dedup

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dedup_min_obj_size_for_dedup](../../../config/rgw/rgw.md#SP_rgw_dedup_min_obj_size_for_dedup) |

**作用：** The minimum RGW object size for dedup (0 means no minimum size for dedup).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dedup_min_obj_size_for_dedup 64_K
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_split_obj_head

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dedup_split_obj_head](../../../config/rgw/rgw.md#SP_rgw_dedup_split_obj_head) |

**作用：** Enables the split-head functionality

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_dedup_split_obj_head false
ceph config get client.rgw rgw_dedup_split_obj_head
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_expose_bucket

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_expose_bucket](../../../config/rgw/rgw.md#SP_rgw_expose_bucket) |

**作用：** Send Bucket HTTP header with the response

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_expose_bucket true
ceph config get client.rgw rgw_expose_bucket
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_filter

| | |
|---|---|
| 类型 | Str · enum: ["none", "base", "d4n"] · default `none` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_filter](../../../config/rgw/rgw.md#SP_rgw_filter) |

**作用：** experimental Option to set a filter

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_filter none
ceph config get client.rgw rgw_filter
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["none", "base", "d4n"].
2. Default `none` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_graceful_stop

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_graceful_stop](../../../config/rgw/rgw.md#SP_rgw_graceful_stop) |

**作用：** Delay the shutdown until all outstanding requests have completed

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_graceful_stop true
ceph config get client.rgw rgw_graceful_stop
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_healthcheck_disabling_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_healthcheck_disabling_path](../../../config/rgw/rgw.md#SP_rgw_healthcheck_disabling_path) |

**作用：** Swift health check api can be disabled if a file can be accessed in this path.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_healthcheck_disabling_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_healthcheck_disabling_path
```

**寻找最优值：**

**调优模型：** Capacity

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
| 类型 | Str · default `/var/lib/ceph/radosgw/config.json` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_json_config](../../../config/rgw/rgw.md#SP_rgw_json_config) |

**作用：** Path to a json file that contains the static zone and zonegroup configuration. Requires rgw_config_store=json.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_json_config "/var/lib/ceph/radosgw/config.json"
ceph config get client.rgw rgw_json_config
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/config.json`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_json_config
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_mime_types_file

| | |
|---|---|
| 类型 | Str · default `/etc/mime.types` · **Basic** |
| 表格 | [rgw.md#SP_rgw_mime_types_file](../../../config/rgw/rgw.md#SP_rgw_mime_types_file) |

**作用：** Path to local mime types file

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_mime_types_file "/etc/mime.types"
ceph config get client.rgw rgw_mime_types_file
```

**寻找最优值：**

**调优模型：** Capacity

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
| 类型 | Int · default `-1` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_numa_node](../../../config/rgw/rgw.md#SP_rgw_numa_node) |

**作用：** set the RGW daemon's CPU affinity to a NUMA node (-1 for none)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_numa_node -1
ceph config get client.rgw rgw_numa_node
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_op_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_op_tracing](../../../config/rgw/rgw.md#SP_rgw_op_tracing) |

**作用：** Enables LTTng-UST operator tracepoints.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_op_tracing true
ceph config get client.rgw rgw_op_tracing
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_parquet_buffer_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_parquet_buffer_size](../../../config/rgw/rgw.md#SP_rgw_parquet_buffer_size) |

**作用：** the Maximum parquet buffer size, a limit to memory consumption for parquet reading operations.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_parquet_buffer_size 16_M
ceph config get client.rgw rgw_parquet_buffer_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_parquet_buffer_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_rados_pool_autoscale_bias

| | |
|---|---|
| 类型 | Float · default `4` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_rados_pool_autoscale_bias](../../../config/rgw/rgw.md#SP_rgw_rados_pool_autoscale_bias) |

**作用：** pg_autoscale_bias value for RGW metadata (omap-heavy) pools

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_rados_pool_autoscale_bias 4
ceph config get client.rgw rgw_rados_pool_autoscale_bias
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_autoscale_bias
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0.01`, max `100000`.

---

### rgw_rados_pool_recovery_priority

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_rados_pool_recovery_priority](../../../config/rgw/rgw.md#SP_rgw_rados_pool_recovery_priority) |

**作用：** recovery_priority value for RGW metadata (omap-heavy) pools

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_rados_pool_recovery_priority 5
ceph config get client.rgw rgw_rados_pool_recovery_priority
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_recovery_priority
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `-10`, max `10`.

---

### rgw_rados_tracing

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_rados_tracing](../../../config/rgw/rgw.md#SP_rgw_rados_tracing) |

**作用：** Enables LTTng-UST tracepoints.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_rados_tracing true
ceph config get client.rgw rgw_rados_tracing
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_script_uri

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_script_uri](../../../config/rgw/rgw.md#SP_rgw_script_uri) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_script_uri "https://service.example.com/"
ceph config get client.rgw rgw_script_uri
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
ceph config get client.rgw rgw_script_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
