# Persistent

RBD config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_persistent_cache_mode](#rbd_persistent_cache_mode) | `disabled` | Advanced | Performance |
| [rbd_persistent_cache_path](#rbd_persistent_cache_path) | `/tmp` | Advanced | Capacity |
| [rbd_persistent_cache_size](#rbd_persistent_cache_size) | `1_G` | Advanced | Performance |

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

### rbd_persistent_cache_mode

| | |
|---|---|
| Type | Str · enum: ["disabled", "rwl", "ssd"] · default `disabled` · **Advanced** |
| Table | [rbd.md#SP_rbd_persistent_cache_mode](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_mode) |

**What it does:** enable persistent write back cache for this volume

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_persistent_cache_mode disabled
ceph config get client rbd_persistent_cache_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `disabled`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_persistent_cache_mode
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_persistent_cache_path

| | |
|---|---|
| Type | Str · default `/tmp` · **Advanced** |
| Table | [rbd.md#SP_rbd_persistent_cache_path](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_path) |

**What it does:** location of the persistent write back cache in a DAX-enabled filesystem on persistent memory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_persistent_cache_path "/tmp"
ceph config get client rbd_persistent_cache_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/tmp`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_persistent_cache_path
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_persistent_cache_size

| | |
|---|---|
| Type | Uint · default `1_G` · **Advanced** |
| Table | [rbd.md#SP_rbd_persistent_cache_size](../../../config/rbd/rbd.md#SP_rbd_persistent_cache_size) |

**What it does:** size of the persistent write back cache for this volume

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_persistent_cache_size 1_G
ceph config get client rbd_persistent_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1_G`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_persistent_cache_size
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
