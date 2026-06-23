# Cache

RBD config deep dive — 8 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_cache_block_writes_upfront](#rbd_cache_block_writes_upfront) | `False` | Advanced | Performance |
| [rbd_cache_max_dirty](#rbd_cache_max_dirty) | `24_M` | Advanced | Performance |
| [rbd_cache_max_dirty_age](#rbd_cache_max_dirty_age) | `1` | Advanced | Performance |
| [rbd_cache_max_dirty_object](#rbd_cache_max_dirty_object) | `0` | Advanced | Performance |
| [rbd_cache_policy](#rbd_cache_policy) | `writearound` | Advanced | Performance |
| [rbd_cache_size](#rbd_cache_size) | `32_M` | Advanced | Performance |
| [rbd_cache_target_dirty](#rbd_cache_target_dirty) | `16_M` | Advanced | Performance |
| [rbd_cache_writethrough_until_flush](#rbd_cache_writethrough_until_flush) | `True` | Advanced | Performance |

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

### rbd_cache_block_writes_upfront

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_block_writes_upfront](../../../config/rbd/rbd.md#SP_rbd_cache_block_writes_upfront) |

**What it does:** whether to block writes to the cache before the aio_write call completes

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client rbd_cache_block_writes_upfront true
ceph config get client rbd_cache_block_writes_upfront
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_block_writes_upfront
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_max_dirty

| | |
|---|---|
| Type | Size · default `24_M` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_max_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty) |

**What it does:** dirty limit in bytes - set to 0 for write-through caching

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_cache_max_dirty 24_M
ceph config get client rbd_cache_max_dirty
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `24_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_max_dirty
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_max_dirty_age

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_max_dirty_age](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_age) |

**What it does:** seconds in cache before writeback starts

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_cache_max_dirty_age 1
ceph config get client rbd_cache_max_dirty_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_max_dirty_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_max_dirty_object

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_max_dirty_object](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_object) |

**What it does:** dirty limit for objects - set to 0 for auto calculate from rbd_cache_size

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_cache_max_dirty_object 64
ceph config get client rbd_cache_max_dirty_object
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_max_dirty_object
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_policy

| | |
|---|---|
| Type | Str · enum: ["writethrough", "writeback", "writearound"] · default `writearound` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_policy](../../../config/rbd/rbd.md#SP_rbd_cache_policy) |

**What it does:** cache policy for handling writes.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_cache_policy writearound
ceph config get client rbd_cache_policy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `writearound`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_policy
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_size

| | |
|---|---|
| Type | Size · default `32_M` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_size](../../../config/rbd/rbd.md#SP_rbd_cache_size) |

**What it does:** cache size in bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_cache_size 32_M
ceph config get client rbd_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_size
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_target_dirty

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_target_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_target_dirty) |

**What it does:** target dirty limit in bytes

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_cache_target_dirty 16_M
ceph config get client rbd_cache_target_dirty
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_target_dirty
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_cache_writethrough_until_flush

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_cache_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_cache_writethrough_until_flush) |

**What it does:** whether to make writeback caching writethrough until flush is called, to be sure the user of librbd will send flushes so that writeback is safe

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_cache_writethrough_until_flush false
ceph config get client rbd_cache_writethrough_until_flush
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_cache_writethrough_until_flush
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
