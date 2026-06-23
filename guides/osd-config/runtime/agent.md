# Cache agent

OSD config deep dive — 7 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_agent_delay_time](#osd_agent_delay_time) | `5` | Advanced | Performance |
| [osd_agent_hist_halflife](#osd_agent_hist_halflife) | `1000` | Advanced | Performance |
| [osd_agent_max_low_ops](#osd_agent_max_low_ops) | `2` | Advanced | Performance |
| [osd_agent_max_ops](#osd_agent_max_ops) | `4` | Advanced | Performance |
| [osd_agent_min_evict_effort](#osd_agent_min_evict_effort) | `0.1` | Advanced | Performance |
| [osd_agent_quantize_effort](#osd_agent_quantize_effort) | `0.1` | Advanced | Performance |
| [osd_agent_slop](#osd_agent_slop) | `0.02` | Advanced | Performance |

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

### osd_agent_delay_time

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_agent_delay_time](../../../config/osd/osd.md#SP_osd_agent_delay_time) |

**What it does:** how long agent should sleep if it has no work to do

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_agent_delay_time 5
ceph config get osd osd_agent_delay_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_delay_time
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_hist_halflife

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [osd.md#SP_osd_agent_hist_halflife](../../../config/osd/osd.md#SP_osd_agent_hist_halflife) |

**What it does:** halflife of agent atime and temp histograms

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_agent_hist_halflife 1000
ceph config get osd osd_agent_hist_halflife
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_hist_halflife
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_low_ops

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_agent_max_low_ops](../../../config/osd/osd.md#SP_osd_agent_max_low_ops) |

**What it does:** maximum concurrent low-priority tiering operations for tiering agent

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_agent_max_low_ops 2
ceph config get osd osd_agent_max_low_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_max_low_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_max_ops

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [osd.md#SP_osd_agent_max_ops](../../../config/osd/osd.md#SP_osd_agent_max_ops) |

**What it does:** maximum concurrent tiering operations for tiering agent

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_agent_max_ops 4
ceph config get osd osd_agent_max_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_max_ops
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_min_evict_effort

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [osd.md#SP_osd_agent_min_evict_effort](../../../config/osd/osd.md#SP_osd_agent_min_evict_effort) |

**What it does:** minimum effort to expend evicting clean objects

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_agent_min_evict_effort 0.1
ceph config get osd osd_agent_min_evict_effort
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `0.99`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_min_evict_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_quantize_effort

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [osd.md#SP_osd_agent_quantize_effort](../../../config/osd/osd.md#SP_osd_agent_quantize_effort) |

**What it does:** size of quantize unit for eviction effort

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_agent_quantize_effort 0.1
ceph config get osd osd_agent_quantize_effort
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_quantize_effort
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_agent_slop

| | |
|---|---|
| Type | Float · default `0.02` · **Advanced** |
| Table | [osd.md#SP_osd_agent_slop](../../../config/osd/osd.md#SP_osd_agent_slop) |

**What it does:** slop factor to avoid switching tiering flush and eviction mode

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_agent_slop 0.02
ceph config get osd osd_agent_slop
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.02`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_agent_slop
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
