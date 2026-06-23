# Journal

راهنمای عمیق پیکربندی RBD — 11 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_journal_commit_age](#rbd_journal_commit_age) | `5` | Advanced | عملکرد |
| [rbd_journal_max_concurrent_object_sets](#rbd_journal_max_concurrent_object_sets) | `0` | Advanced | عملکرد |
| [rbd_journal_max_payload_bytes](#rbd_journal_max_payload_bytes) | `16_K` | Advanced | عملکرد |
| [rbd_journal_object_flush_age](#rbd_journal_object_flush_age) | `0` | Advanced | عملکرد |
| [rbd_journal_object_flush_bytes](#rbd_journal_object_flush_bytes) | `1_M` | Advanced | عملکرد |
| [rbd_journal_object_flush_interval](#rbd_journal_object_flush_interval) | `0` | Advanced | عملکرد |
| [rbd_journal_object_max_in_flight_appends](#rbd_journal_object_max_in_flight_appends) | `0` | Advanced | عملکرد |
| [rbd_journal_object_writethrough_until_flush](#rbd_journal_object_writethrough_until_flush) | `True` | Advanced | عملکرد |
| [rbd_journal_order](#rbd_journal_order) | `24` | Advanced | عملکرد |
| [rbd_journal_pool](#rbd_journal_pool) | `(empty)` | Advanced | عملکرد |
| [rbd_journal_splay_width](#rbd_journal_splay_width) | `4` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_journal_commit_age

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_commit_age](../../../config/rbd/rbd.md#SP_rbd_journal_commit_age) |

**کارکرد:** commit time interval, seconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_commit_age 5
ceph config get client rbd_journal_commit_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_commit_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_max_concurrent_object_sets

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_max_concurrent_object_sets](../../../config/rbd/rbd.md#SP_rbd_journal_max_concurrent_object_sets) |

**کارکرد:** maximum number of object sets a journal client can be behind before it is automatically unregistered

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_journal_max_concurrent_object_sets 64
ceph config get client rbd_journal_max_concurrent_object_sets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_max_concurrent_object_sets
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_max_payload_bytes

| | |
|---|---|
| نوع | Size · default `16_K` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_max_payload_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_max_payload_bytes) |

**کارکرد:** maximum journal payload size before splitting

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_journal_max_payload_bytes 16_K
ceph config get client rbd_journal_max_payload_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_max_payload_bytes
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_object_flush_age

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_object_flush_age](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_age) |

**کارکرد:** maximum age (in seconds) for pending commits

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_object_flush_age 0
ceph config get client rbd_journal_object_flush_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_object_flush_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_object_flush_bytes

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_object_flush_bytes](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_bytes) |

**کارکرد:** maximum number of pending bytes per journal object

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_object_flush_bytes 1_M
ceph config get client rbd_journal_object_flush_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_object_flush_bytes
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_object_flush_interval

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_object_flush_interval](../../../config/rbd/rbd.md#SP_rbd_journal_object_flush_interval) |

**کارکرد:** maximum number of pending commits per journal object

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set client rbd_journal_object_flush_interval 64
ceph config get client rbd_journal_object_flush_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_object_flush_interval
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_object_max_in_flight_appends

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_object_max_in_flight_appends](../../../config/rbd/rbd.md#SP_rbd_journal_object_max_in_flight_appends) |

**کارکرد:** maximum number of in-flight appends per journal object

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_journal_object_max_in_flight_appends 64
ceph config get client rbd_journal_object_max_in_flight_appends
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_object_max_in_flight_appends
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_object_writethrough_until_flush

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_object_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_journal_object_writethrough_until_flush) |

**کارکرد:** when enabled, the rbd_journal_object_flush* configuration options are ignored until the first flush so that batched journal IO is known to be safe for consistency

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client rbd_journal_object_writethrough_until_flush false
ceph config get client rbd_journal_object_writethrough_until_flush
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_object_writethrough_until_flush
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_order

| | |
|---|---|
| نوع | Uint · default `24` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_order](../../../config/rbd/rbd.md#SP_rbd_journal_order) |

**کارکرد:** default order (object size) for journal data objects

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_order 24
ceph config get client rbd_journal_order
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `24`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `12`، حداکثر `26`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_order
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_pool

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_pool](../../../config/rbd/rbd.md#SP_rbd_journal_pool) |

**کارکرد:** pool for journal objects

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_pool "example"
ceph config get client rbd_journal_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_pool
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_journal_splay_width

| | |
|---|---|
| نوع | Uint · default `4` · **Advanced** |
| جدول | [rbd.md#SP_rbd_journal_splay_width](../../../config/rbd/rbd.md#SP_rbd_journal_splay_width) |

**کارکرد:** number of active journal objects

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_journal_splay_width 4
ceph config get client rbd_journal_splay_width
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_journal_splay_width
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
