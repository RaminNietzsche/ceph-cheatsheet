# Objectstore

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [objectstore_blackhole](#objectstore_blackhole) | `False` | Advanced | Performance |
| [objectstore_debug_throw_on_failed_txc](#objectstore_debug_throw_on_failed_txc) | `False` | Dev | Dev |

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

### objectstore_blackhole

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [objectstore.md#SP_objectstore_blackhole](../../../config/global/objectstore.md#SP_objectstore_blackhole) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global objectstore_blackhole true
ceph config get global objectstore_blackhole
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global objectstore_blackhole
ceph -s
```

---

### objectstore_debug_throw_on_failed_txc

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [objectstore.md#SP_objectstore_debug_throw_on_failed_txc](../../../config/global/objectstore.md#SP_objectstore_debug_throw_on_failed_txc) |

**What it does:** Enables exception throwing instead of process abort on transaction submission error.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global objectstore_debug_throw_on_failed_txc true
ceph config get global objectstore_debug_throw_on_failed_txc
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
