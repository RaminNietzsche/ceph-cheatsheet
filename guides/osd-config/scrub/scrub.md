# Scrub

OSD config deep dive — 39 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_blocked_scrub_grace_period](#osd_blocked_scrub_grace_period) | `120` | Advanced | Performance |
| [osd_deep_scrub_interval](#osd_deep_scrub_interval) | `7_day` | Advanced | Performance |
| [osd_deep_scrub_interval_cv](#osd_deep_scrub_interval_cv) | `0.2` | Advanced | Performance |
| [osd_deep_scrub_keys](#osd_deep_scrub_keys) | `1024` | Advanced | Performance |
| [osd_deep_scrub_large_omap_object_key_threshold](#osd_deep_scrub_large_omap_object_key_threshold) | `200000` | Advanced | Performance |
| [osd_deep_scrub_large_omap_object_value_sum_threshold](#osd_deep_scrub_large_omap_object_value_sum_threshold) | `1_G` | Advanced | Performance |
| [osd_deep_scrub_randomize_ratio](#osd_deep_scrub_randomize_ratio) | `0.15` | Advanced | Performance |
| [osd_deep_scrub_stride](#osd_deep_scrub_stride) | `4_M` | Advanced | Performance |
| [osd_deep_scrub_update_digest_min_age](#osd_deep_scrub_update_digest_min_age) | `2_hr` | Advanced | Performance |
| [osd_max_scrubs](#osd_max_scrubs) | `3` | Advanced | Performance |
| [osd_scrub_auto_repair](#osd_scrub_auto_repair) | `False` | Advanced | Performance |
| [osd_scrub_auto_repair_num_errors](#osd_scrub_auto_repair_num_errors) | `5` | Advanced | Performance |
| [osd_scrub_backoff_ratio](#osd_scrub_backoff_ratio) | `0.66` | Dev | Dev |
| [osd_scrub_begin_hour](#osd_scrub_begin_hour) | `0` | Advanced | Performance |
| [osd_scrub_begin_week_day](#osd_scrub_begin_week_day) | `0` | Advanced | Performance |
| [osd_scrub_chunk_max](#osd_scrub_chunk_max) | `15` | Advanced | Performance |
| [osd_scrub_chunk_min](#osd_scrub_chunk_min) | `5` | Advanced | Performance |
| [osd_scrub_disable_reservation_queuing](#osd_scrub_disable_reservation_queuing) | `False` | Advanced | Policy |
| [osd_scrub_during_recovery](#osd_scrub_during_recovery) | `False` | Advanced | Performance |
| [osd_scrub_end_hour](#osd_scrub_end_hour) | `0` | Advanced | Performance |
| [osd_scrub_end_week_day](#osd_scrub_end_week_day) | `0` | Advanced | Performance |
| [osd_scrub_extended_sleep](#osd_scrub_extended_sleep) | `0` | Advanced | Performance |
| [osd_scrub_interval_randomize_ratio](#osd_scrub_interval_randomize_ratio) | `0.5` | Advanced | Performance |
| [osd_scrub_invalid_stats](#osd_scrub_invalid_stats) | `True` | Advanced | Performance |
| [osd_scrub_load_threshold](#osd_scrub_load_threshold) | `10.0` | Advanced | Performance |
| [osd_scrub_max_interval](#osd_scrub_max_interval) | `7_day` | Advanced | Performance |
| [osd_scrub_max_preemptions](#osd_scrub_max_preemptions) | `5` | Advanced | Performance |
| [osd_scrub_min_interval](#osd_scrub_min_interval) | `1_day` | Advanced | Performance |
| [osd_scrub_queued_snaptrims_limit](#osd_scrub_queued_snaptrims_limit) | `500` | Advanced | Performance |
| [osd_scrub_retry_after_noscrub](#osd_scrub_retry_after_noscrub) | `60` | Advanced | Performance |
| [osd_scrub_retry_delay](#osd_scrub_retry_delay) | `30` | Advanced | Performance |
| [osd_scrub_retry_new_interval](#osd_scrub_retry_new_interval) | `10` | Advanced | Performance |
| [osd_scrub_retry_pg_state](#osd_scrub_retry_pg_state) | `60` | Advanced | Performance |
| [osd_scrub_retry_trimming](#osd_scrub_retry_trimming) | `10` | Advanced | Performance |
| [osd_scrub_sleep](#osd_scrub_sleep) | `0` | Advanced | Performance |
| [osd_shallow_scrub_chunk_max](#osd_shallow_scrub_chunk_max) | `100` | Advanced | Performance |
| [osd_shallow_scrub_chunk_min](#osd_shallow_scrub_chunk_min) | `50` | Advanced | Performance |
| [osd_stats_update_period_not_scrubbing](#osd_stats_update_period_not_scrubbing) | `120` | Advanced | Performance |
| [osd_stats_update_period_scrubbing](#osd_stats_update_period_scrubbing) | `15` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_blocked_scrub_grace_period

| | |
|---|---|
| Type | Int · default `120` · **Advanced** |
| Table | [osd.md#SP_osd_blocked_scrub_grace_period](../../../config/osd/osd.md#SP_osd_blocked_scrub_grace_period) |

**What it does:** Time (seconds) before issuing a cluster-log warning

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_blocked_scrub_grace_period 120
ceph config get osd osd_blocked_scrub_grace_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_blocked_scrub_grace_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_interval

| | |
|---|---|
| Type | Float · default `7_day` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_interval](../../../config/osd/osd.md#SP_osd_deep_scrub_interval) |

**What it does:** Interval (seconds) between deep scrubs that verify full object checksums.

**When to use:** Shorten for compliance-heavy environments; lengthen on large HDD pools where deep scrub IO is costly.

**Example:**

```bash
ceph config set osd osd_deep_scrub_interval 7_day
ceph config get osd osd_deep_scrub_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7_day`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_interval_cv

| | |
|---|---|
| Type | Float · default `0.2` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_interval_cv](../../../config/osd/osd.md#SP_osd_deep_scrub_interval_cv) |

**What it does:** Determines the amount of variation in the deep scrub interval

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_deep_scrub_interval_cv 0.2
ceph config get osd osd_deep_scrub_interval_cv
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `0.4`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_interval_cv
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_keys

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_keys](../../../config/osd/osd.md#SP_osd_deep_scrub_keys) |

**What it does:** Number of keys to read from an object at a time during deep scrub

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_deep_scrub_keys 1024
ceph config get osd osd_deep_scrub_keys
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_keys
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_large_omap_object_key_threshold

| | |
|---|---|
| Type | Uint · default `200000` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold) |

**What it does:** Warn when we encounter an object with more omap keys than this

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_key_threshold 200000
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_large_omap_object_value_sum_threshold

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold) |

**What it does:** Warn when we encounter an object with more omap key bytes than this

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_value_sum_threshold 1_G
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_randomize_ratio

| | |
|---|---|
| Type | Float · default `0.15` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_randomize_ratio](../../../config/osd/osd.md#SP_osd_deep_scrub_randomize_ratio) |

**What it does:** deprecated. Has no effect.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_deep_scrub_randomize_ratio 0.15
ceph config get osd osd_deep_scrub_randomize_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_stride

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_stride](../../../config/osd/osd.md#SP_osd_deep_scrub_stride) |

**What it does:** Number of bytes to read from an object at a time during deep scrub

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_deep_scrub_stride 4_M
ceph config get osd osd_deep_scrub_stride
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_stride
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_deep_scrub_update_digest_min_age

| | |
|---|---|
| Type | Int · default `2_hr` · **Advanced** |
| Table | [osd.md#SP_osd_deep_scrub_update_digest_min_age](../../../config/osd/osd.md#SP_osd_deep_scrub_update_digest_min_age) |

**What it does:** Update overall object digest only if object was last modified longer ago than this

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_deep_scrub_update_digest_min_age 2_hr
ceph config get osd osd_deep_scrub_update_digest_min_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_deep_scrub_update_digest_min_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_scrubs

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [osd.md#SP_osd_max_scrubs](../../../config/osd/osd.md#SP_osd_max_scrubs) |

**What it does:** Maximum concurrent scrub operations per OSD. Scrub reads object data to verify checksums — too many scrubs compete with client I/O.

**When to use:** Increase cautiously on fast media when scrubs lag behind the scrub interval. Decrease when `ceph -s` reports slow ops or OSD latency spikes during scrub windows.

**Example:**

```bash
ceph config set osd osd_max_scrubs 3
ceph config get osd osd_max_scrubs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_scrubs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

Pair with `osd_scrub_sleep` and deep-scrub intervals. HDD clusters often stay at 1; NVMe may tolerate 2–3 if load is low.

---

### osd_scrub_auto_repair

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_auto_repair](../../../config/osd/osd.md#SP_osd_scrub_auto_repair) |

**What it does:** Automatically repair damaged objects detected during scrub

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_scrub_auto_repair true
ceph config get osd osd_scrub_auto_repair
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_auto_repair
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_auto_repair_num_errors

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_auto_repair_num_errors](../../../config/osd/osd.md#SP_osd_scrub_auto_repair_num_errors) |

**What it does:** Maximum number of damaged objects to automatically repair

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_auto_repair_num_errors 5
ceph config get osd osd_scrub_auto_repair_num_errors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_auto_repair_num_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_backoff_ratio

| | |
|---|---|
| Type | Float · default `0.66` · **Dev** |
| Table | [osd.md#SP_osd_scrub_backoff_ratio](../../../config/osd/osd.md#SP_osd_scrub_backoff_ratio) |

**What it does:** Backoff ratio for scheduling scrubs

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_scrub_backoff_ratio 0.66
ceph config get osd osd_scrub_backoff_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.66`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_scrub_begin_hour

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_begin_hour](../../../config/osd/osd.md#SP_osd_scrub_begin_hour) |

**What it does:** Restrict scrubbing to this hour of the day or later

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_begin_hour 64
ceph config get osd osd_scrub_begin_hour
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `23`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_begin_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_begin_week_day

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_begin_week_day](../../../config/osd/osd.md#SP_osd_scrub_begin_week_day) |

**What it does:** Restrict scrubbing to this day of the week or later

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_begin_week_day 64
ceph config get osd osd_scrub_begin_week_day
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `6`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_begin_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_chunk_max

| | |
|---|---|
| Type | Int · default `15` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_scrub_chunk_max) |

**What it does:** Maximum number of objects to deep-scrub in a single chunk

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_chunk_max 15
ceph config get osd osd_scrub_chunk_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_chunk_min

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_scrub_chunk_min) |

**What it does:** Minimum number of objects to deep-scrub in a single chunk

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_chunk_min 5
ceph config get osd osd_scrub_chunk_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_disable_reservation_queuing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_disable_reservation_queuing](../../../config/osd/osd.md#SP_osd_scrub_disable_reservation_queuing) |

**What it does:** Disable queuing of scrub reservations

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_scrub_disable_reservation_queuing true
ceph config get osd osd_scrub_disable_reservation_queuing
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_disable_reservation_queuing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_during_recovery

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_during_recovery](../../../config/osd/osd.md#SP_osd_scrub_during_recovery) |

**What it does:** Allow scrubbing when PGs on the OSD are undergoing recovery

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_scrub_during_recovery true
ceph config get osd osd_scrub_during_recovery
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_during_recovery
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_end_hour

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_end_hour](../../../config/osd/osd.md#SP_osd_scrub_end_hour) |

**What it does:** Restrict scrubbing to hours of the day earlier than this

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_end_hour 64
ceph config get osd osd_scrub_end_hour
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `23`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_end_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_end_week_day

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_end_week_day](../../../config/osd/osd.md#SP_osd_scrub_end_week_day) |

**What it does:** Restrict scrubbing to days of the week earlier than this

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_end_week_day 64
ceph config get osd osd_scrub_end_week_day
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `6`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_end_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_extended_sleep

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_extended_sleep](../../../config/osd/osd.md#SP_osd_scrub_extended_sleep) |

**What it does:** Duration (in seconds) of delay injected between chunks when scrubbing out of scrubbing hours

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_scrub_extended_sleep 0
ceph config get osd osd_scrub_extended_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_extended_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_interval_randomize_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_interval_randomize_ratio](../../../config/osd/osd.md#SP_osd_scrub_interval_randomize_ratio) |

**What it does:** Ratio of scrub interval to randomly vary

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_scrub_interval_randomize_ratio 0.5
ceph config get osd osd_scrub_interval_randomize_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_interval_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_invalid_stats

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_invalid_stats](../../../config/osd/osd.md#SP_osd_scrub_invalid_stats) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_scrub_invalid_stats false
ceph config get osd osd_scrub_invalid_stats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_invalid_stats
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_load_threshold

| | |
|---|---|
| Type | Float · default `10.0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_load_threshold](../../../config/osd/osd.md#SP_osd_scrub_load_threshold) |

**What it does:** Allow scrubbing when system load divided by number of CPUs is below this value

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_load_threshold 10.0
ceph config get osd osd_scrub_load_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10.0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_load_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_max_interval

| | |
|---|---|
| Type | Float · default `7_day` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_max_interval](../../../config/osd/osd.md#SP_osd_scrub_max_interval) |

**What it does:** Maximum interval (seconds) between shallow scrubs for a PG.

**When to use:** Align with maintenance policy. Monitor `mon_warn_pg_not_scrubbed_ratio` warnings.

**Example:**

```bash
ceph config set osd osd_scrub_max_interval 7_day
ceph config get osd osd_scrub_max_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7_day`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_max_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_max_preemptions

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_max_preemptions](../../../config/osd/osd.md#SP_osd_scrub_max_preemptions) |

**What it does:** Set the maximum number of times we will preempt a deep scrub due to a client operation before blocking client IO to complete the scrub

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_scrub_max_preemptions 5
ceph config get osd osd_scrub_max_preemptions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `30`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_max_preemptions
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_min_interval

| | |
|---|---|
| Type | Float · default `1_day` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_min_interval](../../../config/osd/osd.md#SP_osd_scrub_min_interval) |

**What it does:** The desired interval between scrubs of a specific PG. Note that this option must be set at ``global`` scope, or for both ``mgr`` and``osd``.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_scrub_min_interval 1_day
ceph config get osd osd_scrub_min_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_day`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_min_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_queued_snaptrims_limit

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_queued_snaptrims_limit](../../../config/osd/osd.md#SP_osd_scrub_queued_snaptrims_limit) |

**What it does:** Do not initiate periodic scrubs when the total snap-trim queues across all PGs exceeds this value. A value of '0' disables this limit.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_scrub_queued_snaptrims_limit 500
ceph config get osd osd_scrub_queued_snaptrims_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_queued_snaptrims_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_retry_after_noscrub

| | |
|---|---|
| Type | Int · default `60` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_retry_after_noscrub](../../../config/osd/osd.md#SP_osd_scrub_retry_after_noscrub) |

**What it does:** Period (in seconds) before retrying to scrub a PG at a specific level after detecting a no-scrub or no-deep-scrub flag

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_retry_after_noscrub 60
ceph config get osd osd_scrub_retry_after_noscrub
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_retry_after_noscrub
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_retry_delay

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_retry_delay](../../../config/osd/osd.md#SP_osd_scrub_retry_delay) |

**What it does:** Period (in seconds) before retrying a PG that has failed a prior scrub.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_retry_delay 30
ceph config get osd osd_scrub_retry_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_retry_delay
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_retry_new_interval

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_retry_new_interval](../../../config/osd/osd.md#SP_osd_scrub_retry_new_interval) |

**What it does:** Period (in seconds) before retrying a scrub aborted on a new interval

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_scrub_retry_new_interval 10
ceph config get osd osd_scrub_retry_new_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_retry_new_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_retry_pg_state

| | |
|---|---|
| Type | Int · default `60` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_retry_pg_state](../../../config/osd/osd.md#SP_osd_scrub_retry_pg_state) |

**What it does:** Period (in seconds) before retrying to scrub a previously inactive/not-clean PG

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_retry_pg_state 60
ceph config get osd osd_scrub_retry_pg_state
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_retry_pg_state
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_retry_trimming

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_retry_trimming](../../../config/osd/osd.md#SP_osd_scrub_retry_trimming) |

**What it does:** Period (in seconds) before retrying to scrub a previously snap-trimming PG

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_scrub_retry_trimming 10
ceph config get osd osd_scrub_retry_trimming
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_retry_trimming
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_scrub_sleep

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_scrub_sleep](../../../config/osd/osd.md#SP_osd_scrub_sleep) |

**What it does:** Duration (in seconds) of delay injected between chunks when scrubbing

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_scrub_sleep 0
ceph config get osd osd_scrub_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_scrub_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_shallow_scrub_chunk_max

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [osd.md#SP_osd_shallow_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_max) |

**What it does:** Maximum number of objects to scrub in a single chunk

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_shallow_scrub_chunk_max 100
ceph config get osd osd_shallow_scrub_chunk_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_shallow_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_shallow_scrub_chunk_min

| | |
|---|---|
| Type | Int · default `50` · **Advanced** |
| Table | [osd.md#SP_osd_shallow_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_min) |

**What it does:** Minimum number of objects to scrub in a single chunk

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_shallow_scrub_chunk_min 50
ceph config get osd osd_shallow_scrub_chunk_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_shallow_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_stats_update_period_not_scrubbing

| | |
|---|---|
| Type | Int · default `120` · **Advanced** |
| Table | [osd.md#SP_osd_stats_update_period_not_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_not_scrubbing) |

**What it does:** Stats update period (seconds) when not scrubbing

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_stats_update_period_not_scrubbing 120
ceph config get osd osd_stats_update_period_not_scrubbing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `120`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_stats_update_period_not_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_stats_update_period_scrubbing

| | |
|---|---|
| Type | Int · default `15` · **Advanced** |
| Table | [osd.md#SP_osd_stats_update_period_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_scrubbing) |

**What it does:** Stats update period (seconds) when scrubbing

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_stats_update_period_scrubbing 15
ceph config get osd osd_stats_update_period_scrubbing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_stats_update_period_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
