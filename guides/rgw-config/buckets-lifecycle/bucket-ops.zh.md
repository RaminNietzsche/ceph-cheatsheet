# Bucket operations

RGW 配置深度指南 — 12 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_bucket_counters_cache](#rgw_bucket_counters_cache) | `False` | Dev | 性能 |
| [rgw_bucket_counters_cache_size](#rgw_bucket_counters_cache_size) | `10000` | Advanced | 性能 |
| [rgw_bucket_default_quota_max_objects](#rgw_bucket_default_quota_max_objects) | `-1` | Basic | 策略 |
| [rgw_bucket_default_quota_max_size](#rgw_bucket_default_quota_max_size) | `-1` | Advanced | 策略 |
| [rgw_bucket_eexist_override](#rgw_bucket_eexist_override) | `False` | Advanced | 策略 |
| [rgw_bucket_index_max_aio](#rgw_bucket_index_max_aio) | `128` | Advanced | 性能 |
| [rgw_bucket_index_transaction_instrumentation](#rgw_bucket_index_transaction_instrumentation) | `False` | Dev | 开发 |
| [rgw_bucket_logging_obj_roll_time](#rgw_bucket_logging_obj_roll_time) | `300` | Advanced | 性能 |
| [rgw_bucket_persistent_notif_num_shards](#rgw_bucket_persistent_notif_num_shards) | `11` | Advanced | 策略 |
| [rgw_bucket_quota_cache_size](#rgw_bucket_quota_cache_size) | `10000` | Advanced | 性能 |
| [rgw_bucket_quota_ttl](#rgw_bucket_quota_ttl) | `10_min` | Advanced | 性能 |
| [rgw_bucket_sync_spawn_window](#rgw_bucket_sync_spawn_window) | `20` | Dev | 性能 |

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

### rgw_bucket_counters_cache

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rgw.md#SP_rgw_bucket_counters_cache](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache) |

**作用：** Enables an in-memory cache for **perf counters** with a bucket label, so per-bucket metrics avoid repeated counter lookups.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- `rgw_bucket_counters_cache_size`

**示例：**

```bash
ceph config set client.rgw rgw_bucket_counters_cache true
ceph config set client.rgw rgw_bucket_counters_cache_size 20000
```

**寻找最优值：**

**调优模型：** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_bucket_counters_cache_size

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_bucket_counters_cache_size) |

**作用：** Maximum number of labeled per-bucket perf counter entries kept in the cache.

**何时使用：** Increase on clusters with many active buckets and bucket-level monitoring enabled.

**示例：**

```bash
ceph config set client.rgw rgw_bucket_counters_cache_size 10000
ceph config get client.rgw rgw_bucket_counters_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_default_quota_max_objects

| | |
|---|---|
| 类型 | Int · default `-1` · **Basic** |
| 表格 | [rgw.md#SP_rgw_bucket_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_objects) |

**作用：** Default maximum **objects per bucket** for **newly created users**. Does not retroactively change existing users.

**何时使用：** Enforce per-bucket object limits for every new tenant without per-user `radosgw-admin quota` calls.

**相关选项：**

- `rgw_bucket_default_quota_max_size`, `rgw_user_default_quota_*`

**示例：**

```bash
ceph config set client rgw_bucket_default_quota_max_objects 500000
radosgw-admin user create --uid=newuser --display-name="New User"
```

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_default_quota_max_size

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_bucket_default_quota_max_size) |

**作用：** Default maximum **bytes per bucket** for new users.

**何时使用：** 为新用户、账户或 bucket 设置租户/平台默认限制。

**示例：**

```bash
ceph config set client rgw_bucket_default_quota_max_size $((100*1024*1024*1024))

radosgw-admin quota set --quota-scope=user --uid=alice --max-size=50G --max-objects=10000
radosgw-admin quota enable --quota-scope=user --uid=alice
```

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_bucket_eexist_override

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_eexist_override](../../../config/rgw/rgw.md#SP_rgw_bucket_eexist_override) |

**作用：** When `true`, `CreateBucket` on an existing bucket (same owner) returns **HTTP 409 / EEXIST** instead of succeeding idempotently.

**Default (`false`):** Matches AWS S3 — repeated CreateBucket by the same owner typically returns 200 OK.

**何时使用：** Clients or automation that expect an error on duplicate bucket creation.

**示例：**

```bash
ceph config set client.rgw rgw_bucket_eexist_override true
# aws s3 mb s3://existing-bucket  →  409 BucketAlreadyExists
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_bucket_index_max_aio

| | |
|---|---|
| 类型 | Uint · default `128` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_index_max_aio](../../../config/rgw/rgw.md#SP_rgw_bucket_index_max_aio) |

**作用：** Limits **concurrent RADOS requests** across **bucket index shards** (list operations, index maintenance, multi-shard updates). Used in `svc_bi_rados.cc`.

**何时使用：**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**相关选项：**

- [`rgw_multi_obj_del_max_aio`](../../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) (default 16)
- [`rgw_override_bucket_index_max_shards`](../../../config/rgw/rgw.md#SP_rgw_override_bucket_index_max_shards)

**示例：**

```bash
ceph config set client.rgw rgw_bucket_index_max_aio 256
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `128` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**观测信号：** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_bucket_index_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

More shards and faster OSDs tolerate higher values; during `nearfull` or heavy recovery, lower is safer.

---

### rgw_bucket_index_transaction_instrumentation

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rgw.md#SP_rgw_bucket_index_transaction_instrumentation](../../../config/rgw/rgw.md#SP_rgw_bucket_index_transaction_instrumentation) |

**作用：** Turns on extra instrumentation surrounding bucket index transactions.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_bucket_index_transaction_instrumentation true
ceph config get client.rgw rgw_bucket_index_transaction_instrumentation
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_bucket_logging_obj_roll_time

| | |
|---|---|
| 类型 | Uint · default `300` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_logging_obj_roll_time](../../../config/rgw/rgw.md#SP_rgw_bucket_logging_obj_roll_time) |

**作用：** Default time in seconds for the bucket logging object to roll

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_bucket_logging_obj_roll_time 300
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
```

**寻找最优值：**

**调优模型：** Performance

1. Default `300` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_logging_obj_roll_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_persistent_notif_num_shards

| | |
|---|---|
| 类型 | Uint · default `11` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_persistent_notif_num_shards](../../../config/rgw/rgw.md#SP_rgw_bucket_persistent_notif_num_shards) |

**作用：** Number of shards for a persistent topic.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_bucket_persistent_notif_num_shards 11
ceph config get client.rgw rgw_bucket_persistent_notif_num_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `11` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_bucket_quota_cache_size

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_quota_cache_size](../../../config/rgw/rgw.md#SP_rgw_bucket_quota_cache_size) |

**作用：** RGW quota stats cache size

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_bucket_quota_cache_size 10000
ceph config get client.rgw rgw_bucket_quota_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_bucket_quota_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_quota_ttl

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_bucket_quota_ttl](../../../config/rgw/rgw.md#SP_rgw_bucket_quota_ttl) |

**作用：** Bucket quota stats cache TTL

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_bucket_quota_ttl 10_min
ceph config get client.rgw rgw_bucket_quota_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_bucket_quota_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_bucket_sync_spawn_window

| | |
|---|---|
| 类型 | Int · default `20` · **Dev** |
| 表格 | [rgw.md#SP_rgw_bucket_sync_spawn_window](../../../config/rgw/rgw.md#SP_rgw_bucket_sync_spawn_window) |

**何时使用：**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**示例：**

```bash
ceph config set client.rgw rgw_bucket_sync_spawn_window 20
ceph config get client.rgw rgw_bucket_sync_spawn_window
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**观测信号：** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_bucket_sync_spawn_window
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---


[← RGW 配置概览](../OVERVIEW.md)
