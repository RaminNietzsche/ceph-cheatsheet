# Mon

deep dive پیکربندی Global — 74 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mon_allow_pool_delete](#mon_allow_pool_delete) | `False` | Advanced | Policy |
| [mon_client_bytes](#mon_client_bytes) | `100_M` | Advanced | Performance |
| [mon_client_directed_command_retry](#mon_client_directed_command_retry) | `2` | Dev | Dev |
| [mon_client_hunt_interval](#mon_client_hunt_interval) | `3` | Advanced | Performance |
| [mon_client_hunt_interval_backoff](#mon_client_hunt_interval_backoff) | `1.5` | Advanced | Performance |
| [mon_client_hunt_interval_max_multiple](#mon_client_hunt_interval_max_multiple) | `10` | Advanced | Performance |
| [mon_client_hunt_interval_min_multiple](#mon_client_hunt_interval_min_multiple) | `1` | Advanced | Performance |
| [mon_client_hunt_on_resend](#mon_client_hunt_on_resend) | `True` | Advanced | Performance |
| [mon_client_hunt_parallel](#mon_client_hunt_parallel) | `3` | Advanced | Performance |
| [mon_client_log_interval](#mon_client_log_interval) | `1` | Advanced | Performance |
| [mon_client_max_log_entries_per_message](#mon_client_max_log_entries_per_message) | `1000` | Advanced | Performance |
| [mon_client_ping_interval](#mon_client_ping_interval) | `10` | Advanced | Performance |
| [mon_client_ping_timeout](#mon_client_ping_timeout) | `30` | Advanced | Performance |
| [mon_client_target_rank](#mon_client_target_rank) | `-1` | Advanced | Performance |
| [mon_config_key_max_entry_size](#mon_config_key_max_entry_size) | `64_K` | Advanced | Performance |
| [mon_debug_block_osdmap_trim](#mon_debug_block_osdmap_trim) | `False` | Dev | Dev |
| [mon_debug_deprecated_as_obsolete](#mon_debug_deprecated_as_obsolete) | `False` | Dev | Dev |
| [mon_debug_dump_json](#mon_debug_dump_json) | `False` | Dev | Dev |
| [mon_debug_dump_location](#mon_debug_dump_location) | `/var/log/ceph/$cluster-$name.tdump` | Dev | Dev |
| [mon_debug_dump_transactions](#mon_debug_dump_transactions) | `False` | Dev | Dev |
| [mon_debug_extra_checks](#mon_debug_extra_checks) | `False` | Dev | Dev |
| [mon_debug_no_initial_persistent_features](#mon_debug_no_initial_persistent_features) | `False` | Dev | Dev |
| [mon_debug_no_require_bluestore_for_ec_overwrites](#mon_debug_no_require_bluestore_for_ec_overwrites) | `False` | Dev | Dev |
| [mon_debug_no_require_tentacle](#mon_debug_no_require_tentacle) | `False` | Dev | Dev |
| [mon_debug_no_require_umbrella](#mon_debug_no_require_umbrella) | `False` | Dev | Dev |
| [mon_debug_unsafe_allow_tier_with_nonempty_snaps](#mon_debug_unsafe_allow_tier_with_nonempty_snaps) | `False` | Dev | Dev |
| [mon_dns_srv_name](#mon_dns_srv_name) | `ceph-mon` | Advanced | Performance |
| [mon_fake_pool_delete](#mon_fake_pool_delete) | `False` | Advanced | Performance |
| [mon_force_quorum_join](#mon_force_quorum_join) | `False` | Advanced | Performance |
| [mon_globalid_prealloc](#mon_globalid_prealloc) | `10000` | Advanced | Performance |
| [mon_host](#mon_host) | `(empty)` | Basic | Policy |
| [mon_host_override](#mon_host_override) | `(empty)` | Advanced | Performance |
| [mon_initial_members](#mon_initial_members) | `(empty)` | Advanced | Performance |
| [mon_inject_pg_merge_bounce_probability](#mon_inject_pg_merge_bounce_probability) | `0` | Dev | Dev |
| [mon_inject_sync_get_chunk_delay](#mon_inject_sync_get_chunk_delay) | `0` | Dev | Dev |
| [mon_inject_transaction_delay_max](#mon_inject_transaction_delay_max) | `10` | Dev | Dev |
| [mon_inject_transaction_delay_probability](#mon_inject_transaction_delay_probability) | `0` | Dev | Dev |
| [mon_keyvaluedb](#mon_keyvaluedb) | `rocksdb` | Advanced | Performance |
| [mon_max_log_epochs](#mon_max_log_epochs) | `500` | Advanced | Performance |
| [mon_max_mdsmap_epochs](#mon_max_mdsmap_epochs) | `500` | Advanced | Performance |
| [mon_max_mgrmap_epochs](#mon_max_mgrmap_epochs) | `500` | Advanced | Performance |
| [mon_max_nvmeof_epochs](#mon_max_nvmeof_epochs) | `500` | Advanced | Performance |
| [mon_max_osd](#mon_max_osd) | `10000` | Advanced | Performance |
| [mon_max_pg_per_osd](#mon_max_pg_per_osd) | `500` | Advanced | Performance |
| [mon_max_snap_prune_per_epoch](#mon_max_snap_prune_per_epoch) | `100` | Advanced | Performance |
| [mon_min_osdmap_epochs](#mon_min_osdmap_epochs) | `500` | Advanced | Performance |
| [mon_osd_backfillfull_ratio](#mon_osd_backfillfull_ratio) | `0.9` | Advanced | Performance |
| [mon_osd_force_trim_to](#mon_osd_force_trim_to) | `0` | Dev | Dev |
| [mon_osd_full_ratio](#mon_osd_full_ratio) | `0.95` | Advanced | Performance |
| [mon_osd_initial_require_min_compat_client](#mon_osd_initial_require_min_compat_client) | `luminous` | Advanced | Performance |
| [mon_osd_min_down_reporters](#mon_osd_min_down_reporters) | `2` | Advanced | Performance |
| [mon_osd_nearfull_ratio](#mon_osd_nearfull_ratio) | `0.85` | Advanced | Performance |
| [mon_osd_report_timeout](#mon_osd_report_timeout) | `15_min` | Advanced | Performance |
| [mon_osd_reporter_subtree_level](#mon_osd_reporter_subtree_level) | `host` | Advanced | Performance |
| [mon_osd_snap_trim_queue_warn_on](#mon_osd_snap_trim_queue_warn_on) | `32768` | Advanced | Performance |
| [mon_probe_timeout](#mon_probe_timeout) | `2` | Advanced | Performance |
| [mon_scrub_inject_crc_mismatch](#mon_scrub_inject_crc_mismatch) | `0` | Dev | Dev |
| [mon_scrub_inject_missing_keys](#mon_scrub_inject_missing_keys) | `0` | Dev | Dev |
| [mon_scrub_interval](#mon_scrub_interval) | `1_day` | Advanced | Performance |
| [mon_scrub_max_keys](#mon_scrub_max_keys) | `100` | Advanced | Performance |
| [mon_scrub_timeout](#mon_scrub_timeout) | `5_min` | Advanced | Performance |
| [mon_sync_debug](#mon_sync_debug) | `False` | Dev | Dev |
| [mon_sync_max_payload_keys](#mon_sync_max_payload_keys) | `2000` | Advanced | Performance |
| [mon_sync_max_payload_size](#mon_sync_max_payload_size) | `1_M` | Advanced | Performance |
| [mon_sync_provider_kill_at](#mon_sync_provider_kill_at) | `0` | Dev | Dev |
| [mon_sync_requester_kill_at](#mon_sync_requester_kill_at) | `0` | Dev | Dev |
| [mon_sync_timeout](#mon_sync_timeout) | `1_min` | Advanced | Performance |
| [mon_warn_on_insecure_global_id_reclaim](#mon_warn_on_insecure_global_id_reclaim) | `True` | Advanced | Performance |
| [mon_warn_on_insecure_global_id_reclaim_allowed](#mon_warn_on_insecure_global_id_reclaim_allowed) | `True` | Advanced | Policy |
| [mon_warn_on_msgr2_not_enabled](#mon_warn_on_msgr2_not_enabled) | `True` | Advanced | Policy |
| [mon_warn_on_slow_ping_ratio](#mon_warn_on_slow_ping_ratio) | `0.05` | Advanced | Performance |
| [mon_warn_on_slow_ping_time](#mon_warn_on_slow_ping_time) | `0` | Advanced | Performance |
| [mon_warn_pg_not_deep_scrubbed_ratio](#mon_warn_pg_not_deep_scrubbed_ratio) | `0.75` | Advanced | Performance |
| [mon_warn_pg_not_scrubbed_ratio](#mon_warn_pg_not_scrubbed_ratio) | `0.5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_allow_pool_delete

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_allow_pool_delete](../../../config/global/mon.md#SP_mon_allow_pool_delete) |

**کارکرد:** allow pool deletions

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set mon mon_allow_pool_delete true
ceph config get mon mon_allow_pool_delete
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_allow_pool_delete
ceph -s
ceph mon stat
```

---

### mon_client_bytes

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [mon.md#SP_mon_client_bytes](../../../config/global/mon.md#SP_mon_client_bytes) |

**کارکرد:** Max bytes of outstanding client messages mon will read off the network

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_client_bytes 100_M
ceph config get mon mon_client_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_bytes
ceph -s
ceph mon stat
```

---

### mon_client_directed_command_retry

| | |
|---|---|
| نوع | Int · default `2` · **Dev** |
| جدول | [mon.md#SP_mon_client_directed_command_retry](../../../config/global/mon.md#SP_mon_client_directed_command_retry) |

**کارکرد:** Number of times to try sending a command directed at a specific Monitor

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_client_directed_command_retry 2
ceph config get mon mon_client_directed_command_retry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`2`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_client_hunt_interval

| | |
|---|---|
| نوع | Float · default `3` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_interval](../../../config/global/mon.md#SP_mon_client_hunt_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_client_hunt_interval 3
ceph config get mon mon_client_hunt_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_interval
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_backoff

| | |
|---|---|
| نوع | Float · default `1.5` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_interval_backoff](../../../config/global/mon.md#SP_mon_client_hunt_interval_backoff) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_client_hunt_interval_backoff 1.5
ceph config get mon mon_client_hunt_interval_backoff
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_interval_backoff
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_max_multiple

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_interval_max_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_max_multiple) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_client_hunt_interval_max_multiple 10
ceph config get mon mon_client_hunt_interval_max_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_interval_max_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_min_multiple

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_interval_min_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_min_multiple) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_client_hunt_interval_min_multiple 1
ceph config get mon mon_client_hunt_interval_min_multiple
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_interval_min_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_on_resend

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_on_resend](../../../config/global/mon.md#SP_mon_client_hunt_on_resend) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_client_hunt_on_resend false
ceph config get mon mon_client_hunt_on_resend
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_on_resend
ceph -s
ceph mon stat
```

---

### mon_client_hunt_parallel

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [mon.md#SP_mon_client_hunt_parallel](../../../config/global/mon.md#SP_mon_client_hunt_parallel) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_client_hunt_parallel 3
ceph config get mon mon_client_hunt_parallel
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_hunt_parallel
ceph -s
ceph mon stat
```

---

### mon_client_log_interval

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mon.md#SP_mon_client_log_interval](../../../config/global/mon.md#SP_mon_client_log_interval) |

**کارکرد:** How frequently we send queued cluster log messages to the Monitors

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_client_log_interval 1
ceph config get mon mon_client_log_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_log_interval
ceph -s
ceph mon stat
```

---

### mon_client_max_log_entries_per_message

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [mon.md#SP_mon_client_max_log_entries_per_message](../../../config/global/mon.md#SP_mon_client_max_log_entries_per_message) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_client_max_log_entries_per_message 1000
ceph config get mon mon_client_max_log_entries_per_message
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_max_log_entries_per_message
ceph -s
ceph mon stat
```

---

### mon_client_ping_interval

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mon.md#SP_mon_client_ping_interval](../../../config/global/mon.md#SP_mon_client_ping_interval) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_client_ping_interval 10
ceph config get mon mon_client_ping_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_ping_interval
ceph -s
ceph mon stat
```

---

### mon_client_ping_timeout

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [mon.md#SP_mon_client_ping_timeout](../../../config/global/mon.md#SP_mon_client_ping_timeout) |

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_client_ping_timeout 30
ceph config get mon mon_client_ping_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_client_target_rank

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** |
| جدول | [mon.md#SP_mon_client_target_rank](../../../config/global/mon.md#SP_mon_client_target_rank) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_client_target_rank 128
ceph config get mon mon_client_target_rank
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `-1`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_client_target_rank
ceph -s
ceph mon stat
```

---

### mon_config_key_max_entry_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [mon.md#SP_mon_config_key_max_entry_size](../../../config/global/mon.md#SP_mon_config_key_max_entry_size) |

**کارکرد:** Defines the number of bytes allowed to be held in a single config-key entry

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_config_key_max_entry_size 64_K
ceph config get mon mon_config_key_max_entry_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_config_key_max_entry_size
ceph -s
ceph mon stat
```

---

### mon_debug_block_osdmap_trim

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_block_osdmap_trim](../../../config/global/mon.md#SP_mon_debug_block_osdmap_trim) |

**کارکرد:** Block OSDMap trimming while the option is enabled.

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_block_osdmap_trim true
ceph config get mon mon_debug_block_osdmap_trim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_deprecated_as_obsolete

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_deprecated_as_obsolete](../../../config/global/mon.md#SP_mon_debug_deprecated_as_obsolete) |

**کارکرد:** Treat deprecated mon commands as obsolete

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_deprecated_as_obsolete true
ceph config get mon mon_debug_deprecated_as_obsolete
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_dump_json

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_dump_json](../../../config/global/mon.md#SP_mon_debug_dump_json) |

**کارکرد:** Dump paxos transasctions to log as JSON

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_dump_json true
ceph config get mon mon_debug_dump_json
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_dump_location

| | |
|---|---|
| نوع | Str · default `/var/log/ceph/$cluster-$name.tdump` · **Dev** |
| جدول | [mon.md#SP_mon_debug_dump_location](../../../config/global/mon.md#SP_mon_debug_dump_location) |

**کارکرد:** File to which to dump Paxos transactions

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_dump_location "/var/log/ceph/$cluster-$name.tdump"
ceph config get mon mon_debug_dump_location
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`/var/log/ceph/$cluster-$name.tdump`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_dump_transactions

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_dump_transactions](../../../config/global/mon.md#SP_mon_debug_dump_transactions) |

**کارکرد:** Dump Paxos transactions to log

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_dump_transactions true
ceph config get mon mon_debug_dump_transactions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_extra_checks

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_extra_checks](../../../config/global/mon.md#SP_mon_debug_extra_checks) |

**کارکرد:** Enable some additional monitor checks

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_extra_checks true
ceph config get mon mon_debug_extra_checks
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_no_initial_persistent_features

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_no_initial_persistent_features](../../../config/global/mon.md#SP_mon_debug_no_initial_persistent_features) |

**کارکرد:** Do not set any monmap features for new Monitor clusters

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_no_initial_persistent_features true
ceph config get mon mon_debug_no_initial_persistent_features
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_no_require_bluestore_for_ec_overwrites

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites](../../../config/global/mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites) |

**کارکرد:** Do not require BlueStore OSDs to enable EC overwrites within a RADOS pool

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_no_require_bluestore_for_ec_overwrites true
ceph config get mon mon_debug_no_require_bluestore_for_ec_overwrites
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_no_require_tentacle

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_no_require_tentacle](../../../config/global/mon.md#SP_mon_debug_no_require_tentacle) |

**کارکرد:** Do not require the Tentacle feature for new Monitor clusters

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_no_require_tentacle true
ceph config get mon mon_debug_no_require_tentacle
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_no_require_umbrella

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_no_require_umbrella](../../../config/global/mon.md#SP_mon_debug_no_require_umbrella) |

**کارکرد:** Do not require the Umbrella feature for new Monitor clusters

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_no_require_umbrella true
ceph config get mon mon_debug_no_require_umbrella
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_debug_unsafe_allow_tier_with_nonempty_snaps

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps](../../../config/global/mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps) |

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_debug_unsafe_allow_tier_with_nonempty_snaps true
ceph config get mon mon_debug_unsafe_allow_tier_with_nonempty_snaps
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_dns_srv_name

| | |
|---|---|
| نوع | Str · default `ceph-mon` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mon.md#SP_mon_dns_srv_name](../../../config/global/mon.md#SP_mon_dns_srv_name) |

**کارکرد:** Name of DNS SRV record to check for monitor addresses

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_dns_srv_name "ceph-mon"
ceph config get mon mon_dns_srv_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `ceph-mon`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_dns_srv_name
ceph -s
ceph mon stat
```

---

### mon_fake_pool_delete

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_fake_pool_delete](../../../config/global/mon.md#SP_mon_fake_pool_delete) |

**کارکرد:** Fake pool deletions by renaming the RADOS pool

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set mon mon_fake_pool_delete true
ceph config get mon mon_fake_pool_delete
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_fake_pool_delete
ceph -s
ceph mon stat
```

---

### mon_force_quorum_join

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mon.md#SP_mon_force_quorum_join](../../../config/global/mon.md#SP_mon_force_quorum_join) |

**کارکرد:** Force a Monitor to rejoin the quorum even though it was just removed

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set mon mon_force_quorum_join true
ceph config get mon mon_force_quorum_join
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_force_quorum_join
ceph -s
ceph mon stat
```

---

### mon_globalid_prealloc

| | |
|---|---|
| نوع | Uint · default `10000` · **Advanced** |
| جدول | [mon.md#SP_mon_globalid_prealloc](../../../config/global/mon.md#SP_mon_globalid_prealloc) |

**کارکرد:** number of globalid values to preallocate

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_globalid_prealloc 10000
ceph config get mon mon_globalid_prealloc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_globalid_prealloc
ceph -s
ceph mon stat
```

---

### mon_host

| | |
|---|---|
| نوع | Str · default `(empty)` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mon.md#SP_mon_host](../../../config/global/mon.md#SP_mon_host) |

**کارکرد:** List of hosts or addresses to search for a monitor

**زمان استفاده:** رفتار اصلی Global — قبل از تغییر در production بررسی کنید.

**مثال:**

```bash
ceph config set mon mon_host "example"
ceph config get mon mon_host
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `(empty)` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_host
ceph -s
ceph mon stat
```

---

### mon_host_override

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mon.md#SP_mon_host_override](../../../config/global/mon.md#SP_mon_host_override) |

**کارکرد:** Monitor(s) to use overriding the MonMap

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_host_override "example"
ceph config get mon mon_host_override
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_host_override
ceph -s
ceph mon stat
```

---

### mon_initial_members

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [mon.md#SP_mon_initial_members](../../../config/global/mon.md#SP_mon_initial_members) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_initial_members "example"
ceph config get mon mon_initial_members
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_initial_members
ceph -s
ceph mon stat
```

---

### mon_inject_pg_merge_bounce_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_inject_pg_merge_bounce_probability](../../../config/global/mon.md#SP_mon_inject_pg_merge_bounce_probability) |

**کارکرد:** Probability of failing and reverting a pg_num decrement

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_inject_pg_merge_bounce_probability 0
ceph config get mon mon_inject_pg_merge_bounce_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_inject_sync_get_chunk_delay

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_inject_sync_get_chunk_delay](../../../config/global/mon.md#SP_mon_inject_sync_get_chunk_delay) |

**کارکرد:** Inject delay during Monitor sync (seconds)

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_inject_sync_get_chunk_delay 0
ceph config get mon mon_inject_sync_get_chunk_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_inject_transaction_delay_max

| | |
|---|---|
| نوع | Float · default `10` · **Dev** |
| جدول | [mon.md#SP_mon_inject_transaction_delay_max](../../../config/global/mon.md#SP_mon_inject_transaction_delay_max) |

**کارکرد:** Max duration of injected delay in Paxos

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_inject_transaction_delay_max 10
ceph config get mon mon_inject_transaction_delay_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`10`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_inject_transaction_delay_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_inject_transaction_delay_probability](../../../config/global/mon.md#SP_mon_inject_transaction_delay_probability) |

**کارکرد:** Probability of injecting a delay in Paxos

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_inject_transaction_delay_probability 0
ceph config get mon mon_inject_transaction_delay_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_keyvaluedb

| | |
|---|---|
| نوع | Str · enum: ["rocksdb"] · default `rocksdb` · **Advanced** |
| جدول | [mon.md#SP_mon_keyvaluedb](../../../config/global/mon.md#SP_mon_keyvaluedb) |

**کارکرد:** Database backend to use for the Monitor database

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_keyvaluedb rocksdb
ceph config get mon mon_keyvaluedb
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `rocksdb`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_keyvaluedb
ceph -s
ceph mon stat
```

---

### mon_max_log_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_max_log_epochs](../../../config/global/mon.md#SP_mon_max_log_epochs) |

**کارکرد:** Max number of past cluster log epochs to store

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_log_epochs 500
ceph config get mon mon_max_log_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_log_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mdsmap_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_max_mdsmap_epochs](../../../config/global/mon.md#SP_mon_max_mdsmap_epochs) |

**کارکرد:** Max number of FSMaps/MDSMaps to store

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_mdsmap_epochs 500
ceph config get mon mon_max_mdsmap_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_mdsmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mgrmap_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_max_mgrmap_epochs](../../../config/global/mon.md#SP_mon_max_mgrmap_epochs) |

**کارکرد:** Max number of MgrMaps to store

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_mgrmap_epochs 500
ceph config get mon mon_max_mgrmap_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_mgrmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_nvmeof_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_max_nvmeof_epochs](../../../config/global/mon.md#SP_mon_max_nvmeof_epochs) |

**کارکرد:** Max number of NVMeoF gateway maps to store

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_nvmeof_epochs 500
ceph config get mon mon_max_nvmeof_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_nvmeof_epochs
ceph -s
ceph mon stat
```

---

### mon_max_osd

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [mon.md#SP_mon_max_osd](../../../config/global/mon.md#SP_mon_max_osd) |

**کارکرد:** Max number of OSDs in a cluster

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_osd 10000
ceph config get mon mon_max_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_osd
ceph -s
ceph mon stat
```

---

### mon_max_pg_per_osd

| | |
|---|---|
| نوع | Uint · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_max_pg_per_osd](../../../config/global/mon.md#SP_mon_max_pg_per_osd) |

**کارکرد:** Max number of PGs per OSD the cluster will allow

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_pg_per_osd 500
ceph config get mon mon_max_pg_per_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_max_snap_prune_per_epoch

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [mon.md#SP_mon_max_snap_prune_per_epoch](../../../config/global/mon.md#SP_mon_max_snap_prune_per_epoch) |

**کارکرد:** Max number of pruned snaps we will process in a single OSDMap epoch

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_max_snap_prune_per_epoch 100
ceph config get mon mon_max_snap_prune_per_epoch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_max_snap_prune_per_epoch
ceph -s
ceph mon stat
```

---

### mon_min_osdmap_epochs

| | |
|---|---|
| نوع | Int · default `500` · **Advanced** |
| جدول | [mon.md#SP_mon_min_osdmap_epochs](../../../config/global/mon.md#SP_mon_min_osdmap_epochs) |

**کارکرد:** Min number of OSDMaps to store

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_min_osdmap_epochs 500
ceph config get mon mon_min_osdmap_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `500`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_min_osdmap_epochs
ceph -s
ceph mon stat
```

---

### mon_osd_backfillfull_ratio

| | |
|---|---|
| نوع | Float · default `0.9` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_backfillfull_ratio](../../../config/global/mon.md#SP_mon_osd_backfillfull_ratio) |

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_osd_backfillfull_ratio 0.9
ceph config get mon mon_osd_backfillfull_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.9`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_backfillfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_force_trim_to

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_osd_force_trim_to](../../../config/global/mon.md#SP_mon_osd_force_trim_to) |

**کارکرد:** Force Monitors to trim osdmaps through this epoch

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_osd_force_trim_to 64
ceph config get mon mon_osd_force_trim_to
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_osd_full_ratio

| | |
|---|---|
| نوع | Float · default `0.95` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_full_ratio](../../../config/global/mon.md#SP_mon_osd_full_ratio) |

**کارکرد:** Full ratio of OSDs to be set during initial creation of the cluster

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_osd_full_ratio 0.95
ceph config get mon mon_osd_full_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.95`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_full_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_initial_require_min_compat_client

| | |
|---|---|
| نوع | Str · default `luminous` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_initial_require_min_compat_client](../../../config/global/mon.md#SP_mon_osd_initial_require_min_compat_client) |

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_initial_require_min_compat_client luminous
ceph config get mon mon_osd_initial_require_min_compat_client
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `luminous`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_initial_require_min_compat_client
ceph -s
ceph mon stat
```

---

### mon_osd_min_down_reporters

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_min_down_reporters](../../../config/global/mon.md#SP_mon_osd_min_down_reporters) |

**کارکرد:** Number of OSDs from different subtrees who need to report a down OSD for it to count

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_osd_min_down_reporters 2
ceph config get mon mon_osd_min_down_reporters
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_min_down_reporters
ceph -s
ceph mon stat
```

---

### mon_osd_nearfull_ratio

| | |
|---|---|
| نوع | Float · default `0.85` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_nearfull_ratio](../../../config/global/mon.md#SP_mon_osd_nearfull_ratio) |

**کارکرد:** Nearfull ratio for OSDs to be set during initial creation of cluster

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_osd_nearfull_ratio 0.85
ceph config get mon mon_osd_nearfull_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.85`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_nearfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_report_timeout

| | |
|---|---|
| نوع | Int · default `15_min` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_report_timeout](../../../config/global/mon.md#SP_mon_osd_report_timeout) |

**کارکرد:** Time before OSDs who do not report to the mons are marked down (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_osd_report_timeout 15_min
ceph config get mon mon_osd_report_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `15_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_report_timeout
ceph -s
ceph mon stat
```

---

### mon_osd_reporter_subtree_level

| | |
|---|---|
| نوع | Str · default `host` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_reporter_subtree_level](../../../config/global/mon.md#SP_mon_osd_reporter_subtree_level) |

**کارکرد:** At which level of parent bucket the reporters are counted

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_osd_reporter_subtree_level host
ceph config get mon mon_osd_reporter_subtree_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `host`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_reporter_subtree_level
ceph -s
ceph mon stat
```

---

### mon_osd_snap_trim_queue_warn_on

| | |
|---|---|
| نوع | Int · default `32768` · **Advanced** |
| جدول | [mon.md#SP_mon_osd_snap_trim_queue_warn_on](../../../config/global/mon.md#SP_mon_osd_snap_trim_queue_warn_on) |

**کارکرد:** Warn when snap trim queue reaches or exceeds this value

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_osd_snap_trim_queue_warn_on 32768
ceph config get mon mon_osd_snap_trim_queue_warn_on
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `32768`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_osd_snap_trim_queue_warn_on
ceph -s
ceph mon stat
```

---

### mon_probe_timeout

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mon.md#SP_mon_probe_timeout](../../../config/global/mon.md#SP_mon_probe_timeout) |

**کارکرد:** Timeout for querying other mons during bootstrap pre-election phase (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_probe_timeout 2
ceph config get mon mon_probe_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_probe_timeout
ceph -s
ceph mon stat
```

---

### mon_scrub_inject_crc_mismatch

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_scrub_inject_crc_mismatch](../../../config/global/mon.md#SP_mon_scrub_inject_crc_mismatch) |

**کارکرد:** Probability for injecting crc mismatches into mon scrub

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_scrub_inject_crc_mismatch 0
ceph config get mon mon_scrub_inject_crc_mismatch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_scrub_inject_missing_keys

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_scrub_inject_missing_keys](../../../config/global/mon.md#SP_mon_scrub_inject_missing_keys) |

**کارکرد:** Probability for injecting missing keys into mon scrub

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_scrub_inject_missing_keys 0
ceph config get mon mon_scrub_inject_missing_keys
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_scrub_interval

| | |
|---|---|
| نوع | Secs · default `1_day` · **Advanced** |
| جدول | [mon.md#SP_mon_scrub_interval](../../../config/global/mon.md#SP_mon_scrub_interval) |

**کارکرد:** Frequency for scrubbing the Monitor database

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_scrub_interval 1_day
ceph config get mon mon_scrub_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_day`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_scrub_interval
ceph -s
ceph mon stat
```

---

### mon_scrub_max_keys

| | |
|---|---|
| نوع | Int · default `100` · **Advanced** |
| جدول | [mon.md#SP_mon_scrub_max_keys](../../../config/global/mon.md#SP_mon_scrub_max_keys) |

**کارکرد:** Max keys per on scrub chunk/step

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_scrub_max_keys 100
ceph config get mon mon_scrub_max_keys
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `100`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_scrub_max_keys
ceph -s
ceph mon stat
```

---

### mon_scrub_timeout

| | |
|---|---|
| نوع | Int · default `5_min` · **Advanced** |
| جدول | [mon.md#SP_mon_scrub_timeout](../../../config/global/mon.md#SP_mon_scrub_timeout) |

**کارکرد:** Timeout to restart scrub of mon quorum participant does not respond for the latest chunk

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_scrub_timeout 5_min
ceph config get mon mon_scrub_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_scrub_timeout
ceph -s
ceph mon stat
```

---

### mon_sync_debug

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mon.md#SP_mon_sync_debug](../../../config/global/mon.md#SP_mon_sync_debug) |

**کارکرد:** Enable extra debugging during mon sync

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_sync_debug true
ceph config get mon mon_sync_debug
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`False`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_sync_max_payload_keys

| | |
|---|---|
| نوع | Int · default `2000` · **Advanced** |
| جدول | [mon.md#SP_mon_sync_max_payload_keys](../../../config/global/mon.md#SP_mon_sync_max_payload_keys) |

**کارکرد:** Target max keys in message payload for Monitor sync

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_sync_max_payload_keys 2000
ceph config get mon mon_sync_max_payload_keys
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `2000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_sync_max_payload_keys
ceph -s
ceph mon stat
```

---

### mon_sync_max_payload_size

| | |
|---|---|
| نوع | Size · default `1_M` · **Advanced** |
| جدول | [mon.md#SP_mon_sync_max_payload_size](../../../config/global/mon.md#SP_mon_sync_max_payload_size) |

**کارکرد:** Target max message payload for mon sync

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mon mon_sync_max_payload_size 1_M
ceph config get mon mon_sync_max_payload_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_sync_max_payload_size
ceph -s
ceph mon stat
```

---

### mon_sync_provider_kill_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_sync_provider_kill_at](../../../config/global/mon.md#SP_mon_sync_provider_kill_at) |

**کارکرد:** Kill mon sync provider at specific point

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_sync_provider_kill_at 64
ceph config get mon mon_sync_provider_kill_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_sync_requester_kill_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mon.md#SP_mon_sync_requester_kill_at](../../../config/global/mon.md#SP_mon_sync_requester_kill_at) |

**کارکرد:** Kill mon sync requestor at specific point

**زمان استفاده:** فقط برای توسعه، تست یا دیباگ upstream — نه برای تنظیم production.

**مثال:**

```bash
ceph config set mon mon_sync_requester_kill_at 64
ceph config get mon mon_sync_requester_kill_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Dev

1. پیش‌فرض upstream (`0`) را در production نگه دارید.
2. فقط در lab هنگام بازتولید issue مشخص تغییر دهید.
3. قبل از بازگرداندن نود به pool production برگردانید.

---

### mon_sync_timeout

| | |
|---|---|
| نوع | Float · default `1_min` · **Advanced** |
| جدول | [mon.md#SP_mon_sync_timeout](../../../config/global/mon.md#SP_mon_sync_timeout) |

**کارکرد:** Timeout before canceling sync if syncing mon does not respond

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mon mon_sync_timeout 1_min
ceph config get mon mon_sync_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_sync_timeout
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim) |

**کارکرد:** Raise the AUTH_INSECURE_GLOBAL_ID_RECLAIM health warning if any connected clients are insecurely reclaiming global_ids

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim false
ceph config get mon mon_warn_on_insecure_global_id_reclaim
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim_allowed

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed) |

**کارکرد:** issue AUTH_INSECURE_GLOBAL_ID_RECLAIM_ALLOWED health warning if insecure global_id reclaim is allowed

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim_allowed false
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
ceph -s
ceph mon stat
```

---

### mon_warn_on_msgr2_not_enabled

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_msgr2_not_enabled](../../../config/global/mon.md#SP_mon_warn_on_msgr2_not_enabled) |

**کارکرد:** Raise the MON_MSGR2_NOT_ENABLED health warning if monitors are all running Nautilus but not all binding to a msgr2 port

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mon mon_warn_on_msgr2_not_enabled false
ceph config get mon mon_warn_on_msgr2_not_enabled
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_msgr2_not_enabled
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_ratio

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_slow_ping_ratio](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_ratio) |

**کارکرد:** Issue a health warning if heartbeat ping longer than percentage of osd_heartbeat_grace

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_warn_on_slow_ping_ratio 0.05
ceph config get mon mon_warn_on_slow_ping_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_slow_ping_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_time

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_on_slow_ping_time](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_time) |

**کارکرد:** Override mon_warn_on_slow_ping_ratio with specified threshold in milliseconds

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_warn_on_slow_ping_time 0
ceph config get mon mon_warn_on_slow_ping_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_on_slow_ping_time
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_deep_scrubbed_ratio

| | |
|---|---|
| نوع | Float · default `0.75` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio) |

**کارکرد:** Percentage of the deep scrub interval past the deep scrub interval to warn - Set this configurable with the command "ceph config set mgr mon_warn_pg_not_deep_scrubbed_ratio <ratio_value>"

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_warn_pg_not_deep_scrubbed_ratio 0.75
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.75`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_scrubbed_ratio

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [mon.md#SP_mon_warn_pg_not_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_scrubbed_ratio) |

**کارکرد:** Raise a health warning when shallow scrubs are delayed by this percentage of the shallow scrub interval. Note that this must be set at mgr or with global scope. Set this configurable with the command "ceph config set mgr mon_warn_pg_not_scrubbed_ratio <ratio_value>".

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set mon mon_warn_pg_not_scrubbed_ratio 0.5
ceph config get mon mon_warn_pg_not_scrubbed_ratio
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.

**محدوده:** حداقل `0`، حداکثر `—`.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get mon mon_warn_pg_not_scrubbed_ratio
ceph -s
ceph mon stat
```

---


[← نمای کلی](../OVERVIEW.md)
