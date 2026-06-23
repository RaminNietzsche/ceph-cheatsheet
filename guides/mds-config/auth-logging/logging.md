# Logging

MDS config deep dive — 15 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mds_kill_after_journal_logs_flushed](#mds_kill_after_journal_logs_flushed) | `False` | Dev | Dev |
| [mds_log_event_large_threshold](#mds_log_event_large_threshold) | `512_K` | Advanced | Performance |
| [mds_log_events_per_segment](#mds_log_events_per_segment) | `1024` | Advanced | Performance |
| [mds_log_max_events](#mds_log_max_events) | `-1` | Advanced | Performance |
| [mds_log_max_segments](#mds_log_max_segments) | `128` | Advanced | Performance |
| [mds_log_minor_segments_per_major_segment](#mds_log_minor_segments_per_major_segment) | `16` | Advanced | Performance |
| [mds_log_pause](#mds_log_pause) | `False` | Dev | Dev |
| [mds_log_segment_size](#mds_log_segment_size) | `0` | Advanced | Performance |
| [mds_log_skip_corrupt_events](#mds_log_skip_corrupt_events) | `False` | Dev | Dev |
| [mds_log_skip_unbounded_events](#mds_log_skip_unbounded_events) | `False` | Dev | Dev |
| [mds_log_trim_decay_rate](#mds_log_trim_decay_rate) | `1.0` | Advanced | Performance |
| [mds_log_trim_threshold](#mds_log_trim_threshold) | `128` | Advanced | Performance |
| [mds_log_trim_upkeep_interval](#mds_log_trim_upkeep_interval) | `1000` | Advanced | Performance |
| [mds_log_warn_factor](#mds_log_warn_factor) | `2` | Advanced | Performance |
| [mds_op_log_threshold](#mds_op_log_threshold) | `5` | Dev | Dev |

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

### mds_kill_after_journal_logs_flushed

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_kill_after_journal_logs_flushed](../../../config/mds/mds.md#SP_mds_kill_after_journal_logs_flushed) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_after_journal_logs_flushed true
ceph config get mds mds_kill_after_journal_logs_flushed
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_log_event_large_threshold

| | |
|---|---|
| Type | Uint · default `512_K` · **Advanced** |
| Table | [mds.md#SP_mds_log_event_large_threshold](../../../config/mds/mds.md#SP_mds_log_event_large_threshold) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_event_large_threshold 512_K
ceph config get mds mds_log_event_large_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1_K`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_event_large_threshold
ceph -s
ceph fs status
```

---

### mds_log_events_per_segment

| | |
|---|---|
| Type | Uint · default `1024` · **Advanced** |
| Table | [mds.md#SP_mds_log_events_per_segment](../../../config/mds/mds.md#SP_mds_log_events_per_segment) |

**What it does:** maximum number of events in an MDS journal segment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_events_per_segment 1024
ceph config get mds mds_log_events_per_segment
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_events_per_segment
ceph -s
ceph fs status
```

---

### mds_log_max_events

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [mds.md#SP_mds_log_max_events](../../../config/mds/mds.md#SP_mds_log_max_events) |

**What it does:** Maximum journal events before the MDS forces a segment rollover.

**When to use:** Advanced — affects journal segmentation and recovery time after crash.

**Example:**

```bash
ceph config set mds mds_log_max_events 128
ceph config get mds mds_log_max_events
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_max_events
ceph -s
ceph fs status
```

---

### mds_log_max_segments

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [mds.md#SP_mds_log_max_segments](../../../config/mds/mds.md#SP_mds_log_max_segments) |

**What it does:** maximum number of segments which may be untrimmed

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_log_max_segments 128
ceph config get mds mds_log_max_segments
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `8`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_max_segments
ceph -s
ceph fs status
```

---

### mds_log_minor_segments_per_major_segment

| | |
|---|---|
| Type | Uint · default `16` · **Advanced** |
| Table | [mds.md#SP_mds_log_minor_segments_per_major_segment](../../../config/mds/mds.md#SP_mds_log_minor_segments_per_major_segment) |

**What it does:** Number of minor segments per major segment.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_minor_segments_per_major_segment 16
ceph config get mds mds_log_minor_segments_per_major_segment
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `4`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_minor_segments_per_major_segment
ceph -s
ceph fs status
```

---

### mds_log_pause

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_log_pause](../../../config/mds/mds.md#SP_mds_log_pause) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_log_pause true
ceph config get mds mds_log_pause
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_log_segment_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_log_segment_size](../../../config/mds/mds.md#SP_mds_log_segment_size) |

**What it does:** size in bytes of each MDS log segment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_segment_size 64
ceph config get mds mds_log_segment_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_segment_size
ceph -s
ceph fs status
```

---

### mds_log_skip_corrupt_events

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_log_skip_corrupt_events](../../../config/mds/mds.md#SP_mds_log_skip_corrupt_events) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_log_skip_corrupt_events true
ceph config get mds mds_log_skip_corrupt_events
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_log_skip_unbounded_events

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_log_skip_unbounded_events](../../../config/mds/mds.md#SP_mds_log_skip_unbounded_events) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_log_skip_unbounded_events true
ceph config get mds mds_log_skip_unbounded_events
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_log_trim_decay_rate

| | |
|---|---|
| Type | Float · default `1.0` · **Advanced** |
| Table | [mds.md#SP_mds_log_trim_decay_rate](../../../config/mds/mds.md#SP_mds_log_trim_decay_rate) |

**What it does:** MDS log trim decay rate

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_trim_decay_rate 1.0
ceph config get mds mds_log_trim_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0.01`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_trim_decay_rate
ceph -s
ceph fs status
```

---

### mds_log_trim_threshold

| | |
|---|---|
| Type | Size · default `128` · **Advanced** |
| Table | [mds.md#SP_mds_log_trim_threshold](../../../config/mds/mds.md#SP_mds_log_trim_threshold) |

**What it does:** MDS log trim threshold

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_trim_threshold 128
ceph config get mds mds_log_trim_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_trim_threshold
ceph -s
ceph fs status
```

---

### mds_log_trim_upkeep_interval

| | |
|---|---|
| Type | Millisecs · default `1000` · **Advanced** |
| Table | [mds.md#SP_mds_log_trim_upkeep_interval](../../../config/mds/mds.md#SP_mds_log_trim_upkeep_interval) |

**What it does:** MDS log trimming interval

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_log_trim_upkeep_interval 1000
ceph config get mds mds_log_trim_upkeep_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_trim_upkeep_interval
ceph -s
ceph fs status
```

---

### mds_log_warn_factor

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [mds.md#SP_mds_log_warn_factor](../../../config/mds/mds.md#SP_mds_log_warn_factor) |

**What it does:** trigger MDS_HEALTH_TRIM warning when the mds log is longer than mds_log_max_segments * mds_log_warn_factor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_log_warn_factor 2
ceph config get mds mds_log_warn_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_log_warn_factor
ceph -s
ceph fs status
```

---

### mds_op_log_threshold

| | |
|---|---|
| Type | Int · default `5` · **Dev** |
| Table | [mds.md#SP_mds_op_log_threshold](../../../config/mds/mds.md#SP_mds_op_log_threshold) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_op_log_threshold 5
ceph config get mds mds_op_log_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
