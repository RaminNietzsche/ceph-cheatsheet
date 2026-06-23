# Intervals & throttling

deep dive پیکربندی OSD — 12 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_delete_sleep](#osd_delete_sleep) | `0` | Advanced | Performance |
| [osd_delete_sleep_hdd](#osd_delete_sleep_hdd) | `5` | Advanced | Performance |
| [osd_delete_sleep_hybrid](#osd_delete_sleep_hybrid) | `1` | Advanced | Performance |
| [osd_delete_sleep_ssd](#osd_delete_sleep_ssd) | `1` | Advanced | Performance |
| [osd_max_markdown_period](#osd_max_markdown_period) | `10_min` | Advanced | Performance |
| [osd_op_thread_suicide_timeout](#osd_op_thread_suicide_timeout) | `150` | Advanced | Performance |
| [osd_op_thread_timeout](#osd_op_thread_timeout) | `15` | Advanced | Performance |
| [osd_smart_report_timeout](#osd_smart_report_timeout) | `5` | Advanced | Performance |
| [osd_snap_trim_sleep](#osd_snap_trim_sleep) | `0` | Advanced | Performance |
| [osd_snap_trim_sleep_hdd](#osd_snap_trim_sleep_hdd) | `5` | Advanced | Performance |
| [osd_snap_trim_sleep_hybrid](#osd_snap_trim_sleep_hybrid) | `2` | Advanced | Performance |
| [osd_snap_trim_sleep_ssd](#osd_snap_trim_sleep_ssd) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_delete_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_delete_sleep](../../../config/osd/osd.md#SP_osd_delete_sleep) |

**کارکرد:** Time in seconds to sleep before next removal transaction. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_delete_sleep 0
ceph config get osd osd_delete_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_delete_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_hdd

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_delete_sleep_hdd](../../../config/osd/osd.md#SP_osd_delete_sleep_hdd) |

**کارکرد:** Time in seconds to sleep before next removal transaction for HDDs.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_delete_sleep_hdd 5
ceph config get osd osd_delete_sleep_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_delete_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_hybrid

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_delete_sleep_hybrid](../../../config/osd/osd.md#SP_osd_delete_sleep_hybrid) |

**کارکرد:** Time in seconds to sleep before next removal transaction when OSD data is on HDD and OSD journal or WAL+DB is on SSD

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_delete_sleep_hybrid 1
ceph config get osd osd_delete_sleep_hybrid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_delete_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_ssd

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [osd.md#SP_osd_delete_sleep_ssd](../../../config/osd/osd.md#SP_osd_delete_sleep_ssd) |

**کارکرد:** Time in seconds to sleep before next removal transaction for SSDs

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_delete_sleep_ssd 1
ceph config get osd osd_delete_sleep_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_delete_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_markdown_period

| | |
|---|---|
| نوع | Int · default `10_min` · **Advanced** |
| جدول | [osd.md#SP_osd_max_markdown_period](../../../config/osd/osd.md#SP_osd_max_markdown_period) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set osd osd_max_markdown_period 10_min
ceph config get osd osd_max_markdown_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_max_markdown_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_thread_suicide_timeout

| | |
|---|---|
| نوع | Int · default `150` · **Advanced** |
| جدول | [osd.md#SP_osd_op_thread_suicide_timeout](../../../config/osd/osd.md#SP_osd_op_thread_suicide_timeout) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_op_thread_suicide_timeout 150
ceph config get osd osd_op_thread_suicide_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `150`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_op_thread_suicide_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_thread_timeout

| | |
|---|---|
| نوع | Int · default `15` · **Advanced** |
| جدول | [osd.md#SP_osd_op_thread_timeout](../../../config/osd/osd.md#SP_osd_op_thread_timeout) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_op_thread_timeout 15
ceph config get osd osd_op_thread_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_op_thread_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_smart_report_timeout

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_smart_report_timeout](../../../config/osd/osd.md#SP_osd_smart_report_timeout) |

**کارکرد:** Timeout (in seconds) for smartctl to run, default is set to 5

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_smart_report_timeout 5
ceph config get osd osd_smart_report_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_smart_report_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_sleep](../../../config/osd/osd.md#SP_osd_snap_trim_sleep) |

**کارکرد:** Time in seconds to sleep before next snap trim. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_snap_trim_sleep 0
ceph config get osd osd_snap_trim_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_snap_trim_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_hdd

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_sleep_hdd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hdd) |

**کارکرد:** Time in seconds to sleep before next snap trim for HDDs

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_snap_trim_sleep_hdd 5
ceph config get osd osd_snap_trim_sleep_hdd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_snap_trim_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_hybrid

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_sleep_hybrid](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hybrid) |

**کارکرد:** Time in seconds to sleep before next snap trim when data is on HDD and journal is on SSD

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_snap_trim_sleep_hybrid 2
ceph config get osd osd_snap_trim_sleep_hybrid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_snap_trim_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_ssd

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_snap_trim_sleep_ssd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_ssd) |

**کارکرد:** Time in seconds to sleep before next snap trim for SSDs

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set osd osd_snap_trim_sleep_ssd 0
ceph config get osd osd_snap_trim_sleep_ssd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_snap_trim_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
