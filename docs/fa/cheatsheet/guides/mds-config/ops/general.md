# General

راهنمای عمیق پیکربندی MDS — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [defer_client_eviction_on_laggy_osds](#defer_client_eviction_on_laggy_osds) | `False` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### defer_client_eviction_on_laggy_osds

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mds.md#SP_defer_client_eviction_on_laggy_osds](../../../config/mds/mds.md#SP_defer_client_eviction_on_laggy_osds) |

**کارکرد:** Do not evict client if any osd is laggy

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds defer_client_eviction_on_laggy_osds true
ceph config get mds defer_client_eviction_on_laggy_osds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds defer_client_eviction_on_laggy_osds
ceph -s
ceph fs status
ceph mds stat
```

---


[← نمای کلی](../OVERVIEW.md)
