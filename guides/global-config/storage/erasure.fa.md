# Erasure

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [erasure_code_dir](#erasure_code_dir) | `0/erasure-code` | Advanced | Capacity |

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

### erasure_code_dir

| | |
|---|---|
| نوع | Str · default `0/erasure-code` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [erasure.md#SP_erasure_code_dir](../../../config/global/erasure.md#SP_erasure_code_dir) |

**کارکرد:** Directory where erasure-code plugins can be found

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global erasure_code_dir "0/erasure-code"
ceph config get global erasure_code_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `0/erasure-code`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global erasure_code_dir
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
