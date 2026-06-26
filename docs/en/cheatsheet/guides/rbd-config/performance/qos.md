# QoS & throttling

RBD config deep dive — 20 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_qos_bps_burst](#rbd_qos_bps_burst) | `0` | Advanced | Performance |
| [rbd_qos_bps_burst_seconds](#rbd_qos_bps_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_bps_limit](#rbd_qos_bps_limit) | `0` | Advanced | Performance |
| [rbd_qos_exclude_ops](#rbd_qos_exclude_ops) | `(empty)` | Advanced | Performance |
| [rbd_qos_iops_burst](#rbd_qos_iops_burst) | `0` | Advanced | Performance |
| [rbd_qos_iops_burst_seconds](#rbd_qos_iops_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_iops_limit](#rbd_qos_iops_limit) | `0` | Advanced | Performance |
| [rbd_qos_read_bps_burst](#rbd_qos_read_bps_burst) | `0` | Advanced | Performance |
| [rbd_qos_read_bps_burst_seconds](#rbd_qos_read_bps_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_read_bps_limit](#rbd_qos_read_bps_limit) | `0` | Advanced | Performance |
| [rbd_qos_read_iops_burst](#rbd_qos_read_iops_burst) | `0` | Advanced | Performance |
| [rbd_qos_read_iops_burst_seconds](#rbd_qos_read_iops_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_read_iops_limit](#rbd_qos_read_iops_limit) | `0` | Advanced | Performance |
| [rbd_qos_schedule_tick_min](#rbd_qos_schedule_tick_min) | `50` | Advanced | Performance |
| [rbd_qos_write_bps_burst](#rbd_qos_write_bps_burst) | `0` | Advanced | Performance |
| [rbd_qos_write_bps_burst_seconds](#rbd_qos_write_bps_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_write_bps_limit](#rbd_qos_write_bps_limit) | `0` | Advanced | Performance |
| [rbd_qos_write_iops_burst](#rbd_qos_write_iops_burst) | `0` | Advanced | Performance |
| [rbd_qos_write_iops_burst_seconds](#rbd_qos_write_iops_burst_seconds) | `1` | Advanced | Performance |
| [rbd_qos_write_iops_limit](#rbd_qos_write_iops_limit) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_qos_bps_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst) |

**What it does:** the desired burst limit of IO bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_bps_burst 64
ceph config get client rbd_qos_bps_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_bps_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_bps_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst_seconds) |

**What it does:** the desired burst duration in seconds of IO bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_bps_burst_seconds 1
ceph config get client rbd_qos_bps_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_bps_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_bps_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_bps_limit) |

**What it does:** the desired limit of IO bytes per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_bps_limit 64
ceph config get client rbd_qos_bps_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_bps_limit
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_exclude_ops

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_exclude_ops](../../../config/rbd/rbd.md#SP_rbd_qos_exclude_ops) |

**What it does:** optionally exclude ops from QoS Optionally exclude ops from QoS. This setting accepts either an integer bitmask value or comma-delimited string of op names. This setting is always internally stored as an integer bitmask value. The mapping between op bitmask value and op name is as follows: +1 -> read, +2 -> write, +4 -> discard, +8 -> write_same, +16 -> compare_and_write

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_exclude_ops "example"
ceph config get client rbd_qos_exclude_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_exclude_ops
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_iops_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst) |

**What it does:** the desired burst limit of IO operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_iops_burst 64
ceph config get client rbd_qos_iops_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_iops_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_iops_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst_seconds) |

**What it does:** the desired burst duration in seconds of IO operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_iops_burst_seconds 1
ceph config get client rbd_qos_iops_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_iops_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_iops_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_iops_limit) |

**What it does:** the desired limit of IO operations per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_iops_limit 64
ceph config get client rbd_qos_iops_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_iops_limit
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_bps_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst) |

**What it does:** the desired burst limit of read bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_read_bps_burst 64
ceph config get client rbd_qos_read_bps_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_bps_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_bps_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst_seconds) |

**What it does:** the desired burst duration in seconds of read bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_read_bps_burst_seconds 1
ceph config get client rbd_qos_read_bps_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_bps_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_bps_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_limit) |

**What it does:** the desired limit of read bytes per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_read_bps_limit 64
ceph config get client rbd_qos_read_bps_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_bps_limit
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_iops_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst) |

**What it does:** the desired burst limit of read operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_read_iops_burst 64
ceph config get client rbd_qos_read_iops_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_iops_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_iops_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst_seconds) |

**What it does:** the desired burst duration in seconds of read operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_read_iops_burst_seconds 1
ceph config get client rbd_qos_read_iops_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_iops_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_read_iops_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_read_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_limit) |

**What it does:** the desired limit of read operations per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_read_iops_limit 64
ceph config get client rbd_qos_read_iops_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_read_iops_limit
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_schedule_tick_min

| | |
|---|---|
| Type | Uint · default `50` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_schedule_tick_min](../../../config/rbd/rbd.md#SP_rbd_qos_schedule_tick_min) |

**What it does:** minimum schedule tick (in milliseconds) for QoS This determines the minimum time (in milliseconds) at which I/Os can become unblocked if the limit of a throttle is hit. In terms of the token bucket algorithm, this is the minimum interval at which tokens are added to the bucket.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_schedule_tick_min 50
ceph config get client rbd_qos_schedule_tick_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_schedule_tick_min
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_bps_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst) |

**What it does:** the desired burst limit of write bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_write_bps_burst 64
ceph config get client rbd_qos_write_bps_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_bps_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_bps_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst_seconds) |

**What it does:** the desired burst duration in seconds of write bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_write_bps_burst_seconds 1
ceph config get client rbd_qos_write_bps_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_bps_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_bps_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_limit) |

**What it does:** the desired limit of write bytes per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_write_bps_limit 64
ceph config get client rbd_qos_write_bps_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_bps_limit
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_iops_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst) |

**What it does:** the desired burst limit of write operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_write_iops_burst 64
ceph config get client rbd_qos_write_iops_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_iops_burst
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_iops_burst_seconds

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst_seconds) |

**What it does:** the desired burst duration in seconds of write operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_qos_write_iops_burst_seconds 1
ceph config get client rbd_qos_write_iops_burst_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_iops_burst_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_qos_write_iops_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_qos_write_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_limit) |

**What it does:** the desired limit of write operations per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_qos_write_iops_limit 64
ceph config get client rbd_qos_write_iops_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_qos_write_iops_limit
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
