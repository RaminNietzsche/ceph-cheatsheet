# Garbage collection

RGW 配置深度指南 — 7 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_gc_max_concurrent_io](#rgw_gc_max_concurrent_io) | `10` | Advanced | Performance |
| [rgw_gc_max_objs](#rgw_gc_max_objs) | `32` | Advanced | Policy |
| [rgw_gc_max_queue_size](#rgw_gc_max_queue_size) | `131071_K` | Advanced | Policy |
| [rgw_gc_max_trim_chunk](#rgw_gc_max_trim_chunk) | `16` | Advanced | Policy |
| [rgw_gc_obj_min_wait](#rgw_gc_obj_min_wait) | `2_hr` | Advanced | Performance |
| [rgw_gc_processor_max_time](#rgw_gc_processor_max_time) | `1_hr` | Advanced | Policy |
| [rgw_gc_processor_period](#rgw_gc_processor_period) | `1_hr` | Advanced | Performance |

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

### rgw_gc_max_concurrent_io

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_max_concurrent_io](../../../config/rgw/rgw.md#SP_rgw_gc_max_concurrent_io) |

**作用：** Max concurrent RADOS IO operations for garbage collection

**何时使用：**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**示例：**

```bash
ceph config set client.rgw rgw_gc_max_concurrent_io 10
ceph config get client.rgw rgw_gc_max_concurrent_io
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_gc_max_concurrent_io
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_max_objs

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_gc_max_objs](../../../config/rgw/rgw.md#SP_rgw_gc_max_objs) |

**作用：** Number of shards for garbage collector data

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_gc_max_objs 32
ceph config get client.rgw rgw_gc_max_objs
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_queue_size

| | |
|---|---|
| 类型 | Uint · default `131071_K` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_max_queue_size](../../../config/rgw/rgw.md#SP_rgw_gc_max_queue_size) |

**作用：** Maximum allowed queue size for gc

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_gc_max_queue_size 131071_K
ceph config get client.rgw rgw_gc_max_queue_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `131071_K` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_max_trim_chunk

| | |
|---|---|
| 类型 | Int · default `16` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_max_trim_chunk](../../../config/rgw/rgw.md#SP_rgw_gc_max_trim_chunk) |

**作用：** Max number of keys to remove from garbage collector log in a single operation

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_gc_max_trim_chunk 16
ceph config get client.rgw rgw_gc_max_trim_chunk
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_obj_min_wait

| | |
|---|---|
| 类型 | Int · default `2_hr` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_obj_min_wait](../../../config/rgw/rgw.md#SP_rgw_gc_obj_min_wait) |

**作用：** Garbage collection object expiration time

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_gc_obj_min_wait 2_hr
ceph config get client.rgw rgw_gc_obj_min_wait
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `2_hr`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_gc_obj_min_wait
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_gc_processor_max_time

| | |
|---|---|
| 类型 | Int · default `1_hr` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_processor_max_time](../../../config/rgw/rgw.md#SP_rgw_gc_processor_max_time) |

**作用：** Length of time GC processor can lease shard

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_gc_processor_max_time 1_hr
ceph config get client.rgw rgw_gc_processor_max_time
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1_hr` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_gc_processor_period

| | |
|---|---|
| 类型 | Int · default `1_hr` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_gc_processor_period](../../../config/rgw/rgw.md#SP_rgw_gc_processor_period) |

**作用：** Garbage collector cycle run time

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_gc_processor_period 1_hr
ceph config get client.rgw rgw_gc_processor_period
```

**寻找最优值：**

**调优模型：** Performance

1. Default `1_hr` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_gc_processor_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
