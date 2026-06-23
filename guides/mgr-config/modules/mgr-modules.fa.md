# Manager & cephadm modules

راهنمای عمیق پیکربندی MGR — 31 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [cephadm_path](#cephadm_path) | `/usr/sbin/cephadm` | Advanced | Capacity |
| [mgr_client_bytes](#mgr_client_bytes) | `128_M` | Dev | Dev |
| [mgr_client_messages](#mgr_client_messages) | `512` | Dev | Dev |
| [mgr_data](#mgr_data) | `/var/lib/ceph/mgr/$cluster-$id` | Advanced | Performance |
| [mgr_debug_aggressive_pg_num_changes](#mgr_debug_aggressive_pg_num_changes) | `False` | Dev | Dev |
| [mgr_disabled_modules](#mgr_disabled_modules) | `0` | Advanced | Performance |
| [mgr_initial_modules](#mgr_initial_modules) | `iostat nfs nvmeof` | Basic | Policy |
| [mgr_max_pg_creating](#mgr_max_pg_creating) | `1024` | Advanced | Performance |
| [mgr_max_pg_num_change](#mgr_max_pg_num_change) | `128` | Advanced | Performance |
| [mgr_mds_bytes](#mgr_mds_bytes) | `128_M` | Dev | Dev |
| [mgr_mds_messages](#mgr_mds_messages) | `128` | Dev | Dev |
| [mgr_module_load_delay](#mgr_module_load_delay) | `0` | Dev | Dev |
| [mgr_module_load_delay_name](#mgr_module_load_delay_name) | `(empty)` | Dev | Dev |
| [mgr_module_load_expiration](#mgr_module_load_expiration) | `20000` | Dev | Dev |
| [mgr_module_monitor_interval](#mgr_module_monitor_interval) | `5` | Advanced | Performance |
| [mgr_module_path](#mgr_module_path) | `0/mgr` | Advanced | Capacity |
| [mgr_mon_bytes](#mgr_mon_bytes) | `128_M` | Dev | Dev |
| [mgr_mon_messages](#mgr_mon_messages) | `128` | Dev | Dev |
| [mgr_osd_bytes](#mgr_osd_bytes) | `512_M` | Dev | Dev |
| [mgr_osd_messages](#mgr_osd_messages) | `8_K` | Dev | Dev |
| [mgr_osd_upgrade_check_convergence_factor](#mgr_osd_upgrade_check_convergence_factor) | `0.8` | Advanced | Performance |
| [mgr_pool](#mgr_pool) | `True` | Dev | Dev |
| [mgr_service_beacon_grace](#mgr_service_beacon_grace) | `1_min` | Advanced | Performance |
| [mgr_standby_modules](#mgr_standby_modules) | `True` | Advanced | Performance |
| [mgr_stats_period](#mgr_stats_period) | `5` | Basic | Policy |
| [mgr_stats_period_autotune](#mgr_stats_period_autotune) | `True` | Basic | Policy |
| [mgr_stats_period_autotune_queue_threshold](#mgr_stats_period_autotune_queue_threshold) | `100` | Advanced | Performance |
| [mgr_stats_threshold](#mgr_stats_threshold) | `5` | Advanced | Performance |
| [mgr_subinterpreter_modules](#mgr_subinterpreter_modules) | `0` | Advanced | Performance |
| [mgr_test_metadata_error](#mgr_test_metadata_error) | `False` | Dev | Dev |
| [mgr_tick_period](#mgr_tick_period) | `2` | Advanced | Performance |

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

### cephadm_path

| | |
|---|---|
| نوع | Str · default `/usr/sbin/cephadm` · **Advanced** |
| جدول | [cephadm.md#SP_cephadm_path](../../../config/mgr/cephadm.md#SP_cephadm_path) |

**کارکرد:** Path to the `cephadm` binary used by the cephadm orchestrator module.

**زمان استفاده:** Set when cephadm is not in `$PATH` for the mgr daemon user (common with custom installs).

**مثال:**

```bash
ceph config set mgr cephadm_path "/usr/sbin/cephadm"
ceph config get mgr cephadm_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `/usr/sbin/cephadm`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr cephadm_path
ceph -s
ceph mgr stat
```

---

### mgr_client_bytes

| | |
|---|---|
| نوع | Size · default `128_M` · **Dev** |
| جدول | [mgr.md#SP_mgr_client_bytes](../../../config/mgr/mgr.md#SP_mgr_client_bytes) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_client_bytes 128_M
ceph config get mgr mgr_client_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`128_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_client_messages

| | |
|---|---|
| نوع | Uint · default `512` · **Dev** |
| جدول | [mgr.md#SP_mgr_client_messages](../../../config/mgr/mgr.md#SP_mgr_client_messages) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_client_messages 512
ceph config get mgr mgr_client_messages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`512`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/mgr/$cluster-$id` · **Advanced** |
| جدول | [mgr.md#SP_mgr_data](../../../config/mgr/mgr.md#SP_mgr_data) |

**کارکرد:** Filesystem path to the Manager's data directory, which contains keyrings and other data

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr mgr_data "/var/lib/ceph/mgr/$cluster-$id"
ceph config get mgr mgr_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/mgr/$cluster-$id`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_data
ceph -s
ceph mgr stat
```

---

### mgr_debug_aggressive_pg_num_changes

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mgr.md#SP_mgr_debug_aggressive_pg_num_changes](../../../config/mgr/mgr.md#SP_mgr_debug_aggressive_pg_num_changes) |

**کارکرد:** Bypass most throttling and safety checks in pg&#91;p&#93;_num controller

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_debug_aggressive_pg_num_changes true
ceph config get mgr mgr_debug_aggressive_pg_num_changes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_disabled_modules

| | |
|---|---|
| نوع | Str · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mgr.md#SP_mgr_disabled_modules](../../../config/mgr/mgr.md#SP_mgr_disabled_modules) |

**کارکرد:** Comma-separated list of manager modules that must not be loaded.

**زمان استفاده:** Disable unused modules to reduce attack surface and MGR startup time.

**مثال:**

```bash
ceph config set mgr mgr_disabled_modules "example"
ceph config get mgr mgr_disabled_modules
ceph orch restart mgr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_disabled_modules
ceph -s
ceph mgr stat
```

---

### mgr_initial_modules

| | |
|---|---|
| نوع | Str · default `iostat nfs nvmeof` · **Basic** |
| جدول | [mgr.md#SP_mgr_initial_modules](../../../config/mgr/mgr.md#SP_mgr_initial_modules) |

**کارکرد:** List of manager modules to enable when the cluster is first started

**زمان استفاده:** رفتار اصلی MGR — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set mgr mgr_initial_modules "iostat nfs nvmeof"
ceph config get mgr mgr_initial_modules
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `iostat nfs nvmeof` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_initial_modules
ceph -s
ceph mgr stat
```

---

### mgr_max_pg_creating

| | |
|---|---|
| نوع | Uint · default `1024` · **Advanced** |
| جدول | [mgr.md#SP_mgr_max_pg_creating](../../../config/mgr/mgr.md#SP_mgr_max_pg_creating) |

**کارکرد:** bound on max creating pgs when acting to create more pgs

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mgr mgr_max_pg_creating 1024
ceph config get mgr mgr_max_pg_creating
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1024`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_max_pg_creating
ceph -s
ceph mgr stat
```

---

### mgr_max_pg_num_change

| | |
|---|---|
| نوع | Int · default `128` · **Advanced** |
| جدول | [mgr.md#SP_mgr_max_pg_num_change](../../../config/mgr/mgr.md#SP_mgr_max_pg_num_change) |

**کارکرد:** Maximum PG count change the MGR balancer/autoscaler applies per iteration.

**زمان استفاده:** Lower on busy clusters to avoid large placement churn; raise for faster PG convergence after expansion.

**مثال:**

```bash
ceph config set mgr mgr_max_pg_num_change 128
ceph config get mgr mgr_max_pg_num_change
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `128`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_max_pg_num_change
ceph -s
ceph mgr stat
```

---

### mgr_mds_bytes

| | |
|---|---|
| نوع | Size · default `128_M` · **Dev** |
| جدول | [mgr.md#SP_mgr_mds_bytes](../../../config/mgr/mgr.md#SP_mgr_mds_bytes) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_mds_bytes 128_M
ceph config get mgr mgr_mds_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`128_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_mds_messages

| | |
|---|---|
| نوع | Uint · default `128` · **Dev** |
| جدول | [mgr.md#SP_mgr_mds_messages](../../../config/mgr/mgr.md#SP_mgr_mds_messages) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_mds_messages 128
ceph config get mgr mgr_mds_messages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`128`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_module_load_delay

| | |
|---|---|
| نوع | Millisecs · default `0` · **Dev** |
| جدول | [mgr.md#SP_mgr_module_load_delay](../../../config/mgr/mgr.md#SP_mgr_module_load_delay) |

**کارکرد:** Number of milliseconds for Manager modules to delay loading. For testing purposes only.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_module_load_delay 0
ceph config get mgr mgr_module_load_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_module_load_delay_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [mgr.md#SP_mgr_module_load_delay_name](../../../config/mgr/mgr.md#SP_mgr_module_load_delay_name) |

**کارکرد:** Specify which Manager module is to delay loading by mgr_module_load_delay milliseconds. For testing purposes only.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_module_load_delay_name "example"
ceph config get mgr mgr_module_load_delay_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_module_load_expiration

| | |
|---|---|
| نوع | Millisecs · default `20000` · **Dev** |
| جدول | [mgr.md#SP_mgr_module_load_expiration](../../../config/mgr/mgr.md#SP_mgr_module_load_expiration) |

**کارکرد:** Maximum number of milliseconds the active mgr is allowed to load the mgr modules before declaring availability.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_module_load_expiration 20000
ceph config get mgr mgr_module_load_expiration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`20000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_module_monitor_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mgr.md#SP_mgr_module_monitor_interval](../../../config/mgr/mgr.md#SP_mgr_module_monitor_interval) |

**کارکرد:** Period in seconds for collecting Manager modules cpu and memory performance counters.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mgr mgr_module_monitor_interval 5
ceph config get mgr mgr_module_monitor_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_module_monitor_interval
ceph -s
ceph mgr stat
```

---

### mgr_module_path

| | |
|---|---|
| نوع | Str · default `0/mgr` · **Advanced** |
| جدول | [mgr.md#SP_mgr_module_path](../../../config/mgr/mgr.md#SP_mgr_module_path) |

**کارکرد:** Directory where Ceph manager modules are loaded from.

**زمان استفاده:** Change only for custom module paths or non-packaged installs.

**مثال:**

```bash
ceph config set mgr mgr_module_path "0/mgr"
ceph config get mgr mgr_module_path
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Capacity

1. خط پایه روی `0/mgr`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_module_path
ceph -s
ceph mgr stat
```

---

### mgr_mon_bytes

| | |
|---|---|
| نوع | Size · default `128_M` · **Dev** |
| جدول | [mgr.md#SP_mgr_mon_bytes](../../../config/mgr/mgr.md#SP_mgr_mon_bytes) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_mon_bytes 128_M
ceph config get mgr mgr_mon_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`128_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_mon_messages

| | |
|---|---|
| نوع | Uint · default `128` · **Dev** |
| جدول | [mgr.md#SP_mgr_mon_messages](../../../config/mgr/mgr.md#SP_mgr_mon_messages) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_mon_messages 128
ceph config get mgr mgr_mon_messages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`128`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_osd_bytes

| | |
|---|---|
| نوع | Size · default `512_M` · **Dev** |
| جدول | [mgr.md#SP_mgr_osd_bytes](../../../config/mgr/mgr.md#SP_mgr_osd_bytes) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_osd_bytes 512_M
ceph config get mgr mgr_osd_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`512_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_osd_messages

| | |
|---|---|
| نوع | Uint · default `8_K` · **Dev** |
| جدول | [mgr.md#SP_mgr_osd_messages](../../../config/mgr/mgr.md#SP_mgr_osd_messages) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_osd_messages 8_K
ceph config get mgr mgr_osd_messages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`8_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_osd_upgrade_check_convergence_factor

| | |
|---|---|
| نوع | Float · default `0.8` · **Advanced** |
| جدول | [mgr.md#SP_mgr_osd_upgrade_check_convergence_factor](../../../config/mgr/mgr.md#SP_mgr_osd_upgrade_check_convergence_factor) |

**کارکرد:** The factor used to converge to a subset of OSDs within a CRUSH bucket that can be upgraded without affecting immediate data availability.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr mgr_osd_upgrade_check_convergence_factor 0.8
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.8`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0.1`، حداکثر `0.9`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
ceph -s
ceph mgr stat
```

---

### mgr_pool

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mgr.md#SP_mgr_pool](../../../config/mgr/mgr.md#SP_mgr_pool) |

**کارکرد:** Allow use/creation of .mgr pool.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_pool false
ceph config get mgr mgr_pool
ceph orch restart mgr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_service_beacon_grace

| | |
|---|---|
| نوع | Float · default `1_min` · **Advanced** |
| جدول | [mgr.md#SP_mgr_service_beacon_grace](../../../config/mgr/mgr.md#SP_mgr_service_beacon_grace) |

**کارکرد:** Period in seconds from last beacon to manager dropping state about a monitored service (RGW, rbd-mirror etc)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr mgr_service_beacon_grace 1_min
ceph config get mgr mgr_service_beacon_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_service_beacon_grace
ceph -s
ceph mgr stat
```

---

### mgr_standby_modules

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mgr.md#SP_mgr_standby_modules](../../../config/mgr/mgr.md#SP_mgr_standby_modules) |

**کارکرد:** When `true`, standby MGR daemons serve the dashboard/API via HTTP redirect to the active manager.

**زمان استفاده:** Disable (`false`) when a load balancer fronts MGR endpoints — redirects often break behind LB private IPs.

**مثال:**

```bash
ceph config set mgr mgr_standby_modules false
ceph config get mgr mgr_standby_modules
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_standby_modules
ceph -s
ceph mgr stat
```

---

### mgr_stats_period

| | |
|---|---|
| نوع | Int · default `5` · **Basic** |
| جدول | [mgr.md#SP_mgr_stats_period](../../../config/mgr/mgr.md#SP_mgr_stats_period) |

**کارکرد:** Interval (seconds) between MGR cluster stat refreshes.

**زمان استفاده:** Shorten for fresher dashboard metrics; lengthen on very large clusters to reduce MGR CPU load.

**مثال:**

```bash
ceph config set mgr mgr_stats_period 5
ceph config get mgr mgr_stats_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `5` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_stats_period
ceph -s
ceph mgr stat
```

---

### mgr_stats_period_autotune

| | |
|---|---|
| نوع | Bool · default `True` · **Basic** |
| جدول | [mgr.md#SP_mgr_stats_period_autotune](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune) |

**کارکرد:** Automatically adjust mgr_stats_period based on Manager message queue depth

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mgr mgr_stats_period_autotune false
ceph config get mgr mgr_stats_period_autotune
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_stats_period_autotune
ceph -s
ceph mgr stat
```

---

### mgr_stats_period_autotune_queue_threshold

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [mgr.md#SP_mgr_stats_period_autotune_queue_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune_queue_threshold) |

**کارکرد:** Message queue depth that triggers automatic increase of mgr_stats_period

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mgr mgr_stats_period_autotune_queue_threshold 100
ceph config get mgr mgr_stats_period_autotune_queue_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_stats_period_autotune_queue_threshold
ceph -s
ceph mgr stat
```

---

### mgr_stats_threshold

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mgr.md#SP_mgr_stats_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_threshold) |

**کارکرد:** Lowest perfcounter priority collected by mgr

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr mgr_stats_threshold 5
ceph config get mgr mgr_stats_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `11`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_stats_threshold
ceph -s
ceph mgr stat
```

---

### mgr_subinterpreter_modules

| | |
|---|---|
| نوع | Str · default `0` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mgr.md#SP_mgr_subinterpreter_modules](../../../config/mgr/mgr.md#SP_mgr_subinterpreter_modules) |

**کارکرد:** List of manager modules to load in independent subinterpreters

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mgr mgr_subinterpreter_modules "example"
ceph config get mgr mgr_subinterpreter_modules
ceph orch restart mgr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_subinterpreter_modules
ceph -s
ceph mgr stat
```

---

### mgr_test_metadata_error

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mgr.md#SP_mgr_test_metadata_error](../../../config/mgr/mgr.md#SP_mgr_test_metadata_error) |

**کارکرد:** Used for simulating errors during operations involving metadata.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mgr mgr_test_metadata_error true
ceph config get mgr mgr_test_metadata_error
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mgr_tick_period

| | |
|---|---|
| نوع | Secs · default `2` · **Advanced** |
| جدول | [mgr.md#SP_mgr_tick_period](../../../config/mgr/mgr.md#SP_mgr_tick_period) |

**کارکرد:** Period in seconds of beacon messages to monitor

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mgr mgr_tick_period 2
ceph config get mgr mgr_tick_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mgr mgr_tick_period
ceph -s
ceph mgr stat
```

---


[← نمای کلی](../OVERVIEW.md)
