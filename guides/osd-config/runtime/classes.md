# Object classes

OSD config deep dive — 5 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_class_default_list](#osd_class_default_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Advanced | Performance |
| [osd_class_dir](#osd_class_dir) | `0/rados-classes` | Advanced | Capacity |
| [osd_class_load_list](#osd_class_load_list) | `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` | Advanced | Performance |
| [osd_class_update_on_start](#osd_class_update_on_start) | `True` | Advanced | Performance |
| [osd_open_classes_on_start](#osd_open_classes_on_start) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_class_default_list

| | |
|---|---|
| Type | Str · default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` · **Advanced** |
| Table | [osd.md#SP_osd_class_default_list](../../../config/osd/osd.md#SP_osd_class_default_list) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_class_default_list "cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set"
ceph config get osd osd_class_default_list
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_class_default_list
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_class_dir

| | |
|---|---|
| Type | Str · default `0/rados-classes` · **Advanced** |
| Table | [osd.md#SP_osd_class_dir](../../../config/osd/osd.md#SP_osd_class_dir) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_class_dir "0/rados-classes"
ceph config get osd osd_class_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `0/rados-classes`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_class_dir
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_class_load_list

| | |
|---|---|
| Type | Str · default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set` · **Advanced** |
| Table | [osd.md#SP_osd_class_load_list](../../../config/osd/osd.md#SP_osd_class_load_list) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_class_load_list "cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set"
ceph config get osd osd_class_load_list
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cephfs hello journal lock log numops otp rbd refcount rgw rgw_gc timeindex user version cas cmpomap queue 2pc_queue fifo sem_set`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_class_load_list
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_class_update_on_start

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_class_update_on_start](../../../config/osd/osd.md#SP_osd_class_update_on_start) |

**What it does:** set OSD device class on startup

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_class_update_on_start false
ceph config get osd osd_class_update_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_class_update_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_open_classes_on_start

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_open_classes_on_start](../../../config/osd/osd.md#SP_osd_open_classes_on_start) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_open_classes_on_start false
ceph config get osd osd_open_classes_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_open_classes_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
