# Intervals

MGR config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_delta_reset_interval](#mon_delta_reset_interval) | `10` | Advanced | Performance |
| [mon_stat_smooth_intervals](#mon_stat_smooth_intervals) | `6` | Advanced | Performance |

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

### mon_delta_reset_interval

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_delta_reset_interval](../../../config/mgr/mon.md#SP_mon_delta_reset_interval) |

**What it does:** window duration for rate calculations in 'ceph status'

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_delta_reset_interval 10
ceph config get mon mon_delta_reset_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_delta_reset_interval
ceph -s
ceph mon stat
```

---

### mon_stat_smooth_intervals

| | |
|---|---|
| Type | Uint · default `6` · **Advanced** |
| Table | [mon.md#SP_mon_stat_smooth_intervals](../../../config/mgr/mon.md#SP_mon_stat_smooth_intervals) |

**What it does:** number of PGMaps stats over which we calc the average read/write throughput of the whole cluster

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_stat_smooth_intervals 6
ceph config get mon mon_stat_smooth_intervals
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_stat_smooth_intervals
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
