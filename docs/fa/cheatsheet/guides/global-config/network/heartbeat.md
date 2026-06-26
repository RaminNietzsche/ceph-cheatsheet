# Heartbeat

راهنمای عمیق پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [heartbeat_file](#heartbeat_file) | `(empty)` | Advanced | ظرفیت |
| [heartbeat_inject_failure](#heartbeat_inject_failure) | `0` | Dev | توسعه |
| [heartbeat_interval](#heartbeat_interval) | `5` | Advanced | عملکرد |

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

### heartbeat_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [heartbeat.md#SP_heartbeat_file](../../../config/global/heartbeat.md#SP_heartbeat_file) |

**کارکرد:** File to touch on successful internal heartbeat If set, this file will be touched every time an internal heartbeat check succeeds.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`heartbeat_interval`](../../../config/global/heartbeat.md#SP_heartbeat_interval)

**مثال:**

```bash
ceph config set global heartbeat_file "example"
ceph config get global heartbeat_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `(empty)`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global heartbeat_file
ceph -s
```

---

### heartbeat_inject_failure

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [heartbeat.md#SP_heartbeat_inject_failure](../../../config/global/heartbeat.md#SP_heartbeat_inject_failure) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global heartbeat_inject_failure 64
ceph config get global heartbeat_inject_failure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### heartbeat_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [heartbeat.md#SP_heartbeat_interval](../../../config/global/heartbeat.md#SP_heartbeat_interval) |

**کارکرد:** Frequency of internal heartbeat checks (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global heartbeat_interval 5
ceph config get global heartbeat_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global heartbeat_interval
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
