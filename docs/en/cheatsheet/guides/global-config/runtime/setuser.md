# Setuser

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [setuser](#setuser) | `(empty)` | Advanced | Performance |
| [setuser_match_path](#setuser_match_path) | `(empty)` | Advanced | Capacity |

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

### setuser

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [setuser.md#SP_setuser](../../../config/global/setuser.md#SP_setuser) |

**What it does:** UID or user name to switch to on startup

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global setuser "example"
ceph config get global setuser
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global setuser
ceph -s
```

---

### setuser_match_path

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [setuser.md#SP_setuser_match_path](../../../config/global/setuser.md#SP_setuser_match_path) |

**What it does:** If set, setuser/setgroup is conditional on this path matching ownership

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global setuser_match_path "/var/lib/ceph/example"
ceph config get global setuser_match_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `(empty)`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global setuser_match_path
ceph -s
```

---


[← Overview](../OVERVIEW.md)
