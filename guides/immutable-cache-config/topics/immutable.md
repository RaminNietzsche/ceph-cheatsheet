# Immutable object cache

Immutable cache config deep dive — 13 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/immutable-object-cache/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [immutable_object_cache_client_dedicated_thread_num](#immutable_object_cache_client_dedicated_thread_num) | `2` | Advanced | Performance |
| [immutable_object_cache_max_inflight_ops](#immutable_object_cache_max_inflight_ops) | `128` | Advanced | Performance |
| [immutable_object_cache_max_size](#immutable_object_cache_max_size) | `1_G` | Advanced | Performance |
| [immutable_object_cache_path](#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | Advanced | Capacity |
| [immutable_object_cache_qos_bps_burst](#immutable_object_cache_qos_bps_burst) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_bps_burst_seconds](#immutable_object_cache_qos_bps_burst_seconds) | `1` | Advanced | Performance |
| [immutable_object_cache_qos_bps_limit](#immutable_object_cache_qos_bps_limit) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_iops_burst](#immutable_object_cache_qos_iops_burst) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_iops_burst_seconds](#immutable_object_cache_qos_iops_burst_seconds) | `1` | Advanced | Performance |
| [immutable_object_cache_qos_iops_limit](#immutable_object_cache_qos_iops_limit) | `0` | Advanced | Performance |
| [immutable_object_cache_qos_schedule_tick_min](#immutable_object_cache_qos_schedule_tick_min) | `50` | Advanced | Performance |
| [immutable_object_cache_sock](#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | Advanced | Performance |
| [immutable_object_cache_watermark](#immutable_object_cache_watermark) | `0.9` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. immutable-object-cache
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### immutable_object_cache_client_dedicated_thread_num

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_client_dedicated_thread_num](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_client_dedicated_thread_num) |

**What it does:** immutable object cache client dedicated thread number

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_client_dedicated_thread_num 2
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
ceph -s
```

---

### immutable_object_cache_max_inflight_ops

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_max_inflight_ops](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_inflight_ops) |

**What it does:** max inflight promoting requests for immutable object cache daemon

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_inflight_ops 128
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
ceph -s
```

---

### immutable_object_cache_max_size

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_max_size](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_size) |

**What it does:** max immutable object cache data size

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_size 1_G
ceph config get immutable_object_cache immutable_object_cache_max_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_max_size
ceph -s
```

---

### immutable_object_cache_path

| | |
|---|---|
| Type | Str · default `/tmp/ceph_immutable_object_cache` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_path](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_path) |

**What it does:** immutable object cache data dir

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_path "/tmp/ceph_immutable_object_cache"
ceph config get immutable_object_cache immutable_object_cache_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/tmp/ceph_immutable_object_cache`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_path
ceph -s
```

---

### immutable_object_cache_qos_bps_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_bps_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst) |

**What it does:** the desired burst limit of immutable object cache IO bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
ceph -s
```

---

### immutable_object_cache_qos_bps_burst_seconds

| | |
|---|---|
| Type | Secs · default `1` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds) |

**What it does:** the desired burst duration in seconds of immutable object cache IO bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
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
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_bps_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_bps_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_limit) |

**What it does:** the desired immutable object cache IO bytes limit per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
ceph -s
```

---

### immutable_object_cache_qos_iops_burst

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_iops_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst) |

**What it does:** the desired burst limit of immutable object cache IO operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
ceph -s
```

---

### immutable_object_cache_qos_iops_burst_seconds

| | |
|---|---|
| Type | Secs · default `1` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds) |

**What it does:** the desired burst duration in seconds of immutable object cache IO operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
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
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_iops_limit

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_iops_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_limit) |

**What it does:** the desired immutable object cache IO operations limit per second

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
ceph -s
```

---

### immutable_object_cache_qos_schedule_tick_min

| | |
|---|---|
| Type | Millisecs · default `50` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_qos_schedule_tick_min](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_schedule_tick_min) |

**What it does:** minimum schedule tick for immutable object cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_schedule_tick_min 50
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
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
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
ceph -s
```

---

### immutable_object_cache_sock

| | |
|---|---|
| Type | Str · default `/var/run/ceph/immutable_object_cache_sock` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_sock](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_sock) |

**What it does:** immutable object cache domain socket

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_sock "/var/run/ceph/immutable_object_cache_sock"
ceph config get immutable_object_cache immutable_object_cache_sock
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/run/ceph/immutable_object_cache_sock`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_sock
ceph -s
```

---

### immutable_object_cache_watermark

| | |
|---|---|
| Type | Float · default `0.9` · **Advanced** |
| Table | [immutable.md#SP_immutable_object_cache_watermark](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_watermark) |

**What it does:** immutable object cache water mark

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set immutable_object_cache immutable_object_cache_watermark 0.9
ceph config get immutable_object_cache immutable_object_cache_watermark
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.9`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get immutable_object_cache immutable_object_cache_watermark
ceph -s
```

---


[← Overview](../OVERVIEW.md)
