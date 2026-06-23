# Cache

راهنمای عمیق پیکربندی RBD — 8 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_cache_block_writes_upfront](#rbd_cache_block_writes_upfront) | `False` | Advanced | عملکرد |
| [rbd_cache_max_dirty](#rbd_cache_max_dirty) | `24_M` | Advanced | عملکرد |
| [rbd_cache_max_dirty_age](#rbd_cache_max_dirty_age) | `1` | Advanced | عملکرد |
| [rbd_cache_max_dirty_object](#rbd_cache_max_dirty_object) | `0` | Advanced | عملکرد |
| [rbd_cache_policy](#rbd_cache_policy) | `writearound` | Advanced | عملکرد |
| [rbd_cache_size](#rbd_cache_size) | `32_M` | Advanced | عملکرد |
| [rbd_cache_target_dirty](#rbd_cache_target_dirty) | `16_M` | Advanced | عملکرد |
| [rbd_cache_writethrough_until_flush](#rbd_cache_writethrough_until_flush) | `True` | Advanced | عملکرد |

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

### rbd_cache_block_writes_upfront

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_block_writes_upfront](../../../config/rbd/rbd.md#SP_rbd_cache_block_writes_upfront) |

**کارکرد:** whether to block writes to the cache before the aio_write call completes

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client rbd_cache_block_writes_upfront true
ceph config get client rbd_cache_block_writes_upfront
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_block_writes_upfront
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_max_dirty

| | |
|---|---|
| نوع | Size · default `24_M` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_max_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty) |

**کارکرد:** dirty limit in bytes - set to 0 for write-through caching

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_cache_max_dirty 24_M
ceph config get client rbd_cache_max_dirty
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `24_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_max_dirty
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_max_dirty_age

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_max_dirty_age](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_age) |

**کارکرد:** seconds in cache before writeback starts

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_cache_max_dirty_age 1
ceph config get client rbd_cache_max_dirty_age
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_max_dirty_age
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_max_dirty_object

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_max_dirty_object](../../../config/rbd/rbd.md#SP_rbd_cache_max_dirty_object) |

**کارکرد:** dirty limit for objects - set to 0 for auto calculate from rbd_cache_size

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_cache_max_dirty_object 64
ceph config get client rbd_cache_max_dirty_object
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_max_dirty_object
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_policy

| | |
|---|---|
| نوع | Str · enum: ["writethrough", "writeback", "writearound"] · default `writearound` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_policy](../../../config/rbd/rbd.md#SP_rbd_cache_policy) |

**کارکرد:** cache policy for handling writes.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_cache_policy writearound
ceph config get client rbd_cache_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `writearound`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_policy
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_size

| | |
|---|---|
| نوع | Size · default `32_M` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_size](../../../config/rbd/rbd.md#SP_rbd_cache_size) |

**کارکرد:** cache size in bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_cache_size 32_M
ceph config get client rbd_cache_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_size
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_target_dirty

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_target_dirty](../../../config/rbd/rbd.md#SP_rbd_cache_target_dirty) |

**کارکرد:** target dirty limit in bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_cache_target_dirty 16_M
ceph config get client rbd_cache_target_dirty
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_target_dirty
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_cache_writethrough_until_flush

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [rbd.md#SP_rbd_cache_writethrough_until_flush](../../../config/rbd/rbd.md#SP_rbd_cache_writethrough_until_flush) |

**کارکرد:** whether to make writeback caching writethrough until flush is called, to be sure the user of librbd will send flushes so that writeback is safe

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client rbd_cache_writethrough_until_flush false
ceph config get client rbd_cache_writethrough_until_flush
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_cache_writethrough_until_flush
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
