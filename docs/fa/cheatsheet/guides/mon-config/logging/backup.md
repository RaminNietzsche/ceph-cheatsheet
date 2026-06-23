# Monitor backup

راهنمای عمیق پیکربندی MON — 7 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_backup_cleanup_interval](#mon_backup_cleanup_interval) | `0` | Advanced | عملکرد |
| [mon_backup_interval](#mon_backup_interval) | `0` | Advanced | عملکرد |
| [mon_backup_keep_daily](#mon_backup_keep_daily) | `7` | Advanced | عملکرد |
| [mon_backup_keep_hourly](#mon_backup_keep_hourly) | `5` | Advanced | عملکرد |
| [mon_backup_keep_last](#mon_backup_keep_last) | `6` | Advanced | عملکرد |
| [mon_backup_min_avail](#mon_backup_min_avail) | `10` | Advanced | عملکرد |
| [mon_backup_path](#mon_backup_path) | `/var/backups/ceph/mon/$cluster-$id` | Advanced | ظرفیت |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_backup_cleanup_interval

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_cleanup_interval](../../../config/mon/mon.md#SP_mon_backup_cleanup_interval) |

**کارکرد:** Trigger backup cleanup every N seconds (0 disables)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_backup_cleanup_interval 0
ceph config get mon mon_backup_cleanup_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_cleanup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_interval

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_interval](../../../config/mon/mon.md#SP_mon_backup_interval) |

**کارکرد:** Automatic backups every N seconds (0 disables)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_backup_interval 0
ceph config get mon mon_backup_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_interval
ceph -s
ceph mon stat
```

---

### mon_backup_keep_daily

| | |
|---|---|
| نوع | Uint · default `7` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_keep_daily](../../../config/mon/mon.md#SP_mon_backup_keep_daily) |

**کارکرد:** Number of daily backups

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_backup_keep_daily 7
ceph config get mon mon_backup_keep_daily
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `7`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_keep_daily
ceph -s
ceph mon stat
```

---

### mon_backup_keep_hourly

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_keep_hourly](../../../config/mon/mon.md#SP_mon_backup_keep_hourly) |

**کارکرد:** Number of hourly backups

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_backup_keep_hourly 5
ceph config get mon mon_backup_keep_hourly
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_keep_hourly
ceph -s
ceph mon stat
```

---

### mon_backup_keep_last

| | |
|---|---|
| نوع | Uint · default `6` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_keep_last](../../../config/mon/mon.md#SP_mon_backup_keep_last) |

**کارکرد:** Keep the last N backups

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_backup_keep_last 6
ceph config get mon mon_backup_keep_last
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_keep_last
ceph -s
ceph mon stat
```

---

### mon_backup_min_avail

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_min_avail](../../../config/mon/mon.md#SP_mon_backup_min_avail) |

**کارکرد:** Only capture backups if at least this percentage of the target filesystem is free

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_backup_min_avail 10
ceph config get mon mon_backup_min_avail
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `100`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_min_avail
ceph -s
ceph mon stat
```

---

### mon_backup_path

| | |
|---|---|
| نوع | Str · default `/var/backups/ceph/mon/$cluster-$id` · **Advanced** |
| جدول | [mon.md#SP_mon_backup_path](../../../config/mon/mon.md#SP_mon_backup_path) |

**کارکرد:** Path to Monitor database backups

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_backup_path "/var/backups/ceph/mon/$cluster-$id"
ceph config get mon mon_backup_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `/var/backups/ceph/mon/$cluster-$id`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_backup_path
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
