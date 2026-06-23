# Performance and concurrency

RGW config deep dive — 17 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_list_bucket_min_readahead](#rgw_list_bucket_min_readahead) | `1000` | Advanced |
| [rgw_list_buckets_max_chunk](#rgw_list_buckets_max_chunk) | `1000` | Advanced |
| [rgw_max_chunk_size](#rgw_max_chunk_size) | `4_M` | Advanced |
| [rgw_max_concurrent_requests](#rgw_max_concurrent_requests) | `1024` | Basic |
| [rgw_max_copy_obj_concurrent_io](#rgw_max_copy_obj_concurrent_io) | `10` | Advanced |
| [rgw_max_objs_per_shard](#rgw_max_objs_per_shard) | `100000` | Basic |
| [rgw_multi_obj_del_max_aio](#rgw_multi_obj_del_max_aio) | `16` | Advanced |
| [rgw_num_async_rados_threads](#rgw_num_async_rados_threads) | `32` | Advanced |
| [rgw_num_control_oids](#rgw_num_control_oids) | `8` | Advanced |
| [rgw_obj_stripe_size](#rgw_obj_stripe_size) | `4_M` | Advanced |
| [rgw_objexp_chunk_size](#rgw_objexp_chunk_size) | `100` | Dev |
| [rgw_op_thread_suicide_timeout](#rgw_op_thread_suicide_timeout) | `0` | Dev |
| [rgw_op_thread_timeout](#rgw_op_thread_timeout) | `10_min` | Dev |
| [rgw_redis_connection_pool_size](#rgw_redis_connection_pool_size) | `512` | Basic |
| [rgw_restore_max_objs](#rgw_restore_max_objs) | `32` | Advanced |
| [rgw_restore_processor_period](#rgw_restore_processor_period) | `15_min` | Advanced |
| [rgw_thread_pool_size](#rgw_thread_pool_size) | `512` | Basic |

---

### rgw_list_bucket_min_readahead

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_list_bucket_min_readahead](../../config/rgw/rgw.md#SP_rgw_list_bucket_min_readahead) |

**What it does:** Minimum number of entries to request from rados for bucket listing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_list_bucket_min_readahead 1000
ceph config get client.rgw rgw_list_bucket_min_readahead
```

**Finding optimal value:** Start from upstream default (`1000`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_list_buckets_max_chunk

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_list_buckets_max_chunk](../../config/rgw/rgw.md#SP_rgw_list_buckets_max_chunk) |

**What it does:** Max number of buckets to retrieve in a single listing operation

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_list_buckets_max_chunk 1000
ceph config get client.rgw rgw_list_buckets_max_chunk
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1000`) matches S3 compatibility for most workloads.

---

### rgw_max_chunk_size

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_chunk_size](../../config/rgw/rgw.md#SP_rgw_max_chunk_size) |

**What it does:** The maximum RGW chunk size.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_chunk_size 4_M
ceph config get client.rgw rgw_max_chunk_size
```

**Finding optimal value:** Start from upstream default (`4_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_max_concurrent_requests

| | |
|---|---|
| Type | Int · default `1024` · **Basic** |
| Table | [rgw.md#SP_rgw_max_concurrent_requests](../../config/rgw/rgw.md#SP_rgw_max_concurrent_requests) |

**What it does:** Maximum number of concurrent HTTP requests.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_concurrent_requests 1024
ceph config get client.rgw rgw_max_concurrent_requests
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Default: `1024`.

---

### rgw_max_copy_obj_concurrent_io

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_copy_obj_concurrent_io](../../config/rgw/rgw.md#SP_rgw_max_copy_obj_concurrent_io) |

**What it does:** Number of refcount operations to process concurrently when executing copy_obj

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_copy_obj_concurrent_io 10
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Default: `10`.

---

### rgw_max_objs_per_shard

| | |
|---|---|
| Type | Uint · default `100000` · **Basic** |
| Table | [rgw.md#SP_rgw_max_objs_per_shard](../../config/rgw/rgw.md#SP_rgw_max_objs_per_shard) |

**What it does:** Max objects per shard for dynamic resharding

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_objs_per_shard 100000
ceph config get client.rgw rgw_max_objs_per_shard
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`100000`) matches S3 compatibility for most workloads.

---

### rgw_multi_obj_del_max_aio

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_multi_obj_del_max_aio](../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) |

**What it does:** Max number of concurrent RADOS requests per multi-object delete request.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_multi_obj_del_max_aio 16
ceph config get client.rgw rgw_multi_obj_del_max_aio
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Default: `16`.

---

### rgw_num_async_rados_threads

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_num_async_rados_threads](../../config/rgw/rgw.md#SP_rgw_num_async_rados_threads) |

**What it does:** Number of concurrent RADOS operations in multisite sync

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_num_async_rados_threads 32
ceph config get client.rgw rgw_num_async_rados_threads
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`32`) matches S3 compatibility for most workloads.

---

### rgw_num_control_oids

| | |
|---|---|
| Type | Int · default `8` · **Advanced** |
| Table | [rgw.md#SP_rgw_num_control_oids](../../config/rgw/rgw.md#SP_rgw_num_control_oids) |

**What it does:** Number of control objects used for cross-RGW communication.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_num_control_oids 8
ceph config get client.rgw rgw_num_control_oids
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`8`) matches S3 compatibility for most workloads.

---

### rgw_obj_stripe_size

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [rgw.md#SP_rgw_obj_stripe_size](../../config/rgw/rgw.md#SP_rgw_obj_stripe_size) |

**What it does:** RGW object stripe size

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_obj_stripe_size 4_M
ceph config get client.rgw rgw_obj_stripe_size
```

**Finding optimal value:** Start from upstream default (`4_M`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_objexp_chunk_size

| | |
|---|---|
| Type | Uint · default `100` · **Dev** |
| Table | [rgw.md#SP_rgw_objexp_chunk_size](../../config/rgw/rgw.md#SP_rgw_objexp_chunk_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_objexp_chunk_size 100
ceph config get client.rgw rgw_objexp_chunk_size
```

**Finding optimal value:** Keep the upstream default (`100`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_op_thread_suicide_timeout

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_op_thread_suicide_timeout](../../config/rgw/rgw.md#SP_rgw_op_thread_suicide_timeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_op_thread_suicide_timeout 0
ceph config get client.rgw rgw_op_thread_suicide_timeout
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_op_thread_timeout

| | |
|---|---|
| Type | Int · default `10_min` · **Dev** |
| Table | [rgw.md#SP_rgw_op_thread_timeout](../../config/rgw/rgw.md#SP_rgw_op_thread_timeout) |

**What it does:** Timeout for async rados coroutine operations.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_op_thread_timeout 10_min
ceph config get client.rgw rgw_op_thread_timeout
```

**Finding optimal value:** Keep the upstream default (`10_min`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_redis_connection_pool_size

| | |
|---|---|
| Type | Int · default `512` · **Basic** |
| Table | [rgw.md#SP_rgw_redis_connection_pool_size](../../config/rgw/rgw.md#SP_rgw_redis_connection_pool_size) |

**What it does:** RGW connection pool size for Redis operation per D4N

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_redis_connection_pool_size 512
ceph config get client.rgw rgw_redis_connection_pool_size
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`512`) matches S3 compatibility for most workloads.

---

### rgw_restore_max_objs

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_restore_max_objs](../../config/rgw/rgw.md#SP_rgw_restore_max_objs) |

**What it does:** Number of shards for restore processing

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_restore_max_objs 32
ceph config get client.rgw rgw_restore_max_objs
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`32`) matches S3 compatibility for most workloads.

---

### rgw_restore_processor_period

| | |
|---|---|
| Type | Int · default `15_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_restore_processor_period](../../config/rgw/rgw.md#SP_rgw_restore_processor_period) |

**What it does:** Restore cycle run time

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_restore_processor_period 15_min
ceph config get client.rgw rgw_restore_processor_period
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`15_min`) only when logs show sync, cache, or timeout issues.

---

### rgw_thread_pool_size

| | |
|---|---|
| Type | Int · default `512` · **Basic** |
| Table | [rgw.md#SP_rgw_thread_pool_size](../../config/rgw/rgw.md#SP_rgw_thread_pool_size) |

**What it does:** RGW requests handling thread pool size.

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_thread_pool_size 512
ceph config get client.rgw rgw_thread_pool_size
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`512`) matches S3 compatibility for most workloads.

---


[← RGW config overview](OVERVIEW.md)
