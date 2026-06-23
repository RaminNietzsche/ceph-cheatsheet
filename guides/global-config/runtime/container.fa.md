# Container

deep dive پیکربندی Global — 1 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [container_image](#container_image) | `docker.io/ceph/daemon-base:latest-master-devel` | Basic | Policy |

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

### container_image

| | |
|---|---|
| نوع | Str · default `docker.io/ceph/daemon-base:latest-master-devel` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [container.md#SP_container_image](../../../config/global/container.md#SP_container_image) |

**کارکرد:** Container image for core daemons, used by the cephadm orchestrator

**زمان استفاده:** رفتار اصلی Global — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set global container_image "docker.io/ceph/daemon-base:latest-master-devel"
ceph config get global container_image
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `docker.io/ceph/daemon-base:latest-master-devel` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global container_image
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
