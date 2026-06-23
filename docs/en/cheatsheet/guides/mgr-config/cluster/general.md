# General manager

MGR config deep dive — 8 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_cache_target_full_warn_ratio](#mon_cache_target_full_warn_ratio) | `0.66` | Advanced | Performance |
| [mon_osd_err_op_age_ratio](#mon_osd_err_op_age_ratio) | `128` | Advanced | Performance |
| [mon_reweight_max_change](#mon_reweight_max_change) | `0.05` | Advanced | Performance |
| [mon_reweight_max_osds](#mon_reweight_max_osds) | `4` | Advanced | Performance |
| [mon_reweight_min_bytes_per_osd](#mon_reweight_min_bytes_per_osd) | `100_M` | Advanced | Performance |
| [mon_reweight_min_pgs_per_osd](#mon_reweight_min_pgs_per_osd) | `10` | Advanced | Performance |
| [mon_warn_on_misplaced](#mon_warn_on_misplaced) | `False` | Advanced | Performance |
| [mon_warn_on_too_few_osds](#mon_warn_on_too_few_osds) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_cache_target_full_warn_ratio

| | |
|---|---|
| Type | Float · default `0.66` · **Advanced** |
| Table | [mon.md#SP_mon_cache_target_full_warn_ratio](../../../config/mgr/mon.md#SP_mon_cache_target_full_warn_ratio) |

**What it does:** issue CACHE_POOL_NEAR_FULL health warning when cache pool utilization exceeds this ratio of usable space

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_cache_target_full_warn_ratio 0.66
ceph config get mon mon_cache_target_full_warn_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.66`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cache_target_full_warn_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_err_op_age_ratio

| | |
|---|---|
| Type | Float · default `128` · **Advanced** |
| Table | [mon.md#SP_mon_osd_err_op_age_ratio](../../../config/mgr/mon.md#SP_mon_osd_err_op_age_ratio) |

**What it does:** issue REQUEST_STUCK health error if OSD ops are slower than is age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_err_op_age_ratio 128
ceph config get mon mon_osd_err_op_age_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_err_op_age_ratio
ceph -s
ceph mon stat
```

---

### mon_reweight_max_change

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [mon.md#SP_mon_reweight_max_change](../../../config/mgr/mon.md#SP_mon_reweight_max_change) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_reweight_max_change 0.05
ceph config get mon mon_reweight_max_change
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_reweight_max_change
ceph -s
ceph mon stat
```

---

### mon_reweight_max_osds

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [mon.md#SP_mon_reweight_max_osds](../../../config/mgr/mon.md#SP_mon_reweight_max_osds) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_reweight_max_osds 4
ceph config get mon mon_reweight_max_osds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_reweight_max_osds
ceph -s
ceph mon stat
```

---

### mon_reweight_min_bytes_per_osd

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [mon.md#SP_mon_reweight_min_bytes_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_bytes_per_osd) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_reweight_min_bytes_per_osd 100_M
ceph config get mon mon_reweight_min_bytes_per_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_reweight_min_bytes_per_osd
ceph -s
ceph mon stat
```

---

### mon_reweight_min_pgs_per_osd

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_reweight_min_pgs_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_pgs_per_osd) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_reweight_min_pgs_per_osd 10
ceph config get mon mon_reweight_min_pgs_per_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_reweight_min_pgs_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_misplaced

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_misplaced](../../../config/mgr/mon.md#SP_mon_warn_on_misplaced) |

**What it does:** Issue a health warning if there are misplaced objects

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_warn_on_misplaced true
ceph config get mon mon_warn_on_misplaced
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_misplaced
ceph -s
ceph mon stat
```

---

### mon_warn_on_too_few_osds

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_too_few_osds](../../../config/mgr/mon.md#SP_mon_warn_on_too_few_osds) |

**What it does:** Issue a health warning if there are fewer OSDs than osd_pool_default_size

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_too_few_osds false
ceph config get mon mon_warn_on_too_few_osds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_too_few_osds
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
