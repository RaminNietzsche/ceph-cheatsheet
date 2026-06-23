# RBD mirror

راهنمای عمیق پیکربندی RBD mirror — 24 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd-mirror/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_mirror_concurrent_image_deletions](#rbd_mirror_concurrent_image_deletions) | `1` | Advanced | عملکرد |
| [rbd_mirror_concurrent_image_syncs](#rbd_mirror_concurrent_image_syncs) | `5` | Advanced | عملکرد |
| [rbd_mirror_delete_retry_interval](#rbd_mirror_delete_retry_interval) | `30` | Advanced | عملکرد |
| [rbd_mirror_image_perf_stats_prio](#rbd_mirror_image_perf_stats_prio) | `5` | Advanced | عملکرد |
| [rbd_mirror_image_policy_migration_throttle](#rbd_mirror_image_policy_migration_throttle) | `300` | Advanced | عملکرد |
| [rbd_mirror_image_policy_rebalance_timeout](#rbd_mirror_image_policy_rebalance_timeout) | `0` | Advanced | عملکرد |
| [rbd_mirror_image_policy_type](#rbd_mirror_image_policy_type) | `simple` | Advanced | عملکرد |
| [rbd_mirror_image_policy_update_throttle_interval](#rbd_mirror_image_policy_update_throttle_interval) | `1` | Advanced | عملکرد |
| [rbd_mirror_image_state_check_interval](#rbd_mirror_image_state_check_interval) | `30` | Advanced | عملکرد |
| [rbd_mirror_journal_commit_age](#rbd_mirror_journal_commit_age) | `5` | Advanced | عملکرد |
| [rbd_mirror_journal_poll_age](#rbd_mirror_journal_poll_age) | `5` | Advanced | عملکرد |
| [rbd_mirror_leader_heartbeat_interval](#rbd_mirror_leader_heartbeat_interval) | `5` | Advanced | عملکرد |
| [rbd_mirror_leader_max_acquire_attempts_before_break](#rbd_mirror_leader_max_acquire_attempts_before_break) | `3` | Advanced | عملکرد |
| [rbd_mirror_leader_max_missed_heartbeats](#rbd_mirror_leader_max_missed_heartbeats) | `2` | Advanced | عملکرد |
| [rbd_mirror_memory_autotune](#rbd_mirror_memory_autotune) | `True` | Dev | توسعه |
| [rbd_mirror_memory_base](#rbd_mirror_memory_base) | `768_M` | Dev | توسعه |
| [rbd_mirror_memory_cache_autotune_interval](#rbd_mirror_memory_cache_autotune_interval) | `30` | Dev | توسعه |
| [rbd_mirror_memory_cache_min](#rbd_mirror_memory_cache_min) | `128_M` | Dev | توسعه |
| [rbd_mirror_memory_cache_resize_interval](#rbd_mirror_memory_cache_resize_interval) | `5` | Dev | توسعه |
| [rbd_mirror_memory_expected_fragmentation](#rbd_mirror_memory_expected_fragmentation) | `0.15` | Dev | توسعه |
| [rbd_mirror_memory_target](#rbd_mirror_memory_target) | `4_G` | Basic | سیاست |
| [rbd_mirror_perf_stats_prio](#rbd_mirror_perf_stats_prio) | `5` | Advanced | عملکرد |
| [rbd_mirror_pool_replayers_refresh_interval](#rbd_mirror_pool_replayers_refresh_interval) | `30` | Advanced | عملکرد |
| [rbd_mirror_sync_point_update_age](#rbd_mirror_sync_point_update_age) | `30` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. rbd-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_mirror_concurrent_image_deletions

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_concurrent_image_deletions](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_deletions) |

**کارکرد:** maximum number of image deletions in parallel

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_concurrent_image_deletions 1
ceph config get client rbd_mirror_concurrent_image_deletions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_concurrent_image_deletions
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_concurrent_image_syncs

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_concurrent_image_syncs](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_syncs) |

**کارکرد:** maximum number of image syncs in parallel

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_concurrent_image_syncs 5
ceph config get client rbd_mirror_concurrent_image_syncs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_concurrent_image_syncs
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_delete_retry_interval

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_delete_retry_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_delete_retry_interval) |

**کارکرد:** interval to check and retry the failed deletion requests

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_delete_retry_interval 30
ceph config get client rbd_mirror_delete_retry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_delete_retry_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_perf_stats_prio

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_perf_stats_prio) |

**کارکرد:** Priority level for mirror daemon per-image replication perf counters

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_image_perf_stats_prio 5
ceph config get client rbd_mirror_image_perf_stats_prio
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
ceph config get client rbd_mirror_image_perf_stats_prio
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_policy_migration_throttle

| | |
|---|---|
| نوع | Uint · default `300` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_policy_migration_throttle](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_migration_throttle) |

**کارکرد:** number of seconds after which an image can be reshuffled (migrated) again

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_image_policy_migration_throttle 300
ceph config get client rbd_mirror_image_policy_migration_throttle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `300`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_image_policy_migration_throttle
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_policy_rebalance_timeout

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout) |

**کارکرد:** number of seconds policy should be idle before triggering reshuffle (rebalance) of images

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_image_policy_rebalance_timeout 0
ceph config get client rbd_mirror_image_policy_rebalance_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_image_policy_rebalance_timeout
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_policy_type

| | |
|---|---|
| نوع | Str · enum: ["none", "simple"] · default `simple` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_policy_type](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_type) |

**کارکرد:** active/active policy type for mapping images to instances

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_image_policy_type simple
ceph config get client rbd_mirror_image_policy_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `simple`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_image_policy_type
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_policy_update_throttle_interval

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval) |

**کارکرد:** interval (in seconds) to throttle images for mirror daemon peer updates

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_image_policy_update_throttle_interval 1
ceph config get client rbd_mirror_image_policy_update_throttle_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_image_policy_update_throttle_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_image_state_check_interval

| | |
|---|---|
| نوع | Uint · default `30` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_image_state_check_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_state_check_interval) |

**کارکرد:** interval to get images from pool watcher and set sources in replayer

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_image_state_check_interval 30
ceph config get client rbd_mirror_image_state_check_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_image_state_check_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_journal_commit_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_journal_commit_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_commit_age) |

**کارکرد:** commit time interval, seconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_journal_commit_age 5
ceph config get client rbd_mirror_journal_commit_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_journal_commit_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_journal_poll_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_journal_poll_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_poll_age) |

**کارکرد:** maximum age (in seconds) between successive journal polls

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_journal_poll_age 5
ceph config get client rbd_mirror_journal_poll_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_journal_poll_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_leader_heartbeat_interval

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_leader_heartbeat_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_heartbeat_interval) |

**کارکرد:** interval (in seconds) between mirror leader heartbeats

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_leader_heartbeat_interval 5
ceph config get client rbd_mirror_leader_heartbeat_interval
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
ceph config get client rbd_mirror_leader_heartbeat_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_leader_max_acquire_attempts_before_break

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break) |

**کارکرد:** number of failed attempts to acquire lock after missing heartbeats before breaking lock

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_mirror_leader_max_acquire_attempts_before_break 3
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_leader_max_missed_heartbeats

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats) |

**کارکرد:** number of missed heartbeats for non-lock owner to attempt to acquire lock

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_mirror_leader_max_missed_heartbeats 2
ceph config get client rbd_mirror_leader_max_missed_heartbeats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_leader_max_missed_heartbeats
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_memory_autotune

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_autotune](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_autotune) |

**کارکرد:** Automatically tune the ratio of caches while respecting min values.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_autotune false
ceph config get client rbd_mirror_memory_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_base

| | |
|---|---|
| نوع | Size · default `768_M` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_base](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_base) |

**کارکرد:** When tcmalloc and cache autotuning is enabled, estimate the minimum amount of memory in bytes the rbd-mirror daemon will need.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_base 768_M
ceph config get client rbd_mirror_memory_base
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`768_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_cache_autotune_interval

| | |
|---|---|
| نوع | Float · default `30` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_cache_autotune_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_autotune_interval) |

**کارکرد:** The number of seconds to wait between rebalances when cache autotune is enabled.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_cache_autotune_interval 30
ceph config get client rbd_mirror_memory_cache_autotune_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`30`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_cache_min

| | |
|---|---|
| نوع | Size · default `128_M` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_cache_min](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_min) |

**کارکرد:** When tcmalloc and cache autotuning is enabled, set the minimum amount of memory used for cache.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_cache_min 128_M
ceph config get client rbd_mirror_memory_cache_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`128_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_cache_resize_interval

| | |
|---|---|
| نوع | Float · default `5` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_cache_resize_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_resize_interval) |

**کارکرد:** When tcmalloc and cache autotuning is enabled, wait this many seconds between resizing caches.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_cache_resize_interval 5
ceph config get client rbd_mirror_memory_cache_resize_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_expected_fragmentation

| | |
|---|---|
| نوع | Float · default `0.15` · **Dev** |
| جدول | [rbd.md#SP_rbd_mirror_memory_expected_fragmentation](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_expected_fragmentation) |

**کارکرد:** When tcmalloc and cache autotuning is enabled, estimate the percent of memory fragmentation.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_expected_fragmentation 0.15
ceph config get client rbd_mirror_memory_expected_fragmentation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.15`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### rbd_mirror_memory_target

| | |
|---|---|
| نوع | Size · default `4_G` · **Basic** |
| جدول | [rbd.md#SP_rbd_mirror_memory_target](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_target) |

**کارکرد:** When tcmalloc and cache autotuning is enabled, try to keep this many bytes mapped in memory.

**زمان استفاده:** رفتار اصلی RBD mirror — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set client rbd_mirror_memory_target 4_G
ceph config get client rbd_mirror_memory_target
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `4_G` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_memory_target
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_perf_stats_prio

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_perf_stats_prio) |

**کارکرد:** Priority level for mirror daemon replication perf counters

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_perf_stats_prio 5
ceph config get client rbd_mirror_perf_stats_prio
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
ceph config get client rbd_mirror_perf_stats_prio
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_pool_replayers_refresh_interval

| | |
|---|---|
| نوع | Uint · default `30` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval) |

**کارکرد:** interval to refresh peers in rbd-mirror daemon

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_mirror_pool_replayers_refresh_interval 30
ceph config get client rbd_mirror_pool_replayers_refresh_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_pool_replayers_refresh_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirror_sync_point_update_age

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirror_sync_point_update_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_sync_point_update_age) |

**کارکرد:** number of seconds between each update of the image sync point object number

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirror_sync_point_update_age 30
ceph config get client rbd_mirror_sync_point_update_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirror_sync_point_update_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
