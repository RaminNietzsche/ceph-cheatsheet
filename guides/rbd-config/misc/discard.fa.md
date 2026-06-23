# Discard

deep dive پیکربندی RBD — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_discard_granularity_bytes](#rbd_discard_granularity_bytes) | `64_K` | Advanced | Performance |
| [rbd_discard_on_zeroed_write_same](#rbd_discard_on_zeroed_write_same) | `True` | Advanced | Performance |

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

### rbd_discard_granularity_bytes

| | |
|---|---|
| نوع | Uint · default `64_K` · **Advanced** |
| جدول | [rbd.md#SP_rbd_discard_granularity_bytes](../../../config/rbd/rbd.md#SP_rbd_discard_granularity_bytes) |

**کارکرد:** minimum aligned size of discard operations &#91;&#93;(std::string *value, std::string *error_message) { uint64_t f = strict_si_cast<uint64_t>(*value, error_message); if (!error_message->empty()) { return -EINVAL; } else if (!std::has_single_bit(f)) { *error_message = "value must be a power of two"; return -EINVAL; } return 0; }

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_discard_granularity_bytes 64_K
ceph config get client rbd_discard_granularity_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `4_K`، حداکثر `32_M`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_discard_granularity_bytes
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_discard_on_zeroed_write_same

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rbd.md#SP_rbd_discard_on_zeroed_write_same](../../../config/rbd/rbd.md#SP_rbd_discard_on_zeroed_write_same) |

**کارکرد:** discard data on zeroed write same instead of writing zero

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client rbd_discard_on_zeroed_write_same false
ceph config get client rbd_discard_on_zeroed_write_same
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_discard_on_zeroed_write_same
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
