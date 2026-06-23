# Intervals

راهنمای عمیق پیکربندی MGR — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_delta_reset_interval](#mon_delta_reset_interval) | `10` | Advanced | عملکرد |
| [mon_stat_smooth_intervals](#mon_stat_smooth_intervals) | `6` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_delta_reset_interval

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_delta_reset_interval](../../../config/mgr/mon.md#SP_mon_delta_reset_interval) |

**کارکرد:** window duration for rate calculations in 'ceph status'

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_delta_reset_interval 10
ceph config get mon mon_delta_reset_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_delta_reset_interval
ceph -s
ceph mon stat
```

---

### mon_stat_smooth_intervals

| | |
|---|---|
| نوع | Uint · default `6` · **Advanced** |
| جدول | [mon.md#SP_mon_stat_smooth_intervals](../../../config/mgr/mon.md#SP_mon_stat_smooth_intervals) |

**کارکرد:** number of PGMaps stats over which we calc the average read/write throughput of the whole cluster

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_stat_smooth_intervals 6
ceph config get mon mon_stat_smooth_intervals
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_stat_smooth_intervals
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
