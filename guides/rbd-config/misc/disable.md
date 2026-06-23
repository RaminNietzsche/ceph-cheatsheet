# Disable

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_disable_zero_copy_writes](#rbd_disable_zero_copy_writes) | `True` | Advanced | Policy |

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

### rbd_disable_zero_copy_writes

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_disable_zero_copy_writes](../../../config/rbd/rbd.md#SP_rbd_disable_zero_copy_writes) |

**What it does:** Disable the use of zero-copy writes to ensure unstable writes from clients cannot cause a CRC mismatch

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_disable_zero_copy_writes false
ceph config get client rbd_disable_zero_copy_writes
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_disable_zero_copy_writes
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
