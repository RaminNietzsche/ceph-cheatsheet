# Concurrency & RADOS I/O

RGW 配置深度指南 — 14 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_list_bucket_min_readahead](#rgw_list_bucket_min_readahead) | `1000` | Advanced | 性能 |
| [rgw_max_concurrent_requests](#rgw_max_concurrent_requests) | `1024` | Basic | 性能 |
| [rgw_max_copy_obj_concurrent_io](#rgw_max_copy_obj_concurrent_io) | `10` | Advanced | 性能 |
| [rgw_max_objs_per_shard](#rgw_max_objs_per_shard) | `100000` | Basic | 策略 |
| [rgw_multi_obj_del_max_aio](#rgw_multi_obj_del_max_aio) | `16` | Advanced | 性能 |
| [rgw_num_async_rados_threads](#rgw_num_async_rados_threads) | `32` | Advanced | 性能 |
| [rgw_num_control_oids](#rgw_num_control_oids) | `8` | Advanced | 策略 |
| [rgw_obj_stripe_size](#rgw_obj_stripe_size) | `4_M` | Advanced | 性能 |
| [rgw_op_thread_suicide_timeout](#rgw_op_thread_suicide_timeout) | `0` | Dev | 开发 |
| [rgw_op_thread_timeout](#rgw_op_thread_timeout) | `10_min` | Dev | 开发 |
| [rgw_redis_connection_pool_size](#rgw_redis_connection_pool_size) | `512` | Basic | 性能 |
| [rgw_restore_max_objs](#rgw_restore_max_objs) | `32` | Advanced | 策略 |
| [rgw_restore_processor_period](#rgw_restore_processor_period) | `15_min` | Advanced | 性能 |
| [rgw_thread_pool_size](#rgw_thread_pool_size) | `512` | Basic | 性能 |

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

### rgw_list_bucket_min_readahead

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_list_bucket_min_readahead](../../../config/rgw/rgw.md#SP_rgw_list_bucket_min_readahead) |

**作用：** Minimum number of entries to request from rados for bucket listing

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_list_bucket_min_readahead 1000
ceph config get client.rgw rgw_list_bucket_min_readahead
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_list_bucket_min_readahead
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_concurrent_requests

| | |
|---|---|
| 类型 | Int · default `1024` · **Basic** |
| 表格 | [rgw.md#SP_rgw_max_concurrent_requests](../../../config/rgw/rgw.md#SP_rgw_max_concurrent_requests) |

**作用：** Maximum number of concurrent HTTP requests. Maximum number of concurrent HTTP requests that the beast frontend will process. Tuning this can help to limit memory usage under heavy load.

**何时使用：**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**相关选项：**

- [`rgw_frontends`](../../../config/rgw/rgw.md#SP_rgw_frontends)

**示例：**

```bash
ceph config set client.rgw rgw_max_concurrent_requests 1024
ceph config get client.rgw rgw_max_concurrent_requests
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `1024` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_concurrent_requests
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_copy_obj_concurrent_io

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_copy_obj_concurrent_io](../../../config/rgw/rgw.md#SP_rgw_max_copy_obj_concurrent_io) |

**作用：** Number of refcount operations to process concurrently when executing copy_obj

**何时使用：**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**示例：**

```bash
ceph config set client.rgw rgw_max_copy_obj_concurrent_io 10
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_objs_per_shard

| | |
|---|---|
| 类型 | Uint · default `100000` · **Basic** |
| 表格 | [rgw.md#SP_rgw_max_objs_per_shard](../../../config/rgw/rgw.md#SP_rgw_max_objs_per_shard) |

**作用：** Max objects per shard for dynamic resharding This is the max number of objects per bucket index shard that RGW will allow with dynamic resharding. RGW will trigger an automatic reshard operation on the bucket if it exceeds this number.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_objs_per_shard 100000
ceph config get client.rgw rgw_max_objs_per_shard
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `100000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_multi_obj_del_max_aio

| | |
|---|---|
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_multi_obj_del_max_aio](../../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) |

**作用：** Max number of concurrent RADOS requests per multi-object delete request.

**何时使用：**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**示例：**

```bash
ceph config set client.rgw rgw_multi_obj_del_max_aio 16
ceph config get client.rgw rgw_multi_obj_del_max_aio
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `16` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**观测信号：** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_multi_obj_del_max_aio
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

---

### rgw_num_async_rados_threads

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_num_async_rados_threads](../../../config/rgw/rgw.md#SP_rgw_num_async_rados_threads) |

**作用：** Number of concurrent RADOS operations in multisite sync The number of concurrent RADOS IO operations that will be triggered for handling multisite sync operations. This includes control related work, and not the actual sync operations.

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

**示例：**

```bash
ceph config set client.rgw rgw_num_async_rados_threads 32
ceph config get client.rgw rgw_num_async_rados_threads
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `32` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_num_async_rados_threads
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_num_control_oids

| | |
|---|---|
| 类型 | Int · default `8` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_num_control_oids](../../../config/rgw/rgw.md#SP_rgw_num_control_oids) |

**作用：** Number of control objects used for cross-RGW communication. RGW uses certain control objects to send messages between different RGW processes running on the same zone. These messages include metadata cache invalidation info that is being sent when metadata is modified (such as user or bucket information). A higher number of control objects allows better concurrency of these messages, at the cost of more resource utilization.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_num_control_oids 8
ceph config get client.rgw rgw_num_control_oids
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_obj_stripe_size

| | |
|---|---|
| 类型 | Size · default `4_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_obj_stripe_size](../../../config/rgw/rgw.md#SP_rgw_obj_stripe_size) |

**作用：** RGW object stripe size The size of an object stripe for RGW objects. This is the maximum size a backing RADOS object will have. RGW objects that are larger than this will span over multiple objects.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_obj_stripe_size 4_M
ceph config get client.rgw rgw_obj_stripe_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_obj_stripe_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_op_thread_suicide_timeout

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_op_thread_suicide_timeout](../../../config/rgw/rgw.md#SP_rgw_op_thread_suicide_timeout) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_op_thread_suicide_timeout 60
ceph config get client.rgw rgw_op_thread_suicide_timeout
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_op_thread_timeout

| | |
|---|---|
| 类型 | Int · default `10_min` · **Dev** |
| 表格 | [rgw.md#SP_rgw_op_thread_timeout](../../../config/rgw/rgw.md#SP_rgw_op_thread_timeout) |

**作用：** Timeout for async rados coroutine operations.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_op_thread_timeout 10_min
ceph config get client.rgw rgw_op_thread_timeout
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`10_min`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_redis_connection_pool_size

| | |
|---|---|
| 类型 | Int · default `512` · **Basic** |
| 表格 | [rgw.md#SP_rgw_redis_connection_pool_size](../../../config/rgw/rgw.md#SP_rgw_redis_connection_pool_size) |

**作用：** RGW connection pool size for Redis operation per D4N This option sets the size of the connection pool for Redis operations in D4N. It is used to manage the number of concurrent connections to Redis. A larger pool size can improve performance when multiple threads are accessing Redis simultaneously, but it also increases resource usage.

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_redis_connection_pool_size 512
ceph config get client.rgw rgw_redis_connection_pool_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_redis_connection_pool_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_restore_max_objs

| | |
|---|---|
| 类型 | Int · default `32` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_restore_max_objs](../../../config/rgw/rgw.md#SP_rgw_restore_max_objs) |

**作用：** Number of shards for restore processing Number of RADOS objects to use for storing restore entries which are in progress. This affects concurrency of restore maintenance, as shards can be processed in parallel.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_restore_max_objs 32
ceph config get client.rgw rgw_restore_max_objs
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_restore_processor_period

| | |
|---|---|
| 类型 | Int · default `15_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_restore_processor_period](../../../config/rgw/rgw.md#SP_rgw_restore_processor_period) |

**作用：** Restore cycle run time The amount of time between the start of consecutive runs of the restore processing threads. If the thread runs takes more than this period, it will not wait before running again.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_restore_processor_period 15_min
ceph config get client.rgw rgw_restore_processor_period
```

**寻找最优值：**

**调优模型：** Performance

1. Default `15_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_restore_processor_period
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_thread_pool_size

| | |
|---|---|
| 类型 | Int · default `512` · **Basic** |
| 表格 | [rgw.md#SP_rgw_thread_pool_size](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size) |

**作用：** RGW requests handling thread pool size. This parameter determines the number of concurrent requests RGW can process when using either the civetweb, or the fastcgi frontends. The higher this number is, RGW will be able to deal with more concurrent requests at the cost of more resource utilization.

**何时使用：**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**示例：**

```bash
ceph config set client.rgw rgw_thread_pool_size 512
ceph config get client.rgw rgw_thread_pool_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at `512` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**观测信号：** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_thread_pool_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
