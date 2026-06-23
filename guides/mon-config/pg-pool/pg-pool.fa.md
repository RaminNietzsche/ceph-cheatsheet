# PG & pool health

deep dive پیکربندی MON — 14 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_allow_pool_size_one](#mon_allow_pool_size_one) | `False` | Advanced | Policy |
| [mon_clean_pg_upmaps_per_chunk](#mon_clean_pg_upmaps_per_chunk) | `256` | Dev | Dev |
| [mon_max_pool_pg_num](#mon_max_pool_pg_num) | `64_K` | Advanced | Performance |
| [mon_osd_prime_pg_temp](#mon_osd_prime_pg_temp) | `True` | Dev | Dev |
| [mon_osd_prime_pg_temp_max_estimate](#mon_osd_prime_pg_temp_max_estimate) | `0.25` | Advanced | Performance |
| [mon_osd_prime_pg_temp_max_time](#mon_osd_prime_pg_temp_max_time) | `0.5` | Dev | Dev |
| [mon_stretch_pool_min_size](#mon_stretch_pool_min_size) | `2` | Dev | Dev |
| [mon_stretch_pool_size](#mon_stretch_pool_size) | `4` | Dev | Dev |
| [mon_warn_on_cache_pools_without_hit_sets](#mon_warn_on_cache_pools_without_hit_sets) | `True` | Advanced | Performance |
| [mon_warn_on_pool_no_redundancy](#mon_warn_on_pool_no_redundancy) | `True` | Advanced | Performance |
| [mon_warn_on_pool_pg_num_not_power_of_two](#mon_warn_on_pool_pg_num_not_power_of_two) | `True` | Dev | Dev |
| [pool_availability_update_interval](#pool_availability_update_interval) | `1` | Advanced | Performance |
| [osd_pool_default_crimson](#osd_pool_default_crimson) | `False` | Advanced | Performance |
| [osd_pool_erasure_code_stripe_unit](#osd_pool_erasure_code_stripe_unit) | `0` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_allow_pool_size_one

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_allow_pool_size_one](../../../config/mon/mon.md#SP_mon_allow_pool_size_one) |

**کارکرد:** Allow pools with `size=1` (no redundancy).

**زمان استفاده:** Lab only. Keep `false` in production unless you accept data loss risk.

**مثال:**

```bash
ceph config set mon mon_allow_pool_size_one true
ceph config get mon mon_allow_pool_size_one
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_allow_pool_size_one
ceph -s
ceph mon stat
```

---

### mon_clean_pg_upmaps_per_chunk

| | |
|---|---|
| نوع | Uint · default `256` · **Dev** |
| جدول | [mon.md#SP_mon_clean_pg_upmaps_per_chunk](../../../config/mon/mon.md#SP_mon_clean_pg_upmaps_per_chunk) |

**کارکرد:** granularity of PG upmap validation background work

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_clean_pg_upmaps_per_chunk 256
ceph config get mon mon_clean_pg_upmaps_per_chunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`256`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_max_pool_pg_num

| | |
|---|---|
| نوع | Uint · default `64_K` · **Advanced** |
| جدول | [mon.md#SP_mon_max_pool_pg_num](../../../config/mon/mon.md#SP_mon_max_pool_pg_num) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_pool_pg_num 64_K
ceph config get mon mon_max_pool_pg_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_pool_pg_num
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mon.md#SP_mon_osd_prime_pg_temp](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp) |

**کارکرد:** minimize peering work by priming pg_temp values after a map change

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_osd_prime_pg_temp false
ceph config get mon mon_osd_prime_pg_temp
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_osd_prime_pg_temp_max_estimate

| | |
|---|---|
| نوع | Float · default `0.25` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_prime_pg_temp_max_estimate](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_estimate) |

**کارکرد:** calculate all PG mappings if estimated fraction of PGs that change is above this amount

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_estimate 0.25
ceph config get mon mon_osd_prime_pg_temp_max_estimate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.25`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_prime_pg_temp_max_estimate
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp_max_time

| | |
|---|---|
| نوع | Float · default `0.5` · **Dev** |
| جدول | [mon.md#SP_mon_osd_prime_pg_temp_max_time](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_time) |

**کارکرد:** maximum time to spend precalculating PG mappings on map change (seconds)

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_time 0.5
ceph config get mon mon_osd_prime_pg_temp_max_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0.5`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_stretch_pool_min_size

| | |
|---|---|
| نوع | Uint · default `2` · **Dev** |
| جدول | [mon.md#SP_mon_stretch_pool_min_size](../../../config/mon/mon.md#SP_mon_stretch_pool_min_size) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_stretch_pool_min_size 2
ceph config get mon mon_stretch_pool_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`2`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_stretch_pool_size

| | |
|---|---|
| نوع | Uint · default `4` · **Dev** |
| جدول | [mon.md#SP_mon_stretch_pool_size](../../../config/mon/mon.md#SP_mon_stretch_pool_size) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_stretch_pool_size 4
ceph config get mon mon_stretch_pool_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`4`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_warn_on_cache_pools_without_hit_sets

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_cache_pools_without_hit_sets](../../../config/mon/mon.md#SP_mon_warn_on_cache_pools_without_hit_sets) |

**کارکرد:** issue CACHE_POOL_NO_HIT_SET health warning for cache pools that do not have hit sets configured

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_cache_pools_without_hit_sets false
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_redundancy

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_pool_no_redundancy](../../../config/mon/mon.md#SP_mon_warn_on_pool_no_redundancy) |

**کارکرد:** Warn when any pool has no redundancy (`size=1` or `min_size=1`).

**زمان استفاده:** Leave enabled in production.

**مثال:**

```bash
ceph config set mon mon_warn_on_pool_no_redundancy false
ceph config get mon mon_warn_on_pool_no_redundancy
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_pool_no_redundancy
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_pg_num_not_power_of_two

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two](../../../config/mon/mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two) |

**کارکرد:** issue POOL_PG_NUM_NOT_POWER_OF_TWO warning if pool has a non-power-of-two pg_num value

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_warn_on_pool_pg_num_not_power_of_two false
ceph config get mon mon_warn_on_pool_pg_num_not_power_of_two
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### pool_availability_update_interval

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mon.md#SP_pool_availability_update_interval](../../../config/mon/mon.md#SP_pool_availability_update_interval) |

**کارکرد:** Update data availability score at this interval. By default the interval is same as paxos_propose_interval configuration.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon pool_availability_update_interval 1
ceph config get mon pool_availability_update_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon pool_availability_update_interval
ceph -s
ceph mon stat
```

---

### osd_pool_default_crimson

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_default_crimson](../../../config/mon/osd.md#SP_osd_pool_default_crimson) |

**کارکرد:** Create pools by default with FLAG_CRIMSON

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set osd osd_pool_default_crimson true
ceph config get osd osd_pool_default_crimson
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_pool_default_crimson
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_erasure_code_stripe_unit

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [osd.md#SP_osd_pool_erasure_code_stripe_unit](../../../config/mon/osd.md#SP_osd_pool_erasure_code_stripe_unit) |

**کارکرد:** the amount of data (in bytes) in a data chunk, per stripe

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set osd osd_pool_erasure_code_stripe_unit 64
ceph config get osd osd_pool_erasure_code_stripe_unit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get osd osd_pool_erasure_code_stripe_unit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← نمای کلی](../OVERVIEW.md)
