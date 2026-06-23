# Journal

RBD config deep dive — 11 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_journal_commit_age](#rbd_journal_commit_age) | `5` | Advanced | Performance |
| [rbd_journal_max_concurrent_object_sets](#rbd_journal_max_concurrent_object_sets) | `0` | Advanced | Performance |
| [rbd_journal_max_payload_bytes](#rbd_journal_max_payload_bytes) | `16_K` | Advanced | Performance |
| [rbd_journal_object_flush_age](#rbd_journal_object_flush_age) | `0` | Advanced | Performance |
| [rbd_journal_object_flush_bytes](#rbd_journal_object_flush_bytes) | `1_M` | Advanced | Performance |
| [rbd_journal_object_flush_interval](#rbd_journal_object_flush_interval) | `0` | Advanced | Performance |
| [rbd_journal_object_max_in_flight_appends](#rbd_journal_object_max_in_flight_appends) | `0` | Advanced | Performance |
| [rbd_journal_object_writethrough_until_flush](#rbd_journal_object_writethrough_until_flush) | `True` | Advanced | Performance |
| [rbd_journal_order](#rbd_journal_order) | `24` | Advanced | Performance |
| [rbd_journal_pool](#rbd_journal_pool) | `(empty)` | Advanced | Performance |
| [rbd_journal_splay_width](#rbd_journal_splay_width) | `4` | Advanced | Performance |

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

### rbd_journal_commit_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_commit_age](../../../config/rbd/rbd.md#SP_rbd_journal_commit_age) |

**What it does:** commit time interval, seconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_commit_age 5
ceph config get client rbd_journal_commit_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_commit_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_max_concurrent_object_sets

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_max_concurrent_object_sets](../../../config/rbd/rbd.md#SP_rbd_journal_max_concurrent_object_sets) |

**What it does:** maximum number of object sets a journal client can be behind before it is automatically unregistered

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_journal_max_concurrent_object_sets 64
ceph config get client rbd_journal_max_concurrent_object_sets
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_max_concurrent_object_sets
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_max_payload_bytes

| | |
|---|---|
| Type | Size · default `16_K` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_max_payload_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_max_payload_bytes) |

**What it does:** maximum journal payload size before splitting

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_journal_max_payload_bytes 16_K
ceph config get client rbd_journal_max_payload_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_max_payload_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_object_flush_age

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_object_flush_age](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_age) |

**What it does:** maximum age (in seconds) for pending commits

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_object_flush_age 0
ceph config get client rbd_journal_object_flush_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_object_flush_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_object_flush_bytes

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_object_flush_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_bytes) |

**What it does:** maximum number of pending bytes per journal object

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_object_flush_bytes 1_M
ceph config get client rbd_journal_object_flush_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_object_flush_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_object_flush_interval

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_object_flush_interval](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_interval) |

**What it does:** maximum number of pending commits per journal object

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_journal_object_flush_interval 64
ceph config get client rbd_journal_object_flush_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_object_flush_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_object_max_in_flight_appends

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_object_max_in_flight_appends](../../../config/rbd/rbd.md#SP_rbd_journal_object_max_in_flight_appends) |

**What it does:** maximum number of in-flight appends per journal object

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_journal_object_max_in_flight_appends 64
ceph config get client rbd_journal_object_max_in_flight_appends
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_object_max_in_flight_appends
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_object_writethrough_until_flush

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_object_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_journal_object_writethrough_until_flush) |

**What it does:** when enabled, the rbd_journal_object_flush* configuration options are ignored until the first flush so that batched journal IO is known to be safe for consistency

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_journal_object_writethrough_until_flush false
ceph config get client rbd_journal_object_writethrough_until_flush
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_object_writethrough_until_flush
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_order

| | |
|---|---|
| Type | Uint · default `24` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_order](../../../config/rbd/rbd.md#SP_rbd_journal_order) |

**What it does:** default order (object size) for journal data objects

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_order 24
ceph config get client rbd_journal_order
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `24`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `12`, max `26`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_order
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_pool

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_pool](../../../config/rbd/rbd.md#SP_rbd_journal_pool) |

**What it does:** pool for journal objects

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_pool "example"
ceph config get client rbd_journal_pool
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_pool
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_journal_splay_width

| | |
|---|---|
| Type | Uint · default `4` · **Advanced** |
| Table | [rbd.md#SP_rbd_journal_splay_width](../../../config/rbd/rbd.md#SP_rbd_journal_splay_width) |

**What it does:** number of active journal objects

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_journal_splay_width 4
ceph config get client rbd_journal_splay_width
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_journal_splay_width
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
