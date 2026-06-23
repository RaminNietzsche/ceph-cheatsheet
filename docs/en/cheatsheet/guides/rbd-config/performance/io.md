# Io

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_io_scheduler](#rbd_io_scheduler) | `simple` | Advanced | Performance |
| [rbd_io_scheduler_simple_max_delay](#rbd_io_scheduler_simple_max_delay) | `0` | Advanced | Performance |

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

### rbd_io_scheduler

| | |
|---|---|
| Type | Str · enum: ["none", "simple"] · default `simple` · **Advanced** |
| Table | [rbd.md#SP_rbd_io_scheduler](../../../config/rbd/rbd.md#SP_rbd_io_scheduler) |

**What it does:** RBD IO scheduler

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_io_scheduler simple
ceph config get client rbd_io_scheduler
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `simple`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_io_scheduler
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_io_scheduler_simple_max_delay

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_io_scheduler_simple_max_delay](../../../config/rbd/rbd.md#SP_rbd_io_scheduler_simple_max_delay) |

**What it does:** maximum io delay (in milliseconds) for simple io scheduler (if set to 0 dalay is calculated based on latency stats)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_io_scheduler_simple_max_delay 64
ceph config get client rbd_io_scheduler_simple_max_delay
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
ceph config get client rbd_io_scheduler_simple_max_delay
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
