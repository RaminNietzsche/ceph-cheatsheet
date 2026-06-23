# Defaults

deep dive پیکربندی RBD — 10 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_default_clone_format](#rbd_default_clone_format) | `auto` | Advanced | Performance |
| [rbd_default_data_pool](#rbd_default_data_pool) | `(empty)` | Advanced | Performance |
| [rbd_default_features](#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Advanced | Performance |
| [rbd_default_format](#rbd_default_format) | `2` | Advanced | Performance |
| [rbd_default_map_options](#rbd_default_map_options) | `(empty)` | Advanced | Performance |
| [rbd_default_order](#rbd_default_order) | `22` | Advanced | Performance |
| [rbd_default_pool](#rbd_default_pool) | `rbd` | Advanced | Performance |
| [rbd_default_snapshot_quiesce_mode](#rbd_default_snapshot_quiesce_mode) | `required` | Advanced | Performance |
| [rbd_default_stripe_count](#rbd_default_stripe_count) | `0` | Advanced | Performance |
| [rbd_default_stripe_unit](#rbd_default_stripe_unit) | `0` | Advanced | Performance |

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

**کارکرد:** default internal format for handling clones

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_clone_format auto
ceph config get client rbd_default_clone_format
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `auto`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_clone_format
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_data_pool

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_data_pool](../../../config/rbd/rbd.md#SP_rbd_default_data_pool) |

**کارکرد:** default pool for storing data blocks for new images &#91;&#93;(std::string *value, std::string *error_message) { std::regex pattern("^&#91;^@/&#93;*$"); if (!std::regex_match (*value, pattern)) { *value = ""; *error_message = "ignoring invalid RBD data pool"; } return 0; }

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_data_pool "example"
ceph config get client rbd_default_data_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_data_pool
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_features

| | |
|---|---|
| نوع | Str · default `layering,exclusive-lock,object-map,fast-diff,deep-flatten` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_features](../../../config/rbd/rbd.md#SP_rbd_default_features) |

**کارکرد:** default v2 image features for new images &#91;&#93;(std::string *value, std::string *error_message) { std::stringstream ss; uint64_t features = librbd::rbd_features_from_string(*value, &ss); // Leave this in integer form to avoid breaking Cinder. Someday // we would like to present this in string form instead... *value = stringify(features); if (ss.str().size()) { return -EINVAL; } return 0; }

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_features "layering,exclusive-lock,object-map,fast-diff,deep-flatten"
ceph config get client rbd_default_features
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `layering,exclusive-lock,object-map,fast-diff,deep-flatten`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_features
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_format

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_format](../../../config/rbd/rbd.md#SP_rbd_default_format) |

**کارکرد:** default image format for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_format 2
ceph config get client rbd_default_format
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_format
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_map_options

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_map_options](../../../config/rbd/rbd.md#SP_rbd_default_map_options) |

**کارکرد:** default krbd map options

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_map_options "example"
ceph config get client rbd_default_map_options
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_map_options
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_order

| | |
|---|---|
| نوع | Uint · default `22` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_order](../../../config/rbd/rbd.md#SP_rbd_default_order) |

**کارکرد:** default order (data block object size) for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_order 22
ceph config get client rbd_default_order
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `22`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_order
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_pool

| | |
|---|---|
| نوع | Str · default `rbd` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_pool](../../../config/rbd/rbd.md#SP_rbd_default_pool) |

**کارکرد:** default pool for storing new images &#91;&#93;(std::string *value, std::string *error_message) { std::regex pattern("^&#91;^@/&#93;+$"); if (!std::regex_match (*value, pattern)) { *value = "rbd"; *error_message = "invalid RBD default pool, resetting to 'rbd'"; } return 0; }

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_pool rbd
ceph config get client rbd_default_pool
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `rbd`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_pool
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_snapshot_quiesce_mode

| | |
|---|---|
| نوع | Str · enum: ["required", "ignore-error", "skip"] · default `required` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_snapshot_quiesce_mode](../../../config/rbd/rbd.md#SP_rbd_default_snapshot_quiesce_mode) |

**کارکرد:** default snapshot quiesce mode

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_snapshot_quiesce_mode required
ceph config get client rbd_default_snapshot_quiesce_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `required`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_snapshot_quiesce_mode
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_stripe_count

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_stripe_count](../../../config/rbd/rbd.md#SP_rbd_default_stripe_count) |

**کارکرد:** default stripe count for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_stripe_count 64
ceph config get client rbd_default_stripe_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_stripe_count
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_default_stripe_unit

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_default_stripe_unit](../../../config/rbd/rbd.md#SP_rbd_default_stripe_unit) |

**کارکرد:** default stripe width for new images

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set client rbd_default_stripe_unit 64
ceph config get client rbd_default_stripe_unit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client rbd_default_stripe_unit
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
