# Admin

راهنمای عمیق پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [admin_socket](#admin_socket) | `$run_dir/$cluster-$name.asok` | Advanced | عملکرد |
| [admin_socket_mode](#admin_socket_mode) | `(empty)` | Advanced | عملکرد |

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

### admin_socket

| | |
|---|---|
| نوع | Str · default `$run_dir/$cluster-$name.asok` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [admin.md#SP_admin_socket](../../../config/global/admin.md#SP_admin_socket) |

**کارکرد:** Path for the runtime control socket file, used by the 'ceph daemon' command

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global admin_socket "$run_dir/$cluster-$name.asok"
ceph config get global admin_socket
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `$run_dir/$cluster-$name.asok`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global admin_socket
ceph -s
```

---

### admin_socket_mode

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [admin.md#SP_admin_socket_mode](../../../config/global/admin.md#SP_admin_socket_mode) |

**کارکرد:** File mode to set for the admin socket, e.g, '0755'

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`admin_socket`](../../../config/global/admin.md#SP_admin_socket)

**مثال:**

```bash
ceph config set global admin_socket_mode "example"
ceph config get global admin_socket_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global admin_socket_mode
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
