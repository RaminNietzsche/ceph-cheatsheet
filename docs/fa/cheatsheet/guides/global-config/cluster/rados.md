# Rados

راهنمای عمیق پیکربندی Global — 5 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rados_mon_op_timeout](#rados_mon_op_timeout) | `0` | Advanced | عملکرد |
| [rados_osd_op_timeout](#rados_osd_op_timeout) | `0` | Advanced | عملکرد |
| [rados_replica_read_policy](#rados_replica_read_policy) | `default` | Advanced | عملکرد |
| [rados_replica_read_policy_on_objclass](#rados_replica_read_policy_on_objclass) | `False` | Advanced | عملکرد |
| [rados_tracing](#rados_tracing) | `False` | Advanced | عملکرد |

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

### rados_mon_op_timeout

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [rados.md#SP_rados_mon_op_timeout](../../../config/global/rados.md#SP_rados_mon_op_timeout) |

**کارکرد:** Timeout for operations handled by Monitors, for example statfs(). (0 is unlimited)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global rados_mon_op_timeout 0
ceph config get global rados_mon_op_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global rados_mon_op_timeout
ceph -s
```

---

### rados_osd_op_timeout

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [rados.md#SP_rados_osd_op_timeout](../../../config/global/rados.md#SP_rados_osd_op_timeout) |

**کارکرد:** Timeout for operations handled by OSDs, for example write(). (0 is unlimited)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global rados_osd_op_timeout 0
ceph config get global rados_osd_op_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global rados_osd_op_timeout
ceph -s
```

---

### rados_replica_read_policy

| | |
|---|---|
| نوع | Str · enum: ["default", "balance", "localize"] · default `default` · **Advanced** |
| جدول | [rados.md#SP_rados_replica_read_policy](../../../config/global/rados.md#SP_rados_replica_read_policy) |

**کارکرد:** Read policy for sending read requests to OSD

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global rados_replica_read_policy default
ceph config get global rados_replica_read_policy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `default`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global rados_replica_read_policy
ceph -s
```

---

### rados_replica_read_policy_on_objclass

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rados.md#SP_rados_replica_read_policy_on_objclass](../../../config/global/rados.md#SP_rados_replica_read_policy_on_objclass) |

**کارکرد:** Enable read policy for sending read requests to OSD on objclass ops

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global rados_replica_read_policy_on_objclass true
ceph config get global rados_replica_read_policy_on_objclass
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global rados_replica_read_policy_on_objclass
ceph -s
```

---

### rados_tracing

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rados.md#SP_rados_tracing](../../../config/global/rados.md#SP_rados_tracing) |

**کارکرد:** Should LTTng-UST tracepoints be enabled?

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global rados_tracing true
ceph config get global rados_tracing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global rados_tracing
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
