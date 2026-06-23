# Core runtime

راهنمای عمیق پیکربندی RGW — 16 گزینه. [← نمای کلی پیکربندی RGW](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rgw_data](#rgw_data) | `/var/lib/ceph/radosgw/$cluster-$id` | Advanced | عملکرد |
| [rgw_dedup_min_obj_size_for_dedup](#rgw_dedup_min_obj_size_for_dedup) | `64_K` | Advanced | عملکرد |
| [rgw_dedup_split_obj_head](#rgw_dedup_split_obj_head) | `True` | Advanced | سیاست |
| [rgw_expose_bucket](#rgw_expose_bucket) | `False` | Advanced | سیاست |
| [rgw_filter](#rgw_filter) | `none` | Advanced | معماری |
| [rgw_graceful_stop](#rgw_graceful_stop) | `False` | Advanced | سیاست |
| [rgw_healthcheck_disabling_path](#rgw_healthcheck_disabling_path) | `(empty)` | Dev | ظرفیت |
| [rgw_json_config](#rgw_json_config) | `/var/lib/ceph/radosgw/config.json` | Advanced | عملکرد |
| [rgw_mime_types_file](#rgw_mime_types_file) | `/etc/mime.types` | Basic | ظرفیت |
| [rgw_numa_node](#rgw_numa_node) | `-1` | Advanced | سیاست |
| [rgw_op_tracing](#rgw_op_tracing) | `False` | Advanced | سیاست |
| [rgw_parquet_buffer_size](#rgw_parquet_buffer_size) | `16_M` | Advanced | عملکرد |
| [rgw_rados_pool_autoscale_bias](#rgw_rados_pool_autoscale_bias) | `4` | Advanced | عملکرد |
| [rgw_rados_pool_recovery_priority](#rgw_rados_pool_recovery_priority) | `5` | Advanced | عملکرد |
| [rgw_rados_tracing](#rgw_rados_tracing) | `False` | Advanced | سیاست |
| [rgw_script_uri](#rgw_script_uri) | `(empty)` | Dev | اتصال |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری API، محدودیت tenant |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه pool |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش OSD/RGW |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **معماری** | backend، توپولوژی چندسایته — نه جستجوی عددی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/radosgw/$cluster-$id` · **Advanced** |
| جدول | [rgw.md#SP_rgw_data](../../../config/rgw/rgw.md#SP_rgw_data) |

**کارکرد:** Alternative location for RGW configuration.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_data "/var/lib/ceph/radosgw/$cluster-$id"
ceph config get client.rgw rgw_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_min_obj_size_for_dedup

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dedup_min_obj_size_for_dedup](../../../config/rgw/rgw.md#SP_rgw_dedup_min_obj_size_for_dedup) |

**کارکرد:** The minimum RGW object size for dedup (0 means no minimum size for dedup).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_dedup_min_obj_size_for_dedup 64_K
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dedup_min_obj_size_for_dedup
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dedup_split_obj_head

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rgw.md#SP_rgw_dedup_split_obj_head](../../../config/rgw/rgw.md#SP_rgw_dedup_split_obj_head) |

**کارکرد:** Enables the split-head functionality

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_dedup_split_obj_head false
ceph config get client.rgw rgw_dedup_split_obj_head
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_expose_bucket

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_expose_bucket](../../../config/rgw/rgw.md#SP_rgw_expose_bucket) |

**کارکرد:** Send Bucket HTTP header with the response

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_expose_bucket true
ceph config get client.rgw rgw_expose_bucket
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_filter

| | |
|---|---|
| نوع | Str · enum: ["none", "base", "d4n"] · default `none` · **Advanced** |
| جدول | [rgw.md#SP_rgw_filter](../../../config/rgw/rgw.md#SP_rgw_filter) |

**کارکرد:** experimental Option to set a filter

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_filter none
ceph config get client.rgw rgw_filter
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Architecture

1. Valid values: ["none", "base", "d4n"].
2. Default `none` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_graceful_stop

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_graceful_stop](../../../config/rgw/rgw.md#SP_rgw_graceful_stop) |

**کارکرد:** Delay the shutdown until all outstanding requests have completed

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_graceful_stop true
ceph config get client.rgw rgw_graceful_stop
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_healthcheck_disabling_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_healthcheck_disabling_path](../../../config/rgw/rgw.md#SP_rgw_healthcheck_disabling_path) |

**کارکرد:** Swift health check api can be disabled if a file can be accessed in this path.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_healthcheck_disabling_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_healthcheck_disabling_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_healthcheck_disabling_path)
iostat -x 5  # disk saturation
```

---

### rgw_json_config

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/radosgw/config.json` · **Advanced** |
| جدول | [rgw.md#SP_rgw_json_config](../../../config/rgw/rgw.md#SP_rgw_json_config) |

**کارکرد:** Path to a json file that contains the static zone and zonegroup configuration. Requires rgw_config_store=json.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_json_config "/var/lib/ceph/radosgw/config.json"
ceph config get client.rgw rgw_json_config
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `/var/lib/ceph/radosgw/config.json`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_json_config
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_mime_types_file

| | |
|---|---|
| نوع | Str · default `/etc/mime.types` · **Basic** |
| جدول | [rgw.md#SP_rgw_mime_types_file](../../../config/rgw/rgw.md#SP_rgw_mime_types_file) |

**کارکرد:** Path to local mime types file

**زمان استفاده:** رفتار اصلی RGW — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_mime_types_file "/etc/mime.types"
ceph config get client.rgw rgw_mime_types_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/etc/mime.types`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_mime_types_file)
iostat -x 5  # disk saturation
```

---

### rgw_numa_node

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rgw.md#SP_rgw_numa_node](../../../config/rgw/rgw.md#SP_rgw_numa_node) |

**کارکرد:** set the RGW daemon's CPU affinity to a NUMA node (-1 for none)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_numa_node -1
ceph config get client.rgw rgw_numa_node
ceph orch restart rgw
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_op_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_op_tracing](../../../config/rgw/rgw.md#SP_rgw_op_tracing) |

**کارکرد:** Enables LTTng-UST operator tracepoints.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_op_tracing true
ceph config get client.rgw rgw_op_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_parquet_buffer_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [rgw.md#SP_rgw_parquet_buffer_size](../../../config/rgw/rgw.md#SP_rgw_parquet_buffer_size) |

**کارکرد:** the Maximum parquet buffer size, a limit to memory consumption for parquet reading operations.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_parquet_buffer_size 16_M
ceph config get client.rgw rgw_parquet_buffer_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_parquet_buffer_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_rados_pool_autoscale_bias

| | |
|---|---|
| نوع | Float · default `4` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rados_pool_autoscale_bias](../../../config/rgw/rgw.md#SP_rgw_rados_pool_autoscale_bias) |

**کارکرد:** pg_autoscale_bias value for RGW metadata (omap-heavy) pools

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_rados_pool_autoscale_bias 4
ceph config get client.rgw rgw_rados_pool_autoscale_bias
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_autoscale_bias
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `0.01`, max `100000`.

---

### rgw_rados_pool_recovery_priority

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rados_pool_recovery_priority](../../../config/rgw/rgw.md#SP_rgw_rados_pool_recovery_priority) |

**کارکرد:** recovery_priority value for RGW metadata (omap-heavy) pools

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client.rgw rgw_rados_pool_recovery_priority 5
ceph config get client.rgw rgw_rados_pool_recovery_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**سیگنال‌ها:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_rados_pool_recovery_priority
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**محدوده:** min `-10`, max `10`.

---

### rgw_rados_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rgw.md#SP_rgw_rados_tracing](../../../config/rgw/rgw.md#SP_rgw_rados_tracing) |

**کارکرد:** Enables LTTng-UST tracepoints.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client.rgw rgw_rados_tracing true
ceph config get client.rgw rgw_rados_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_script_uri

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [rgw.md#SP_rgw_script_uri](../../../config/rgw/rgw.md#SP_rgw_script_uri) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client.rgw rgw_script_uri "https://service.example.com/"
ceph config get client.rgw rgw_script_uri
# curl -k <url>  # from each RGW node
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_script_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← نمای کلی پیکربندی RGW](../OVERVIEW.md)
