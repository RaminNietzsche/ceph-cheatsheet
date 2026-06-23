# Paths & storage

راهنمای عمیق پیکربندی MON — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_data](#mon_data) | `/var/lib/ceph/mon/$cluster-$id` | Advanced | Performance |
| [mon_data_avail_crit](#mon_data_avail_crit) | `5` | Advanced | Performance |
| [mon_data_avail_warn](#mon_data_avail_warn) | `30` | Advanced | Performance |
| [mon_data_size_warn](#mon_data_size_warn) | `15_G` | Advanced | Performance |

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

### mon_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/mon/$cluster-$id` · **Advanced** |
| جدول | [mon.md#SP_mon_data](../../../config/mon/mon.md#SP_mon_data) |

**کارکرد:** path to mon database

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_data "/var/lib/ceph/mon/$cluster-$id"
ceph config get mon mon_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/mon/$cluster-$id`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_data
ceph -s
ceph mon stat
```

---

### mon_data_avail_crit

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_data_avail_crit](../../../config/mon/mon.md#SP_mon_data_avail_crit) |

**کارکرد:** issue MON_DISK_CRIT health error when mon available space below this percentage

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_data_avail_crit 5
ceph config get mon mon_data_avail_crit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_data_avail_crit
ceph -s
ceph mon stat
```

---

### mon_data_avail_warn

| | |
|---|---|
| نوع | Int · default `30` · **Advanced** |
| جدول | [mon.md#SP_mon_data_avail_warn](../../../config/mon/mon.md#SP_mon_data_avail_warn) |

**کارکرد:** issue MON_DISK_LOW health warning when mon available space below this percentage

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_data_avail_warn 30
ceph config get mon mon_data_avail_warn
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_data_avail_warn
ceph -s
ceph mon stat
```

---

### mon_data_size_warn

| | |
|---|---|
| نوع | Size · default `15_G` · **Advanced** |
| جدول | [mon.md#SP_mon_data_size_warn](../../../config/mon/mon.md#SP_mon_data_size_warn) |

**کارکرد:** issue MON_DISK_BIG health warning when mon database is above this size

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_data_size_warn 15_G
ceph config get mon mon_data_size_warn
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `15_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_data_size_warn
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
