# D4N / D3N cache

RGW config deep dive — 22 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [d4n_writecache_enabled](#d4n_writecache_enabled) | `False` | Advanced | Performance |
| [rgw_d3n_l1_datacache_persistent_path](#rgw_d3n_l1_datacache_persistent_path) | `/tmp/rgw_datacache/` | Advanced | Capacity |
| [rgw_d3n_l1_datacache_size](#rgw_d3n_l1_datacache_size) | `1_G` | Advanced | Performance |
| [rgw_d3n_l1_evict_cache_on_start](#rgw_d3n_l1_evict_cache_on_start) | `True` | Advanced | Performance |
| [rgw_d3n_l1_eviction_policy](#rgw_d3n_l1_eviction_policy) | `lru` | Advanced | Architecture |
| [rgw_d3n_l1_fadvise](#rgw_d3n_l1_fadvise) | `4` | Advanced | Performance |
| [rgw_d3n_l1_local_datacache_enabled](#rgw_d3n_l1_local_datacache_enabled) | `False` | Advanced | Performance |
| [rgw_d3n_libaio_aio_num](#rgw_d3n_libaio_aio_num) | `64` | Advanced | Policy |
| [rgw_d3n_libaio_aio_threads](#rgw_d3n_libaio_aio_threads) | `20` | Advanced | Performance |
| [rgw_d4n_address](#rgw_d4n_address) | `127.0.0.1:6379` | Advanced | Performance |
| [rgw_d4n_backend_address](#rgw_d4n_backend_address) | `127.0.0.1:6379` | Advanced | Performance |
| [rgw_d4n_cache_cleaning_interval](#rgw_d4n_cache_cleaning_interval) | `1000` | Advanced | Performance |
| [rgw_d4n_l1_datacache_address](#rgw_d4n_l1_datacache_address) | `127.0.0.1:6379` | Advanced | Performance |
| [rgw_d4n_l1_datacache_disk_reserve](#rgw_d4n_l1_datacache_disk_reserve) | `1_G` | Advanced | Performance |
| [rgw_d4n_l1_datacache_persistent_path](#rgw_d4n_l1_datacache_persistent_path) | `/tmp/rgw_d4n_datacache/` | Advanced | Capacity |
| [rgw_d4n_l1_evict_cache_on_start](#rgw_d4n_l1_evict_cache_on_start) | `True` | Advanced | Performance |
| [rgw_d4n_l1_fadvise](#rgw_d4n_l1_fadvise) | `4` | Advanced | Performance |
| [rgw_d4n_l1_write_open_flags](#rgw_d4n_l1_write_open_flags) | `4096` | Advanced | Performance |
| [rgw_d4n_libaio_aio_num](#rgw_d4n_libaio_aio_num) | `64` | Advanced | Policy |
| [rgw_d4n_libaio_aio_threads](#rgw_d4n_libaio_aio_threads) | `20` | Advanced | Performance |
| [rgw_d4n_local_rgw_address](#rgw_d4n_local_rgw_address) | `127.0.0.1:8000` | Advanced | Performance |
| [rgw_d4n_localweight_processing_interval](#rgw_d4n_localweight_processing_interval) | `3600` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

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
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_d4n_writecache_enabled](../../../config/rgw/rgw.md#SP_d4n_writecache_enabled) |

**What it does:** Enables the D4N (Data Delivery Network) **write-back cache**. When `true`, writes are staged in the local D4N cache layer (SSD path or Redis) before reaching the backend store.

**When to use:** Experimental edge/cache scenarios to reduce write latency. Requires `rgw_filter = d4n` — not for standard production RGW on RADOS alone.

**Related options:**

- `rgw_filter` = `d4n` (required)
- `rgw_d4n_l1_datacache_persistent_path`, `rgw_d4n_address`, `rgw_d4n_l1_datacache_disk_reserve`, `rgw_d4n_cache_cleaning_interval`

**Example:**

```bash
ceph config set client.rgw rgw_filter d4n
ceph config set client.rgw d4n_writecache_enabled true
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_datacache_persistent_path

| | |
|---|---|
| Type | Str · default `/tmp/rgw_datacache/` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_persistent_path) |

**What it does:** path for the directory for storing the local cache objects data

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_persistent_path "/tmp/rgw_datacache/"
ceph config get client.rgw rgw_d3n_l1_datacache_persistent_path
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Size · default `1_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_datacache_size](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_size) |

**What it does:** datacache maximum size on disk in bytes

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_size 1_G
ceph config get client.rgw rgw_d3n_l1_datacache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_evict_cache_on_start) |

**What it does:** clear the content of the persistent data cache directory on start

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d3n_l1_evict_cache_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_eviction_policy

| | |
|---|---|
| Type | Str · enum: ["lru", "random"] · default `lru` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_eviction_policy](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_eviction_policy) |

**What it does:** select the d3n cache eviction policy

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_eviction_policy lru
ceph config get client.rgw rgw_d3n_l1_eviction_policy
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["lru", "random"].
2. Default `lru` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_d3n_l1_fadvise

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_fadvise) |

**What it does:** posix_fadvise() flag for access pattern of cache files for example to bypass the page-cache - POSIX_FADV_DONTNEED=4

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_fadvise 4
ceph config get client.rgw rgw_d3n_l1_fadvise
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_local_datacache_enabled](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_local_datacache_enabled) |

**What it does:** Enable datacenter-scale dataset delivery local cache

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_local_datacache_enabled true
ceph config get client.rgw rgw_d3n_l1_local_datacache_enabled
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_libaio_aio_num

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_num) |

**What it does:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_thread_pool_size`](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size)

**Example:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_num 64
ceph config get client.rgw rgw_d3n_libaio_aio_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d3n_libaio_aio_threads

| | |
|---|---|
| Type | Int · default `20` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_threads) |

**What it does:** specifies the maximum number of worker threads that may be used by libaio

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_thread_pool_size`](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size)

**Example:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_threads 20
ceph config get client.rgw rgw_d3n_libaio_aio_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_address](../../../config/rgw/rgw.md#SP_rgw_d4n_address) |

**What it does:** address for the D4N Redis connection The current D4N implementation supports one Redis node which the D4N directory, policy, and overall filter communicate with. This default value is also the address that a Redis server with no additional configuration will use.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_address
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_backend_address](../../../config/rgw/rgw.md#SP_rgw_d4n_backend_address) |

**What it does:** The backend address used by D4N cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_backend_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_backend_address
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Int · default `1000` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_cache_cleaning_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_cache_cleaning_interval) |

**What it does:** This is the interval in seconds for invoking write cache cleaning process

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_cache_cleaning_interval 1000
ceph config get client.rgw rgw_d4n_cache_cleaning_interval
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

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
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_address](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_address) |

**What it does:** local Redis cache address This is the address used to configure the Redis cache backend connection. The default value is the same address used by Redis without any additional configuration. The SSD cache does not use this option.

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_l1_datacache_address
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Size · default `1_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve) |

**What it does:** amount of disk space to keep free for datacache The local SSD cache uses this option to determine how much disk space to reserve. The cache can grow until disk usage reaches (total disk space - reserved space).

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_disk_reserve 1_G
ceph config get client.rgw rgw_d4n_l1_datacache_disk_reserve
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `/tmp/rgw_d4n_datacache/` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_persistent_path) |

**What it does:** path used for storing locally cached object data One cache backend option for D4N is the local SSD, which uses this path to write and read object data. This is the default cache backend chosen by the D4N filter. Only the SSD cache backend uses this path for object data storage since the RedisDriver uses a Redis server instead and there are no additional cache backend implementations available at the moment.

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path "/tmp/rgw_d4n_datacache/"
ceph config get client.rgw rgw_d4n_l1_datacache_persistent_path
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_evict_cache_on_start) |

**What it does:** clear the contents of the persistent datacache on start The local SSD cache uses this option to clear the contents of the path supplied by the rgw_d4n_l1_datacache_persistent_path config option on start. If false, the path's contents will be retained.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d4n_l1_evict_cache_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d4n_l1_fadvise

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_fadvise) |

**What it does:** posix_fadvise() flag for access pattern of cache files For example, to bypass the page-cache - POSIX_FADV_DONTNEED=4

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_fadvise 4
ceph config get client.rgw rgw_d4n_l1_fadvise
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Uint · default `4096` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_write_open_flags](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_write_open_flags) |

**What it does:** cache files write 'man 2 open' 'file status flags' modifiers For example, to configure synchronized I/O, fcntl-linux.h defines (converted from octal) O_SYNC = 1052672 O_DSYNC = 4096 O_DIRECT = 16384 O_SYNC \

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_write_open_flags 4096
ceph config get client.rgw rgw_d4n_l1_write_open_flags
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4096`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Int · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_num) |

**What it does:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue This option is used by the SSD cache backend during initialization to set the maximum number of simultaneous I/O requests that libaio can expect to enqueue. It does not apply to the Redis cache backend.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_thread_pool_size`](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size)

**Example:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_num 64
ceph config get client.rgw rgw_d4n_libaio_aio_num
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d4n_libaio_aio_threads

| | |
|---|---|
| Type | Int · default `20` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_threads) |

**What it does:** specifies the maximum number of worker threads that may be used by libaio This option is used by the SSD cache backend during initialization to set the maximum number of worker threads libaio may use. It does not apply to the Redis cache backend.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_thread_pool_size`](../../../config/rgw/rgw.md#SP_rgw_thread_pool_size)

**Example:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_threads 20
ceph config get client.rgw rgw_d4n_libaio_aio_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · default `127.0.0.1:8000` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_local_rgw_address](../../../config/rgw/rgw.md#SP_rgw_d4n_local_rgw_address) |

**What it does:** local RGW address This is the address used to represent the local RGW in a distributed D4N system that involves remote RGWs.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_local_rgw_address "127.0.0.1:8000"
ceph config get client.rgw rgw_d4n_local_rgw_address
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1:8000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Int · default `3600` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_localweight_processing_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_localweight_processing_interval) |

**What it does:** This is the interval in seconds for invoking local weight writer thread

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_localweight_processing_interval 3600
ceph config get client.rgw rgw_d4n_localweight_processing_interval
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `3600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_d4n_localweight_processing_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
