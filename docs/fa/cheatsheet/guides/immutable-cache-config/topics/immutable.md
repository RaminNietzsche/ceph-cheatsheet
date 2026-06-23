# Immutable object cache

راهنمای عمیق پیکربندی Immutable cache — 13 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/immutable-object-cache/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [immutable_object_cache_client_dedicated_thread_num](#immutable_object_cache_client_dedicated_thread_num) | `2` | Advanced | عملکرد |
| [immutable_object_cache_max_inflight_ops](#immutable_object_cache_max_inflight_ops) | `128` | Advanced | عملکرد |
| [immutable_object_cache_max_size](#immutable_object_cache_max_size) | `1_G` | Advanced | عملکرد |
| [immutable_object_cache_path](#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | Advanced | ظرفیت |
| [immutable_object_cache_qos_bps_burst](#immutable_object_cache_qos_bps_burst) | `0` | Advanced | عملکرد |
| [immutable_object_cache_qos_bps_burst_seconds](#immutable_object_cache_qos_bps_burst_seconds) | `1` | Advanced | عملکرد |
| [immutable_object_cache_qos_bps_limit](#immutable_object_cache_qos_bps_limit) | `0` | Advanced | عملکرد |
| [immutable_object_cache_qos_iops_burst](#immutable_object_cache_qos_iops_burst) | `0` | Advanced | عملکرد |
| [immutable_object_cache_qos_iops_burst_seconds](#immutable_object_cache_qos_iops_burst_seconds) | `1` | Advanced | عملکرد |
| [immutable_object_cache_qos_iops_limit](#immutable_object_cache_qos_iops_limit) | `0` | Advanced | عملکرد |
| [immutable_object_cache_qos_schedule_tick_min](#immutable_object_cache_qos_schedule_tick_min) | `50` | Advanced | عملکرد |
| [immutable_object_cache_sock](#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | Advanced | عملکرد |
| [immutable_object_cache_watermark](#immutable_object_cache_watermark) | `0.9` | Advanced | عملکرد |

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
ceph config get <daemon> <option>  # e.g. immutable-object-cache
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### immutable_object_cache_client_dedicated_thread_num

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_client_dedicated_thread_num](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_client_dedicated_thread_num) |

**کارکرد:** immutable object cache client dedicated thread number

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_client_dedicated_thread_num 2
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_client_dedicated_thread_num
ceph -s
```

---

### immutable_object_cache_max_inflight_ops

| | |
|---|---|
| نوع | Uint · default `128` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_max_inflight_ops](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_inflight_ops) |

**کارکرد:** max inflight promoting requests for immutable object cache daemon

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_inflight_ops 128
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_max_inflight_ops
ceph -s
```

---

### immutable_object_cache_max_size

| | |
|---|---|
| نوع | Size · default `1_G` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_max_size](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_max_size) |

**کارکرد:** max immutable object cache data size

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_max_size 1_G
ceph config get immutable_object_cache immutable_object_cache_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_max_size
ceph -s
```

---

### immutable_object_cache_path

| | |
|---|---|
| نوع | Str · default `/tmp/ceph_immutable_object_cache` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_path](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_path) |

**کارکرد:** immutable object cache data dir

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_path "/tmp/ceph_immutable_object_cache"
ceph config get immutable_object_cache immutable_object_cache_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `/tmp/ceph_immutable_object_cache`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_path
ceph -s
```

---

### immutable_object_cache_qos_bps_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_bps_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst) |

**کارکرد:** the desired burst limit of immutable object cache IO bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst
ceph -s
```

---

### immutable_object_cache_qos_bps_burst_seconds

| | |
|---|---|
| نوع | Secs · default `1` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of immutable object cache IO bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_bps_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_bps_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_bps_limit) |

**کارکرد:** the desired immutable object cache IO bytes limit per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_bps_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_bps_limit
ceph -s
```

---

### immutable_object_cache_qos_iops_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_iops_burst](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst) |

**کارکرد:** the desired burst limit of immutable object cache IO operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst
ceph -s
```

---

### immutable_object_cache_qos_iops_burst_seconds

| | |
|---|---|
| نوع | Secs · default `1` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of immutable object cache IO operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_burst_seconds 1
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_burst_seconds
ceph -s
```

---

### immutable_object_cache_qos_iops_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_iops_limit](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_iops_limit) |

**کارکرد:** the desired immutable object cache IO operations limit per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_iops_limit 64
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_iops_limit
ceph -s
```

---

### immutable_object_cache_qos_schedule_tick_min

| | |
|---|---|
| نوع | Millisecs · default `50` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_qos_schedule_tick_min](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_qos_schedule_tick_min) |

**کارکرد:** minimum schedule tick for immutable object cache

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_qos_schedule_tick_min 50
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_qos_schedule_tick_min
ceph -s
```

---

### immutable_object_cache_sock

| | |
|---|---|
| نوع | Str · default `/var/run/ceph/immutable_object_cache_sock` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_sock](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_sock) |

**کارکرد:** immutable object cache domain socket

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_sock "/var/run/ceph/immutable_object_cache_sock"
ceph config get immutable_object_cache immutable_object_cache_sock
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `/var/run/ceph/immutable_object_cache_sock`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_sock
ceph -s
```

---

### immutable_object_cache_watermark

| | |
|---|---|
| نوع | Float · default `0.9` · **Advanced** |
| جدول | [immutable.md#SP_immutable_object_cache_watermark](../../../config/immutable-object-cache/immutable.md#SP_immutable_object_cache_watermark) |

**کارکرد:** immutable object cache water mark

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set immutable_object_cache immutable_object_cache_watermark 0.9
ceph config get immutable_object_cache immutable_object_cache_watermark
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.9`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get immutable_object_cache immutable_object_cache_watermark
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
