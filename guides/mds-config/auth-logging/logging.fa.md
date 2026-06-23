# Logging

راهنمای عمیق پیکربندی MDS — 15 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_kill_after_journal_logs_flushed](#mds_kill_after_journal_logs_flushed) | `False` | Dev | توسعه |
| [mds_log_event_large_threshold](#mds_log_event_large_threshold) | `512_K` | Advanced | عملکرد |
| [mds_log_events_per_segment](#mds_log_events_per_segment) | `1024` | Advanced | عملکرد |
| [mds_log_max_events](#mds_log_max_events) | `-1` | Advanced | عملکرد |
| [mds_log_max_segments](#mds_log_max_segments) | `128` | Advanced | عملکرد |
| [mds_log_minor_segments_per_major_segment](#mds_log_minor_segments_per_major_segment) | `16` | Advanced | عملکرد |
| [mds_log_pause](#mds_log_pause) | `False` | Dev | توسعه |
| [mds_log_segment_size](#mds_log_segment_size) | `0` | Advanced | عملکرد |
| [mds_log_skip_corrupt_events](#mds_log_skip_corrupt_events) | `False` | Dev | توسعه |
| [mds_log_skip_unbounded_events](#mds_log_skip_unbounded_events) | `False` | Dev | توسعه |
| [mds_log_trim_decay_rate](#mds_log_trim_decay_rate) | `1.0` | Advanced | عملکرد |
| [mds_log_trim_threshold](#mds_log_trim_threshold) | `128` | Advanced | عملکرد |
| [mds_log_trim_upkeep_interval](#mds_log_trim_upkeep_interval) | `1000` | Advanced | عملکرد |
| [mds_log_warn_factor](#mds_log_warn_factor) | `2` | Advanced | عملکرد |
| [mds_op_log_threshold](#mds_op_log_threshold) | `5` | Dev | توسعه |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_kill_after_journal_logs_flushed

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_kill_after_journal_logs_flushed](../../../config/mds/mds.md#SP_mds_kill_after_journal_logs_flushed) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_after_journal_logs_flushed true
ceph config get mds mds_kill_after_journal_logs_flushed
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_log_event_large_threshold

| | |
|---|---|
| نوع | Uint · default `512_K` · **Advanced** |
| جدول | [mds.md#SP_mds_log_event_large_threshold](../../../config/mds/mds.md#SP_mds_log_event_large_threshold) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_event_large_threshold 512_K
ceph config get mds mds_log_event_large_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `512_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1_K`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_event_large_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_events_per_segment

| | |
|---|---|
| نوع | Uint · default `1024` · **Advanced** |
| جدول | [mds.md#SP_mds_log_events_per_segment](../../../config/mds/mds.md#SP_mds_log_events_per_segment) |

**کارکرد:** maximum number of events in an MDS journal segment

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_events_per_segment 1024
ceph config get mds mds_log_events_per_segment
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1024`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_events_per_segment
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_max_events

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [mds.md#SP_mds_log_max_events](../../../config/mds/mds.md#SP_mds_log_max_events) |

**کارکرد:** Maximum journal events before the MDS forces a segment rollover.

**زمان استفاده:** Advanced — affects journal segmentation and recovery time after crash.

**مثال:**

```bash
ceph config set mds mds_log_max_events 128
ceph config get mds mds_log_max_events
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_max_events
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_max_segments

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [mds.md#SP_mds_log_max_segments](../../../config/mds/mds.md#SP_mds_log_max_segments) |

**کارکرد:** maximum number of segments which may be untrimmed

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_log_max_segments 128
ceph config get mds mds_log_max_segments
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `8`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_max_segments
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_minor_segments_per_major_segment

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [mds.md#SP_mds_log_minor_segments_per_major_segment](../../../config/mds/mds.md#SP_mds_log_minor_segments_per_major_segment) |

**کارکرد:** Number of minor segments per major segment.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_minor_segments_per_major_segment 16
ceph config get mds mds_log_minor_segments_per_major_segment
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `4`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_minor_segments_per_major_segment
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_pause

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_log_pause](../../../config/mds/mds.md#SP_mds_log_pause) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_log_pause true
ceph config get mds mds_log_pause
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_log_segment_size

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_log_segment_size](../../../config/mds/mds.md#SP_mds_log_segment_size) |

**کارکرد:** size in bytes of each MDS log segment

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_segment_size 64
ceph config get mds mds_log_segment_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_segment_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_skip_corrupt_events

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_log_skip_corrupt_events](../../../config/mds/mds.md#SP_mds_log_skip_corrupt_events) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_log_skip_corrupt_events true
ceph config get mds mds_log_skip_corrupt_events
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_log_skip_unbounded_events

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_log_skip_unbounded_events](../../../config/mds/mds.md#SP_mds_log_skip_unbounded_events) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_log_skip_unbounded_events true
ceph config get mds mds_log_skip_unbounded_events
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_log_trim_decay_rate

| | |
|---|---|
| نوع | Float · default `1.0` · **Advanced** |
| جدول | [mds.md#SP_mds_log_trim_decay_rate](../../../config/mds/mds.md#SP_mds_log_trim_decay_rate) |

**کارکرد:** MDS log trim decay rate

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_trim_decay_rate 1.0
ceph config get mds mds_log_trim_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1.0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0.01`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_trim_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_trim_threshold

| | |
|---|---|
| نوع | Size · default `128` · **Advanced** |
| جدول | [mds.md#SP_mds_log_trim_threshold](../../../config/mds/mds.md#SP_mds_log_trim_threshold) |

**کارکرد:** MDS log trim threshold

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_trim_threshold 128
ceph config get mds mds_log_trim_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_trim_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_trim_upkeep_interval

| | |
|---|---|
| نوع | Millisecs · default `1000` · **Advanced** |
| جدول | [mds.md#SP_mds_log_trim_upkeep_interval](../../../config/mds/mds.md#SP_mds_log_trim_upkeep_interval) |

**کارکرد:** MDS log trimming interval

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_log_trim_upkeep_interval 1000
ceph config get mds mds_log_trim_upkeep_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_log_trim_upkeep_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_log_warn_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mds.md#SP_mds_log_warn_factor](../../../config/mds/mds.md#SP_mds_log_warn_factor) |

**کارکرد:** trigger MDS_HEALTH_TRIM warning when the mds log is longer than mds_log_max_segments * mds_log_warn_factor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_log_warn_factor 2
ceph config get mds mds_log_warn_factor
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
ceph config get mds mds_log_warn_factor
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_log_threshold

| | |
|---|---|
| نوع | Int · default `5` · **Dev** |
| جدول | [mds.md#SP_mds_op_log_threshold](../../../config/mds/mds.md#SP_mds_op_log_threshold) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_op_log_threshold 5
ceph config get mds mds_op_log_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
