# Uadk

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [uadk_compressor_enabled](#uadk_compressor_enabled) | `False` | Advanced | Policy |
| [uadk_wd_sync_ctx_num](#uadk_wd_sync_ctx_num) | `2` | Advanced | Performance |

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

### uadk_compressor_enabled

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [uadk.md#SP_uadk_compressor_enabled](../../../config/global/uadk.md#SP_uadk_compressor_enabled) |

**کارکرد:** Enable UADK acceleration support for compression if available

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global uadk_compressor_enabled true
ceph config get global uadk_compressor_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global uadk_compressor_enabled
ceph -s
```

---

### uadk_wd_sync_ctx_num

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [uadk.md#SP_uadk_wd_sync_ctx_num](../../../config/global/uadk.md#SP_uadk_wd_sync_ctx_num) |

**کارکرد:** Set the number of instances in the queue

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global uadk_wd_sync_ctx_num 2
ceph config get global uadk_wd_sync_ctx_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `2`، حداکثر `1024`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global uadk_wd_sync_ctx_num
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
