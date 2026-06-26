# Defaults

RBD config deep dive — 10 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_default_clone_format](#rbd_default_clone_format) | `auto` | Advanced | Performance |
| [rbd_default_data_pool](#rbd_default_data_pool) | `(empty)` | Advanced | Performance |
| [rbd_default_features](#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Advanced | Performance |
| [rbd_default_format](#rbd_default_format) | `2` | Advanced | Performance |
| [rbd_default_map_options](#rbd_default_map_options) | `(empty)` | Advanced | Performance |
| [rbd_default_order](#rbd_default_order) | `22` | Advanced | Performance |
| [rbd_default_pool](#rbd_default_pool) | `rbd` | Advanced | Performance |
| [rbd_default_snapshot_quiesce_mode](#rbd_default_snapshot_quiesce_mode) | `required` | Advanced | Performance |
| [rbd_default_stripe_count](#rbd_default_stripe_count) | `0` | Advanced | Performance |
| [rbd_default_stripe_unit](#rbd_default_stripe_unit) | `0` | Advanced | Performance |

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

### rbd_default_clone_format

| | |
|---|---|
| Type | Str · enum: ["1", "2", "auto"] · default `auto` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_clone_format](../../../config/rbd/rbd.md#SP_rbd_default_clone_format) |

**What it does:** default internal format for handling clones This sets the internal format for tracking cloned images. The value of ``1`` requires attaching to protected snapshots that cannot be removed until the clone is removed or flattened. The value of ``2`` will allow clones to be attached to any snapshot and permits removing in-use parent snapshots but requires Mimic or later clients. The default value of ``auto`` will use the v2 format if the cluster is configured to require Mimic or later clients.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_clone_format auto
ceph config get client rbd_default_clone_format
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `auto`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_clone_format
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_data_pool

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_data_pool](../../../config/rbd/rbd.md#SP_rbd_default_data_pool) |

**What it does:** default pool for storing data blocks for new images

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_data_pool "example"
ceph config get client rbd_default_data_pool
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_data_pool
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_features

| | |
|---|---|
| Type | Str · default `layering,exclusive-lock,object-map,fast-diff,deep-flatten` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_features](../../../config/rbd/rbd.md#SP_rbd_default_features) |

**What it does:** default v2 image features for new images RBD features are only applicable for v2 images. This setting accepts either an integer bitmask value or comma-delimited string of RBD feature names. This setting is always internally stored as an integer bitmask value. The mapping between feature bitmask value and feature name is as follows: +1 -> layering, +2 -> striping, +4 -> exclusive-lock, +8 -> object-map, +16 -> fast-diff, +32 -> deep-flatten, +64 -> journaling, +128 -> data-pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_features "layering,exclusive-lock,object-map,fast-diff,deep-flatten"
ceph config get client rbd_default_features
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `layering,exclusive-lock,object-map,fast-diff,deep-flatten`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_features
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_format

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_format](../../../config/rbd/rbd.md#SP_rbd_default_format) |

**What it does:** default image format for new images

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_format 2
ceph config get client rbd_default_format
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_format
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_map_options

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_map_options](../../../config/rbd/rbd.md#SP_rbd_default_map_options) |

**What it does:** default krbd map options

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_map_options "example"
ceph config get client rbd_default_map_options
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_map_options
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_order

| | |
|---|---|
| Type | Uint · default `22` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_order](../../../config/rbd/rbd.md#SP_rbd_default_order) |

**What it does:** default order (data block object size) for new images This configures the default object size for new images. The value is used as a power of two, meaning ``default_object_size = 2 ^ rbd_default_order``. Configure a value between 12 and 25 (inclusive), translating to 4KiB lower and 32MiB upper limit.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_order 22
ceph config get client rbd_default_order
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `22`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_order
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_pool

| | |
|---|---|
| Type | Str · default `rbd` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_pool](../../../config/rbd/rbd.md#SP_rbd_default_pool) |

**What it does:** default pool for storing new images

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_pool rbd
ceph config get client rbd_default_pool
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `rbd`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_pool
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_snapshot_quiesce_mode

| | |
|---|---|
| Type | Str · enum: ["required", "ignore-error", "skip"] · default `required` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_snapshot_quiesce_mode](../../../config/rbd/rbd.md#SP_rbd_default_snapshot_quiesce_mode) |

**What it does:** default snapshot quiesce mode

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_snapshot_quiesce_mode required
ceph config get client rbd_default_snapshot_quiesce_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `required`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_snapshot_quiesce_mode
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_stripe_count

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_stripe_count](../../../config/rbd/rbd.md#SP_rbd_default_stripe_count) |

**What it does:** default stripe count for new images

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_stripe_count 64
ceph config get client rbd_default_stripe_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_stripe_count
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_default_stripe_unit

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_default_stripe_unit](../../../config/rbd/rbd.md#SP_rbd_default_stripe_unit) |

**What it does:** default stripe width for new images

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_default_stripe_unit 64
ceph config get client rbd_default_stripe_unit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_default_stripe_unit
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
