# Fio

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [fio_dir](#fio_dir) | `/tmp/fio` | Advanced | Capacity |

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

### fio_dir

| | |
|---|---|
| Type | Str · default `/tmp/fio` · **Advanced** |
| Table | [fio.md#SP_fio_dir](../../../config/global/fio.md#SP_fio_dir) |

**What it does:** FIO data directory for FIO-objectstore

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global fio_dir "/tmp/fio"
ceph config get global fio_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/tmp/fio`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global fio_dir
ceph -s
```

---


[← Overview](../OVERVIEW.md)
