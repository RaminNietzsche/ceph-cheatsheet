# General monitor

راهنمای عمیق پیکربندی MON — 44 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [enable_availability_tracking](#enable_availability_tracking) | `False` | Advanced | سیاست |
| [mon_clock_drift_allowed](#mon_clock_drift_allowed) | `0.05` | Advanced | عملکرد |
| [mon_clock_drift_warn_backoff](#mon_clock_drift_warn_backoff) | `5` | Advanced | عملکرد |
| [mon_compact_on_bootstrap](#mon_compact_on_bootstrap) | `False` | Advanced | عملکرد |
| [mon_compact_on_start](#mon_compact_on_start) | `False` | Advanced | عملکرد |
| [mon_compact_on_trim](#mon_compact_on_trim) | `True` | Advanced | عملکرد |
| [mon_con_tracker_score_halflife](#mon_con_tracker_score_halflife) | `43200` | Advanced | عملکرد |
| [mon_cpu_threads](#mon_cpu_threads) | `4` | Advanced | عملکرد |
| [mon_crush_min_required_version](#mon_crush_min_required_version) | `hammer` | Advanced | عملکرد |
| [mon_daemon_bytes](#mon_daemon_bytes) | `400_M` | Advanced | عملکرد |
| [mon_down_added_grace](#mon_down_added_grace) | `3_min` | Advanced | عملکرد |
| [mon_down_mkfs_grace](#mon_down_mkfs_grace) | `1_min` | Advanced | عملکرد |
| [mon_down_uptime_grace](#mon_down_uptime_grace) | `1_min` | Advanced | عملکرد |
| [mon_elector_ignore_propose_margin](#mon_elector_ignore_propose_margin) | `0.0005` | Advanced | عملکرد |
| [mon_elector_ping_divisor](#mon_elector_ping_divisor) | `2` | Advanced | عملکرد |
| [mon_enable_op_tracker](#mon_enable_op_tracker) | `True` | Advanced | سیاست |
| [mon_fsmap_prune_threshold](#mon_fsmap_prune_threshold) | `300` | Advanced | عملکرد |
| [mon_health_max_detail](#mon_health_max_detail) | `50` | Advanced | عملکرد |
| [mon_lease](#mon_lease) | `5` | Advanced | عملکرد |
| [mon_mds_force_trim_to](#mon_mds_force_trim_to) | `0` | Dev | توسعه |
| [mon_mds_skip_sanity](#mon_mds_skip_sanity) | `False` | Advanced | عملکرد |
| [mon_memory_autotune](#mon_memory_autotune) | `True` | Basic | سیاست |
| [mon_memory_target](#mon_memory_target) | `2_G` | Basic | سیاست |
| [mon_nvmeofgw_beacon_grace](#mon_nvmeofgw_beacon_grace) | `7` | Advanced | عملکرد |
| [mon_nvmeofgw_beacons_till_ack](#mon_nvmeofgw_beacons_till_ack) | `15` | Advanced | عملکرد |
| [mon_nvmeofgw_delete_grace](#mon_nvmeofgw_delete_grace) | `15_min` | Advanced | عملکرد |
| [mon_nvmeofgw_set_group_id_retry](#mon_nvmeofgw_set_group_id_retry) | `1000` | Advanced | عملکرد |
| [mon_nvmeofgw_wrong_map_ignore_sec](#mon_nvmeofgw_wrong_map_ignore_sec) | `15` | Advanced | عملکرد |
| [mon_op_complaint_time](#mon_op_complaint_time) | `30` | Advanced | عملکرد |
| [mon_op_history_duration](#mon_op_history_duration) | `10_min` | Advanced | عملکرد |
| [mon_op_history_size](#mon_op_history_size) | `20` | Advanced | عملکرد |
| [mon_op_history_slow_op_size](#mon_op_history_slow_op_size) | `20` | Advanced | عملکرد |
| [mon_op_history_slow_op_threshold](#mon_op_history_slow_op_threshold) | `10` | Advanced | عملکرد |
| [mon_rocksdb_options](#mon_rocksdb_options) | `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` | Advanced | عملکرد |
| [mon_stretch_cluster_recovery_ratio](#mon_stretch_cluster_recovery_ratio) | `0.6` | Advanced | عملکرد |
| [mon_stretch_max_bucket_weight_delta](#mon_stretch_max_bucket_weight_delta) | `0.1` | Dev | توسعه |
| [mon_stretch_recovery_min_wait](#mon_stretch_recovery_min_wait) | `15` | Advanced | عملکرد |
| [mon_warn_on_colocated_monitors](#mon_warn_on_colocated_monitors) | `False` | Advanced | عملکرد |
| [mon_warn_on_crush_straw_calc_version_zero](#mon_warn_on_crush_straw_calc_version_zero) | `True` | Advanced | عملکرد |
| [mon_warn_on_degraded_stretch_mode](#mon_warn_on_degraded_stretch_mode) | `True` | Advanced | عملکرد |
| [mon_warn_on_legacy_crush_tunables](#mon_warn_on_legacy_crush_tunables) | `True` | Advanced | عملکرد |
| [mon_warn_on_older_version](#mon_warn_on_older_version) | `True` | Advanced | عملکرد |
| [nvmeof_mon_client_connect_panic](#nvmeof_mon_client_connect_panic) | `30` | Advanced | عملکرد |
| [nvmeof_mon_client_disconnect_panic](#nvmeof_mon_client_disconnect_panic) | `100` | Advanced | عملکرد |

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

### enable_availability_tracking

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_enable_availability_tracking](../../../config/mon/mon.md#SP_enable_availability_tracking) |

**کارکرد:** Calculate and store availablity score for each pool in the cluster at regular intervals

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon enable_availability_tracking true
ceph config get mon enable_availability_tracking
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon enable_availability_tracking
ceph -s
ceph mon stat
```

---

### mon_clock_drift_allowed

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [mon.md#SP_mon_clock_drift_allowed](../../../config/mon/mon.md#SP_mon_clock_drift_allowed) |

**کارکرد:** Maximum clock drift (seconds) between monitors before health warnings.

**زمان استفاده:** Ensure NTP/chrony is stable first. Increase only as a temporary mitigation while fixing time sync.

**مثال:**

```bash
ceph config set mon mon_clock_drift_allowed 0.05
ceph config get mon mon_clock_drift_allowed
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_clock_drift_allowed
ceph -s
ceph mon stat
```

---

### mon_clock_drift_warn_backoff

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_clock_drift_warn_backoff](../../../config/mon/mon.md#SP_mon_clock_drift_warn_backoff) |

**کارکرد:** exponential backoff factor for logging clock drift warnings in the cluster log

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_clock_drift_warn_backoff 5
ceph config get mon mon_clock_drift_warn_backoff
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_clock_drift_warn_backoff
ceph -s
ceph mon stat
```

---

### mon_compact_on_bootstrap

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_compact_on_bootstrap](../../../config/mon/mon.md#SP_mon_compact_on_bootstrap) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_compact_on_bootstrap true
ceph config get mon mon_compact_on_bootstrap
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_compact_on_bootstrap
ceph -s
ceph mon stat
```

---

### mon_compact_on_start

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_compact_on_start](../../../config/mon/mon.md#SP_mon_compact_on_start) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_compact_on_start true
ceph config get mon mon_compact_on_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_compact_on_start
ceph -s
ceph mon stat
```

---

### mon_compact_on_trim

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_compact_on_trim](../../../config/mon/mon.md#SP_mon_compact_on_trim) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_compact_on_trim false
ceph config get mon mon_compact_on_trim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_compact_on_trim
ceph -s
ceph mon stat
```

---

### mon_con_tracker_score_halflife

| | |
|---|---|
| نوع | Uint · default `43200` · **Advanced** |
| جدول | [mon.md#SP_mon_con_tracker_score_halflife](../../../config/mon/mon.md#SP_mon_con_tracker_score_halflife) |

**کارکرد:** The 'halflife' used when updating/calculating peer connection scores

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_con_tracker_score_halflife 43200
ceph config get mon mon_con_tracker_score_halflife
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `43200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `60`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_con_tracker_score_halflife
ceph -s
ceph mon stat
```

---

### mon_cpu_threads

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [mon.md#SP_mon_cpu_threads](../../../config/mon/mon.md#SP_mon_cpu_threads) |

**کارکرد:** worker threads for CPU intensive background work

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_cpu_threads 4
ceph config get mon mon_cpu_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_cpu_threads
ceph -s
ceph mon stat
```

---

### mon_crush_min_required_version

| | |
|---|---|
| نوع | Str · default `hammer` · **Advanced** |
| جدول | [mon.md#SP_mon_crush_min_required_version](../../../config/mon/mon.md#SP_mon_crush_min_required_version) |

**کارکرد:** minimum ceph release to use for mon_warn_on_legacy_crush_tunables

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`mon_warn_on_legacy_crush_tunables`](../../../config/mon/mon.md#SP_mon_warn_on_legacy_crush_tunables)

**مثال:**

```bash
ceph config set mon mon_crush_min_required_version hammer
ceph config get mon mon_crush_min_required_version
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `hammer`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_crush_min_required_version
ceph -s
ceph mon stat
```

---

### mon_daemon_bytes

| | |
|---|---|
| نوع | Size · default `400_M` · **Advanced** |
| جدول | [mon.md#SP_mon_daemon_bytes](../../../config/mon/mon.md#SP_mon_daemon_bytes) |

**کارکرد:** max bytes of outstanding mon messages mon will read off the network

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_daemon_bytes 400_M
ceph config get mon mon_daemon_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `400_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_daemon_bytes
ceph -s
ceph mon stat
```

---

### mon_down_added_grace

| | |
|---|---|
| نوع | Secs · default `3_min` · **Advanced** |
| جدول | [mon.md#SP_mon_down_added_grace](../../../config/mon/mon.md#SP_mon_down_added_grace) |

**کارکرد:** Period in seconds that the cluster may have a newly added mon down

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_down_added_grace 3_min
ceph config get mon mon_down_added_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_down_added_grace
ceph -s
ceph mon stat
```

---

### mon_down_mkfs_grace

| | |
|---|---|
| نوع | Secs · default `1_min` · **Advanced** |
| جدول | [mon.md#SP_mon_down_mkfs_grace](../../../config/mon/mon.md#SP_mon_down_mkfs_grace) |

**کارکرد:** Period in seconds that the cluster may have a mon down after cluster creation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_down_mkfs_grace 1_min
ceph config get mon mon_down_mkfs_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_down_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_down_uptime_grace

| | |
|---|---|
| نوع | Secs · default `1_min` · **Advanced** |
| جدول | [mon.md#SP_mon_down_uptime_grace](../../../config/mon/mon.md#SP_mon_down_uptime_grace) |

**کارکرد:** Period in seconds that the cluster may have a mon down after this (leader) monitor comes up.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_down_uptime_grace 1_min
ceph config get mon mon_down_uptime_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_down_uptime_grace
ceph -s
ceph mon stat
```

---

### mon_elector_ignore_propose_margin

| | |
|---|---|
| نوع | Float · default `0.0005` · **Advanced** |
| جدول | [mon.md#SP_mon_elector_ignore_propose_margin](../../../config/mon/mon.md#SP_mon_elector_ignore_propose_margin) |

**کارکرد:** The difference in connection score allowed before a peon stops ignoring out-of-quorum PROPOSEs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_elector_ignore_propose_margin 0.0005
ceph config get mon mon_elector_ignore_propose_margin
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.0005`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_elector_ignore_propose_margin
ceph -s
ceph mon stat
```

---

### mon_elector_ping_divisor

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_elector_ping_divisor](../../../config/mon/mon.md#SP_mon_elector_ping_divisor) |

**کارکرد:** We will send a ping up to this many times per timeout per

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`mon_elector_ping_timeout`](../../../config/mon/mon.md#SP_mon_elector_ping_timeout)

**مثال:**

```bash
ceph config set mon mon_elector_ping_divisor 2
ceph config get mon mon_elector_ping_divisor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_elector_ping_divisor
ceph -s
ceph mon stat
```

---

### mon_enable_op_tracker

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_enable_op_tracker](../../../config/mon/mon.md#SP_mon_enable_op_tracker) |

**کارکرد:** enable/disable MON op tracking

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_enable_op_tracker false
ceph config get mon mon_enable_op_tracker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_enable_op_tracker
ceph -s
ceph mon stat
```

---

### mon_fsmap_prune_threshold

| | |
|---|---|
| نوع | Secs · default `300` · **Advanced** |
| جدول | [mon.md#SP_mon_fsmap_prune_threshold](../../../config/mon/mon.md#SP_mon_fsmap_prune_threshold) |

**کارکرد:** prune fsmap older than this threshold in seconds

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_fsmap_prune_threshold 300
ceph config get mon mon_fsmap_prune_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `300`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_fsmap_prune_threshold
ceph -s
ceph mon stat
```

---

### mon_health_max_detail

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [mon.md#SP_mon_health_max_detail](../../../config/mon/mon.md#SP_mon_health_max_detail) |

**کارکرد:** max detailed pgs to report in health detail

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_health_max_detail 50
ceph config get mon mon_health_max_detail
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_health_max_detail
ceph -s
ceph mon stat
```

---

### mon_lease

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_lease](../../../config/mon/mon.md#SP_mon_lease) |

**کارکرد:** lease interval between quorum monitors (seconds) This setting controls how sensitive your mon quorum is to intermittent network issues or other failures.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_lease 5
ceph config get mon mon_lease
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_lease
ceph -s
ceph mon stat
```

---

### mon_mds_force_trim_to

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_mds_force_trim_to](../../../config/mon/mon.md#SP_mon_mds_force_trim_to) |

**کارکرد:** force mons to trim mdsmaps/fsmaps up to this epoch

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_mds_force_trim_to 64
ceph config get mon mon_mds_force_trim_to
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_mds_skip_sanity

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_mds_skip_sanity](../../../config/mon/mon.md#SP_mon_mds_skip_sanity) |

**کارکرد:** skip sanity checks on fsmap/mdsmap

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_mds_skip_sanity true
ceph config get mon mon_mds_skip_sanity
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_mds_skip_sanity
ceph -s
ceph mon stat
```

---

### mon_memory_autotune

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [mon.md#SP_mon_memory_autotune](../../../config/mon/mon.md#SP_mon_memory_autotune) |

**کارکرد:** Autotune the cache memory being used for osd monitors and kv database

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_memory_autotune false
ceph config get mon mon_memory_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_memory_autotune
ceph -s
ceph mon stat
```

---

### mon_memory_target

| | |
|---|---|
| نوع | Size · default `2_G` · **Basic** |
| جدول | [mon.md#SP_mon_memory_target](../../../config/mon/mon.md#SP_mon_memory_target) |

**کارکرد:** The amount of bytes pertaining to osd monitor caches and kv cache to be kept mapped in memory with cache auto-tuning enabled

**زمان استفاده:** رفتار اصلی MON — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set mon mon_memory_target 2_G
ceph config get mon mon_memory_target
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `2_G` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_memory_target
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacon_grace

| | |
|---|---|
| نوع | Secs · default `7` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_beacon_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacon_grace) |

**کارکرد:** Period in seconds from last beacon to monitor marking a NVMeoF gateway as failed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_beacon_grace 7
ceph config get mon mon_nvmeofgw_beacon_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `7`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_nvmeofgw_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_beacons_till_ack

| | |
|---|---|
| نوع | Uint · default `15` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_beacons_till_ack](../../../config/mon/mon.md#SP_mon_nvmeofgw_beacons_till_ack) |

**کارکرد:** Number of beacons from MonClient before NVMeofGwMon sends ack-map to it

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_beacons_till_ack 15
ceph config get mon mon_nvmeofgw_beacons_till_ack
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_nvmeofgw_beacons_till_ack
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_delete_grace

| | |
|---|---|
| نوع | Secs · default `15_min` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_delete_grace](../../../config/mon/mon.md#SP_mon_nvmeofgw_delete_grace) |

**کارکرد:** Issue NVMEOF_GATEWAY_DELETING health warning after this amount of time has elapsed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_delete_grace 15_min
ceph config get mon mon_nvmeofgw_delete_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_nvmeofgw_delete_grace
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_set_group_id_retry

| | |
|---|---|
| نوع | Uint · default `1000` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_set_group_id_retry](../../../config/mon/mon.md#SP_mon_nvmeofgw_set_group_id_retry) |

**کارکرد:** Retry wait time in microsecond for set group id between the monitor client and gateway The monitor server determines the gateway's group ID. If the monitor client receives a monitor group ID assignment before the gateway is fully up during initialization, a retry is required.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_set_group_id_retry 1000
ceph config get mon mon_nvmeofgw_set_group_id_retry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_nvmeofgw_set_group_id_retry
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_wrong_map_ignore_sec

| | |
|---|---|
| نوع | Uint · default `15` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec](../../../config/mon/mon.md#SP_mon_nvmeofgw_wrong_map_ignore_sec) |

**کارکرد:** Period in seconds from MonClient startup to ignore wrong maps from Monitor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_wrong_map_ignore_sec 15
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_nvmeofgw_wrong_map_ignore_sec
ceph -s
ceph mon stat
```

---

### mon_op_complaint_time

| | |
|---|---|
| نوع | Secs · default `30` · **Advanced** |
| جدول | [mon.md#SP_mon_op_complaint_time](../../../config/mon/mon.md#SP_mon_op_complaint_time) |

**کارکرد:** time after which to consider a monitor operation blocked after no updates

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_op_complaint_time 30
ceph config get mon mon_op_complaint_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_op_complaint_time
ceph -s
ceph mon stat
```

---

### mon_op_history_duration

| | |
|---|---|
| نوع | Secs · default `10_min` · **Advanced** |
| جدول | [mon.md#SP_mon_op_history_duration](../../../config/mon/mon.md#SP_mon_op_history_duration) |

**کارکرد:** expiration time in seconds of historical MON OPS

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_op_history_duration 10_min
ceph config get mon mon_op_history_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_op_history_duration
ceph -s
ceph mon stat
```

---

### mon_op_history_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mon.md#SP_mon_op_history_size](../../../config/mon/mon.md#SP_mon_op_history_size) |

**کارکرد:** max number of completed ops to track

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_op_history_size 20
ceph config get mon mon_op_history_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_op_history_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mon.md#SP_mon_op_history_slow_op_size](../../../config/mon/mon.md#SP_mon_op_history_slow_op_size) |

**کارکرد:** max number of slow historical MON OPS to keep

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_op_history_slow_op_size 20
ceph config get mon mon_op_history_slow_op_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_op_history_slow_op_size
ceph -s
ceph mon stat
```

---

### mon_op_history_slow_op_threshold

| | |
|---|---|
| نوع | Secs · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_op_history_slow_op_threshold](../../../config/mon/mon.md#SP_mon_op_history_slow_op_threshold) |

**کارکرد:** duration of an op to be considered as a historical slow op

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_op_history_slow_op_threshold 10
ceph config get mon mon_op_history_slow_op_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_op_history_slow_op_threshold
ceph -s
ceph mon stat
```

---

### mon_rocksdb_options

| | |
|---|---|
| نوع | Str · default `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true` · **Advanced** |
| جدول | [mon.md#SP_mon_rocksdb_options](../../../config/mon/mon.md#SP_mon_rocksdb_options) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_rocksdb_options "write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true"
ceph config get mon mon_rocksdb_options
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `write_buffer_size=33554432,compression=kNoCompression,level_compaction_dynamic_level_bytes=true`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_rocksdb_options
ceph -s
ceph mon stat
```

---

### mon_stretch_cluster_recovery_ratio

| | |
|---|---|
| نوع | Float · default `0.6` · **Advanced** |
| جدول | [mon.md#SP_mon_stretch_cluster_recovery_ratio](../../../config/mon/mon.md#SP_mon_stretch_cluster_recovery_ratio) |

**کارکرد:** the ratio of up OSDs at which a degraded stretch cluster enters recovery

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon mon_stretch_cluster_recovery_ratio 0.6
ceph config get mon mon_stretch_cluster_recovery_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0.51`، حداکثر `1`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_stretch_cluster_recovery_ratio
ceph -s
ceph mon stat
```

---

### mon_stretch_max_bucket_weight_delta

| | |
|---|---|
| نوع | Float · default `0.1` · **Dev** |
| جدول | [mon.md#SP_mon_stretch_max_bucket_weight_delta](../../../config/mon/mon.md#SP_mon_stretch_max_bucket_weight_delta) |

**کارکرد:** Max difference allowed among CRUSH bucket weights when in stretch mode. The value is a percentage expressed as a real number between 0.0 and 1.0.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mon mon_stretch_max_bucket_weight_delta 0.1
ceph config get mon mon_stretch_max_bucket_weight_delta
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mon_stretch_recovery_min_wait

| | |
|---|---|
| نوع | Float · default `15` · **Advanced** |
| جدول | [mon.md#SP_mon_stretch_recovery_min_wait](../../../config/mon/mon.md#SP_mon_stretch_recovery_min_wait) |

**کارکرد:** how long the monitors wait before considering fully-healthy PGs as evidence the stretch mode is repaired

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_stretch_recovery_min_wait 15
ceph config get mon mon_stretch_recovery_min_wait
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_stretch_recovery_min_wait
ceph -s
ceph mon stat
```

---

### mon_warn_on_colocated_monitors

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_colocated_monitors](../../../config/mon/mon.md#SP_mon_warn_on_colocated_monitors) |

**کارکرد:** Issue MON_COLOCATED health warning if two or more Monitors have the same IP address

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_colocated_monitors true
ceph config get mon mon_warn_on_colocated_monitors
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_colocated_monitors
ceph -s
ceph mon stat
```

---

### mon_warn_on_crush_straw_calc_version_zero

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_crush_straw_calc_version_zero](../../../config/mon/mon.md#SP_mon_warn_on_crush_straw_calc_version_zero) |

**کارکرد:** issue OLD_CRUSH_STRAW_CALC_VERSION health warning if the CRUSH map's straw_calc_version is zero

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_crush_straw_calc_version_zero false
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_crush_straw_calc_version_zero
ceph -s
ceph mon stat
```

---

### mon_warn_on_degraded_stretch_mode

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_degraded_stretch_mode](../../../config/mon/mon.md#SP_mon_warn_on_degraded_stretch_mode) |

**کارکرد:** Issue a health warning if we are in degraded stretch mode

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_degraded_stretch_mode false
ceph config get mon mon_warn_on_degraded_stretch_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_degraded_stretch_mode
ceph -s
ceph mon stat
```

---

### mon_warn_on_legacy_crush_tunables

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_legacy_crush_tunables](../../../config/mon/mon.md#SP_mon_warn_on_legacy_crush_tunables) |

**کارکرد:** issue OLD_CRUSH_TUNABLES health warning if CRUSH tunables are older than mon_crush_min_required_version

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`mon_crush_min_required_version`](../../../config/mon/mon.md#SP_mon_crush_min_required_version)

**مثال:**

```bash
ceph config set mon mon_warn_on_legacy_crush_tunables false
ceph config get mon mon_warn_on_legacy_crush_tunables
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_legacy_crush_tunables
ceph -s
ceph mon stat
```

---

### mon_warn_on_older_version

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_older_version](../../../config/mon/mon.md#SP_mon_warn_on_older_version) |

**کارکرد:** issue DAEMON_OLD_VERSION health warning if daemons are not all running the same version

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_older_version false
ceph config get mon mon_warn_on_older_version
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon mon_warn_on_older_version
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_connect_panic

| | |
|---|---|
| نوع | Secs · default `30` · **Advanced** |
| جدول | [mon.md#SP_nvmeof_mon_client_connect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_connect_panic) |

**کارکرد:** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it does not receive the initial map from the monitor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon nvmeof_mon_client_connect_panic 30
ceph config get mon nvmeof_mon_client_connect_panic
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon nvmeof_mon_client_connect_panic
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_disconnect_panic

| | |
|---|---|
| نوع | Secs · default `100` · **Advanced** |
| جدول | [mon.md#SP_nvmeof_mon_client_disconnect_panic](../../../config/mon/mon.md#SP_nvmeof_mon_client_disconnect_panic) |

**کارکرد:** The duration, expressed in seconds, after which the nvmeof gateway should trigger a panic if it loses connection to the monitor

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mon nvmeof_mon_client_disconnect_panic 100
ceph config get mon nvmeof_mon_client_disconnect_panic
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mon nvmeof_mon_client_disconnect_panic
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
