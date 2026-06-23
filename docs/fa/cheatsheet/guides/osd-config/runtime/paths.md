# Paths & data dirs

راهنمای عمیق پیکربندی OSD — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_data](#osd_data) | `/var/lib/ceph/osd/$cluster-$id` | Advanced | عملکرد |
| [osd_skip_data_digest](#osd_skip_data_digest) | `False` | Dev | توسعه |

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

### osd_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/osd/$cluster-$id` · **Advanced** |
| جدول | [osd.md#SP_osd_data](../../../config/osd/osd.md#SP_osd_data) |

**کارکرد:** path to OSD data

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_data "/var/lib/ceph/osd/$cluster-$id"
ceph config get osd osd_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/osd/$cluster-$id`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_data
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_data_digest

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_skip_data_digest](../../../config/osd/osd.md#SP_osd_skip_data_digest) |

**کارکرد:** Do not store full-object checksums if the backend (bluestore) does its own checksums. Only usable with all BlueStore OSDs.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_skip_data_digest true
ceph config get osd osd_skip_data_digest
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
