# Mirroring

راهنمای عمیق پیکربندی RBD — 4 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [rbd_mirroring_delete_delay](#rbd_mirroring_delete_delay) | `0` | Advanced | عملکرد |
| [rbd_mirroring_max_mirroring_snapshots](#rbd_mirroring_max_mirroring_snapshots) | `5` | Advanced | عملکرد |
| [rbd_mirroring_replay_delay](#rbd_mirroring_replay_delay) | `0` | Advanced | عملکرد |
| [rbd_mirroring_resync_after_disconnect](#rbd_mirroring_resync_after_disconnect) | `False` | Advanced | عملکرد |

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

### rbd_mirroring_delete_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_delete_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_delete_delay) |

**کارکرد:** time-delay in seconds for rbd-mirror delete propagation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirroring_delete_delay 64
ceph config get client rbd_mirroring_delete_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirroring_delete_delay
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_max_mirroring_snapshots

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_max_mirroring_snapshots](../../../config/rbd/rbd.md#SP_rbd_mirroring_max_mirroring_snapshots) |

**کارکرد:** mirroring snapshots limit

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set client rbd_mirroring_max_mirroring_snapshots 5
ceph config get client rbd_mirroring_max_mirroring_snapshots
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `3`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirroring_max_mirroring_snapshots
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_replay_delay

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_replay_delay](../../../config/rbd/rbd.md#SP_rbd_mirroring_replay_delay) |

**کارکرد:** time-delay in seconds for rbd-mirror asynchronous replication

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set client rbd_mirroring_replay_delay 64
ceph config get client rbd_mirroring_replay_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirroring_replay_delay
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---

### rbd_mirroring_resync_after_disconnect

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [rbd.md#SP_rbd_mirroring_resync_after_disconnect](../../../config/rbd/rbd.md#SP_rbd_mirroring_resync_after_disconnect) |

**کارکرد:** automatically start image resync after mirroring is disconnected due to being laggy

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set client rbd_mirroring_resync_after_disconnect true
ceph config get client rbd_mirroring_resync_after_disconnect
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get client rbd_mirroring_resync_after_disconnect
ceph -s
# گزینه‌های کلاینت: در بخش client یا ceph.conf تنظیم کنید
```

---


[← نمای کلی](../OVERVIEW.md)
