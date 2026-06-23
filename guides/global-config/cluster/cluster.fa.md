# Cluster

راهنمای عمیق پیکربندی Global — 3 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cluster_addr](#cluster_addr) | `(empty)` | Basic | Connectivity |
| [cluster_network](#cluster_network) | `(empty)` | Advanced | Performance |
| [cluster_network_interface](#cluster_network_interface) | `(empty)` | Advanced | Performance |

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

### cluster_addr

| | |
|---|---|
| نوع | Addr · default `(empty)` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [cluster.md#SP_cluster_addr](../../../config/global/cluster.md#SP_cluster_addr) |

**کارکرد:** Cluster-facing address to bind to

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global cluster_addr (empty)
ceph config get global cluster_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Connectivity

1. نقاط پایانی (endpoint) کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. پایدارترین نقطهٔ پایانی با کمترین تأخیر (latency) را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cluster_addr
ceph -s
```

---

### cluster_network

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [cluster.md#SP_cluster_network](../../../config/global/cluster.md#SP_cluster_network) |

**کارکرد:** Network(s) from which to choose a cluster address to bind to

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global cluster_network "example"
ceph config get global cluster_network
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cluster_network
ceph -s
```

---

### cluster_network_interface

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [cluster.md#SP_cluster_network_interface](../../../config/global/cluster.md#SP_cluster_network_interface) |

**کارکرد:** Interface name(s) from which to choose an address from a ``cluster_network`` to bind to; ``cluster_network`` must also be specified.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global cluster_network_interface "example"
ceph config get global cluster_network_interface
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global cluster_network_interface
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
