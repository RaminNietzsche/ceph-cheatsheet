# Recovery & backfill

OSD config deep dive — 28 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_allow_recovery_below_min_size](#osd_allow_recovery_below_min_size) | `True` | Dev | Dev |
| [osd_backfill_retry_interval](#osd_backfill_retry_interval) | `30` | Advanced | Performance |
| [osd_backfill_scan_max](#osd_backfill_scan_max) | `512` | Advanced | Performance |
| [osd_backfill_scan_min](#osd_backfill_scan_min) | `64` | Advanced | Performance |
| [osd_max_backfills](#osd_max_backfills) | `1` | Advanced | Performance |
| [osd_mclock_override_recovery_settings](#osd_mclock_override_recovery_settings) | `False` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_lim](#osd_mclock_scheduler_background_recovery_lim) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_res](#osd_mclock_scheduler_background_recovery_res) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_wgt](#osd_mclock_scheduler_background_recovery_wgt) | `1` | Advanced | Performance |
| [osd_min_recovery_priority](#osd_min_recovery_priority) | `0` | Advanced | Performance |
| [osd_recover_clone_overlap](#osd_recover_clone_overlap) | `True` | Advanced | Performance |
| [osd_recover_clone_overlap_limit](#osd_recover_clone_overlap_limit) | `10` | Advanced | Performance |
| [osd_recovery_delay_start](#osd_recovery_delay_start) | `0` | Advanced | Performance |
| [osd_recovery_max_active](#osd_recovery_max_active) | `0` | Advanced | Performance |
| [osd_recovery_max_active_hdd](#osd_recovery_max_active_hdd) | `3` | Advanced | Performance |
| [osd_recovery_max_active_ssd](#osd_recovery_max_active_ssd) | `10` | Advanced | Performance |
| [osd_recovery_max_chunk](#osd_recovery_max_chunk) | `8_M` | Advanced | Performance |
| [osd_recovery_max_omap_entries_per_chunk](#osd_recovery_max_omap_entries_per_chunk) | `8096` | Advanced | Performance |
| [osd_recovery_max_single_start](#osd_recovery_max_single_start) | `1` | Advanced | Performance |
| [osd_recovery_retry_interval](#osd_recovery_retry_interval) | `30` | Advanced | Performance |
| [osd_recovery_sleep](#osd_recovery_sleep) | `0` | Advanced | Performance |
| [osd_recovery_sleep_degraded](#osd_recovery_sleep_degraded) | `0` | Advanced | Performance |
| [osd_recovery_sleep_degraded_hdd](#osd_recovery_sleep_degraded_hdd) | `0.1` | Advanced | Performance |
| [osd_recovery_sleep_degraded_hybrid](#osd_recovery_sleep_degraded_hybrid) | `0.025` | Advanced | Performance |
| [osd_recovery_sleep_degraded_ssd](#osd_recovery_sleep_degraded_ssd) | `0` | Advanced | Performance |
| [osd_recovery_sleep_hdd](#osd_recovery_sleep_hdd) | `0.1` | Advanced | Performance |
| [osd_recovery_sleep_hybrid](#osd_recovery_sleep_hybrid) | `0.025` | Advanced | Performance |
| [osd_recovery_sleep_ssd](#osd_recovery_sleep_ssd) | `0` | Advanced | Performance |

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

### osd_allow_recovery_below_min_size

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [osd.md#SP_osd_allow_recovery_below_min_size](../../../config/osd/osd.md#SP_osd_allow_recovery_below_min_size) |

**What it does:** allow replicated pools to recover with < min_size active members

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_allow_recovery_below_min_size false
ceph config get osd osd_allow_recovery_below_min_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_backfill_retry_interval

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_backfill_retry_interval](../../../config/osd/osd.md#SP_osd_backfill_retry_interval) |

**What it does:** how frequently to retry backfill reservations after being denied (e.g., due to a full OSD)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_backfill_retry_interval 30
ceph config get osd osd_backfill_retry_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backfill_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_backfill_scan_max

| | |
|---|---|
| Type | Int · default `512` · **Advanced** |
| Table | [osd.md#SP_osd_backfill_scan_max](../../../config/osd/osd.md#SP_osd_backfill_scan_max) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_backfill_scan_max 512
ceph config get osd osd_backfill_scan_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backfill_scan_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_backfill_scan_min

| | |
|---|---|
| Type | Int · default `64` · **Advanced** |
| Table | [osd.md#SP_osd_backfill_scan_min](../../../config/osd/osd.md#SP_osd_backfill_scan_min) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_backfill_scan_min 64
ceph config get osd osd_backfill_scan_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_backfill_scan_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_backfills

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_max_backfills](../../../config/osd/osd.md#SP_osd_max_backfills) |

**What it does:** Maximum number of concurrent local and remote backfills or recoveries per OSD

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_backfills 1
ceph config get osd osd_max_backfills
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_backfills
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_mclock_override_recovery_settings

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_override_recovery_settings](../../../config/osd/osd.md#SP_osd_mclock_override_recovery_settings) |

**What it does:** Setting this option enables the override of recovery/backfill limits for the mClock scheduler.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_mclock_override_recovery_settings true
ceph config get osd osd_mclock_override_recovery_settings
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_override_recovery_settings
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_mclock_scheduler_background_recovery_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_recovery_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_lim) |

**What it does:** IO limit for background recovery over reservation. The default value of 0 specifies no limit enforcement, which means background recovery operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background recovery operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_lim 0
ceph config get osd osd_mclock_scheduler_background_recovery_lim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `1.0`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_mclock_scheduler_background_recovery_res

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_recovery_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_res) |

**What it does:** IO proportion reserved for background recovery (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background recovery operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_res 0
ceph config get osd osd_mclock_scheduler_background_recovery_res
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `1.0`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_mclock_scheduler_background_recovery_wgt

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_recovery_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_wgt) |

**What it does:** IO share for each background recovery over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_wgt 1
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_min_recovery_priority

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_min_recovery_priority](../../../config/osd/osd.md#SP_osd_min_recovery_priority) |

**What it does:** Minimum priority below which recovery is not performed

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_min_recovery_priority 64
ceph config get osd osd_min_recovery_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_min_recovery_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recover_clone_overlap

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_recover_clone_overlap](../../../config/osd/osd.md#SP_osd_recover_clone_overlap) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_recover_clone_overlap false
ceph config get osd osd_recover_clone_overlap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recover_clone_overlap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recover_clone_overlap_limit

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_recover_clone_overlap_limit](../../../config/osd/osd.md#SP_osd_recover_clone_overlap_limit) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recover_clone_overlap_limit 10
ceph config get osd osd_recover_clone_overlap_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recover_clone_overlap_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_delay_start

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_delay_start](../../../config/osd/osd.md#SP_osd_recovery_delay_start) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_recovery_delay_start 0
ceph config get osd osd_recovery_delay_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_delay_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_max_active

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_active](../../../config/osd/osd.md#SP_osd_recovery_max_active) |

**What it does:** Cap on concurrent recovery/backfill operations per OSD (0 = derive from HDD/SSD/hybrid-specific settings).

**When to use:** Raise temporarily after OSD replacement to rebuild faster; lower during production peaks to protect client latency.

**Example:**

```bash
ceph config set osd osd_recovery_max_active 64
ceph config get osd osd_recovery_max_active
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_active
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

Watch `recovering`/`backfilling` PG count and client p99. See also `osd_recovery_max_active_hdd` / `_ssd` when set to 0.

---

### osd_recovery_max_active_hdd

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_active_hdd](../../../config/osd/osd.md#SP_osd_recovery_max_active_hdd) |

**What it does:** Number of simultaneous active recovery operations per OSD (for rotational devices)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recovery_max_active_hdd 3
ceph config get osd osd_recovery_max_active_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_active_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_max_active_ssd

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_active_ssd](../../../config/osd/osd.md#SP_osd_recovery_max_active_ssd) |

**What it does:** Number of simultaneous active recovery operations per OSD (for non-rotational solid state devices)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recovery_max_active_ssd 10
ceph config get osd osd_recovery_max_active_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_active_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_max_chunk

| | |
|---|---|
| Type | Size · default `8_M` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_chunk) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recovery_max_chunk 8_M
ceph config get osd osd_recovery_max_chunk
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_max_omap_entries_per_chunk

| | |
|---|---|
| Type | Uint · default `8096` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_omap_entries_per_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_omap_entries_per_chunk) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recovery_max_omap_entries_per_chunk 8096
ceph config get osd osd_recovery_max_omap_entries_per_chunk
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8096`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_omap_entries_per_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_max_single_start

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_max_single_start](../../../config/osd/osd.md#SP_osd_recovery_max_single_start) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_recovery_max_single_start 1
ceph config get osd osd_recovery_max_single_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_max_single_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_retry_interval

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_retry_interval](../../../config/osd/osd.md#SP_osd_recovery_retry_interval) |

**What it does:** how frequently to retry recovery reservations after being denied (e.g., due to a full OSD)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_retry_interval 30
ceph config get osd osd_recovery_retry_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep](../../../config/osd/osd.md#SP_osd_recovery_sleep) |

**What it does:** Pause between recovery/backfill chunks (seconds). Non-zero values throttle recovery to leave headroom for application I/O.

**When to use:** Use on busy clusters during business hours; set to 0 for fastest rebuild in maintenance windows.

**Example:**

```bash
ceph config set osd osd_recovery_sleep 0
ceph config get osd osd_recovery_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_degraded

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_degraded](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded) |

**What it does:** Time in seconds to sleep before next recovery or backfill op when PGs are degraded. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_degraded 0
ceph config get osd osd_recovery_sleep_degraded
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_degraded
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_degraded_hdd

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_degraded_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hdd) |

**What it does:** Time in seconds to sleep before next recovery or backfill op for HDDs when PGs is degraded.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_degraded_hdd 0.1
ceph config get osd osd_recovery_sleep_degraded_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_degraded_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_degraded_hybrid

| | |
|---|---|
| Type | Float · default `0.025` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_degraded_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hybrid) |

**What it does:** Time in seconds to sleep before next recovery or backfill op when PGs are degraded and data is on HDD and journal is on SSD

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_degraded_hybrid 0.025
ceph config get osd osd_recovery_sleep_degraded_hybrid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.025`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_degraded_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_degraded_ssd

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_degraded_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_ssd) |

**What it does:** Time in seconds to sleep before next recovery or backfill op for SSDs when PGs are degraded.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_degraded_ssd 0
ceph config get osd osd_recovery_sleep_degraded_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_degraded_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_hdd

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_hdd) |

**What it does:** Time in seconds to sleep before next recovery or backfill op for HDDs

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_hdd 0.1
ceph config get osd osd_recovery_sleep_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_hybrid

| | |
|---|---|
| Type | Float · default `0.025` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_hybrid) |

**What it does:** Time in seconds to sleep before next recovery or backfill op when data is on HDD and journal is on SSD

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_hybrid 0.025
ceph config get osd osd_recovery_sleep_hybrid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.025`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_recovery_sleep_ssd

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_recovery_sleep_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_ssd) |

**What it does:** Time in seconds to sleep before next recovery or backfill op for SSDs

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_recovery_sleep_ssd 0
ceph config get osd osd_recovery_sleep_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_recovery_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
