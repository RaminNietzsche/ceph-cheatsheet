# Defaults

راهنمای عمیق پیکربندی RBD — 10 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_default_clone_format](#rbd_default_clone_format) | `auto` | Advanced | عملکرد |
| [rbd_default_data_pool](#rbd_default_data_pool) | `(empty)` | Advanced | عملکرد |
| [rbd_default_features](#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Advanced | عملکرد |
| [rbd_default_format](#rbd_default_format) | `2` | Advanced | عملکرد |
| [rbd_default_map_options](#rbd_default_map_options) | `(empty)` | Advanced | عملکرد |
| [rbd_default_order](#rbd_default_order) | `22` | Advanced | عملکرد |
| [rbd_default_pool](#rbd_default_pool) | `rbd` | Advanced | عملکرد |
| [rbd_default_snapshot_quiesce_mode](#rbd_default_snapshot_quiesce_mode) | `required` | Advanced | عملکرد |
| [rbd_default_stripe_count](#rbd_default_stripe_count) | `0` | Advanced | عملکرد |
| [rbd_default_stripe_unit](#rbd_default_stripe_unit) | `0` | Advanced | عملکرد |

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

### rbd_default_clone_format

| | |
|---|---|
| نوع | Str · enum: ["1", "2", "auto"] · default `auto` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_clone_format](../../../config/rbd/rbd.md#SP_rbd_default_clone_format) |

**کارکرد:** default internal format for handling clones This sets the internal format for tracking cloned images. The value of ``1`` requires attaching to protected snapshots that cannot be removed until the clone is removed or flattened. The value of ``2`` will allow clones to be attached to any snapshot and permits removing in-use parent snapshots but requires Mimic or later clients. The default value of ``auto`` will use the v2 format if the cluster is configured to require Mimic or later clients.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_clone_format auto
ceph config get client rbd_default_clone_format
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `auto`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_clone_format
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_data_pool

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_data_pool](../../../config/rbd/rbd.md#SP_rbd_default_data_pool) |

**کارکرد:** default pool for storing data blocks for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_data_pool "example"
ceph config get client rbd_default_data_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_data_pool
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_features

| | |
|---|---|
| نوع | Str · default `layering,exclusive-lock,object-map,fast-diff,deep-flatten` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_features](../../../config/rbd/rbd.md#SP_rbd_default_features) |

**کارکرد:** default v2 image features for new images RBD features are only applicable for v2 images. This setting accepts either an integer bitmask value or comma-delimited string of RBD feature names. This setting is always internally stored as an integer bitmask value. The mapping between feature bitmask value and feature name is as follows: +1 -> layering, +2 -> striping, +4 -> exclusive-lock, +8 -> object-map, +16 -> fast-diff, +32 -> deep-flatten, +64 -> journaling, +128 -> data-pool

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_features "layering,exclusive-lock,object-map,fast-diff,deep-flatten"
ceph config get client rbd_default_features
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `layering,exclusive-lock,object-map,fast-diff,deep-flatten`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_features
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_format

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_format](../../../config/rbd/rbd.md#SP_rbd_default_format) |

**کارکرد:** default image format for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_format 2
ceph config get client rbd_default_format
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_format
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_map_options

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_map_options](../../../config/rbd/rbd.md#SP_rbd_default_map_options) |

**کارکرد:** default krbd map options

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_map_options "example"
ceph config get client rbd_default_map_options
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_map_options
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_order

| | |
|---|---|
| نوع | Uint · default `22` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_order](../../../config/rbd/rbd.md#SP_rbd_default_order) |

**کارکرد:** default order (data block object size) for new images This configures the default object size for new images. The value is used as a power of two, meaning ``default_object_size = 2 ^ rbd_default_order``. Configure a value between 12 and 25 (inclusive), translating to 4KiB lower and 32MiB upper limit.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_order 22
ceph config get client rbd_default_order
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `22`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_order
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_pool

| | |
|---|---|
| نوع | Str · default `rbd` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_pool](../../../config/rbd/rbd.md#SP_rbd_default_pool) |

**کارکرد:** default pool for storing new images

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_pool rbd
ceph config get client rbd_default_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `rbd`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_pool
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_snapshot_quiesce_mode

| | |
|---|---|
| نوع | Str · enum: ["required", "ignore-error", "skip"] · default `required` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_snapshot_quiesce_mode](../../../config/rbd/rbd.md#SP_rbd_default_snapshot_quiesce_mode) |

**کارکرد:** default snapshot quiesce mode

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_snapshot_quiesce_mode required
ceph config get client rbd_default_snapshot_quiesce_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `required`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_snapshot_quiesce_mode
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_stripe_count

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_stripe_count](../../../config/rbd/rbd.md#SP_rbd_default_stripe_count) |

**کارکرد:** default stripe count for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_stripe_count 64
ceph config get client rbd_default_stripe_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_stripe_count
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_stripe_unit

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_stripe_unit](../../../config/rbd/rbd.md#SP_rbd_default_stripe_unit) |

**کارکرد:** default stripe width for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_default_stripe_unit 64
ceph config get client rbd_default_stripe_unit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_default_stripe_unit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
