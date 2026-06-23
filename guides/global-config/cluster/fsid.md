# Fsid

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [fsid](#fsid) | `(empty)` | Basic | Policy |

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

### fsid

| | |
|---|---|
| Type | Uuid · default `(empty)` · **Basic** · **STARTUP** (restart required) |
| Table | [fsid.md#SP_fsid](../../../config/global/fsid.md#SP_fsid) |

**What it does:** cluster fsid (uuid)

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global fsid (empty)
ceph config get global fsid
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `(empty)` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global fsid
ceph -s
```

---


[← Overview](../OVERVIEW.md)
