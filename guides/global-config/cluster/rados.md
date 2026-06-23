# Rados

Global config deep dive — 5 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rados_mon_op_timeout](#rados_mon_op_timeout) | `0` | Advanced | Performance |
| [rados_osd_op_timeout](#rados_osd_op_timeout) | `0` | Advanced | Performance |
| [rados_replica_read_policy](#rados_replica_read_policy) | `default` | Advanced | Performance |
| [rados_replica_read_policy_on_objclass](#rados_replica_read_policy_on_objclass) | `False` | Advanced | Performance |
| [rados_tracing](#rados_tracing) | `False` | Advanced | Performance |

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

### rados_mon_op_timeout

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [rados.md#SP_rados_mon_op_timeout](../../../config/global/rados.md#SP_rados_mon_op_timeout) |

**What it does:** Timeout for operations handled by Monitors, for example statfs(). (0 is unlimited)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global rados_mon_op_timeout 0
ceph config get global rados_mon_op_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rados_mon_op_timeout
ceph -s
```

---

### rados_osd_op_timeout

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [rados.md#SP_rados_osd_op_timeout](../../../config/global/rados.md#SP_rados_osd_op_timeout) |

**What it does:** Timeout for operations handled by OSDs, for example write(). (0 is unlimited)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global rados_osd_op_timeout 0
ceph config get global rados_osd_op_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rados_osd_op_timeout
ceph -s
```

---

### rados_replica_read_policy

| | |
|---|---|
| Type | Str · enum: ["default", "balance", "localize"] · default `default` · **Advanced** |
| Table | [rados.md#SP_rados_replica_read_policy](../../../config/global/rados.md#SP_rados_replica_read_policy) |

**What it does:** Read policy for sending read requests to OSD

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rados_replica_read_policy default
ceph config get global rados_replica_read_policy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rados_replica_read_policy
ceph -s
```

---

### rados_replica_read_policy_on_objclass

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rados.md#SP_rados_replica_read_policy_on_objclass](../../../config/global/rados.md#SP_rados_replica_read_policy_on_objclass) |

**What it does:** Enable read policy for sending read requests to OSD on objclass ops

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rados_replica_read_policy_on_objclass true
ceph config get global rados_replica_read_policy_on_objclass
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rados_replica_read_policy_on_objclass
ceph -s
```

---

### rados_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rados.md#SP_rados_tracing](../../../config/global/rados.md#SP_rados_tracing) |

**What it does:** Should LTTng-UST tracepoints be enabled?

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rados_tracing true
ceph config get global rados_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rados_tracing
ceph -s
```

---


[← Overview](../OVERVIEW.md)
