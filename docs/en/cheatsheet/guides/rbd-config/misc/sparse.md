# Sparse

RBD config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_sparse_read_threshold_bytes](#rbd_sparse_read_threshold_bytes) | `64_K` | Advanced | Performance |

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

### rbd_sparse_read_threshold_bytes

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [rbd.md#SP_rbd_sparse_read_threshold_bytes](../../../config/rbd/rbd.md#SP_rbd_sparse_read_threshold_bytes) |

**What it does:** threshold for issuing a sparse-read

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_sparse_read_threshold_bytes 64_K
ceph config get client rbd_sparse_read_threshold_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_sparse_read_threshold_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
