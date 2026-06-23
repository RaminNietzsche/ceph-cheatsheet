# Public

deep dive پیکربندی Global — 5 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [public_addr](#public_addr) | `(empty)` | Basic | Connectivity |
| [public_addrv](#public_addrv) | `(empty)` | Basic | Policy |
| [public_bind_addr](#public_bind_addr) | `(empty)` | Advanced | Connectivity |
| [public_network](#public_network) | `(empty)` | Advanced | Performance |
| [public_network_interface](#public_network_interface) | `(empty)` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### public_addr

| | |
|---|---|
| نوع | Addr · default `(empty)` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [public.md#SP_public_addr](../../../config/global/public.md#SP_public_addr) |

**کارکرد:** Public-facing address to which to bind

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global public_addr (empty)
ceph config get global public_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. endpointهای کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. endpoint پایدار با کمترین latency را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global public_addr
ceph -s
```

---

### public_addrv

| | |
|---|---|
| نوع | Addrvec · default `(empty)` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [public.md#SP_public_addrv](../../../config/global/public.md#SP_public_addrv) |

**کارکرد:** Public-facing addresses to which services are to bind

**زمان استفاده:** رفتار اصلی Global — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set global public_addrv (empty)
ceph config get global public_addrv
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `(empty)` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global public_addrv
ceph -s
```

---

### public_bind_addr

| | |
|---|---|
| نوع | Addr · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [public.md#SP_public_bind_addr](../../../config/global/public.md#SP_public_bind_addr) |

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global public_bind_addr (empty)
ceph config get global public_bind_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. endpointهای کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. endpoint پایدار با کمترین latency را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global public_bind_addr
ceph -s
```

---

### public_network

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [public.md#SP_public_network](../../../config/global/public.md#SP_public_network) |

**کارکرد:** Network(s) from which to choose a public address to bind to

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global public_network "example"
ceph config get global public_network
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global public_network
ceph -s
```

---

### public_network_interface

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [public.md#SP_public_network_interface](../../../config/global/public.md#SP_public_network_interface) |

**کارکرد:** Interface name(s) from which to choose an address from a ``public_network`` to bind to; ``public_network`` must also be specified.

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global public_network_interface "example"
ceph config get global public_network_interface
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global public_network_interface
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
