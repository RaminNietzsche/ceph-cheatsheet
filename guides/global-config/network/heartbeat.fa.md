# Heartbeat

deep dive پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [heartbeat_file](#heartbeat_file) | `(empty)` | Advanced | Capacity |
| [heartbeat_inject_failure](#heartbeat_inject_failure) | `0` | Dev | Dev |
| [heartbeat_interval](#heartbeat_interval) | `5` | Advanced | Performance |

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

### heartbeat_file

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [heartbeat.md#SP_heartbeat_file](../../../config/global/heartbeat.md#SP_heartbeat_file) |

**کارکرد:** File to touch on successful internal heartbeat

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global heartbeat_file "example"
ceph config get global heartbeat_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `(empty)`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global heartbeat_file
ceph -s
```

---

### heartbeat_inject_failure

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [heartbeat.md#SP_heartbeat_inject_failure](../../../config/global/heartbeat.md#SP_heartbeat_inject_failure) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set global heartbeat_inject_failure 64
ceph config get global heartbeat_inject_failure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### heartbeat_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [heartbeat.md#SP_heartbeat_interval](../../../config/global/heartbeat.md#SP_heartbeat_interval) |

**کارکرد:** Frequency of internal heartbeat checks (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global heartbeat_interval 5
ceph config get global heartbeat_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global heartbeat_interval
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
