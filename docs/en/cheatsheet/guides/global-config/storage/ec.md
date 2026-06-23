# Ec

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [ec_extent_cache_size](#ec_extent_cache_size) | `10485760` | Advanced | Performance |
| [ec_pdw_write_mode](#ec_pdw_write_mode) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### ec_extent_cache_size

| | |
|---|---|
| Type | Uint · default `10485760` · **Advanced** |
| Table | [ec.md#SP_ec_extent_cache_size](../../../config/global/ec.md#SP_ec_extent_cache_size) |

**What it does:** Size of the per-shard extent cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ec_extent_cache_size 10485760
ceph config get global ec_extent_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10485760`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ec_extent_cache_size
ceph -s
```

---

### ec_pdw_write_mode

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [ec.md#SP_ec_pdw_write_mode](../../../config/global/ec.md#SP_ec_pdw_write_mode) |

**What it does:** When EC writes should generate PDWs (development only) 0=optimal 1=never 2=when possible

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ec_pdw_write_mode 64
ceph config get global ec_pdw_write_mode
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
