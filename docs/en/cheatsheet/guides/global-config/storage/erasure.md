# Erasure

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [erasure_code_dir](#erasure_code_dir) | `0/erasure-code` | Advanced | Capacity |

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

### erasure_code_dir

| | |
|---|---|
| Type | Str · default `0/erasure-code` · **Advanced** · **STARTUP** (restart required) |
| Table | [erasure.md#SP_erasure_code_dir](../../../config/global/erasure.md#SP_erasure_code_dir) |

**What it does:** Directory where erasure-code plugins can be found

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global erasure_code_dir "0/erasure-code"
ceph config get global erasure_code_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `0/erasure-code`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global erasure_code_dir
ceph -s
```

---


[← Overview](../OVERVIEW.md)
