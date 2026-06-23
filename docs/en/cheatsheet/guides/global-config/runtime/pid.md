# Pid

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [pid_file](#pid_file) | `(empty)` | Advanced | Capacity |

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

### pid_file

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [pid.md#SP_pid_file](../../../config/global/pid.md#SP_pid_file) |

**What it does:** path to write a pid file (if any)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global pid_file "example"
ceph config get global pid_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `(empty)`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global pid_file
ceph -s
```

---


[← Overview](../OVERVIEW.md)
