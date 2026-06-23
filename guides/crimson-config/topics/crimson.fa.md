# Crimson OSD

deep dive پیکربندی Crimson — 14 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [crimson_allow_pg_split](#crimson_allow_pg_split) | `True` | Advanced | Policy |
| [crimson_bluestore_cpu_set](#crimson_bluestore_cpu_set) | `(empty)` | Advanced | Performance |
| [crimson_bluestore_num_threads](#crimson_bluestore_num_threads) | `6` | Advanced | Performance |
| [crimson_cpu_num](#crimson_cpu_num) | `0` | Advanced | Performance |
| [crimson_cpu_set](#crimson_cpu_set) | `(empty)` | Advanced | Performance |
| [crimson_memory](#crimson_memory) | `0` | Advanced | Performance |
| [crimson_osd_obc_lru_size](#crimson_osd_obc_lru_size) | `512` | Advanced | Performance |
| [crimson_osd_scheduler_concurrency](#crimson_osd_scheduler_concurrency) | `0` | Advanced | Performance |
| [crimson_osd_stat_interval](#crimson_osd_stat_interval) | `0` | Advanced | Performance |
| [crimson_poll_mode](#crimson_poll_mode) | `False` | Advanced | Performance |
| [crimson_reactor_backend](#crimson_reactor_backend) | `(empty)` | Advanced | Performance |
| [crimson_reactor_idle_poll_time_us](#crimson_reactor_idle_poll_time_us) | `200` | Advanced | Performance |
| [crimson_reactor_io_latency_goal_ms](#crimson_reactor_io_latency_goal_ms) | `0` | Advanced | Performance |
| [crimson_reactor_task_quota_ms](#crimson_reactor_task_quota_ms) | `0.5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### crimson_allow_pg_split

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [crimson.md#SP_crimson_allow_pg_split](../../../config/crimson/crimson.md#SP_crimson_allow_pg_split) |

**کارکرد:** Allow Crimson pools to increase their PG count (split)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd crimson_allow_pg_split false
ceph config get osd crimson_allow_pg_split
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_allow_pg_split
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_cpu_set

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_bluestore_cpu_set](../../../config/crimson/crimson.md#SP_crimson_bluestore_cpu_set) |

**کارکرد:** CPU cores on which POSIX threads alienized to seastar will run in cpuset(7) format

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_bluestore_cpu_set "example"
ceph config get osd crimson_bluestore_cpu_set
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_bluestore_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_num_threads

| | |
|---|---|
| نوع | Uint · default `6` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_bluestore_num_threads](../../../config/crimson/crimson.md#SP_crimson_bluestore_num_threads) |

**کارکرد:** The number of POSIX threads alienized to seastar for serving Bluestore

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_bluestore_num_threads 6
ceph config get osd crimson_bluestore_num_threads
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_bluestore_num_threads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_num

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_cpu_num](../../../config/crimson/crimson.md#SP_crimson_cpu_num) |

**کارکرد:** The number of CPUs to use for serving seastar reactors per OSD without CPU pinning.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_cpu_num 64
ceph config get osd crimson_cpu_num
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `32`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_cpu_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_set

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_cpu_set](../../../config/crimson/crimson.md#SP_crimson_cpu_set) |

**کارکرد:** CPU cores on which seastar reactor threads will run in cpuset(7) format per OSD with pinning.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_cpu_set "example"
ceph config get osd crimson_cpu_set
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_memory

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_memory](../../../config/crimson/crimson.md#SP_crimson_memory) |

**کارکرد:** Total memory to use for the seastar allocator per OSD.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_memory 64
ceph config get osd crimson_memory
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_memory
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_obc_lru_size

| | |
|---|---|
| نوع | Uint · default `512` · **Advanced** |
| جدول | [crimson.md#SP_crimson_osd_obc_lru_size](../../../config/crimson/crimson.md#SP_crimson_osd_obc_lru_size) |

**کارکرد:** Number of obcs to cache

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_osd_obc_lru_size 512
ceph config get osd crimson_osd_obc_lru_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `512`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_osd_obc_lru_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_scheduler_concurrency

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [crimson.md#SP_crimson_osd_scheduler_concurrency](../../../config/crimson/crimson.md#SP_crimson_osd_scheduler_concurrency) |

**کارکرد:** The maximum number concurrent IO operations, 0 for unlimited

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_osd_scheduler_concurrency 64
ceph config get osd crimson_osd_scheduler_concurrency
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_osd_scheduler_concurrency
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_stat_interval

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [crimson.md#SP_crimson_osd_stat_interval](../../../config/crimson/crimson.md#SP_crimson_osd_stat_interval) |

**کارکرد:** Report OSD status periodically in seconds, 0 to disable

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd crimson_osd_stat_interval 64
ceph config get osd crimson_osd_stat_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_osd_stat_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_poll_mode

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_poll_mode](../../../config/crimson/crimson.md#SP_crimson_poll_mode) |

**کارکرد:** Let the seastar reactor poll continuously without sleeping at the expense of 100% cpu usage.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set osd crimson_poll_mode true
ceph config get osd crimson_poll_mode
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_poll_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_backend

| | |
|---|---|
| نوع | Str · enum: ["io_uring", "linux-aio", "epoll"] · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_reactor_backend](../../../config/crimson/crimson.md#SP_crimson_reactor_backend) |

**کارکرد:** Select which Seastar's internal reactor implementation

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_reactor_backend "example"
ceph config get osd crimson_reactor_backend
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_reactor_backend
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_idle_poll_time_us

| | |
|---|---|
| نوع | Uint · default `200` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_reactor_idle_poll_time_us](../../../config/crimson/crimson.md#SP_crimson_reactor_idle_poll_time_us) |

**کارکرد:** Seastar's reactor idle polling time (ms) before going back to sleep.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_reactor_idle_poll_time_us 200
ceph config get osd crimson_reactor_idle_poll_time_us
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_reactor_idle_poll_time_us
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_io_latency_goal_ms

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_reactor_io_latency_goal_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_io_latency_goal_ms) |

**کارکرد:** The maximum time (ms) Seastar's reactor IO operations must take. If not set(0 mean not set), defaults to 1.5 * crimson_reactor_task_quota_ms

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_reactor_io_latency_goal_ms 0
ceph config get osd crimson_reactor_io_latency_goal_ms
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_reactor_io_latency_goal_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_task_quota_ms

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [crimson.md#SP_crimson_reactor_task_quota_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_task_quota_ms) |

**کارکرد:** The maximum time (ms) Seastar reactors will wait between polls.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd crimson_reactor_task_quota_ms 0.5
ceph config get osd crimson_reactor_task_quota_ms
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd crimson_reactor_task_quota_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
