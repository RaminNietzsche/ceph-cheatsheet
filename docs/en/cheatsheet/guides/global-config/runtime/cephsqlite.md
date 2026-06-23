# Cephsqlite

Global config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [cephsqlite_blocklist_dead_locker](#cephsqlite_blocklist_dead_locker) | `True` | Advanced | Performance |
| [cephsqlite_lock_renewal_interval](#cephsqlite_lock_renewal_interval) | `2000` | Advanced | Performance |
| [cephsqlite_lock_renewal_timeout](#cephsqlite_lock_renewal_timeout) | `30000` | Advanced | Performance |

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

### cephsqlite_blocklist_dead_locker

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [cephsqlite.md#SP_cephsqlite_blocklist_dead_locker](../../../config/global/cephsqlite.md#SP_cephsqlite_blocklist_dead_locker) |

**What it does:** Blocklist the last dead owner of the database lock

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global cephsqlite_blocklist_dead_locker false
ceph config get global cephsqlite_blocklist_dead_locker
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephsqlite_blocklist_dead_locker
ceph -s
```

---

### cephsqlite_lock_renewal_interval

| | |
|---|---|
| Type | Millisecs · default `2000` · **Advanced** |
| Table | [cephsqlite.md#SP_cephsqlite_lock_renewal_interval](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_interval) |

**What it does:** Number of milliseconds before a cephsqlite lock is renewed

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global cephsqlite_lock_renewal_interval 2000
ceph config get global cephsqlite_lock_renewal_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `100`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephsqlite_lock_renewal_interval
ceph -s
```

---

### cephsqlite_lock_renewal_timeout

| | |
|---|---|
| Type | Millisecs · default `30000` · **Advanced** |
| Table | [cephsqlite.md#SP_cephsqlite_lock_renewal_timeout](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_timeout) |

**What it does:** Number of milliseconds before a libcephsqlite transaction lock times out

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global cephsqlite_lock_renewal_timeout 30000
ceph config get global cephsqlite_lock_renewal_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `100`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global cephsqlite_lock_renewal_timeout
ceph -s
```

---


[← Overview](../OVERVIEW.md)
