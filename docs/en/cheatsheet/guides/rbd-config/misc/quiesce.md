# Quiesce

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_quiesce_notification_attempts](#rbd_quiesce_notification_attempts) | `10` | Dev | Dev |

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

### rbd_quiesce_notification_attempts

| | |
|---|---|
| Type | Uint · default `10` · **Dev** |
| Table | [rbd.md#SP_rbd_quiesce_notification_attempts](../../../config/rbd/rbd.md#SP_rbd_quiesce_notification_attempts) |

**What it does:** the number of quiesce notification attempts

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_quiesce_notification_attempts 10
ceph config get client rbd_quiesce_notification_attempts
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
