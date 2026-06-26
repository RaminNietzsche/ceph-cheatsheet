# PG & pool health

MON config deep dive — 14 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_allow_pool_size_one](#mon_allow_pool_size_one) | `False` | Advanced | Policy |
| [mon_clean_pg_upmaps_per_chunk](#mon_clean_pg_upmaps_per_chunk) | `256` | Dev | Dev |
| [mon_max_pool_pg_num](#mon_max_pool_pg_num) | `64_K` | Advanced | Performance |
| [mon_osd_prime_pg_temp](#mon_osd_prime_pg_temp) | `True` | Dev | Dev |
| [mon_osd_prime_pg_temp_max_estimate](#mon_osd_prime_pg_temp_max_estimate) | `0.25` | Advanced | Performance |
| [mon_osd_prime_pg_temp_max_time](#mon_osd_prime_pg_temp_max_time) | `0.5` | Dev | Dev |
| [mon_stretch_pool_min_size](#mon_stretch_pool_min_size) | `2` | Dev | Dev |
| [mon_stretch_pool_size](#mon_stretch_pool_size) | `4` | Dev | Dev |
| [mon_warn_on_cache_pools_without_hit_sets](#mon_warn_on_cache_pools_without_hit_sets) | `True` | Advanced | Performance |
| [mon_warn_on_pool_no_redundancy](#mon_warn_on_pool_no_redundancy) | `True` | Advanced | Performance |
| [mon_warn_on_pool_pg_num_not_power_of_two](#mon_warn_on_pool_pg_num_not_power_of_two) | `True` | Dev | Dev |
| [pool_availability_update_interval](#pool_availability_update_interval) | `1` | Advanced | Performance |
| [osd_pool_default_crimson](#osd_pool_default_crimson) | `False` | Advanced | Performance |
| [osd_pool_erasure_code_stripe_unit](#osd_pool_erasure_code_stripe_unit) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_allow_pool_size_one

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_allow_pool_size_one](../../../config/mon/mon.md#SP_mon_allow_pool_size_one) |

**What it does:** Allow pools with `size=1` (no redundancy).

**When to use:** Lab only. Keep `false` in production unless you accept data loss risk.

**Example:**

```bash
ceph config set mon mon_allow_pool_size_one true
ceph config get mon mon_allow_pool_size_one
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_allow_pool_size_one
ceph -s
ceph mon stat
```

---

### mon_clean_pg_upmaps_per_chunk

| | |
|---|---|
| Type | Uint · default `256` · **Dev** |
| Table | [mon.md#SP_mon_clean_pg_upmaps_per_chunk](../../../config/mon/mon.md#SP_mon_clean_pg_upmaps_per_chunk) |

**What it does:** granularity of PG upmap validation background work

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_clean_pg_upmaps_per_chunk 256
ceph config get mon mon_clean_pg_upmaps_per_chunk
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`256`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_max_pool_pg_num

| | |
|---|---|
| Type | Uint · default `64_K` · **Advanced** |
| Table | [mon.md#SP_mon_max_pool_pg_num](../../../config/mon/mon.md#SP_mon_max_pool_pg_num) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_pool_pg_num 64_K
ceph config get mon mon_max_pool_pg_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_pool_pg_num
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mon.md#SP_mon_osd_prime_pg_temp](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp) |

**What it does:** minimize peering work by priming pg_temp values after a map change

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_osd_prime_pg_temp false
ceph config get mon mon_osd_prime_pg_temp
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_osd_prime_pg_temp_max_estimate

| | |
|---|---|
| Type | Float · default `0.25` · **Advanced** |
| Table | [mon.md#SP_mon_osd_prime_pg_temp_max_estimate](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_estimate) |

**What it does:** calculate all PG mappings if estimated fraction of PGs that change is above this amount

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_estimate 0.25
ceph config get mon mon_osd_prime_pg_temp_max_estimate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.25`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_prime_pg_temp_max_estimate
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp_max_time

| | |
|---|---|
| Type | Float · default `0.5` · **Dev** |
| Table | [mon.md#SP_mon_osd_prime_pg_temp_max_time](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_time) |

**What it does:** maximum time to spend precalculating PG mappings on map change (seconds)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_time 0.5
ceph config get mon mon_osd_prime_pg_temp_max_time
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_stretch_pool_min_size

| | |
|---|---|
| Type | Uint · default `2` · **Dev** |
| Table | [mon.md#SP_mon_stretch_pool_min_size](../../../config/mon/mon.md#SP_mon_stretch_pool_min_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_stretch_pool_min_size 2
ceph config get mon mon_stretch_pool_min_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_stretch_pool_size

| | |
|---|---|
| Type | Uint · default `4` · **Dev** |
| Table | [mon.md#SP_mon_stretch_pool_size](../../../config/mon/mon.md#SP_mon_stretch_pool_size) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_stretch_pool_size 4
ceph config get mon mon_stretch_pool_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_warn_on_cache_pools_without_hit_sets

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_cache_pools_without_hit_sets](../../../config/mon/mon.md#SP_mon_warn_on_cache_pools_without_hit_sets) |

**What it does:** issue CACHE_POOL_NO_HIT_SET health warning for cache pools that do not have hit sets configured

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_cache_pools_without_hit_sets false
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_redundancy

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_pool_no_redundancy](../../../config/mon/mon.md#SP_mon_warn_on_pool_no_redundancy) |

**What it does:** Warn when any pool has no redundancy (`size=1` or `min_size=1`).

**When to use:** Leave enabled in production.

**Example:**

```bash
ceph config set mon mon_warn_on_pool_no_redundancy false
ceph config get mon mon_warn_on_pool_no_redundancy
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_pool_no_redundancy
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_pg_num_not_power_of_two

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two](../../../config/mon/mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two) |

**What it does:** issue POOL_PG_NUM_NOT_POWER_OF_TWO warning if pool has a non-power-of-two pg_num value

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_warn_on_pool_pg_num_not_power_of_two false
ceph config get mon mon_warn_on_pool_pg_num_not_power_of_two
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### pool_availability_update_interval

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [mon.md#SP_pool_availability_update_interval](../../../config/mon/mon.md#SP_pool_availability_update_interval) |

**What it does:** Update data availability score at this interval. By default the interval is same as paxos_propose_interval configuration.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon pool_availability_update_interval 1
ceph config get mon pool_availability_update_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon pool_availability_update_interval
ceph -s
ceph mon stat
```

---

### osd_pool_default_crimson

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_pool_default_crimson](../../../config/mon/osd.md#SP_osd_pool_default_crimson) |

**What it does:** Create pools by default with FLAG_CRIMSON

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_pool_default_crimson true
ceph config get osd osd_pool_default_crimson
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_default_crimson
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_erasure_code_stripe_unit

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_pool_erasure_code_stripe_unit](../../../config/mon/osd.md#SP_osd_pool_erasure_code_stripe_unit) |

**What it does:** the amount of data (in bytes) in a data chunk, per stripe A value of 0 causes the code to select either a 4KB or 16KB stripe_unit depending on whether allow_ec_optimizations is enabled.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_pool_erasure_code_stripe_unit 64
ceph config get osd osd_pool_erasure_code_stripe_unit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pool_erasure_code_stripe_unit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
