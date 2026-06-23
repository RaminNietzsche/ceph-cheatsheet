# Filer

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [filer_max_purge_ops](#filer_max_purge_ops) | `10` | Advanced | Performance |
| [filer_max_truncate_ops](#filer_max_truncate_ops) | `128` | Advanced | Performance |

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

### filer_max_purge_ops

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [filer.md#SP_filer_max_purge_ops](../../../config/global/filer.md#SP_filer_max_purge_ops) |

**کارکرد:** Max in-flight operations for purging a striped range (e.g., MDS journal)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filer_max_purge_ops 10
ceph config get global filer_max_purge_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global filer_max_purge_ops
ceph -s
```

---

### filer_max_truncate_ops

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [filer.md#SP_filer_max_truncate_ops](../../../config/global/filer.md#SP_filer_max_truncate_ops) |

**کارکرد:** Max in-flight operations for truncating/deleting a striped sequence (e.g., MDS journal)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global filer_max_truncate_ops 128
ceph config get global filer_max_truncate_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global filer_max_truncate_ops
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
