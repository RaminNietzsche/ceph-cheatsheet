# CephFS mirror

راهنمای عمیق پیکربندی CephFS mirror — 15 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/cephfs-mirror/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cephfs_mirror_action_update_interval](#cephfs_mirror_action_update_interval) | `2` | Advanced | Performance |
| [cephfs_mirror_blockdiff_min_file_size](#cephfs_mirror_blockdiff_min_file_size) | `16_M` | Advanced | Performance |
| [cephfs_mirror_datasync_files_per_batch](#cephfs_mirror_datasync_files_per_batch) | `64` | Advanced | Performance |
| [cephfs_mirror_directory_scan_interval](#cephfs_mirror_directory_scan_interval) | `10` | Advanced | Performance |
| [cephfs_mirror_distribute_datasync_threads](#cephfs_mirror_distribute_datasync_threads) | `True` | Advanced | Performance |
| [cephfs_mirror_max_concurrent_directory_syncs](#cephfs_mirror_max_concurrent_directory_syncs) | `3` | Advanced | Performance |
| [cephfs_mirror_max_consecutive_failures_per_directory](#cephfs_mirror_max_consecutive_failures_per_directory) | `10` | Advanced | Performance |
| [cephfs_mirror_max_datasync_threads](#cephfs_mirror_max_datasync_threads) | `6` | Advanced | Performance |
| [cephfs_mirror_max_snapshot_sync_per_cycle](#cephfs_mirror_max_snapshot_sync_per_cycle) | `3` | Advanced | Performance |
| [cephfs_mirror_mount_timeout](#cephfs_mirror_mount_timeout) | `10` | Advanced | Performance |
| [cephfs_mirror_perf_stats_prio](#cephfs_mirror_perf_stats_prio) | `5` | Advanced | Performance |
| [cephfs_mirror_restart_mirror_on_blocklist_interval](#cephfs_mirror_restart_mirror_on_blocklist_interval) | `30` | Advanced | Performance |
| [cephfs_mirror_restart_mirror_on_failure_interval](#cephfs_mirror_restart_mirror_on_failure_interval) | `20` | Advanced | Performance |
| [cephfs_mirror_retry_failed_directories_interval](#cephfs_mirror_retry_failed_directories_interval) | `60` | Advanced | Performance |
| [cephfs_mirror_tick_interval](#cephfs_mirror_tick_interval) | `5` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

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

**کارکرد:** interval for driving asynchronous mirror actions

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_action_update_interval 2
ceph config get cephfs_mirror cephfs_mirror_action_update_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** minimum file size threshold in bytes above which block-level diff is used during CephFS mirroring.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_blockdiff_min_file_size 16_M
ceph config get cephfs_mirror cephfs_mirror_blockdiff_min_file_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** maximum number of files processed by datasync threads per scheduling cycle before yielding.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_datasync_files_per_batch 64
ceph config get cephfs_mirror cephfs_mirror_datasync_files_per_batch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** interval to scan directories to mirror snapshots

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_directory_scan_interval 10
ceph config get cephfs_mirror cephfs_mirror_directory_scan_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** distribute data synchronization threads evenly across multiple snapshots.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_distribute_datasync_threads false
ceph config get cephfs_mirror cephfs_mirror_distribute_datasync_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** maximum number of concurrent snapshot synchronization crawler threads

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs 3
ceph config get cephfs_mirror cephfs_mirror_max_concurrent_directory_syncs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** consecutive failed directory synchronization attempts before marking a directory as "failed"

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory 10
ceph config get cephfs_mirror cephfs_mirror_max_consecutive_failures_per_directory
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** maximum number of concurrent snapshot data synchronization threads

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_datasync_threads 6
ceph config get cephfs_mirror cephfs_mirror_max_datasync_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** number of snapshots to mirror in one cycle

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle 3
ceph config get cephfs_mirror cephfs_mirror_max_snapshot_sync_per_cycle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** timeout for mounting primary/secondary ceph file system

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_mount_timeout 10
ceph config get cephfs_mirror cephfs_mirror_mount_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** Priority level for mirror daemon replication perf counters

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_perf_stats_prio 5
ceph config get cephfs_mirror cephfs_mirror_perf_stats_prio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** interval to restart blocklisted instances

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval 30
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_blocklist_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** interval to restart failed mirror instances

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval 20
ceph config get cephfs_mirror cephfs_mirror_restart_mirror_on_failure_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** failed directory retry interval for synchronization

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_retry_failed_directories_interval 60
ceph config get cephfs_mirror cephfs_mirror_retry_failed_directories_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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

**کارکرد:** interval for the per-peer mirroring tick thread

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set cephfs_mirror cephfs_mirror_tick_interval 5
ceph config get cephfs_mirror cephfs_mirror_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

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
