# Bucket index & sharding

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_override_bucket_index_max_shards](#rgw_override_bucket_index_max_shards) | `0` | Dev | 策略 |
| [rgw_pending_bucket_index_op_expiration](#rgw_pending_bucket_index_op_expiration) | `120` | Advanced | 性能 |
| [rgw_safe_max_objects_per_shard](#rgw_safe_max_objects_per_shard) | `102400` | Advanced | 策略 |
| [rgw_shard_warning_threshold](#rgw_shard_warning_threshold) | `90` | Advanced | 性能 |

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

### rgw_override_bucket_index_max_shards

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_override_bucket_index_max_shards](../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards) |

**作用：** The default number of bucket index shards for newly-created buckets. This value overrides bucket_index_max_shards stored in the zone. Setting this value in the zone is preferred, because it applies globally to all radosgw daemons running in the zone.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_override_bucket_index_max_shards 128
ceph config get client.rgw rgw_override_bucket_index_max_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_pending_bucket_index_op_expiration

| | |
|---|---|
| 类型 | Uint · default `120` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_pending_bucket_index_op_expiration](../../../config/rgw/rgw.md#SP_rgw_pending_bucket_index_op_expiration) |

**作用：** Number of seconds a pending operation can remain in bucket index shard.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_pending_bucket_index_op_expiration 120
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_pending_bucket_index_op_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_safe_max_objects_per_shard

| | |
|---|---|
| 类型 | Int · default `102400` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_safe_max_objects_per_shard](../../../config/rgw/rgw.md#SP_rgw_safe_max_objects_per_shard) |

**作用：** Safe number of objects per shard

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_safe_max_objects_per_shard 102400
ceph config get client.rgw rgw_safe_max_objects_per_shard
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `102400` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_shard_warning_threshold

| | |
|---|---|
| 类型 | Float · default `90` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_shard_warning_threshold](../../../config/rgw/rgw.md#SP_rgw_shard_warning_threshold) |

**作用：** Warn about max objects per shard

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_shard_warning_threshold 90
ceph config get client.rgw rgw_shard_warning_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `90`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_shard_warning_threshold
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
