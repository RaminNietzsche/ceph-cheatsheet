# MGR-related settings

راهنمای عمیق پیکربندی MON — 6 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_mgr_beacon_grace](#mon_mgr_beacon_grace) | `30` | Advanced | عملکرد |
| [mon_mgr_blocklist_interval](#mon_mgr_blocklist_interval) | `1_day` | Dev | توسعه |
| [mon_mgr_digest_period](#mon_mgr_digest_period) | `5` | Dev | توسعه |
| [mon_mgr_inactive_grace](#mon_mgr_inactive_grace) | `1_min` | Advanced | عملکرد |
| [mon_mgr_mkfs_grace](#mon_mgr_mkfs_grace) | `2_min` | Advanced | عملکرد |
| [mon_mgr_proxy_client_bytes_ratio](#mon_mgr_proxy_client_bytes_ratio) | `0.3` | Dev | توسعه |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_mgr_beacon_grace

| | |
|---|---|
| نوع | Secs · default `30` · **Advanced** |
| جدول | [mon.md#SP_mon_mgr_beacon_grace](../../../config/mon/mon.md#SP_mon_mgr_beacon_grace) |

**کارکرد:** Period in seconds from last beacon to monitor marking a manager daemon as failed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_mgr_beacon_grace 30
ceph config get mon mon_mgr_beacon_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_mgr_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_blocklist_interval

| | |
|---|---|
| نوع | Float · default `1_day` · **Dev** |
| جدول | [mon.md#SP_mon_mgr_blocklist_interval](../../../config/mon/mon.md#SP_mon_mgr_blocklist_interval) |

**کارکرد:** Duration in seconds that blocklist entries for mgr daemons remain in the OSD map

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_mgr_blocklist_interval 1_day
ceph config get mon mon_mgr_blocklist_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_day`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_mgr_digest_period

| | |
|---|---|
| نوع | Int · default `5` · **Dev** |
| جدول | [mon.md#SP_mon_mgr_digest_period](../../../config/mon/mon.md#SP_mon_mgr_digest_period) |

**کارکرد:** Period in seconds between monitor-to-manager health/status updates

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_mgr_digest_period 5
ceph config get mon mon_mgr_digest_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_mgr_inactive_grace

| | |
|---|---|
| نوع | Int · default `1_min` · **Advanced** |
| جدول | [mon.md#SP_mon_mgr_inactive_grace](../../../config/mon/mon.md#SP_mon_mgr_inactive_grace) |

**کارکرد:** Period in seconds after cluster creation during which cluster may have no active manager

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_mgr_inactive_grace 1_min
ceph config get mon mon_mgr_inactive_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_mgr_inactive_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_mkfs_grace

| | |
|---|---|
| نوع | Int · default `2_min` · **Advanced** |
| جدول | [mon.md#SP_mon_mgr_mkfs_grace](../../../config/mon/mon.md#SP_mon_mgr_mkfs_grace) |

**کارکرد:** Period in seconds that the cluster may have no active manager before this is reported as an ERR rather than a WARN

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_mgr_mkfs_grace 2_min
ceph config get mon mon_mgr_mkfs_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_mgr_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_proxy_client_bytes_ratio

| | |
|---|---|
| نوع | Float · default `0.3` · **Dev** |
| جدول | [mon.md#SP_mon_mgr_proxy_client_bytes_ratio](../../../config/mon/mon.md#SP_mon_mgr_proxy_client_bytes_ratio) |

**کارکرد:** ratio of mon_client_bytes that can be consumed by proxied mgr commands before we error out to client

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_mgr_proxy_client_bytes_ratio 0.3
ceph config get mon mon_mgr_proxy_client_bytes_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.3`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
