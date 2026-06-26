# QoS & throttling

راهنمای عمیق پیکربندی RBD — 20 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_qos_bps_burst](#rbd_qos_bps_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_bps_burst_seconds](#rbd_qos_bps_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_bps_limit](#rbd_qos_bps_limit) | `0` | Advanced | عملکرد |
| [rbd_qos_exclude_ops](#rbd_qos_exclude_ops) | `(empty)` | Advanced | عملکرد |
| [rbd_qos_iops_burst](#rbd_qos_iops_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_iops_burst_seconds](#rbd_qos_iops_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_iops_limit](#rbd_qos_iops_limit) | `0` | Advanced | عملکرد |
| [rbd_qos_read_bps_burst](#rbd_qos_read_bps_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_read_bps_burst_seconds](#rbd_qos_read_bps_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_read_bps_limit](#rbd_qos_read_bps_limit) | `0` | Advanced | عملکرد |
| [rbd_qos_read_iops_burst](#rbd_qos_read_iops_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_read_iops_burst_seconds](#rbd_qos_read_iops_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_read_iops_limit](#rbd_qos_read_iops_limit) | `0` | Advanced | عملکرد |
| [rbd_qos_schedule_tick_min](#rbd_qos_schedule_tick_min) | `50` | Advanced | عملکرد |
| [rbd_qos_write_bps_burst](#rbd_qos_write_bps_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_write_bps_burst_seconds](#rbd_qos_write_bps_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_write_bps_limit](#rbd_qos_write_bps_limit) | `0` | Advanced | عملکرد |
| [rbd_qos_write_iops_burst](#rbd_qos_write_iops_burst) | `0` | Advanced | عملکرد |
| [rbd_qos_write_iops_burst_seconds](#rbd_qos_write_iops_burst_seconds) | `1` | Advanced | عملکرد |
| [rbd_qos_write_iops_limit](#rbd_qos_write_iops_limit) | `0` | Advanced | عملکرد |

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

### rbd_qos_bps_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst) |

**کارکرد:** the desired burst limit of IO bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_bps_burst 64
ceph config get client rbd_qos_bps_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_bps_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_bps_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of IO bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_bps_burst_seconds 1
ceph config get client rbd_qos_bps_burst_seconds
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
ceph config get client rbd_qos_bps_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_bps_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_bps_limit) |

**کارکرد:** the desired limit of IO bytes per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_bps_limit 64
ceph config get client rbd_qos_bps_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_bps_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_exclude_ops

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_exclude_ops](../../../config/rbd/rbd.md#SP_rbd_qos_exclude_ops) |

**کارکرد:** optionally exclude ops from QoS Optionally exclude ops from QoS. This setting accepts either an integer bitmask value or comma-delimited string of op names. This setting is always internally stored as an integer bitmask value. The mapping between op bitmask value and op name is as follows: +1 -> read, +2 -> write, +4 -> discard, +8 -> write_same, +16 -> compare_and_write

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_exclude_ops "example"
ceph config get client rbd_qos_exclude_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_exclude_ops
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_iops_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst) |

**کارکرد:** the desired burst limit of IO operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_iops_burst 64
ceph config get client rbd_qos_iops_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_iops_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_iops_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of IO operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_iops_burst_seconds 1
ceph config get client rbd_qos_iops_burst_seconds
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
ceph config get client rbd_qos_iops_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_iops_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_iops_limit) |

**کارکرد:** the desired limit of IO operations per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_iops_limit 64
ceph config get client rbd_qos_iops_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_iops_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_bps_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst) |

**کارکرد:** the desired burst limit of read bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_read_bps_burst 64
ceph config get client rbd_qos_read_bps_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_read_bps_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_bps_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of read bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_read_bps_burst_seconds 1
ceph config get client rbd_qos_read_bps_burst_seconds
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
ceph config get client rbd_qos_read_bps_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_bps_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_limit) |

**کارکرد:** the desired limit of read bytes per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_read_bps_limit 64
ceph config get client rbd_qos_read_bps_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_read_bps_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_iops_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst) |

**کارکرد:** the desired burst limit of read operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_read_iops_burst 64
ceph config get client rbd_qos_read_iops_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_read_iops_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_iops_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of read operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_read_iops_burst_seconds 1
ceph config get client rbd_qos_read_iops_burst_seconds
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
ceph config get client rbd_qos_read_iops_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_read_iops_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_read_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_limit) |

**کارکرد:** the desired limit of read operations per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_read_iops_limit 64
ceph config get client rbd_qos_read_iops_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_read_iops_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_schedule_tick_min

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_schedule_tick_min](../../../config/rbd/rbd.md#SP_rbd_qos_schedule_tick_min) |

**کارکرد:** minimum schedule tick (in milliseconds) for QoS This determines the minimum time (in milliseconds) at which I/Os can become unblocked if the limit of a throttle is hit. In terms of the token bucket algorithm, this is the minimum interval at which tokens are added to the bucket.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_schedule_tick_min 50
ceph config get client rbd_qos_schedule_tick_min
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
ceph config get client rbd_qos_schedule_tick_min
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_bps_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst) |

**کارکرد:** the desired burst limit of write bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_write_bps_burst 64
ceph config get client rbd_qos_write_bps_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_write_bps_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_bps_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of write bytes

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_write_bps_burst_seconds 1
ceph config get client rbd_qos_write_bps_burst_seconds
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
ceph config get client rbd_qos_write_bps_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_bps_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_limit) |

**کارکرد:** the desired limit of write bytes per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_write_bps_limit 64
ceph config get client rbd_qos_write_bps_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_write_bps_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_iops_burst

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst) |

**کارکرد:** the desired burst limit of write operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_write_iops_burst 64
ceph config get client rbd_qos_write_iops_burst
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_write_iops_burst
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_iops_burst_seconds

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst_seconds) |

**کارکرد:** the desired burst duration in seconds of write operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_qos_write_iops_burst_seconds 1
ceph config get client rbd_qos_write_iops_burst_seconds
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
ceph config get client rbd_qos_write_iops_burst_seconds
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_qos_write_iops_limit

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_qos_write_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_limit) |

**کارکرد:** the desired limit of write operations per second

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_qos_write_iops_limit 64
ceph config get client rbd_qos_write_iops_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_qos_write_iops_limit
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
