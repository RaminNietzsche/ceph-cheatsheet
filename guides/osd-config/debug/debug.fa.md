# Debug & injection

راهنمای عمیق پیکربندی OSD — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [osd_debug_feed_pullee](#osd_debug_feed_pullee) | `-1` | Dev | توسعه |
| [osd_debug_trim_objects](#osd_debug_trim_objects) | `False` | Advanced | عملکرد |
| [osd_inject_bad_map_crc_probability](#osd_inject_bad_map_crc_probability) | `0` | Dev | توسعه |
| [osd_inject_failure_on_pg_removal](#osd_inject_failure_on_pg_removal) | `False` | Dev | توسعه |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_debug_feed_pullee

| | |
|---|---|
| نوع | Int · default `-1` · **Dev** |
| جدول | [osd.md#SP_osd_debug_feed_pullee](../../../config/osd/osd.md#SP_osd_debug_feed_pullee) |

**کارکرد:** Feed a pullee, and force primary to pull a currently missing object from it

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_feed_pullee 128
ceph config get osd osd_debug_feed_pullee
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`-1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_debug_trim_objects

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_debug_trim_objects](../../../config/osd/osd.md#SP_osd_debug_trim_objects) |

**کارکرد:** Asserts that no clone-objects were added to a snap after we start trimming it

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_debug_trim_objects true
ceph config get osd osd_debug_trim_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get osd osd_debug_trim_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_inject_bad_map_crc_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [osd.md#SP_osd_inject_bad_map_crc_probability](../../../config/osd/osd.md#SP_osd_inject_bad_map_crc_probability) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_inject_bad_map_crc_probability 0
ceph config get osd osd_inject_bad_map_crc_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### osd_inject_failure_on_pg_removal

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [osd.md#SP_osd_inject_failure_on_pg_removal](../../../config/osd/osd.md#SP_osd_inject_failure_on_pg_removal) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set osd osd_inject_failure_on_pg_removal true
ceph config get osd osd_inject_failure_on_pg_removal
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
