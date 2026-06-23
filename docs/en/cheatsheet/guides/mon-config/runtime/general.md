# General monitor

MON config deep dive — 44 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [enable_availability_tracking](#enable_availability_tracking) | `False` | Advanced | Policy |
| [mon_clock_drift_allowed](#mon_clock_drift_allowed) | `0.05` | Advanced | Performance |
| [mon_clock_drift_warn_backoff](#mon_clock_drift_warn_backoff) | `5` | Advanced | Performance |
| [mon_compact_on_bootstrap](#mon_compact_on_bootstrap) | `False` | Advanced | Performance |
| [mon_compact_on_start](#mon_compact_on_start) | `False` | Advanced | Performance |
| [mon_compact_on_trim](#mon_compact_on_trim) | `True` | Advanced | Performance |
| [mon_con_tracker_score_halflife](#mon_con_tracker_score_halflife) | `43200` | Advanced | Performance |
| [mon_cpu_threads](#mon_cpu_threads) | `4` | Advanced | Performance |
| [mon_crush_min_required_version](#mon_crush_min_required_version) | `hammer` | Advanced | Performance |
| [mon_daemon_bytes](#mon_daemon_bytes) | `400_M` | Advanced | Performance |
| [mon_down_added_grace](#mon_down_added_grace) | `3_min` | Advanced | Performance |
| [mon_down_mkfs_grace](#mon_down_mkfs_grace) | `1_min` | Advanced | Performance |
| [mon_down_uptime_grace](#mon_down_uptime_grace) | `1_min` | Advanced | Performance |
| [mon_elector_ignore_propose_margin](#mon_elector_ignore_propose_margin) | `0.0005` | Advanced | Performance |
| [mon_elector_ping_divisor](#mon_elector_ping_divisor) | `2` | Advanced | Performance |
| [mon_enable_op_tracker](#mon_enable_op_tracker) | `True` | Advanced | Policy |
| [mon_fsmap_prune_threshold](#mon_fsmap_prune_threshold) | `300` | Advanced | Performance |
| [mon_health_max_detail](#mon_health_max_detail) | `50` | Advanced | Performance |
| [mon_lease](#mon_lease) | `5` | Advanced | Performance |
| [mon_mds_force_trim_to](#mon_mds_force_trim_to) | `0` | Dev | Dev |
| [mon_mds_skip_sanity](#mon_mds_skip_sanity) | `False` | Advanced | Performance |
| [mon_memory_autotune](#mon_memory_autotune) | `True` | Basic | Policy |
| [mon_memory_target](#mon_memory_target) | `2_G` | Basic | Policy |
| [mon_nvmeofgw_beacon_grace](#mon_nvmeofgw_beacon_grace) | `7` | Advanced | Performance |
| [mon_nvmeofgw_beacons_till_ack](#mon_nvmeofgw_beacons_till_ack) | `15` | Advanced | Performance |
| [mon_nvmeofgw_delete_grace](#mon_nvmeofgw_delete_grace) | `15_min` | Advanced | Performance |
| [mon_nvmeofgw_set_group_id_retry](#mon_nvmeofgw_set_group_id_retry) | `1000` | Advanced | Performance |
| [mon_nvmeofgw_wrong_map_ignore_sec](#mon_nvmeofgw_wrong_map_ignore_sec) | `15` | Advanced | Performance |
| [mon_op_complaint_time](#mon_op_complaint_time) | `30` | Advanced | Performance |
| [mon_op_history_duration](#mon_op_history_duration) | `10_min` | Advanced | Performance |
| [mon_op_history_size](#mon_op_history_size) | `20` | Advanced | Performance |
| [mon_op_history_slow_op_size](#mon_op_history_slow_op_size) | `20` | Advanced | Performance |
| [mon_op_history_slow_op_threshold](#mon_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [mon_rocksdb_options](#mon_rocksdb_options) | `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` | Advanced | Performance |
| [mon_stretch_cluster_recovery_ratio](#mon_stretch_cluster_recovery_ratio) | `0.6` | Advanced | Performance |
| [mon_stretch_max_bucket_weight_delta](#mon_stretch_max_bucket_weight_delta) | `0.1` | Dev | Dev |
| [mon_stretch_recovery_min_wait](#mon_stretch_recovery_min_wait) | `15` | Advanced | Performance |
| [mon_warn_on_colocated_monitors](#mon_warn_on_colocated_monitors) | `False` | Advanced | Performance |
| [mon_warn_on_crush_straw_calc_version_zero](#mon_warn_on_crush_straw_calc_version_zero) | `True` | Advanced | Performance |
| [mon_warn_on_degraded_stretch_mode](#mon_warn_on_degraded_stretch_mode) | `True` | Advanced | Performance |
| [mon_warn_on_legacy_crush_tunables](#mon_warn_on_legacy_crush_tunables) | `True` | Advanced | Performance |
| [mon_warn_on_older_version](#mon_warn_on_older_version) | `True` | Advanced | Performance |
| [nvmeof_mon_client_connect_panic](#nvmeof_mon_client_connect_panic) | `30` | Advanced | Performance |
| [nvmeof_mon_client_disconnect_panic](#nvmeof_mon_client_disconnect_panic) | `100` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### enable_availability_tracking

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_enable_availability_tracking](../../../config/mon/mon.md#SP_enable_availability_tracking) |

**What it does:** Calculate and store availablity score for each pool in the cluster at regular intervals

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon enable_availability_tracking true
ceph config get mon enable_availability_tracking
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon enable_availability_tracking
ceph -s
ceph mon stat
```

---

### mon_clock_drift_allowed

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [mon.md#SP_mon_clock_drift_allowed](../../../config/mon/mon.md#SP_mon_clock_drift_allowed) |

**What it does:** Maximum clock drift (seconds) between monitors before health warnings.

**When to use:** Ensure NTP/chrony is stable first. Increase only as a temporary mitigation while fixing time sync.

**Example:**

```bash
ceph config set mon mon_clock_drift_allowed 0.05
ceph config get mon mon_clock_drift_allowed
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_clock_drift_allowed
ceph -s
ceph mon stat
```

---

### mon_clock_drift_warn_backoff

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_clock_drift_warn_backoff](../../../config/mon/mon.md#SP_mon_clock_drift_warn_backoff) |

**What it does:** exponential backoff factor for logging clock drift warnings in the cluster log

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_clock_drift_warn_backoff 5
ceph config get mon mon_clock_drift_warn_backoff
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_clock_drift_warn_backoff
ceph -s
ceph mon stat
```

---

### mon_compact_on_bootstrap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_compact_on_bootstrap](../../../config/mon/mon.md#SP_mon_compact_on_bootstrap) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_compact_on_bootstrap true
ceph config get mon mon_compact_on_bootstrap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_compact_on_bootstrap
ceph -s
ceph mon stat
```

---

### mon_compact_on_start

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_compact_on_start](../../../config/mon/mon.md#SP_mon_compact_on_start) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_compact_on_start true
ceph config get mon mon_compact_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_compact_on_start
ceph -s
ceph mon stat
```

---

### mon_compact_on_trim

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_compact_on_trim](../../../config/mon/mon.md#SP_mon_compact_on_trim) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_compact_on_trim false
ceph config get mon mon_compact_on_trim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_compact_on_trim
ceph -s
ceph mon stat
```

---

### mon_con_tracker_score_halflife

| | |
|---|---|
| Type | Uint · default `43200` · **Advanced** |
| Table | [mon.md#SP_mon_con_tracker_score_halflife](../../../config/mon/mon.md#SP_mon_con_tracker_score_halflife) |

**What it does:** The 'halflife' used when updating/calculating peer connection scores

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_con_tracker_score_halflife 43200
ceph config get mon mon_con_tracker_score_halflife
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `43200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `60`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_con_tracker_score_halflife
ceph -s
ceph mon stat
```

---

### mon_cpu_threads

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [mon.md#SP_mon_cpu_threads](../../../config/mon/mon.md#SP_mon_cpu_threads) |

**What it does:** worker threads for CPU intensive background work

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_cpu_threads 4
ceph config get mon mon_cpu_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cpu_threads
ceph -s
ceph mon stat
```

---

### mon_crush_min_required_version

| | |
|---|---|
| Type | Str · default `hammer` · **Advanced** |
| Table | [mon.md#SP_mon_crush_min_required_version](../../../config/mon/mon.md#SP_mon_crush_min_required_version) |

**What it does:** minimum ceph release to use for mon_warn_on_legacy_crush_tunables

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_crush_min_required_version hammer
ceph config get mon mon_crush_min_required_version
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `hammer`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_crush_min_required_version
ceph -s
ceph mon stat
```

---

### mon_daemon_bytes

| | |
|---|---|
| Type | Size · default `400_M` · **Advanced** |
| Table | [mon.md#SP_mon_daemon_bytes](../../../config/mon/mon.md#SP_mon_daemon_bytes) |

**What it does:** max bytes of outstanding mon messages mon will read off the network

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_daemon_bytes 400_M
ceph config get mon mon_daemon_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `400_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_daemon_bytes
ceph -s
ceph mon stat
```

---

### mon_down_added_grace

| | |
|---|---|
| Type | Secs · default `3_min` · **Advanced** |
| Table | [mon.md#SP_mon_down_added_grace](../../../config/mon/mon.md#SP_mon_down_added_grace) |

**What it does:** Period in seconds that the cluster may have a newly added mon down

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_down_added_grace 3_min
ceph config get mon mon_down_added_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_down_added_grace
ceph -s
ceph mon stat
```

---

### mon_down_mkfs_grace

| | |
|---|---|
| Type | Secs · default `1_min` · **Advanced** |
| Table | [mon.md#SP_mon_down_mkfs_grace](../../../config/mon/mon.md#SP_mon_down_mkfs_grace) |

**What it does:** Period in seconds that the cluster may have a mon down after cluster creation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_down_mkfs_grace 1_min
ceph config get mon mon_down_mkfs_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_down_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_down_uptime_grace

| | |
|---|---|
| Type | Secs · default `1_min` · **Advanced** |
| Table | [mon.md#SP_mon_down_uptime_grace](../../../config/mon/mon.md#SP_mon_down_uptime_grace) |

**What it does:** Period in seconds that the cluster may have a mon down after this (leader) monitor comes up.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_down_uptime_grace 1_min
ceph config get mon mon_down_uptime_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_down_uptime_grace
ceph -s
ceph mon stat
```

---

### mon_elector_ignore_propose_margin

| | |
|---|---|
| Type | Float · default `0.0005` · **Advanced** |
| Table | [mon.md#SP_mon_elector_ignore_propose_margin](../../../config/mon/mon.md#SP_mon_elector_ignore_propose_margin) |

**What it does:** The difference in connection score allowed before a peon stops ignoring out-of-quorum PROPOSEs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_elector_ignore_propose_margin 0.0005
ceph config get mon mon_elector_ignore_propose_margin
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.0005`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_elector_ignore_propose_margin
ceph -s
ceph mon stat
```

---

### mon_elector_ping_divisor

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_elector_ping_divisor](../../../config/mon/mon.md#SP_mon_elector_ping_divisor) |

**What it does:** We will send a ping up to this many times per timeout per

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_elector_ping_divisor 2
ceph config get mon mon_elector_ping_divisor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_elector_ping_divisor
ceph -s
ceph mon stat
```

---

### mon_enable_op_tracker

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_enable_op_tracker](../../../config/mon/mon.md#SP_mon_enable_op_tracker) |

**What it does:** enable/disable MON op tracking

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_enable_op_tracker false
ceph config get mon mon_enable_op_tracker
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_enable_op_tracker
ceph -s
ceph mon stat
```

---

### mon_fsmap_prune_threshold

| | |
|---|---|
| Type | Secs · default `300` · **Advanced** |
| Table | [mon.md#SP_mon_fsmap_prune_threshold](../../../config/mon/mon.md#SP_mon_fsmap_prune_threshold) |

**What it does:** prune fsmap older than this threshold in seconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_fsmap_prune_threshold 300
ceph config get mon mon_fsmap_prune_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `300`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_fsmap_prune_threshold
ceph -s
ceph mon stat
```

---

### mon_health_max_detail

| | |
|---|---|
| Type | Uint · default `50` · **Advanced** |
| Table | [mon.md#SP_mon_health_max_detail](../../../config/mon/mon.md#SP_mon_health_max_detail) |

**What it does:** max detailed pgs to report in health detail

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_health_max_detail 50
ceph config get mon mon_health_max_detail
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_health_max_detail
ceph -s
ceph mon stat
```

---

### mon_lease

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_lease](../../../config/mon/mon.md#SP_mon_lease) |

**What it does:** lease interval between quorum monitors (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_lease 5
ceph config get mon mon_lease
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_lease
ceph -s
ceph mon stat
```

---

### mon_mds_force_trim_to

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mon.md#SP_mon_mds_force_trim_to](../../../config/mon/mon.md#SP_mon_mds_force_trim_to) |

**What it does:** force mons to trim mdsmaps/fsmaps up to this epoch

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_mds_force_trim_to 64
ceph config get mon mon_mds_force_trim_to
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_mds_skip_sanity

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_mds_skip_sanity](../../../config/mon/mon.md#SP_mon_mds_skip_sanity) |

**What it does:** skip sanity checks on fsmap/mdsmap

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_mds_skip_sanity true
ceph config get mon mon_mds_skip_sanity
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_mds_skip_sanity
ceph -s
ceph mon stat
```

---

### mon_memory_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [mon.md#SP_mon_memory_autotune](../../../config/mon/mon.md#SP_mon_memory_autotune) |

**What it does:** Autotune the cache memory being used for osd monitors and kv database

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_memory_autotune false
ceph config get mon mon_memory_autotune
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_memory_autotune
ceph -s
ceph mon stat
```

---

### mon_memory_target

| | |
|---|---|
| Type | Size · default `2_G` · **Basic** |
| Table | [mon.md#SP_mon_memory_target](../../../config/mon/mon.md#SP_mon_memory_target) |

**What it does:** The amount of bytes pertaining to osd monitor caches and kv cache to be kept mapped in memory with cache auto-tuning enabled

**When to use:** Core MON behavior — review before changing in production.

**Example:**

```bash
ceph config set mon mon_memory_target 2_G
ceph config get mon mon_memory_target
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `2_G` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_memory_target
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacon_grace

| | |
|---|---|
| Type | Secs · default `7` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_beacon_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacon_grace) |

**What it does:** Period in seconds from last beacon to monitor marking a NVMeoF gateway as failed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_beacon_grace 7
ceph config get mon mon_nvmeofgw_beacon_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacons_till_ack

| | |
|---|---|
| Type | Uint · default `15` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_beacons_till_ack](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacons_till_ack) |

**What it does:** Number of beacons from MonClient before NVMeofGwMon sends ack-map to it

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_beacons_till_ack 15
ceph config get mon mon_nvmeofgw_beacons_till_ack
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_beacons_till_ack
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_delete_grace

| | |
|---|---|
| Type | Secs · default `15_min` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_delete_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_delete_grace) |

**What it does:** Issue NVMEOF_GATEWAY_DELETING health warning after this amount of time has elapsed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_delete_grace 15_min
ceph config get mon mon_nvmeofgw_delete_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_delete_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_set_group_id_retry

| | |
|---|---|
| Type | Uint · default `1000` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_set_group_id_retry](../../../config/mon/mon.md#SP_mon_nvmeofgw_set_group_id_retry) |

**What it does:** Retry wait time in microsecond for set group id between the monitor client and gateway

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_set_group_id_retry 1000
ceph config get mon mon_nvmeofgw_set_group_id_retry
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_set_group_id_retry
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_wrong_map_ignore_sec

| | |
|---|---|
| Type | Uint · default `15` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec](../../../config/mon/mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec) |

**What it does:** Period in seconds from MonClient startup to ignore wrong maps from Monitor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_wrong_map_ignore_sec 15
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
ceph -s
ceph mon stat
```

---

### mon_op_complaint_time

| | |
|---|---|
| Type | Secs · default `30` · **Advanced** |
| Table | [mon.md#SP_mon_op_complaint_time](../../../config/mon/mon.md#SP_mon_op_complaint_time) |

**What it does:** time after which to consider a monitor operation blocked after no updates

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_complaint_time 30
ceph config get mon mon_op_complaint_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_complaint_time
ceph -s
ceph mon stat
```

---

### mon_op_history_duration

| | |
|---|---|
| Type | Secs · default `10_min` · **Advanced** |
| Table | [mon.md#SP_mon_op_history_duration](../../../config/mon/mon.md#SP_mon_op_history_duration) |

**What it does:** expiration time in seconds of historical MON OPS

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_history_duration 10_min
ceph config get mon mon_op_history_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_history_duration
ceph -s
ceph mon stat
```

---

### mon_op_history_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [mon.md#SP_mon_op_history_size](../../../config/mon/mon.md#SP_mon_op_history_size) |

**What it does:** max number of completed ops to track

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_history_size 20
ceph config get mon mon_op_history_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_history_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_size

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [mon.md#SP_mon_op_history_slow_op_size](../../../config/mon/mon.md#SP_mon_op_history_slow_op_size) |

**What it does:** max number of slow historical MON OPS to keep

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_history_slow_op_size 20
ceph config get mon mon_op_history_slow_op_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_history_slow_op_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_threshold

| | |
|---|---|
| Type | Secs · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_op_history_slow_op_threshold](../../../config/mon/mon.md#SP_mon_op_history_slow_op_threshold) |

**What it does:** duration of an op to be considered as a historical slow op

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_history_slow_op_threshold 10
ceph config get mon mon_op_history_slow_op_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_history_slow_op_threshold
ceph -s
ceph mon stat
```

---

### mon_rocksdb_options

| | |
|---|---|
| Type | Str · default `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` · **Advanced** |
| Table | [mon.md#SP_mon_rocksdb_options](../../../config/mon/mon.md#SP_mon_rocksdb_options) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_rocksdb_options "write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true"
ceph config get mon mon_rocksdb_options
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_rocksdb_options
ceph -s
ceph mon stat
```

---

### mon_stretch_cluster_recovery_ratio

| | |
|---|---|
| Type | Float · default `0.6` · **Advanced** |
| Table | [mon.md#SP_mon_stretch_cluster_recovery_ratio](../../../config/mon/mon.md#SP_mon_stretch_cluster_recovery_ratio) |

**What it does:** the ratio of up OSDs at which a degraded stretch cluster enters recovery

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_stretch_cluster_recovery_ratio 0.6
ceph config get mon mon_stretch_cluster_recovery_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0.51`, max `1`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_stretch_cluster_recovery_ratio
ceph -s
ceph mon stat
```

---

### mon_stretch_max_bucket_weight_delta

| | |
|---|---|
| Type | Float · default `0.1` · **Dev** |
| Table | [mon.md#SP_mon_stretch_max_bucket_weight_delta](../../../config/mon/mon.md#SP_mon_stretch_max_bucket_weight_delta) |

**What it does:** Max difference allowed among CRUSH bucket weights when in stretch mode. The value is a percentage expressed as a real number between 0.0 and 1.0.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_stretch_max_bucket_weight_delta 0.1
ceph config get mon mon_stretch_max_bucket_weight_delta
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_stretch_recovery_min_wait

| | |
|---|---|
| Type | Float · default `15` · **Advanced** |
| Table | [mon.md#SP_mon_stretch_recovery_min_wait](../../../config/mon/mon.md#SP_mon_stretch_recovery_min_wait) |

**What it does:** how long the monitors wait before considering fully-healthy PGs as evidence the stretch mode is repaired

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_stretch_recovery_min_wait 15
ceph config get mon mon_stretch_recovery_min_wait
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_stretch_recovery_min_wait
ceph -s
ceph mon stat
```

---

### mon_warn_on_colocated_monitors

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_colocated_monitors](../../../config/mon/mon.md#SP_mon_warn_on_colocated_monitors) |

**What it does:** Issue MON_COLOCATED health warning if two or more Monitors have the same IP address

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_warn_on_colocated_monitors true
ceph config get mon mon_warn_on_colocated_monitors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_colocated_monitors
ceph -s
ceph mon stat
```

---

### mon_warn_on_crush_straw_calc_version_zero

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_crush_straw_calc_version_zero](../../../config/mon/mon.md#SP_mon_warn_on_crush_straw_calc_version_zero) |

**What it does:** issue OLD_CRUSH_STRAW_CALC_VERSION health warning if the CRUSH map's straw_calc_version is zero

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_crush_straw_calc_version_zero false
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
ceph -s
ceph mon stat
```

---

### mon_warn_on_degraded_stretch_mode

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_degraded_stretch_mode](../../../config/mon/mon.md#SP_mon_warn_on_degraded_stretch_mode) |

**What it does:** Issue a health warning if we are in degraded stretch mode

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_degraded_stretch_mode false
ceph config get mon mon_warn_on_degraded_stretch_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_degraded_stretch_mode
ceph -s
ceph mon stat
```

---

### mon_warn_on_legacy_crush_tunables

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_legacy_crush_tunables](../../../config/mon/mon.md#SP_mon_warn_on_legacy_crush_tunables) |

**What it does:** issue OLD_CRUSH_TUNABLES health warning if CRUSH tunables are older than mon_crush_min_required_version

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_legacy_crush_tunables false
ceph config get mon mon_warn_on_legacy_crush_tunables
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_legacy_crush_tunables
ceph -s
ceph mon stat
```

---

### mon_warn_on_older_version

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_older_version](../../../config/mon/mon.md#SP_mon_warn_on_older_version) |

**What it does:** issue DAEMON_OLD_VERSION health warning if daemons are not all running the same version

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_older_version false
ceph config get mon mon_warn_on_older_version
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_older_version
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_connect_panic

| | |
|---|---|
| Type | Secs · default `30` · **Advanced** |
| Table | [mon.md#SP_nvmeof_mon_client_connect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_connect_panic) |

**What it does:** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it does not receive the initial map from the monitor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon nvmeof_mon_client_connect_panic 30
ceph config get mon nvmeof_mon_client_connect_panic
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon nvmeof_mon_client_connect_panic
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_disconnect_panic

| | |
|---|---|
| Type | Secs · default `100` · **Advanced** |
| Table | [mon.md#SP_nvmeof_mon_client_disconnect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_disconnect_panic) |

**What it does:** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it loses connection to the monitor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon nvmeof_mon_client_disconnect_panic 100
ceph config get mon nvmeof_mon_client_disconnect_panic
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon nvmeof_mon_client_disconnect_panic
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
