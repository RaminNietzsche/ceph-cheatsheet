# Io

deep dive پیکربندی RBD — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_io_scheduler](#rbd_io_scheduler) | `simple` | Advanced | Performance |
| [rbd_io_scheduler_simple_max_delay](#rbd_io_scheduler_simple_max_delay) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_io_scheduler

| | |
|---|---|
| نوع | Str · enum: ["none", "simple"] · default `simple` · **Advanced** |
| جدول | [rbd.md#SP_rbd_io_scheduler](../../../config/rbd/rbd.md#SP_rbd_io_scheduler) |

**کارکرد:** RBD IO scheduler

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_io_scheduler simple
ceph config get client rbd_io_scheduler
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `simple`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_io_scheduler
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_io_scheduler_simple_max_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_io_scheduler_simple_max_delay](../../../config/rbd/rbd.md#SP_rbd_io_scheduler_simple_max_delay) |

**کارکرد:** maximum io delay (in milliseconds) for simple io scheduler (if set to 0 dalay is calculated based on latency stats)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_io_scheduler_simple_max_delay 64
ceph config get client rbd_io_scheduler_simple_max_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_io_scheduler_simple_max_delay
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
