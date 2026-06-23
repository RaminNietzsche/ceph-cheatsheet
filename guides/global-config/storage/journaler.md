# Journaler

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [journaler_prefetch_periods](#journaler_prefetch_periods) | `10` | Advanced | Performance |
| [journaler_prezero_periods](#journaler_prezero_periods) | `5` | Advanced | Performance |
| [journaler_write_head_interval](#journaler_write_head_interval) | `15` | Advanced | Performance |

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

### journaler_prefetch_periods

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [journaler.md#SP_journaler_prefetch_periods](../../../config/global/journaler.md#SP_journaler_prefetch_periods) |

**What it does:** Number of striping periods to prefetch while reading MDS journal

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global journaler_prefetch_periods 10
ceph config get global journaler_prefetch_periods
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `2`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global journaler_prefetch_periods
ceph -s
```

---

### journaler_prezero_periods

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [journaler.md#SP_journaler_prezero_periods](../../../config/global/journaler.md#SP_journaler_prezero_periods) |

**What it does:** Number of striping periods to zero head of MDS journal write position

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global journaler_prezero_periods 5
ceph config get global journaler_prezero_periods
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `2`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global journaler_prezero_periods
ceph -s
```

---

### journaler_write_head_interval

| | |
|---|---|
| Type | Int · default `15` · **Advanced** |
| Table | [journaler.md#SP_journaler_write_head_interval](../../../config/global/journaler.md#SP_journaler_write_head_interval) |

**What it does:** Interval in seconds between journal header updates (to help bound replay time)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global journaler_write_head_interval 15
ceph config get global journaler_write_head_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global journaler_write_head_interval
ceph -s
```

---


[← Overview](../OVERVIEW.md)
