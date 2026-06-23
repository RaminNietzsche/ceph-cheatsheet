# Usage logging

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_usage_log_flush_threshold](#rgw_usage_log_flush_threshold) | `1024` | Advanced | 性能 |
| [rgw_usage_log_key_transition](#rgw_usage_log_key_transition) | `True` | Advanced | 策略 |
| [rgw_usage_max_shards](#rgw_usage_max_shards) | `32` | Advanced | 策略 |
| [rgw_usage_max_user_shards](#rgw_usage_max_user_shards) | `1` | Advanced | 策略 |

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

### rgw_usage_log_flush_threshold

| | |
|---|---|
| 类型 | Int · default `1024` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_usage_log_flush_threshold](../../../config/rgw/rgw.md#SP_rgw_usage_log_flush_threshold) |

**作用：** Number of entries in usage log before flushing

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_usage_log_flush_threshold 1024
ceph config get client.rgw rgw_usage_log_flush_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_usage_log_flush_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_usage_log_key_transition

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_usage_log_key_transition](../../../config/rgw/rgw.md#SP_rgw_usage_log_key_transition) |

**作用：** Handle the co-existence of both old and new name-by-user keys

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_usage_log_key_transition false
ceph config get client.rgw rgw_usage_log_key_transition
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_usage_max_shards

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_usage_max_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_shards) |

**作用：** Number of shards for usage log.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set global rgw_usage_max_shards 32
ceph config get global rgw_usage_max_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_usage_max_user_shards

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_usage_max_user_shards](../../../config/rgw/rgw.md#SP_rgw_usage_max_user_shards) |

**作用：** Number of shards for single user in usage log

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_usage_max_user_shards 1
ceph config get client.rgw rgw_usage_max_user_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

**边界：** min `1`, max `—`.

---


[← RGW 配置概览](../OVERVIEW.md)
