# Seastore

Crimson config deep dive — 28 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [seastore_block_create](#seastore_block_create) | `True` | Dev | Dev |
| [seastore_cachepin_2q_in_ratio](#seastore_cachepin_2q_in_ratio) | `0.5` | Advanced | Performance |
| [seastore_cachepin_2q_out_ratio](#seastore_cachepin_2q_out_ratio) | `0.5` | Advanced | Performance |
| [seastore_cachepin_size_pershard](#seastore_cachepin_size_pershard) | `2_G` | Advanced | Performance |
| [seastore_cachepin_type](#seastore_cachepin_type) | `LRU` | Dev | Dev |
| [seastore_cbjournal_size](#seastore_cbjournal_size) | `5_G` | Dev | Dev |
| [seastore_cold_tier_generations](#seastore_cold_tier_generations) | `3` | Advanced | Performance |
| [seastore_data_delta_based_overwrite](#seastore_data_delta_based_overwrite) | `0` | Dev | Dev |
| [seastore_default_max_object_size](#seastore_default_max_object_size) | `16777216` | Dev | Dev |
| [seastore_device_size](#seastore_device_size) | `50_G` | Dev | Dev |
| [seastore_disable_end_to_end_data_protection](#seastore_disable_end_to_end_data_protection) | `True` | Dev | Dev |
| [seastore_full_integrity_check](#seastore_full_integrity_check) | `False` | Dev | Dev |
| [seastore_hot_tier_generations](#seastore_hot_tier_generations) | `5` | Advanced | Performance |
| [seastore_journal_batch_capacity](#seastore_journal_batch_capacity) | `16` | Dev | Dev |
| [seastore_journal_batch_flush_size](#seastore_journal_batch_flush_size) | `16_M` | Dev | Dev |
| [seastore_journal_batch_preferred_fullness](#seastore_journal_batch_preferred_fullness) | `0.95` | Dev | Dev |
| [seastore_journal_iodepth_limit](#seastore_journal_iodepth_limit) | `5` | Dev | Dev |
| [seastore_main_device_type](#seastore_main_device_type) | `SSD` | Dev | Dev |
| [seastore_max_concurrent_transactions](#seastore_max_concurrent_transactions) | `128` | Advanced | Performance |
| [seastore_max_data_allocation_size](#seastore_max_data_allocation_size) | `0` | Advanced | Performance |
| [seastore_multiple_tiers_default_evict_ratio](#seastore_multiple_tiers_default_evict_ratio) | `0.6` | Advanced | Performance |
| [seastore_multiple_tiers_fast_evict_ratio](#seastore_multiple_tiers_fast_evict_ratio) | `0.7` | Advanced | Performance |
| [seastore_multiple_tiers_stop_evict_ratio](#seastore_multiple_tiers_stop_evict_ratio) | `0.5` | Advanced | Performance |
| [seastore_require_partition_count_match_reactor_count](#seastore_require_partition_count_match_reactor_count) | `True` | Advanced | Performance |
| [seastore_segment_cleaner_gc_autotune](#seastore_segment_cleaner_gc_autotune) | `True` | Advanced | Performance |
| [seastore_segment_cleaner_gc_autotune_ratio](#seastore_segment_cleaner_gc_autotune_ratio) | `2.0` | Advanced | Performance |
| [seastore_segment_cleaner_gc_formula](#seastore_segment_cleaner_gc_formula) | `cost_benefit` | Advanced | Performance |
| [seastore_segment_size](#seastore_segment_size) | `64_M` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### seastore_block_create

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [seastore.md#SP_seastore_block_create](../../../config/crimson/seastore.md#SP_seastore_block_create) |

**What it does:** Create SegmentManager file if it doesn't exist

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`seastore_device_size`](../../../config/crimson/seastore.md#SP_seastore_device_size)

**Example:**

```bash
ceph config set osd seastore_block_create false
ceph config get osd seastore_block_create
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_cachepin_2q_in_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [seastore.md#SP_seastore_cachepin_2q_in_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_in_ratio) |

**What it does:** Ratio of A1_in queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note that the size of Am(primary) queue in 2Q is cache_size * (1 - in_ratio).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_cachepin_2q_in_ratio 0.5
ceph config get osd seastore_cachepin_2q_in_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_cachepin_2q_in_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_2q_out_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [seastore.md#SP_seastore_cachepin_2q_out_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_out_ratio) |

**What it does:** Ratio of A1_out queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note this size ratio does not reflect actual memory usage, as it represents the size of evicted pages from A1_in queue.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_cachepin_2q_out_ratio 0.5
ceph config get osd seastore_cachepin_2q_out_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_cachepin_2q_out_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_size_pershard

| | |
|---|---|
| Type | Size · default `2_G` · **Advanced** |
| Table | [seastore.md#SP_seastore_cachepin_size_pershard](../../../config/crimson/seastore.md#SP_seastore_cachepin_size_pershard) |

**What it does:** Size in bytes of extents to keep in cache (per reactor).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_cachepin_size_pershard 2_G
ceph config get osd seastore_cachepin_size_pershard
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_cachepin_size_pershard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_cachepin_type

| | |
|---|---|
| Type | Str · enum: ["LRU", "2Q"] · default `LRU` · **Dev** |
| Table | [seastore.md#SP_seastore_cachepin_type](../../../config/crimson/seastore.md#SP_seastore_cachepin_type) |

**What it does:** The cache replacement algorithm used by extent pinboard in seastore. (LRU/2Q)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_cachepin_type LRU
ceph config get osd seastore_cachepin_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`LRU`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_cbjournal_size

| | |
|---|---|
| Type | Size · default `5_G` · **Dev** |
| Table | [seastore.md#SP_seastore_cbjournal_size](../../../config/crimson/seastore.md#SP_seastore_cbjournal_size) |

**What it does:** Total size to use for CircularBoundedJournal if created, it is valid only if seastore_main_device_type is RANDOM_BLOCK

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_cbjournal_size 5_G
ceph config get osd seastore_cbjournal_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_cold_tier_generations

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [seastore.md#SP_seastore_cold_tier_generations](../../../config/crimson/seastore.md#SP_seastore_cold_tier_generations) |

**What it does:** The number of generations in the cold tier if it exists.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_cold_tier_generations 3
ceph config get osd seastore_cold_tier_generations
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_cold_tier_generations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_data_delta_based_overwrite

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [seastore.md#SP_seastore_data_delta_based_overwrite](../../../config/crimson/seastore.md#SP_seastore_data_delta_based_overwrite) |

**What it does:** overwrite the existing data block based on delta if the overwrite size is equal to or less than the value, otherwise do overwrite based on remapping, set to 0 to enforce the remap-based overwrite.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_data_delta_based_overwrite 64
ceph config get osd seastore_data_delta_based_overwrite
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_default_max_object_size

| | |
|---|---|
| Type | Uint · default `16777216` · **Dev** |
| Table | [seastore.md#SP_seastore_default_max_object_size](../../../config/crimson/seastore.md#SP_seastore_default_max_object_size) |

**What it does:** default logical address space reservation for seastore objects' data

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_default_max_object_size 16777216
ceph config get osd seastore_default_max_object_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16777216`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_device_size

| | |
|---|---|
| Type | Size · default `50_G` · **Dev** |
| Table | [seastore.md#SP_seastore_device_size](../../../config/crimson/seastore.md#SP_seastore_device_size) |

**What it does:** Total size to use for SegmentManager block file if created

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_device_size 50_G
ceph config get osd seastore_device_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`50_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_disable_end_to_end_data_protection

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [seastore.md#SP_seastore_disable_end_to_end_data_protection](../../../config/crimson/seastore.md#SP_seastore_disable_end_to_end_data_protection) |

**What it does:** When false, upon mkfs, try to discover whether the nvme device supports internal checksum feature without using sever CPU then enable if available, set to true to disable unconditionally.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_disable_end_to_end_data_protection false
ceph config get osd seastore_disable_end_to_end_data_protection
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_full_integrity_check

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [seastore.md#SP_seastore_full_integrity_check](../../../config/crimson/seastore.md#SP_seastore_full_integrity_check) |

**What it does:** Whether seastore need to fully check the integrity of each extent, non-full integrity check means the integrity check might be skipped during extent remapping for better performance, disable with caution

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_full_integrity_check true
ceph config get osd seastore_full_integrity_check
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_hot_tier_generations

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [seastore.md#SP_seastore_hot_tier_generations](../../../config/crimson/seastore.md#SP_seastore_hot_tier_generations) |

**What it does:** The number of generations in the hot tier or the whole SeaStore instance if there's only one tier.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_hot_tier_generations 5
ceph config get osd seastore_hot_tier_generations
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `5`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_hot_tier_generations
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_journal_batch_capacity

| | |
|---|---|
| Type | Uint · default `16` · **Dev** |
| Table | [seastore.md#SP_seastore_journal_batch_capacity](../../../config/crimson/seastore.md#SP_seastore_journal_batch_capacity) |

**What it does:** The number limit of records in a journal batch

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_journal_batch_capacity 16
ceph config get osd seastore_journal_batch_capacity
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_journal_batch_flush_size

| | |
|---|---|
| Type | Size · default `16_M` · **Dev** |
| Table | [seastore.md#SP_seastore_journal_batch_flush_size](../../../config/crimson/seastore.md#SP_seastore_journal_batch_flush_size) |

**What it does:** The size threshold to force flush a journal batch

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_journal_batch_flush_size 16_M
ceph config get osd seastore_journal_batch_flush_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_journal_batch_preferred_fullness

| | |
|---|---|
| Type | Float · default `0.95` · **Dev** |
| Table | [seastore.md#SP_seastore_journal_batch_preferred_fullness](../../../config/crimson/seastore.md#SP_seastore_journal_batch_preferred_fullness) |

**What it does:** The record fullness threshold to flush a journal batch

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_journal_batch_preferred_fullness 0.95
ceph config get osd seastore_journal_batch_preferred_fullness
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.95`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_journal_iodepth_limit

| | |
|---|---|
| Type | Uint · default `5` · **Dev** |
| Table | [seastore.md#SP_seastore_journal_iodepth_limit](../../../config/crimson/seastore.md#SP_seastore_journal_iodepth_limit) |

**What it does:** The io depth limit to submit journal records

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_journal_iodepth_limit 5
ceph config get osd seastore_journal_iodepth_limit
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_main_device_type

| | |
|---|---|
| Type | Str · default `SSD` · **Dev** |
| Table | [seastore.md#SP_seastore_main_device_type](../../../config/crimson/seastore.md#SP_seastore_main_device_type) |

**What it does:** The main device type seastore uses (SSD or RANDOM_BLOCK_SSD)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd seastore_main_device_type SSD
ceph config get osd seastore_main_device_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`SSD`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### seastore_max_concurrent_transactions

| | |
|---|---|
| Type | Uint · default `128` · **Advanced** |
| Table | [seastore.md#SP_seastore_max_concurrent_transactions](../../../config/crimson/seastore.md#SP_seastore_max_concurrent_transactions) |

**What it does:** maximum concurrent transactions that seastore allows (per reactor)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd seastore_max_concurrent_transactions 128
ceph config get osd seastore_max_concurrent_transactions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_max_concurrent_transactions
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_max_data_allocation_size

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [seastore.md#SP_seastore_max_data_allocation_size](../../../config/crimson/seastore.md#SP_seastore_max_data_allocation_size) |

**What it does:** Max size in bytes that an extent can be, 0 to disable

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd seastore_max_data_allocation_size 64
ceph config get osd seastore_max_data_allocation_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_max_data_allocation_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_default_evict_ratio

| | |
|---|---|
| Type | Float · default `0.6` · **Advanced** |
| Table | [seastore.md#SP_seastore_multiple_tiers_default_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_default_evict_ratio) |

**What it does:** Begin evicting cold data to the cold tier when the used ratio of the main tier reaches this value.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_multiple_tiers_default_evict_ratio 0.6
ceph config get osd seastore_multiple_tiers_default_evict_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_multiple_tiers_default_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_fast_evict_ratio

| | |
|---|---|
| Type | Float · default `0.7` · **Advanced** |
| Table | [seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio) |

**What it does:** Begin fast eviction when the used ratio of the main tier reaches this value.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_multiple_tiers_fast_evict_ratio 0.7
ceph config get osd seastore_multiple_tiers_fast_evict_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.7`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_multiple_tiers_fast_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_multiple_tiers_stop_evict_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio) |

**What it does:** When the used ratio of main tier is less than this value, then stop evict cold data to the cold tier.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_multiple_tiers_stop_evict_ratio 0.5
ceph config get osd seastore_multiple_tiers_stop_evict_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_multiple_tiers_stop_evict_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_require_partition_count_match_reactor_count

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [seastore.md#SP_seastore_require_partition_count_match_reactor_count](../../../config/crimson/seastore.md#SP_seastore_require_partition_count_match_reactor_count) |

**What it does:** disable osd shards changes upon restart.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd seastore_require_partition_count_match_reactor_count false
ceph config get osd seastore_require_partition_count_match_reactor_count
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_require_partition_count_match_reactor_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [seastore.md#SP_seastore_segment_cleaner_gc_autotune](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune) |

**What it does:** When the configured gc formula (cost_benefit or benefit) picks a segment whose free-space fraction (1 - utilization) is at least seastore_segment_cleaner_gc_autotune_ratio times smaller than the lowest-utilization candidate, override the pick with the greedy choice. COST_BENEFIT and BENEFIT weight segment age, which is the right call when age predicts dead-byte accumulation (journaling / LIFO workloads). Under random-write at high alive_ratio dead bytes spread uniformly across segments, age stops predicting deadness, and the formula can pick a high-util old segment whose reclaim frees several times less space than the lowest-util candidate. When this option is enabled the cleaner detects the mis-selection at runtime and overrides the formula's pick with the greedy choice. Disable to honor the configured formula unconditionally. Ignored when seastore_segment_cleaner_gc_formula = greedy.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune false
ceph config get osd seastore_segment_cleaner_gc_autotune
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_segment_cleaner_gc_autotune
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_autotune_ratio

| | |
|---|---|
| Type | Float · default `2.0` · **Advanced** |
| Table | [seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio) |

**What it does:** Override threshold for the gc auto-tune. The configured formula's pick is overridden with the greedy candidate when greedy's free fraction is at least this ratio times the formula's pick's free fraction. Higher is more conservative (override fires less often, the configured formula's age weighting is preserved more aggressively). Lower is more aggressive (override fires more often, behaviour converges toward pure greedy). The default (2.0) captures the random-write failure regime while staying clear of normal-operation fluctuations.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune_ratio 2.0
ceph config get osd seastore_segment_cleaner_gc_autotune_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2.0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1.0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_segment_cleaner_gc_autotune_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_cleaner_gc_formula

| | |
|---|---|
| Type | Str · enum: ["greedy", "cost_benefit", "benefit"] · default `cost_benefit` · **Advanced** |
| Table | [seastore.md#SP_seastore_segment_cleaner_gc_formula](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_formula) |

**What it does:** The algorithm that SegmentCleaner will use to select segments to reclaim

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_segment_cleaner_gc_formula cost_benefit
ceph config get osd seastore_segment_cleaner_gc_formula
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `cost_benefit`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_segment_cleaner_gc_formula
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### seastore_segment_size

| | |
|---|---|
| Type | Size · default `64_M` · **Advanced** |
| Table | [seastore.md#SP_seastore_segment_size](../../../config/crimson/seastore.md#SP_seastore_segment_size) |

**What it does:** Segment size to use for SegmentManager

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd seastore_segment_size 64_M
ceph config get osd seastore_segment_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd seastore_segment_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
