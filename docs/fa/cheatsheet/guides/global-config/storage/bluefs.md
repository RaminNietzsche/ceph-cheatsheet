# Bluefs

راهنمای عمیق پیکربندی Global — 24 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [bluefs_alloc_size](#bluefs_alloc_size) | `1_M` | Advanced | عملکرد |
| [bluefs_allocator](#bluefs_allocator) | `hybrid` | Dev | توسعه |
| [bluefs_buffered_io](#bluefs_buffered_io) | `True` | Advanced | عملکرد |
| [bluefs_check_for_zeros](#bluefs_check_for_zeros) | `False` | Dev | توسعه |
| [bluefs_check_volume_selector_often](#bluefs_check_volume_selector_often) | `False` | Dev | توسعه |
| [bluefs_check_volume_selector_on_mount](#bluefs_check_volume_selector_on_mount) | `False` | Dev | توسعه |
| [bluefs_compact_log_sync](#bluefs_compact_log_sync) | `False` | Advanced | عملکرد |
| [bluefs_debug_force_slow](#bluefs_debug_force_slow) | `False` | Dev | توسعه |
| [bluefs_failed_shared_alloc_cooldown](#bluefs_failed_shared_alloc_cooldown) | `600` | Advanced | عملکرد |
| [bluefs_log_compact_min_ratio](#bluefs_log_compact_min_ratio) | `5` | Advanced | عملکرد |
| [bluefs_log_compact_min_size](#bluefs_log_compact_min_size) | `16_M` | Advanced | عملکرد |
| [bluefs_log_replay_check_allocations](#bluefs_log_replay_check_allocations) | `True` | Advanced | عملکرد |
| [bluefs_max_log_runway](#bluefs_max_log_runway) | `4_M` | Advanced | عملکرد |
| [bluefs_max_prefetch](#bluefs_max_prefetch) | `1_M` | Advanced | عملکرد |
| [bluefs_min_flush_size](#bluefs_min_flush_size) | `512_K` | Advanced | عملکرد |
| [bluefs_min_log_runway](#bluefs_min_log_runway) | `1_M` | Advanced | عملکرد |
| [bluefs_replay_recovery](#bluefs_replay_recovery) | `False` | Dev | توسعه |
| [bluefs_replay_recovery_disable_compact](#bluefs_replay_recovery_disable_compact) | `False` | Advanced | سیاست |
| [bluefs_shared_alloc_size](#bluefs_shared_alloc_size) | `64_K` | Advanced | عملکرد |
| [bluefs_spillover_cleaner](#bluefs_spillover_cleaner) | `False` | Advanced | عملکرد |
| [bluefs_spillover_cleaner_work_ratio](#bluefs_spillover_cleaner_work_ratio) | `0.1` | Advanced | عملکرد |
| [bluefs_spillover_idle_time](#bluefs_spillover_idle_time) | `1200` | Advanced | عملکرد |
| [bluefs_sync_write](#bluefs_sync_write) | `False` | Advanced | عملکرد |
| [bluefs_wal_envelope_mode](#bluefs_wal_envelope_mode) | `True` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### bluefs_alloc_size

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_alloc_size](../../../config/global/bluefs.md#SP_bluefs_alloc_size) |

**کارکرد:** Allocation unit size for DB and WAL devices

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluefs_alloc_size 1_M
ceph config get global bluefs_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_alloc_size
ceph -s
```

---

### bluefs_allocator

| | |
|---|---|
| نوع | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Dev** |
| جدول | [bluefs.md#SP_bluefs_allocator](../../../config/global/bluefs.md#SP_bluefs_allocator) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_allocator hybrid
ceph config get global bluefs_allocator
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`hybrid`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_buffered_io

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_buffered_io](../../../config/global/bluefs.md#SP_bluefs_buffered_io) |

**کارکرد:** Enabled buffered IO for BlueFS reads.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluefs_buffered_io false
ceph config get global bluefs_buffered_io
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_buffered_io
ceph -s
```

---

### bluefs_check_for_zeros

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluefs.md#SP_bluefs_check_for_zeros](../../../config/global/bluefs.md#SP_bluefs_check_for_zeros) |

**کارکرد:** Check data read for suspicious pages

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_check_for_zeros true
ceph config get global bluefs_check_for_zeros
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_check_volume_selector_often

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [bluefs.md#SP_bluefs_check_volume_selector_often](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_often) |

**کارکرد:** Periodically check validity of volume selector

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_check_volume_selector_often true
ceph config get global bluefs_check_volume_selector_often
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_check_volume_selector_on_mount

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluefs.md#SP_bluefs_check_volume_selector_on_mount](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_on_mount) |

**کارکرد:** Check validity of volume selector on mount/umount

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_check_volume_selector_on_mount true
ceph config get global bluefs_check_volume_selector_on_mount
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_compact_log_sync

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_compact_log_sync](../../../config/global/bluefs.md#SP_bluefs_compact_log_sync) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluefs_compact_log_sync true
ceph config get global bluefs_compact_log_sync
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_compact_log_sync
ceph -s
```

---

### bluefs_debug_force_slow

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluefs.md#SP_bluefs_debug_force_slow](../../../config/global/bluefs.md#SP_bluefs_debug_force_slow) |

**کارکرد:** For testing. Force BlueFS to allocate files on slow device.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_debug_force_slow true
ceph config get global bluefs_debug_force_slow
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_failed_shared_alloc_cooldown

| | |
|---|---|
| نوع | Float · default `600` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_failed_shared_alloc_cooldown](../../../config/global/bluefs.md#SP_bluefs_failed_shared_alloc_cooldown) |

**کارکرد:** duration(in seconds) untill the next attempt to use 'bluefs_shared_alloc_size' after facing ENOSPC failure.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluefs_failed_shared_alloc_cooldown 600
ceph config get global bluefs_failed_shared_alloc_cooldown
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `600`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_failed_shared_alloc_cooldown
ceph -s
```

---

### bluefs_log_compact_min_ratio

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_log_compact_min_ratio](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_ratio) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_log_compact_min_ratio 5
ceph config get global bluefs_log_compact_min_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_log_compact_min_ratio
ceph -s
```

---

### bluefs_log_compact_min_size

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_log_compact_min_size](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_log_compact_min_size 16_M
ceph config get global bluefs_log_compact_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_log_compact_min_size
ceph -s
```

---

### bluefs_log_replay_check_allocations

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_log_replay_check_allocations](../../../config/global/bluefs.md#SP_bluefs_log_replay_check_allocations) |

**کارکرد:** Enables checks for allocations consistency during log replay

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluefs_log_replay_check_allocations false
ceph config get global bluefs_log_replay_check_allocations
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_log_replay_check_allocations
ceph -s
```

---

### bluefs_max_log_runway

| | |
|---|---|
| نوع | Size · default `4_M` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_max_log_runway](../../../config/global/bluefs.md#SP_bluefs_max_log_runway) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_max_log_runway 4_M
ceph config get global bluefs_max_log_runway
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_max_log_runway
ceph -s
```

---

### bluefs_max_prefetch

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_max_prefetch](../../../config/global/bluefs.md#SP_bluefs_max_prefetch) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_max_prefetch 1_M
ceph config get global bluefs_max_prefetch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_max_prefetch
ceph -s
```

---

### bluefs_min_flush_size

| | |
|---|---|
| نوع | Size · default `512_K` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_min_flush_size](../../../config/global/bluefs.md#SP_bluefs_min_flush_size) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_min_flush_size 512_K
ceph config get global bluefs_min_flush_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `512_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_min_flush_size
ceph -s
```

---

### bluefs_min_log_runway

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_min_log_runway](../../../config/global/bluefs.md#SP_bluefs_min_log_runway) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global bluefs_min_log_runway 1_M
ceph config get global bluefs_min_log_runway
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_min_log_runway
ceph -s
```

---

### bluefs_replay_recovery

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [bluefs.md#SP_bluefs_replay_recovery](../../../config/global/bluefs.md#SP_bluefs_replay_recovery) |

**کارکرد:** Attempt to read bluefs log so large that it became unreadable.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global bluefs_replay_recovery true
ceph config get global bluefs_replay_recovery
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### bluefs_replay_recovery_disable_compact

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_replay_recovery_disable_compact](../../../config/global/bluefs.md#SP_bluefs_replay_recovery_disable_compact) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluefs_replay_recovery_disable_compact true
ceph config get global bluefs_replay_recovery_disable_compact
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_replay_recovery_disable_compact
ceph -s
```

---

### bluefs_shared_alloc_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_shared_alloc_size](../../../config/global/bluefs.md#SP_bluefs_shared_alloc_size) |

**کارکرد:** Allocation unit size for primary/shared device

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluefs_shared_alloc_size 64_K
ceph config get global bluefs_shared_alloc_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_shared_alloc_size
ceph -s
```

---

### bluefs_spillover_cleaner

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_spillover_cleaner](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner) |

**کارکرد:** Enable Background BlueFS Spillover cleaner thread

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluefs_spillover_cleaner true
ceph config get global bluefs_spillover_cleaner
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_spillover_cleaner
ceph -s
```

---

### bluefs_spillover_cleaner_work_ratio

| | |
|---|---|
| نوع | Float · default `0.1` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_spillover_cleaner_work_ratio](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner_work_ratio) |

**کارکرد:** Fraction of time the BlueFS spillover cleaner spends performing work.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluefs_spillover_cleaner_work_ratio 0.1
ceph config get global bluefs_spillover_cleaner_work_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_spillover_cleaner_work_ratio
ceph -s
```

---

### bluefs_spillover_idle_time

| | |
|---|---|
| نوع | Uint · default `1200` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_spillover_idle_time](../../../config/global/bluefs.md#SP_bluefs_spillover_idle_time) |

**کارکرد:** Idle time in seconds before the BlueFS spillover cleaner wakes up for the next scan cycle.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global bluefs_spillover_idle_time 1200
ceph config get global bluefs_spillover_idle_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_spillover_idle_time
ceph -s
```

---

### bluefs_sync_write

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_sync_write](../../../config/global/bluefs.md#SP_bluefs_sync_write) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global bluefs_sync_write true
ceph config get global bluefs_sync_write
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_sync_write
ceph -s
```

---

### bluefs_wal_envelope_mode

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [bluefs.md#SP_bluefs_wal_envelope_mode](../../../config/global/bluefs.md#SP_bluefs_wal_envelope_mode) |

**کارکرد:** Enables a faster backend in BlueFS for WAL writes.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global bluefs_wal_envelope_mode false
ceph config get global bluefs_wal_envelope_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global bluefs_wal_envelope_mode
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
