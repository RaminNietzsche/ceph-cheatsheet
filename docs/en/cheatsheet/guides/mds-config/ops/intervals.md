# Intervals

MDS config deep dive — 19 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mds_bal_fragment_interval](#mds_bal_fragment_interval) | `5` | Advanced | Performance |
| [mds_bal_interval](#mds_bal_interval) | `10` | Advanced | Performance |
| [mds_bal_sample_interval](#mds_bal_sample_interval) | `3` | Advanced | Performance |
| [mds_beacon_interval](#mds_beacon_interval) | `4` | Advanced | Performance |
| [mds_cache_release_free_interval](#mds_cache_release_free_interval) | `10` | Dev | Dev |
| [mds_cache_trim_interval](#mds_cache_trim_interval) | `1` | Advanced | Performance |
| [mds_dirstat_min_interval](#mds_dirstat_min_interval) | `1` | Dev | Dev |
| [mds_extraordinary_events_dump_interval](#mds_extraordinary_events_dump_interval) | `0` | Advanced | Performance |
| [mds_freeze_tree_timeout](#mds_freeze_tree_timeout) | `30` | Dev | Dev |
| [mds_metrics_update_interval](#mds_metrics_update_interval) | `2` | Advanced | Performance |
| [mds_mon_shutdown_timeout](#mds_mon_shutdown_timeout) | `5` | Advanced | Performance |
| [mds_ping_interval](#mds_ping_interval) | `5` | Advanced | Performance |
| [mds_reconnect_timeout](#mds_reconnect_timeout) | `45` | Advanced | Performance |
| [mds_replay_interval](#mds_replay_interval) | `1` | Advanced | Performance |
| [mds_scatter_nudge_interval](#mds_scatter_nudge_interval) | `5` | Advanced | Performance |
| [mds_session_blocklist_on_timeout](#mds_session_blocklist_on_timeout) | `True` | Advanced | Performance |
| [mds_task_status_update_interval](#mds_task_status_update_interval) | `2` | Dev | Dev |
| [mds_tick_interval](#mds_tick_interval) | `5` | Advanced | Performance |
| [subv_metrics_window_interval](#subv_metrics_window_interval) | `30` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_bal_fragment_interval

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_bal_fragment_interval](../../../config/mds/mds.md#SP_mds_bal_fragment_interval) |

**What it does:** delay in seconds before interrupting client IO to perform splits

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_bal_fragment_interval 5
ceph config get mds mds_bal_fragment_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_bal_fragment_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_interval

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_bal_interval](../../../config/mds/mds.md#SP_mds_bal_interval) |

**What it does:** interval between MDS balancer cycles

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_bal_interval 10
ceph config get mds mds_bal_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_bal_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_sample_interval

| | |
|---|---|
| Type | Float · default `3` · **Advanced** |
| Table | [mds.md#SP_mds_bal_sample_interval](../../../config/mds/mds.md#SP_mds_bal_sample_interval) |

**What it does:** interval in seconds between balancer ticks

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_bal_sample_interval 3
ceph config get mds mds_bal_sample_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_bal_sample_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_beacon_interval

| | |
|---|---|
| Type | Float · default `4` · **Advanced** |
| Table | [mds.md#SP_mds_beacon_interval](../../../config/mds/mds.md#SP_mds_beacon_interval) |

**What it does:** How often (seconds) an MDS sends beacons to monitors.

**When to use:** Rarely changed; must stay well below `mds_beacon_grace`.

**Example:**

```bash
ceph config set mds mds_beacon_interval 4
ceph config get mds mds_beacon_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_beacon_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_release_free_interval

| | |
|---|---|
| Type | Secs · default `10` · **Dev** |
| Table | [mds.md#SP_mds_cache_release_free_interval](../../../config/mds/mds.md#SP_mds_cache_release_free_interval) |

**What it does:** Interval in seconds between heap releases

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_cache_release_free_interval 10
ceph config get mds mds_cache_release_free_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_cache_trim_interval

| | |
|---|---|
| Type | Secs · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_cache_trim_interval](../../../config/mds/mds.md#SP_mds_cache_trim_interval) |

**What it does:** Interval in seconds between cache trims

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_cache_trim_interval 1
ceph config get mds mds_cache_trim_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_cache_trim_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dirstat_min_interval

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [mds.md#SP_mds_dirstat_min_interval](../../../config/mds/mds.md#SP_mds_dirstat_min_interval) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_dirstat_min_interval 1
ceph config get mds mds_dirstat_min_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_extraordinary_events_dump_interval

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_extraordinary_events_dump_interval](../../../config/mds/mds.md#SP_mds_extraordinary_events_dump_interval) |

**What it does:** Interval in seconds for dumping the recent in-memory logs when there is an extra-ordinary event. Interval in seconds for dumping the recent in-memory logs when there is an extra-ordinary event. The default is ``0`` (disabled). The log level should be ``< 10`` and the gather level should be ``>=10`` in debug_mds for enabling this option.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_extraordinary_events_dump_interval 0
ceph config get mds mds_extraordinary_events_dump_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `60`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_extraordinary_events_dump_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_freeze_tree_timeout

| | |
|---|---|
| Type | Float · default `30` · **Dev** |
| Table | [mds.md#SP_mds_freeze_tree_timeout](../../../config/mds/mds.md#SP_mds_freeze_tree_timeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_freeze_tree_timeout 30
ceph config get mds mds_freeze_tree_timeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`30`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_metrics_update_interval

| | |
|---|---|
| Type | Secs · default `2` · **Advanced** |
| Table | [mds.md#SP_mds_metrics_update_interval](../../../config/mds/mds.md#SP_mds_metrics_update_interval) |

**What it does:** interval in seconds for metrics data update. interval in seconds after which active MDSs send client metrics data to rank 0.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_metrics_update_interval 2
ceph config get mds mds_metrics_update_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_metrics_update_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_mon_shutdown_timeout

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_mon_shutdown_timeout](../../../config/mds/mds.md#SP_mds_mon_shutdown_timeout) |

**What it does:** time to wait for mon to receive damaged MDS rank notification

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_mon_shutdown_timeout 5
ceph config get mds mds_mon_shutdown_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_mon_shutdown_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_ping_interval

| | |
|---|---|
| Type | Secs · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_ping_interval](../../../config/mds/mds.md#SP_mds_ping_interval) |

**What it does:** interval in seconds for sending ping messages to active MDSs. interval in seconds for rank 0 to send ping messages to all active MDSs.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_ping_interval 5
ceph config get mds mds_ping_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_ping_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_reconnect_timeout

| | |
|---|---|
| Type | Float · default `45` · **Advanced** |
| Table | [mds.md#SP_mds_reconnect_timeout](../../../config/mds/mds.md#SP_mds_reconnect_timeout) |

**What it does:** Timeout in seconds to wait for clients to reconnect during MDS reconnect recovery state

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_reconnect_timeout 45
ceph config get mds mds_reconnect_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `45`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_reconnect_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_replay_interval

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_replay_interval](../../../config/mds/mds.md#SP_mds_replay_interval) |

**What it does:** time in seconds between replay of updates to journal by standby replay MDS

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_replay_interval 1
ceph config get mds mds_replay_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_replay_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_scatter_nudge_interval

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_scatter_nudge_interval](../../../config/mds/mds.md#SP_mds_scatter_nudge_interval) |

**What it does:** minimum interval between scatter lock updates

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_scatter_nudge_interval 5
ceph config get mds mds_scatter_nudge_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_scatter_nudge_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_blocklist_on_timeout

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_session_blocklist_on_timeout](../../../config/mds/mds.md#SP_mds_session_blocklist_on_timeout) |

**What it does:** Blocklist clients whose sessions have become stale

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_session_blocklist_on_timeout false
ceph config get mds mds_session_blocklist_on_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_session_blocklist_on_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_task_status_update_interval

| | |
|---|---|
| Type | Float · default `2` · **Dev** |
| Table | [mds.md#SP_mds_task_status_update_interval](../../../config/mds/mds.md#SP_mds_task_status_update_interval) |

**What it does:** task status update interval to manager interval (in seconds) for sending mds task status to ceph manager

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_task_status_update_interval 2
ceph config get mds mds_task_status_update_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_tick_interval

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_tick_interval](../../../config/mds/mds.md#SP_mds_tick_interval) |

**What it does:** time in seconds between upkeep tasks

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_tick_interval 5
ceph config get mds mds_tick_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_tick_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### subv_metrics_window_interval

| | |
|---|---|
| Type | Secs · default `30` · **Dev** |
| Table | [mds.md#SP_subv_metrics_window_interval](../../../config/mds/mds.md#SP_subv_metrics_window_interval) |

**What it does:** subvolume metrics sliding window interval, seconds interval in seconds to hold values in sliding window for subvolume metrics

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds subv_metrics_window_interval 30
ceph config get mds subv_metrics_window_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`30`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
