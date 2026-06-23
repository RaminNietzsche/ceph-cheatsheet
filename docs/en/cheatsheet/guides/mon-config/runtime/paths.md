# Paths & storage

MON config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_data](#mon_data) | `/var/lib/ceph/mon/$cluster-$id` | Advanced | Performance |
| [mon_data_avail_crit](#mon_data_avail_crit) | `5` | Advanced | Performance |
| [mon_data_avail_warn](#mon_data_avail_warn) | `30` | Advanced | Performance |
| [mon_data_size_warn](#mon_data_size_warn) | `15_G` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_data

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/mon/$cluster-$id` · **Advanced** |
| Table | [mon.md#SP_mon_data](../../../config/mon/mon.md#SP_mon_data) |

**What it does:** path to mon database

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_data "/var/lib/ceph/mon/$cluster-$id"
ceph config get mon mon_data
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/mon/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_data
ceph -s
ceph mon stat
```

---

### mon_data_avail_crit

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_data_avail_crit](../../../config/mon/mon.md#SP_mon_data_avail_crit) |

**What it does:** issue MON_DISK_CRIT health error when mon available space below this percentage

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_data_avail_crit 5
ceph config get mon mon_data_avail_crit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_data_avail_crit
ceph -s
ceph mon stat
```

---

### mon_data_avail_warn

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [mon.md#SP_mon_data_avail_warn](../../../config/mon/mon.md#SP_mon_data_avail_warn) |

**What it does:** issue MON_DISK_LOW health warning when mon available space below this percentage

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_data_avail_warn 30
ceph config get mon mon_data_avail_warn
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_data_avail_warn
ceph -s
ceph mon stat
```

---

### mon_data_size_warn

| | |
|---|---|
| Type | Size · default `15_G` · **Advanced** |
| Table | [mon.md#SP_mon_data_size_warn](../../../config/mon/mon.md#SP_mon_data_size_warn) |

**What it does:** issue MON_DISK_BIG health warning when mon database is above this size

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_data_size_warn 15_G
ceph config get mon mon_data_size_warn
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_data_size_warn
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
