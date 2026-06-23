# Cephx

راهنمای عمیق پیکربندی Global — 7 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cephx_cluster_require_signatures](#cephx_cluster_require_signatures) | `False` | Advanced | Performance |
| [cephx_cluster_require_version](#cephx_cluster_require_version) | `2` | Advanced | Performance |
| [cephx_require_signatures](#cephx_require_signatures) | `False` | Advanced | Performance |
| [cephx_require_version](#cephx_require_version) | `2` | Advanced | Performance |
| [cephx_service_require_signatures](#cephx_service_require_signatures) | `False` | Advanced | Performance |
| [cephx_service_require_version](#cephx_service_require_version) | `2` | Advanced | Performance |
| [cephx_sign_messages](#cephx_sign_messages) | `True` | Advanced | Performance |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **Dev** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephx_cluster_require_signatures

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [cephx.md#SP_cephx_cluster_require_signatures](../../../config/global/cephx.md#SP_cephx_cluster_require_signatures) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global cephx_cluster_require_signatures true
ceph config get global cephx_cluster_require_signatures
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_cluster_require_signatures
ceph -s
```

---

### cephx_cluster_require_version

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [cephx.md#SP_cephx_cluster_require_version](../../../config/global/cephx.md#SP_cephx_cluster_require_version) |

**کارکرد:** Cephx version required by the cluster from clients (1 = pre-mimic, 2 = mimic+)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global cephx_cluster_require_version 2
ceph config get global cephx_cluster_require_version
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_cluster_require_version
ceph -s
```

---

### cephx_require_signatures

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [cephx.md#SP_cephx_require_signatures](../../../config/global/cephx.md#SP_cephx_require_signatures) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global cephx_require_signatures true
ceph config get global cephx_require_signatures
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_require_signatures
ceph -s
```

---

### cephx_require_version

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [cephx.md#SP_cephx_require_version](../../../config/global/cephx.md#SP_cephx_require_version) |

**کارکرد:** Cephx version required (1 = pre-mimic, 2 = mimic+)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global cephx_require_version 2
ceph config get global cephx_require_version
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_require_version
ceph -s
```

---

### cephx_service_require_signatures

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [cephx.md#SP_cephx_service_require_signatures](../../../config/global/cephx.md#SP_cephx_service_require_signatures) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global cephx_service_require_signatures true
ceph config get global cephx_service_require_signatures
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_service_require_signatures
ceph -s
```

---

### cephx_service_require_version

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [cephx.md#SP_cephx_service_require_version](../../../config/global/cephx.md#SP_cephx_service_require_version) |

**کارکرد:** Cephx version required from ceph services (1 = pre-mimic, 2 = mimic+)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global cephx_service_require_version 2
ceph config get global cephx_service_require_version
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_service_require_version
ceph -s
```

---

### cephx_sign_messages

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [cephx.md#SP_cephx_sign_messages](../../../config/global/cephx.md#SP_cephx_sign_messages) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global cephx_sign_messages false
ceph config get global cephx_sign_messages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cephx_sign_messages
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
