# Ec

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [ec_extent_cache_size](#ec_extent_cache_size) | `10485760` | Advanced | Performance |
| [ec_pdw_write_mode](#ec_pdw_write_mode) | `0` | Dev | Dev |

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

### ec_extent_cache_size

| | |
|---|---|
| نوع | Uint · default `10485760` · **Advanced** |
| جدول | [ec.md#SP_ec_extent_cache_size](../../../config/global/ec.md#SP_ec_extent_cache_size) |

**کارکرد:** Size of the per-shard extent cache

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global ec_extent_cache_size 10485760
ceph config get global ec_extent_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10485760`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global ec_extent_cache_size
ceph -s
```

---

### ec_pdw_write_mode

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [ec.md#SP_ec_pdw_write_mode](../../../config/global/ec.md#SP_ec_pdw_write_mode) |

**کارکرد:** When EC writes should generate PDWs (development only) 0=optimal 1=never 2=when possible

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global ec_pdw_write_mode 64
ceph config get global ec_pdw_write_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
