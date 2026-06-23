# Ceph

Global config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [ceph_assert_supresssions](#ceph_assert_supresssions) | `(empty)` | Dev | Dev |

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

### ceph_assert_supresssions

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [ceph.md#SP_ceph_assert_supresssions](../../../config/global/ceph.md#SP_ceph_assert_supresssions) |

**What it does:** Suppress specific ceph_assert instances to let the execution continue with unknown, potentially DESTRUCTIVE consequences.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ceph_assert_supresssions "example"
ceph config get global ceph_assert_supresssions
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
