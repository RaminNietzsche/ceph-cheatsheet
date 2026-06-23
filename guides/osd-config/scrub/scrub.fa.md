# Scrub

راهنمای عمیق پیکربندی OSD — 39 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_blocked_scrub_grace_period](#osd_blocked_scrub_grace_period) | `120` | Advanced | عملکرد |
| [osd_deep_scrub_interval](#osd_deep_scrub_interval) | `7_day` | Advanced | عملکرد |
| [osd_deep_scrub_interval_cv](#osd_deep_scrub_interval_cv) | `0.2` | Advanced | عملکرد |
| [osd_deep_scrub_keys](#osd_deep_scrub_keys) | `1024` | Advanced | عملکرد |
| [osd_deep_scrub_large_omap_object_key_threshold](#osd_deep_scrub_large_omap_object_key_threshold) | `200000` | Advanced | عملکرد |
| [osd_deep_scrub_large_omap_object_value_sum_threshold](#osd_deep_scrub_large_omap_object_value_sum_threshold) | `1_G` | Advanced | عملکرد |
| [osd_deep_scrub_randomize_ratio](#osd_deep_scrub_randomize_ratio) | `0.15` | Advanced | عملکرد |
| [osd_deep_scrub_stride](#osd_deep_scrub_stride) | `4_M` | Advanced | عملکرد |
| [osd_deep_scrub_update_digest_min_age](#osd_deep_scrub_update_digest_min_age) | `2_hr` | Advanced | عملکرد |
| [osd_max_scrubs](#osd_max_scrubs) | `3` | Advanced | عملکرد |
| [osd_scrub_auto_repair](#osd_scrub_auto_repair) | `False` | Advanced | عملکرد |
| [osd_scrub_auto_repair_num_errors](#osd_scrub_auto_repair_num_errors) | `5` | Advanced | عملکرد |
| [osd_scrub_backoff_ratio](#osd_scrub_backoff_ratio) | `0.66` | Dev | توسعه |
| [osd_scrub_begin_hour](#osd_scrub_begin_hour) | `0` | Advanced | عملکرد |
| [osd_scrub_begin_week_day](#osd_scrub_begin_week_day) | `0` | Advanced | عملکرد |
| [osd_scrub_chunk_max](#osd_scrub_chunk_max) | `15` | Advanced | عملکرد |
| [osd_scrub_chunk_min](#osd_scrub_chunk_min) | `5` | Advanced | عملکرد |
| [osd_scrub_disable_reservation_queuing](#osd_scrub_disable_reservation_queuing) | `False` | Advanced | سیاست |
| [osd_scrub_during_recovery](#osd_scrub_during_recovery) | `False` | Advanced | عملکرد |
| [osd_scrub_end_hour](#osd_scrub_end_hour) | `0` | Advanced | عملکرد |
| [osd_scrub_end_week_day](#osd_scrub_end_week_day) | `0` | Advanced | عملکرد |
| [osd_scrub_extended_sleep](#osd_scrub_extended_sleep) | `0` | Advanced | عملکرد |
| [osd_scrub_interval_randomize_ratio](#osd_scrub_interval_randomize_ratio) | `0.5` | Advanced | عملکرد |
| [osd_scrub_invalid_stats](#osd_scrub_invalid_stats) | `True` | Advanced | عملکرد |
| [osd_scrub_load_threshold](#osd_scrub_load_threshold) | `10.0` | Advanced | عملکرد |
| [osd_scrub_max_interval](#osd_scrub_max_interval) | `7_day` | Advanced | عملکرد |
| [osd_scrub_max_preemptions](#osd_scrub_max_preemptions) | `5` | Advanced | عملکرد |
| [osd_scrub_min_interval](#osd_scrub_min_interval) | `1_day` | Advanced | عملکرد |
| [osd_scrub_queued_snaptrims_limit](#osd_scrub_queued_snaptrims_limit) | `500` | Advanced | عملکرد |
| [osd_scrub_retry_after_noscrub](#osd_scrub_retry_after_noscrub) | `60` | Advanced | عملکرد |
| [osd_scrub_retry_delay](#osd_scrub_retry_delay) | `30` | Advanced | عملکرد |
| [osd_scrub_retry_new_interval](#osd_scrub_retry_new_interval) | `10` | Advanced | عملکرد |
| [osd_scrub_retry_pg_state](#osd_scrub_retry_pg_state) | `60` | Advanced | عملکرد |
| [osd_scrub_retry_trimming](#osd_scrub_retry_trimming) | `10` | Advanced | عملکرد |
| [osd_scrub_sleep](#osd_scrub_sleep) | `0` | Advanced | عملکرد |
| [osd_shallow_scrub_chunk_max](#osd_shallow_scrub_chunk_max) | `100` | Advanced | عملکرد |
| [osd_shallow_scrub_chunk_min](#osd_shallow_scrub_chunk_min) | `50` | Advanced | عملکرد |
| [osd_stats_update_period_not_scrubbing](#osd_stats_update_period_not_scrubbing) | `120` | Advanced | عملکرد |
| [osd_stats_update_period_scrubbing](#osd_stats_update_period_scrubbing) | `15` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_blocked_scrub_grace_period

| | |
|---|---|
| نوع | Int · default `120` · **Advanced** |
| جدول | [osd.md#SP_osd_blocked_scrub_grace_period](../../../config/osd/osd.md#SP_osd_blocked_scrub_grace_period) |

**کارکرد:** Time (seconds) before issuing a cluster-log warning

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_blocked_scrub_grace_period 120
ceph config get osd osd_blocked_scrub_grace_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `120`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_blocked_scrub_grace_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_interval

| | |
|---|---|
| نوع | Float · default `7_day` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_interval](../../../config/osd/osd.md#SP_osd_deep_scrub_interval) |

**کارکرد:** Interval (seconds) between deep scrubs that verify full object checksums.

**زمان استفاده:** Shorten for compliance-heavy environments; lengthen on large HDD pools where deep scrub IO is costly.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_interval 7_day
ceph config get osd osd_deep_scrub_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `7_day`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_interval_cv

| | |
|---|---|
| نوع | Float · default `0.2` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_interval_cv](../../../config/osd/osd.md#SP_osd_deep_scrub_interval_cv) |

**کارکرد:** Determines the amount of variation in the deep scrub interval

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_interval_cv 0.2
ceph config get osd osd_deep_scrub_interval_cv
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `0.4`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_interval_cv
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_keys

| | |
|---|---|
| نوع | Int · default `1024` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_keys](../../../config/osd/osd.md#SP_osd_deep_scrub_keys) |

**کارکرد:** Number of keys to read from an object at a time during deep scrub

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_keys 1024
ceph config get osd osd_deep_scrub_keys
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1024`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_keys
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_large_omap_object_key_threshold

| | |
|---|---|
| نوع | Uint · default `200000` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_key_threshold) |

**کارکرد:** Warn when we encounter an object with more omap keys than this

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_key_threshold 200000
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `200000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_large_omap_object_key_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_large_omap_object_value_sum_threshold

| | |
|---|---|
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold](../../../config/osd/osd.md#SP_osd_deep_scrub_large_omap_object_value_sum_threshold) |

**کارکرد:** Warn when we encounter an object with more omap key bytes than this

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_large_omap_object_value_sum_threshold 1_G
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_large_omap_object_value_sum_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_randomize_ratio

| | |
|---|---|
| نوع | Float · default `0.15` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_randomize_ratio](../../../config/osd/osd.md#SP_osd_deep_scrub_randomize_ratio) |

**کارکرد:** deprecated. Has no effect.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_randomize_ratio 0.15
ceph config get osd osd_deep_scrub_randomize_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_stride

| | |
|---|---|
| نوع | Size · default `4_M` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_stride](../../../config/osd/osd.md#SP_osd_deep_scrub_stride) |

**کارکرد:** Number of bytes to read from an object at a time during deep scrub

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_stride 4_M
ceph config get osd osd_deep_scrub_stride
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_stride
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_deep_scrub_update_digest_min_age

| | |
|---|---|
| نوع | Int · default `2_hr` · **Advanced** |
| جدول | [osd.md#SP_osd_deep_scrub_update_digest_min_age](../../../config/osd/osd.md#SP_osd_deep_scrub_update_digest_min_age) |

**کارکرد:** Update overall object digest only if object was last modified longer ago than this

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_deep_scrub_update_digest_min_age 2_hr
ceph config get osd osd_deep_scrub_update_digest_min_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2_hr`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_deep_scrub_update_digest_min_age
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_scrubs

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [osd.md#SP_osd_max_scrubs](../../../config/osd/osd.md#SP_osd_max_scrubs) |

**کارکرد:** Maximum concurrent scrub operations per OSD. Scrub reads object data to verify checksums — too many scrubs compete with client I/O.

**زمان استفاده:** Increase cautiously on fast media when scrubs lag behind the scrub interval. Decrease when `ceph -s` reports slow ops or OSD latency spikes during scrub windows.

**مثال:**

```bash
ceph config set osd osd_max_scrubs 3
ceph config get osd osd_max_scrubs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_scrubs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

Pair with `osd_scrub_sleep` and deep-scrub intervals. HDD clusters often stay at 1; NVMe may tolerate 2–3 if load is low.

---

### osd_scrub_auto_repair

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_auto_repair](../../../config/osd/osd.md#SP_osd_scrub_auto_repair) |

**کارکرد:** Automatically repair damaged objects detected during scrub

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_auto_repair true
ceph config get osd osd_scrub_auto_repair
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_auto_repair
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_auto_repair_num_errors

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_auto_repair_num_errors](../../../config/osd/osd.md#SP_osd_scrub_auto_repair_num_errors) |

**کارکرد:** Maximum number of damaged objects to automatically repair

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_auto_repair_num_errors 5
ceph config get osd osd_scrub_auto_repair_num_errors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_auto_repair_num_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_backoff_ratio

| | |
|---|---|
| نوع | Float · default `0.66` · **Dev** |
| جدول | [osd.md#SP_osd_scrub_backoff_ratio](../../../config/osd/osd.md#SP_osd_scrub_backoff_ratio) |

**کارکرد:** Backoff ratio for scheduling scrubs

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_scrub_backoff_ratio 0.66
ceph config get osd osd_scrub_backoff_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.66`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_scrub_begin_hour

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_begin_hour](../../../config/osd/osd.md#SP_osd_scrub_begin_hour) |

**کارکرد:** Restrict scrubbing to this hour of the day or later

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_begin_hour 64
ceph config get osd osd_scrub_begin_hour
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `23`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_begin_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_begin_week_day

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_begin_week_day](../../../config/osd/osd.md#SP_osd_scrub_begin_week_day) |

**کارکرد:** Restrict scrubbing to this day of the week or later

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_begin_week_day 64
ceph config get osd osd_scrub_begin_week_day
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `6`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_begin_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_chunk_max

| | |
|---|---|
| نوع | Int · default `15` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_scrub_chunk_max) |

**کارکرد:** Maximum number of objects to deep-scrub in a single chunk

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_chunk_max 15
ceph config get osd osd_scrub_chunk_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_chunk_min

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_scrub_chunk_min) |

**کارکرد:** Minimum number of objects to deep-scrub in a single chunk

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_chunk_min 5
ceph config get osd osd_scrub_chunk_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_disable_reservation_queuing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_disable_reservation_queuing](../../../config/osd/osd.md#SP_osd_scrub_disable_reservation_queuing) |

**کارکرد:** Disable queuing of scrub reservations

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_disable_reservation_queuing true
ceph config get osd osd_scrub_disable_reservation_queuing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_disable_reservation_queuing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_during_recovery

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_during_recovery](../../../config/osd/osd.md#SP_osd_scrub_during_recovery) |

**کارکرد:** Allow scrubbing when PGs on the OSD are undergoing recovery

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_during_recovery true
ceph config get osd osd_scrub_during_recovery
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_during_recovery
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_end_hour

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_end_hour](../../../config/osd/osd.md#SP_osd_scrub_end_hour) |

**کارکرد:** Restrict scrubbing to hours of the day earlier than this

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_end_hour 64
ceph config get osd osd_scrub_end_hour
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `23`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_end_hour
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_end_week_day

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_end_week_day](../../../config/osd/osd.md#SP_osd_scrub_end_week_day) |

**کارکرد:** Restrict scrubbing to days of the week earlier than this

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_end_week_day 64
ceph config get osd osd_scrub_end_week_day
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `6`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_end_week_day
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_extended_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_extended_sleep](../../../config/osd/osd.md#SP_osd_scrub_extended_sleep) |

**کارکرد:** Duration (in seconds) of delay injected between chunks when scrubbing out of scrubbing hours

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_scrub_extended_sleep 0
ceph config get osd osd_scrub_extended_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_extended_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_interval_randomize_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_interval_randomize_ratio](../../../config/osd/osd.md#SP_osd_scrub_interval_randomize_ratio) |

**کارکرد:** Ratio of scrub interval to randomly vary

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_scrub_interval_randomize_ratio 0.5
ceph config get osd osd_scrub_interval_randomize_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_interval_randomize_ratio
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_invalid_stats

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_invalid_stats](../../../config/osd/osd.md#SP_osd_scrub_invalid_stats) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_invalid_stats false
ceph config get osd osd_scrub_invalid_stats
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_invalid_stats
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_load_threshold

| | |
|---|---|
| نوع | Float · default `10.0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_load_threshold](../../../config/osd/osd.md#SP_osd_scrub_load_threshold) |

**کارکرد:** Allow scrubbing when system load divided by number of CPUs is below this value

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_load_threshold 10.0
ceph config get osd osd_scrub_load_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10.0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_load_threshold
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_max_interval

| | |
|---|---|
| نوع | Float · default `7_day` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_max_interval](../../../config/osd/osd.md#SP_osd_scrub_max_interval) |

**کارکرد:** Maximum interval (seconds) between shallow scrubs for a PG.

**زمان استفاده:** Align with maintenance policy. Monitor `mon_warn_pg_not_scrubbed_ratio` warnings.

**مثال:**

```bash
ceph config set osd osd_scrub_max_interval 7_day
ceph config get osd osd_scrub_max_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `7_day`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_max_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_max_preemptions

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_max_preemptions](../../../config/osd/osd.md#SP_osd_scrub_max_preemptions) |

**کارکرد:** Set the maximum number of times we will preempt a deep scrub due to a client operation before blocking client IO to complete the scrub

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_max_preemptions 5
ceph config get osd osd_scrub_max_preemptions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `30`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_max_preemptions
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_min_interval

| | |
|---|---|
| نوع | Float · default `1_day` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_min_interval](../../../config/osd/osd.md#SP_osd_scrub_min_interval) |

**کارکرد:** The desired interval between scrubs of a specific PG. Note that this option must be set at ``global`` scope, or for both ``mgr`` and``osd``.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_min_interval 1_day
ceph config get osd osd_scrub_min_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_day`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_min_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_queued_snaptrims_limit

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_queued_snaptrims_limit](../../../config/osd/osd.md#SP_osd_scrub_queued_snaptrims_limit) |

**کارکرد:** Do not initiate periodic scrubs when the total snap-trim queues across all PGs exceeds this value. A value of '0' disables this limit.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_scrub_queued_snaptrims_limit 500
ceph config get osd osd_scrub_queued_snaptrims_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_queued_snaptrims_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_after_noscrub

| | |
|---|---|
| نوع | Int · default `60` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_retry_after_noscrub](../../../config/osd/osd.md#SP_osd_scrub_retry_after_noscrub) |

**کارکرد:** Period (in seconds) before retrying to scrub a PG at a specific level after detecting a no-scrub or no-deep-scrub flag

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_retry_after_noscrub 60
ceph config get osd osd_scrub_retry_after_noscrub
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
ceph config get osd osd_scrub_retry_after_noscrub
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_delay

| | |
|---|---|
| نوع | Int · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_retry_delay](../../../config/osd/osd.md#SP_osd_scrub_retry_delay) |

**کارکرد:** Period (in seconds) before retrying a PG that has failed a prior scrub.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_retry_delay 30
ceph config get osd osd_scrub_retry_delay
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
ceph config get osd osd_scrub_retry_delay
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_new_interval

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_retry_new_interval](../../../config/osd/osd.md#SP_osd_scrub_retry_new_interval) |

**کارکرد:** Period (in seconds) before retrying a scrub aborted on a new interval

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_scrub_retry_new_interval 10
ceph config get osd osd_scrub_retry_new_interval
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
ceph config get osd osd_scrub_retry_new_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_pg_state

| | |
|---|---|
| نوع | Int · default `60` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_retry_pg_state](../../../config/osd/osd.md#SP_osd_scrub_retry_pg_state) |

**کارکرد:** Period (in seconds) before retrying to scrub a previously inactive/not-clean PG

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_retry_pg_state 60
ceph config get osd osd_scrub_retry_pg_state
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
ceph config get osd osd_scrub_retry_pg_state
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_retry_trimming

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_retry_trimming](../../../config/osd/osd.md#SP_osd_scrub_retry_trimming) |

**کارکرد:** Period (in seconds) before retrying to scrub a previously snap-trimming PG

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_scrub_retry_trimming 10
ceph config get osd osd_scrub_retry_trimming
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
ceph config get osd osd_scrub_retry_trimming
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_scrub_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_scrub_sleep](../../../config/osd/osd.md#SP_osd_scrub_sleep) |

**کارکرد:** Duration (in seconds) of delay injected between chunks when scrubbing

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_scrub_sleep 0
ceph config get osd osd_scrub_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_scrub_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shallow_scrub_chunk_max

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [osd.md#SP_osd_shallow_scrub_chunk_max](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_max) |

**کارکرد:** Maximum number of objects to scrub in a single chunk

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_shallow_scrub_chunk_max 100
ceph config get osd osd_shallow_scrub_chunk_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_shallow_scrub_chunk_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_shallow_scrub_chunk_min

| | |
|---|---|
| نوع | Int · default `50` · **Advanced** |
| جدول | [osd.md#SP_osd_shallow_scrub_chunk_min](../../../config/osd/osd.md#SP_osd_shallow_scrub_chunk_min) |

**کارکرد:** Minimum number of objects to scrub in a single chunk

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_shallow_scrub_chunk_min 50
ceph config get osd osd_shallow_scrub_chunk_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_shallow_scrub_chunk_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_stats_update_period_not_scrubbing

| | |
|---|---|
| نوع | Int · default `120` · **Advanced** |
| جدول | [osd.md#SP_osd_stats_update_period_not_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_not_scrubbing) |

**کارکرد:** Stats update period (seconds) when not scrubbing

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_stats_update_period_not_scrubbing 120
ceph config get osd osd_stats_update_period_not_scrubbing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `120`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_stats_update_period_not_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_stats_update_period_scrubbing

| | |
|---|---|
| نوع | Int · default `15` · **Advanced** |
| جدول | [osd.md#SP_osd_stats_update_period_scrubbing](../../../config/osd/osd.md#SP_osd_stats_update_period_scrubbing) |

**کارکرد:** Stats update period (seconds) when scrubbing

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_stats_update_period_scrubbing 15
ceph config get osd osd_stats_update_period_scrubbing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_stats_update_period_scrubbing
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
