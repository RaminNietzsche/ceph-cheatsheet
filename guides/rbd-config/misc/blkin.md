# Blkin

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_blkin_trace_all](#rbd_blkin_trace_all) | `False` | Advanced | Performance |

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

### rbd_blkin_trace_all

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_blkin_trace_all](../../../config/rbd/rbd.md#SP_rbd_blkin_trace_all) |

**What it does:** create a blkin trace for all RBD requests

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_blkin_trace_all true
ceph config get client rbd_blkin_trace_all
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_blkin_trace_all
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
