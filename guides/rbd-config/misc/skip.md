# Skip

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_skip_partial_discard](#rbd_skip_partial_discard) | `True` | Advanced | Performance |

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

### rbd_skip_partial_discard

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_skip_partial_discard](../../../config/rbd/rbd.md#SP_rbd_skip_partial_discard) |

**What it does:** skip discard (zero) of unaligned extents within an object

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_skip_partial_discard false
ceph config get client rbd_skip_partial_discard
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_skip_partial_discard
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
