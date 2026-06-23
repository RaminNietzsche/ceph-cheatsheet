# Rocksdb

deep dive پیکربندی Global — 21 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
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

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rocksdb_block_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_block_size](../../../config/global/rocksdb.md#SP_rocksdb_block_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_block_size 4_K
ceph config get global rocksdb_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_block_size
ceph -s
```

---

### rocksdb_bloom_bits_per_key

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_bloom_bits_per_key](../../../config/global/rocksdb.md#SP_rocksdb_bloom_bits_per_key) |

**کارکرد:** Number of bits per key to use for RocksDB's bloom filters.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_bloom_bits_per_key 20
ceph config get global rocksdb_bloom_bits_per_key
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_bloom_bits_per_key
ceph -s
```

---

### rocksdb_cache_index_and_filter_blocks

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks) |

**کارکرد:** Whether to cache indices and filters in block cache

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks false
ceph config get global rocksdb_cache_index_and_filter_blocks
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_cache_index_and_filter_blocks_with_high_priority

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority](../../../config/global/rocksdb.md#SP_rocksdb_cache_index_and_filter_blocks_with_high_priority) |

**کارکرد:** Whether to cache indices and filters in the block cache with high priority

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_cache_index_and_filter_blocks_with_high_priority true
ceph config get global rocksdb_cache_index_and_filter_blocks_with_high_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_cache_row_ratio

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_cache_row_ratio](../../../config/global/rocksdb.md#SP_rocksdb_cache_row_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_cache_row_ratio 0
ceph config get global rocksdb_cache_row_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_cache_row_ratio
ceph -s
```

---

### rocksdb_cache_shard_bits

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [rocksdb.md#SP_rocksdb_cache_shard_bits](../../../config/global/rocksdb.md#SP_rocksdb_cache_shard_bits) |

**کارکرد:** Specifies the number of shards by designating the number of significant bits in hash keys. 4 bits -> 16 shards.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_cache_shard_bits 4
ceph config get global rocksdb_cache_shard_bits
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_cache_shard_bits
ceph -s
```

---

### rocksdb_cache_size

| | |
|---|---|
| نوع | Size · default `512_M` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_cache_size](../../../config/global/rocksdb.md#SP_rocksdb_cache_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_cache_size 512_M
ceph config get global rocksdb_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `512_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_cache_size
ceph -s
```

---

### rocksdb_cache_type

| | |
|---|---|
| نوع | Str · default `binned_lru` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_cache_type](../../../config/global/rocksdb.md#SP_rocksdb_cache_type) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_cache_type binned_lru
ceph config get global rocksdb_cache_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `binned_lru`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_cache_type
ceph -s
```

---

### rocksdb_cf_compact_on_deletion

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion) |

**کارکرد:** Compact the column family when a certain number of tombstones are observed within a given window.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion false
ceph config get global rocksdb_cf_compact_on_deletion
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_cf_compact_on_deletion_sliding_window

| | |
|---|---|
| نوع | Int · default `32768` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_sliding_window) |

**کارکرد:** The sliding window to use when rocksdb_cf_compact_on_deletion is enabled.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_sliding_window 32768
ceph config get global rocksdb_cf_compact_on_deletion_sliding_window
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`32768`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_cf_compact_on_deletion_trigger

| | |
|---|---|
| نوع | Int · default `16384` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger](../../../config/global/rocksdb.md#SP_rocksdb_cf_compact_on_deletion_trigger) |

**کارکرد:** The trigger to use when rocksdb_cf_compact_on_deletion is enabled.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_cf_compact_on_deletion_trigger 16384
ceph config get global rocksdb_cf_compact_on_deletion_trigger
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`16384`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_collect_compaction_stats

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_collect_compaction_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_compaction_stats) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global rocksdb_collect_compaction_stats true
ceph config get global rocksdb_collect_compaction_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_collect_compaction_stats
ceph -s
```

---

### rocksdb_collect_extended_stats

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_collect_extended_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_extended_stats) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global rocksdb_collect_extended_stats true
ceph config get global rocksdb_collect_extended_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_collect_extended_stats
ceph -s
```

---

### rocksdb_collect_memory_stats

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_collect_memory_stats](../../../config/global/rocksdb.md#SP_rocksdb_collect_memory_stats) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global rocksdb_collect_memory_stats true
ceph config get global rocksdb_collect_memory_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_collect_memory_stats
ceph -s
```

---

### rocksdb_delete_range_threshold

| | |
|---|---|
| نوع | Uint · default `1_M` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_delete_range_threshold](../../../config/global/rocksdb.md#SP_rocksdb_delete_range_threshold) |

**کارکرد:** The number of keys required to invoke DeleteRange when deleting muliple keys.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global rocksdb_delete_range_threshold 1_M
ceph config get global rocksdb_delete_range_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_delete_range_threshold
ceph -s
```

---

### rocksdb_index_type

| | |
|---|---|
| نوع | Str · default `binary_search` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_index_type](../../../config/global/rocksdb.md#SP_rocksdb_index_type) |

**کارکرد:** Type of index for SST files: binary_search, hash_search, two_level

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_index_type binary_search
ceph config get global rocksdb_index_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`binary_search`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_log_to_ceph_log

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_log_to_ceph_log](../../../config/global/rocksdb.md#SP_rocksdb_log_to_ceph_log) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global rocksdb_log_to_ceph_log false
ceph config get global rocksdb_log_to_ceph_log
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_log_to_ceph_log
ceph -s
```

---

### rocksdb_metadata_block_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_metadata_block_size](../../../config/global/rocksdb.md#SP_rocksdb_metadata_block_size) |

**کارکرد:** The block size for index partitions. (0 = rocksdb default)

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_metadata_block_size 4_K
ceph config get global rocksdb_metadata_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`4_K`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_partition_filters

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_partition_filters](../../../config/global/rocksdb.md#SP_rocksdb_partition_filters) |

**کارکرد:** (Experimental) partition SST index/filters into smaller blocks

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_partition_filters true
ceph config get global rocksdb_partition_filters
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### rocksdb_perf

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rocksdb.md#SP_rocksdb_perf](../../../config/global/rocksdb.md#SP_rocksdb_perf) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global rocksdb_perf true
ceph config get global rocksdb_perf
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global rocksdb_perf
ceph -s
```

---

### rocksdb_pin_l0_filter_and_index_blocks_in_cache

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache](../../../config/global/rocksdb.md#SP_rocksdb_pin_l0_filter_and_index_blocks_in_cache) |

**کارکرد:** Whether to pin Level 0 indices and bloom filters in the block cache

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global rocksdb_pin_l0_filter_and_index_blocks_in_cache true
ceph config get global rocksdb_pin_l0_filter_and_index_blocks_in_cache
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
