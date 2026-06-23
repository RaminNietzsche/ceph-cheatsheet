# Filestore

راهنمای عمیق پیکربندی Global — 84 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [filestore_apply_finisher_threads](#filestore_apply_finisher_threads) | `1` | Dev | توسعه |
| [filestore_blackhole](#filestore_blackhole) | `False` | Dev | توسعه |
| [filestore_btrfs_clone_range](#filestore_btrfs_clone_range) | `True` | Advanced | عملکرد |
| [filestore_btrfs_snap](#filestore_btrfs_snap) | `True` | Dev | توسعه |
| [filestore_caller_concurrency](#filestore_caller_concurrency) | `10` | Dev | توسعه |
| [filestore_collect_device_partition_information](#filestore_collect_device_partition_information) | `True` | Advanced | عملکرد |
| [filestore_commit_timeout](#filestore_commit_timeout) | `10_min` | Advanced | عملکرد |
| [filestore_debug_inject_read_err](#filestore_debug_inject_read_err) | `False` | Dev | توسعه |
| [filestore_debug_omap_check](#filestore_debug_omap_check) | `False` | Dev | توسعه |
| [filestore_debug_verify_split](#filestore_debug_verify_split) | `False` | Dev | توسعه |
| [filestore_dump_file](#filestore_dump_file) | `(empty)` | Dev | توسعه |
| [filestore_expected_throughput_bytes](#filestore_expected_throughput_bytes) | `209715200` | Advanced | عملکرد |
| [filestore_expected_throughput_ops](#filestore_expected_throughput_ops) | `200` | Advanced | عملکرد |
| [filestore_fadvise](#filestore_fadvise) | `True` | Advanced | عملکرد |
| [filestore_fail_eio](#filestore_fail_eio) | `True` | Dev | توسعه |
| [filestore_fd_cache_shards](#filestore_fd_cache_shards) | `16` | Dev | توسعه |
| [filestore_fd_cache_size](#filestore_fd_cache_size) | `128` | Dev | توسعه |
| [filestore_fiemap](#filestore_fiemap) | `False` | Advanced | عملکرد |
| [filestore_fiemap_threshold](#filestore_fiemap_threshold) | `4_K` | Dev | توسعه |
| [filestore_fsync_flushes_journal_data](#filestore_fsync_flushes_journal_data) | `False` | Dev | توسعه |
| [filestore_index_retry_probability](#filestore_index_retry_probability) | `0` | Dev | توسعه |
| [filestore_inject_stall](#filestore_inject_stall) | `0` | Dev | توسعه |
| [filestore_journal_parallel](#filestore_journal_parallel) | `False` | Dev | توسعه |
| [filestore_journal_trailing](#filestore_journal_trailing) | `False` | Dev | توسعه |
| [filestore_journal_writeahead](#filestore_journal_writeahead) | `False` | Dev | توسعه |
| [filestore_kill_at](#filestore_kill_at) | `0` | Dev | توسعه |
| [filestore_max_alloc_hint_size](#filestore_max_alloc_hint_size) | `1_M` | Dev | توسعه |
| [filestore_max_inline_xattr_size](#filestore_max_inline_xattr_size) | `0` | Dev | توسعه |
| [filestore_max_inline_xattr_size_btrfs](#filestore_max_inline_xattr_size_btrfs) | `2_K` | Dev | توسعه |
| [filestore_max_inline_xattr_size_other](#filestore_max_inline_xattr_size_other) | `512` | Dev | توسعه |
| [filestore_max_inline_xattr_size_xfs](#filestore_max_inline_xattr_size_xfs) | `64_K` | Dev | توسعه |
| [filestore_max_inline_xattrs](#filestore_max_inline_xattrs) | `0` | Dev | توسعه |
| [filestore_max_inline_xattrs_btrfs](#filestore_max_inline_xattrs_btrfs) | `10` | Dev | توسعه |
| [filestore_max_inline_xattrs_other](#filestore_max_inline_xattrs_other) | `2` | Dev | توسعه |
| [filestore_max_inline_xattrs_xfs](#filestore_max_inline_xattrs_xfs) | `10` | Dev | توسعه |
| [filestore_max_sync_interval](#filestore_max_sync_interval) | `5` | Advanced | عملکرد |
| [filestore_max_xattr_value_size](#filestore_max_xattr_value_size) | `0` | Dev | توسعه |
| [filestore_max_xattr_value_size_btrfs](#filestore_max_xattr_value_size_btrfs) | `64_K` | Dev | توسعه |
| [filestore_max_xattr_value_size_other](#filestore_max_xattr_value_size_other) | `1_K` | Dev | توسعه |
| [filestore_max_xattr_value_size_xfs](#filestore_max_xattr_value_size_xfs) | `64_K` | Dev | توسعه |
| [filestore_merge_threshold](#filestore_merge_threshold) | `-10` | Dev | توسعه |
| [filestore_min_sync_interval](#filestore_min_sync_interval) | `0.01` | Dev | توسعه |
| [filestore_odsync_write](#filestore_odsync_write) | `False` | Dev | توسعه |
| [filestore_omap_backend](#filestore_omap_backend) | `rocksdb` | Dev | توسعه |
| [filestore_omap_backend_path](#filestore_omap_backend_path) | `(empty)` | Dev | توسعه |
| [filestore_omap_header_cache_size](#filestore_omap_header_cache_size) | `1_K` | Dev | توسعه |
| [filestore_ondisk_finisher_threads](#filestore_ondisk_finisher_threads) | `1` | Dev | توسعه |
| [filestore_op_thread_suicide_timeout](#filestore_op_thread_suicide_timeout) | `3_min` | Advanced | عملکرد |
| [filestore_op_thread_timeout](#filestore_op_thread_timeout) | `1_min` | Advanced | عملکرد |
| [filestore_op_threads](#filestore_op_threads) | `2` | Advanced | عملکرد |
| [filestore_punch_hole](#filestore_punch_hole) | `False` | Advanced | عملکرد |
| [filestore_queue_high_delay_multiple](#filestore_queue_high_delay_multiple) | `0` | Dev | توسعه |
| [filestore_queue_high_delay_multiple_bytes](#filestore_queue_high_delay_multiple_bytes) | `0` | Dev | توسعه |
| [filestore_queue_high_delay_multiple_ops](#filestore_queue_high_delay_multiple_ops) | `0` | Dev | توسعه |
| [filestore_queue_high_threshhold](#filestore_queue_high_threshhold) | `0.9` | Dev | توسعه |
| [filestore_queue_low_threshhold](#filestore_queue_low_threshhold) | `0.3` | Dev | توسعه |
| [filestore_queue_max_bytes](#filestore_queue_max_bytes) | `100_M` | Advanced | عملکرد |
| [filestore_queue_max_delay_multiple](#filestore_queue_max_delay_multiple) | `0` | Dev | توسعه |
| [filestore_queue_max_delay_multiple_bytes](#filestore_queue_max_delay_multiple_bytes) | `0` | Dev | توسعه |
| [filestore_queue_max_delay_multiple_ops](#filestore_queue_max_delay_multiple_ops) | `0` | Dev | توسعه |
| [filestore_queue_max_ops](#filestore_queue_max_ops) | `50` | Advanced | عملکرد |
| [filestore_rocksdb_options](#filestore_rocksdb_options) | `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` | Dev | توسعه |
| [filestore_seek_data_hole](#filestore_seek_data_hole) | `False` | Advanced | عملکرد |
| [filestore_sloppy_crc](#filestore_sloppy_crc) | `False` | Dev | توسعه |
| [filestore_sloppy_crc_block_size](#filestore_sloppy_crc_block_size) | `64_K` | Dev | توسعه |
| [filestore_splice](#filestore_splice) | `False` | Advanced | عملکرد |
| [filestore_split_multiple](#filestore_split_multiple) | `2` | Dev | توسعه |
| [filestore_split_rand_factor](#filestore_split_rand_factor) | `20` | Dev | توسعه |
| [filestore_update_to](#filestore_update_to) | `1000` | Dev | توسعه |
| [filestore_wbthrottle_btrfs_bytes_hard_limit](#filestore_wbthrottle_btrfs_bytes_hard_limit) | `400_M` | Advanced | عملکرد |
| [filestore_wbthrottle_btrfs_bytes_start_flusher](#filestore_wbthrottle_btrfs_bytes_start_flusher) | `40_M` | Advanced | عملکرد |
| [filestore_wbthrottle_btrfs_inodes_hard_limit](#filestore_wbthrottle_btrfs_inodes_hard_limit) | `5000` | Advanced | عملکرد |
| [filestore_wbthrottle_btrfs_inodes_start_flusher](#filestore_wbthrottle_btrfs_inodes_start_flusher) | `500` | Advanced | عملکرد |
| [filestore_wbthrottle_btrfs_ios_hard_limit](#filestore_wbthrottle_btrfs_ios_hard_limit) | `5000` | Advanced | عملکرد |
| [filestore_wbthrottle_btrfs_ios_start_flusher](#filestore_wbthrottle_btrfs_ios_start_flusher) | `500` | Advanced | عملکرد |
| [filestore_wbthrottle_enable](#filestore_wbthrottle_enable) | `True` | Advanced | سیاست |
| [filestore_wbthrottle_xfs_bytes_hard_limit](#filestore_wbthrottle_xfs_bytes_hard_limit) | `400_M` | Advanced | عملکرد |
| [filestore_wbthrottle_xfs_bytes_start_flusher](#filestore_wbthrottle_xfs_bytes_start_flusher) | `40_M` | Advanced | عملکرد |
| [filestore_wbthrottle_xfs_inodes_hard_limit](#filestore_wbthrottle_xfs_inodes_hard_limit) | `5000` | Advanced | عملکرد |
| [filestore_wbthrottle_xfs_inodes_start_flusher](#filestore_wbthrottle_xfs_inodes_start_flusher) | `500` | Advanced | عملکرد |
| [filestore_wbthrottle_xfs_ios_hard_limit](#filestore_wbthrottle_xfs_ios_hard_limit) | `5000` | Advanced | عملکرد |
| [filestore_wbthrottle_xfs_ios_start_flusher](#filestore_wbthrottle_xfs_ios_start_flusher) | `500` | Advanced | عملکرد |
| [filestore_xfs_extsize](#filestore_xfs_extsize) | `False` | Advanced | عملکرد |
| [filestore_zfs_snap](#filestore_zfs_snap) | `False` | Dev | توسعه |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### filestore_apply_finisher_threads

| | |
|---|---|
| نوع | Int · default `1` · **Dev** |
| جدول | [filestore.md#SP_filestore_apply_finisher_threads](../../../config/global/filestore.md#SP_filestore_apply_finisher_threads) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_apply_finisher_threads 1
ceph config get global filestore_apply_finisher_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_blackhole

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_blackhole](../../../config/global/filestore.md#SP_filestore_blackhole) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_blackhole true
ceph config get global filestore_blackhole
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_btrfs_clone_range

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [filestore.md#SP_filestore_btrfs_clone_range](../../../config/global/filestore.md#SP_filestore_btrfs_clone_range) |

**کارکرد:** Use btrfs clone_range ioctl to efficiently duplicate objects (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global filestore_btrfs_clone_range false
ceph config get global filestore_btrfs_clone_range
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_btrfs_clone_range
ceph -s
```

---

### filestore_btrfs_snap

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [filestore.md#SP_filestore_btrfs_snap](../../../config/global/filestore.md#SP_filestore_btrfs_snap) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_btrfs_snap false
ceph config get global filestore_btrfs_snap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_caller_concurrency

| | |
|---|---|
| نوع | Int · default `10` · **Dev** |
| جدول | [filestore.md#SP_filestore_caller_concurrency](../../../config/global/filestore.md#SP_filestore_caller_concurrency) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_caller_concurrency 10
ceph config get global filestore_caller_concurrency
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_collect_device_partition_information

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [filestore.md#SP_filestore_collect_device_partition_information](../../../config/global/filestore.md#SP_filestore_collect_device_partition_information) |

**کارکرد:** Collect metadata about the backing file system on OSD startup (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global filestore_collect_device_partition_information false
ceph config get global filestore_collect_device_partition_information
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_collect_device_partition_information
ceph -s
```

---

### filestore_commit_timeout

| | |
|---|---|
| نوع | Float · default `10_min` · **Advanced** |
| جدول | [filestore.md#SP_filestore_commit_timeout](../../../config/global/filestore.md#SP_filestore_commit_timeout) |

**کارکرد:** Seconds before backing file system is considered hung (deprecated)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global filestore_commit_timeout 10_min
ceph config get global filestore_commit_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_commit_timeout
ceph -s
```

---

### filestore_debug_inject_read_err

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_debug_inject_read_err](../../../config/global/filestore.md#SP_filestore_debug_inject_read_err) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_debug_inject_read_err true
ceph config get global filestore_debug_inject_read_err
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_debug_omap_check

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_debug_omap_check](../../../config/global/filestore.md#SP_filestore_debug_omap_check) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_debug_omap_check true
ceph config get global filestore_debug_omap_check
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_debug_verify_split

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_debug_verify_split](../../../config/global/filestore.md#SP_filestore_debug_verify_split) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_debug_verify_split true
ceph config get global filestore_debug_verify_split
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_dump_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [filestore.md#SP_filestore_dump_file](../../../config/global/filestore.md#SP_filestore_dump_file) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_dump_file "example"
ceph config get global filestore_dump_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_expected_throughput_bytes

| | |
|---|---|
| نوع | Float · default `209715200` · **Advanced** |
| جدول | [filestore.md#SP_filestore_expected_throughput_bytes](../../../config/global/filestore.md#SP_filestore_expected_throughput_bytes) |

**کارکرد:** Expected throughput of backend device (aids throttling calculations) (deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_expected_throughput_bytes 209715200
ceph config get global filestore_expected_throughput_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `209715200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_expected_throughput_bytes
ceph -s
```

---

### filestore_expected_throughput_ops

| | |
|---|---|
| نوع | Float · default `200` · **Advanced** |
| جدول | [filestore.md#SP_filestore_expected_throughput_ops](../../../config/global/filestore.md#SP_filestore_expected_throughput_ops) |

**کارکرد:** Expected through of backend device in IOPS (aids throttling calculations) (deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_expected_throughput_ops 200
ceph config get global filestore_expected_throughput_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_expected_throughput_ops
ceph -s
```

---

### filestore_fadvise

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [filestore.md#SP_filestore_fadvise](../../../config/global/filestore.md#SP_filestore_fadvise) |

**کارکرد:** Use posix_fadvise(2) to pass hints to file system (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global filestore_fadvise false
ceph config get global filestore_fadvise
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_fadvise
ceph -s
```

---

### filestore_fail_eio

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [filestore.md#SP_filestore_fail_eio](../../../config/global/filestore.md#SP_filestore_fail_eio) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_fail_eio false
ceph config get global filestore_fail_eio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_fd_cache_shards

| | |
|---|---|
| نوع | Int · default `16` · **Dev** |
| جدول | [filestore.md#SP_filestore_fd_cache_shards](../../../config/global/filestore.md#SP_filestore_fd_cache_shards) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_fd_cache_shards 16
ceph config get global filestore_fd_cache_shards
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_fd_cache_size

| | |
|---|---|
| نوع | Int · default `128` · **Dev** |
| جدول | [filestore.md#SP_filestore_fd_cache_size](../../../config/global/filestore.md#SP_filestore_fd_cache_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_fd_cache_size 128
ceph config get global filestore_fd_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`128`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_fiemap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [filestore.md#SP_filestore_fiemap](../../../config/global/filestore.md#SP_filestore_fiemap) |

**کارکرد:** Use fiemap ioctl(2) to determine which parts of objects are sparse (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global filestore_fiemap true
ceph config get global filestore_fiemap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_fiemap
ceph -s
```

---

### filestore_fiemap_threshold

| | |
|---|---|
| نوع | Size · default `4_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_fiemap_threshold](../../../config/global/filestore.md#SP_filestore_fiemap_threshold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_fiemap_threshold 4_K
ceph config get global filestore_fiemap_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`4_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_fsync_flushes_journal_data

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_fsync_flushes_journal_data](../../../config/global/filestore.md#SP_filestore_fsync_flushes_journal_data) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_fsync_flushes_journal_data true
ceph config get global filestore_fsync_flushes_journal_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_index_retry_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_index_retry_probability](../../../config/global/filestore.md#SP_filestore_index_retry_probability) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_index_retry_probability 0
ceph config get global filestore_index_retry_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_inject_stall

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_inject_stall](../../../config/global/filestore.md#SP_filestore_inject_stall) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_inject_stall 64
ceph config get global filestore_inject_stall
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_journal_parallel

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_journal_parallel](../../../config/global/filestore.md#SP_filestore_journal_parallel) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_journal_parallel true
ceph config get global filestore_journal_parallel
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_journal_trailing

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_journal_trailing](../../../config/global/filestore.md#SP_filestore_journal_trailing) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_journal_trailing true
ceph config get global filestore_journal_trailing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_journal_writeahead

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_journal_writeahead](../../../config/global/filestore.md#SP_filestore_journal_writeahead) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_journal_writeahead true
ceph config get global filestore_journal_writeahead
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_kill_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_kill_at](../../../config/global/filestore.md#SP_filestore_kill_at) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_kill_at 64
ceph config get global filestore_kill_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_alloc_hint_size

| | |
|---|---|
| نوع | Size · default `1_M` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_alloc_hint_size](../../../config/global/filestore.md#SP_filestore_max_alloc_hint_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_alloc_hint_size 1_M
ceph config get global filestore_max_alloc_hint_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattr_size

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattr_size](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattr_size 64
ceph config get global filestore_max_inline_xattr_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattr_size_btrfs

| | |
|---|---|
| نوع | Size · default `2_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattr_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_btrfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattr_size_btrfs 2_K
ceph config get global filestore_max_inline_xattr_size_btrfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattr_size_other

| | |
|---|---|
| نوع | Size · default `512` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattr_size_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_other) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattr_size_other 512
ceph config get global filestore_max_inline_xattr_size_other
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`512`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattr_size_xfs

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattr_size_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattr_size_xfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattr_size_xfs 64_K
ceph config get global filestore_max_inline_xattr_size_xfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattrs

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattrs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattrs 64
ceph config get global filestore_max_inline_xattrs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattrs_btrfs

| | |
|---|---|
| نوع | Uint · default `10` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattrs_btrfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_btrfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattrs_btrfs 10
ceph config get global filestore_max_inline_xattrs_btrfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattrs_other

| | |
|---|---|
| نوع | Uint · default `2` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattrs_other](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_other) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattrs_other 2
ceph config get global filestore_max_inline_xattrs_other
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_inline_xattrs_xfs

| | |
|---|---|
| نوع | Uint · default `10` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_inline_xattrs_xfs](../../../config/global/filestore.md#SP_filestore_max_inline_xattrs_xfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_inline_xattrs_xfs 10
ceph config get global filestore_max_inline_xattrs_xfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_sync_interval

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [filestore.md#SP_filestore_max_sync_interval](../../../config/global/filestore.md#SP_filestore_max_sync_interval) |

**کارکرد:** Period between calls to syncfs(2) and journal trims (seconds)(Deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_max_sync_interval 5
ceph config get global filestore_max_sync_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_max_sync_interval
ceph -s
```

---

### filestore_max_xattr_value_size

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_xattr_value_size](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_xattr_value_size 64
ceph config get global filestore_max_xattr_value_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_xattr_value_size_btrfs

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_xattr_value_size_btrfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_btrfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_xattr_value_size_btrfs 64_K
ceph config get global filestore_max_xattr_value_size_btrfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_xattr_value_size_other

| | |
|---|---|
| نوع | Size · default `1_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_xattr_value_size_other](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_other) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_xattr_value_size_other 1_K
ceph config get global filestore_max_xattr_value_size_other
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_max_xattr_value_size_xfs

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_max_xattr_value_size_xfs](../../../config/global/filestore.md#SP_filestore_max_xattr_value_size_xfs) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_max_xattr_value_size_xfs 64_K
ceph config get global filestore_max_xattr_value_size_xfs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_merge_threshold

| | |
|---|---|
| نوع | Int · default `-10` · **Dev** |
| جدول | [filestore.md#SP_filestore_merge_threshold](../../../config/global/filestore.md#SP_filestore_merge_threshold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_merge_threshold -10
ceph config get global filestore_merge_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`-10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_min_sync_interval

| | |
|---|---|
| نوع | Float · default `0.01` · **Dev** |
| جدول | [filestore.md#SP_filestore_min_sync_interval](../../../config/global/filestore.md#SP_filestore_min_sync_interval) |

**کارکرد:** Minimum period between calls to syncfs(2) (deprecated)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_min_sync_interval 0.01
ceph config get global filestore_min_sync_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.01`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_odsync_write

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_odsync_write](../../../config/global/filestore.md#SP_filestore_odsync_write) |

**کارکرد:** Write with O_DSYNC (deprecated)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_odsync_write true
ceph config get global filestore_odsync_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_omap_backend

| | |
|---|---|
| نوع | Str · enum: ["leveldb", "rocksdb"] · default `rocksdb` · **Dev** |
| جدول | [filestore.md#SP_filestore_omap_backend](../../../config/global/filestore.md#SP_filestore_omap_backend) |

**کارکرد:** The KeyValueDB to use for Filestore metadata (that is, omaps) (deprecated).

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_omap_backend rocksdb
ceph config get global filestore_omap_backend
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`rocksdb`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_omap_backend_path

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [filestore.md#SP_filestore_omap_backend_path](../../../config/global/filestore.md#SP_filestore_omap_backend_path) |

**کارکرد:** The path where the Filestore KeyValueDB should store its database(s) (deprecated)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_omap_backend_path "/var/lib/ceph/example"
ceph config get global filestore_omap_backend_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_omap_header_cache_size

| | |
|---|---|
| نوع | Size · default `1_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_omap_header_cache_size](../../../config/global/filestore.md#SP_filestore_omap_header_cache_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_omap_header_cache_size 1_K
ceph config get global filestore_omap_header_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_ondisk_finisher_threads

| | |
|---|---|
| نوع | Int · default `1` · **Dev** |
| جدول | [filestore.md#SP_filestore_ondisk_finisher_threads](../../../config/global/filestore.md#SP_filestore_ondisk_finisher_threads) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_ondisk_finisher_threads 1
ceph config get global filestore_ondisk_finisher_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_op_thread_suicide_timeout

| | |
|---|---|
| نوع | Int · default `3_min` · **Advanced** |
| جدول | [filestore.md#SP_filestore_op_thread_suicide_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_suicide_timeout) |

**کارکرد:** Seconds before a worker thread is considered dead (deprecated)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global filestore_op_thread_suicide_timeout 3_min
ceph config get global filestore_op_thread_suicide_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_op_thread_suicide_timeout
ceph -s
```

---

### filestore_op_thread_timeout

| | |
|---|---|
| نوع | Int · default `1_min` · **Advanced** |
| جدول | [filestore.md#SP_filestore_op_thread_timeout](../../../config/global/filestore.md#SP_filestore_op_thread_timeout) |

**کارکرد:** Seconds before a worker thread is considered stalled (deprecated)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global filestore_op_thread_timeout 1_min
ceph config get global filestore_op_thread_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_op_thread_timeout
ceph -s
```

---

### filestore_op_threads

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [filestore.md#SP_filestore_op_threads](../../../config/global/filestore.md#SP_filestore_op_threads) |

**کارکرد:** Threads used to apply changes to backing file system (deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_op_threads 2
ceph config get global filestore_op_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_op_threads
ceph -s
```

---

### filestore_punch_hole

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [filestore.md#SP_filestore_punch_hole](../../../config/global/filestore.md#SP_filestore_punch_hole) |

**کارکرد:** Use fallocate(2) FALLOC_FL_PUNCH_HOLE to efficiently zero ranges of objects (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global filestore_punch_hole true
ceph config get global filestore_punch_hole
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_punch_hole
ceph -s
```

---

### filestore_queue_high_delay_multiple

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_high_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_high_delay_multiple 0
ceph config get global filestore_queue_high_delay_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_high_delay_multiple_bytes

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_high_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_bytes) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_high_delay_multiple_bytes 0
ceph config get global filestore_queue_high_delay_multiple_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_high_delay_multiple_ops

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_high_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_high_delay_multiple_ops) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_high_delay_multiple_ops 0
ceph config get global filestore_queue_high_delay_multiple_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_high_threshhold

| | |
|---|---|
| نوع | Float · default `0.9` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_high_threshhold](../../../config/global/filestore.md#SP_filestore_queue_high_threshhold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_high_threshhold 0.9
ceph config get global filestore_queue_high_threshhold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.9`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_low_threshhold

| | |
|---|---|
| نوع | Float · default `0.3` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_low_threshhold](../../../config/global/filestore.md#SP_filestore_queue_low_threshhold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_low_threshhold 0.3
ceph config get global filestore_queue_low_threshhold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.3`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_max_bytes

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [filestore.md#SP_filestore_queue_max_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_bytes) |

**کارکرد:** Max (written) bytes in flight (deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_queue_max_bytes 100_M
ceph config get global filestore_queue_max_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_queue_max_bytes
ceph -s
```

---

### filestore_queue_max_delay_multiple

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_max_delay_multiple](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_max_delay_multiple 0
ceph config get global filestore_queue_max_delay_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_max_delay_multiple_bytes

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_max_delay_multiple_bytes](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_bytes) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_max_delay_multiple_bytes 0
ceph config get global filestore_queue_max_delay_multiple_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_max_delay_multiple_ops

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [filestore.md#SP_filestore_queue_max_delay_multiple_ops](../../../config/global/filestore.md#SP_filestore_queue_max_delay_multiple_ops) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_queue_max_delay_multiple_ops 0
ceph config get global filestore_queue_max_delay_multiple_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_queue_max_ops

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [filestore.md#SP_filestore_queue_max_ops](../../../config/global/filestore.md#SP_filestore_queue_max_ops) |

**کارکرد:** Max IO operations in flight (deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_queue_max_ops 50
ceph config get global filestore_queue_max_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_queue_max_ops
ceph -s
```

---

### filestore_rocksdb_options

| | |
|---|---|
| نوع | Str · default `max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression` · **Dev** |
| جدول | [filestore.md#SP_filestore_rocksdb_options](../../../config/global/filestore.md#SP_filestore_rocksdb_options) |

**کارکرد:** Options to pass through when RocksDB is used as the KeyValueDB for (deprecated) Filestore.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_rocksdb_options "max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression"
ceph config get global filestore_rocksdb_options
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`max_background_jobs=10,compaction_readahead_size=2097152,compression=kNoCompression`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_seek_data_hole

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [filestore.md#SP_filestore_seek_data_hole](../../../config/global/filestore.md#SP_filestore_seek_data_hole) |

**کارکرد:** Use lseek(2) SEEK_HOLE and SEEK_DATA to determine which parts of objects are sparse (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global filestore_seek_data_hole true
ceph config get global filestore_seek_data_hole
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_seek_data_hole
ceph -s
```

---

### filestore_sloppy_crc

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_sloppy_crc](../../../config/global/filestore.md#SP_filestore_sloppy_crc) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_sloppy_crc true
ceph config get global filestore_sloppy_crc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_sloppy_crc_block_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [filestore.md#SP_filestore_sloppy_crc_block_size](../../../config/global/filestore.md#SP_filestore_sloppy_crc_block_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_sloppy_crc_block_size 64_K
ceph config get global filestore_sloppy_crc_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_splice

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [filestore.md#SP_filestore_splice](../../../config/global/filestore.md#SP_filestore_splice) |

**کارکرد:** Use splice(2) to more efficiently copy data between files (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global filestore_splice true
ceph config get global filestore_splice
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_splice
ceph -s
```

---

### filestore_split_multiple

| | |
|---|---|
| نوع | Int · default `2` · **Dev** |
| جدول | [filestore.md#SP_filestore_split_multiple](../../../config/global/filestore.md#SP_filestore_split_multiple) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_split_multiple 2
ceph config get global filestore_split_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_split_rand_factor

| | |
|---|---|
| نوع | Uint · default `20` · **Dev** |
| جدول | [filestore.md#SP_filestore_split_rand_factor](../../../config/global/filestore.md#SP_filestore_split_rand_factor) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_split_rand_factor 20
ceph config get global filestore_split_rand_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`20`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_update_to

| | |
|---|---|
| نوع | Int · default `1000` · **Dev** |
| جدول | [filestore.md#SP_filestore_update_to](../../../config/global/filestore.md#SP_filestore_update_to) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_update_to 1000
ceph config get global filestore_update_to
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### filestore_wbthrottle_btrfs_bytes_hard_limit

| | |
|---|---|
| نوع | Size · default `400_M` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_hard_limit) |

**کارکرد:** Block writes when this many bytes haven't been flushed (fsynced) (btrfs, deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `400_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_bytes_start_flusher

| | |
|---|---|
| نوع | Size · default `40_M` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_bytes_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many bytes are written (btrfs, deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `40_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_hard_limit

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_hard_limit) |

**کارکرد:** Block writing when this many inodes have outstanding writes (btrfs, deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_inodes_start_flusher

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_inodes_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many distinct inodes have been modified (deprecated) (btrfs)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_hard_limit

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_hard_limit) |

**کارکرد:** Block writes when this many IOs haven't been flushed (fsynced) (btrfs,deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_btrfs_ios_start_flusher

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_btrfs_ios_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many IOs are written (brtrfs, deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_btrfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_btrfs_ios_start_flusher
ceph -s
```

---

### filestore_wbthrottle_enable

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_enable](../../../config/global/filestore.md#SP_filestore_wbthrottle_enable) |

**کارکرد:** Enabling throttling of operations to backing file system (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_enable false
ceph config get global filestore_wbthrottle_enable
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_enable
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_hard_limit

| | |
|---|---|
| نوع | Size · default `400_M` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_hard_limit) |

**کارکرد:** Block writes when this many bytes haven't been flushed (fsynced) (xfs, deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_hard_limit 400_M
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `400_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_bytes_start_flusher

| | |
|---|---|
| نوع | Size · default `40_M` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_bytes_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many bytes are written (xfs, deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_bytes_start_flusher 40_M
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `40_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_bytes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_hard_limit

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_hard_limit) |

**کارکرد:** Block writing when this many inodes have outstanding writes (xfs, deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_inodes_start_flusher

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_inodes_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many distinct inodes have been modified (xfs, deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_inodes_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_inodes_start_flusher
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_hard_limit

| | |
|---|---|
| نوع | Uint · default `5000` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_hard_limit) |

**کارکرد:** Block writes when this many IOs haven't been flushed (fsynced) (xfs, deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_hard_limit 5000
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_ios_hard_limit
ceph -s
```

---

### filestore_wbthrottle_xfs_ios_start_flusher

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher](../../../config/global/filestore.md#SP_filestore_wbthrottle_xfs_ios_start_flusher) |

**کارکرد:** Start flushing (fsyncing) when this many IOs are written (xfs, deprecated)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global filestore_wbthrottle_xfs_ios_start_flusher 500
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_wbthrottle_xfs_ios_start_flusher
ceph -s
```

---

### filestore_xfs_extsize

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [filestore.md#SP_filestore_xfs_extsize](../../../config/global/filestore.md#SP_filestore_xfs_extsize) |

**کارکرد:** Use XFS extsize ioctl(2) to hint allocator about expected write sizes (deprecated)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global filestore_xfs_extsize true
ceph config get global filestore_xfs_extsize
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global filestore_xfs_extsize
ceph -s
```

---

### filestore_zfs_snap

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [filestore.md#SP_filestore_zfs_snap](../../../config/global/filestore.md#SP_filestore_zfs_snap) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global filestore_zfs_snap true
ceph config get global filestore_zfs_snap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
