# Heartbeat

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [heartbeat_file](#heartbeat_file) | `(empty)` | Advanced | Capacity |
| [heartbeat_inject_failure](#heartbeat_inject_failure) | `0` | Dev | Dev |
| [heartbeat_interval](#heartbeat_interval) | `5` | Advanced | Performance |

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

### heartbeat_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [heartbeat.md#SP_heartbeat_file](../../../config/global/heartbeat.md#SP_heartbeat_file) |

**What it does:** File to touch on successful internal heartbeat If set, this file will be touched every time an internal heartbeat check succeeds.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`heartbeat_interval`](../../../config/global/heartbeat.md#SP_heartbeat_interval)

**Example:**

```bash
ceph config set global heartbeat_file "example"
ceph config get global heartbeat_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `(empty)`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global heartbeat_file
ceph -s
```

---

### heartbeat_inject_failure

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [heartbeat.md#SP_heartbeat_inject_failure](../../../config/global/heartbeat.md#SP_heartbeat_inject_failure) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global heartbeat_inject_failure 64
ceph config get global heartbeat_inject_failure
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### heartbeat_interval

| | |
|---|---|
| Type | Int · default `5` · **Advanced** · **STARTUP** (restart required) |
| Table | [heartbeat.md#SP_heartbeat_interval](../../../config/global/heartbeat.md#SP_heartbeat_interval) |

**What it does:** Frequency of internal heartbeat checks (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global heartbeat_interval 5
ceph config get global heartbeat_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global heartbeat_interval
ceph -s
```

---


[← Overview](../OVERVIEW.md)
