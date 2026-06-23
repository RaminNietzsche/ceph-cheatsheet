# NFS gateway

RGW 配置深度指南 — 14 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_nfs_fhcache_partitions](#rgw_nfs_fhcache_partitions) | `3` | Advanced | 性能 |
| [rgw_nfs_fhcache_size](#rgw_nfs_fhcache_size) | `2017` | Advanced | 性能 |
| [rgw_nfs_frontends](#rgw_nfs_frontends) | `rgw-nfs` | Basic | 性能 |
| [rgw_nfs_lru_lane_hiwat](#rgw_nfs_lru_lane_hiwat) | `911` | Advanced | 性能 |
| [rgw_nfs_lru_lanes](#rgw_nfs_lru_lanes) | `5` | Advanced | 性能 |
| [rgw_nfs_max_gc](#rgw_nfs_max_gc) | `5_min` | Advanced | 策略 |
| [rgw_nfs_namespace_expire_secs](#rgw_nfs_namespace_expire_secs) | `5_min` | Advanced | 性能 |
| [rgw_nfs_run_gc_threads](#rgw_nfs_run_gc_threads) | `False` | Advanced | 策略 |
| [rgw_nfs_run_lc_threads](#rgw_nfs_run_lc_threads) | `False` | Advanced | 策略 |
| [rgw_nfs_run_quota_threads](#rgw_nfs_run_quota_threads) | `True` | Advanced | 策略 |
| [rgw_nfs_run_restore_threads](#rgw_nfs_run_restore_threads) | `False` | Advanced | 策略 |
| [rgw_nfs_run_sync_thread](#rgw_nfs_run_sync_thread) | `False` | Advanced | 策略 |
| [rgw_nfs_s3_fast_attrs](#rgw_nfs_s3_fast_attrs) | `False` | Advanced | 策略 |
| [rgw_nfs_write_completion_interval_s](#rgw_nfs_write_completion_interval_s) | `10` | Advanced | 性能 |

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

### rgw_nfs_fhcache_partitions

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_fhcache_partitions](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_partitions) |

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_nfs_fhcache_partitions 3
ceph config get client.rgw rgw_nfs_fhcache_partitions
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_nfs_fhcache_partitions
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_fhcache_size

| | |
|---|---|
| 类型 | Int · default `2017` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_fhcache_size](../../../config/rgw/rgw.md#SP_rgw_nfs_fhcache_size) |

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_nfs_fhcache_size 2017
ceph config get client.rgw rgw_nfs_fhcache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `2017`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_nfs_fhcache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_frontends

| | |
|---|---|
| 类型 | Str · default `rgw-nfs` · **Basic** |
| 表格 | [rgw.md#SP_rgw_nfs_frontends](../../../config/rgw/rgw.md#SP_rgw_nfs_frontends) |

**作用：** RGW frontends configuration when running as librgw/nfs

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_frontends "rgw-nfs"
ceph config get client.rgw rgw_nfs_frontends
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `rgw-nfs`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_frontends
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_lru_lane_hiwat

| | |
|---|---|
| 类型 | Int · default `911` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_lru_lane_hiwat](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lane_hiwat) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_lru_lane_hiwat 911
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `911`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_lru_lane_hiwat
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_lru_lanes

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_lru_lanes](../../../config/rgw/rgw.md#SP_rgw_nfs_lru_lanes) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_lru_lanes 5
ceph config get client.rgw rgw_nfs_lru_lanes
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_lru_lanes
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_nfs_max_gc

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_max_gc](../../../config/rgw/rgw.md#SP_rgw_nfs_max_gc) |

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_max_gc 5_min
ceph config get client.rgw rgw_nfs_max_gc
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `5_min` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `1`, max `—`.

---

### rgw_nfs_namespace_expire_secs

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_namespace_expire_secs](../../../config/rgw/rgw.md#SP_rgw_nfs_namespace_expire_secs) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_namespace_expire_secs 5_min
ceph config get client.rgw rgw_nfs_namespace_expire_secs
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_nfs_namespace_expire_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `1`, max `—`.

---

### rgw_nfs_run_gc_threads

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_run_gc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_gc_threads) |

**作用：** run GC threads in librgw (default off)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_run_gc_threads true
ceph config get client.rgw rgw_nfs_run_gc_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_lc_threads

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_run_lc_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_lc_threads) |

**作用：** run lifecycle threads in librgw (default off)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_run_lc_threads true
ceph config get client.rgw rgw_nfs_run_lc_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_quota_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_run_quota_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_quota_threads) |

**作用：** run quota threads in librgw (default on)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_run_quota_threads false
ceph config get client.rgw rgw_nfs_run_quota_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_restore_threads

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_run_restore_threads](../../../config/rgw/rgw.md#SP_rgw_nfs_run_restore_threads) |

**作用：** run objects' restore threads in librgw (default off)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_run_restore_threads true
ceph config get client.rgw rgw_nfs_run_restore_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_run_sync_thread

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_run_sync_thread](../../../config/rgw/rgw.md#SP_rgw_nfs_run_sync_thread) |

**作用：** run sync thread in librgw (default off)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_run_sync_thread true
ceph config get client.rgw rgw_nfs_run_sync_thread
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_s3_fast_attrs

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_s3_fast_attrs](../../../config/rgw/rgw.md#SP_rgw_nfs_s3_fast_attrs) |

**作用：** use fast S3 attrs from bucket index (immutable only)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_nfs_s3_fast_attrs true
ceph config get client.rgw rgw_nfs_s3_fast_attrs
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_nfs_write_completion_interval_s

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_nfs_write_completion_interval_s](../../../config/rgw/rgw.md#SP_rgw_nfs_write_completion_interval_s) |

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_nfs_write_completion_interval_s 10
ceph config get client.rgw rgw_nfs_write_completion_interval_s
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_nfs_write_completion_interval_s
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
