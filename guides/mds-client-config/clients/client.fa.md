# CephFS client

راهنمای عمیق پیکربندی MDS client — 53 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [client_acl_type](#client_acl_type) | `(empty)` | Advanced | Performance |
| [client_asio_thread_count](#client_asio_thread_count) | `2` | Advanced | Performance |
| [client_cache_mid](#client_cache_mid) | `0.75` | Advanced | Performance |
| [client_cache_size](#client_cache_size) | `16_K` | Basic | Performance |
| [client_caps_release_delay](#client_caps_release_delay) | `5` | Dev | Dev |
| [client_check_pool_perm](#client_check_pool_perm) | `True` | Advanced | Performance |
| [client_collect_and_send_global_metrics](#client_collect_and_send_global_metrics) | `False` | Advanced | Performance |
| [client_debug_force_sync_read](#client_debug_force_sync_read) | `False` | Dev | Dev |
| [client_debug_getattr_caps](#client_debug_getattr_caps) | `False` | Dev | Dev |
| [client_debug_inject_features](#client_debug_inject_features) | `(empty)` | Dev | Dev |
| [client_debug_inject_tick_delay](#client_debug_inject_tick_delay) | `0` | Dev | Dev |
| [client_die_on_failed_dentry_invalidate](#client_die_on_failed_dentry_invalidate) | `True` | Advanced | Performance |
| [client_die_on_failed_remount](#client_die_on_failed_remount) | `False` | Dev | Dev |
| [client_dirsize_rbytes](#client_dirsize_rbytes) | `True` | Advanced | Performance |
| [client_file_blockdiff_max_concurrent_object_scans](#client_file_blockdiff_max_concurrent_object_scans) | `16` | Advanced | Performance |
| [client_force_lazyio](#client_force_lazyio) | `False` | Advanced | Performance |
| [client_fs](#client_fs) | `(empty)` | Advanced | Performance |
| [client_fscrypt_as](#client_fscrypt_as) | `True` | Advanced | Performance |
| [client_fscrypt_dummy_encryption](#client_fscrypt_dummy_encryption) | `False` | Dev | Dev |
| [client_inject_fixed_oldest_tid](#client_inject_fixed_oldest_tid) | `False` | Dev | Dev |
| [client_inject_release_failure](#client_inject_release_failure) | `False` | Dev | Dev |
| [client_inject_write_delay_secs](#client_inject_write_delay_secs) | `0` | Dev | Dev |
| [client_max_inline_size](#client_max_inline_size) | `4_K` | Dev | Dev |
| [client_max_retries_on_remount_failure](#client_max_retries_on_remount_failure) | `5` | Advanced | Performance |
| [client_mds_namespace](#client_mds_namespace) | `(empty)` | Dev | Dev |
| [client_metadata](#client_metadata) | `(empty)` | Advanced | Performance |
| [client_mount_gid](#client_mount_gid) | `-1` | Advanced | Performance |
| [client_mount_timeout](#client_mount_timeout) | `5_min` | Advanced | Performance |
| [client_mount_uid](#client_mount_uid) | `-1` | Advanced | Performance |
| [client_mountpoint](#client_mountpoint) | `/` | Advanced | Performance |
| [client_notify_timeout](#client_notify_timeout) | `10` | Dev | Dev |
| [client_oc](#client_oc) | `True` | Advanced | Performance |
| [client_oc_max_dirty](#client_oc_max_dirty) | `100_M` | Advanced | Performance |
| [client_oc_max_dirty_age](#client_oc_max_dirty_age) | `5` | Advanced | Performance |
| [client_oc_max_objects](#client_oc_max_objects) | `1000` | Advanced | Performance |
| [client_oc_size](#client_oc_size) | `200_M` | Advanced | Performance |
| [client_oc_target_dirty](#client_oc_target_dirty) | `8_M` | Advanced | Performance |
| [client_permissions](#client_permissions) | `True` | Advanced | Performance |
| [client_quota](#client_quota) | `True` | Advanced | Performance |
| [client_quota_df](#client_quota_df) | `True` | Advanced | Performance |
| [client_readahead_max_bytes](#client_readahead_max_bytes) | `0` | Advanced | Performance |
| [client_readahead_max_periods](#client_readahead_max_periods) | `4` | Advanced | Performance |
| [client_readahead_min](#client_readahead_min) | `128_K` | Advanced | Performance |
| [client_reconnect_stale](#client_reconnect_stale) | `False` | Advanced | Performance |
| [client_respect_subvolume_snapshot_visibility](#client_respect_subvolume_snapshot_visibility) | `False` | Advanced | Performance |
| [client_shutdown_timeout](#client_shutdown_timeout) | `30` | Advanced | Performance |
| [client_snapdir](#client_snapdir) | `.snap` | Advanced | Performance |
| [client_tick_interval](#client_tick_interval) | `1` | Dev | Dev |
| [client_trace](#client_trace) | `(empty)` | Dev | Dev |
| [client_try_dentry_invalidate](#client_try_dentry_invalidate) | `False` | Dev | Dev |
| [client_use_faked_inos](#client_use_faked_inos) | `False` | Dev | Dev |
| [client_use_random_mds](#client_use_random_mds) | `False` | Dev | Dev |
| [osd_client_watch_timeout](#osd_client_watch_timeout) | `30` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### client_acl_type

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [client.md#SP_client_acl_type](../../../config/mds-client/client.md#SP_client_acl_type) |

**کارکرد:** ACL type to enforce (none or "posix_acl")

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_acl_type "example"
ceph config get client client_acl_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_acl_type
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_asio_thread_count

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [client.md#SP_client_asio_thread_count](../../../config/mds-client/client.md#SP_client_asio_thread_count) |

**کارکرد:** Size of thread pool for ASIO completions

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_asio_thread_count 2
ceph config get client client_asio_thread_count
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
ceph config get client client_asio_thread_count
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_cache_mid

| | |
|---|---|
| نوع | Float · default `0.75` · **Advanced** |
| جدول | [client.md#SP_client_cache_mid](../../../config/mds-client/client.md#SP_client_cache_mid) |

**کارکرد:** mid-point of client cache LRU

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_cache_mid 0.75
ceph config get client client_cache_mid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.75`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_cache_mid
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_cache_size

| | |
|---|---|
| نوع | Size · default `16_K` · **Basic** |
| جدول | [client.md#SP_client_cache_size](../../../config/mds-client/client.md#SP_client_cache_size) |

**کارکرد:** soft maximum number of directory entries in client cache

**زمان استفاده:** رفتار اصلی MDS client — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client client_cache_size 16_K
ceph config get client client_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `16_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_cache_size
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_caps_release_delay

| | |
|---|---|
| نوع | Secs · default `5` · **Dev** |
| جدول | [client.md#SP_client_caps_release_delay](../../../config/mds-client/client.md#SP_client_caps_release_delay) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_caps_release_delay 5
ceph config get client client_caps_release_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_check_pool_perm

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_check_pool_perm](../../../config/mds-client/client.md#SP_client_check_pool_perm) |

**کارکرد:** confirm access to inode's data pool/namespace described in file layout

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_check_pool_perm false
ceph config get client client_check_pool_perm
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_check_pool_perm
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_collect_and_send_global_metrics

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [client.md#SP_client_collect_and_send_global_metrics](../../../config/mds-client/client.md#SP_client_collect_and_send_global_metrics) |

**کارکرد:** to enable and force collecting and sending the global metrics to MDS

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client client_collect_and_send_global_metrics true
ceph config get client client_collect_and_send_global_metrics
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_collect_and_send_global_metrics
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_debug_force_sync_read

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_debug_force_sync_read](../../../config/mds-client/client.md#SP_client_debug_force_sync_read) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_debug_force_sync_read true
ceph config get client client_debug_force_sync_read
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_debug_getattr_caps

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_debug_getattr_caps](../../../config/mds-client/client.md#SP_client_debug_getattr_caps) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_debug_getattr_caps true
ceph config get client client_debug_getattr_caps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_debug_inject_features

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_debug_inject_features](../../../config/mds-client/client.md#SP_client_debug_inject_features) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_debug_inject_features "example"
ceph config get client client_debug_inject_features
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_debug_inject_tick_delay

| | |
|---|---|
| نوع | Secs · default `0` · **Dev** |
| جدول | [client.md#SP_client_debug_inject_tick_delay](../../../config/mds-client/client.md#SP_client_debug_inject_tick_delay) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_debug_inject_tick_delay 0
ceph config get client client_debug_inject_tick_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_die_on_failed_dentry_invalidate

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_die_on_failed_dentry_invalidate](../../../config/mds-client/client.md#SP_client_die_on_failed_dentry_invalidate) |

**کارکرد:** kill the client when no dentry invalidation options are available

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_die_on_failed_dentry_invalidate false
ceph config get client client_die_on_failed_dentry_invalidate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_die_on_failed_dentry_invalidate
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_die_on_failed_remount

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_die_on_failed_remount](../../../config/mds-client/client.md#SP_client_die_on_failed_remount) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_die_on_failed_remount true
ceph config get client client_die_on_failed_remount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_dirsize_rbytes

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_dirsize_rbytes](../../../config/mds-client/client.md#SP_client_dirsize_rbytes) |

**کارکرد:** set the directory size as the number of file bytes recursively used

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_dirsize_rbytes false
ceph config get client client_dirsize_rbytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_dirsize_rbytes
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_file_blockdiff_max_concurrent_object_scans

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [client.md#SP_client_file_blockdiff_max_concurrent_object_scans](../../../config/mds-client/client.md#SP_client_file_blockdiff_max_concurrent_object_scans) |

**کارکرد:** maximum number of concurrent object scans

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_file_blockdiff_max_concurrent_object_scans 16
ceph config get client client_file_blockdiff_max_concurrent_object_scans
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_file_blockdiff_max_concurrent_object_scans
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_force_lazyio

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_force_lazyio](../../../config/mds-client/client.md#SP_client_force_lazyio) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client client_force_lazyio true
ceph config get client client_force_lazyio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_force_lazyio
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_fs

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_fs](../../../config/mds-client/client.md#SP_client_fs) |

**کارکرد:** CephFS file system name to mount

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_fs "example"
ceph config get client client_fs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_fs
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_fscrypt_as

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_fscrypt_as](../../../config/mds-client/client.md#SP_client_fscrypt_as) |

**کارکرد:** Enable fscrypt access semantics

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_fscrypt_as false
ceph config get client client_fscrypt_as
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_fscrypt_as
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_fscrypt_dummy_encryption

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_fscrypt_dummy_encryption](../../../config/mds-client/client.md#SP_client_fscrypt_dummy_encryption) |

**کارکرد:** Enable fscrypt dummy encryption

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_fscrypt_dummy_encryption true
ceph config get client client_fscrypt_dummy_encryption
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_inject_fixed_oldest_tid

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_inject_fixed_oldest_tid](../../../config/mds-client/client.md#SP_client_inject_fixed_oldest_tid) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_inject_fixed_oldest_tid true
ceph config get client client_inject_fixed_oldest_tid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_inject_release_failure

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_inject_release_failure](../../../config/mds-client/client.md#SP_client_inject_release_failure) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_inject_release_failure true
ceph config get client client_inject_release_failure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_inject_write_delay_secs

| | |
|---|---|
| نوع | Secs · default `0` · **Dev** |
| جدول | [client.md#SP_client_inject_write_delay_secs](../../../config/mds-client/client.md#SP_client_inject_write_delay_secs) |

**کارکرد:** induce delay in write operation for testing

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_inject_write_delay_secs 0
ceph config get client client_inject_write_delay_secs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_max_inline_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Dev** |
| جدول | [client.md#SP_client_max_inline_size](../../../config/mds-client/client.md#SP_client_max_inline_size) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_max_inline_size 4_K
ceph config get client client_max_inline_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`4_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_max_retries_on_remount_failure

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [client.md#SP_client_max_retries_on_remount_failure](../../../config/mds-client/client.md#SP_client_max_retries_on_remount_failure) |

**کارکرد:** number of consecutive failed remount attempts for invalidating kernel dcache after which client would abort.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_max_retries_on_remount_failure 5
ceph config get client client_max_retries_on_remount_failure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_max_retries_on_remount_failure
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_mds_namespace

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_mds_namespace](../../../config/mds-client/client.md#SP_client_mds_namespace) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_mds_namespace "example"
ceph config get client client_mds_namespace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_metadata

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [client.md#SP_client_metadata](../../../config/mds-client/client.md#SP_client_metadata) |

**کارکرد:** metadata key=value comma-delimited pairs appended to session metadata

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_metadata "example"
ceph config get client client_metadata
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_metadata
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_mount_gid

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [client.md#SP_client_mount_gid](../../../config/mds-client/client.md#SP_client_mount_gid) |

**کارکرد:** gid to mount as

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_mount_gid 128
ceph config get client client_mount_gid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_mount_gid
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_mount_timeout

| | |
|---|---|
| نوع | Secs · default `5_min` · **Advanced** |
| جدول | [client.md#SP_client_mount_timeout](../../../config/mds-client/client.md#SP_client_mount_timeout) |

**کارکرد:** timeout for mounting CephFS (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client client_mount_timeout 5_min
ceph config get client client_mount_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_mount_timeout
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_mount_uid

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [client.md#SP_client_mount_uid](../../../config/mds-client/client.md#SP_client_mount_uid) |

**کارکرد:** uid to mount as

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_mount_uid 128
ceph config get client client_mount_uid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_mount_uid
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_mountpoint

| | |
|---|---|
| نوع | Str · default `/` · **Advanced** |
| جدول | [client.md#SP_client_mountpoint](../../../config/mds-client/client.md#SP_client_mountpoint) |

**کارکرد:** default mount-point

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_mountpoint "/"
ceph config get client client_mountpoint
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `/`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_mountpoint
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_notify_timeout

| | |
|---|---|
| نوع | Int · default `10` · **Dev** |
| جدول | [client.md#SP_client_notify_timeout](../../../config/mds-client/client.md#SP_client_notify_timeout) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_notify_timeout 10
ceph config get client client_notify_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`10`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_oc

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_oc](../../../config/mds-client/client.md#SP_client_oc) |

**کارکرد:** enable object caching

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_oc false
ceph config get client client_oc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_oc_max_dirty

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [client.md#SP_client_oc_max_dirty](../../../config/mds-client/client.md#SP_client_oc_max_dirty) |

**کارکرد:** maximum size of dirty pages in object cache

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_oc_max_dirty 100_M
ceph config get client client_oc_max_dirty
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc_max_dirty
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_oc_max_dirty_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [client.md#SP_client_oc_max_dirty_age](../../../config/mds-client/client.md#SP_client_oc_max_dirty_age) |

**کارکرد:** maximum age of dirty pages in object cache (seconds)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_oc_max_dirty_age 5
ceph config get client client_oc_max_dirty_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc_max_dirty_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_oc_max_objects

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [client.md#SP_client_oc_max_objects](../../../config/mds-client/client.md#SP_client_oc_max_objects) |

**کارکرد:** maximum number of objects in cache

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_oc_max_objects 1000
ceph config get client client_oc_max_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc_max_objects
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_oc_size

| | |
|---|---|
| نوع | Size · default `200_M` · **Advanced** |
| جدول | [client.md#SP_client_oc_size](../../../config/mds-client/client.md#SP_client_oc_size) |

**کارکرد:** maximum size of object cache

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_oc_size 200_M
ceph config get client client_oc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `200_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc_size
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_oc_target_dirty

| | |
|---|---|
| نوع | Size · default `8_M` · **Advanced** |
| جدول | [client.md#SP_client_oc_target_dirty](../../../config/mds-client/client.md#SP_client_oc_target_dirty) |

**کارکرد:** target size of dirty pages object cache

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_oc_target_dirty 8_M
ceph config get client client_oc_target_dirty
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `8_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_oc_target_dirty
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_permissions

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_permissions](../../../config/mds-client/client.md#SP_client_permissions) |

**کارکرد:** client-enforced permission checking

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_permissions false
ceph config get client client_permissions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_permissions
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_quota

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_quota](../../../config/mds-client/client.md#SP_client_quota) |

**کارکرد:** Enable quota enforcement

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_quota false
ceph config get client client_quota
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_quota
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_quota_df

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [client.md#SP_client_quota_df](../../../config/mds-client/client.md#SP_client_quota_df) |

**کارکرد:** show quota usage for statfs (df)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client client_quota_df false
ceph config get client client_quota_df
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_quota_df
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_readahead_max_bytes

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [client.md#SP_client_readahead_max_bytes](../../../config/mds-client/client.md#SP_client_readahead_max_bytes) |

**کارکرد:** maximum bytes to readahead in a file (zero is unlimited)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_readahead_max_bytes 64
ceph config get client client_readahead_max_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_readahead_max_bytes
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_readahead_max_periods

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [client.md#SP_client_readahead_max_periods](../../../config/mds-client/client.md#SP_client_readahead_max_periods) |

**کارکرد:** maximum stripe periods to readahead in a file

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client client_readahead_max_periods 4
ceph config get client client_readahead_max_periods
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_readahead_max_periods
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_readahead_min

| | |
|---|---|
| نوع | Size · default `128_K` · **Advanced** |
| جدول | [client.md#SP_client_readahead_min](../../../config/mds-client/client.md#SP_client_readahead_min) |

**کارکرد:** minimum bytes to readahead in a file

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_readahead_min 128_K
ceph config get client client_readahead_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `128_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_readahead_min
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_reconnect_stale

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [client.md#SP_client_reconnect_stale](../../../config/mds-client/client.md#SP_client_reconnect_stale) |

**کارکرد:** reconnect when the session becomes stale

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client client_reconnect_stale true
ceph config get client client_reconnect_stale
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_reconnect_stale
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_respect_subvolume_snapshot_visibility

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [client.md#SP_client_respect_subvolume_snapshot_visibility](../../../config/mds-client/client.md#SP_client_respect_subvolume_snapshot_visibility) |

**کارکرد:** Respect subvolume snapshot visibility

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client client_respect_subvolume_snapshot_visibility true
ceph config get client client_respect_subvolume_snapshot_visibility
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_respect_subvolume_snapshot_visibility
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_shutdown_timeout

| | |
|---|---|
| نوع | Secs · default `30` · **Advanced** |
| جدول | [client.md#SP_client_shutdown_timeout](../../../config/mds-client/client.md#SP_client_shutdown_timeout) |

**کارکرد:** timeout for shutting down CephFS

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client client_shutdown_timeout 30
ceph config get client client_shutdown_timeout
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
ceph config get client client_shutdown_timeout
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_snapdir

| | |
|---|---|
| نوع | Str · default `.snap` · **Advanced** |
| جدول | [client.md#SP_client_snapdir](../../../config/mds-client/client.md#SP_client_snapdir) |

**کارکرد:** pseudo directory for snapshot access to a directory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client client_snapdir ".snap"
ceph config get client client_snapdir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `.snap`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client client_snapdir
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### client_tick_interval

| | |
|---|---|
| نوع | Secs · default `1` · **Dev** |
| جدول | [client.md#SP_client_tick_interval](../../../config/mds-client/client.md#SP_client_tick_interval) |

**کارکرد:** seconds between client upkeep ticks

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_tick_interval 1
ceph config get client client_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_trace

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [client.md#SP_client_trace](../../../config/mds-client/client.md#SP_client_trace) |

**کارکرد:** file containing trace of client operations

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_trace "example"
ceph config get client client_trace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_try_dentry_invalidate

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_try_dentry_invalidate](../../../config/mds-client/client.md#SP_client_try_dentry_invalidate) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_try_dentry_invalidate true
ceph config get client client_try_dentry_invalidate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_use_faked_inos

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [client.md#SP_client_use_faked_inos](../../../config/mds-client/client.md#SP_client_use_faked_inos) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_use_faked_inos true
ceph config get client client_use_faked_inos
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### client_use_random_mds

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [client.md#SP_client_use_random_mds](../../../config/mds-client/client.md#SP_client_use_random_mds) |

**کارکرد:** issue new requests to a random active MDS

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client client_use_random_mds true
ceph config get client client_use_random_mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_client_watch_timeout

| | |
|---|---|
| نوع | Int · default `30` · **Dev** |
| جدول | [osd.md#SP_osd_client_watch_timeout](../../../config/mds-client/osd.md#SP_osd_client_watch_timeout) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_client_watch_timeout 30
ceph config get osd osd_client_watch_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`30`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
