# Op

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_op_thread_timeout](#rbd_op_thread_timeout) | `60` | Advanced | Performance |
| [rbd_op_threads](#rbd_op_threads) | `1` | Advanced | Performance |

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

### rbd_op_thread_timeout

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** |
| Table | [rbd.md#SP_rbd_op_thread_timeout](../../../config/rbd/rbd.md#SP_rbd_op_thread_timeout) |

**What it does:** time in seconds for detecting a hung thread

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_op_thread_timeout 60
ceph config get client rbd_op_thread_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_op_thread_timeout
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_op_threads

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_op_threads](../../../config/rbd/rbd.md#SP_rbd_op_threads) |

**What it does:** number of threads to utilize for internal processing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_op_threads 1
ceph config get client rbd_op_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_op_threads
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
