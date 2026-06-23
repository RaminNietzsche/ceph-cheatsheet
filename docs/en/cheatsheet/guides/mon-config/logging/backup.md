# Monitor backup

MON config deep dive — 7 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_backup_cleanup_interval](#mon_backup_cleanup_interval) | `0` | Advanced | Performance |
| [mon_backup_interval](#mon_backup_interval) | `0` | Advanced | Performance |
| [mon_backup_keep_daily](#mon_backup_keep_daily) | `7` | Advanced | Performance |
| [mon_backup_keep_hourly](#mon_backup_keep_hourly) | `5` | Advanced | Performance |
| [mon_backup_keep_last](#mon_backup_keep_last) | `6` | Advanced | Performance |
| [mon_backup_min_avail](#mon_backup_min_avail) | `10` | Advanced | Performance |
| [mon_backup_path](#mon_backup_path) | `/var/backups/ceph/mon/$cluster-$id` | Advanced | Capacity |

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

### mon_backup_cleanup_interval

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_backup_cleanup_interval](../../../config/mon/mon.md#SP_mon_backup_cleanup_interval) |

**What it does:** Trigger backup cleanup every N seconds (0 disables)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_backup_cleanup_interval 0
ceph config get mon mon_backup_cleanup_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_cleanup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_interval

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_backup_interval](../../../config/mon/mon.md#SP_mon_backup_interval) |

**What it does:** Automatic backups every N seconds (0 disables)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_backup_interval 0
ceph config get mon mon_backup_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_keep_daily

| | |
|---|---|
| Type | Uint · default `7` · **Advanced** |
| Table | [mon.md#SP_mon_backup_keep_daily](../../../config/mon/mon.md#SP_mon_backup_keep_daily) |

**What it does:** Number of daily backups

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_backup_keep_daily 7
ceph config get mon mon_backup_keep_daily
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_keep_daily
ceph -s
ceph mon stat
```

---

### mon_backup_keep_hourly

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_backup_keep_hourly](../../../config/mon/mon.md#SP_mon_backup_keep_hourly) |

**What it does:** Number of hourly backups

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_backup_keep_hourly 5
ceph config get mon mon_backup_keep_hourly
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_keep_hourly
ceph -s
ceph mon stat
```

---

### mon_backup_keep_last

| | |
|---|---|
| Type | Uint · default `6` · **Advanced** |
| Table | [mon.md#SP_mon_backup_keep_last](../../../config/mon/mon.md#SP_mon_backup_keep_last) |

**What it does:** Keep the last N backups

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_backup_keep_last 6
ceph config get mon mon_backup_keep_last
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_keep_last
ceph -s
ceph mon stat
```

---

### mon_backup_min_avail

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_backup_min_avail](../../../config/mon/mon.md#SP_mon_backup_min_avail) |

**What it does:** Only capture backups if at least this percentage of the target filesystem is free

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_backup_min_avail 10
ceph config get mon mon_backup_min_avail
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `100`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_min_avail
ceph -s
ceph mon stat
```

---

### mon_backup_path

| | |
|---|---|
| Type | Str · default `/var/backups/ceph/mon/$cluster-$id` · **Advanced** |
| Table | [mon.md#SP_mon_backup_path](../../../config/mon/mon.md#SP_mon_backup_path) |

**What it does:** Path to Monitor database backups

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_backup_path "/var/backups/ceph/mon/$cluster-$id"
ceph config get mon mon_backup_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/backups/ceph/mon/$cluster-$id`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_backup_path
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
