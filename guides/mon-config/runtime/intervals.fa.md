# Intervals & timeouts

deep dive پیکربندی MON — 17 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_con_tracker_persist_interval](#mon_con_tracker_persist_interval) | `10` | Advanced | Performance |
| [mon_elector_ping_timeout](#mon_elector_ping_timeout) | `2` | Advanced | Performance |
| [mon_lease_ack_timeout_factor](#mon_lease_ack_timeout_factor) | `2` | Advanced | Performance |
| [mon_lease_renew_interval_factor](#mon_lease_renew_interval_factor) | `0.6` | Advanced | Performance |
| [mon_mds_blocklist_interval](#mon_mds_blocklist_interval) | `1_day` | Dev | Dev |
| [mon_netsplit_grace_period](#mon_netsplit_grace_period) | `9` | Advanced | Performance |
| [mon_nvmeofgw_failback_delay](#mon_nvmeofgw_failback_delay) | `0` | Advanced | Performance |
| [mon_nvmeofgw_skip_failovers_interval](#mon_nvmeofgw_skip_failovers_interval) | `16` | Advanced | Performance |
| [mon_session_timeout](#mon_session_timeout) | `5_min` | Advanced | Performance |
| [mon_smart_report_timeout](#mon_smart_report_timeout) | `5` | Advanced | Performance |
| [mon_subscribe_interval](#mon_subscribe_interval) | `1_day` | Dev | Dev |
| [mon_tick_interval](#mon_tick_interval) | `5` | Advanced | Performance |
| [mon_timecheck_interval](#mon_timecheck_interval) | `5_min` | Advanced | Performance |
| [mon_timecheck_skew_interval](#mon_timecheck_skew_interval) | `30` | Advanced | Performance |
| [mon_use_min_delay_socket](#mon_use_min_delay_socket) | `False` | Advanced | Performance |
| [mon_warn_older_version_delay](#mon_warn_older_version_delay) | `7_day` | Advanced | Performance |
| [nvmeof_mon_client_tick_period](#nvmeof_mon_client_tick_period) | `1` | Advanced | Performance |

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

### mon_con_tracker_persist_interval

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_con_tracker_persist_interval](../../../config/mon/mon.md#SP_mon_con_tracker_persist_interval) |

**کارکرد:** how many updates the ConnectionTracker takes before it persists to disk

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_con_tracker_persist_interval 10
ceph config get mon mon_con_tracker_persist_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `1`، حداکثر `100000`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_con_tracker_persist_interval
ceph -s
ceph mon stat
```

---

### mon_elector_ping_timeout

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_elector_ping_timeout](../../../config/mon/mon.md#SP_mon_elector_ping_timeout) |

**کارکرد:** The time after which a ping 'times out' and a connection is considered down

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_elector_ping_timeout 2
ceph config get mon mon_elector_ping_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_elector_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_lease_ack_timeout_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_lease_ack_timeout_factor](../../../config/mon/mon.md#SP_mon_lease_ack_timeout_factor) |

**کارکرد:** multiple of mon_lease for the lease ack interval before calling new election

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_lease_ack_timeout_factor 2
ceph config get mon mon_lease_ack_timeout_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `1.0001`، حداکثر `100`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_lease_ack_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_lease_renew_interval_factor

| | |
|---|---|
| نوع | Float · default `0.6` · **Advanced** |
| جدول | [mon.md#SP_mon_lease_renew_interval_factor](../../../config/mon/mon.md#SP_mon_lease_renew_interval_factor) |

**کارکرد:** multiple of mon_lease for the lease renewal interval

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_lease_renew_interval_factor 0.6
ceph config get mon mon_lease_renew_interval_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.6`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `0.9999999`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_lease_renew_interval_factor
ceph -s
ceph mon stat
```

---

### mon_mds_blocklist_interval

| | |
|---|---|
| نوع | Float · default `1_day` · **Dev** |
| جدول | [mon.md#SP_mon_mds_blocklist_interval](../../../config/mon/mon.md#SP_mon_mds_blocklist_interval) |

**کارکرد:** Duration in seconds that blocklist entries for MDS daemons remain in the OSD map

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_mds_blocklist_interval 1_day
ceph config get mon mon_mds_blocklist_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1_day`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_netsplit_grace_period

| | |
|---|---|
| نوع | Secs · default `9` · **Advanced** |
| جدول | [mon.md#SP_mon_netsplit_grace_period](../../../config/mon/mon.md#SP_mon_netsplit_grace_period) |

**کارکرد:** Time (in seconds) to wait before emitting a MON_NETSPLIT health warning.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_netsplit_grace_period 9
ceph config get mon mon_netsplit_grace_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `9`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_netsplit_grace_period
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_failback_delay

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_failback_delay](../../../config/mon/mon.md#SP_mon_nvmeofgw_failback_delay) |

**کارکرد:** Period in seconds to delay HA failback of the gateway

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_failback_delay 0
ceph config get mon mon_nvmeofgw_failback_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_nvmeofgw_failback_delay
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_skip_failovers_interval

| | |
|---|---|
| نوع | Secs · default `16` · **Advanced** |
| جدول | [mon.md#SP_mon_nvmeofgw_skip_failovers_interval](../../../config/mon/mon.md#SP_mon_nvmeofgw_skip_failovers_interval) |

**کارکرد:** Period in seconds in which no failovers are performed in GW's pool-group this is equal to max GW redeploy interval

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_nvmeofgw_skip_failovers_interval 16
ceph config get mon mon_nvmeofgw_skip_failovers_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_nvmeofgw_skip_failovers_interval
ceph -s
ceph mon stat
```

---

### mon_session_timeout

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [mon.md#SP_mon_session_timeout](../../../config/mon/mon.md#SP_mon_session_timeout) |

**کارکرد:** close inactive mon client connections after this many seconds

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_session_timeout 5_min
ceph config get mon mon_session_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_session_timeout
ceph -s
ceph mon stat
```

---

### mon_smart_report_timeout

| | |
|---|---|
| نوع | Uint · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_smart_report_timeout](../../../config/mon/mon.md#SP_mon_smart_report_timeout) |

**کارکرد:** Timeout (in seconds) for smartctl to run, default is set to 5

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_smart_report_timeout 5
ceph config get mon mon_smart_report_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_smart_report_timeout
ceph -s
ceph mon stat
```

---

### mon_subscribe_interval

| | |
|---|---|
| نوع | Float · default `1_day` · **Dev** |
| جدول | [mon.md#SP_mon_subscribe_interval](../../../config/mon/mon.md#SP_mon_subscribe_interval) |

**کارکرد:** subscribe interval for pre-jewel clients

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_subscribe_interval 1_day
ceph config get mon mon_subscribe_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1_day`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_tick_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mon.md#SP_mon_tick_interval](../../../config/mon/mon.md#SP_mon_tick_interval) |

**کارکرد:** interval for internal mon background checks

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_tick_interval 5
ceph config get mon mon_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_tick_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_interval

| | |
|---|---|
| نوع | Float · default `5_min` · **Advanced** |
| جدول | [mon.md#SP_mon_timecheck_interval](../../../config/mon/mon.md#SP_mon_timecheck_interval) |

**کارکرد:** frequency of clock synchronization checks between monitors (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_timecheck_interval 5_min
ceph config get mon mon_timecheck_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_timecheck_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_skew_interval

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [mon.md#SP_mon_timecheck_skew_interval](../../../config/mon/mon.md#SP_mon_timecheck_skew_interval) |

**کارکرد:** frequency of clock synchronization (re)checks between monitors while clocks are believed to be skewed (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_timecheck_skew_interval 30
ceph config get mon mon_timecheck_skew_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_timecheck_skew_interval
ceph -s
ceph mon stat
```

---

### mon_use_min_delay_socket

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_use_min_delay_socket](../../../config/mon/mon.md#SP_mon_use_min_delay_socket) |

**کارکرد:** priority packets between mons

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set mon mon_use_min_delay_socket true
ceph config get mon mon_use_min_delay_socket
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_use_min_delay_socket
ceph -s
ceph mon stat
```

---

### mon_warn_older_version_delay

| | |
|---|---|
| نوع | Secs · default `7_day` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_older_version_delay](../../../config/mon/mon.md#SP_mon_warn_older_version_delay) |

**کارکرد:** issue DAEMON_OLD_VERSION health warning after this amount of time has elapsed

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_warn_older_version_delay 7_day
ceph config get mon mon_warn_older_version_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `7_day`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_older_version_delay
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_tick_period

| | |
|---|---|
| نوع | Secs · default `1` · **Advanced** |
| جدول | [mon.md#SP_nvmeof_mon_client_tick_period](../../../config/mon/mon.md#SP_nvmeof_mon_client_tick_period) |

**کارکرد:** Period in seconds of nvmeof gateway beacon messages to monitor

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon nvmeof_mon_client_tick_period 1
ceph config get mon nvmeof_mon_client_tick_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon nvmeof_mon_client_tick_period
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
