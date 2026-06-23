# Mgr

deep dive پیکربندی Global — 11 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mgr_client_service_daemon_unregister_timeout](#mgr_client_service_daemon_unregister_timeout) | `1` | Dev | Dev |
| [mgr_connect_retry_interval](#mgr_connect_retry_interval) | `1` | Dev | Dev |
| [mgr_enable_op_tracker](#mgr_enable_op_tracker) | `True` | Advanced | Policy |
| [mgr_map_cache_enabled](#mgr_map_cache_enabled) | `True` | Dev | Dev |
| [mgr_num_op_tracker_shard](#mgr_num_op_tracker_shard) | `32` | Advanced | Performance |
| [mgr_op_complaint_time](#mgr_op_complaint_time) | `30` | Advanced | Performance |
| [mgr_op_history_duration](#mgr_op_history_duration) | `600` | Advanced | Performance |
| [mgr_op_history_size](#mgr_op_history_size) | `20` | Advanced | Performance |
| [mgr_op_history_slow_op_size](#mgr_op_history_slow_op_size) | `20` | Advanced | Performance |
| [mgr_op_history_slow_op_threshold](#mgr_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [mgr_op_log_threshold](#mgr_op_log_threshold) | `5` | Advanced | Performance |

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

### mgr_client_service_daemon_unregister_timeout

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [mgr.md#SP_mgr_client_service_daemon_unregister_timeout](../../../config/global/mgr.md#SP_mgr_client_service_daemon_unregister_timeout) |

**کارکرد:** Time to wait during shutdown to deregister a service with the Manager

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mgr mgr_client_service_daemon_unregister_timeout 1
ceph config get mgr mgr_client_service_daemon_unregister_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mgr_connect_retry_interval

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [mgr.md#SP_mgr_connect_retry_interval](../../../config/global/mgr.md#SP_mgr_connect_retry_interval) |

**کارکرد:** Manager reconnect retry interval

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mgr mgr_connect_retry_interval 1
ceph config get mgr mgr_connect_retry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mgr_enable_op_tracker

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mgr.md#SP_mgr_enable_op_tracker](../../../config/global/mgr.md#SP_mgr_enable_op_tracker) |

**کارکرد:** Enable / disable the Manager op tracker

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mgr mgr_enable_op_tracker false
ceph config get mgr mgr_enable_op_tracker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_enable_op_tracker
ceph -s
ceph mgr stat
```

---

### mgr_map_cache_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mgr.md#SP_mgr_map_cache_enabled](../../../config/global/mgr.md#SP_mgr_map_cache_enabled) |

**کارکرد:** Enable the manager's map cache for API calls

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mgr mgr_map_cache_enabled false
ceph config get mgr mgr_map_cache_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mgr_num_op_tracker_shard

| | |
|---|---|
| نوع | Uint · default `32` · **Advanced** |
| جدول | [mgr.md#SP_mgr_num_op_tracker_shard](../../../config/global/mgr.md#SP_mgr_num_op_tracker_shard) |

**کارکرد:** The number of shards for Manager ops

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_num_op_tracker_shard 32
ceph config get mgr mgr_num_op_tracker_shard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_num_op_tracker_shard
ceph -s
ceph mgr stat
```

---

### mgr_op_complaint_time

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_complaint_time](../../../config/global/mgr.md#SP_mgr_op_complaint_time) |

**کارکرد:** A Manager operation becomes complaint-worthy after the specified number of seconds have elapsed.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_complaint_time 30
ceph config get mgr mgr_op_complaint_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_complaint_time
ceph -s
ceph mgr stat
```

---

### mgr_op_history_duration

| | |
|---|---|
| نوع | Uint · default `600` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_history_duration](../../../config/global/mgr.md#SP_mgr_op_history_duration) |

**کارکرد:** The oldest completed Manager operation to track.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_history_duration 600
ceph config get mgr mgr_op_history_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `600`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_history_duration
ceph -s
ceph mgr stat
```

---

### mgr_op_history_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_history_size](../../../config/global/mgr.md#SP_mgr_op_history_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_history_size 20
ceph config get mgr mgr_op_history_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_history_size
ceph -s
ceph mgr stat
```

---

### mgr_op_history_slow_op_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_history_slow_op_size](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_size) |

**کارکرد:** Max number of slow Manager ops to track

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_history_slow_op_size 20
ceph config get mgr mgr_op_history_slow_op_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_history_slow_op_size
ceph -s
ceph mgr stat
```

---

### mgr_op_history_slow_op_threshold

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_history_slow_op_threshold](../../../config/global/mgr.md#SP_mgr_op_history_slow_op_threshold) |

**کارکرد:** Duration of a Manager op to be considered as a historical slow op

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_history_slow_op_threshold 10
ceph config get mgr mgr_op_history_slow_op_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_history_slow_op_threshold
ceph -s
ceph mgr stat
```

---

### mgr_op_log_threshold

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mgr.md#SP_mgr_op_log_threshold](../../../config/global/mgr.md#SP_mgr_op_log_threshold) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mgr mgr_op_log_threshold 5
ceph config get mgr mgr_op_log_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mgr mgr_op_log_threshold
ceph -s
ceph mgr stat
```

---


[← نمای کلی](../OVERVIEW.md)
