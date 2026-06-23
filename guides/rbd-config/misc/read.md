# Read

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_read_from_replica_policy](#rbd_read_from_replica_policy) | `default` | Basic | Policy |

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

### rbd_read_from_replica_policy

| | |
|---|---|
| Type | Str · enum: ["default", "balance", "localize"] · default `default` · **Basic** |
| Table | [rbd.md#SP_rbd_read_from_replica_policy](../../../config/rbd/rbd.md#SP_rbd_read_from_replica_policy) |

**What it does:** Read replica policy send to the OSDS during reads

**When to use:** Core RBD behavior — review before changing in production.

**Example:**

```bash
ceph config set client rbd_read_from_replica_policy default
ceph config get client rbd_read_from_replica_policy
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `default` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_read_from_replica_policy
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
