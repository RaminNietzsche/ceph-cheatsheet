# Plugin

راهنمای عمیق پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [plugin_crypto_accelerator](#plugin_crypto_accelerator) | `crypto_isal` | Advanced | Performance |
| [plugin_dir](#plugin_dir) | `0` | Advanced | Capacity |

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

### plugin_crypto_accelerator

| | |
|---|---|
| نوع | Str · default `crypto_isal` · **Advanced** |
| جدول | [plugin.md#SP_plugin_crypto_accelerator](../../../config/global/plugin.md#SP_plugin_crypto_accelerator) |

**کارکرد:** Crypto accelerator library to use

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global plugin_crypto_accelerator crypto_isal
ceph config get global plugin_crypto_accelerator
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `crypto_isal`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global plugin_crypto_accelerator
ceph -s
```

---

### plugin_dir

| | |
|---|---|
| نوع | Str · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [plugin.md#SP_plugin_dir](../../../config/global/plugin.md#SP_plugin_dir) |

**کارکرد:** Base directory for dynamically loaded plugins

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global plugin_dir "/var/lib/ceph/example"
ceph config get global plugin_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `0`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global plugin_dir
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
