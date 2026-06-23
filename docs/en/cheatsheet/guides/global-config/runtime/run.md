# Run

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [run_dir](#run_dir) | `/var/run/ceph` | Advanced | Capacity |

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

### run_dir

| | |
|---|---|
| Type | Str · default `/var/run/ceph` · **Advanced** · **STARTUP** (restart required) |
| Table | [run.md#SP_run_dir](../../../config/global/run.md#SP_run_dir) |

**What it does:** Path for the 'run' directory for storing pid and socket files

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global run_dir "/var/run/ceph"
ceph config get global run_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/run/ceph`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global run_dir
ceph -s
```

---


[← Overview](../OVERVIEW.md)
