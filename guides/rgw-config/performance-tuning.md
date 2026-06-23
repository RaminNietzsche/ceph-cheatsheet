# Performance and concurrency

RGW config deep dive — 17 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_list_bucket_min_readahead](#rgw_list_bucket_min_readahead) | `1000` | Advanced | Performance |
| [rgw_list_buckets_max_chunk](#rgw_list_buckets_max_chunk) | `1000` | Advanced | Policy |
| [rgw_max_chunk_size](#rgw_max_chunk_size) | `4_M` | Advanced | Performance |
| [rgw_max_concurrent_requests](#rgw_max_concurrent_requests) | `1024` | Basic | Performance |
| [rgw_max_copy_obj_concurrent_io](#rgw_max_copy_obj_concurrent_io) | `10` | Advanced | Performance |
| [rgw_max_objs_per_shard](#rgw_max_objs_per_shard) | `100000` | Basic | Policy |
| [rgw_multi_obj_del_max_aio](#rgw_multi_obj_del_max_aio) | `16` | Advanced | Performance |
| [rgw_num_async_rados_threads](#rgw_num_async_rados_threads) | `32` | Advanced | Performance |
| [rgw_num_control_oids](#rgw_num_control_oids) | `8` | Advanced | Policy |
| [rgw_obj_stripe_size](#rgw_obj_stripe_size) | `4_M` | Advanced | Performance |
| [rgw_objexp_chunk_size](#rgw_objexp_chunk_size) | `100` | Dev | Performance |
| [rgw_op_thread_suicide_timeout](#rgw_op_thread_suicide_timeout) | `0` | Dev | Dev |
| [rgw_op_thread_timeout](#rgw_op_thread_timeout) | `10_min` | Dev | Dev |
| [rgw_redis_connection_pool_size](#rgw_redis_connection_pool_size) | `512` | Basic | Performance |
| [rgw_restore_max_objs](#rgw_restore_max_objs) | `32` | Advanced | Policy |
| [rgw_restore_processor_period](#rgw_restore_processor_period) | `15_min` | Advanced | Performance |
| [rgw_thread_pool_size](#rgw_thread_pool_size) | `512` | Basic | Performance |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_list_bucket_min_readahead
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_max_chunk_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_max_concurrent_requests

| | |
|---|---|
| Type | Int · default `1024` · **Basic** |
| Table | [rgw.md#SP_rgw_max_concurrent_requests](../../config/rgw/rgw.md#SP_rgw_max_concurrent_requests) |

**What it does:** Maximum number of concurrent HTTP requests.

**When to use:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**Example:**

```bash
ceph config set client.rgw rgw_max_concurrent_requests 1024
ceph config get client.rgw rgw_max_concurrent_requests
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `1024` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_concurrent_requests
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_max_copy_obj_concurrent_io

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_copy_obj_concurrent_io](../../config/rgw/rgw.md#SP_rgw_max_copy_obj_concurrent_io) |

**What it does:** Number of refcount operations to process concurrently when executing copy_obj

**When to use:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**Example:**

```bash
ceph config set client.rgw rgw_max_copy_obj_concurrent_io 10
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `10` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_max_copy_obj_concurrent_io
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `100000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_multi_obj_del_max_aio

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_multi_obj_del_max_aio](../../config/rgw/rgw.md#SP_rgw_multi_obj_del_max_aio) |

**What it does:** Max number of concurrent RADOS requests per multi-object delete request.

**When to use:**

- **Increase** when listings/deletes on sharded buckets are slow and OSDs have headroom.
- **Decrease** when bucket-index pools show sustained load spikes or slow ops.

**Example:**

```bash
ceph config set client.rgw rgw_multi_obj_del_max_aio 16
ceph config get client.rgw rgw_multi_obj_del_max_aio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `16` with large bucket LIST, bulk DELETE, multipart completion.
2. Watch list/delete p99, RGW CPU, and OSD slow ops.
3. Increase in steps (~25%: e.g. 128 → 160 → 192 → 256) until latency stops improving.
4. **Decrease** under recovery pressure, `nearfull`, or sustained bucket-index pool load.

**Signals:** OSD `slow requests`, rising `rgw` throttle counters, flat client throughput.

```bash
ceph config get client.rgw rgw_multi_obj_del_max_aio
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
radosgw-admin bucket stats --bucket=BIG_BUCKET | jq '.num_shards'
```

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `32` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_num_async_rados_threads
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `8` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `4_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_obj_stripe_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `100` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_objexp_chunk_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

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

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10_min`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

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

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_redis_connection_pool_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `32` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

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

**Finding optimal value:**

**Tuning model:** Performance

1. Default `15_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_restore_processor_period
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_thread_pool_size

| | |
|---|---|
| Type | Int · default `512` · **Basic** |
| Table | [rgw.md#SP_rgw_thread_pool_size](../../config/rgw/rgw.md#SP_rgw_thread_pool_size) |

**What it does:** RGW requests handling thread pool size.

**When to use:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**Example:**

```bash
ceph config set client.rgw rgw_thread_pool_size 512
ceph config get client.rgw rgw_thread_pool_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `512` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_thread_pool_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
