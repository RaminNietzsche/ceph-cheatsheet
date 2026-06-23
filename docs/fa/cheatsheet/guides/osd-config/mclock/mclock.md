# mClock scheduler

راهنمای عمیق پیکربندی OSD — 18 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_mclock_force_run_benchmark_on_init](#osd_mclock_force_run_benchmark_on_init) | `False` | Advanced | عملکرد |
| [osd_mclock_iops_capacity_low_threshold_hdd](#osd_mclock_iops_capacity_low_threshold_hdd) | `50` | Basic | عملکرد |
| [osd_mclock_iops_capacity_low_threshold_ssd](#osd_mclock_iops_capacity_low_threshold_ssd) | `1000` | Basic | عملکرد |
| [osd_mclock_iops_capacity_threshold_hdd](#osd_mclock_iops_capacity_threshold_hdd) | `500` | Basic | عملکرد |
| [osd_mclock_iops_capacity_threshold_ssd](#osd_mclock_iops_capacity_threshold_ssd) | `80000` | Basic | عملکرد |
| [osd_mclock_max_capacity_iops_hdd](#osd_mclock_max_capacity_iops_hdd) | `315` | Basic | عملکرد |
| [osd_mclock_max_capacity_iops_ssd](#osd_mclock_max_capacity_iops_ssd) | `21500` | Basic | عملکرد |
| [osd_mclock_max_sequential_bandwidth_hdd](#osd_mclock_max_sequential_bandwidth_hdd) | `150_M` | Basic | عملکرد |
| [osd_mclock_max_sequential_bandwidth_ssd](#osd_mclock_max_sequential_bandwidth_ssd) | `1200_M` | Basic | عملکرد |
| [osd_mclock_profile](#osd_mclock_profile) | `balanced` | Advanced | عملکرد |
| [osd_mclock_scheduler_anticipation_timeout](#osd_mclock_scheduler_anticipation_timeout) | `0` | Advanced | عملکرد |
| [osd_mclock_scheduler_background_best_effort_lim](#osd_mclock_scheduler_background_best_effort_lim) | `0` | Advanced | عملکرد |
| [osd_mclock_scheduler_background_best_effort_res](#osd_mclock_scheduler_background_best_effort_res) | `0` | Advanced | عملکرد |
| [osd_mclock_scheduler_background_best_effort_wgt](#osd_mclock_scheduler_background_best_effort_wgt) | `1` | Advanced | عملکرد |
| [osd_mclock_scheduler_client_lim](#osd_mclock_scheduler_client_lim) | `0` | Advanced | عملکرد |
| [osd_mclock_scheduler_client_res](#osd_mclock_scheduler_client_res) | `0` | Advanced | عملکرد |
| [osd_mclock_scheduler_client_wgt](#osd_mclock_scheduler_client_wgt) | `1` | Advanced | عملکرد |
| [osd_mclock_skip_benchmark](#osd_mclock_skip_benchmark) | `False` | Dev | توسعه |

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

### osd_mclock_force_run_benchmark_on_init

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [osd.md#SP_osd_mclock_force_run_benchmark_on_init](../../../config/osd/osd.md#SP_osd_mclock_force_run_benchmark_on_init) |

**کارکرد:** Force run the OSD benchmark on OSD initialization/boot-up

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_force_run_benchmark_on_init true
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph orch restart osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_force_run_benchmark_on_init
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_hdd

| | |
|---|---|
| نوع | Float · default `50` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_hdd) |

**کارکرد:** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for rotational media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_hdd 50
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_low_threshold_ssd

| | |
|---|---|
| نوع | Float · default `1000` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_low_threshold_ssd) |

**کارکرد:** The threshold IOPs capacity (at 4KiB block size) below which to ignore the OSD bench results for an OSD (for solid state media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_iops_capacity_low_threshold_ssd 1000
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_iops_capacity_low_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_hdd

| | |
|---|---|
| نوع | Float · default `500` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_iops_capacity_threshold_hdd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_hdd) |

**کارکرد:** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for rotational media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_hdd 500
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_iops_capacity_threshold_ssd

| | |
|---|---|
| نوع | Float · default `80000` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_iops_capacity_threshold_ssd](../../../config/osd/osd.md#SP_osd_mclock_iops_capacity_threshold_ssd) |

**کارکرد:** The threshold IOPs capacity (at 4KiB block size) beyond which to ignore the OSD bench results for an OSD (for solid state media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_iops_capacity_threshold_ssd 80000
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `80000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_iops_capacity_threshold_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_hdd

| | |
|---|---|
| نوع | Float · default `315` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_max_capacity_iops_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_hdd) |

**کارکرد:** Max random write IOPS capacity (at 4KiB block size) to consider per OSD (for rotational media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_max_capacity_iops_hdd 315
ceph config get osd osd_mclock_max_capacity_iops_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `315`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_max_capacity_iops_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_capacity_iops_ssd

| | |
|---|---|
| نوع | Float · default `21500` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_max_capacity_iops_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_capacity_iops_ssd) |

**کارکرد:** Max random write IOPS capacity (at 4 KiB block size) to consider per OSD (for solid state media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_max_capacity_iops_ssd 21500
ceph config get osd osd_mclock_max_capacity_iops_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `21500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_max_capacity_iops_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_hdd

| | |
|---|---|
| نوع | Size · default `150_M` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_hdd) |

**کارکرد:** The maximum sequential bandwidth in bytes/second of the OSD (for rotational media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_hdd 150_M
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `150_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_max_sequential_bandwidth_ssd

| | |
|---|---|
| نوع | Size · default `1200_M` · **Basic** |
| جدول | [osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd](../../../config/osd/osd.md#SP_osd_mclock_max_sequential_bandwidth_ssd) |

**کارکرد:** The maximum sequential bandwidth in bytes/second of the OSD (for solid state media)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_mclock_max_sequential_bandwidth_ssd 1200_M
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1200_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_max_sequential_bandwidth_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_profile

| | |
|---|---|
| نوع | Str · enum: ["balanced", "high_recovery_ops", "high_client_ops", "custom"] · default `balanced` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_profile](../../../config/osd/osd.md#SP_osd_mclock_profile) |

**کارکرد:** Selects the mClock scheduler profile (`balanced`, `high_client_ops`, `high_recovery_ops`, or custom).

**زمان استفاده:** Start with `balanced` on mixed workloads. Use `high_client_ops` when recovery dominates latency; `high_recovery_ops` for aggressive rebuild windows.

**مثال:**

```bash
ceph config set osd osd_mclock_profile high_client_ops
ceph config get osd osd_mclock_profile
ceph daemon osd.<id> config show | grep mclock
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `balanced`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_profile
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_anticipation_timeout

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_anticipation_timeout](../../../config/osd/osd.md#SP_osd_mclock_scheduler_anticipation_timeout) |

**کارکرد:** mclock anticipation timeout in seconds

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_anticipation_timeout 0
ceph config get osd osd_mclock_scheduler_anticipation_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_anticipation_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_best_effort_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_lim) |

**کارکرد:** IO limit for background best_effort over reservation. The default value of 0 specifies no limit enforcement, which means background best_effort operation can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that background best_effort operation receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_lim 0
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_best_effort_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_res

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_best_effort_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_res) |

**کارکرد:** IO proportion reserved for background best_effort (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for background best_effort operations in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_res 0
ceph config get osd osd_mclock_scheduler_background_best_effort_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_best_effort_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_background_best_effort_wgt

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_background_best_effort_wgt) |

**کارکرد:** IO share for each background best_effort over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_background_best_effort_wgt 1
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_background_best_effort_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_lim

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_client_lim](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_lim) |

**کارکرد:** IO limit for each client (default) over reservation. The default value of 0 specifies no limit enforcement, which means each client can use the maximum possible IOPS capacity of the OSD. Any value greater than 0 and up to 1.0 specifies the upper IO limit over reservation that each client receives in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_client_lim 0
ceph config get osd osd_mclock_scheduler_client_lim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_client_lim
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_res

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_client_res](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_res) |

**کارکرد:** IO proportion reserved for each client (default). The default value of 0 specifies the lowest possible reservation. Any value greater than 0 and up to 1.0 specifies the minimum IO proportion to reserve for each client in terms of a fraction of the OSD's maximum IOPS capacity. Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_client_res 0
ceph config get osd osd_mclock_scheduler_client_res
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1.0`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_client_res
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_scheduler_client_wgt

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_mclock_scheduler_client_wgt](../../../config/osd/osd.md#SP_osd_mclock_scheduler_client_wgt) |

**کارکرد:** IO share for each client (default) over reservation Ignored unless osd_mclock_profile is set to 'custom'.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_mclock_scheduler_client_wgt 1
ceph config get osd osd_mclock_scheduler_client_wgt
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_mclock_scheduler_client_wgt
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_mclock_skip_benchmark

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_mclock_skip_benchmark](../../../config/osd/osd.md#SP_osd_mclock_skip_benchmark) |

**کارکرد:** Skip the OSD benchmark on OSD initialization/boot-up

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_mclock_skip_benchmark true
ceph config get osd osd_mclock_skip_benchmark
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
