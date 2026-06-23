# PG & pool settings

راهنمای عمیق پیکربندی MGR — 11 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_pg_check_down_all_threshold](#mon_pg_check_down_all_threshold) | `0.5` | Advanced | Performance |
| [mon_pg_stuck_threshold](#mon_pg_stuck_threshold) | `1_min` | Advanced | Performance |
| [mon_pg_warn_max_object_skew](#mon_pg_warn_max_object_skew) | `10` | Advanced | Performance |
| [mon_pg_warn_min_objects](#mon_pg_warn_min_objects) | `10000` | Advanced | Performance |
| [mon_pg_warn_min_per_osd](#mon_pg_warn_min_per_osd) | `0` | Advanced | Performance |
| [mon_pg_warn_min_pool_objects](#mon_pg_warn_min_pool_objects) | `1000` | Advanced | Performance |
| [mon_pool_quota_crit_threshold](#mon_pool_quota_crit_threshold) | `0` | Advanced | Performance |
| [mon_pool_quota_warn_threshold](#mon_pool_quota_warn_threshold) | `0` | Advanced | Performance |
| [mon_target_pg_per_osd](#mon_target_pg_per_osd) | `200` | Advanced | Performance |
| [mon_warn_on_pool_no_app](#mon_warn_on_pool_no_app) | `True` | Dev | Dev |
| [mon_warn_on_pool_no_app_grace](#mon_warn_on_pool_no_app_grace) | `5_min` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_pg_check_down_all_threshold

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_check_down_all_threshold](../../../config/mgr/mon.md#SP_mon_pg_check_down_all_threshold) |

**کارکرد:** threshold of down osds after which we check all pgs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_pg_check_down_all_threshold 0.5
ceph config get mon mon_pg_check_down_all_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_check_down_all_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_stuck_threshold

| | |
|---|---|
| نوع | Int · default `1_min` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_stuck_threshold](../../../config/mgr/mon.md#SP_mon_pg_stuck_threshold) |

**کارکرد:** number of seconds after which pgs can be considered stuck inactive, unclean, etc

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_pg_stuck_threshold 1_min
ceph config get mon mon_pg_stuck_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_stuck_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_warn_max_object_skew

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_warn_max_object_skew](../../../config/mgr/mon.md#SP_mon_pg_warn_max_object_skew) |

**کارکرد:** max skew few average in objects per pg

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_pg_warn_max_object_skew 10
ceph config get mon mon_pg_warn_max_object_skew
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_warn_max_object_skew
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_objects

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_warn_min_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_objects) |

**کارکرد:** do not warn below this object #

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_pg_warn_min_objects 10000
ceph config get mon mon_pg_warn_min_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_warn_min_objects
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_per_osd

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_warn_min_per_osd](../../../config/mgr/mon.md#SP_mon_pg_warn_min_per_osd) |

**کارکرد:** minimal number PGs per (in) osd before we warn the admin

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_pg_warn_min_per_osd 64
ceph config get mon mon_pg_warn_min_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_warn_min_per_osd
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_pool_objects

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [mon.md#SP_mon_pg_warn_min_pool_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_pool_objects) |

**کارکرد:** do not warn on pools below this object #

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_pg_warn_min_pool_objects 1000
ceph config get mon mon_pg_warn_min_pool_objects
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pg_warn_min_pool_objects
ceph -s
ceph mon stat
```

---

### mon_pool_quota_crit_threshold

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_pool_quota_crit_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_crit_threshold) |

**کارکرد:** percent of quota at which to issue errors

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_pool_quota_crit_threshold 64
ceph config get mon mon_pool_quota_crit_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pool_quota_crit_threshold
ceph -s
ceph mon stat
```

---

### mon_pool_quota_warn_threshold

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_pool_quota_warn_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_warn_threshold) |

**کارکرد:** percent of quota at which to issue warnings

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_pool_quota_warn_threshold 64
ceph config get mon mon_pool_quota_warn_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_pool_quota_warn_threshold
ceph -s
ceph mon stat
```

---

### mon_target_pg_per_osd

| | |
|---|---|
| نوع | Uint · default `200` · **Advanced** |
| جدول | [mon.md#SP_mon_target_pg_per_osd](../../../config/mgr/mon.md#SP_mon_target_pg_per_osd) |

**کارکرد:** Target PGs per OSD for autoscaler and PG health warnings (also listed under MON cross-daemon settings in mgr config tables).

**زمان استفاده:** Adjust when autoscaler consistently over/under-shards pools for your OSD count.

**مثال:**

```bash
ceph config set mon mon_target_pg_per_osd 200
ceph config get mon mon_target_pg_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_target_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_app

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mon.md#SP_mon_warn_on_pool_no_app](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app) |

**کارکرد:** issue POOL_APP_NOT_ENABLED health warning if pool has not application enabled

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_warn_on_pool_no_app false
ceph config get mon mon_warn_on_pool_no_app
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_warn_on_pool_no_app_grace

| | |
|---|---|
| نوع | Secs · default `5_min` · **Dev** |
| جدول | [mon.md#SP_mon_warn_on_pool_no_app_grace](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app_grace) |

**کارکرد:** time after which POOL_APP_NOT_ENABLED health warning is issued

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_warn_on_pool_no_app_grace 5_min
ceph config get mon mon_warn_on_pool_no_app_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`5_min`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
