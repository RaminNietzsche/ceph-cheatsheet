# Gss

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [gss_ktab_client_file](#gss_ktab_client_file) | `/var/lib/ceph/$name/gss_client_$name.ktab` | Advanced | Capacity |
| [gss_target_name](#gss_target_name) | `ceph` | Advanced | Performance |

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

### gss_ktab_client_file

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/$name/gss_client_$name.ktab` · **Advanced** |
| جدول | [gss.md#SP_gss_ktab_client_file](../../../config/global/gss.md#SP_gss_ktab_client_file) |

**کارکرد:** GSS/KRB5 Keytab file for client authentication

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global gss_ktab_client_file "/var/lib/ceph/$name/gss_client_$name.ktab"
ceph config get global gss_ktab_client_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/var/lib/ceph/$name/gss_client_$name.ktab`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global gss_ktab_client_file
ceph -s
```

---

### gss_target_name

| | |
|---|---|
| نوع | Str · default `ceph` · **Advanced** |
| جدول | [gss.md#SP_gss_target_name](../../../config/global/gss.md#SP_gss_target_name) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global gss_target_name ceph
ceph config get global gss_target_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `ceph`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global gss_target_name
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
