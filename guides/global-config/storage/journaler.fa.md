# Journaler

deep dive پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [journaler_prefetch_periods](#journaler_prefetch_periods) | `10` | Advanced | Performance |
| [journaler_prezero_periods](#journaler_prezero_periods) | `5` | Advanced | Performance |
| [journaler_write_head_interval](#journaler_write_head_interval) | `15` | Advanced | Performance |

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

### journaler_prefetch_periods

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [journaler.md#SP_journaler_prefetch_periods](../../../config/global/journaler.md#SP_journaler_prefetch_periods) |

**کارکرد:** Number of striping periods to prefetch while reading MDS journal

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global journaler_prefetch_periods 10
ceph config get global journaler_prefetch_periods
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `2`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global journaler_prefetch_periods
ceph -s
```

---

### journaler_prezero_periods

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [journaler.md#SP_journaler_prezero_periods](../../../config/global/journaler.md#SP_journaler_prezero_periods) |

**کارکرد:** Number of striping periods to zero head of MDS journal write position

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global journaler_prezero_periods 5
ceph config get global journaler_prezero_periods
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `2`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global journaler_prezero_periods
ceph -s
```

---

### journaler_write_head_interval

| | |
|---|---|
| نوع | Int · default `15` · **Advanced** |
| جدول | [journaler.md#SP_journaler_write_head_interval](../../../config/global/journaler.md#SP_journaler_write_head_interval) |

**کارکرد:** Interval in seconds between journal header updates (to help bound replay time)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global journaler_write_head_interval 15
ceph config get global journaler_write_head_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global journaler_write_head_interval
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
