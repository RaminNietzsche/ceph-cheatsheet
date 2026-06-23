# Filer

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [filer_max_purge_ops](#filer_max_purge_ops) | `10` | Advanced | Performance |
| [filer_max_truncate_ops](#filer_max_truncate_ops) | `128` | Advanced | Performance |

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

### filer_max_purge_ops

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [filer.md#SP_filer_max_purge_ops](../../../config/global/filer.md#SP_filer_max_purge_ops) |

**What it does:** Max in-flight operations for purging a striped range (e.g., MDS journal)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filer_max_purge_ops 10
ceph config get global filer_max_purge_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filer_max_purge_ops
ceph -s
```

---

### filer_max_truncate_ops

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [filer.md#SP_filer_max_truncate_ops](../../../config/global/filer.md#SP_filer_max_truncate_ops) |

**What it does:** Max in-flight operations for truncating/deleting a striped sequence (e.g., MDS journal)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global filer_max_truncate_ops 128
ceph config get global filer_max_truncate_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global filer_max_truncate_ops
ceph -s
```

---


[← Overview](../OVERVIEW.md)
