# Target

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [target_max_misplaced_ratio](#target_max_misplaced_ratio) | `0.05` | Basic | Performance |

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

### target_max_misplaced_ratio

| | |
|---|---|
| Type | Float · default `0.05` · **Basic** |
| Table | [target.md#SP_target_max_misplaced_ratio](../../../config/global/target.md#SP_target_max_misplaced_ratio) |

**What it does:** Max ratio of misplaced RADOS objects to target when scheduling data rebalancing activity. A lower value results in the balancer making smaller, less impactful changes with the tradeoff of decreased efficiency and longer time to converge. When making CRUSH rules or topolgy changes or performing large cluster expansions, a lower value can help avoid transitory nearfull or backfillfull ratio excursions.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global target_max_misplaced_ratio 0.05
ceph config get global target_max_misplaced_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global target_max_misplaced_ratio
ceph -s
```

---


[← Overview](../OVERVIEW.md)
