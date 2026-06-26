# Lockdep

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [lockdep](#lockdep) | `False` | Dev | Dev |
| [lockdep_force_backtrace](#lockdep_force_backtrace) | `False` | Dev | Dev |

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

### lockdep

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [lockdep.md#SP_lockdep](../../../config/global/lockdep.md#SP_lockdep) |

**What it does:** Enable the lockdep lock dependency analyzer

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global lockdep true
ceph config get global lockdep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### lockdep_force_backtrace

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [lockdep.md#SP_lockdep_force_backtrace](../../../config/global/lockdep.md#SP_lockdep_force_backtrace) |

**What it does:** Gather a current backtrace at every lock

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`lockdep`](../../../config/global/lockdep.md#SP_lockdep)

**Example:**

```bash
ceph config set global lockdep_force_backtrace true
ceph config get global lockdep_force_backtrace
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
