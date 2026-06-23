# General

MDS config deep dive — 1 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [defer_client_eviction_on_laggy_osds](#defer_client_eviction_on_laggy_osds) | `False` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### defer_client_eviction_on_laggy_osds

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mds.md#SP_defer_client_eviction_on_laggy_osds](../../../config/mds/mds.md#SP_defer_client_eviction_on_laggy_osds) |

**What it does:** Do not evict client if any osd is laggy

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds defer_client_eviction_on_laggy_osds true
ceph config get mds defer_client_eviction_on_laggy_osds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds defer_client_eviction_on_laggy_osds
ceph -s
ceph fs status
```

---


[← Overview](../OVERVIEW.md)
