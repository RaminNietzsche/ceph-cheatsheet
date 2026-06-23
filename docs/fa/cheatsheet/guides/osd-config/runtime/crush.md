# CRUSH & weight

راهنمای عمیق پیکربندی OSD — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_crush_initial_weight](#osd_crush_initial_weight) | `-1` | Advanced | عملکرد |
| [osd_crush_update_on_start](#osd_crush_update_on_start) | `True` | Advanced | عملکرد |

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

### osd_crush_initial_weight

| | |
|---|---|
| نوع | Float · default `-1` · **Advanced** |
| جدول | [osd.md#SP_osd_crush_initial_weight](../../../config/osd/osd.md#SP_osd_crush_initial_weight) |

**کارکرد:** if >= 0, initial CRUSH weight for newly created OSDs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set osd osd_crush_initial_weight -1
ceph config get osd osd_crush_initial_weight
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_crush_initial_weight
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_crush_update_on_start

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [osd.md#SP_osd_crush_update_on_start](../../../config/osd/osd.md#SP_osd_crush_update_on_start) |

**کارکرد:** update OSD CRUSH location on startup

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set osd osd_crush_update_on_start false
ceph config get osd osd_crush_update_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_crush_update_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
