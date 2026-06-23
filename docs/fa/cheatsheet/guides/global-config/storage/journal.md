# Journal

راهنمای عمیق پیکربندی Global — 17 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [journal_aio](#journal_aio) | `True` | Dev | توسعه |
| [journal_align_min_size](#journal_align_min_size) | `64_K` | Dev | توسعه |
| [journal_block_align](#journal_block_align) | `True` | Dev | توسعه |
| [journal_block_size](#journal_block_size) | `4_K` | Dev | توسعه |
| [journal_dio](#journal_dio) | `True` | Dev | توسعه |
| [journal_discard](#journal_discard) | `False` | Dev | توسعه |
| [journal_force_aio](#journal_force_aio) | `False` | Dev | توسعه |
| [journal_ignore_corruption](#journal_ignore_corruption) | `False` | Dev | توسعه |
| [journal_max_write_bytes](#journal_max_write_bytes) | `10_M` | Advanced | عملکرد |
| [journal_max_write_entries](#journal_max_write_entries) | `100` | Advanced | عملکرد |
| [journal_replay_from](#journal_replay_from) | `0` | Dev | توسعه |
| [journal_throttle_high_multiple](#journal_throttle_high_multiple) | `0` | Dev | توسعه |
| [journal_throttle_high_threshhold](#journal_throttle_high_threshhold) | `0.9` | Dev | توسعه |
| [journal_throttle_low_threshhold](#journal_throttle_low_threshhold) | `0.6` | Dev | توسعه |
| [journal_throttle_max_multiple](#journal_throttle_max_multiple) | `0` | Dev | توسعه |
| [journal_write_header_frequency](#journal_write_header_frequency) | `0` | Dev | توسعه |
| [journal_zero_on_create](#journal_zero_on_create) | `False` | Dev | توسعه |

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

### journal_aio

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [journal.md#SP_journal_aio](../../../config/global/journal.md#SP_journal_aio) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_aio false
ceph config get global journal_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_align_min_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [journal.md#SP_journal_align_min_size](../../../config/global/journal.md#SP_journal_align_min_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_align_min_size 64_K
ceph config get global journal_align_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_block_align

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [journal.md#SP_journal_block_align](../../../config/global/journal.md#SP_journal_block_align) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_block_align false
ceph config get global journal_block_align
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_block_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Dev** |
| جدول | [journal.md#SP_journal_block_size](../../../config/global/journal.md#SP_journal_block_size) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_block_size 4_K
ceph config get global journal_block_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`4_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_dio

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [journal.md#SP_journal_dio](../../../config/global/journal.md#SP_journal_dio) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_dio false
ceph config get global journal_dio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_discard

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [journal.md#SP_journal_discard](../../../config/global/journal.md#SP_journal_discard) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_discard true
ceph config get global journal_discard
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_force_aio

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [journal.md#SP_journal_force_aio](../../../config/global/journal.md#SP_journal_force_aio) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_force_aio true
ceph config get global journal_force_aio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_ignore_corruption

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [journal.md#SP_journal_ignore_corruption](../../../config/global/journal.md#SP_journal_ignore_corruption) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_ignore_corruption true
ceph config get global journal_ignore_corruption
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_max_write_bytes

| | |
|---|---|
| نوع | Size · default `10_M` · **Advanced** |
| جدول | [journal.md#SP_journal_max_write_bytes](../../../config/global/journal.md#SP_journal_max_write_bytes) |

**کارکرد:** Max bytes in flight to journal

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global journal_max_write_bytes 10_M
ceph config get global journal_max_write_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global journal_max_write_bytes
ceph -s
```

---

### journal_max_write_entries

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [journal.md#SP_journal_max_write_entries](../../../config/global/journal.md#SP_journal_max_write_entries) |

**کارکرد:** Max IOs in flight to journal (deprecated)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global journal_max_write_entries 100
ceph config get global journal_max_write_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global journal_max_write_entries
ceph -s
```

---

### journal_replay_from

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [journal.md#SP_journal_replay_from](../../../config/global/journal.md#SP_journal_replay_from) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_replay_from 64
ceph config get global journal_replay_from
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_throttle_high_multiple

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [journal.md#SP_journal_throttle_high_multiple](../../../config/global/journal.md#SP_journal_throttle_high_multiple) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_throttle_high_multiple 0
ceph config get global journal_throttle_high_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_throttle_high_threshhold

| | |
|---|---|
| نوع | Float · default `0.9` · **Dev** |
| جدول | [journal.md#SP_journal_throttle_high_threshhold](../../../config/global/journal.md#SP_journal_throttle_high_threshhold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_throttle_high_threshhold 0.9
ceph config get global journal_throttle_high_threshhold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.9`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_throttle_low_threshhold

| | |
|---|---|
| نوع | Float · default `0.6` · **Dev** |
| جدول | [journal.md#SP_journal_throttle_low_threshhold](../../../config/global/journal.md#SP_journal_throttle_low_threshhold) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_throttle_low_threshhold 0.6
ceph config get global journal_throttle_low_threshhold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.6`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_throttle_max_multiple

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [journal.md#SP_journal_throttle_max_multiple](../../../config/global/journal.md#SP_journal_throttle_max_multiple) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_throttle_max_multiple 0
ceph config get global journal_throttle_max_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_write_header_frequency

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [journal.md#SP_journal_write_header_frequency](../../../config/global/journal.md#SP_journal_write_header_frequency) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_write_header_frequency 64
ceph config get global journal_write_header_frequency
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### journal_zero_on_create

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [journal.md#SP_journal_zero_on_create](../../../config/global/journal.md#SP_journal_zero_on_create) |

**کارکرد:** Deprecated

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global journal_zero_on_create true
ceph config get global journal_zero_on_create
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
