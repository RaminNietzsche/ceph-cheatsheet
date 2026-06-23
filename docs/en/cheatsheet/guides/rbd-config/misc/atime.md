# Atime

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_atime_update_interval](#rbd_atime_update_interval) | `60` | Advanced | Performance |

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

### rbd_atime_update_interval

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** |
| Table | [rbd.md#SP_rbd_atime_update_interval](../../../config/rbd/rbd.md#SP_rbd_atime_update_interval) |

**What it does:** RBD Image access timestamp refresh interval. Set to 0 to disable access timestamp update.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_atime_update_interval 60
ceph config get client rbd_atime_update_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_atime_update_interval
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
