# Objecter

راهنمای عمیق پیکربندی Global — 8 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [objecter_completion_locks_per_session](#objecter_completion_locks_per_session) | `32` | Dev | توسعه |
| [objecter_debug_inject_relock_delay](#objecter_debug_inject_relock_delay) | `False` | Dev | توسعه |
| [objecter_inflight_op_bytes](#objecter_inflight_op_bytes) | `100_M` | Advanced | عملکرد |
| [objecter_inflight_ops](#objecter_inflight_ops) | `1_K` | Advanced | عملکرد |
| [objecter_inject_no_watch_ping](#objecter_inject_no_watch_ping) | `False` | Dev | توسعه |
| [objecter_retry_writes_after_first_reply](#objecter_retry_writes_after_first_reply) | `False` | Dev | توسعه |
| [objecter_tick_interval](#objecter_tick_interval) | `5` | Dev | توسعه |
| [objecter_timeout](#objecter_timeout) | `10` | Advanced | عملکرد |

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

### objecter_completion_locks_per_session

| | |
|---|---|
| نوع | Uint · default `32` · **Dev** |
| جدول | [objecter.md#SP_objecter_completion_locks_per_session](../../../config/global/objecter.md#SP_objecter_completion_locks_per_session) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objecter_completion_locks_per_session 32
ceph config get global objecter_completion_locks_per_session
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`32`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### objecter_debug_inject_relock_delay

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [objecter.md#SP_objecter_debug_inject_relock_delay](../../../config/global/objecter.md#SP_objecter_debug_inject_relock_delay) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objecter_debug_inject_relock_delay true
ceph config get global objecter_debug_inject_relock_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### objecter_inflight_op_bytes

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [objecter.md#SP_objecter_inflight_op_bytes](../../../config/global/objecter.md#SP_objecter_inflight_op_bytes) |

**کارکرد:** Max in-flight data in bytes (both directions)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global objecter_inflight_op_bytes 100_M
ceph config get global objecter_inflight_op_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global objecter_inflight_op_bytes
ceph -s
```

---

### objecter_inflight_ops

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [objecter.md#SP_objecter_inflight_ops](../../../config/global/objecter.md#SP_objecter_inflight_ops) |

**کارکرد:** Max in-flight operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global objecter_inflight_ops 1_K
ceph config get global objecter_inflight_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global objecter_inflight_ops
ceph -s
```

---

### objecter_inject_no_watch_ping

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [objecter.md#SP_objecter_inject_no_watch_ping](../../../config/global/objecter.md#SP_objecter_inject_no_watch_ping) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objecter_inject_no_watch_ping true
ceph config get global objecter_inject_no_watch_ping
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### objecter_retry_writes_after_first_reply

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [objecter.md#SP_objecter_retry_writes_after_first_reply](../../../config/global/objecter.md#SP_objecter_retry_writes_after_first_reply) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objecter_retry_writes_after_first_reply true
ceph config get global objecter_retry_writes_after_first_reply
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### objecter_tick_interval

| | |
|---|---|
| نوع | Float · default `5` · **Dev** |
| جدول | [objecter.md#SP_objecter_tick_interval](../../../config/global/objecter.md#SP_objecter_tick_interval) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global objecter_tick_interval 5
ceph config get global objecter_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### objecter_timeout

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [objecter.md#SP_objecter_timeout](../../../config/global/objecter.md#SP_objecter_timeout) |

**کارکرد:** Seconds before in-flight op is considered laggy and we query the Monitors for the latest OSDMap

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global objecter_timeout 10
ceph config get global objecter_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global objecter_timeout
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
