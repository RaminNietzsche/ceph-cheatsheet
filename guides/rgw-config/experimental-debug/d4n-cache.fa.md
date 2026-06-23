# D4N / D3N cache

deep dive پیکربندی RGW — 22 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
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

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری API، محدودیت tenant |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه pool |
| **Performance** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Architecture** | backend، توپولوژی multisite — نه sweep عددی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

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
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_d4n_writecache_enabled](../../../config/rgw/rgw.md#SP_d4n_writecache_enabled) |

**کارکرد:** Enables the D4N (Data Delivery Network) **write-back cache**. When `true`, writes are staged in the local D4N cache layer (SSD path or Redis) before reaching the backend store.

**زمان استفاده:** Experimental edge/cache scenarios to reduce write latency. Requires `rgw_filter = d4n` — not for standard production RGW on RADOS alone.

**گزینه‌های مرتبط:**

- `rgw_filter` = `d4n` (required)
- `rgw_d4n_l1_datacache_persistent_path`, `rgw_d4n_address`, `rgw_d4n_l1_datacache_disk_reserve`, `rgw_d4n_cache_cleaning_interval`

**مثال:**

```bash
ceph config set client.rgw rgw_filter d4n
ceph config set client.rgw d4n_writecache_enabled true
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path /var/cache/rgw_d4n/
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_datacache_persistent_path

| | |
|---|---|
| نوع | Str · default `/tmp/rgw_datacache/` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_persistent_path) |

**کارکرد:** path for the directory for storing the local cache objects data

**زمان استفاده:** وقتی cache متادیتا/quota/token روی lag صحت یا فشار حافظه RGW اثر می‌گذارد.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_persistent_path "/tmp/rgw_datacache/"
ceph config get client.rgw rgw_d3n_l1_datacache_persistent_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

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
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_datacache_size](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_datacache_size) |

**کارکرد:** datacache maximum size on disk in bytes

**زمان استفاده:** وقتی cache متادیتا/quota/token روی lag صحت یا فشار حافظه RGW اثر می‌گذارد.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_datacache_size 1_G
ceph config get client.rgw rgw_d3n_l1_datacache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_evict_cache_on_start) |

**کارکرد:** clear the content of the persistent data cache directory on start

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d3n_l1_evict_cache_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_l1_eviction_policy

| | |
|---|---|
| نوع | Str · enum: ["lru", "random"] · default `lru` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_eviction_policy](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_eviction_policy) |

**کارکرد:** select the d3n cache eviction policy

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_eviction_policy lru
ceph config get client.rgw rgw_d3n_l1_eviction_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["lru", "random"].
2. Default `lru` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_d3n_l1_fadvise

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_fadvise) |

**کارکرد:** posix_fadvise() flag for access pattern of cache files

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_fadvise 4
ceph config get client.rgw rgw_d3n_l1_fadvise
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_l1_local_datacache_enabled](../../../config/rgw/rgw.md#SP_rgw_d3n_l1_local_datacache_enabled) |

**کارکرد:** Enable datacenter-scale dataset delivery local cache

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_l1_local_datacache_enabled true
ceph config get client.rgw rgw_d3n_l1_local_datacache_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d3n_libaio_aio_num

| | |
|---|---|
| نوع | Int · default `64` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_num) |

**کارکرد:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_num 64
ceph config get client.rgw rgw_d3n_libaio_aio_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d3n_libaio_aio_threads

| | |
|---|---|
| نوع | Int · default `20` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d3n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d3n_libaio_aio_threads) |

**کارکرد:** specifies the maximum number of worker threads that may be used by libaio

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d3n_libaio_aio_threads 20
ceph config get client.rgw rgw_d3n_libaio_aio_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_address](../../../config/rgw/rgw.md#SP_rgw_d4n_address) |

**کارکرد:** address for the D4N Redis connection

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_address
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_backend_address](../../../config/rgw/rgw.md#SP_rgw_d4n_backend_address) |

**کارکرد:** The backend address used by D4N cache

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_backend_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_backend_address
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `1000` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_cache_cleaning_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_cache_cleaning_interval) |

**کارکرد:** This is the interval in seconds for invoking write cache cleaning process

**زمان استفاده:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_cache_cleaning_interval 1000
ceph config get client.rgw rgw_d4n_cache_cleaning_interval
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**سیگنال‌ها:** rising RGW memory, repeated metadata lookups in logs.

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
| نوع | Str · default `127.0.0.1:6379` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_l1_datacache_address](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_address) |

**کارکرد:** local Redis cache address

**زمان استفاده:** وقتی cache متادیتا/quota/token روی lag صحت یا فشار حافظه RGW اثر می‌گذارد.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_address "127.0.0.1:6379"
ceph config get client.rgw rgw_d4n_l1_datacache_address
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `127.0.0.1:6379`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_disk_reserve) |

**کارکرد:** amount of disk space to keep free for datacache

**زمان استفاده:** وقتی cache متادیتا/quota/token روی lag صحت یا فشار حافظه RGW اثر می‌گذارد.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_disk_reserve 1_G
ceph config get client.rgw rgw_d4n_l1_datacache_disk_reserve
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Str · default `/tmp/rgw_d4n_datacache/` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_l1_datacache_persistent_path](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_datacache_persistent_path) |

**کارکرد:** path used for storing locally cached object data

**زمان استفاده:** وقتی cache متادیتا/quota/token روی lag صحت یا فشار حافظه RGW اثر می‌گذارد.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_datacache_persistent_path "/tmp/rgw_d4n_datacache/"
ceph config get client.rgw rgw_d4n_l1_datacache_persistent_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

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
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_l1_evict_cache_on_start](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_evict_cache_on_start) |

**کارکرد:** clear the contents of the persistent datacache on start

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_evict_cache_on_start false
ceph config get client.rgw rgw_d4n_l1_evict_cache_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_d4n_l1_fadvise

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_l1_fadvise](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_fadvise) |

**کارکرد:** posix_fadvise() flag for access pattern of cache files

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_fadvise 4
ceph config get client.rgw rgw_d4n_l1_fadvise
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Uint · default `4096` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_l1_write_open_flags](../../../config/rgw/rgw.md#SP_rgw_d4n_l1_write_open_flags) |

**کارکرد:** cache files write 'man 2 open' 'file status flags' modifiers

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_l1_write_open_flags 4096
ceph config get client.rgw rgw_d4n_l1_write_open_flags
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4096`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `64` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_libaio_aio_num](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_num) |

**کارکرد:** specifies the maximum number of simultaneous I/O requests that libaio expects to enqueue

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_num 64
ceph config get client.rgw rgw_d4n_libaio_aio_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_d4n_libaio_aio_threads

| | |
|---|---|
| نوع | Int · default `20` · **Advanced** |
| جدول | [rgw.md#SP_rgw_d4n_libaio_aio_threads](../../../config/rgw/rgw.md#SP_rgw_d4n_libaio_aio_threads) |

**کارکرد:** specifies the maximum number of worker threads that may be used by libaio

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_libaio_aio_threads 20
ceph config get client.rgw rgw_d4n_libaio_aio_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Str · default `127.0.0.1:8000` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_local_rgw_address](../../../config/rgw/rgw.md#SP_rgw_d4n_local_rgw_address) |

**کارکرد:** local RGW address

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_local_rgw_address "127.0.0.1:8000"
ceph config get client.rgw rgw_d4n_local_rgw_address
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `127.0.0.1:8000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| نوع | Int · default `3600` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_d4n_localweight_processing_interval](../../../config/rgw/rgw.md#SP_rgw_d4n_localweight_processing_interval) |

**کارکرد:** This is the interval in seconds for invoking local weight writer thread

**زمان استفاده:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**مثال:**

```bash
ceph config set client.rgw rgw_d4n_localweight_processing_interval 3600
ceph config get client.rgw rgw_d4n_localweight_processing_interval
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Default `3600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**سیگنال‌ها:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_d4n_localweight_processing_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
