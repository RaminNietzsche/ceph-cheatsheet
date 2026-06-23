# MDS-related settings

راهنمای عمیق پیکربندی MON — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_beacon_mon_down_grace](#mds_beacon_mon_down_grace) | `1_min` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_beacon_mon_down_grace

| | |
|---|---|
| نوع | Secs · default `1_min` · **Advanced** |
| جدول | [mds.md#SP_mds_beacon_mon_down_grace](../../../config/mon/mds.md#SP_mds_beacon_mon_down_grace) |

**کارکرد:** tolerance in seconds for missed MDS beacons to monitors

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_beacon_mon_down_grace 1_min
ceph config get mds mds_beacon_mon_down_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_beacon_mon_down_grace
ceph -s
ceph fs status
ceph mds stat
```

---


[← نمای کلی](../OVERVIEW.md)
