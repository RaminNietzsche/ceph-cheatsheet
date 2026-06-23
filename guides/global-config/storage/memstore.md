# Memstore

Global config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [memstore_debug_omit_block_device_write](#memstore_debug_omit_block_device_write) | `False` | Dev | Dev |
| [memstore_device_bytes](#memstore_device_bytes) | `1_G` | Advanced | Performance |
| [memstore_page_set](#memstore_page_set) | `False` | Advanced | Performance |
| [memstore_page_size](#memstore_page_size) | `64_K` | Advanced | Performance |

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

### memstore_debug_omit_block_device_write

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [memstore.md#SP_memstore_debug_omit_block_device_write](../../../config/global/memstore.md#SP_memstore_debug_omit_block_device_write) |

**What it does:** write metadata only

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global memstore_debug_omit_block_device_write true
ceph config get global memstore_debug_omit_block_device_write
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### memstore_device_bytes

| | |
|---|---|
| Type | Size · default `1_G` · **Advanced** |
| Table | [memstore.md#SP_memstore_device_bytes](../../../config/global/memstore.md#SP_memstore_device_bytes) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global memstore_device_bytes 1_G
ceph config get global memstore_device_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global memstore_device_bytes
ceph -s
```

---

### memstore_page_set

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [memstore.md#SP_memstore_page_set](../../../config/global/memstore.md#SP_memstore_page_set) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global memstore_page_set true
ceph config get global memstore_page_set
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global memstore_page_set
ceph -s
```

---

### memstore_page_size

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [memstore.md#SP_memstore_page_size](../../../config/global/memstore.md#SP_memstore_page_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global memstore_page_size 64_K
ceph config get global memstore_page_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global memstore_page_size
ceph -s
```

---


[← Overview](../OVERVIEW.md)
