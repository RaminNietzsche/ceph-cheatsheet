# Readahead

RBD config deep dive — 3 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_readahead_disable_after_bytes](#rbd_readahead_disable_after_bytes) | `50_M` | Advanced | Performance |
| [rbd_readahead_max_bytes](#rbd_readahead_max_bytes) | `512_K` | Advanced | Performance |
| [rbd_readahead_trigger_requests](#rbd_readahead_trigger_requests) | `10` | Advanced | Performance |

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

### rbd_readahead_disable_after_bytes

| | |
|---|---|
| Type | Size · default `50_M` · **Advanced** |
| Table | [rbd.md#SP_rbd_readahead_disable_after_bytes](../../../config/rbd/rbd.md#SP_rbd_readahead_disable_after_bytes) |

**What it does:** how many bytes are read in total before readahead is disabled

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_readahead_disable_after_bytes 50_M
ceph config get client rbd_readahead_disable_after_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_readahead_disable_after_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_readahead_max_bytes

| | |
|---|---|
| Type | Size · default `512_K` · **Advanced** |
| Table | [rbd.md#SP_rbd_readahead_max_bytes](../../../config/rbd/rbd.md#SP_rbd_readahead_max_bytes) |

**What it does:** set to 0 to disable readahead

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_readahead_max_bytes 512_K
ceph config get client rbd_readahead_max_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_readahead_max_bytes
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_readahead_trigger_requests

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rbd.md#SP_rbd_readahead_trigger_requests](../../../config/rbd/rbd.md#SP_rbd_readahead_trigger_requests) |

**What it does:** number of sequential requests necessary to trigger readahead

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_readahead_trigger_requests 10
ceph config get client rbd_readahead_trigger_requests
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_readahead_trigger_requests
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
