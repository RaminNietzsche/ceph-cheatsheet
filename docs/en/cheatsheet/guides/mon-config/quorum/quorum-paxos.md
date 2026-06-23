# Quorum & Paxos

MON config deep dive — 14 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_accept_timeout_factor](#mon_accept_timeout_factor) | `2` | Advanced | Performance |
| [mon_election_default_strategy](#mon_election_default_strategy) | `1` | Advanced | Performance |
| [mon_election_timeout](#mon_election_timeout) | `5` | Advanced | Performance |
| [paxos_kill_at](#paxos_kill_at) | `0` | Dev | Dev |
| [paxos_max_join_drift](#paxos_max_join_drift) | `10` | Advanced | Performance |
| [paxos_min](#paxos_min) | `500` | Advanced | Performance |
| [paxos_min_wait](#paxos_min_wait) | `0.05` | Advanced | Performance |
| [paxos_propose_interval](#paxos_propose_interval) | `1` | Advanced | Performance |
| [paxos_service_trim_max](#paxos_service_trim_max) | `500` | Advanced | Performance |
| [paxos_service_trim_max_multiplier](#paxos_service_trim_max_multiplier) | `20` | Advanced | Performance |
| [paxos_service_trim_min](#paxos_service_trim_min) | `250` | Advanced | Performance |
| [paxos_stash_full_interval](#paxos_stash_full_interval) | `25` | Advanced | Performance |
| [paxos_trim_max](#paxos_trim_max) | `500` | Advanced | Performance |
| [paxos_trim_min](#paxos_trim_min) | `250` | Advanced | Performance |

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

### mon_accept_timeout_factor

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_accept_timeout_factor](../../../config/mon/mon.md#SP_mon_accept_timeout_factor) |

**What it does:** multiple of mon_lease for follower mons to accept proposed state changes before calling a new election

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_accept_timeout_factor 2
ceph config get mon mon_accept_timeout_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_accept_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_election_default_strategy

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [mon.md#SP_mon_election_default_strategy](../../../config/mon/mon.md#SP_mon_election_default_strategy) |

**What it does:** The election strategy to set when constructing the first monmap.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_election_default_strategy 1
ceph config get mon mon_election_default_strategy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `3`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_election_default_strategy
ceph -s
ceph mon stat
```

---

### mon_election_timeout

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_election_timeout](../../../config/mon/mon.md#SP_mon_election_timeout) |

**What it does:** maximum time for a mon election (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_election_timeout 5
ceph config get mon mon_election_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_election_timeout
ceph -s
ceph mon stat
```

---

### paxos_kill_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [paxos.md#SP_paxos_kill_at](../../../config/mon/paxos.md#SP_paxos_kill_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon paxos_kill_at 64
ceph config get mon paxos_kill_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### paxos_max_join_drift

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [paxos.md#SP_paxos_max_join_drift](../../../config/mon/paxos.md#SP_paxos_max_join_drift) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon paxos_max_join_drift 10
ceph config get mon paxos_max_join_drift
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_max_join_drift
ceph -s
ceph mon stat
```

---

### paxos_min

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [paxos.md#SP_paxos_min](../../../config/mon/paxos.md#SP_paxos_min) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon paxos_min 500
ceph config get mon paxos_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_min
ceph -s
ceph mon stat
```

---

### paxos_min_wait

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [paxos.md#SP_paxos_min_wait](../../../config/mon/paxos.md#SP_paxos_min_wait) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon paxos_min_wait 0.05
ceph config get mon paxos_min_wait
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_min_wait
ceph -s
ceph mon stat
```

---

### paxos_propose_interval

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [paxos.md#SP_paxos_propose_interval](../../../config/mon/paxos.md#SP_paxos_propose_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon paxos_propose_interval 1
ceph config get mon paxos_propose_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_propose_interval
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [paxos.md#SP_paxos_service_trim_max](../../../config/mon/paxos.md#SP_paxos_service_trim_max) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon paxos_service_trim_max 500
ceph config get mon paxos_service_trim_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_service_trim_max
ceph -s
ceph mon stat
```

---

### paxos_service_trim_max_multiplier

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [paxos.md#SP_paxos_service_trim_max_multiplier](../../../config/mon/paxos.md#SP_paxos_service_trim_max_multiplier) |

**What it does:** factor by which paxos_service_trim_max will be multiplied to get a new upper bound when trim sizes are high (0 disables it)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon paxos_service_trim_max_multiplier 20
ceph config get mon paxos_service_trim_max_multiplier
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_service_trim_max_multiplier
ceph -s
ceph mon stat
```

---

### paxos_service_trim_min

| | |
|---|---|
| Type | Uint · default `250` · **Advanced** |
| Table | [paxos.md#SP_paxos_service_trim_min](../../../config/mon/paxos.md#SP_paxos_service_trim_min) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon paxos_service_trim_min 250
ceph config get mon paxos_service_trim_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `250`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_service_trim_min
ceph -s
ceph mon stat
```

---

### paxos_stash_full_interval

| | |
|---|---|
| Type | Int · default `25` · **Advanced** |
| Table | [paxos.md#SP_paxos_stash_full_interval](../../../config/mon/paxos.md#SP_paxos_stash_full_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon paxos_stash_full_interval 25
ceph config get mon paxos_stash_full_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `25`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_stash_full_interval
ceph -s
ceph mon stat
```

---

### paxos_trim_max

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [paxos.md#SP_paxos_trim_max](../../../config/mon/paxos.md#SP_paxos_trim_max) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon paxos_trim_max 500
ceph config get mon paxos_trim_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_trim_max
ceph -s
ceph mon stat
```

---

### paxos_trim_min

| | |
|---|---|
| Type | Int · default `250` · **Advanced** |
| Table | [paxos.md#SP_paxos_trim_min](../../../config/mon/paxos.md#SP_paxos_trim_min) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon paxos_trim_min 250
ceph config get mon paxos_trim_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `250`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon paxos_trim_min
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
