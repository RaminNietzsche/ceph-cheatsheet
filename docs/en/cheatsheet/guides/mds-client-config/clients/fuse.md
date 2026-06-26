# FUSE client

MDS client config deep dive — 15 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [fuse_allow_other](#fuse_allow_other) | `True` | Advanced | Policy |
| [fuse_atomic_o_trunc](#fuse_atomic_o_trunc) | `True` | Advanced | Performance |
| [fuse_big_writes](#fuse_big_writes) | `True` | Advanced | Performance |
| [fuse_debug](#fuse_debug) | `False` | Advanced | Performance |
| [fuse_default_permissions](#fuse_default_permissions) | `False` | Advanced | Performance |
| [fuse_disable_pagecache](#fuse_disable_pagecache) | `False` | Advanced | Policy |
| [fuse_max_write](#fuse_max_write) | `0` | Advanced | Performance |
| [fuse_multithreaded](#fuse_multithreaded) | `True` | Advanced | Performance |
| [fuse_require_active_mds](#fuse_require_active_mds) | `True` | Advanced | Performance |
| [fuse_set_user_groups](#fuse_set_user_groups) | `True` | Advanced | Performance |
| [fuse_splice_move](#fuse_splice_move) | `True` | Advanced | Performance |
| [fuse_splice_read](#fuse_splice_read) | `True` | Advanced | Performance |
| [fuse_splice_write](#fuse_splice_write) | `True` | Advanced | Performance |
| [fuse_syncfs_on_mksnap](#fuse_syncfs_on_mksnap) | `True` | Advanced | Performance |
| [fuse_use_invalidate_cb](#fuse_use_invalidate_cb) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### fuse_allow_other

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_allow_other](../../../config/mds-client/fuse.md#SP_fuse_allow_other) |

**What it does:** pass allow_other to FUSE on mount

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_allow_other false
ceph config get client fuse_allow_other
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_allow_other
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_atomic_o_trunc

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_atomic_o_trunc](../../../config/mds-client/fuse.md#SP_fuse_atomic_o_trunc) |

**What it does:** pass atomic_o_trunc flag to FUSE on mount

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_atomic_o_trunc false
ceph config get client fuse_atomic_o_trunc
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_atomic_o_trunc
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_big_writes

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_big_writes](../../../config/mds-client/fuse.md#SP_fuse_big_writes) |

**What it does:** big_writes is deprecated in libfuse 3.0.0

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_big_writes false
ceph config get client fuse_big_writes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_big_writes
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_debug

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [fuse.md#SP_fuse_debug](../../../config/mds-client/fuse.md#SP_fuse_debug) |

**What it does:** enable debugging for the libfuse

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client fuse_debug true
ceph config get client fuse_debug
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_debug
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_default_permissions

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [fuse.md#SP_fuse_default_permissions](../../../config/mds-client/fuse.md#SP_fuse_default_permissions) |

**What it does:** pass default_permisions to FUSE on mount

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client fuse_default_permissions true
ceph config get client fuse_default_permissions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_default_permissions
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_disable_pagecache

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [fuse.md#SP_fuse_disable_pagecache](../../../config/mds-client/fuse.md#SP_fuse_disable_pagecache) |

**What it does:** disable page caching in the kernel for this FUSE mount

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set client fuse_disable_pagecache true
ceph config get client fuse_disable_pagecache
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_disable_pagecache
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_max_write

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [fuse.md#SP_fuse_max_write](../../../config/mds-client/fuse.md#SP_fuse_max_write) |

**What it does:** set the maximum number of bytes in a single write operation Set the maximum number of bytes in a single write operation that may pass atomically through FUSE. The FUSE default is 128kB and may be indicated by setting this option to 0.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client fuse_max_write 64
ceph config get client fuse_max_write
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_max_write
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_multithreaded

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_multithreaded](../../../config/mds-client/fuse.md#SP_fuse_multithreaded) |

**What it does:** allow parallel processing through FUSE library

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_multithreaded false
ceph config get client fuse_multithreaded
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_multithreaded
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_require_active_mds

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_require_active_mds](../../../config/mds-client/fuse.md#SP_fuse_require_active_mds) |

**What it does:** require active MDSs in the file system when mounting

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_require_active_mds false
ceph config get client fuse_require_active_mds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_require_active_mds
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_set_user_groups

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_set_user_groups](../../../config/mds-client/fuse.md#SP_fuse_set_user_groups) |

**What it does:** check for ceph-fuse to consider supplementary groups for permissions

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_set_user_groups false
ceph config get client fuse_set_user_groups
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_set_user_groups
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_splice_move

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_splice_move](../../../config/mds-client/fuse.md#SP_fuse_splice_move) |

**What it does:** enable splice move to reduce the memory copies

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_splice_move false
ceph config get client fuse_splice_move
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_splice_move
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_splice_read

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_splice_read](../../../config/mds-client/fuse.md#SP_fuse_splice_read) |

**What it does:** enable splice read to reduce the memory copies

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_splice_read false
ceph config get client fuse_splice_read
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_splice_read
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_splice_write

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_splice_write](../../../config/mds-client/fuse.md#SP_fuse_splice_write) |

**What it does:** enable splice write to reduce the memory copies

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_splice_write false
ceph config get client fuse_splice_write
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_splice_write
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_syncfs_on_mksnap

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_syncfs_on_mksnap](../../../config/mds-client/fuse.md#SP_fuse_syncfs_on_mksnap) |

**What it does:** synchronize all local metadata/file changes after snapshot

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_syncfs_on_mksnap false
ceph config get client fuse_syncfs_on_mksnap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_syncfs_on_mksnap
ceph -s
# client options: set on client section or ceph.conf
```

---

### fuse_use_invalidate_cb

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [fuse.md#SP_fuse_use_invalidate_cb](../../../config/mds-client/fuse.md#SP_fuse_use_invalidate_cb) |

**What it does:** use fuse 2.8+ invalidate callback to keep page cache consistent

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client fuse_use_invalidate_cb false
ceph config get client fuse_use_invalidate_cb
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client fuse_use_invalidate_cb
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
