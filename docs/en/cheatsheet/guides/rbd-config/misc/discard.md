# Discard

RBD config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_discard_granularity_bytes](#rbd_discard_granularity_bytes) | `64_K` | Advanced | Performance |
| [rbd_discard_on_zeroed_write_same](#rbd_discard_on_zeroed_write_same) | `True` | Advanced | Performance |

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

### rbd_discard_granularity_bytes

| | |
|---|---|
| Type | Uint · default `64_K` · **Advanced** |
| Table | [rbd.md#SP_rbd_discard_granularity_bytes](../../../config/rbd/rbd.md#SP_rbd_discard_granularity_bytes) |

**What it does:** minimum aligned size of discard operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_discard_granularity_bytes 64_K
ceph config get client rbd_discard_granularity_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `4_K`, max `32_M`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_discard_granularity_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_discard_on_zeroed_write_same

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rbd.md#SP_rbd_discard_on_zeroed_write_same](../../../config/rbd/rbd.md#SP_rbd_discard_on_zeroed_write_same) |

**What it does:** discard data on zeroed write same instead of writing zero

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client rbd_discard_on_zeroed_write_same false
ceph config get client rbd_discard_on_zeroed_write_same
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_discard_on_zeroed_write_same
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
