# Threadpool

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [threadpool_default_timeout](#threadpool_default_timeout) | `1_min` | Advanced | Performance |
| [threadpool_empty_queue_max_wait](#threadpool_empty_queue_max_wait) | `2` | Advanced | Performance |

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

### threadpool_default_timeout

| | |
|---|---|
| Type | Int · default `1_min` · **Advanced** |
| Table | [threadpool.md#SP_threadpool_default_timeout](../../../config/global/threadpool.md#SP_threadpool_default_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global threadpool_default_timeout 1_min
ceph config get global threadpool_default_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global threadpool_default_timeout
ceph -s
```

---

### threadpool_empty_queue_max_wait

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [threadpool.md#SP_threadpool_empty_queue_max_wait](../../../config/global/threadpool.md#SP_threadpool_empty_queue_max_wait) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global threadpool_empty_queue_max_wait 2
ceph config get global threadpool_empty_queue_max_wait
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global threadpool_empty_queue_max_wait
ceph -s
```

---


[← Overview](../OVERVIEW.md)
