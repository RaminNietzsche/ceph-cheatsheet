# Replication & sync

RGW 配置深度指南 — 28 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_data_log_changes_size](#rgw_data_log_changes_size) | `1000` | Dev | Performance |
| [rgw_data_log_num_shards](#rgw_data_log_num_shards) | `128` | Advanced | Policy |
| [rgw_data_log_window](#rgw_data_log_window) | `30` | Advanced | Performance |
| [rgw_data_notify_interval_msec](#rgw_data_notify_interval_msec) | `0` | Advanced | Performance |
| [rgw_data_sync_poll_interval](#rgw_data_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_data_sync_spawn_window](#rgw_data_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_lfuda_sync_frequency](#rgw_lfuda_sync_frequency) | `60` | Advanced | Performance |
| [rgw_md_log_max_shards](#rgw_md_log_max_shards) | `64` | Advanced | Policy |
| [rgw_md_notify_interval_msec](#rgw_md_notify_interval_msec) | `200` | Advanced | Performance |
| [rgw_meta_sync_poll_interval](#rgw_meta_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_meta_sync_spawn_window](#rgw_meta_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_run_sync_thread](#rgw_run_sync_thread) | `True` | Advanced | Policy |
| [rgw_sync_data_full_inject_err_probability](#rgw_sync_data_full_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_data_inject_err_probability](#rgw_sync_data_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_lease_period](#rgw_sync_lease_period) | `2_min` | Dev | Performance |
| [rgw_sync_log_trim_concurrent_buckets](#rgw_sync_log_trim_concurrent_buckets) | `4` | Advanced | Performance |
| [rgw_sync_log_trim_interval](#rgw_sync_log_trim_interval) | `20_min` | Advanced | Performance |
| [rgw_sync_log_trim_max_buckets](#rgw_sync_log_trim_max_buckets) | `16` | Advanced | Policy |
| [rgw_sync_log_trim_min_cold_buckets](#rgw_sync_log_trim_min_cold_buckets) | `4` | Advanced | Performance |
| [rgw_sync_meta_inject_err_probability](#rgw_sync_meta_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_obj_etag_verify](#rgw_sync_obj_etag_verify) | `False` | Advanced | Policy |
| [rgw_sync_trace_history_size](#rgw_sync_trace_history_size) | `4_K` | Advanced | Performance |
| [rgw_sync_trace_per_node_log_size](#rgw_sync_trace_per_node_log_size) | `32` | Advanced | Performance |
| [rgw_sync_trace_servicemap_update_interval](#rgw_sync_trace_servicemap_update_interval) | `10` | Advanced | Performance |
| [rgw_user_quota_bucket_sync_interval](#rgw_user_quota_bucket_sync_interval) | `3_min` | Advanced | Performance |
| [rgw_user_quota_sync_idle_users](#rgw_user_quota_sync_idle_users) | `False` | Advanced | Policy |
| [rgw_user_quota_sync_interval](#rgw_user_quota_sync_interval) | `1_day` | Advanced | Performance |
| [rgw_user_quota_sync_wait_time](#rgw_user_quota_sync_wait_time) | `1_day` | Advanced | Performance |

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

### rgw_data_log_changes_size

| | |
|---|---|
| 类型 | Int · default `1000` · **Dev** |
| 表格 | [rgw.md#SP_rgw_data_log_changes_size](../../../config/rgw/rgw.md#SP_rgw_data_log_changes_size) |

**作用：** Max size of pending changes in data log

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_data_log_changes_size 1000
ceph config get client.rgw rgw_data_log_changes_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data_log_changes_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_log_num_shards

| | |
|---|---|
| 类型 | Int · default `128` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_data_log_num_shards](../../../config/rgw/rgw.md#SP_rgw_data_log_num_shards) |

**作用：** Number of data log shards

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_data_log_num_shards 128
ceph config get client.rgw rgw_data_log_num_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_data_log_window

| | |
|---|---|
| 类型 | Int · default `30` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_data_log_window](../../../config/rgw/rgw.md#SP_rgw_data_log_window) |

**作用：** Data log time window

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_data_log_window 30
ceph config get client.rgw rgw_data_log_window
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `30` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_data_log_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_notify_interval_msec

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_data_notify_interval_msec](../../../config/rgw/rgw.md#SP_rgw_data_notify_interval_msec) |

**作用：** data changes notification interval to followers

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_data_notify_interval_msec 60
ceph config get client.rgw rgw_data_notify_interval_msec
```

**寻找最优值：**

**调优模型：** Performance

1. Default `0` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_notify_interval_msec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_poll_interval

| | |
|---|---|
| 类型 | Int · default `20` · **Dev** |
| 表格 | [rgw.md#SP_rgw_data_sync_poll_interval](../../../config/rgw/rgw.md#SP_rgw_data_sync_poll_interval) |

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_data_sync_poll_interval 20
ceph config get client.rgw rgw_data_sync_poll_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_sync_poll_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_spawn_window

| | |
|---|---|
| 类型 | Int · default `20` · **Dev** |
| 表格 | [rgw.md#SP_rgw_data_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_data_sync_spawn_window) |

**何时使用：**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**示例：**

```bash
ceph config set client.rgw rgw_data_sync_spawn_window 20
ceph config get client.rgw rgw_data_sync_spawn_window
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**观测信号：** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_data_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_lfuda_sync_frequency

| | |
|---|---|
| 类型 | Int · default `60` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_lfuda_sync_frequency](../../../config/rgw/rgw.md#SP_rgw_lfuda_sync_frequency) |

**作用：** LFUDA variables' sync frequency in seconds

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lfuda_sync_frequency 60
ceph config get client.rgw rgw_lfuda_sync_frequency
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lfuda_sync_frequency
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_md_log_max_shards

| | |
|---|---|
| 类型 | Int · default `64` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_md_log_max_shards](../../../config/rgw/rgw.md#SP_rgw_md_log_max_shards) |

**作用：** RGW number of metadata log shards

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_md_log_max_shards 64
ceph config get client.rgw rgw_md_log_max_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_md_notify_interval_msec

| | |
|---|---|
| 类型 | Int · default `200` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_md_notify_interval_msec](../../../config/rgw/rgw.md#SP_rgw_md_notify_interval_msec) |

**作用：** Length of time to aggregate metadata changes

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_md_notify_interval_msec 200
ceph config get client.rgw rgw_md_notify_interval_msec
```

**寻找最优值：**

**调优模型：** Performance

1. Default `200` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_md_notify_interval_msec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_poll_interval

| | |
|---|---|
| 类型 | Int · default `20` · **Dev** |
| 表格 | [rgw.md#SP_rgw_meta_sync_poll_interval](../../../config/rgw/rgw.md#SP_rgw_meta_sync_poll_interval) |

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_meta_sync_poll_interval 20
ceph config get client.rgw rgw_meta_sync_poll_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_meta_sync_poll_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_spawn_window

| | |
|---|---|
| 类型 | Int · default `20` · **Dev** |
| 表格 | [rgw.md#SP_rgw_meta_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_meta_sync_spawn_window) |

**何时使用：**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**示例：**

```bash
ceph config set client.rgw rgw_meta_sync_spawn_window 20
ceph config get client.rgw rgw_meta_sync_spawn_window
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**观测信号：** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_meta_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_run_sync_thread

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_run_sync_thread](../../../config/rgw/rgw.md#SP_rgw_run_sync_thread) |

**作用：** Should run sync thread

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_run_sync_thread false
ceph config get client.rgw rgw_run_sync_thread
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_sync_data_full_inject_err_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_sync_data_full_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_data_full_inject_err_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_sync_data_full_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_full_inject_err_probability
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_data_inject_err_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_sync_data_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_data_inject_err_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_sync_data_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_inject_err_probability
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_lease_period

| | |
|---|---|
| 类型 | Int · default `2_min` · **Dev** |
| 表格 | [rgw.md#SP_rgw_sync_lease_period](../../../config/rgw/rgw.md#SP_rgw_sync_lease_period) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_sync_lease_period 2_min
ceph config get client.rgw rgw_sync_lease_period
```

**寻找最优值：**

**调优模型：** Performance

1. Default `2_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_lease_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_concurrent_buckets

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_log_trim_concurrent_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_concurrent_buckets) |

**作用：** Maximum number of buckets to trim in parallel

**何时使用：**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**示例：**

```bash
ceph config set client.rgw rgw_sync_log_trim_concurrent_buckets 4
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `4` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_interval

| | |
|---|---|
| 类型 | Int · default `20_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_log_trim_interval](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_interval) |

**作用：** Sync log trim interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_sync_log_trim_interval 20_min
ceph config get client.rgw rgw_sync_log_trim_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_log_trim_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_max_buckets

| | |
|---|---|
| 类型 | Int · default `16` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_log_trim_max_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_max_buckets) |

**作用：** Maximum number of buckets to trim per interval

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_sync_log_trim_max_buckets 16
ceph config get client.rgw rgw_sync_log_trim_max_buckets
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sync_log_trim_min_cold_buckets

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_log_trim_min_cold_buckets](../../../config/rgw/rgw.md#SP_rgw_sync_log_trim_min_cold_buckets) |

**作用：** Minimum number of cold buckets to trim per interval

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_sync_log_trim_min_cold_buckets 4
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_meta_inject_err_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_sync_meta_inject_err_probability](../../../config/rgw/rgw.md#SP_rgw_sync_meta_inject_err_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_sync_meta_inject_err_probability 0
ceph config get client.rgw rgw_sync_meta_inject_err_probability
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_obj_etag_verify

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_obj_etag_verify](../../../config/rgw/rgw.md#SP_rgw_sync_obj_etag_verify) |

**作用：** Verify if the object copied from remote is identical to its source

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_sync_obj_etag_verify true
ceph config get client.rgw rgw_sync_obj_etag_verify
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_sync_trace_history_size

| | |
|---|---|
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_trace_history_size](../../../config/rgw/rgw.md#SP_rgw_sync_trace_history_size) |

**作用：** Sync trace history size

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_sync_trace_history_size 4_K
ceph config get client.rgw rgw_sync_trace_history_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_history_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_per_node_log_size

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_trace_per_node_log_size](../../../config/rgw/rgw.md#SP_rgw_sync_trace_per_node_log_size) |

**作用：** Sync trace per-node log size

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_sync_trace_per_node_log_size 32
ceph config get client.rgw rgw_sync_trace_per_node_log_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_per_node_log_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_servicemap_update_interval

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sync_trace_servicemap_update_interval](../../../config/rgw/rgw.md#SP_rgw_sync_trace_servicemap_update_interval) |

**作用：** Sync-trace service-map update interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_sync_trace_servicemap_update_interval 10
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_bucket_sync_interval

| | |
|---|---|
| 类型 | Int · default `3_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_quota_bucket_sync_interval](../../../config/rgw/rgw.md#SP_rgw_user_quota_bucket_sync_interval) |

**作用：** User quota bucket sync interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_user_quota_bucket_sync_interval 3_min
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `3_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_idle_users

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_quota_sync_idle_users](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_idle_users) |

**作用：** Should sync idle users quota

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_user_quota_sync_idle_users true
ceph config get client.rgw rgw_user_quota_sync_idle_users
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_quota_sync_interval

| | |
|---|---|
| 类型 | Int · default `1_day` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_quota_sync_interval](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_interval) |

**作用：** User quota sync interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_user_quota_sync_interval 1_day
ceph config get client.rgw rgw_user_quota_sync_interval
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `1_day` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_sync_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_wait_time

| | |
|---|---|
| 类型 | Int · default `1_day` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_quota_sync_wait_time](../../../config/rgw/rgw.md#SP_rgw_user_quota_sync_wait_time) |

**作用：** User quota full-sync wait time

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_user_quota_sync_wait_time 1_day
ceph config get client.rgw rgw_user_quota_sync_wait_time
```

**寻找最优值：**

**调优模型：** Performance

1. Default `1_day` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_user_quota_sync_wait_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
