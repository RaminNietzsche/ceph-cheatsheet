# Mirroring

RBD config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_mirroring_delete_delay](#rbd_mirroring_delete_delay) | `0` | Advanced | Performance |
| [rbd_mirroring_max_mirroring_snapshots](#rbd_mirroring_max_mirroring_snapshots) | `5` | Advanced | Performance |
| [rbd_mirroring_replay_delay](#rbd_mirroring_replay_delay) | `0` | Advanced | Performance |
| [rbd_mirroring_resync_after_disconnect](#rbd_mirroring_resync_after_disconnect) | `False` | Advanced | Performance |

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

### rbd_mirroring_delete_delay

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirroring_delete_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_delete_delay) |

**What it does:** time-delay in seconds for rbd-mirror delete propagation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirroring_delete_delay 64
ceph config get client rbd_mirroring_delete_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirroring_delete_delay
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirroring_max_mirroring_snapshots

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirroring_max_mirroring_snapshots](../../../config/rbd/rbd.md#SP_rbd_mirroring_max_mirroring_snapshots) |

**What it does:** mirroring snapshots limit

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_mirroring_max_mirroring_snapshots 5
ceph config get client rbd_mirroring_max_mirroring_snapshots
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `3`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirroring_max_mirroring_snapshots
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirroring_replay_delay

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirroring_replay_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_replay_delay) |

**What it does:** time-delay in seconds for rbd-mirror asynchronous replication

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirroring_replay_delay 64
ceph config get client rbd_mirroring_replay_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirroring_replay_delay
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirroring_resync_after_disconnect

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirroring_resync_after_disconnect](../../../config/rbd/rbd.md#SP_rbd_mirroring_resync_after_disconnect) |

**What it does:** automatically start image resync after mirroring is disconnected due to being laggy

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_mirroring_resync_after_disconnect true
ceph config get client rbd_mirroring_resync_after_disconnect
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirroring_resync_after_disconnect
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
