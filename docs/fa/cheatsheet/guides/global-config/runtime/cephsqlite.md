# Cephsqlite

راهنمای عمیق پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cephsqlite_blocklist_dead_locker](#cephsqlite_blocklist_dead_locker) | `True` | Advanced | عملکرد |
| [cephsqlite_lock_renewal_interval](#cephsqlite_lock_renewal_interval) | `2000` | Advanced | عملکرد |
| [cephsqlite_lock_renewal_timeout](#cephsqlite_lock_renewal_timeout) | `30000` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephsqlite_blocklist_dead_locker

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [cephsqlite.md#SP_cephsqlite_blocklist_dead_locker](../../../config/global/cephsqlite.md#SP_cephsqlite_blocklist_dead_locker) |

**کارکرد:** Blocklist the last dead owner of the database lock

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global cephsqlite_blocklist_dead_locker false
ceph config get global cephsqlite_blocklist_dead_locker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephsqlite_blocklist_dead_locker
ceph -s
```

---

### cephsqlite_lock_renewal_interval

| | |
|---|---|
| نوع | Millisecs · default `2000` · **Advanced** |
| جدول | [cephsqlite.md#SP_cephsqlite_lock_renewal_interval](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_interval) |

**کارکرد:** Number of milliseconds before a cephsqlite lock is renewed

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global cephsqlite_lock_renewal_interval 2000
ceph config get global cephsqlite_lock_renewal_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `100`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephsqlite_lock_renewal_interval
ceph -s
```

---

### cephsqlite_lock_renewal_timeout

| | |
|---|---|
| نوع | Millisecs · default `30000` · **Advanced** |
| جدول | [cephsqlite.md#SP_cephsqlite_lock_renewal_timeout](../../../config/global/cephsqlite.md#SP_cephsqlite_lock_renewal_timeout) |

**کارکرد:** Number of milliseconds before a libcephsqlite transaction lock times out

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global cephsqlite_lock_renewal_timeout 30000
ceph config get global cephsqlite_lock_renewal_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `100`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephsqlite_lock_renewal_timeout
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
