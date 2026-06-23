# General manager

راهنمای عمیق پیکربندی MGR — 8 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_cache_target_full_warn_ratio](#mon_cache_target_full_warn_ratio) | `0.66` | Advanced | Performance |
| [mon_osd_err_op_age_ratio](#mon_osd_err_op_age_ratio) | `128` | Advanced | Performance |
| [mon_reweight_max_change](#mon_reweight_max_change) | `0.05` | Advanced | Performance |
| [mon_reweight_max_osds](#mon_reweight_max_osds) | `4` | Advanced | Performance |
| [mon_reweight_min_bytes_per_osd](#mon_reweight_min_bytes_per_osd) | `100_M` | Advanced | Performance |
| [mon_reweight_min_pgs_per_osd](#mon_reweight_min_pgs_per_osd) | `10` | Advanced | Performance |
| [mon_warn_on_misplaced](#mon_warn_on_misplaced) | `False` | Advanced | Performance |
| [mon_warn_on_too_few_osds](#mon_warn_on_too_few_osds) | `True` | Advanced | Performance |

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

### mon_cache_target_full_warn_ratio

| | |
|---|---|
| نوع | Float · default `0.66` · **Advanced** |
| جدول | [mon.md#SP_mon_cache_target_full_warn_ratio](../../../config/mgr/mon.md#SP_mon_cache_target_full_warn_ratio) |

**کارکرد:** issue CACHE_POOL_NEAR_FULL health warning when cache pool utilization exceeds this ratio of usable space

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_cache_target_full_warn_ratio 0.66
ceph config get mon mon_cache_target_full_warn_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.66`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_cache_target_full_warn_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_err_op_age_ratio

| | |
|---|---|
| نوع | Float · default `128` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_err_op_age_ratio](../../../config/mgr/mon.md#SP_mon_osd_err_op_age_ratio) |

**کارکرد:** issue REQUEST_STUCK health error if OSD ops are slower than is age (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_osd_err_op_age_ratio 128
ceph config get mon mon_osd_err_op_age_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_osd_err_op_age_ratio
ceph -s
ceph mon stat
```

---

### mon_reweight_max_change

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [mon.md#SP_mon_reweight_max_change](../../../config/mgr/mon.md#SP_mon_reweight_max_change) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_reweight_max_change 0.05
ceph config get mon mon_reweight_max_change
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_reweight_max_change
ceph -s
ceph mon stat
```

---

### mon_reweight_max_osds

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [mon.md#SP_mon_reweight_max_osds](../../../config/mgr/mon.md#SP_mon_reweight_max_osds) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_reweight_max_osds 4
ceph config get mon mon_reweight_max_osds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_reweight_max_osds
ceph -s
ceph mon stat
```

---

### mon_reweight_min_bytes_per_osd

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [mon.md#SP_mon_reweight_min_bytes_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_bytes_per_osd) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_reweight_min_bytes_per_osd 100_M
ceph config get mon mon_reweight_min_bytes_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_reweight_min_bytes_per_osd
ceph -s
ceph mon stat
```

---

### mon_reweight_min_pgs_per_osd

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_reweight_min_pgs_per_osd](../../../config/mgr/mon.md#SP_mon_reweight_min_pgs_per_osd) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_reweight_min_pgs_per_osd 10
ceph config get mon mon_reweight_min_pgs_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_reweight_min_pgs_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_misplaced

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_misplaced](../../../config/mgr/mon.md#SP_mon_warn_on_misplaced) |

**کارکرد:** Issue a health warning if there are misplaced objects

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_misplaced true
ceph config get mon mon_warn_on_misplaced
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_misplaced
ceph -s
ceph mon stat
```

---

### mon_warn_on_too_few_osds

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_too_few_osds](../../../config/mgr/mon.md#SP_mon_warn_on_too_few_osds) |

**کارکرد:** Issue a health warning if there are fewer OSDs than osd_pool_default_size

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_too_few_osds false
ceph config get mon mon_warn_on_too_few_osds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_too_few_osds
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
