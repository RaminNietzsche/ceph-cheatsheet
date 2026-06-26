# CephFS mirror

راهنمای عمیق پیکربندی CephFS mirror — 15 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/cephfs-mirror/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cephfs_mirror_action_update_interval](#cephfs_mirror_action_update_interval) | `2` | Advanced | عملکرد |
| [cephfs_mirror_blockdiff_min_file_size](#cephfs_mirror_blockdiff_min_file_size) | `16_M` | Advanced | عملکرد |
| [cephfs_mirror_datasync_files_per_batch](#cephfs_mirror_datasync_files_per_batch) | `64` | Advanced | عملکرد |
| [cephfs_mirror_directory_scan_interval](#cephfs_mirror_directory_scan_interval) | `10` | Advanced | عملکرد |
| [cephfs_mirror_distribute_datasync_threads](#cephfs_mirror_distribute_datasync_threads) | `True` | Advanced | عملکرد |
| [cephfs_mirror_max_concurrent_directory_syncs](#cephfs_mirror_max_concurrent_directory_syncs) | `3` | Advanced | عملکرد |
| [cephfs_mirror_max_consecutive_failures_per_directory](#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | Advanced | عملکرد |
| [cephfs_mirror_max_datasync_threads](#cephfs_mirror_max_datasync_threads) | `6` | Advanced | عملکرد |
| [cephfs_mirror_max_snapshot_sync_per_cycle](#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | Advanced | عملکرد |
| [cephfs_mirror_mount_timeout](#cephfs_mirror_mount_timeout) | `10` | Advanced | عملکرد |
| [cephfs_mirror_perf_stats_prio](#cephfs_mirror_perf_stats_prio) | `5` | Advanced | عملکرد |
| [cephfs_mirror_restart_mirror_on_blocklist_interval](#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | Advanced | عملکرد |
| [cephfs_mirror_restart_mirror_on_failure_interval](#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | Advanced | عملکرد |
| [cephfs_mirror_retry_failed_directories_interval](#cephfs_mirror_retry_failed_directories_interval) | `60` | Advanced | عملکرد |
| [cephfs_mirror_tick_interval](#cephfs_mirror_tick_interval) | `5` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. cephfs-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephfs_mirror_action_update_interval

| | |
|---|---|
| نوع | Secs · default `2` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_action_update_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_action_update_interval) |

**کارکرد:** interval for driving asynchronous mirror actions Interval in seconds to process pending mirror update actions.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_action_update_interval 2
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
ceph -s
```

---

### cephfs_mirror_blockdiff_min_file_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_blockdiff_min_file_size) |

**کارکرد:** minimum file size threshold in bytes above which block-level diff is used during CephFS mirroring. defines the minimum file size, in bytes, required for CephFS mirroring to use block-level delta synchronization instead of performing a full file copy. When a file’s size is greater than to this threshold, the mirroring engine attempts to synchronize only the modified block extents between snapshots. For files smaller than or equal to this value, a full file copy is performed instead, as block-level diff may not provide meaningful performance benefits for small files.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_blockdiff_min_file_size 16_M
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
ceph -s
```

---

### cephfs_mirror_datasync_files_per_batch

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_datasync_files_per_batch](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_datasync_files_per_batch) |

**کارکرد:** maximum number of files processed by datasync threads per scheduling cycle before yielding. defines the maximum number of files a data synchronization thread will process for a specific snapshot before yielding the thread to re-check scheduling logic. This is applicable only when cephfs_mirror_distribute_datasync_threads is enabled. This batch size determines the granularity of thread distribution; smaller batches allow threads to rotate between snapshots more frequently, while larger batches improve throughput by minimizing the overhead of thread re-assignment.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_datasync_files_per_batch 64
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
ceph -s
```

---

### cephfs_mirror_directory_scan_interval

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_directory_scan_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_directory_scan_interval) |

**کارکرد:** interval to scan directories to mirror snapshots interval in seconds to scan configured directories for snapshot mirroring.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_directory_scan_interval 10
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
ceph -s
```

---

### cephfs_mirror_distribute_datasync_threads

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_distribute_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_distribute_datasync_threads) |

**کارکرد:** distribute data synchronization threads evenly across multiple snapshots. controls how datasync worker threads are scheduled when multiple snapshots are queued for synchronization. When enabled, worker threads are distributed fairly across active snapshots, preventing a single large snapshot from monopolizing all available threads and causing other snapshots to starve. When disabled, datasync threads process one snapshot until completion before switching to another, which can improve throughput for individual large snapshots but may increase latency for other queued snapshots. Enabling this option improves responsiveness and reduces starvation in environments where multiple directories are configured to be mirrored.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_distribute_datasync_threads false
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_concurrent_directory_syncs

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_concurrent_directory_syncs) |

**کارکرد:** maximum number of concurrent snapshot synchronization crawler threads maximum number of directory snapshots that can be crawled concurrently by cephfs-mirror daemon. Controls the number of synchronization crawler threads. Note that the crawler threads also does entry operations like directory creations, file deletes and snapshot deletes/renames.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs 3
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
ceph -s
```

---

### cephfs_mirror_max_consecutive_failures_per_directory

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_consecutive_failures_per_directory) |

**کارکرد:** consecutive failed directory synchronization attempts before marking a directory as "failed" number of consecutive snapshot synchronization failures to mark a directory as "failed". failed directories are retried for synchronization less frequently.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory 10
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
ceph -s
```

---

### cephfs_mirror_max_datasync_threads

| | |
|---|---|
| نوع | Uint · default `6` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_max_datasync_threads](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_datasync_threads) |

**کارکرد:** maximum number of concurrent snapshot data synchronization threads specifies the maximum number of worker threads in the CephFS mirror data synchronization thread pool. These threads process file synchronization tasks produced by crawler threads for mirrored directory snapshots.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_datasync_threads 6
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
ceph -s
```

---

### cephfs_mirror_max_snapshot_sync_per_cycle

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_max_snapshot_sync_per_cycle) |

**کارکرد:** number of snapshots to mirror in one cycle maximum number of snapshots to mirror when a directory is picked up for mirroring by worker threads.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle 3
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
ceph -s
```

---

### cephfs_mirror_mount_timeout

| | |
|---|---|
| نوع | Secs · default `10` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_mount_timeout](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_mount_timeout) |

**کارکرد:** timeout for mounting primary/secondary ceph file system Timeout in seconds for mounting primary or secondary (remote) ceph file system by the cephfs-mirror daemon. Setting this to a higher value could result in the mirror daemon getting stalled when mounting a file system if the cluster is not reachable. This option is used to override the usual client_mount_timeout.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_mount_timeout 10
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
ceph -s
```

---

### cephfs_mirror_perf_stats_prio

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_perf_stats_prio](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_perf_stats_prio) |

**کارکرد:** Priority level for mirror daemon replication perf counters The daemon will send perf counter data to the manager daemon if the priority is not lower than mgr_stats_threshold.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_perf_stats_prio 5
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `11`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_blocklist_interval

| | |
|---|---|
| نوع | Secs · default `30` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_blocklist_interval) |

**کارکرد:** interval to restart blocklisted instances Interval in seconds to restart blocklisted mirror instances. Setting to zero (0) disables restarting blocklisted instances.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval 30
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
ceph -s
```

---

### cephfs_mirror_restart_mirror_on_failure_interval

| | |
|---|---|
| نوع | Secs · default `20` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_restart_mirror_on_failure_interval) |

**کارکرد:** interval to restart failed mirror instances Interval in seconds to restart failed mirror instances. Setting to zero (0) disables restarting failed mirror instances.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval 20
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
ceph -s
```

---

### cephfs_mirror_retry_failed_directories_interval

| | |
|---|---|
| نوع | Uint · default `60` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_retry_failed_directories_interval) |

**کارکرد:** failed directory retry interval for synchronization interval in seconds to retry synchronization for failed directories.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_retry_failed_directories_interval 60
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `60`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
ceph -s
```

---

### cephfs_mirror_tick_interval

| | |
|---|---|
| نوع | Secs · default `5` · **Advanced** |
| جدول | [cephfs.md#SP_cephfs_mirror_tick_interval](../../../config/cephfs-mirror/cephfs.md#SP_cephfs_mirror_tick_interval) |

**کارکرد:** interval for the per-peer mirroring tick thread interval in seconds for the per-peer tick thread that runs periodic mirroring work. The value is re-read each iteration so configuration changes take effect without restarting the daemon.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_tick_interval 5
ceph config get cephfs_mirror cephfs_mirror_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get cephfs_mirror cephfs_mirror_tick_interval
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
