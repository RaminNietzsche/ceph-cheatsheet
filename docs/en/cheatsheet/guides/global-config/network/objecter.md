# Objecter

Global config deep dive — 8 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [objecter_completion_locks_per_session](#objecter_completion_locks_per_session) | `32` | Dev | Dev |
| [objecter_debug_inject_relock_delay](#objecter_debug_inject_relock_delay) | `False` | Dev | Dev |
| [objecter_inflight_op_bytes](#objecter_inflight_op_bytes) | `100_M` | Advanced | Performance |
| [objecter_inflight_ops](#objecter_inflight_ops) | `1_K` | Advanced | Performance |
| [objecter_inject_no_watch_ping](#objecter_inject_no_watch_ping) | `False` | Dev | Dev |
| [objecter_retry_writes_after_first_reply](#objecter_retry_writes_after_first_reply) | `False` | Dev | Dev |
| [objecter_tick_interval](#objecter_tick_interval) | `5` | Dev | Dev |
| [objecter_timeout](#objecter_timeout) | `10` | Advanced | Performance |

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

### objecter_completion_locks_per_session

| | |
|---|---|
| Type | Uint · default `32` · **Dev** |
| Table | [objecter.md#SP_objecter_completion_locks_per_session](../../../config/global/objecter.md#SP_objecter_completion_locks_per_session) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objecter_completion_locks_per_session 32
ceph config get global objecter_completion_locks_per_session
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`32`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### objecter_debug_inject_relock_delay

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [objecter.md#SP_objecter_debug_inject_relock_delay](../../../config/global/objecter.md#SP_objecter_debug_inject_relock_delay) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objecter_debug_inject_relock_delay true
ceph config get global objecter_debug_inject_relock_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### objecter_inflight_op_bytes

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [objecter.md#SP_objecter_inflight_op_bytes](../../../config/global/objecter.md#SP_objecter_inflight_op_bytes) |

**What it does:** Max in-flight data in bytes (both directions)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global objecter_inflight_op_bytes 100_M
ceph config get global objecter_inflight_op_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global objecter_inflight_op_bytes
ceph -s
```

---

### objecter_inflight_ops

| | |
|---|---|
| Type | Uint · default `1_K` · **Advanced** |
| Table | [objecter.md#SP_objecter_inflight_ops](../../../config/global/objecter.md#SP_objecter_inflight_ops) |

**What it does:** Max in-flight operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global objecter_inflight_ops 1_K
ceph config get global objecter_inflight_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global objecter_inflight_ops
ceph -s
```

---

### objecter_inject_no_watch_ping

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [objecter.md#SP_objecter_inject_no_watch_ping](../../../config/global/objecter.md#SP_objecter_inject_no_watch_ping) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objecter_inject_no_watch_ping true
ceph config get global objecter_inject_no_watch_ping
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### objecter_retry_writes_after_first_reply

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [objecter.md#SP_objecter_retry_writes_after_first_reply](../../../config/global/objecter.md#SP_objecter_retry_writes_after_first_reply) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objecter_retry_writes_after_first_reply true
ceph config get global objecter_retry_writes_after_first_reply
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### objecter_tick_interval

| | |
|---|---|
| Type | Float · default `5` · **Dev** |
| Table | [objecter.md#SP_objecter_tick_interval](../../../config/global/objecter.md#SP_objecter_tick_interval) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objecter_tick_interval 5
ceph config get global objecter_tick_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### objecter_timeout

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [objecter.md#SP_objecter_timeout](../../../config/global/objecter.md#SP_objecter_timeout) |

**What it does:** Seconds before in-flight op is considered laggy and we query the Monitors for the latest OSDMap

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global objecter_timeout 10
ceph config get global objecter_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global objecter_timeout
ceph -s
```

---


[← Overview](../OVERVIEW.md)
