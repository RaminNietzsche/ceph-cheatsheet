# Recovery & backfill

راهنمای عمیق پیکربندی OSD — 28 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_allow_recovery_below_min_size](#osd_allow_recovery_below_min_size) | `True` | Dev | Dev |
| [osd_backfill_retry_interval](#osd_backfill_retry_interval) | `30` | Advanced | Performance |
| [osd_backfill_scan_max](#osd_backfill_scan_max) | `512` | Advanced | Performance |
| [osd_backfill_scan_min](#osd_backfill_scan_min) | `64` | Advanced | Performance |
| [osd_max_backfills](#osd_max_backfills) | `1` | Advanced | Performance |
| [osd_mclock_override_recovery_settings](#osd_mclock_override_recovery_settings) | `False` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_lim](#osd_mclock_scheduler_background_recovery_lim) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_res](#osd_mclock_scheduler_background_recovery_res) | `0` | Advanced | Performance |
| [osd_mclock_scheduler_background_recovery_wgt](#osd_mclock_scheduler_background_recovery_wgt) | `1` | Advanced | Performance |
| [osd_min_recovery_priority](#osd_min_recovery_priority) | `0` | Advanced | Performance |
| [osd_recover_clone_overlap](#osd_recover_clone_overlap) | `True` | Advanced | Performance |
| [osd_recover_clone_overlap_limit](#osd_recover_clone_overlap_limit) | `10` | Advanced | Performance |
| [osd_recovery_delay_start](#osd_recovery_delay_start) | `0` | Advanced | Performance |
| [osd_recovery_max_active](#osd_recovery_max_active) | `0` | Advanced | Performance |
| [osd_recovery_max_active_hdd](#osd_recovery_max_active_hdd) | `3` | Advanced | Performance |
| [osd_recovery_max_active_ssd](#osd_recovery_max_active_ssd) | `10` | Advanced | Performance |
| [osd_recovery_max_chunk](#osd_recovery_max_chunk) | `8_M` | Advanced | Performance |
| [osd_recovery_max_omap_entries_per_chunk](#osd_recovery_max_omap_entries_per_chunk) | `8096` | Advanced | Performance |
| [osd_recovery_max_single_start](#osd_recovery_max_single_start) | `1` | Advanced | Performance |
| [osd_recovery_retry_interval](#osd_recovery_retry_interval) | `30` | Advanced | Performance |
| [osd_recovery_sleep](#osd_recovery_sleep) | `0` | Advanced | Performance |
| [osd_recovery_sleep_degraded](#osd_recovery_sleep_degraded) | `0` | Advanced | Performance |
| [osd_recovery_sleep_degraded_hdd](#osd_recovery_sleep_degraded_hdd) | `0.1` | Advanced | Performance |
| [osd_recovery_sleep_degraded_hybrid](#osd_recovery_sleep_degraded_hybrid) | `0.025` | Advanced | Performance |
| [osd_recovery_sleep_degraded_ssd](#osd_recovery_sleep_degraded_ssd) | `0` | Advanced | Performance |
| [osd_recovery_sleep_hdd](#osd_recovery_sleep_hdd) | `0.1` | Advanced | Performance |
| [osd_recovery_sleep_hybrid](#osd_recovery_sleep_hybrid) | `0.025` | Advanced | Performance |
| [osd_recovery_sleep_ssd](#osd_recovery_sleep_ssd) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_allow_recovery_below_min_size

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [osd.md#SP_osd_allow_recovery_below_min_size](../../../config/osd/osd.md#SP_osd_allow_recovery_below_min_size) |

**کارکرد:** allow replicated pools to recover with < min_size active members

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_allow_recovery_below_min_size false
ceph config get osd osd_allow_recovery_below_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_backfill_retry_interval

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_backfill_retry_interval](../../../config/osd/osd.md#SP_osd_backfill_retry_interval) |

**کارکرد:** how frequently to retry backfill reservations after being denied (e.g., due to a full OSD)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_backfill_retry_interval 30
ceph config get osd osd_backfill_retry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backfill_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backfill_scan_max

| | |
|---|---|
| نوع | Int · default `512` · **Advanced** |
| جدول | [osd.md#SP_osd_backfill_scan_max](../../../config/osd/osd.md#SP_osd_backfill_scan_max) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_backfill_scan_max 512
ceph config get osd osd_backfill_scan_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `512`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backfill_scan_max
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_backfill_scan_min

| | |
|---|---|
| نوع | Int · default `64` · **Advanced** |
| جدول | [osd.md#SP_osd_backfill_scan_min](../../../config/osd/osd.md#SP_osd_backfill_scan_min) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_backfill_scan_min 64
ceph config get osd osd_backfill_scan_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_backfill_scan_min
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_backfills

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_max_backfills](../../../config/osd/osd.md#SP_osd_max_backfills) |

**کارکرد:** Maximum number of concurrent local and remote backfills or recoveries per OSD

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_backfills 1
ceph config get osd osd_max_backfills
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_max_backfills
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_override_recovery_settings

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_override_recovery_settings](../../../config/osd/osd.md#SP_osd_mclock_override_recovery_settings) |

**کارکرد:** Setting this option enables the override of recovery/backfill limits for the mClock scheduler.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_override_recovery_settings true
ceph config get osd osd_mclock_override_recovery_settings
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_override_recovery_settings
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_recovery_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_lim) |

**کارکرد:** IO limit for background recovery over reservation. The default value of 0 specifies no limit enforcement, which means background recovery operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background recovery operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_lim 0
ceph config get osd osd_mclock_scheduler_background_recovery_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_res

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_recovery_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_res) |

**کارکرد:** IO proportion reserved for background recovery (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background recovery operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_res 0
ceph config get osd osd_mclock_scheduler_background_recovery_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_recovery_wgt

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_recovery_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_recovery_wgt) |

**کارکرد:** IO share for each background recovery over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_recovery_wgt 1
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_recovery_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_min_recovery_priority

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_min_recovery_priority](../../../config/osd/osd.md#SP_osd_min_recovery_priority) |

**کارکرد:** Minimum priority below which recovery is not performed

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_min_recovery_priority 64
ceph config get osd osd_min_recovery_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_min_recovery_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recover_clone_overlap

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_recover_clone_overlap](../../../config/osd/osd.md#SP_osd_recover_clone_overlap) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_recover_clone_overlap false
ceph config get osd osd_recover_clone_overlap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recover_clone_overlap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recover_clone_overlap_limit

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_recover_clone_overlap_limit](../../../config/osd/osd.md#SP_osd_recover_clone_overlap_limit) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recover_clone_overlap_limit 10
ceph config get osd osd_recover_clone_overlap_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recover_clone_overlap_limit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_delay_start

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_delay_start](../../../config/osd/osd.md#SP_osd_recovery_delay_start) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_recovery_delay_start 0
ceph config get osd osd_recovery_delay_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_delay_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_active

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_active](../../../config/osd/osd.md#SP_osd_recovery_max_active) |

**کارکرد:** Cap on concurrent recovery/backfill operations per OSD (0 = derive from HDD/SSD/hybrid-specific settings).

**زمان استفاده:** Raise temporarily after OSD replacement to rebuild faster; lower during production peaks to protect client latency.

**مثال:**

```bash
ceph config set osd osd_recovery_max_active 64
ceph config get osd osd_recovery_max_active
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_active
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

Watch `recovering`/`backfilling` PG count and client p99. See also `osd_recovery_max_active_hdd` / `_ssd` when set to 0.

---

### osd_recovery_max_active_hdd

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_active_hdd](../../../config/osd/osd.md#SP_osd_recovery_max_active_hdd) |

**کارکرد:** Number of simultaneous active recovery operations per OSD (for rotational devices)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recovery_max_active_hdd 3
ceph config get osd osd_recovery_max_active_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_active_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_active_ssd

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_active_ssd](../../../config/osd/osd.md#SP_osd_recovery_max_active_ssd) |

**کارکرد:** Number of simultaneous active recovery operations per OSD (for non-rotational solid state devices)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recovery_max_active_ssd 10
ceph config get osd osd_recovery_max_active_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_active_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_chunk

| | |
|---|---|
| نوع | Size · default `8_M` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_chunk) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recovery_max_chunk 8_M
ceph config get osd osd_recovery_max_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `8_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_omap_entries_per_chunk

| | |
|---|---|
| نوع | Uint · default `8096` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_omap_entries_per_chunk](../../../config/osd/osd.md#SP_osd_recovery_max_omap_entries_per_chunk) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recovery_max_omap_entries_per_chunk 8096
ceph config get osd osd_recovery_max_omap_entries_per_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `8096`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_omap_entries_per_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_max_single_start

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_max_single_start](../../../config/osd/osd.md#SP_osd_recovery_max_single_start) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_recovery_max_single_start 1
ceph config get osd osd_recovery_max_single_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_max_single_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_retry_interval

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_retry_interval](../../../config/osd/osd.md#SP_osd_recovery_retry_interval) |

**کارکرد:** how frequently to retry recovery reservations after being denied (e.g., due to a full OSD)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_retry_interval 30
ceph config get osd osd_recovery_retry_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_retry_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep](../../../config/osd/osd.md#SP_osd_recovery_sleep) |

**کارکرد:** Pause between recovery/backfill chunks (seconds). Non-zero values throttle recovery to leave headroom for application I/O.

**زمان استفاده:** Use on busy clusters during business hours; set to 0 for fastest rebuild in maintenance windows.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep 0
ceph config get osd osd_recovery_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_degraded](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op when PGs are degraded. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_degraded 0
ceph config get osd osd_recovery_sleep_degraded
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_degraded
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_hdd

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_degraded_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hdd) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op for HDDs when PGs is degraded.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_degraded_hdd 0.1
ceph config get osd osd_recovery_sleep_degraded_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_degraded_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_hybrid

| | |
|---|---|
| نوع | Float · default `0.025` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_degraded_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_hybrid) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op when PGs are degraded and data is on HDD and journal is on SSD

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_degraded_hybrid 0.025
ceph config get osd osd_recovery_sleep_degraded_hybrid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.025`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_degraded_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_degraded_ssd

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_degraded_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_degraded_ssd) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op for SSDs when PGs are degraded.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_degraded_ssd 0
ceph config get osd osd_recovery_sleep_degraded_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_degraded_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_hdd

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_hdd](../../../config/osd/osd.md#SP_osd_recovery_sleep_hdd) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op for HDDs

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_hdd 0.1
ceph config get osd osd_recovery_sleep_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_hybrid

| | |
|---|---|
| نوع | Float · default `0.025` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_hybrid](../../../config/osd/osd.md#SP_osd_recovery_sleep_hybrid) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op when data is on HDD and journal is on SSD

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_hybrid 0.025
ceph config get osd osd_recovery_sleep_hybrid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.025`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_recovery_sleep_ssd

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_recovery_sleep_ssd](../../../config/osd/osd.md#SP_osd_recovery_sleep_ssd) |

**کارکرد:** Time in seconds to sleep before next recovery or backfill op for SSDs

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_recovery_sleep_ssd 0
ceph config get osd osd_recovery_sleep_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_recovery_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
