# Blocklist

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_blocklist_expire_seconds](#rbd_blocklist_expire_seconds) | `0` | Advanced | Performance |
| [rbd_blocklist_on_break_lock](#rbd_blocklist_on_break_lock) | `True` | Advanced | Performance |

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

### rbd_blocklist_expire_seconds

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_blocklist_expire_seconds](../../../config/rbd/rbd.md#SP_rbd_blocklist_expire_seconds) |

**What it does:** number of seconds to blocklist - set to 0 for OSD default

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_blocklist_expire_seconds 64
ceph config get client rbd_blocklist_expire_seconds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_blocklist_expire_seconds
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_blocklist_on_break_lock

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_blocklist_on_break_lock](../../../config/rbd/rbd.md#SP_rbd_blocklist_on_break_lock) |

**What it does:** whether to blocklist clients whose lock was broken

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_blocklist_on_break_lock false
ceph config get client rbd_blocklist_on_break_lock
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_blocklist_on_break_lock
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
