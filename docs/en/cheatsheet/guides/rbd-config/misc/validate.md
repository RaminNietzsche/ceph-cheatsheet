# Validate

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_validate_names](#rbd_validate_names) | `True` | Advanced | Performance |
| [rbd_validate_pool](#rbd_validate_pool) | `True` | Dev | Dev |

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

### rbd_validate_names

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_validate_names](../../../config/rbd/rbd.md#SP_rbd_validate_names) |

**What it does:** validate new image names for RBD compatibility

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_validate_names false
ceph config get client rbd_validate_names
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_validate_names
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_validate_pool

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rbd.md#SP_rbd_validate_pool](../../../config/rbd/rbd.md#SP_rbd_validate_pool) |

**What it does:** validate empty pools for RBD compatibility

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_validate_pool false
ceph config get client rbd_validate_pool
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
