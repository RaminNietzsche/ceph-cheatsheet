# Tmp

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [tmp_dir](#tmp_dir) | `/tmp` | Advanced | Capacity |
| [tmp_file_template](#tmp_file_template) | `$tmp_dir/$cluster-$name.XXXXXX` | Advanced | Performance |

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

### tmp_dir

| | |
|---|---|
| نوع | Str · default `/tmp` · **Advanced** |
| جدول | [tmp.md#SP_tmp_dir](../../../config/global/tmp.md#SP_tmp_dir) |

**کارکرد:** Path for the 'tmp' directory

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global tmp_dir "/tmp"
ceph config get global tmp_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/tmp`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global tmp_dir
ceph -s
```

---

### tmp_file_template

| | |
|---|---|
| نوع | Str · default `$tmp_dir/$cluster-$name.XXXXXX` · **Advanced** |
| جدول | [tmp.md#SP_tmp_file_template](../../../config/global/tmp.md#SP_tmp_file_template) |

**کارکرد:** Template for temporary files created by daemons for ceph tell commands

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global tmp_file_template "$tmp_dir/$cluster-$name.XXXXXX"
ceph config get global tmp_file_template
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `$tmp_dir/$cluster-$name.XXXXXX`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global tmp_file_template
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
