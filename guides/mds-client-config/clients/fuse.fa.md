# FUSE client

deep dive پیکربندی MDS client — 15 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds-client/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [fuse_allow_other](#fuse_allow_other) | `True` | Advanced | Policy |
| [fuse_atomic_o_trunc](#fuse_atomic_o_trunc) | `True` | Advanced | Performance |
| [fuse_big_writes](#fuse_big_writes) | `True` | Advanced | Performance |
| [fuse_debug](#fuse_debug) | `False` | Advanced | Performance |
| [fuse_default_permissions](#fuse_default_permissions) | `False` | Advanced | Performance |
| [fuse_disable_pagecache](#fuse_disable_pagecache) | `False` | Advanced | Policy |
| [fuse_max_write](#fuse_max_write) | `0` | Advanced | Performance |
| [fuse_multithreaded](#fuse_multithreaded) | `True` | Advanced | Performance |
| [fuse_require_active_mds](#fuse_require_active_mds) | `True` | Advanced | Performance |
| [fuse_set_user_groups](#fuse_set_user_groups) | `True` | Advanced | Performance |
| [fuse_splice_move](#fuse_splice_move) | `True` | Advanced | Performance |
| [fuse_splice_read](#fuse_splice_read) | `True` | Advanced | Performance |
| [fuse_splice_write](#fuse_splice_write) | `True` | Advanced | Performance |
| [fuse_syncfs_on_mksnap](#fuse_syncfs_on_mksnap) | `True` | Advanced | Performance |
| [fuse_use_invalidate_cb](#fuse_use_invalidate_cb) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mds-client
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### fuse_allow_other

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_allow_other](../../../config/mds-client/fuse.md#SP_fuse_allow_other) |

**کارکرد:** pass allow_other to FUSE on mount

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_allow_other false
ceph config get client fuse_allow_other
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_allow_other
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_atomic_o_trunc

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_atomic_o_trunc](../../../config/mds-client/fuse.md#SP_fuse_atomic_o_trunc) |

**کارکرد:** pass atomic_o_trunc flag to FUSE on mount

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_atomic_o_trunc false
ceph config get client fuse_atomic_o_trunc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_atomic_o_trunc
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_big_writes

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_big_writes](../../../config/mds-client/fuse.md#SP_fuse_big_writes) |

**کارکرد:** big_writes is deprecated in libfuse 3.0.0

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_big_writes false
ceph config get client fuse_big_writes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_big_writes
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_debug

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [fuse.md#SP_fuse_debug](../../../config/mds-client/fuse.md#SP_fuse_debug) |

**کارکرد:** enable debugging for the libfuse

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set client fuse_debug true
ceph config get client fuse_debug
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_debug
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_default_permissions

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [fuse.md#SP_fuse_default_permissions](../../../config/mds-client/fuse.md#SP_fuse_default_permissions) |

**کارکرد:** pass default_permisions to FUSE on mount

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client fuse_default_permissions true
ceph config get client fuse_default_permissions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_default_permissions
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_disable_pagecache

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [fuse.md#SP_fuse_disable_pagecache](../../../config/mds-client/fuse.md#SP_fuse_disable_pagecache) |

**کارکرد:** disable page caching in the kernel for this FUSE mount

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set client fuse_disable_pagecache true
ceph config get client fuse_disable_pagecache
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_disable_pagecache
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_max_write

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [fuse.md#SP_fuse_max_write](../../../config/mds-client/fuse.md#SP_fuse_max_write) |

**کارکرد:** set the maximum number of bytes in a single write operation

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client fuse_max_write 64
ceph config get client fuse_max_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_max_write
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_multithreaded

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_multithreaded](../../../config/mds-client/fuse.md#SP_fuse_multithreaded) |

**کارکرد:** allow parallel processing through FUSE library

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_multithreaded false
ceph config get client fuse_multithreaded
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_multithreaded
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_require_active_mds

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_require_active_mds](../../../config/mds-client/fuse.md#SP_fuse_require_active_mds) |

**کارکرد:** require active MDSs in the file system when mounting

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_require_active_mds false
ceph config get client fuse_require_active_mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_require_active_mds
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_set_user_groups

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_set_user_groups](../../../config/mds-client/fuse.md#SP_fuse_set_user_groups) |

**کارکرد:** check for ceph-fuse to consider supplementary groups for permissions

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_set_user_groups false
ceph config get client fuse_set_user_groups
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_set_user_groups
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_splice_move

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_splice_move](../../../config/mds-client/fuse.md#SP_fuse_splice_move) |

**کارکرد:** enable splice move to reduce the memory copies

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_splice_move false
ceph config get client fuse_splice_move
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_splice_move
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_splice_read

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_splice_read](../../../config/mds-client/fuse.md#SP_fuse_splice_read) |

**کارکرد:** enable splice read to reduce the memory copies

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_splice_read false
ceph config get client fuse_splice_read
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_splice_read
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_splice_write

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_splice_write](../../../config/mds-client/fuse.md#SP_fuse_splice_write) |

**کارکرد:** enable splice write to reduce the memory copies

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_splice_write false
ceph config get client fuse_splice_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_splice_write
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_syncfs_on_mksnap

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_syncfs_on_mksnap](../../../config/mds-client/fuse.md#SP_fuse_syncfs_on_mksnap) |

**کارکرد:** synchronize all local metadata/file changes after snapshot

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_syncfs_on_mksnap false
ceph config get client fuse_syncfs_on_mksnap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_syncfs_on_mksnap
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---

### fuse_use_invalidate_cb

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [fuse.md#SP_fuse_use_invalidate_cb](../../../config/mds-client/fuse.md#SP_fuse_use_invalidate_cb) |

**کارکرد:** use fuse 2.8+ invalidate callback to keep page cache consistent

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set client fuse_use_invalidate_cb false
ceph config get client fuse_use_invalidate_cb
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get client fuse_use_invalidate_cb
ceph -s
# گزینه‌های client: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
