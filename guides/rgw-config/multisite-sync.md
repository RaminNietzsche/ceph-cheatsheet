# Multisite sync

RGW config deep dive — 28 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_data_log_changes_size](#rgw_data_log_changes_size) | `1000` | Dev |
| [rgw_data_log_num_shards](#rgw_data_log_num_shards) | `128` | Advanced |
| [rgw_data_log_window](#rgw_data_log_window) | `30` | Advanced |
| [rgw_data_notify_interval_msec](#rgw_data_notify_interval_msec) | `0` | Advanced |
| [rgw_data_sync_poll_interval](#rgw_data_sync_poll_interval) | `20` | Dev |
| [rgw_data_sync_spawn_window](#rgw_data_sync_spawn_window) | `20` | Dev |
| [rgw_lfuda_sync_frequency](#rgw_lfuda_sync_frequency) | `60` | Advanced |
| [rgw_md_log_max_shards](#rgw_md_log_max_shards) | `64` | Advanced |
| [rgw_md_notify_interval_msec](#rgw_md_notify_interval_msec) | `200` | Advanced |
| [rgw_meta_sync_poll_interval](#rgw_meta_sync_poll_interval) | `20` | Dev |
| [rgw_meta_sync_spawn_window](#rgw_meta_sync_spawn_window) | `20` | Dev |
| [rgw_run_sync_thread](#rgw_run_sync_thread) | `True` | Advanced |
| [rgw_sync_data_full_inject_err_probability](#rgw_sync_data_full_inject_err_probability) | `0` | Dev |
| [rgw_sync_data_inject_err_probability](#rgw_sync_data_inject_err_probability) | `0` | Dev |
| [rgw_sync_lease_period](#rgw_sync_lease_period) | `2_min` | Dev |
| [rgw_sync_log_trim_concurrent_buckets](#rgw_sync_log_trim_concurrent_buckets) | `4` | Advanced |
| [rgw_sync_log_trim_interval](#rgw_sync_log_trim_interval) | `20_min` | Advanced |
| [rgw_sync_log_trim_max_buckets](#rgw_sync_log_trim_max_buckets) | `16` | Advanced |
| [rgw_sync_log_trim_min_cold_buckets](#rgw_sync_log_trim_min_cold_buckets) | `4` | Advanced |
| [rgw_sync_meta_inject_err_probability](#rgw_sync_meta_inject_err_probability) | `0` | Dev |
| [rgw_sync_obj_etag_verify](#rgw_sync_obj_etag_verify) | `False` | Advanced |
| [rgw_sync_trace_history_size](#rgw_sync_trace_history_size) | `4_K` | Advanced |
| [rgw_sync_trace_per_node_log_size](#rgw_sync_trace_per_node_log_size) | `32` | Advanced |
| [rgw_sync_trace_servicemap_update_interval](#rgw_sync_trace_servicemap_update_interval) | `10` | Advanced |
| [rgw_user_quota_bucket_sync_interval](#rgw_user_quota_bucket_sync_interval) | `3_min` | Advanced |
| [rgw_user_quota_sync_idle_users](#rgw_user_quota_sync_idle_users) | `False` | Advanced |
| [rgw_user_quota_sync_interval](#rgw_user_quota_sync_interval) | `1_day` | Advanced |
| [rgw_user_quota_sync_wait_time](#rgw_user_quota_sync_wait_time) | `1_day` | Advanced |

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

**Finding optimal value:** Keep the upstream default (`1000`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`128`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Start from upstream default (`30`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_data_notify_interval_msec

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_data_notify_interval_msec](../../config/rgw/rgw.md#SP_rgw_data_notify_interval_msec) |

**What it does:** data changes notification interval to followers

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_data_notify_interval_msec 0
ceph config get client.rgw rgw_data_notify_interval_msec
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`0`) only when logs show sync, cache, or timeout issues.

---

### rgw_data_sync_poll_interval

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_data_sync_poll_interval](../../config/rgw/rgw.md#SP_rgw_data_sync_poll_interval) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_data_sync_poll_interval 20
ceph config get client.rgw rgw_data_sync_poll_interval
```

**Finding optimal value:** Keep the upstream default (`20`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_data_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_data_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_data_sync_spawn_window) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_data_sync_spawn_window 20
ceph config get client.rgw rgw_data_sync_spawn_window
```

**Finding optimal value:** Keep the upstream default (`20`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Start from upstream default (`60`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`64`) matches S3 compatibility for most workloads.

---

### rgw_md_notify_interval_msec

| | |
|---|---|
| Type | Int · default `200` · **Advanced** |
| Table | [rgw.md#SP_rgw_md_notify_interval_msec](../../config/rgw/rgw.md#SP_rgw_md_notify_interval_msec) |

**What it does:** Length of time to aggregate metadata changes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_md_notify_interval_msec 200
ceph config get client.rgw rgw_md_notify_interval_msec
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`200`) only when logs show sync, cache, or timeout issues.

---

### rgw_meta_sync_poll_interval

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_meta_sync_poll_interval](../../config/rgw/rgw.md#SP_rgw_meta_sync_poll_interval) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_meta_sync_poll_interval 20
ceph config get client.rgw rgw_meta_sync_poll_interval
```

**Finding optimal value:** Keep the upstream default (`20`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_meta_sync_spawn_window

| | |
|---|---|
| Type | Int · default `20` · **Dev** |
| Table | [rgw.md#SP_rgw_meta_sync_spawn_window](../../config/rgw/rgw.md#SP_rgw_meta_sync_spawn_window) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_meta_sync_spawn_window 20
ceph config get client.rgw rgw_meta_sync_spawn_window
```

**Finding optimal value:** Keep the upstream default (`20`) in production. Enable or change only during targeted debugging sessions.

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
ceph config set client.rgw rgw_run_sync_thread True
ceph config get client.rgw rgw_run_sync_thread
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

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

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Keep the upstream default (`2_min`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_sync_log_trim_concurrent_buckets

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_concurrent_buckets](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_concurrent_buckets) |

**What it does:** Maximum number of buckets to trim in parallel

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_concurrent_buckets 4
ceph config get client.rgw rgw_sync_log_trim_concurrent_buckets
```

**Finding optimal value:** Performance sweep: baseline at default, then increase in steps while watching RGW CPU, request p99, and OSD slow ops. Optimal is the highest value before OSD or network saturation. Default: `4`.

---

### rgw_sync_log_trim_interval

| | |
|---|---|
| Type | Int · default `20_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_log_trim_interval](../../config/rgw/rgw.md#SP_rgw_sync_log_trim_interval) |

**What it does:** Sync log trim interval

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_log_trim_interval 20_min
ceph config get client.rgw rgw_sync_log_trim_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`20_min`) only when logs show sync, cache, or timeout issues.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`16`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Start from upstream default (`4`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

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
ceph config set client.rgw rgw_sync_obj_etag_verify False
ceph config get client.rgw rgw_sync_obj_etag_verify
```

**Finding optimal value:** Security/compliance setting — prefer `true` in production unless a trusted lab requires `False`.

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

**Finding optimal value:** Start from upstream default (`4_K`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`32`) matches S3 compatibility for most workloads.

---

### rgw_sync_trace_servicemap_update_interval

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_sync_trace_servicemap_update_interval](../../config/rgw/rgw.md#SP_rgw_sync_trace_servicemap_update_interval) |

**What it does:** Sync-trace service-map update interval

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_sync_trace_servicemap_update_interval 10
ceph config get client.rgw rgw_sync_trace_servicemap_update_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`10`) only when logs show sync, cache, or timeout issues.

---

### rgw_user_quota_bucket_sync_interval

| | |
|---|---|
| Type | Int · default `3_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_bucket_sync_interval](../../config/rgw/rgw.md#SP_rgw_user_quota_bucket_sync_interval) |

**What it does:** User quota bucket sync interval

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_bucket_sync_interval 3_min
ceph config get client.rgw rgw_user_quota_bucket_sync_interval
```

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`3_min`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

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
ceph config set client.rgw rgw_user_quota_sync_idle_users False
ceph config get client.rgw rgw_user_quota_sync_idle_users
```

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`False`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

---

### rgw_user_quota_sync_interval

| | |
|---|---|
| Type | Int · default `1_day` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_quota_sync_interval](../../config/rgw/rgw.md#SP_rgw_user_quota_sync_interval) |

**What it does:** User quota sync interval

**When to use:** Multisite replication and sync tuning — adjust when lag or sync load is problematic.

**Example:**

```bash
ceph config set client.rgw rgw_user_quota_sync_interval 1_day
ceph config get client.rgw rgw_user_quota_sync_interval
```

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`1_day`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

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

**Finding optimal value:** Balance quota enforcement freshness vs RGW/CLS load. Start at default (`1_day`); shorten if users exceed limits before stats catch up, lengthen if quota sync dominates CPU.

---


[← RGW config overview](OVERVIEW.md)
