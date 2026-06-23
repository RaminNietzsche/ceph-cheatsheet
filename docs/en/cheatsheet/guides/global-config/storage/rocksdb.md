# Rocksdb

Global config deep dive — 21 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rocksdb_block_size](#rocksdb_block_size) | `4_K` | Advanced | Performance |
| [rocksdb_bloom_bits_per_key](#rocksdb_bloom_bits_per_key) | `20` | Advanced | Performance |
| [rocksdb_cache_index_and_filter_blocks](#rocksdb_cache_index_and_filter_blocks) | `True` | Dev | Dev |
| [rocksdb_cache_index_and_filter_blocks_with_high_priority](#rocksdb_cache_index_and_filter_blocks_with_high_priority) | `False` | Dev | Dev |
| [rocksdb_cache_row_ratio](#rocksdb_cache_row_ratio) | `0` | Advanced | Performance |
| [rocksdb_cache_shard_bits](#rocksdb_cache_shard_bits) | `4` | Advanced | Performance |
| [rocksdb_cache_size](#rocksdb_cache_size) | `512_M` | Advanced | Performance |
| [rocksdb_cache_type](#rocksdb_cache_type) | `binned_lru` | Advanced | Performance |
| [rocksdb_cf_compact_on_deletion](#rocksdb_cf_compact_on_deletion) | `True` | Dev | Dev |
| [rocksdb_cf_compact_on_deletion_sliding_window](#rocksdb_cf_compact_on_deletion_sliding_window) | `32768` | Dev | Dev |
| [rocksdb_cf_compact_on_deletion_trigger](#rocksdb_cf_compact_on_deletion_trigger) | `16384` | Dev | Dev |
| [rocksdb_collect_compaction_stats](#rocksdb_collect_compaction_stats) | `False` | Advanced | Performance |
| [rocksdb_collect_extended_stats](#rocksdb_collect_extended_stats) | `False` | Advanced | Performance |
| [rocksdb_collect_memory_stats](#rocksdb_collect_memory_stats) | `False` | Advanced | Performance |
| [rocksdb_delete_range_threshold](#rocksdb_delete_range_threshold) | `1_M` | Advanced | Performance |
| [rocksdb_index_type](#rocksdb_index_type) | `binary_search` | Dev | Dev |
| [rocksdb_log_to_ceph_log](#rocksdb_log_to_ceph_log) | `True` | Advanced | Performance |
| [rocksdb_metadata_block_size](#rocksdb_metadata_block_size) | `4_K` | Dev | Dev |
| [rocksdb_partition_filters](#rocksdb_partition_filters) | `False` | Dev | Dev |
| [rocksdb_perf](#rocksdb_perf) | `False` | Advanced | Performance |
| [rocksdb_pin_l0_filter_and_index_blocks_in_cache](#rocksdb_pin_l0_filter_and_index_blocks_in_cache) | `False` | Dev | Dev |

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

### rocksdb_block_size

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_block_size](../../../config/global/rocksdb.md#SP_rocksdb_block_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_block_size 4_K
ceph config get global rocksdb_block_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_block_size
ceph -s
```

---

### rocksdb_bloom_bits_per_key

| | |
|---|---|
| Type | Uint · default `20` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_bloom_bits_per_key](../../../config/global/rocksdb.md#SP_rocksdb_bloom_bits_per_key) |

**What it does:** Number of bits per key to use for RocksDB's bloom filters.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_bloom_bits_per_key 20
ceph config get global rocksdb_bloom_bits_per_key
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_bloom_bits_per_key
ceph -s
```

---

### rocksdb_cache_index_and_filter_blocks

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks) |

**What it does:** Whether to cache indices and filters in block cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks false
ceph config get global rocksdb_cache_index_and_filter_blocks
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_cache_index_and_filter_blocks_with_high_priority

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority) |

**What it does:** Whether to cache indices and filters in the block cache with high priority

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks_with_high_priority true
ceph config get global rocksdb_cache_index_and_filter_blocks_with_high_priority
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_cache_row_ratio

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_cache_row_ratio](../../../config/global/rocksdb.md#SP_rocksdb_cache_row_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_cache_row_ratio 0
ceph config get global rocksdb_cache_row_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_cache_row_ratio
ceph -s
```

---

### rocksdb_cache_shard_bits

| | |
|---|---|
| Type | Int · default `4` · **Advanced** · **STARTUP** (restart required) |
| Table | [rocksdb.md#SP_rocksdb_cache_shard_bits](../../../config/global/rocksdb.md#SP_rocksdb_cache_shard_bits) |

**What it does:** Specifies the number of shards by designating the number of significant bits in hash keys. 4 bits -> 16 shards.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_cache_shard_bits 4
ceph config get global rocksdb_cache_shard_bits
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_cache_shard_bits
ceph -s
```

---

### rocksdb_cache_size

| | |
|---|---|
| Type | Size · default `512_M` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_cache_size](../../../config/global/rocksdb.md#SP_rocksdb_cache_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_cache_size 512_M
ceph config get global rocksdb_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_cache_size
ceph -s
```

---

### rocksdb_cache_type

| | |
|---|---|
| Type | Str · default `binned_lru` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_cache_type](../../../config/global/rocksdb.md#SP_rocksdb_cache_type) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_cache_type binned_lru
ceph config get global rocksdb_cache_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `binned_lru`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_cache_type
ceph -s
```

---

### rocksdb_cf_compact_on_deletion

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion) |

**What it does:** Compact the column family when a certain number of tombstones are observed within a given window.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion false
ceph config get global rocksdb_cf_compact_on_deletion
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_cf_compact_on_deletion_sliding_window

| | |
|---|---|
| Type | Int · default `32768` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window) |

**What it does:** The sliding window to use when rocksdb_cf_compact_on_deletion is enabled.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_sliding_window 32768
ceph config get global rocksdb_cf_compact_on_deletion_sliding_window
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`32768`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_cf_compact_on_deletion_trigger

| | |
|---|---|
| Type | Int · default `16384` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger) |

**What it does:** The trigger to use when rocksdb_cf_compact_on_deletion is enabled.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_trigger 16384
ceph config get global rocksdb_cf_compact_on_deletion_trigger
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16384`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_collect_compaction_stats

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_collect_compaction_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_compaction_stats) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rocksdb_collect_compaction_stats true
ceph config get global rocksdb_collect_compaction_stats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_collect_compaction_stats
ceph -s
```

---

### rocksdb_collect_extended_stats

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_collect_extended_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_extended_stats) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rocksdb_collect_extended_stats true
ceph config get global rocksdb_collect_extended_stats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_collect_extended_stats
ceph -s
```

---

### rocksdb_collect_memory_stats

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_collect_memory_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_memory_stats) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rocksdb_collect_memory_stats true
ceph config get global rocksdb_collect_memory_stats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_collect_memory_stats
ceph -s
```

---

### rocksdb_delete_range_threshold

| | |
|---|---|
| Type | Uint · default `1_M` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_delete_range_threshold](../../../config/global/rocksdb.md#SP_rocksdb_delete_range_threshold) |

**What it does:** The number of keys required to invoke DeleteRange when deleting muliple keys.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global rocksdb_delete_range_threshold 1_M
ceph config get global rocksdb_delete_range_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_delete_range_threshold
ceph -s
```

---

### rocksdb_index_type

| | |
|---|---|
| Type | Str · default `binary_search` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_index_type](../../../config/global/rocksdb.md#SP_rocksdb_index_type) |

**What it does:** Type of index for SST files: binary_search, hash_search, two_level

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_index_type binary_search
ceph config get global rocksdb_index_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`binary_search`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_log_to_ceph_log

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_log_to_ceph_log](../../../config/global/rocksdb.md#SP_rocksdb_log_to_ceph_log) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global rocksdb_log_to_ceph_log false
ceph config get global rocksdb_log_to_ceph_log
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_log_to_ceph_log
ceph -s
```

---

### rocksdb_metadata_block_size

| | |
|---|---|
| Type | Size · default `4_K` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_metadata_block_size](../../../config/global/rocksdb.md#SP_rocksdb_metadata_block_size) |

**What it does:** The block size for index partitions. (0 = rocksdb default)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_metadata_block_size 4_K
ceph config get global rocksdb_metadata_block_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_partition_filters

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_partition_filters](../../../config/global/rocksdb.md#SP_rocksdb_partition_filters) |

**What it does:** (Experimental) partition SST index/filters into smaller blocks

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_partition_filters true
ceph config get global rocksdb_partition_filters
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rocksdb_perf

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rocksdb.md#SP_rocksdb_perf](../../../config/global/rocksdb.md#SP_rocksdb_perf) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global rocksdb_perf true
ceph config get global rocksdb_perf
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global rocksdb_perf
ceph -s
```

---

### rocksdb_pin_l0_filter_and_index_blocks_in_cache

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache](../../../config/global/rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache) |

**What it does:** Whether to pin Level 0 indices and bloom filters in the block cache

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global rocksdb_pin_l0_filter_and_index_blocks_in_cache true
ceph config get global rocksdb_pin_l0_filter_and_index_blocks_in_cache
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
