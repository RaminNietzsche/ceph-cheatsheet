# Debug

MDS client config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [debug_allow_any_pool_priority](#debug_allow_any_pool_priority) | `False` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### debug_allow_any_pool_priority

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [debug.md#SP_debug_allow_any_pool_priority](../../../config/mds-client/debug.md#SP_debug_allow_any_pool_priority) |

**What it does:** Allow any pool priority to be set to test conversion to new range

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client debug_allow_any_pool_priority true
ceph config get client debug_allow_any_pool_priority
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
