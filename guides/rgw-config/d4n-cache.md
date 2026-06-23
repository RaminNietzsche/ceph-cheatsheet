# D4N / D3N cache

RGW config deep dive — 21 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_d3n_l1_datacache_persistent_path](#rgw_d3n_l1_datacache_persistent_path) | `/tmp/rgw_datacache/` | Advanced |
| [rgw_d3n_l1_datacache_size](#rgw_d3n_l1_datacache_size) | `1_G` | Advanced |
| [rgw_d3n_l1_evict_cache_on_start](#rgw_d3n_l1_evict_cache_on_start) | `True` | Advanced |
| [rgw_d3n_l1_eviction_policy](#rgw_d3n_l1_eviction_policy) | `lru` | Advanced |
| [rgw_d3n_l1_fadvise](#rgw_d3n_l1_fadvise) | `4` | Advanced |
| [rgw_d3n_l1_local_datacache_enabled](#rgw_d3n_l1_local_datacache_enabled) | `False` | Advanced |
| [rgw_d3n_libaio_aio_num](#rgw_d3n_libaio_aio_num) | `64` | Advanced |
| [rgw_d3n_libaio_aio_threads](#rgw_d3n_libaio_aio_threads) | `20` | Advanced |
| [rgw_d4n_address](#rgw_d4n_address) | `127.0.0.1:6379` | Advanced |
| [rgw_d4n_backend_address](#rgw_d4n_backend_address) | `127.0.0.1:6379` | Advanced |
| [rgw_d4n_cache_cleaning_interval](#rgw_d4n_cache_cleaning_interval) | `1000` | Advanced |
| [rgw_d4n_l1_datacache_address](#rgw_d4n_l1_datacache_address) | `127.0.0.1:6379` | Advanced |
| [rgw_d4n_l1_datacache_disk_reserve](#rgw_d4n_l1_datacache_disk_reserve) | `1_G` | Advanced |
| [rgw_d4n_l1_datacache_persistent_path](#rgw_d4n_l1_datacache_persistent_path) | `/tmp/rgw_d4n_datacache/` | Advanced |
| [rgw_d4n_l1_evict_cache_on_start](#rgw_d4n_l1_evict_cache_on_start) | `True` | Advanced |
| [rgw_d4n_l1_fadvise](#rgw_d4n_l1_fadvise) | `4` | Advanced |
| [rgw_d4n_l1_write_open_flags](#rgw_d4n_l1_write_open_flags) | `4096` | Advanced |
| [rgw_d4n_libaio_aio_num](#rgw_d4n_libaio_aio_num) | `64` | Advanced |
| [rgw_d4n_libaio_aio_threads](#rgw_d4n_libaio_aio_threads) | `20` | Advanced |
| [rgw_d4n_local_rgw_address](#rgw_d4n_local_rgw_address) | `127.0.0.1:8000` | Advanced |
| [rgw_d4n_localweight_processing_interval](#rgw_d4n_localweight_processing_interval) | `3600` | Advanced |

---

### rgw_d3n_l1_datacache_persistent_path

| | |
|---|---|
| Type | Str · default `/tmp/rgw_datacache/` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_datacache_persistent_path](../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_persistent_path) |

**What it does:** path for the directory for storing the local cache objects data

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_persistent_path "/tmp/rgw_datacache/"
ceph config get client.rgw rgw_d3n_l1_datacache_persistent_path
```

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/tmp/rgw_datacache/`) is fine when that path is on a separate volume.

---

### rgw_d3n_l1_datacache_size

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_datacache_size](../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_size) |

**What it does:** datacache maximum size on disk in bytes

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_size 1_G
ceph config get client.rgw rgw_d3n_l1_datacache_size
```

**Finding optimal value:** Start from upstream default (`1_G`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d3n_l1_evict_cache_on_start

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_evict_cache_on_start](../../config/rgw/rgw.md#SP_rgw_d3n_l1_evict_cache_on_start) |

**What it does:** clear the content of the persistent data cache directory on start

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_evict_cache_on_start True
ceph config get client.rgw rgw_d3n_l1_evict_cache_on_start
```

**Finding optimal value:** Enable only when the related metrics or correctness path needs it. Default (`True`) is usually optimal for standard deployments.

---

### rgw_d3n_l1_eviction_policy

| | |
|---|---|
| Type | Str · default `lru` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_eviction_policy](../../config/rgw/rgw.md#SP_rgw_d3n_l1_eviction_policy) |

**What it does:** select the d3n cache eviction policy

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_eviction_policy lru
ceph config get client.rgw rgw_d3n_l1_eviction_policy
```

**Finding optimal value:** Choose from valid values ["lru", "random"]. Default `lru` is optimal unless your backend or integration requires another value.

---

### rgw_d3n_l1_fadvise

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_fadvise](../../config/rgw/rgw.md#SP_rgw_d3n_l1_fadvise) |

**What it does:** posix_fadvise() flag for access pattern of cache files

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_fadvise 4
ceph config get client.rgw rgw_d3n_l1_fadvise
```

**Finding optimal value:** Start from upstream default (`4`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d3n_l1_local_datacache_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_l1_local_datacache_enabled](../../config/rgw/rgw.md#SP_rgw_d3n_l1_local_datacache_enabled) |

**What it does:** Enable datacenter-scale dataset delivery local cache

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_l1_local_datacache_enabled False
ceph config get client.rgw rgw_d3n_l1_local_datacache_enabled
```

**Finding optimal value:** Enable only when the related metrics or correctness path needs it. Default (`False`) is usually optimal for standard deployments.

---

### rgw_d3n_libaio_aio_num

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_libaio_aio_num](../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_num) |

**What it does:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_num 64
ceph config get client.rgw rgw_d3n_libaio_aio_num
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`64`) matches S3 compatibility for most workloads.

---

### rgw_d3n_libaio_aio_threads

| | |
|---|---|
| Type | Int · default `20` · **Advanced** |
| Table | [rgw.md#SP_rgw_d3n_libaio_aio_threads](../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_threads) |

**What it does:** specifies the maximum number of worker threads that may be used by libaio

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_threads 20
ceph config get client.rgw rgw_d3n_libaio_aio_threads
```

**Finding optimal value:** Start from upstream default (`20`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_address

| | |
|---|---|
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_address](../../config/rgw/rgw.md#SP_rgw_d4n_address) |

**What it does:** address for the D4N Redis connection

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_address 127.0.0.1:6379
ceph config get client.rgw rgw_d4n_address
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`127.0.0.1:6379`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_backend_address

| | |
|---|---|
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_backend_address](../../config/rgw/rgw.md#SP_rgw_d4n_backend_address) |

**What it does:** The backend address used by D4N cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_backend_address 127.0.0.1:6379
ceph config get client.rgw rgw_d4n_backend_address
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`127.0.0.1:6379`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_cache_cleaning_interval

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_cache_cleaning_interval](../../config/rgw/rgw.md#SP_rgw_d4n_cache_cleaning_interval) |

**What it does:** This is the interval in seconds for invoking write cache cleaning process

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_cache_cleaning_interval 1000
ceph config get client.rgw rgw_d4n_cache_cleaning_interval
ceph orch restart rgw
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`1000`) while watching RGW RSS.

---

### rgw_d4n_l1_datacache_address

| | |
|---|---|
| Type | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_address](../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_address) |

**What it does:** local Redis cache address

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_address 127.0.0.1:6379
ceph config get client.rgw rgw_d4n_l1_datacache_address
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`127.0.0.1:6379`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_l1_datacache_disk_reserve

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve](../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve) |

**What it does:** amount of disk space to keep free for datacache

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_disk_reserve 1_G
ceph config get client.rgw rgw_d4n_l1_datacache_disk_reserve
```

**Finding optimal value:** Start from upstream default (`1_G`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_l1_datacache_persistent_path

| | |
|---|---|
| Type | Str · default `/tmp/rgw_d4n_datacache/` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_datacache_persistent_path](../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_persistent_path) |

**What it does:** path used for storing locally cached object data

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path "/tmp/rgw_d4n_datacache/"
ceph config get client.rgw rgw_d4n_l1_datacache_persistent_path
```

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/tmp/rgw_d4n_datacache/`) is fine when that path is on a separate volume.

---

### rgw_d4n_l1_evict_cache_on_start

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_evict_cache_on_start](../../config/rgw/rgw.md#SP_rgw_d4n_l1_evict_cache_on_start) |

**What it does:** clear the contents of the persistent datacache on start

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_evict_cache_on_start True
ceph config get client.rgw rgw_d4n_l1_evict_cache_on_start
```

**Finding optimal value:** Enable only when the related metrics or correctness path needs it. Default (`True`) is usually optimal for standard deployments.

---

### rgw_d4n_l1_fadvise

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_fadvise](../../config/rgw/rgw.md#SP_rgw_d4n_l1_fadvise) |

**What it does:** posix_fadvise() flag for access pattern of cache files

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_fadvise 4
ceph config get client.rgw rgw_d4n_l1_fadvise
```

**Finding optimal value:** Start from upstream default (`4`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_l1_write_open_flags

| | |
|---|---|
| Type | Uint · default `4096` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_l1_write_open_flags](../../config/rgw/rgw.md#SP_rgw_d4n_l1_write_open_flags) |

**What it does:** cache files write 'man 2 open' 'file status flags' modifiers

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_l1_write_open_flags 4096
ceph config get client.rgw rgw_d4n_l1_write_open_flags
```

**Finding optimal value:** Start from upstream default (`4096`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_libaio_aio_num

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_libaio_aio_num](../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_num) |

**What it does:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_num 64
ceph config get client.rgw rgw_d4n_libaio_aio_num
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`64`) matches S3 compatibility for most workloads.

---

### rgw_d4n_libaio_aio_threads

| | |
|---|---|
| Type | Int · default `20` · **Advanced** |
| Table | [rgw.md#SP_rgw_d4n_libaio_aio_threads](../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_threads) |

**What it does:** specifies the maximum number of worker threads that may be used by libaio

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_threads 20
ceph config get client.rgw rgw_d4n_libaio_aio_threads
```

**Finding optimal value:** Start from upstream default (`20`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_local_rgw_address

| | |
|---|---|
| Type | Str · default `127.0.0.1:8000` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_local_rgw_address](../../config/rgw/rgw.md#SP_rgw_d4n_local_rgw_address) |

**What it does:** local RGW address

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_local_rgw_address 127.0.0.1:8000
ceph config get client.rgw rgw_d4n_local_rgw_address
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`127.0.0.1:8000`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_d4n_localweight_processing_interval

| | |
|---|---|
| Type | Int · default `3600` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_d4n_localweight_processing_interval](../../config/rgw/rgw.md#SP_rgw_d4n_localweight_processing_interval) |

**What it does:** This is the interval in seconds for invoking local weight writer thread

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_d4n_localweight_processing_interval 3600
ceph config get client.rgw rgw_d4n_localweight_processing_interval
ceph orch restart rgw
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`3600`) only when logs show sync, cache, or timeout issues.

---


[← RGW config overview](OVERVIEW.md)
