# Crash

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [crash_dir](#crash_dir) | `/var/lib/ceph/crash` | Advanced | Capacity |

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

### crash_dir

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/crash` · **Advanced** · **STARTUP** (restart required) |
| Table | [crash.md#SP_crash_dir](../../../config/global/crash.md#SP_crash_dir) |

**What it does:** Directory where crash reports are archived

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global crash_dir "/var/lib/ceph/crash"
ceph config get global crash_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/lib/ceph/crash`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global crash_dir
ceph -s
```

---


[← Overview](../OVERVIEW.md)
