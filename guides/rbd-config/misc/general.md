# General

RBD config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_cache](#rbd_cache) | `True` | Advanced | Performance |
| [rbd_plugins](#rbd_plugins) | `(empty)` | Advanced | Performance |
| [rbd_tracing](#rbd_tracing) | `False` | Advanced | Performance |

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

### rbd_cache

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache](../../../config/rbd/rbd.md#SP_rbd_cache) |

**What it does:** whether to enable caching (writeback unless rbd_cache_max_dirty is 0)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_cache false
ceph config get client rbd_cache
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_plugins

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rbd.md#SP_rbd_plugins](../../../config/rbd/rbd.md#SP_rbd_plugins) |

**What it does:** comma-delimited list of librbd plugins to enable

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_plugins "example"
ceph config get client rbd_plugins
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_plugins
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_tracing

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_tracing](../../../config/rbd/rbd.md#SP_rbd_tracing) |

**What it does:** true if LTTng-UST tracepoints should be enabled

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_tracing true
ceph config get client rbd_tracing
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_tracing
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
