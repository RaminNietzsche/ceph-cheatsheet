# Timeouts & intervals

RGW 配置深度指南 — 8 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_exit_timeout_secs](#rgw_exit_timeout_secs) | `2_min` | Advanced | 性能 |
| [rgw_init_timeout](#rgw_init_timeout) | `5_min` | Basic | 性能 |
| [rgw_objexp_gc_interval](#rgw_objexp_gc_interval) | `600` | Advanced | 性能 |
| [rgw_olh_pending_timeout_sec](#rgw_olh_pending_timeout_sec) | `1_hr` | Dev | 性能 |
| [rgw_ratelimit_interval](#rgw_ratelimit_interval) | `60` | Advanced | 性能 |
| [rgw_read_through_timeout_ms](#rgw_read_through_timeout_ms) | `10000` | Advanced | 性能 |
| [rgw_restore_debug_interval](#rgw_restore_debug_interval) | `-1` | Dev | 开发 |
| [rgw_usage_log_tick_interval](#rgw_usage_log_tick_interval) | `30` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、API 兼容性、租户限制 |
| **容量** | 磁盘布局、路径、池容量 |
| **性能** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **连通性** | 最近且稳定的外部端点 |
| **架构** | 后端、多站点拓扑 — 非数值扫描 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_exit_timeout_secs

| | |
|---|---|
| 类型 | Int · default `2_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_exit_timeout_secs](../../../config/rgw/rgw.md#SP_rgw_exit_timeout_secs) |

**作用：** RGW shutdown timeout

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_exit_timeout_secs 2_min
ceph config get client.rgw rgw_exit_timeout_secs
```

**寻找最优值：**

**调优模型：** Performance

1. Default `2_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_exit_timeout_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_init_timeout

| | |
|---|---|
| 类型 | Int · default `5_min` · **Basic** |
| 表格 | [rgw.md#SP_rgw_init_timeout](../../../config/rgw/rgw.md#SP_rgw_init_timeout) |

**作用：** Initialization timeout

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_init_timeout 5_min
ceph config get client.rgw rgw_init_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. Default `5_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_init_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_gc_interval

| | |
|---|---|
| 类型 | Uint · default `600` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_objexp_gc_interval](../../../config/rgw/rgw.md#SP_rgw_objexp_gc_interval) |

**作用：** Swift objects expirer garbage collector interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_objexp_gc_interval 600
ceph config get client.rgw rgw_objexp_gc_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_objexp_gc_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_olh_pending_timeout_sec

| | |
|---|---|
| 类型 | Int · default `1_hr` · **Dev** |
| 表格 | [rgw.md#SP_rgw_olh_pending_timeout_sec](../../../config/rgw/rgw.md#SP_rgw_olh_pending_timeout_sec) |

**作用：** Max time for pending OLH change to complete

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_olh_pending_timeout_sec 1_hr
ceph config get client.rgw rgw_olh_pending_timeout_sec
```

**寻找最优值：**

**调优模型：** Performance

1. Default `1_hr` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_olh_pending_timeout_sec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ratelimit_interval

| | |
|---|---|
| 类型 | Uint · default `60` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_ratelimit_interval](../../../config/rgw/rgw.md#SP_rgw_ratelimit_interval) |

**作用：** Time window for rate limiting in seconds

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_ratelimit_interval 60
ceph config get client.rgw rgw_ratelimit_interval
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Default `60` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_ratelimit_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `1`, max `—`.

---

### rgw_read_through_timeout_ms

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_read_through_timeout_ms](../../../config/rgw/rgw.md#SP_rgw_read_through_timeout_ms) |

**作用：** Maximum time in milliseconds for read-through GET requests to wait for cloud object restore completion

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_read_through_timeout_ms 10000
ceph config get client.rgw rgw_read_through_timeout_ms
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_read_through_timeout_ms
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `0`, max `—`.

---

### rgw_restore_debug_interval

| | |
|---|---|
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [rgw.md#SP_rgw_restore_debug_interval](../../../config/rgw/rgw.md#SP_rgw_restore_debug_interval) |

**作用：** The number of seconds that simulate one "day" in order to debug RGW CloudRestore. Do *not* modify for a production cluster.

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_restore_debug_interval -1
ceph config get client.rgw rgw_restore_debug_interval
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_usage_log_tick_interval

| | |
|---|---|
| 类型 | Int · default `30` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_usage_log_tick_interval](../../../config/rgw/rgw.md#SP_rgw_usage_log_tick_interval) |

**作用：** Number of seconds between usage log flush cycles

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_usage_log_tick_interval 30
ceph config get client.rgw rgw_usage_log_tick_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_usage_log_tick_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
