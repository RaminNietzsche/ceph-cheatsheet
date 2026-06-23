# Replication & sync

RGW config deep dive — 28 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_data_log_changes_size](#rgw_data_log_changes_size) | `1000` | Dev | Performance |
| [rgw_data_log_num_shards](#rgw_data_log_num_shards) | `128` | Advanced | Policy |
| [rgw_data_log_window](#rgw_data_log_window) | `30` | Advanced | Performance |
| [rgw_data_notify_interval_msec](#rgw_data_notify_interval_msec) | `0` | Advanced | Performance |
| [rgw_data_sync_poll_interval](#rgw_data_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_data_sync_spawn_window](#rgw_data_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_lfuda_sync_frequency](#rgw_lfuda_sync_frequency) | `60` | Advanced | Performance |
| [rgw_md_log_max_shards](#rgw_md_log_max_shards) | `64` | Advanced | Policy |
| [rgw_md_notify_interval_msec](#rgw_md_notify_interval_msec) | `200` | Advanced | Performance |
| [rgw_meta_sync_poll_interval](#rgw_meta_sync_poll_interval) | `20` | Dev | Performance |
| [rgw_meta_sync_spawn_window](#rgw_meta_sync_spawn_window) | `20` | Dev | Performance |
| [rgw_run_sync_thread](#rgw_run_sync_thread) | `True` | Advanced | Policy |
| [rgw_sync_data_full_inject_err_probability](#rgw_sync_data_full_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_data_inject_err_probability](#rgw_sync_data_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_lease_period](#rgw_sync_lease_period) | `2_min` | Dev | Performance |
| [rgw_sync_log_trim_concurrent_buckets](#rgw_sync_log_trim_concurrent_buckets) | `4` | Advanced | Performance |
| [rgw_sync_log_trim_interval](#rgw_sync_log_trim_interval) | `20_min` | Advanced | Performance |
| [rgw_sync_log_trim_max_buckets](#rgw_sync_log_trim_max_buckets) | `16` | Advanced | Policy |
| [rgw_sync_log_trim_min_cold_buckets](#rgw_sync_log_trim_min_cold_buckets) | `4` | Advanced | Performance |
| [rgw_sync_meta_inject_err_probability](#rgw_sync_meta_inject_err_probability) | `0` | Dev | Dev |
| [rgw_sync_obj_etag_verify](#rgw_sync_obj_etag_verify) | `False` | Advanced | Policy |
| [rgw_sync_trace_history_size](#rgw_sync_trace_history_size) | `4_K` | Advanced | Performance |
| [rgw_sync_trace_per_node_log_size](#rgw_sync_trace_per_node_log_size) | `32` | Advanced | Performance |
| [rgw_sync_trace_servicemap_update_interval](#rgw_sync_trace_servicemap_update_interval) | `10` | Advanced | Performance |
| [rgw_user_quota_bucket_sync_interval](#rgw_user_quota_bucket_sync_interval) | `3_min` | Advanced | Performance |
| [rgw_user_quota_sync_idle_users](#rgw_user_quota_sync_idle_users) | `False` | Advanced | Policy |
| [rgw_user_quota_sync_interval](#rgw_user_quota_sync_interval) | `1_day` | Advanced | Performance |
| [rgw_user_quota_sync_wait_time](#rgw_user_quota_sync_wait_time) | `1_day` | Advanced | Performance |

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

### rgw_data_log_changes_size

| | |
|---|---|
| Type | Int · default `1000` · **Dev** |
| Table | [rgw.md#SP_rgw_data_log_changes_size](../../config/rgw/rgw.md#SP_rgw_data_log_changes_size) |

**What it does:** Max size of pending changes in data log

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_data_log_changes_size 1000
ceph config get client.rgw rgw_data_log_changes_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_data_log_changes_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_data_log_num_shards

| | |
|---|---|
| Type | Int · default `128` · **Advanced** |
| Table | [rgw.md#SP_rgw_data_log_num_shards](../../config/rgw/rgw.md#SP_rgw_data_log_num_shards) |

**What it does:** Number of data log shards

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_data_log_num_shards 128
ceph config get client.rgw rgw_data_log_num_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `128` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_data_log_window

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [rgw.md#SP_rgw_data_log_window](../../config/rgw/rgw.md#SP_rgw_data_log_window) |

**What it does:** Data log time window

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_data_log_window 30
ceph config get client.rgw rgw_data_log_window
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline `30` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**Signals:** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_data_log_window
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_data_notify_interval_msec

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_data_notify_interval_msec](../../config/rgw/rgw.md#SP_rgw_data_notify_interval_msec) |

**What it does:** data changes notification interval to followers

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_data_notify_interval_msec 60
ceph config get client.rgw rgw_data_notify_interval_msec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `0` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_notify_interval_msec
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_poll_interval

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_data_sync_poll_interval](../../config/rgw/rgw.md#SP_rgw_data_sync_poll_interval) |

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_data_sync_poll_interval 20
ceph config get client.rgw rgw_data_sync_poll_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_data_sync_poll_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_data_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_data_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_data_sync_spawn_window) |

**When to use:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**Example:**

```bash
ceph config set client.rgw rgw_data_sync_spawn_window 20
ceph config get client.rgw rgw_data_sync_spawn_window
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**Signals:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_data_sync_spawn_window
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_lfuda_sync_frequency

| | |
|---|---|
| Type | Int · default `60` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_lfuda_sync_frequency](../../config/rgw/rgw.md#SP_rgw_lfuda_sync_frequency) |

**What it does:** LFUDA variables' sync frequency in seconds

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_lfuda_sync_frequency 60
ceph config get client.rgw rgw_lfuda_sync_frequency
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_lfuda_sync_frequency
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_md_log_max_shards

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [rgw.md#SP_rgw_md_log_max_shards](../../config/rgw/rgw.md#SP_rgw_md_log_max_shards) |

**What it does:** RGW number of metadata log shards

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_md_log_max_shards 64
ceph config get client.rgw rgw_md_log_max_shards
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `64` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_md_notify_interval_msec

| | |
|---|---|
| Type | Int · default `200` · **Advanced** |
| Table | [rgw.md#SP_rgw_md_notify_interval_msec](../../config/rgw/rgw.md#SP_rgw_md_notify_interval_msec) |

**What it does:** Length of time to aggregate metadata changes

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_md_notify_interval_msec 200
ceph config get client.rgw rgw_md_notify_interval_msec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `200` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_md_notify_interval_msec
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_poll_interval

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_meta_sync_poll_interval](../../config/rgw/rgw.md#SP_rgw_meta_sync_poll_interval) |

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_meta_sync_poll_interval 20
ceph config get client.rgw rgw_meta_sync_poll_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_meta_sync_poll_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_meta_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_meta_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_meta_sync_spawn_window) |

**When to use:**

- **Increase** when multisite replication lag grows.
- **Decrease** when sync load competes with client I/O.

**Example:**

```bash
ceph config set client.rgw rgw_meta_sync_spawn_window 20
ceph config get client.rgw rgw_meta_sync_spawn_window
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20` limits parallel sync coroutines per bucket/zone.
2. **Increase** when multisite lag grows and RGW CPU headroom exists.
3. **Decrease** if sync threads starve client-facing requests or OSDs spike.

**Signals:** `radosgw-admin sync status`, data/meta sync lag, RGW load average.

```bash
ceph config get client.rgw rgw_meta_sync_spawn_window
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
radosgw-admin sync status
```

---

### rgw_run_sync_thread

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_run_sync_thread](../../config/rgw/rgw.md#SP_rgw_run_sync_thread) |

**What it does:** Should run sync thread

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_run_sync_thread false
ceph config get client.rgw rgw_run_sync_thread
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_sync_data_full_inject_err_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_sync_data_full_inject_err_probability](../../config/rgw/rgw.md#SP_rgw_sync_data_full_inject_err_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_sync_data_full_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_full_inject_err_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_data_inject_err_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_sync_data_inject_err_probability](../../config/rgw/rgw.md#SP_rgw_sync_data_inject_err_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_sync_data_inject_err_probability 0
ceph config get client.rgw rgw_sync_data_inject_err_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_lease_period

| | |
|---|---|
| Type | Int · default `2_min` · **Dev** |
| Table | [rgw.md#SP_rgw_sync_lease_period](../../config/rgw/rgw.md#SP_rgw_sync_lease_period) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_sync_lease_period 2_min
ceph config get client.rgw rgw_sync_lease_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `2_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_lease_period
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_concurrent_buckets

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_concurrent_buckets](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_concurrent_buckets) |

**What it does:** Maximum number of buckets to trim in parallel

**When to use:**

- **Increase** when RGW queues requests but CPU is not saturated.
- **Decrease** when latency spikes or CPU context-switch overhead grows.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_concurrent_buckets 4
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at `4` under peak concurrent clients.
2. Monitor RGW CPU, `rgw_throttle` counters, and client p99.
3. Increase if RGW CPU is low but requests queue; decrease if CPU saturates or latency spikes.
4. Pair with `rgw_frontends` thread count — frontend and RADOS concurrency move together.

**Signals:** 503/slowdown responses, high `active_requests` vs `max_concurrent`.

```bash
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_interval

| | |
|---|---|
| Type | Int · default `20_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_interval](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_interval) |

**What it does:** Sync log trim interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_interval 20_min
ceph config get client.rgw rgw_sync_log_trim_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `20_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_log_trim_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_log_trim_max_buckets

| | |
|---|---|
| Type | Int · default `16` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_max_buckets](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_max_buckets) |

**What it does:** Maximum number of buckets to trim per interval

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_max_buckets 16
ceph config get client.rgw rgw_sync_log_trim_max_buckets
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `16` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sync_log_trim_min_cold_buckets

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_min_cold_buckets](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_min_cold_buckets) |

**What it does:** Minimum number of cold buckets to trim per interval

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_min_cold_buckets 4
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_log_trim_min_cold_buckets
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_meta_inject_err_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_sync_meta_inject_err_probability](../../config/rgw/rgw.md#SP_rgw_sync_meta_inject_err_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_sync_meta_inject_err_probability 0
ceph config get client.rgw rgw_sync_meta_inject_err_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_sync_obj_etag_verify

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_obj_etag_verify](../../config/rgw/rgw.md#SP_rgw_sync_obj_etag_verify) |

**What it does:** Verify if the object copied from remote is identical to its source

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_sync_obj_etag_verify true
ceph config get client.rgw rgw_sync_obj_etag_verify
```

**Finding optimal value:**

**Tuning model:** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_sync_trace_history_size

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_trace_history_size](../../config/rgw/rgw.md#SP_rgw_sync_trace_history_size) |

**What it does:** Sync trace history size

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_trace_history_size 4_K
ceph config get client.rgw rgw_sync_trace_history_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_history_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_per_node_log_size

| | |
|---|---|
| Type | Int · default `32` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_trace_per_node_log_size](../../config/rgw/rgw.md#SP_rgw_sync_trace_per_node_log_size) |

**What it does:** Sync trace per-node log size

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_trace_per_node_log_size 32
ceph config get client.rgw rgw_sync_trace_per_node_log_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sync_trace_per_node_log_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_sync_trace_servicemap_update_interval

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_trace_servicemap_update_interval](../../config/rgw/rgw.md#SP_rgw_sync_trace_servicemap_update_interval) |

**What it does:** Sync-trace service-map update interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_sync_trace_servicemap_update_interval 10
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_bucket_sync_interval

| | |
|---|---|
| Type | Int · default `3_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_bucket_sync_interval](../../config/rgw/rgw.md#SP_rgw_user_quota_bucket_sync_interval) |

**What it does:** User quota bucket sync interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_bucket_sync_interval 3_min
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `3_min` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_idle_users

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_sync_idle_users](../../config/rgw/rgw.md#SP_rgw_user_quota_sync_idle_users) |

**What it does:** Should sync idle users quota

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_sync_idle_users true
ceph config get client.rgw rgw_user_quota_sync_idle_users
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_quota_sync_interval

| | |
|---|---|
| Type | Int · default `1_day` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_sync_interval](../../config/rgw/rgw.md#SP_rgw_user_quota_sync_interval) |

**What it does:** User quota sync interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_sync_interval 1_day
ceph config get client.rgw rgw_user_quota_sync_interval
radosgw-admin sync status
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `1_day` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_user_quota_sync_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_user_quota_sync_wait_time

| | |
|---|---|
| Type | Int · default `1_day` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_sync_wait_time](../../config/rgw/rgw.md#SP_rgw_user_quota_sync_wait_time) |

**What it does:** User quota full-sync wait time

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_sync_wait_time 1_day
ceph config get client.rgw rgw_user_quota_sync_wait_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `1_day` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_user_quota_sync_wait_time
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
