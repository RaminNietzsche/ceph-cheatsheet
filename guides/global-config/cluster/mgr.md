# Mgr

Global config deep dive — 11 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mgr_client_service_daemon_unregister_timeout](#mgr_client_service_daemon_unregister_timeout) | `1` | Dev | Dev |
| [mgr_connect_retry_interval](#mgr_connect_retry_interval) | `1` | Dev | Dev |
| [mgr_enable_op_tracker](#mgr_enable_op_tracker) | `True` | Advanced | Policy |
| [mgr_map_cache_enabled](#mgr_map_cache_enabled) | `True` | Dev | Dev |
| [mgr_num_op_tracker_shard](#mgr_num_op_tracker_shard) | `32` | Advanced | Performance |
| [mgr_op_complaint_time](#mgr_op_complaint_time) | `30` | Advanced | Performance |
| [mgr_op_history_duration](#mgr_op_history_duration) | `600` | Advanced | Performance |
| [mgr_op_history_size](#mgr_op_history_size) | `20` | Advanced | Performance |
| [mgr_op_history_slow_op_size](#mgr_op_history_slow_op_size) | `20` | Advanced | Performance |
| [mgr_op_history_slow_op_threshold](#mgr_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [mgr_op_log_threshold](#mgr_op_log_threshold) | `5` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mgr_client_service_daemon_unregister_timeout

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [mgr.md#SP_mgr_client_service_daemon_unregister_timeout](../../../config/global/mgr.md#SP_mgr_client_service_daemon_unregister_timeout) |

**What it does:** Time to wait during shutdown to deregister a service with the Manager

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_client_service_daemon_unregister_timeout 1
ceph config get mgr mgr_client_service_daemon_unregister_timeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_connect_retry_interval

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [mgr.md#SP_mgr_connect_retry_interval](../../../config/global/mgr.md#SP_mgr_connect_retry_interval) |

**What it does:** Manager reconnect retry interval

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_connect_retry_interval 1
ceph config get mgr mgr_connect_retry_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_enable_op_tracker

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mgr.md#SP_mgr_enable_op_tracker](../../../config/global/mgr.md#SP_mgr_enable_op_tracker) |

**What it does:** Enable / disable the Manager op tracker

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mgr mgr_enable_op_tracker false
ceph config get mgr mgr_enable_op_tracker
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_enable_op_tracker
ceph -s
ceph mgr dump
```

---

### mgr_map_cache_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mgr.md#SP_mgr_map_cache_enabled](../../../config/global/mgr.md#SP_mgr_map_cache_enabled) |

**What it does:** Enable the manager's map cache for API calls

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_map_cache_enabled false
ceph config get mgr mgr_map_cache_enabled
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_num_op_tracker_shard

| | |
|---|---|
| Type | Uint · default `32` · **Advanced** |
| Table | [mgr.md#SP_mgr_num_op_tracker_shard](../../../config/global/mgr.md#SP_mgr_num_op_tracker_shard) |

**What it does:** The number of shards for Manager ops

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_num_op_tracker_shard 32
ceph config get mgr mgr_num_op_tracker_shard
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_num_op_tracker_shard
ceph -s
ceph mgr dump
```

---

### mgr_op_complaint_time

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_complaint_time](../../../config/global/mgr.md#SP_mgr_op_complaint_time) |

**What it does:** A Manager operation becomes complaint-worthy after the specified number of seconds have elapsed.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_complaint_time 30
ceph config get mgr mgr_op_complaint_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_complaint_time
ceph -s
ceph mgr dump
```

---

### mgr_op_history_duration

| | |
|---|---|
| Type | Uint · default `600` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_history_duration](../../../config/global/mgr.md#SP_mgr_op_history_duration) |

**What it does:** The oldest completed Manager operation to track.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_history_duration 600
ceph config get mgr mgr_op_history_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `600`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_history_duration
ceph -s
ceph mgr dump
```

---

### mgr_op_history_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_history_size](../../../config/global/mgr.md#SP_mgr_op_history_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_history_size 20
ceph config get mgr mgr_op_history_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_history_size
ceph -s
ceph mgr dump
```

---

### mgr_op_history_slow_op_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_history_slow_op_size](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_size) |

**What it does:** Max number of slow Manager ops to track

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_history_slow_op_size 20
ceph config get mgr mgr_op_history_slow_op_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_history_slow_op_size
ceph -s
ceph mgr dump
```

---

### mgr_op_history_slow_op_threshold

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_history_slow_op_threshold](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_threshold) |

**What it does:** Duration of a Manager op to be considered as a historical slow op

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_history_slow_op_threshold 10
ceph config get mgr mgr_op_history_slow_op_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_history_slow_op_threshold
ceph -s
ceph mgr dump
```

---

### mgr_op_log_threshold

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mgr.md#SP_mgr_op_log_threshold](../../../config/global/mgr.md#SP_mgr_op_log_threshold) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_op_log_threshold 5
ceph config get mgr mgr_op_log_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_op_log_threshold
ceph -s
ceph mgr dump
```

---


[← Overview](../OVERVIEW.md)
