# Bdev

راهنمای عمیق پیکربندی Global — 31 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [bdev_aio](#bdev_aio) | `True` | Advanced | Performance |
| [bdev_aio_max_queue_depth](#bdev_aio_max_queue_depth) | `1024` | Advanced | Performance |
| [bdev_aio_poll_ms](#bdev_aio_poll_ms) | `250` | Advanced | Performance |
| [bdev_aio_reap_max](#bdev_aio_reap_max) | `16` | Advanced | Performance |
| [bdev_aio_submit_retry_initial_delay_us](#bdev_aio_submit_retry_initial_delay_us) | `125` | Advanced | Performance |
| [bdev_aio_submit_retry_max](#bdev_aio_submit_retry_max) | `16` | Advanced | Performance |
| [bdev_async_discard](#bdev_async_discard) | `False` | Advanced | Performance |
| [bdev_async_discard_max_pending](#bdev_async_discard_max_pending) | `1000000` | Advanced | Performance |
| [bdev_async_discard_threads](#bdev_async_discard_threads) | `0` | Advanced | Performance |
| [bdev_block_size](#bdev_block_size) | `4_K` | Advanced | Performance |
| [bdev_debug_aio](#bdev_debug_aio) | `False` | Dev | Dev |
| [bdev_debug_aio_log_age](#bdev_debug_aio_log_age) | `5` | Dev | Dev |
| [bdev_debug_aio_suicide_timeout](#bdev_debug_aio_suicide_timeout) | `1_min` | Dev | Dev |
| [bdev_debug_discard_sleep](#bdev_debug_discard_sleep) | `0` | Dev | Dev |
| [bdev_debug_inflight_ios](#bdev_debug_inflight_ios) | `False` | Dev | Dev |
| [bdev_discard_max_bytes](#bdev_discard_max_bytes) | `10_G` | Advanced | Performance |
| [bdev_enable_discard](#bdev_enable_discard) | `False` | Advanced | Policy |
| [bdev_flock_retry](#bdev_flock_retry) | `3` | Advanced | Performance |
| [bdev_flock_retry_interval](#bdev_flock_retry_interval) | `0.1` | Advanced | Performance |
| [bdev_inject_crash](#bdev_inject_crash) | `0` | Dev | Dev |
| [bdev_inject_crash_flush_delay](#bdev_inject_crash_flush_delay) | `2` | Dev | Dev |
| [bdev_ioring](#bdev_ioring) | `False` | Advanced | Performance |
| [bdev_ioring_hipri](#bdev_ioring_hipri) | `False` | Advanced | Performance |
| [bdev_ioring_sqthread_poll](#bdev_ioring_sqthread_poll) | `False` | Advanced | Performance |
| [bdev_max_discard_length](#bdev_max_discard_length) | `2147483648` | Advanced | Performance |
| [bdev_nvme_unbind_from_kernel](#bdev_nvme_unbind_from_kernel) | `False` | Advanced | Performance |
| [bdev_read_buffer_alignment](#bdev_read_buffer_alignment) | `4_K` | Advanced | Performance |
| [bdev_read_preallocated_huge_buffers](#bdev_read_preallocated_huge_buffers) | `(empty)` | Advanced | Performance |
| [bdev_stalled_read_warn_lifetime](#bdev_stalled_read_warn_lifetime) | `86400` | Advanced | Performance |
| [bdev_stalled_read_warn_threshold](#bdev_stalled_read_warn_threshold) | `1` | Advanced | Performance |
| [bdev_type](#bdev_type) | `(empty)` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### bdev_aio

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio](../../../config/global/bdev.md#SP_bdev_aio) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bdev_aio false
ceph config get global bdev_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio
ceph -s
```

---

### bdev_aio_max_queue_depth

| | |
|---|---|
| نوع | Int · default `1024` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio_max_queue_depth](../../../config/global/bdev.md#SP_bdev_aio_max_queue_depth) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bdev_aio_max_queue_depth 1024
ceph config get global bdev_aio_max_queue_depth
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1024`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio_max_queue_depth
ceph -s
```

---

### bdev_aio_poll_ms

| | |
|---|---|
| نوع | Int · default `250` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio_poll_ms](../../../config/global/bdev.md#SP_bdev_aio_poll_ms) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_aio_poll_ms 250
ceph config get global bdev_aio_poll_ms
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `250`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio_poll_ms
ceph -s
```

---

### bdev_aio_reap_max

| | |
|---|---|
| نوع | Int · default `16` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio_reap_max](../../../config/global/bdev.md#SP_bdev_aio_reap_max) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_aio_reap_max 16
ceph config get global bdev_aio_reap_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio_reap_max
ceph -s
```

---

### bdev_aio_submit_retry_initial_delay_us

| | |
|---|---|
| نوع | Int · default `125` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio_submit_retry_initial_delay_us](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_initial_delay_us) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_aio_submit_retry_initial_delay_us 125
ceph config get global bdev_aio_submit_retry_initial_delay_us
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `125`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio_submit_retry_initial_delay_us
ceph -s
```

---

### bdev_aio_submit_retry_max

| | |
|---|---|
| نوع | Int · default `16` · **Advanced** |
| جدول | [bdev.md#SP_bdev_aio_submit_retry_max](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_max) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_aio_submit_retry_max 16
ceph config get global bdev_aio_submit_retry_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_aio_submit_retry_max
ceph -s
```

---

### bdev_async_discard

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_async_discard](../../../config/global/bdev.md#SP_bdev_async_discard) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_async_discard true
ceph config get global bdev_async_discard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_async_discard
ceph -s
```

---

### bdev_async_discard_max_pending

| | |
|---|---|
| نوع | Uint · default `1000000` · **Advanced** |
| جدول | [bdev.md#SP_bdev_async_discard_max_pending](../../../config/global/bdev.md#SP_bdev_async_discard_max_pending) |

**کارکرد:** maximum number of pending discards

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bdev_async_discard_max_pending 1000000
ceph config get global bdev_async_discard_max_pending
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1000000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_async_discard_max_pending
ceph -s
```

---

### bdev_async_discard_threads

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [bdev.md#SP_bdev_async_discard_threads](../../../config/global/bdev.md#SP_bdev_async_discard_threads) |

**کارکرد:** Number of discard threads used to issue discards to the device

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_async_discard_threads 64
ceph config get global bdev_async_discard_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_async_discard_threads
ceph -s
```

---

### bdev_block_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [bdev.md#SP_bdev_block_size](../../../config/global/bdev.md#SP_bdev_block_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_block_size 4_K
ceph config get global bdev_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_block_size
ceph -s
```

---

### bdev_debug_aio

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bdev.md#SP_bdev_debug_aio](../../../config/global/bdev.md#SP_bdev_debug_aio) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_debug_aio true
ceph config get global bdev_debug_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_debug_aio_log_age

| | |
|---|---|
| نوع | Float · default `5` · **Dev** |
| جدول | [bdev.md#SP_bdev_debug_aio_log_age](../../../config/global/bdev.md#SP_bdev_debug_aio_log_age) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_debug_aio_log_age 5
ceph config get global bdev_debug_aio_log_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_debug_aio_suicide_timeout

| | |
|---|---|
| نوع | Float · default `1_min` · **Dev** |
| جدول | [bdev.md#SP_bdev_debug_aio_suicide_timeout](../../../config/global/bdev.md#SP_bdev_debug_aio_suicide_timeout) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_debug_aio_suicide_timeout 1_min
ceph config get global bdev_debug_aio_suicide_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1_min`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_debug_discard_sleep

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [bdev.md#SP_bdev_debug_discard_sleep](../../../config/global/bdev.md#SP_bdev_debug_discard_sleep) |

**کارکرد:** A debugging tool to simulate slow discard operations by introducing a delay of `bdev_debug_discard_sleep` milliseconds

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_debug_discard_sleep 64
ceph config get global bdev_debug_discard_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_debug_inflight_ios

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bdev.md#SP_bdev_debug_inflight_ios](../../../config/global/bdev.md#SP_bdev_debug_inflight_ios) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_debug_inflight_ios true
ceph config get global bdev_debug_inflight_ios
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_discard_max_bytes

| | |
|---|---|
| نوع | Size · default `10_G` · **Advanced** |
| جدول | [bdev.md#SP_bdev_discard_max_bytes](../../../config/global/bdev.md#SP_bdev_discard_max_bytes) |

**کارکرد:** Discard queue size in bytes that triggers health warning

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bdev_discard_max_bytes 10_G
ceph config get global bdev_discard_max_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_discard_max_bytes
ceph -s
```

---

### bdev_enable_discard

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_enable_discard](../../../config/global/bdev.md#SP_bdev_enable_discard) |

**کارکرد:** Enable OSD devices trimming during in runtime

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_enable_discard true
ceph config get global bdev_enable_discard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_enable_discard
ceph -s
```

---

### bdev_flock_retry

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [bdev.md#SP_bdev_flock_retry](../../../config/global/bdev.md#SP_bdev_flock_retry) |

**کارکرد:** times to retry the flock

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_flock_retry 3
ceph config get global bdev_flock_retry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_flock_retry
ceph -s
```

---

### bdev_flock_retry_interval

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [bdev.md#SP_bdev_flock_retry_interval](../../../config/global/bdev.md#SP_bdev_flock_retry_interval) |

**کارکرد:** Interval after which to retry flock

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global bdev_flock_retry_interval 0.1
ceph config get global bdev_flock_retry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_flock_retry_interval
ceph -s
```

---

### bdev_inject_crash

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [bdev.md#SP_bdev_inject_crash](../../../config/global/bdev.md#SP_bdev_inject_crash) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_inject_crash 64
ceph config get global bdev_inject_crash
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_inject_crash_flush_delay

| | |
|---|---|
| نوع | Int · default `2` · **Dev** |
| جدول | [bdev.md#SP_bdev_inject_crash_flush_delay](../../../config/global/bdev.md#SP_bdev_inject_crash_flush_delay) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bdev_inject_crash_flush_delay 2
ceph config get global bdev_inject_crash_flush_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bdev_ioring

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_ioring](../../../config/global/bdev.md#SP_bdev_ioring) |

**کارکرد:** Enables the Linux io_uring API instead of libaio

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_ioring true
ceph config get global bdev_ioring
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_ioring
ceph -s
```

---

### bdev_ioring_hipri

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_ioring_hipri](../../../config/global/bdev.md#SP_bdev_ioring_hipri) |

**کارکرد:** Enables Linux io_uring API Use polled IO completions

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_ioring_hipri true
ceph config get global bdev_ioring_hipri
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_ioring_hipri
ceph -s
```

---

### bdev_ioring_sqthread_poll

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_ioring_sqthread_poll](../../../config/global/bdev.md#SP_bdev_ioring_sqthread_poll) |

**کارکرد:** Enables Linux io_uring API Offload submission/completion to kernel thread

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_ioring_sqthread_poll true
ceph config get global bdev_ioring_sqthread_poll
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_ioring_sqthread_poll
ceph -s
```

---

### bdev_max_discard_length

| | |
|---|---|
| نوع | Uint · default `2147483648` · **Advanced** |
| جدول | [bdev.md#SP_bdev_max_discard_length](../../../config/global/bdev.md#SP_bdev_max_discard_length) |

**کارکرد:** Maximum length of a single discard request

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bdev_max_discard_length 2147483648
ceph config get global bdev_max_discard_length
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2147483648`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_max_discard_length
ceph -s
```

---

### bdev_nvme_unbind_from_kernel

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bdev.md#SP_bdev_nvme_unbind_from_kernel](../../../config/global/bdev.md#SP_bdev_nvme_unbind_from_kernel) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bdev_nvme_unbind_from_kernel true
ceph config get global bdev_nvme_unbind_from_kernel
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_nvme_unbind_from_kernel
ceph -s
```

---

### bdev_read_buffer_alignment

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [bdev.md#SP_bdev_read_buffer_alignment](../../../config/global/bdev.md#SP_bdev_read_buffer_alignment) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_read_buffer_alignment 4_K
ceph config get global bdev_read_buffer_alignment
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_read_buffer_alignment
ceph -s
```

---

### bdev_read_preallocated_huge_buffers

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [bdev.md#SP_bdev_read_preallocated_huge_buffers](../../../config/global/bdev.md#SP_bdev_read_preallocated_huge_buffers) |

**کارکرد:** description of pools arrangement for huge page-based read buffers

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_read_preallocated_huge_buffers "example"
ceph config get global bdev_read_preallocated_huge_buffers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_read_preallocated_huge_buffers
ceph -s
```

---

### bdev_stalled_read_warn_lifetime

| | |
|---|---|
| نوع | Uint · default `86400` · **Advanced** |
| جدول | [bdev.md#SP_bdev_stalled_read_warn_lifetime](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_lifetime) |

**کارکرد:** A configurable duration for a stalled read warning to be raised when the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_stalled_read_warn_lifetime 86400
ceph config get global bdev_stalled_read_warn_lifetime
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `86400`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_stalled_read_warn_lifetime
ceph -s
```

---

### bdev_stalled_read_warn_threshold

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [bdev.md#SP_bdev_stalled_read_warn_threshold](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_threshold) |

**کارکرد:** A configurable number for stalled read warnings to be raised if the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_stalled_read_warn_threshold 1
ceph config get global bdev_stalled_read_warn_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_stalled_read_warn_threshold
ceph -s
```

---

### bdev_type

| | |
|---|---|
| نوع | Str · enum: ["aio", "spdk", "pmem"] · default `(empty)` · **Advanced** |
| جدول | [bdev.md#SP_bdev_type](../../../config/global/bdev.md#SP_bdev_type) |

**کارکرد:** Explicitly set the device type to select the driver if needed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bdev_type "example"
ceph config get global bdev_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bdev_type
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
