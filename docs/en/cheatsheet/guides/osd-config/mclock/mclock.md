# mClock scheduler

OSD config deep dive — 18 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_mclock_force_run_benchmark_on_init](#osd_mclock_force_run_benchmark_on_init) | `False` | Advanced | Performance |
| [osd_mclock_iops_capacity_low_threshold_hdd](#osd_mclock_iops_capacity_low_threshold_hdd) | `50` | Basic | Performance |
| [osd_mclock_iops_capacity_low_threshold_ssd](#osd_mclock_iops_capacity_low_threshold_ssd) | `1000` | Basic | Performance |
| [osd_mclock_iops_capacity_threshold_hdd](#osd_mclock_iops_capacity_threshold_hdd) | `500` | Basic | Performance |
| [osd_mclock_iops_capacity_threshold_ssd](#osd_mclock_iops_capacity_threshold_ssd) | `80000` | Basic | Performance |
| [osd_mclock_max_capacity_iops_hdd](#osd_mclock_max_capacity_iops_hdd) | `315` | Basic | Performance |
| [osd_mclock_max_capacity_iops_ssd](#osd_mclock_max_capacity_iops_ssd) | `21500` | Basic | Performance |
| [osd_mclock_max_sequential_bandwidth_hdd](#osd_mclock_max_sequential_bandwidth_hdd) | `150_M` | Basic | Performance |
| [osd_mclock_max_sequential_bandwidth_ssd](#osd_mclock_max_sequential_bandwidth_ssd) | `1200_M` | Basic | Performance |
| [osd_mclock_profile](#osd_mclock_profile) | `balanced` | Advanced | Performance |
| [osd_mclock_scheduler_anticipation_timeout](#osd_mclock_scheduler_anticipation_timeout) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_best_effort_lim](#osd_mclock_scheduler_background_best_effort_lim) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_best_effort_res](#osd_mclock_scheduler_background_best_effort_res) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_best_effort_wgt](#osd_mclock_scheduler_background_best_effort_wgt) | `1` | Advanced | Performance |
| [osd_mclock_scheduler_client_lim](#osd_mclock_scheduler_client_lim) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_client_res](#osd_mclock_scheduler_client_res) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_client_wgt](#osd_mclock_scheduler_client_wgt) | `1` | Advanced | Performance |
| [osd_mclock_skip_benchmark](#osd_mclock_skip_benchmark) | `False` | Dev | Dev |

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

### osd_mclock_force_run_benchmark_on_init

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_mclock_force_run_benchmark_on_init](../../../config/osd/osd.md#SP_osd_mclock_force_run_benchmark_on_init) |

**What it does:** Force run the OSD benchmark on OSD initialization/boot-up

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_mclock_force_run_benchmark_on_init true
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_hdd

| | |
|---|---|
| Type | Float · default `50` · **Basic** |
| Table | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd) |

**What it does:** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for rotational media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_hdd 50
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_ssd

| | |
|---|---|
| Type | Float · default `1000` · **Basic** |
| Table | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd) |

**What it does:** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for solid state media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_ssd 1000
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_hdd

| | |
|---|---|
| Type | Float · default `500` · **Basic** |
| Table | [osd.md#SP_osd_mclock_iops_capacity_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_hdd) |

**What it does:** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for rotational media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_hdd 500
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_ssd

| | |
|---|---|
| Type | Float · default `80000` · **Basic** |
| Table | [osd.md#SP_osd_mclock_iops_capacity_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_ssd) |

**What it does:** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for solid state media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_ssd 80000
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `80000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_hdd

| | |
|---|---|
| Type | Float · default `315` · **Basic** |
| Table | [osd.md#SP_osd_mclock_max_capacity_iops_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_hdd) |

**What it does:** Max random write IOPS capacity (at 4KiB block size) to consider per OSD (for rotational media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_max_capacity_iops_hdd 315
ceph config get osd osd_mclock_max_capacity_iops_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `315`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_max_capacity_iops_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_ssd

| | |
|---|---|
| Type | Float · default `21500` · **Basic** |
| Table | [osd.md#SP_osd_mclock_max_capacity_iops_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_ssd) |

**What it does:** Max random write IOPS capacity (at 4 KiB block size) to consider per OSD (for solid state media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_max_capacity_iops_ssd 21500
ceph config get osd osd_mclock_max_capacity_iops_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `21500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_max_capacity_iops_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_hdd

| | |
|---|---|
| Type | Size · default `150_M` · **Basic** |
| Table | [osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd) |

**What it does:** The maximum sequential bandwidth in bytes/second of the OSD (for rotational media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_hdd 150_M
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `150_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_ssd

| | |
|---|---|
| Type | Size · default `1200_M` · **Basic** |
| Table | [osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd) |

**What it does:** The maximum sequential bandwidth in bytes/second of the OSD (for solid state media)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_ssd 1200_M
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1200_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_profile

| | |
|---|---|
| Type | Str · enum: ["balanced", "high_recovery_ops", "high_client_ops", "custom"] · default `balanced` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_profile](../../../config/osd/osd.md#SP_osd_mclock_profile) |

**What it does:** Selects the mClock scheduler profile (`balanced`, `high_client_ops`, `high_recovery_ops`, or custom).

**When to use:** Start with `balanced` on mixed workloads. Use `high_client_ops` when recovery dominates latency; `high_recovery_ops` for aggressive rebuild windows.

**Example:**

```bash
ceph config set osd osd_mclock_profile high_client_ops
ceph config get osd osd_mclock_profile
ceph daemon osd.<id> config show | grep mclock
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `balanced`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_profile
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_anticipation_timeout

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_anticipation_timeout](../../../config/osd/osd.md#SP_osd_mclock_scheduler_anticipation_timeout) |

**What it does:** mclock anticipation timeout in seconds

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_anticipation_timeout 0
ceph config get osd osd_mclock_scheduler_anticipation_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_anticipation_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_best_effort_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_lim) |

**What it does:** IO limit for background best_effort over reservation. The default value of 0 specifies no limit enforcement, which means background best_effort operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background best_effort operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_lim 0
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
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
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_res

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_best_effort_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_res) |

**What it does:** IO proportion reserved for background best_effort (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background best_effort operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_res 0
ceph config get osd osd_mclock_scheduler_background_best_effort_res
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
ceph config get osd osd_mclock_scheduler_background_best_effort_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_wgt

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt) |

**What it does:** IO share for each background best_effort over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_wgt 1
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_client_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_lim) |

**What it does:** IO limit for each client (default) over reservation. The default value of 0 specifies no limit enforcement, which means each client can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that each client receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_client_lim 0
ceph config get osd osd_mclock_scheduler_client_lim
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
ceph config get osd osd_mclock_scheduler_client_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_res

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_client_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_res) |

**What it does:** IO proportion reserved for each client (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for each client in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_client_res 0
ceph config get osd osd_mclock_scheduler_client_res
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
ceph config get osd osd_mclock_scheduler_client_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_wgt

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_mclock_scheduler_client_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_wgt) |

**What it does:** IO share for each client (default) over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_mclock_scheduler_client_wgt 1
ceph config get osd osd_mclock_scheduler_client_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_mclock_scheduler_client_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_skip_benchmark

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_mclock_skip_benchmark](../../../config/osd/osd.md#SP_osd_mclock_skip_benchmark) |

**What it does:** Skip the OSD benchmark on OSD initialization/boot-up

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_mclock_skip_benchmark true
ceph config get osd osd_mclock_skip_benchmark
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
