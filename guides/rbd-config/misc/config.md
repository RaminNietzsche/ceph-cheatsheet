# Config

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_config_pool_override_update_timestamp](#rbd_config_pool_override_update_timestamp) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_config_pool_override_update_timestamp

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rbd.md#SP_rbd_config_pool_override_update_timestamp](../../../config/rbd/rbd.md#SP_rbd_config_pool_override_update_timestamp) |

**What it does:** timestamp of last update to pool-level config overrides

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_config_pool_override_update_timestamp 64
ceph config get client rbd_config_pool_override_update_timestamp
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
