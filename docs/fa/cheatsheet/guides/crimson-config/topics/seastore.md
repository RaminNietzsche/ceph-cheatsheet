# Seastore

راهنمای عمیق پیکربندی Crimson — 28 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [seastore_block_create](#seastore_block_create) | `True` | Dev | توسعه |
| [seastore_cachepin_2q_in_ratio](#seastore_cachepin_2q_in_ratio) | `0.5` | Advanced | عملکرد |
| [seastore_cachepin_2q_out_ratio](#seastore_cachepin_2q_out_ratio) | `0.5` | Advanced | عملکرد |
| [seastore_cachepin_size_pershard](#seastore_cachepin_size_pershard) | `2_G` | Advanced | عملکرد |
| [seastore_cachepin_type](#seastore_cachepin_type) | `LRU` | Dev | توسعه |
| [seastore_cbjournal_size](#seastore_cbjournal_size) | `5_G` | Dev | توسعه |
| [seastore_cold_tier_generations](#seastore_cold_tier_generations) | `3` | Advanced | عملکرد |
| [seastore_data_delta_based_overwrite](#seastore_data_delta_based_overwrite) | `0` | Dev | توسعه |
| [seastore_default_max_object_size](#seastore_default_max_object_size) | `16777216` | Dev | توسعه |
| [seastore_device_size](#seastore_device_size) | `50_G` | Dev | توسعه |
| [seastore_disable_end_to_end_data_protection](#seastore_disable_end_to_end_data_protection) | `True` | Dev | توسعه |
| [seastore_full_integrity_check](#seastore_full_integrity_check) | `False` | Dev | توسعه |
| [seastore_hot_tier_generations](#seastore_hot_tier_generations) | `5` | Advanced | عملکرد |
| [seastore_journal_batch_capacity](#seastore_journal_batch_capacity) | `16` | Dev | توسعه |
| [seastore_journal_batch_flush_size](#seastore_journal_batch_flush_size) | `16_M` | Dev | توسعه |
| [seastore_journal_batch_preferred_fullness](#seastore_journal_batch_preferred_fullness) | `0.95` | Dev | توسعه |
| [seastore_journal_iodepth_limit](#seastore_journal_iodepth_limit) | `5` | Dev | توسعه |
| [seastore_main_device_type](#seastore_main_device_type) | `SSD` | Dev | توسعه |
| [seastore_max_concurrent_transactions](#seastore_max_concurrent_transactions) | `128` | Advanced | عملکرد |
| [seastore_max_data_allocation_size](#seastore_max_data_allocation_size) | `0` | Advanced | عملکرد |
| [seastore_multiple_tiers_default_evict_ratio](#seastore_multiple_tiers_default_evict_ratio) | `0.6` | Advanced | عملکرد |
| [seastore_multiple_tiers_fast_evict_ratio](#seastore_multiple_tiers_fast_evict_ratio) | `0.7` | Advanced | عملکرد |
| [seastore_multiple_tiers_stop_evict_ratio](#seastore_multiple_tiers_stop_evict_ratio) | `0.5` | Advanced | عملکرد |
| [seastore_require_partition_count_match_reactor_count](#seastore_require_partition_count_match_reactor_count) | `True` | Advanced | عملکرد |
| [seastore_segment_cleaner_gc_autotune](#seastore_segment_cleaner_gc_autotune) | `True` | Advanced | عملکرد |
| [seastore_segment_cleaner_gc_autotune_ratio](#seastore_segment_cleaner_gc_autotune_ratio) | `2.0` | Advanced | عملکرد |
| [seastore_segment_cleaner_gc_formula](#seastore_segment_cleaner_gc_formula) | `cost_benefit` | Advanced | عملکرد |
| [seastore_segment_size](#seastore_segment_size) | `64_M` | Advanced | عملکرد |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### seastore_block_create

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [seastore.md#SP_seastore_block_create](../../../config/crimson/seastore.md#SP_seastore_block_create) |

**کارکرد:** Create SegmentManager file if it doesn't exist

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_block_create false
ceph config get osd seastore_block_create
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_cachepin_2q_in_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [seastore.md#SP_seastore_cachepin_2q_in_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_in_ratio) |

**کارکرد:** Ratio of A1_in queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note that the size of Am(primary) queue in 2Q is cache_size * (1 - in_ratio).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_cachepin_2q_in_ratio 0.5
ceph config get osd seastore_cachepin_2q_in_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [seastore.md#SP_seastore_cachepin_2q_out_ratio](../../../config/crimson/seastore.md#SP_seastore_cachepin_2q_out_ratio) |

**کارکرد:** Ratio of A1_out queue size to cache size(seastore_cachepin_size_pershard) in 2Q cache algorithm. Note this size ratio does not reflect actual memory usage, as it represents the size of evicted pages from A1_in queue.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_cachepin_2q_out_ratio 0.5
ceph config get osd seastore_cachepin_2q_out_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Size · default `2_G` · **Advanced** |
| جدول | [seastore.md#SP_seastore_cachepin_size_pershard](../../../config/crimson/seastore.md#SP_seastore_cachepin_size_pershard) |

**کارکرد:** Size in bytes of extents to keep in cache (per reactor).

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_cachepin_size_pershard 2_G
ceph config get osd seastore_cachepin_size_pershard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Str · enum: ["LRU", "2Q"] · default `LRU` · **Dev** |
| جدول | [seastore.md#SP_seastore_cachepin_type](../../../config/crimson/seastore.md#SP_seastore_cachepin_type) |

**کارکرد:** The cache replacement algorithm used by extent pinboard in seastore. (LRU/2Q)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_cachepin_type LRU
ceph config get osd seastore_cachepin_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`LRU`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_cbjournal_size

| | |
|---|---|
| نوع | Size · default `5_G` · **Dev** |
| جدول | [seastore.md#SP_seastore_cbjournal_size](../../../config/crimson/seastore.md#SP_seastore_cbjournal_size) |

**کارکرد:** Total size to use for CircularBoundedJournal if created, it is valid only if seastore_main_device_type is RANDOM_BLOCK

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_cbjournal_size 5_G
ceph config get osd seastore_cbjournal_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_cold_tier_generations

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [seastore.md#SP_seastore_cold_tier_generations](../../../config/crimson/seastore.md#SP_seastore_cold_tier_generations) |

**کارکرد:** The number of generations in the cold tier if it exists.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_cold_tier_generations 3
ceph config get osd seastore_cold_tier_generations
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Size · default `0` · **Dev** |
| جدول | [seastore.md#SP_seastore_data_delta_based_overwrite](../../../config/crimson/seastore.md#SP_seastore_data_delta_based_overwrite) |

**کارکرد:** overwrite the existing data block based on delta if the overwrite size is equal to or less than the value, otherwise do overwrite based on remapping, set to 0 to enforce the remap-based overwrite.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_data_delta_based_overwrite 64
ceph config get osd seastore_data_delta_based_overwrite
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_default_max_object_size

| | |
|---|---|
| نوع | Uint · default `16777216` · **Dev** |
| جدول | [seastore.md#SP_seastore_default_max_object_size](../../../config/crimson/seastore.md#SP_seastore_default_max_object_size) |

**کارکرد:** default logical address space reservation for seastore objects' data

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_default_max_object_size 16777216
ceph config get osd seastore_default_max_object_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16777216`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_device_size

| | |
|---|---|
| نوع | Size · default `50_G` · **Dev** |
| جدول | [seastore.md#SP_seastore_device_size](../../../config/crimson/seastore.md#SP_seastore_device_size) |

**کارکرد:** Total size to use for SegmentManager block file if created

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_device_size 50_G
ceph config get osd seastore_device_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`50_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_disable_end_to_end_data_protection

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [seastore.md#SP_seastore_disable_end_to_end_data_protection](../../../config/crimson/seastore.md#SP_seastore_disable_end_to_end_data_protection) |

**کارکرد:** When false, upon mkfs, try to discover whether the nvme device supports internal checksum feature without using sever CPU then enable if available, set to true to disable unconditionally.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_disable_end_to_end_data_protection false
ceph config get osd seastore_disable_end_to_end_data_protection
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_full_integrity_check

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [seastore.md#SP_seastore_full_integrity_check](../../../config/crimson/seastore.md#SP_seastore_full_integrity_check) |

**کارکرد:** Whether seastore need to fully check the integrity of each extent, non-full integrity check means the integrity check might be skipped during extent remapping for better performance, disable with caution

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_full_integrity_check true
ceph config get osd seastore_full_integrity_check
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_hot_tier_generations

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [seastore.md#SP_seastore_hot_tier_generations](../../../config/crimson/seastore.md#SP_seastore_hot_tier_generations) |

**کارکرد:** The number of generations in the hot tier or the whole SeaStore instance if there's only one tier.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_hot_tier_generations 5
ceph config get osd seastore_hot_tier_generations
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `5`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Uint · default `16` · **Dev** |
| جدول | [seastore.md#SP_seastore_journal_batch_capacity](../../../config/crimson/seastore.md#SP_seastore_journal_batch_capacity) |

**کارکرد:** The number limit of records in a journal batch

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_journal_batch_capacity 16
ceph config get osd seastore_journal_batch_capacity
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_journal_batch_flush_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Dev** |
| جدول | [seastore.md#SP_seastore_journal_batch_flush_size](../../../config/crimson/seastore.md#SP_seastore_journal_batch_flush_size) |

**کارکرد:** The size threshold to force flush a journal batch

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_journal_batch_flush_size 16_M
ceph config get osd seastore_journal_batch_flush_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_journal_batch_preferred_fullness

| | |
|---|---|
| نوع | Float · default `0.95` · **Dev** |
| جدول | [seastore.md#SP_seastore_journal_batch_preferred_fullness](../../../config/crimson/seastore.md#SP_seastore_journal_batch_preferred_fullness) |

**کارکرد:** The record fullness threshold to flush a journal batch

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_journal_batch_preferred_fullness 0.95
ceph config get osd seastore_journal_batch_preferred_fullness
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.95`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_journal_iodepth_limit

| | |
|---|---|
| نوع | Uint · default `5` · **Dev** |
| جدول | [seastore.md#SP_seastore_journal_iodepth_limit](../../../config/crimson/seastore.md#SP_seastore_journal_iodepth_limit) |

**کارکرد:** The io depth limit to submit journal records

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_journal_iodepth_limit 5
ceph config get osd seastore_journal_iodepth_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_main_device_type

| | |
|---|---|
| نوع | Str · default `SSD` · **Dev** |
| جدول | [seastore.md#SP_seastore_main_device_type](../../../config/crimson/seastore.md#SP_seastore_main_device_type) |

**کارکرد:** The main device type seastore uses (SSD or RANDOM_BLOCK_SSD)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd seastore_main_device_type SSD
ceph config get osd seastore_main_device_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`SSD`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### seastore_max_concurrent_transactions

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [seastore.md#SP_seastore_max_concurrent_transactions](../../../config/crimson/seastore.md#SP_seastore_max_concurrent_transactions) |

**کارکرد:** maximum concurrent transactions that seastore allows (per reactor)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd seastore_max_concurrent_transactions 128
ceph config get osd seastore_max_concurrent_transactions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Size · default `0` · **Advanced** |
| جدول | [seastore.md#SP_seastore_max_data_allocation_size](../../../config/crimson/seastore.md#SP_seastore_max_data_allocation_size) |

**کارکرد:** Max size in bytes that an extent can be, 0 to disable

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd seastore_max_data_allocation_size 64
ceph config get osd seastore_max_data_allocation_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Float · default `0.6` · **Advanced** |
| جدول | [seastore.md#SP_seastore_multiple_tiers_default_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_default_evict_ratio) |

**کارکرد:** Begin evicting cold data to the cold tier when the used ratio of the main tier reaches this value.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_multiple_tiers_default_evict_ratio 0.6
ceph config get osd seastore_multiple_tiers_default_evict_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Float · default `0.7` · **Advanced** |
| جدول | [seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_fast_evict_ratio) |

**کارکرد:** Begin fast eviction when the used ratio of the main tier reaches this value.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_multiple_tiers_fast_evict_ratio 0.7
ceph config get osd seastore_multiple_tiers_fast_evict_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.7`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio](../../../config/crimson/seastore.md#SP_seastore_multiple_tiers_stop_evict_ratio) |

**کارکرد:** When the used ratio of main tier is less than this value, then stop evict cold data to the cold tier.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_multiple_tiers_stop_evict_ratio 0.5
ceph config get osd seastore_multiple_tiers_stop_evict_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Bool · default `True` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [seastore.md#SP_seastore_require_partition_count_match_reactor_count](../../../config/crimson/seastore.md#SP_seastore_require_partition_count_match_reactor_count) |

**کارکرد:** disable osd shards changes upon restart.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd seastore_require_partition_count_match_reactor_count false
ceph config get osd seastore_require_partition_count_match_reactor_count
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Bool · default `True` · **Advanced** |
| جدول | [seastore.md#SP_seastore_segment_cleaner_gc_autotune](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune) |

**کارکرد:** When the configured gc formula (cost_benefit or benefit) picks a segment whose free-space fraction (1 - utilization) is at least seastore_segment_cleaner_gc_autotune_ratio times smaller than the lowest-utilization candidate, override the pick with the greedy choice.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune false
ceph config get osd seastore_segment_cleaner_gc_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Float · default `2.0` · **Advanced** |
| جدول | [seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_autotune_ratio) |

**کارکرد:** Override threshold for the gc auto-tune. The configured formula's pick is overridden with the greedy candidate when greedy's free fraction is at least this ratio times the formula's pick's free fraction.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_segment_cleaner_gc_autotune_ratio 2.0
ceph config get osd seastore_segment_cleaner_gc_autotune_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2.0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1.0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Str · enum: ["greedy", "cost_benefit", "benefit"] · default `cost_benefit` · **Advanced** |
| جدول | [seastore.md#SP_seastore_segment_cleaner_gc_formula](../../../config/crimson/seastore.md#SP_seastore_segment_cleaner_gc_formula) |

**کارکرد:** The algorithm that SegmentCleaner will use to select segments to reclaim

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_segment_cleaner_gc_formula cost_benefit
ceph config get osd seastore_segment_cleaner_gc_formula
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `cost_benefit`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

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
| نوع | Size · default `64_M` · **Advanced** |
| جدول | [seastore.md#SP_seastore_segment_size](../../../config/crimson/seastore.md#SP_seastore_segment_size) |

**کارکرد:** Segment size to use for SegmentManager

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd seastore_segment_size 64_M
ceph config get osd seastore_segment_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd seastore_segment_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
