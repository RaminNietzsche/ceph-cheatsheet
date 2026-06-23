# D4N / D3N cache

RGW 配置深度指南 — 22 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [d4n_writecache_enabled](#d4n_writecache_enabled) | `False` | Advanced | 性能 |
| [rgw_d3n_l1_datacache_persistent_path](#rgw_d3n_l1_datacache_persistent_path) | `/tmp/rgw_datacache/` | Advanced | 容量 |
| [rgw_d3n_l1_datacache_size](#rgw_d3n_l1_datacache_size) | `1_G` | Advanced | 性能 |
| [rgw_d3n_l1_evict_cache_on_start](#rgw_d3n_l1_evict_cache_on_start) | `True` | Advanced | 性能 |
| [rgw_d3n_l1_eviction_policy](#rgw_d3n_l1_eviction_policy) | `lru` | Advanced | 架构 |
| [rgw_d3n_l1_fadvise](#rgw_d3n_l1_fadvise) | `4` | Advanced | 性能 |
| [rgw_d3n_l1_local_datacache_enabled](#rgw_d3n_l1_local_datacache_enabled) | `False` | Advanced | 性能 |
| [rgw_d3n_libaio_aio_num](#rgw_d3n_libaio_aio_num) | `64` | Advanced | 策略 |
| [rgw_d3n_libaio_aio_threads](#rgw_d3n_libaio_aio_threads) | `20` | Advanced | 性能 |
| [rgw_d4n_address](#rgw_d4n_address) | `127.0.0.1:6379` | Advanced | 性能 |
| [rgw_d4n_backend_address](#rgw_d4n_backend_address) | `127.0.0.1:6379` | Advanced | 性能 |
| [rgw_d4n_cache_cleaning_interval](#rgw_d4n_cache_cleaning_interval) | `1000` | Advanced | 性能 |
| [rgw_d4n_l1_datacache_address](#rgw_d4n_l1_datacache_address) | `127.0.0.1:6379` | Advanced | 性能 |
| [rgw_d4n_l1_datacache_disk_reserve](#rgw_d4n_l1_datacache_disk_reserve) | `1_G` | Advanced | 性能 |
| [rgw_d4n_l1_datacache_persistent_path](#rgw_d4n_l1_datacache_persistent_path) | `/tmp/rgw_d4n_datacache/` | Advanced | 容量 |
| [rgw_d4n_l1_evict_cache_on_start](#rgw_d4n_l1_evict_cache_on_start) | `True` | Advanced | 性能 |
| [rgw_d4n_l1_fadvise](#rgw_d4n_l1_fadvise) | `4` | Advanced | 性能 |
| [rgw_d4n_l1_write_open_flags](#rgw_d4n_l1_write_open_flags) | `4096` | Advanced | 性能 |
| [rgw_d4n_libaio_aio_num](#rgw_d4n_libaio_aio_num) | `64` | Advanced | 策略 |
| [rgw_d4n_libaio_aio_threads](#rgw_d4n_libaio_aio_threads) | `20` | Advanced | 性能 |
| [rgw_d4n_local_rgw_address](#rgw_d4n_local_rgw_address) | `127.0.0.1:8000` | Advanced | 性能 |
| [rgw_d4n_localweight_processing_interval](#rgw_d4n_localweight_processing_interval) | `3600` | Advanced | 性能 |

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

### d4n_writecache_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_d4n_writecache_enabled](../../../config/rgw/rgw.md#SP_d4n_writecache_enabled) |

**作用：** Enables the D4N (Data Delivery Network) **write-back cache**. When `true`, writes are staged in the local D4N cache layer (SSD path or Redis) before reaching the backend store.

**何时使用：** Experimental edge/cache scenarios to reduce write latency. Requires `rgw_filter = d4n` — not for standard production RGW on RADOS alone.

**相关选项：**

- `rgw_filter` = `d4n` (required)
- `rgw_d4n_l1_datacache_persistent_path`, `rgw_d4n_address`, `rgw_d4n_l1_datacache_disk_reserve`, `rgw_d4n_cache_cleaning_interval`

**示例：**

```bash
ceph config set client.rgw rgw_filter d4n
ceph config set client.rgw d4n_writecache_enabled true
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_datacache_persistent_path

| | |
|---|---|
| 类型 | Str · default `/tmp/rgw_datacache/` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_persistent_path) |

**作用：** path for the directory for storing the local cache objects data

**何时使用：** 元数据/quota/令牌缓存影响正确性延迟或 RGW 内存压力时调整。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_persistent_path "/tmp/rgw_datacache/"
ceph config get client.rgw rgw_d3n_l1_datacache_persistent_path
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/tmp/rgw_datacache/`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_d3n_l1_datacache_persistent_path)
iostat -x 5  # disk saturation
```

---

### rgw_d3n_l1_datacache_size

| | |
|---|---|
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_datacache_size](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_size) |

**作用：** datacache maximum size on disk in bytes

**何时使用：** 元数据/quota/令牌缓存影响正确性延迟或 RGW 内存压力时调整。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_size 1_G
ceph config get client.rgw rgw_d3n_l1_datacache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d3n_l1_datacache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d3n_l1_evict_cache_on_start

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_evict_cache_on_start) |

**作用：** clear the content of the persistent data cache directory on start

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d3n_l1_evict_cache_on_start
```

**寻找最优值：**

**调优模型：** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_eviction_policy

| | |
|---|---|
| 类型 | Str · enum: ["lru", "random"] · default `lru` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_eviction_policy](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_eviction_policy) |

**作用：** select the d3n cache eviction policy

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_eviction_policy lru
ceph config get client.rgw rgw_d3n_l1_eviction_policy
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["lru", "random"].
2. Default `lru` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_d3n_l1_fadvise

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_fadvise) |

**作用：** posix_fadvise() flag for access pattern of cache files

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_fadvise 4
ceph config get client.rgw rgw_d3n_l1_fadvise
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d3n_l1_fadvise
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d3n_l1_local_datacache_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_l1_local_datacache_enabled](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_local_datacache_enabled) |

**作用：** Enable datacenter-scale dataset delivery local cache

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_l1_local_datacache_enabled true
ceph config get client.rgw rgw_d3n_l1_local_datacache_enabled
```

**寻找最优值：**

**调优模型：** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_libaio_aio_num

| | |
|---|---|
| 类型 | Int · default `64` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_num) |

**作用：** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_num 64
ceph config get client.rgw rgw_d3n_libaio_aio_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d3n_libaio_aio_threads

| | |
|---|---|
| 类型 | Int · default `20` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d3n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_threads) |

**作用：** specifies the maximum number of worker threads that may be used by libaio

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_threads 20
ceph config get client.rgw rgw_d3n_libaio_aio_threads
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d3n_libaio_aio_threads
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_address

| | |
|---|---|
| 类型 | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_address](../../../config/rgw/rgw.md#SP_rgw_d4n_address) |

**作用：** address for the D4N Redis connection

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_address
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_address
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_backend_address

| | |
|---|---|
| 类型 | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_backend_address](../../../config/rgw/rgw.md#SP_rgw_d4n_backend_address) |

**作用：** The backend address used by D4N cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_backend_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_backend_address
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_backend_address
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_cache_cleaning_interval

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_cache_cleaning_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_cache_cleaning_interval) |

**作用：** This is the interval in seconds for invoking write cache cleaning process

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_d4n_cache_cleaning_interval 1000
ceph config get client.rgw rgw_d4n_cache_cleaning_interval
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_d4n_cache_cleaning_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_l1_datacache_address

| | |
|---|---|
| 类型 | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_l1_datacache_address](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_address) |

**作用：** local Redis cache address

**何时使用：** 元数据/quota/令牌缓存影响正确性延迟或 RGW 内存压力时调整。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_l1_datacache_address
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_l1_datacache_address
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_l1_datacache_disk_reserve

| | |
|---|---|
| 类型 | Size · default `1_G` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve) |

**作用：** amount of disk space to keep free for datacache

**何时使用：** 元数据/quota/令牌缓存影响正确性延迟或 RGW 内存压力时调整。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_disk_reserve 1_G
ceph config get client.rgw rgw_d4n_l1_datacache_disk_reserve
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_l1_datacache_disk_reserve
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_l1_datacache_persistent_path

| | |
|---|---|
| 类型 | Str · default `/tmp/rgw_d4n_datacache/` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_persistent_path) |

**作用：** path used for storing locally cached object data

**何时使用：** 元数据/quota/令牌缓存影响正确性延迟或 RGW 内存压力时调整。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path "/tmp/rgw_d4n_datacache/"
ceph config get client.rgw rgw_d4n_l1_datacache_persistent_path
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/tmp/rgw_d4n_datacache/`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_d4n_l1_datacache_persistent_path)
iostat -x 5  # disk saturation
```

---

### rgw_d4n_l1_evict_cache_on_start

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_evict_cache_on_start) |

**作用：** clear the contents of the persistent datacache on start

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d4n_l1_evict_cache_on_start
```

**寻找最优值：**

**调优模型：** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d4n_l1_fadvise

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_fadvise) |

**作用：** posix_fadvise() flag for access pattern of cache files

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_fadvise 4
ceph config get client.rgw rgw_d4n_l1_fadvise
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_l1_fadvise
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_l1_write_open_flags

| | |
|---|---|
| 类型 | Uint · default `4096` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_l1_write_open_flags](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_write_open_flags) |

**作用：** cache files write 'man 2 open' 'file status flags' modifiers

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_l1_write_open_flags 4096
ceph config get client.rgw rgw_d4n_l1_write_open_flags
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `4096`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_l1_write_open_flags
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_libaio_aio_num

| | |
|---|---|
| 类型 | Int · default `64` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_num) |

**作用：** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_num 64
ceph config get client.rgw rgw_d4n_libaio_aio_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d4n_libaio_aio_threads

| | |
|---|---|
| 类型 | Int · default `20` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_d4n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_threads) |

**作用：** specifies the maximum number of worker threads that may be used by libaio

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_threads 20
ceph config get client.rgw rgw_d4n_libaio_aio_threads
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_libaio_aio_threads
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_local_rgw_address

| | |
|---|---|
| 类型 | Str · default `127.0.0.1:8000` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_local_rgw_address](../../../config/rgw/rgw.md#SP_rgw_d4n_local_rgw_address) |

**作用：** local RGW address

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_d4n_local_rgw_address "127.0.0.1:8000"
ceph config get client.rgw rgw_d4n_local_rgw_address
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `127.0.0.1:8000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_d4n_local_rgw_address
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_d4n_localweight_processing_interval

| | |
|---|---|
| 类型 | Int · default `3600` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_d4n_localweight_processing_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_localweight_processing_interval) |

**作用：** This is the interval in seconds for invoking local weight writer thread

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_d4n_localweight_processing_interval 3600
ceph config get client.rgw rgw_d4n_localweight_processing_interval
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Default `3600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_d4n_localweight_processing_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
