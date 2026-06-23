# Intervals

deep dive پیکربندی MDS — 19 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_bal_fragment_interval](#mds_bal_fragment_interval) | `5` | Advanced | Performance |
| [mds_bal_interval](#mds_bal_interval) | `10` | Advanced | Performance |
| [mds_bal_sample_interval](#mds_bal_sample_interval) | `3` | Advanced | Performance |
| [mds_beacon_interval](#mds_beacon_interval) | `4` | Advanced | Performance |
| [mds_cache_release_free_interval](#mds_cache_release_free_interval) | `10` | Dev | Dev |
| [mds_cache_trim_interval](#mds_cache_trim_interval) | `1` | Advanced | Performance |
| [mds_dirstat_min_interval](#mds_dirstat_min_interval) | `1` | Dev | Dev |
| [mds_extraordinary_events_dump_interval](#mds_extraordinary_events_dump_interval) | `0` | Advanced | Performance |
| [mds_freeze_tree_timeout](#mds_freeze_tree_timeout) | `30` | Dev | Dev |
| [mds_metrics_update_interval](#mds_metrics_update_interval) | `2` | Advanced | Performance |
| [mds_mon_shutdown_timeout](#mds_mon_shutdown_timeout) | `5` | Advanced | Performance |
| [mds_ping_interval](#mds_ping_interval) | `5` | Advanced | Performance |
| [mds_reconnect_timeout](#mds_reconnect_timeout) | `45` | Advanced | Performance |
| [mds_replay_interval](#mds_replay_interval) | `1` | Advanced | Performance |
| [mds_scatter_nudge_interval](#mds_scatter_nudge_interval) | `5` | Advanced | Performance |
| [mds_session_blocklist_on_timeout](#mds_session_blocklist_on_timeout) | `True` | Advanced | Performance |
| [mds_task_status_update_interval](#mds_task_status_update_interval) | `2` | Dev | Dev |
| [mds_tick_interval](#mds_tick_interval) | `5` | Advanced | Performance |
| [subv_metrics_window_interval](#subv_metrics_window_interval) | `30` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_bal_fragment_interval

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_fragment_interval](../../../config/mds/mds.md#SP_mds_bal_fragment_interval) |

**کارکرد:** delay in seconds before interrupting client IO to perform splits

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_bal_fragment_interval 5
ceph config get mds mds_bal_fragment_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_bal_fragment_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_interval

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_interval](../../../config/mds/mds.md#SP_mds_bal_interval) |

**کارکرد:** interval between MDS balancer cycles

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_bal_interval 10
ceph config get mds mds_bal_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_bal_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_sample_interval

| | |
|---|---|
| نوع | Float · default `3` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_sample_interval](../../../config/mds/mds.md#SP_mds_bal_sample_interval) |

**کارکرد:** interval in seconds between balancer ticks

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_bal_sample_interval 3
ceph config get mds mds_bal_sample_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_bal_sample_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_beacon_interval

| | |
|---|---|
| نوع | Float · default `4` · **Advanced** |
| جدول | [mds.md#SP_mds_beacon_interval](../../../config/mds/mds.md#SP_mds_beacon_interval) |

**کارکرد:** How often (seconds) an MDS sends beacons to monitors.

**زمان استفاده:** Rarely changed; must stay well below `mds_beacon_grace`.

**مثال:**

```bash
ceph config set mds mds_beacon_interval 4
ceph config get mds mds_beacon_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_beacon_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_release_free_interval

| | |
|---|---|
| نوع | Secs · default `10` · **Dev** |
| جدول | [mds.md#SP_mds_cache_release_free_interval](../../../config/mds/mds.md#SP_mds_cache_release_free_interval) |

**کارکرد:** Interval in seconds between heap releases

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_cache_release_free_interval 10
ceph config get mds mds_cache_release_free_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`10`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_cache_trim_interval

| | |
|---|---|
| نوع | Secs · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_trim_interval](../../../config/mds/mds.md#SP_mds_cache_trim_interval) |

**کارکرد:** Interval in seconds between cache trims

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_cache_trim_interval 1
ceph config get mds mds_cache_trim_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_cache_trim_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dirstat_min_interval

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [mds.md#SP_mds_dirstat_min_interval](../../../config/mds/mds.md#SP_mds_dirstat_min_interval) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_dirstat_min_interval 1
ceph config get mds mds_dirstat_min_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`1`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_extraordinary_events_dump_interval

| | |
|---|---|
| نوع | Secs · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_extraordinary_events_dump_interval](../../../config/mds/mds.md#SP_mds_extraordinary_events_dump_interval) |

**کارکرد:** Interval in seconds for dumping the recent in-memory logs when there is an extra-ordinary event.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_extraordinary_events_dump_interval 0
ceph config get mds mds_extraordinary_events_dump_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `60`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_extraordinary_events_dump_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_freeze_tree_timeout

| | |
|---|---|
| نوع | Float · default `30` · **Dev** |
| جدول | [mds.md#SP_mds_freeze_tree_timeout](../../../config/mds/mds.md#SP_mds_freeze_tree_timeout) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_freeze_tree_timeout 30
ceph config get mds mds_freeze_tree_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`30`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_metrics_update_interval

| | |
|---|---|
| نوع | Secs · default `2` · **Advanced** |
| جدول | [mds.md#SP_mds_metrics_update_interval](../../../config/mds/mds.md#SP_mds_metrics_update_interval) |

**کارکرد:** interval in seconds for metrics data update.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_metrics_update_interval 2
ceph config get mds mds_metrics_update_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_metrics_update_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_mon_shutdown_timeout

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_mon_shutdown_timeout](../../../config/mds/mds.md#SP_mds_mon_shutdown_timeout) |

**کارکرد:** time to wait for mon to receive damaged MDS rank notification

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_mon_shutdown_timeout 5
ceph config get mds mds_mon_shutdown_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_mon_shutdown_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_ping_interval

| | |
|---|---|
| نوع | Secs · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_ping_interval](../../../config/mds/mds.md#SP_mds_ping_interval) |

**کارکرد:** interval in seconds for sending ping messages to active MDSs.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_ping_interval 5
ceph config get mds mds_ping_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_ping_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_reconnect_timeout

| | |
|---|---|
| نوع | Float · default `45` · **Advanced** |
| جدول | [mds.md#SP_mds_reconnect_timeout](../../../config/mds/mds.md#SP_mds_reconnect_timeout) |

**کارکرد:** Timeout in seconds to wait for clients to reconnect during MDS reconnect recovery state

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_reconnect_timeout 45
ceph config get mds mds_reconnect_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `45`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_reconnect_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_replay_interval

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_replay_interval](../../../config/mds/mds.md#SP_mds_replay_interval) |

**کارکرد:** time in seconds between replay of updates to journal by standby replay MDS

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_replay_interval 1
ceph config get mds mds_replay_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_replay_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_scatter_nudge_interval

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_scatter_nudge_interval](../../../config/mds/mds.md#SP_mds_scatter_nudge_interval) |

**کارکرد:** minimum interval between scatter lock updates

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_scatter_nudge_interval 5
ceph config get mds mds_scatter_nudge_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_scatter_nudge_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_blocklist_on_timeout

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_session_blocklist_on_timeout](../../../config/mds/mds.md#SP_mds_session_blocklist_on_timeout) |

**کارکرد:** Blocklist clients whose sessions have become stale

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_session_blocklist_on_timeout false
ceph config get mds mds_session_blocklist_on_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_session_blocklist_on_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_task_status_update_interval

| | |
|---|---|
| نوع | Float · default `2` · **Dev** |
| جدول | [mds.md#SP_mds_task_status_update_interval](../../../config/mds/mds.md#SP_mds_task_status_update_interval) |

**کارکرد:** task status update interval to manager

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds mds_task_status_update_interval 2
ceph config get mds mds_task_status_update_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`2`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mds_tick_interval

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_tick_interval](../../../config/mds/mds.md#SP_mds_tick_interval) |

**کارکرد:** time in seconds between upkeep tasks

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_tick_interval 5
ceph config get mds mds_tick_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mds mds_tick_interval
ceph -s
ceph fs status
ceph mds stat
```

---

### subv_metrics_window_interval

| | |
|---|---|
| نوع | Secs · default `30` · **Dev** |
| جدول | [mds.md#SP_subv_metrics_window_interval](../../../config/mds/mds.md#SP_subv_metrics_window_interval) |

**کارکرد:** subvolume metrics sliding window interval, seconds

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mds subv_metrics_window_interval 30
ceph config get mds subv_metrics_window_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`30`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
