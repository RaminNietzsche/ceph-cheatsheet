# Tmp

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [tmp_dir](#tmp_dir) | `/tmp` | Advanced | Capacity |
| [tmp_file_template](#tmp_file_template) | `$tmp_dir/$cluster-$name.XXXXXX` | Advanced | Performance |

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

### tmp_dir

| | |
|---|---|
| Type | Str · default `/tmp` · **Advanced** |
| Table | [tmp.md#SP_tmp_dir](../../../config/global/tmp.md#SP_tmp_dir) |

**What it does:** Path for the 'tmp' directory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global tmp_dir "/tmp"
ceph config get global tmp_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/tmp`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global tmp_dir
ceph -s
```

---

### tmp_file_template

| | |
|---|---|
| Type | Str · default `$tmp_dir/$cluster-$name.XXXXXX` · **Advanced** |
| Table | [tmp.md#SP_tmp_file_template](../../../config/global/tmp.md#SP_tmp_file_template) |

**What it does:** Template for temporary files created by daemons for ceph tell commands

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global tmp_file_template "$tmp_dir/$cluster-$name.XXXXXX"
ceph config get global tmp_file_template
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `$tmp_dir/$cluster-$name.XXXXXX`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global tmp_file_template
ceph -s
```

---


[← Overview](../OVERVIEW.md)
