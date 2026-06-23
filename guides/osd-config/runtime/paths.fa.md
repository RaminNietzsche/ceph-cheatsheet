# Paths & data dirs

deep dive پیکربندی OSD — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_data](#osd_data) | `/var/lib/ceph/osd/$cluster-$id` | Advanced | Performance |
| [osd_skip_data_digest](#osd_skip_data_digest) | `False` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/osd/$cluster-$id` · **Advanced** |
| جدول | [osd.md#SP_osd_data](../../../config/osd/osd.md#SP_osd_data) |

**کارکرد:** path to OSD data

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd osd_data "/var/lib/ceph/osd/$cluster-$id"
ceph config get osd osd_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/osd/$cluster-$id`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_data
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_skip_data_digest

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_skip_data_digest](../../../config/osd/osd.md#SP_osd_skip_data_digest) |

**کارکرد:** Do not store full-object checksums if the backend (bluestore) does its own checksums. Only usable with all BlueStore OSDs.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set osd osd_skip_data_digest true
ceph config get osd osd_skip_data_digest
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
