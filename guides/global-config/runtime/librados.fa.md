# Librados

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [librados_thread_count](#librados_thread_count) | `2` | Advanced | Performance |

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

### librados_thread_count

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [librados.md#SP_librados_thread_count](../../../config/global/librados.md#SP_librados_thread_count) |

**کارکرد:** Size of thread pool for Objecter

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global librados_thread_count 2
ceph config get global librados_thread_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global librados_thread_count
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
