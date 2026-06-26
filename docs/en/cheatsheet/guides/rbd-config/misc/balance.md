# Balance

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_balance_parent_reads](#rbd_balance_parent_reads) | `False` | Advanced | Performance |
| [rbd_balance_snap_reads](#rbd_balance_snap_reads) | `False` | Advanced | Performance |

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

### rbd_balance_parent_reads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_balance_parent_reads](../../../config/rbd/rbd.md#SP_rbd_balance_parent_reads) |

**What it does:** distribute parent read requests to random OSD

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`rbd_read_from_replica_policy`](../../../config/rbd/rbd.md#SP_rbd_read_from_replica_policy)

**Example:**

```bash
ceph config set client rbd_balance_parent_reads true
ceph config get client rbd_balance_parent_reads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_balance_parent_reads
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_balance_snap_reads

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_balance_snap_reads](../../../config/rbd/rbd.md#SP_rbd_balance_snap_reads) |

**What it does:** distribute snap read requests to random OSD

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`rbd_read_from_replica_policy`](../../../config/rbd/rbd.md#SP_rbd_read_from_replica_policy)

**Example:**

```bash
ceph config set client rbd_balance_snap_reads true
ceph config get client rbd_balance_snap_reads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_balance_snap_reads
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
