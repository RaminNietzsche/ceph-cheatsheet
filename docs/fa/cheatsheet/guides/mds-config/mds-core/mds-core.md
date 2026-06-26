# Metadata server core

راهنمای عمیق پیکربندی MDS — 138 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [mds_abort_on_newly_corrupt_dentry](#mds_abort_on_newly_corrupt_dentry) | `True` | Advanced | عملکرد |
| [mds_action_on_write_error](#mds_action_on_write_error) | `1` | Advanced | عملکرد |
| [mds_allow_async_dirops](#mds_allow_async_dirops) | `True` | Advanced | سیاست |
| [mds_allow_batched_ops](#mds_allow_batched_ops) | `True` | Advanced | سیاست |
| [mds_alternate_name_max](#mds_alternate_name_max) | `8_K` | Advanced | عملکرد |
| [mds_asio_thread_count](#mds_asio_thread_count) | `2` | Advanced | عملکرد |
| [mds_bal_export_pin](#mds_bal_export_pin) | `True` | Advanced | عملکرد |
| [mds_bal_fragment_dirs](#mds_bal_fragment_dirs) | `True` | Advanced | عملکرد |
| [mds_bal_fragment_fast_factor](#mds_bal_fragment_fast_factor) | `1.5` | Advanced | عملکرد |
| [mds_bal_fragment_size_max](#mds_bal_fragment_size_max) | `100000` | Advanced | عملکرد |
| [mds_bal_idle_threshold](#mds_bal_idle_threshold) | `0` | Advanced | عملکرد |
| [mds_bal_max](#mds_bal_max) | `-1` | Dev | توسعه |
| [mds_bal_max_until](#mds_bal_max_until) | `-1` | Dev | توسعه |
| [mds_bal_merge_size](#mds_bal_merge_size) | `50` | Advanced | عملکرد |
| [mds_bal_midchunk](#mds_bal_midchunk) | `0.3` | Dev | توسعه |
| [mds_bal_min_rebalance](#mds_bal_min_rebalance) | `0.1` | Dev | توسعه |
| [mds_bal_min_start](#mds_bal_min_start) | `0.2` | Dev | توسعه |
| [mds_bal_minchunk](#mds_bal_minchunk) | `0.001` | Dev | توسعه |
| [mds_bal_mode](#mds_bal_mode) | `0` | Dev | توسعه |
| [mds_bal_need_max](#mds_bal_need_max) | `1.2` | Dev | توسعه |
| [mds_bal_need_min](#mds_bal_need_min) | `0.8` | Dev | توسعه |
| [mds_bal_overload_epochs](#mds_bal_overload_epochs) | `2` | Dev | توسعه |
| [mds_bal_replicate_threshold](#mds_bal_replicate_threshold) | `8000` | Advanced | عملکرد |
| [mds_bal_split_bits](#mds_bal_split_bits) | `3` | Advanced | عملکرد |
| [mds_bal_split_rd](#mds_bal_split_rd) | `25000` | Advanced | عملکرد |
| [mds_bal_split_size](#mds_bal_split_size) | `10000` | Advanced | عملکرد |
| [mds_bal_split_wr](#mds_bal_split_wr) | `10000` | Advanced | عملکرد |
| [mds_bal_target_decay](#mds_bal_target_decay) | `10` | Advanced | عملکرد |
| [mds_bal_unreplicate_threshold](#mds_bal_unreplicate_threshold) | `0` | Advanced | عملکرد |
| [mds_beacon_grace](#mds_beacon_grace) | `15` | Advanced | عملکرد |
| [mds_cache_memory_limit](#mds_cache_memory_limit) | `4_G` | Basic | عملکرد |
| [mds_cache_mid](#mds_cache_mid) | `0.7` | Advanced | عملکرد |
| [mds_cache_quiesce_decay_rate](#mds_cache_quiesce_decay_rate) | `1` | Advanced | عملکرد |
| [mds_cache_quiesce_delay](#mds_cache_quiesce_delay) | `0` | Dev | توسعه |
| [mds_cache_quiesce_sleep](#mds_cache_quiesce_sleep) | `200` | Advanced | عملکرد |
| [mds_cache_quiesce_threshold](#mds_cache_quiesce_threshold) | `512_K` | Advanced | عملکرد |
| [mds_cache_reservation](#mds_cache_reservation) | `0.05` | Advanced | عملکرد |
| [mds_cache_trim_decay_rate](#mds_cache_trim_decay_rate) | `1` | Advanced | عملکرد |
| [mds_cache_trim_threshold](#mds_cache_trim_threshold) | `256_K` | Advanced | عملکرد |
| [mds_client_delegate_inos_pct](#mds_client_delegate_inos_pct) | `50` | Advanced | عملکرد |
| [mds_client_prealloc_inos](#mds_client_prealloc_inos) | `1000` | Advanced | عملکرد |
| [mds_client_writeable_range_max_inc_objs](#mds_client_writeable_range_max_inc_objs) | `1_K` | Advanced | عملکرد |
| [mds_connect_bootstrapping](#mds_connect_bootstrapping) | `False` | Dev | توسعه |
| [mds_damage_table_max_entries](#mds_damage_table_max_entries) | `10000` | Advanced | عملکرد |
| [mds_data](#mds_data) | `/var/lib/ceph/mds/$cluster-$id` | Advanced | عملکرد |
| [mds_decay_halflife](#mds_decay_halflife) | `5` | Advanced | عملکرد |
| [mds_default_dir_hash](#mds_default_dir_hash) | `2` | Advanced | عملکرد |
| [mds_defer_session_stale](#mds_defer_session_stale) | `True` | Dev | توسعه |
| [mds_delay_journal_replay_for_testing](#mds_delay_journal_replay_for_testing) | `0` | Dev | توسعه |
| [mds_deny_all_reconnect](#mds_deny_all_reconnect) | `False` | Advanced | عملکرد |
| [mds_dir_keys_per_op](#mds_dir_keys_per_op) | `16384` | Advanced | عملکرد |
| [mds_dir_max_commit_size](#mds_dir_max_commit_size) | `10` | Advanced | عملکرد |
| [mds_dir_max_entries](#mds_dir_max_entries) | `0` | Advanced | عملکرد |
| [mds_dir_prefetch](#mds_dir_prefetch) | `True` | Advanced | عملکرد |
| [mds_dump_cache_after_rejoin](#mds_dump_cache_after_rejoin) | `False` | Dev | توسعه |
| [mds_dump_cache_on_map](#mds_dump_cache_on_map) | `False` | Dev | توسعه |
| [mds_dump_cache_threshold_file](#mds_dump_cache_threshold_file) | `0` | Dev | توسعه |
| [mds_dump_cache_threshold_formatter](#mds_dump_cache_threshold_formatter) | `1_G` | Dev | توسعه |
| [mds_early_reply](#mds_early_reply) | `True` | Advanced | عملکرد |
| [mds_enable_op_tracker](#mds_enable_op_tracker) | `True` | Advanced | سیاست |
| [mds_enforce_unique_name](#mds_enforce_unique_name) | `True` | Advanced | سیاست |
| [mds_export_ephemeral_distributed](#mds_export_ephemeral_distributed) | `True` | Advanced | عملکرد |
| [mds_export_ephemeral_distributed_factor](#mds_export_ephemeral_distributed_factor) | `2` | Advanced | عملکرد |
| [mds_export_ephemeral_random](#mds_export_ephemeral_random) | `True` | Advanced | عملکرد |
| [mds_export_ephemeral_random_max](#mds_export_ephemeral_random_max) | `0.01` | Advanced | عملکرد |
| [mds_file_blockdiff_max_concurrent_object_scans](#mds_file_blockdiff_max_concurrent_object_scans) | `16` | Advanced | عملکرد |
| [mds_fscrypt_last_block_max_size](#mds_fscrypt_last_block_max_size) | `4_K` | Advanced | عملکرد |
| [mds_go_bad_corrupt_dentry](#mds_go_bad_corrupt_dentry) | `True` | Advanced | عملکرد |
| [mds_hack_allow_loading_invalid_metadata](#mds_hack_allow_loading_invalid_metadata) | `False` | Advanced | سیاست |
| [mds_health_cache_threshold](#mds_health_cache_threshold) | `1.5` | Advanced | عملکرد |
| [mds_health_summarize_threshold](#mds_health_summarize_threshold) | `10` | Advanced | عملکرد |
| [mds_heartbeat_grace](#mds_heartbeat_grace) | `15` | Advanced | عملکرد |
| [mds_heartbeat_reset_grace](#mds_heartbeat_reset_grace) | `1000` | Advanced | عملکرد |
| [mds_join_fs](#mds_join_fs) | `(empty)` | Basic | سیاست |
| [mds_journal_format](#mds_journal_format) | `1` | Dev | توسعه |
| [mds_kill_create_at](#mds_kill_create_at) | `0` | Dev | توسعه |
| [mds_kill_dirfrag_at](#mds_kill_dirfrag_at) | `0` | Dev | توسعه |
| [mds_kill_export_at](#mds_kill_export_at) | `0` | Dev | توسعه |
| [mds_kill_import_at](#mds_kill_import_at) | `0` | Dev | توسعه |
| [mds_kill_journal_at](#mds_kill_journal_at) | `0` | Dev | توسعه |
| [mds_kill_journal_expire_at](#mds_kill_journal_expire_at) | `0` | Dev | توسعه |
| [mds_kill_journal_replay_at](#mds_kill_journal_replay_at) | `0` | Dev | توسعه |
| [mds_kill_link_at](#mds_kill_link_at) | `0` | Dev | توسعه |
| [mds_kill_mdstable_at](#mds_kill_mdstable_at) | `0` | Dev | توسعه |
| [mds_kill_openc_at](#mds_kill_openc_at) | `0` | Dev | توسعه |
| [mds_kill_rename_at](#mds_kill_rename_at) | `0` | Dev | توسعه |
| [mds_kill_shutdown_at](#mds_kill_shutdown_at) | `0` | Dev | توسعه |
| [mds_max_completed_flushes](#mds_max_completed_flushes) | `100000` | Dev | توسعه |
| [mds_max_completed_requests](#mds_max_completed_requests) | `100000` | Dev | توسعه |
| [mds_max_export_size](#mds_max_export_size) | `20_M` | Dev | توسعه |
| [mds_max_file_recover](#mds_max_file_recover) | `32` | Advanced | عملکرد |
| [mds_max_purge_files](#mds_max_purge_files) | `64` | Advanced | عملکرد |
| [mds_max_purge_ops](#mds_max_purge_ops) | `8_K` | Advanced | عملکرد |
| [mds_max_purge_ops_per_pg](#mds_max_purge_ops_per_pg) | `0.5` | Advanced | عملکرد |
| [mds_max_scrub_ops_in_progress](#mds_max_scrub_ops_in_progress) | `5` | Advanced | عملکرد |
| [mds_max_snaps_per_dir](#mds_max_snaps_per_dir) | `100` | Advanced | ظرفیت |
| [mds_numa_node](#mds_numa_node) | `-1` | Advanced | عملکرد |
| [mds_oft_prefetch_dirfrags](#mds_oft_prefetch_dirfrags) | `False` | Advanced | عملکرد |
| [mds_op_complaint_time](#mds_op_complaint_time) | `30` | Advanced | عملکرد |
| [mds_op_history_duration](#mds_op_history_duration) | `600` | Advanced | عملکرد |
| [mds_op_history_size](#mds_op_history_size) | `20` | Advanced | عملکرد |
| [mds_op_history_slow_op_size](#mds_op_history_slow_op_size) | `20` | Advanced | عملکرد |
| [mds_op_history_slow_op_threshold](#mds_op_history_slow_op_threshold) | `10` | Advanced | عملکرد |
| [mds_ping_grace](#mds_ping_grace) | `15` | Advanced | عملکرد |
| [mds_purge_queue_busy_flush_period](#mds_purge_queue_busy_flush_period) | `1` | Dev | توسعه |
| [mds_recall_global_max_decay_threshold](#mds_recall_global_max_decay_threshold) | `128_K` | Advanced | عملکرد |
| [mds_recall_max_decay_rate](#mds_recall_max_decay_rate) | `1.5` | Advanced | عملکرد |
| [mds_recall_max_decay_threshold](#mds_recall_max_decay_threshold) | `128_K` | Advanced | عملکرد |
| [mds_recall_warning_decay_rate](#mds_recall_warning_decay_rate) | `60` | Advanced | عملکرد |
| [mds_recall_warning_threshold](#mds_recall_warning_threshold) | `256_K` | Advanced | عملکرد |
| [mds_replay_unsafe_with_closed_session](#mds_replay_unsafe_with_closed_session) | `False` | Advanced | عملکرد |
| [mds_request_load_average_decay_rate](#mds_request_load_average_decay_rate) | `1_min` | Advanced | عملکرد |
| [mds_root_ino_gid](#mds_root_ino_gid) | `0` | Advanced | عملکرد |
| [mds_root_ino_uid](#mds_root_ino_uid) | `0` | Advanced | عملکرد |
| [mds_scrub_stats_review_period](#mds_scrub_stats_review_period) | `1` | Advanced | عملکرد |
| [mds_server_dispatch_client_request_delay](#mds_server_dispatch_client_request_delay) | `0` | Dev | توسعه |
| [mds_server_dispatch_killpoint_random](#mds_server_dispatch_killpoint_random) | `0.0` | Dev | توسعه |
| [mds_session_blocklist_on_evict](#mds_session_blocklist_on_evict) | `True` | Advanced | عملکرد |
| [mds_session_cache_liveness_decay_rate](#mds_session_cache_liveness_decay_rate) | `5_min` | Advanced | عملکرد |
| [mds_session_cache_liveness_magnitude](#mds_session_cache_liveness_magnitude) | `10` | Advanced | عملکرد |
| [mds_session_metadata_threshold](#mds_session_metadata_threshold) | `16_M` | Advanced | عملکرد |
| [mds_sessionmap_keys_per_op](#mds_sessionmap_keys_per_op) | `1_K` | Advanced | عملکرد |
| [mds_shutdown_check](#mds_shutdown_check) | `0` | Dev | توسعه |
| [mds_skip_ino](#mds_skip_ino) | `0` | Dev | توسعه |
| [mds_sleep_rank_change](#mds_sleep_rank_change) | `0.0` | Dev | توسعه |
| [mds_snap_max_uid](#mds_snap_max_uid) | `4294967294` | Advanced | عملکرد |
| [mds_snap_min_uid](#mds_snap_min_uid) | `0` | Advanced | عملکرد |
| [mds_snap_rstat](#mds_snap_rstat) | `False` | Advanced | عملکرد |
| [mds_standby_replay_damaged](#mds_standby_replay_damaged) | `False` | Dev | توسعه |
| [mds_symlink_recovery](#mds_symlink_recovery) | `True` | Advanced | عملکرد |
| [mds_thrash_exports](#mds_thrash_exports) | `0` | Dev | توسعه |
| [mds_thrash_fragments](#mds_thrash_fragments) | `0` | Dev | توسعه |
| [mds_use_global_snaprealm_seq_for_subvol](#mds_use_global_snaprealm_seq_for_subvol) | `True` | Advanced | عملکرد |
| [mds_valgrind_exit](#mds_valgrind_exit) | `False` | Dev | توسعه |
| [mds_verify_backtrace](#mds_verify_backtrace) | `1` | Dev | توسعه |
| [mds_verify_scatter](#mds_verify_scatter) | `False` | Dev | توسعه |
| [mds_wipe_ino_prealloc](#mds_wipe_ino_prealloc) | `False` | Dev | توسعه |
| [mds_wipe_sessions](#mds_wipe_sessions) | `False` | Dev | توسعه |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_abort_on_newly_corrupt_dentry

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_abort_on_newly_corrupt_dentry](../../../config/mds/mds.md#SP_mds_abort_on_newly_corrupt_dentry) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_abort_on_newly_corrupt_dentry false
ceph config get mds mds_abort_on_newly_corrupt_dentry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_abort_on_newly_corrupt_dentry
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_action_on_write_error

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_action_on_write_error](../../../config/mds/mds.md#SP_mds_action_on_write_error) |

**کارکرد:** action to take when MDS cannot write to RADOS (0:ignore, 1:read-only, 2:suicide)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_action_on_write_error 1
ceph config get mds mds_action_on_write_error
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_action_on_write_error
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_allow_async_dirops

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_allow_async_dirops](../../../config/mds/mds.md#SP_mds_allow_async_dirops) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_allow_async_dirops false
ceph config get mds mds_allow_async_dirops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_allow_async_dirops
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_allow_batched_ops

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_allow_batched_ops](../../../config/mds/mds.md#SP_mds_allow_batched_ops) |

**کارکرد:** allow MDS to batch lookup/getattr RPCs The MDS will batch a lookup or getattr RPC on the same inode when possible to avoid repetitive locks on metadata and to bypass other requests acquiring write locks. Generally, this should only improve performance but this switch exists to provide a means to turn this behavior off for comparison.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_allow_batched_ops false
ceph config get mds mds_allow_batched_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_allow_batched_ops
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_alternate_name_max

| | |
|---|---|
| نوع | Size · default `8_K` · **Advanced** |
| جدول | [mds.md#SP_mds_alternate_name_max](../../../config/mds/mds.md#SP_mds_alternate_name_max) |

**کارکرد:** Set the maximum length of alternate names for dentries

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_alternate_name_max 8_K
ceph config get mds mds_alternate_name_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_alternate_name_max
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_asio_thread_count

| | |
|---|---|
| نوع | Uint · default `2` · **Advanced** |
| جدول | [mds.md#SP_mds_asio_thread_count](../../../config/mds/mds.md#SP_mds_asio_thread_count) |

**کارکرد:** Size of thread pool for ASIO completions

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_asio_thread_count 2
ceph config get mds mds_asio_thread_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_asio_thread_count
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_export_pin

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_export_pin](../../../config/mds/mds.md#SP_mds_bal_export_pin) |

**کارکرد:** allow setting directory export pins to particular ranks

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_bal_export_pin false
ceph config get mds mds_bal_export_pin
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_export_pin
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_fragment_dirs

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_fragment_dirs](../../../config/mds/mds.md#SP_mds_bal_fragment_dirs) |

**کارکرد:** enable directory fragmentation Directory fragmentation is a standard feature of CephFS that allows sharding directories across multiple objects for performance and stability. Additionally, this allows fragments to be distributed across multiple active MDSs to increase throughput. Disabling (new) fragmentation should only be done in exceptional circumstances and may lead to performance issues.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_bal_fragment_dirs false
ceph config get mds mds_bal_fragment_dirs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_fragment_dirs
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_fragment_fast_factor

| | |
|---|---|
| نوع | Float · default `1.5` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_fragment_fast_factor](../../../config/mds/mds.md#SP_mds_bal_fragment_fast_factor) |

**کارکرد:** ratio of mds_bal_split_size at which fast fragment splitting occurs

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_fragment_fast_factor 1.5
ceph config get mds mds_bal_fragment_fast_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_fragment_fast_factor
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_fragment_size_max

| | |
|---|---|
| نوع | Int · default `100000` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_fragment_size_max](../../../config/mds/mds.md#SP_mds_bal_fragment_size_max) |

**کارکرد:** maximum size of a directory fragment before new creat/links fail

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_fragment_size_max 100000
ceph config get mds mds_bal_fragment_size_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_fragment_size_max
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_idle_threshold

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_idle_threshold](../../../config/mds/mds.md#SP_mds_bal_idle_threshold) |

**کارکرد:** idle metadata popularity threshold before rebalancing

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_idle_threshold 0
ceph config get mds mds_bal_idle_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_idle_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_max

| | |
|---|---|
| نوع | Int · default `-1` · **Dev** |
| جدول | [mds.md#SP_mds_bal_max](../../../config/mds/mds.md#SP_mds_bal_max) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_max 128
ceph config get mds mds_bal_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`-1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_max_until

| | |
|---|---|
| نوع | Int · default `-1` · **Dev** |
| جدول | [mds.md#SP_mds_bal_max_until](../../../config/mds/mds.md#SP_mds_bal_max_until) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_max_until 128
ceph config get mds mds_bal_max_until
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`-1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_merge_size

| | |
|---|---|
| نوع | Int · default `50` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_merge_size](../../../config/mds/mds.md#SP_mds_bal_merge_size) |

**کارکرد:** size of fragments where merging should occur

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_merge_size 50
ceph config get mds mds_bal_merge_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_merge_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_midchunk

| | |
|---|---|
| نوع | Float · default `0.3` · **Dev** |
| جدول | [mds.md#SP_mds_bal_midchunk](../../../config/mds/mds.md#SP_mds_bal_midchunk) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_midchunk 0.3
ceph config get mds mds_bal_midchunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.3`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_min_rebalance

| | |
|---|---|
| نوع | Float · default `0.1` · **Dev** |
| جدول | [mds.md#SP_mds_bal_min_rebalance](../../../config/mds/mds.md#SP_mds_bal_min_rebalance) |

**کارکرد:** amount overloaded over internal target before balancer begins offloading

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_min_rebalance 0.1
ceph config get mds mds_bal_min_rebalance
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_min_start

| | |
|---|---|
| نوع | Float · default `0.2` · **Dev** |
| جدول | [mds.md#SP_mds_bal_min_start](../../../config/mds/mds.md#SP_mds_bal_min_start) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_min_start 0.2
ceph config get mds mds_bal_min_start
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_minchunk

| | |
|---|---|
| نوع | Float · default `0.001` · **Dev** |
| جدول | [mds.md#SP_mds_bal_minchunk](../../../config/mds/mds.md#SP_mds_bal_minchunk) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_minchunk 0.001
ceph config get mds mds_bal_minchunk
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.001`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_mode

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_bal_mode](../../../config/mds/mds.md#SP_mds_bal_mode) |

**کارکرد:** MDS subtree balancer mode (`none`, `normal`, `aggressive`). Controls how aggressively metadata load is migrated between active MDS ranks.

**زمان استفاده:** Use `normal` for multi-active CephFS; `none` for single-MDS or while debugging balance churn.

**مثال:**

```bash
ceph config set mds mds_bal_mode normal
ceph fs status
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_need_max

| | |
|---|---|
| نوع | Float · default `1.2` · **Dev** |
| جدول | [mds.md#SP_mds_bal_need_max](../../../config/mds/mds.md#SP_mds_bal_need_max) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_need_max 1.2
ceph config get mds mds_bal_need_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1.2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_need_min

| | |
|---|---|
| نوع | Float · default `0.8` · **Dev** |
| جدول | [mds.md#SP_mds_bal_need_min](../../../config/mds/mds.md#SP_mds_bal_need_min) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_need_min 0.8
ceph config get mds mds_bal_need_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.8`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_overload_epochs

| | |
|---|---|
| نوع | Int · default `2` · **Dev** |
| جدول | [mds.md#SP_mds_bal_overload_epochs](../../../config/mds/mds.md#SP_mds_bal_overload_epochs) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_bal_overload_epochs 2
ceph config get mds mds_bal_overload_epochs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`2`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_bal_replicate_threshold

| | |
|---|---|
| نوع | Float · default `8000` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_replicate_threshold](../../../config/mds/mds.md#SP_mds_bal_replicate_threshold) |

**کارکرد:** hot popularity threshold to replicate a subtree

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_replicate_threshold 8000
ceph config get mds mds_bal_replicate_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_replicate_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_split_bits

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_split_bits](../../../config/mds/mds.md#SP_mds_bal_split_bits) |

**کارکرد:** power of two child fragments for a fragment on split

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_split_bits 3
ceph config get mds mds_bal_split_bits
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `24`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_split_bits
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_split_rd

| | |
|---|---|
| نوع | Float · default `25000` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_split_rd](../../../config/mds/mds.md#SP_mds_bal_split_rd) |

**کارکرد:** hot read popularity threshold for splitting a directory fragment

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_split_rd 25000
ceph config get mds mds_bal_split_rd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `25000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_split_rd
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_split_size

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_split_size](../../../config/mds/mds.md#SP_mds_bal_split_size) |

**کارکرد:** minimum size of directory fragment before splitting

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_split_size 10000
ceph config get mds mds_bal_split_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_split_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_split_wr

| | |
|---|---|
| نوع | Float · default `10000` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_split_wr](../../../config/mds/mds.md#SP_mds_bal_split_wr) |

**کارکرد:** hot write popularity threshold for splitting a directory fragment

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_split_wr 10000
ceph config get mds mds_bal_split_wr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_split_wr
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_target_decay

| | |
|---|---|
| نوع | Float · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_target_decay](../../../config/mds/mds.md#SP_mds_bal_target_decay) |

**کارکرد:** rate of decay for export targets communicated to clients

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_target_decay 10
ceph config get mds mds_bal_target_decay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_target_decay
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_bal_unreplicate_threshold

| | |
|---|---|
| نوع | Float · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_bal_unreplicate_threshold](../../../config/mds/mds.md#SP_mds_bal_unreplicate_threshold) |

**کارکرد:** cold popularity threshold to merge subtrees

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_bal_unreplicate_threshold 0
ceph config get mds mds_bal_unreplicate_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_bal_unreplicate_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_beacon_grace

| | |
|---|---|
| نوع | Float · default `15` · **Advanced** |
| جدول | [mds.md#SP_mds_beacon_grace](../../../config/mds/mds.md#SP_mds_beacon_grace) |

**کارکرد:** Seconds the monitor waits after a missed MDS beacon before marking the rank laggy/failed.

**زمان استفاده:** Increase during network maintenance; decrease for faster MDS failover at the cost of false positives on slow nodes.

**مثال:**

```bash
ceph config set mds mds_beacon_grace 15
ceph config get mds mds_beacon_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_beacon_grace
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_memory_limit

| | |
|---|---|
| نوع | Size · default `4_G` · **Basic** |
| جدول | [mds.md#SP_mds_cache_memory_limit](../../../config/mds/mds.md#SP_mds_cache_memory_limit) |

**کارکرد:** Soft limit on MDS metadata cache memory (bytes). When exceeded, the MDS trims caps and may evict client sessions.

**زمان استفاده:** Raise for large working sets and many files; lower if MDS RSS causes OOM on constrained nodes.

**مثال:**

```bash
ceph config set mds mds_cache_memory_limit 4_G
ceph config get mds mds_cache_memory_limit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_G`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_memory_limit
ceph -s
ceph fs status
ceph mds stat
```

Watch `ceph fs status`, slow requests, and `mds_cache_trim_*` counters. Size MDS RAM ≥ 2× this limit in production.

---

### mds_cache_mid

| | |
|---|---|
| نوع | Float · default `0.7` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_mid](../../../config/mds/mds.md#SP_mds_cache_mid) |

**کارکرد:** Midpoint for MDS cache LRU

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_mid 0.7
ceph config get mds mds_cache_mid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.7`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_mid
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_quiesce_decay_rate

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_quiesce_decay_rate](../../../config/mds/mds.md#SP_mds_cache_quiesce_decay_rate) |

**کارکرد:** Decay rate for quiescing inodes throttle

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_quiesce_decay_rate 1
ceph config get mds mds_cache_quiesce_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_quiesce_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_quiesce_delay

| | |
|---|---|
| نوع | Millisecs · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_cache_quiesce_delay](../../../config/mds/mds.md#SP_mds_cache_quiesce_delay) |

**کارکرد:** Delay before starting recursive quiesce inode operations

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_cache_quiesce_delay 0
ceph config get mds mds_cache_quiesce_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_cache_quiesce_sleep

| | |
|---|---|
| نوع | Millisecs · default `200` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_quiesce_sleep](../../../config/mds/mds.md#SP_mds_cache_quiesce_sleep) |

**کارکرد:** Sleep time for requests after passing the quiesce threshold

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_cache_quiesce_sleep 200
ceph config get mds mds_cache_quiesce_sleep
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `200`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_quiesce_sleep
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_quiesce_threshold

| | |
|---|---|
| نوع | Size · default `512_K` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_quiesce_threshold](../../../config/mds/mds.md#SP_mds_cache_quiesce_threshold) |

**کارکرد:** Threshold for number of inodes that can be quiesced

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_quiesce_threshold 512_K
ceph config get mds mds_cache_quiesce_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `512_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_quiesce_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_reservation

| | |
|---|---|
| نوع | Float · default `0.05` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_reservation](../../../config/mds/mds.md#SP_mds_cache_reservation) |

**کارکرد:** Amount of memory to reserve for future cached objects

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_reservation 0.05
ceph config get mds mds_cache_reservation
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.05`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_reservation
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_trim_decay_rate

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_trim_decay_rate](../../../config/mds/mds.md#SP_mds_cache_trim_decay_rate) |

**کارکرد:** Decay rate for trimming MDS cache throttle

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_trim_decay_rate 1
ceph config get mds mds_cache_trim_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_trim_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cache_trim_threshold

| | |
|---|---|
| نوع | Size · default `256_K` · **Advanced** |
| جدول | [mds.md#SP_mds_cache_trim_threshold](../../../config/mds/mds.md#SP_mds_cache_trim_threshold) |

**کارکرد:** Threshold for number of dentries that can be trimmed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_cache_trim_threshold 256_K
ceph config get mds mds_cache_trim_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_cache_trim_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_client_delegate_inos_pct

| | |
|---|---|
| نوع | Uint · default `50` · **Advanced** |
| جدول | [mds.md#SP_mds_client_delegate_inos_pct](../../../config/mds/mds.md#SP_mds_client_delegate_inos_pct) |

**کارکرد:** percentage of preallocated inos to delegate to client

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_client_delegate_inos_pct 50
ceph config get mds mds_client_delegate_inos_pct
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `50`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_client_delegate_inos_pct
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_client_prealloc_inos

| | |
|---|---|
| نوع | Int · default `1000` · **Advanced** |
| جدول | [mds.md#SP_mds_client_prealloc_inos](../../../config/mds/mds.md#SP_mds_client_prealloc_inos) |

**کارکرد:** number of unused inodes to pre-allocate to clients for file creation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_client_prealloc_inos 1000
ceph config get mds mds_client_prealloc_inos
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_client_prealloc_inos
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_client_writeable_range_max_inc_objs

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [mds.md#SP_mds_client_writeable_range_max_inc_objs](../../../config/mds/mds.md#SP_mds_client_writeable_range_max_inc_objs) |

**کارکرد:** maximum number of objects in writeable range of a file for a client

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_client_writeable_range_max_inc_objs 1_K
ceph config get mds mds_client_writeable_range_max_inc_objs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_client_writeable_range_max_inc_objs
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_connect_bootstrapping

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_connect_bootstrapping](../../../config/mds/mds.md#SP_mds_connect_bootstrapping) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_connect_bootstrapping true
ceph config get mds mds_connect_bootstrapping
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_damage_table_max_entries

| | |
|---|---|
| نوع | Int · default `10000` · **Advanced** |
| جدول | [mds.md#SP_mds_damage_table_max_entries](../../../config/mds/mds.md#SP_mds_damage_table_max_entries) |

**کارکرد:** maximum number of damage table entries

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_damage_table_max_entries 10000
ceph config get mds mds_damage_table_max_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_damage_table_max_entries
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_data

| | |
|---|---|
| نوع | Str · default `/var/lib/ceph/mds/$cluster-$id` · **Advanced** |
| جدول | [mds.md#SP_mds_data](../../../config/mds/mds.md#SP_mds_data) |

**کارکرد:** Path to MDS data and keyring

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_data "/var/lib/ceph/mds/$cluster-$id"
ceph config get mds mds_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `/var/lib/ceph/mds/$cluster-$id`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_data
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_decay_halflife

| | |
|---|---|
| نوع | Float · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_decay_halflife](../../../config/mds/mds.md#SP_mds_decay_halflife) |

**کارکرد:** Rate of decay for temperature counters on each directory for balancing

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_decay_halflife 5
ceph config get mds mds_decay_halflife
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_decay_halflife
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_default_dir_hash

| | |
|---|---|
| نوع | Int · default `2` · **Advanced** |
| جدول | [mds.md#SP_mds_default_dir_hash](../../../config/mds/mds.md#SP_mds_default_dir_hash) |

**کارکرد:** hash function to select directory fragment for dentry name

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_default_dir_hash 2
ceph config get mds mds_default_dir_hash
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_default_dir_hash
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_defer_session_stale

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [mds.md#SP_mds_defer_session_stale](../../../config/mds/mds.md#SP_mds_defer_session_stale) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_defer_session_stale false
ceph config get mds mds_defer_session_stale
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_delay_journal_replay_for_testing

| | |
|---|---|
| نوع | Millisecs · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_delay_journal_replay_for_testing](../../../config/mds/mds.md#SP_mds_delay_journal_replay_for_testing) |

**کارکرد:** Delay the journal replay to verify the replay time estimate Jorunal replay warning is activated if the mds has been in replay state for more than 30 seconds. This config delays replay for validating the replay warning in tests.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_delay_journal_replay_for_testing 0
ceph config get mds mds_delay_journal_replay_for_testing
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_deny_all_reconnect

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mds.md#SP_mds_deny_all_reconnect](../../../config/mds/mds.md#SP_mds_deny_all_reconnect) |

**کارکرد:** flag to deny all client reconnects during failover

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_deny_all_reconnect true
ceph config get mds mds_deny_all_reconnect
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_deny_all_reconnect
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dir_keys_per_op

| | |
|---|---|
| نوع | Int · default `16384` · **Advanced** |
| جدول | [mds.md#SP_mds_dir_keys_per_op](../../../config/mds/mds.md#SP_mds_dir_keys_per_op) |

**کارکرد:** Number of directory entries to read in one RADOS operation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_dir_keys_per_op 16384
ceph config get mds mds_dir_keys_per_op
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16384`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_dir_keys_per_op
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dir_max_commit_size

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_dir_max_commit_size](../../../config/mds/mds.md#SP_mds_dir_max_commit_size) |

**کارکرد:** Maximum size in mebibytes for a RADOS write to a directory

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_dir_max_commit_size 10
ceph config get mds mds_dir_max_commit_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_dir_max_commit_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dir_max_entries

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_dir_max_entries](../../../config/mds/mds.md#SP_mds_dir_max_entries) |

**کارکرد:** maximum number of entries per directory before new creat/links fail The maximum number of entries before any new entries are rejected with ENOSPC.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_dir_max_entries 64
ceph config get mds mds_dir_max_entries
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_dir_max_entries
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dir_prefetch

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_dir_prefetch](../../../config/mds/mds.md#SP_mds_dir_prefetch) |

**کارکرد:** flag to prefetch entire dir

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_dir_prefetch false
ceph config get mds mds_dir_prefetch
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_dir_prefetch
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_dump_cache_after_rejoin

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_dump_cache_after_rejoin](../../../config/mds/mds.md#SP_mds_dump_cache_after_rejoin) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_dump_cache_after_rejoin true
ceph config get mds mds_dump_cache_after_rejoin
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_dump_cache_on_map

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_dump_cache_on_map](../../../config/mds/mds.md#SP_mds_dump_cache_on_map) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_dump_cache_on_map true
ceph config get mds mds_dump_cache_on_map
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_dump_cache_threshold_file

| | |
|---|---|
| نوع | Size · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_dump_cache_threshold_file](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_file) |

**کارکرد:** threshold for cache usage to disallow "dump cache" operation to file Disallow MDS from dumping caches to file via "dump cache" command if cache usage exceeds this threshold.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_dump_cache_threshold_file 64
ceph config get mds mds_dump_cache_threshold_file
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_dump_cache_threshold_formatter

| | |
|---|---|
| نوع | Size · default `1_G` · **Dev** |
| جدول | [mds.md#SP_mds_dump_cache_threshold_formatter](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_formatter) |

**کارکرد:** threshold for cache usage to disallow "dump cache" operation to formatter Disallow MDS from dumping caches to formatter via "dump cache" command if cache usage exceeds this threshold.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_dump_cache_threshold_formatter 1_G
ceph config get mds mds_dump_cache_threshold_formatter
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1_G`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_early_reply

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_early_reply](../../../config/mds/mds.md#SP_mds_early_reply) |

**کارکرد:** additional reply to clients that metadata requests are complete but not yet durable

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_early_reply false
ceph config get mds mds_early_reply
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_early_reply
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_enable_op_tracker

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_enable_op_tracker](../../../config/mds/mds.md#SP_mds_enable_op_tracker) |

**کارکرد:** track remote operation progression and statistics

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_enable_op_tracker false
ceph config get mds mds_enable_op_tracker
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_enable_op_tracker
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_enforce_unique_name

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_enforce_unique_name](../../../config/mds/mds.md#SP_mds_enforce_unique_name) |

**کارکرد:** Require unique MDS names

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_enforce_unique_name false
ceph config get mds mds_enforce_unique_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_enforce_unique_name
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_export_ephemeral_distributed

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_export_ephemeral_distributed](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed) |

**کارکرد:** allow ephemeral distributed pinning of the loaded subtrees pin the immediate child directories of the loaded directory inode based on the consistent hash of the child's inode number.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_export_ephemeral_distributed false
ceph config get mds mds_export_ephemeral_distributed
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_export_ephemeral_distributed
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_export_ephemeral_distributed_factor

| | |
|---|---|
| نوع | Float · default `2` · **Advanced** |
| جدول | [mds.md#SP_mds_export_ephemeral_distributed_factor](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed_factor) |

**کارکرد:** multiple of max_mds for splitting and distributing directory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_export_ephemeral_distributed_factor 2
ceph config get mds mds_export_ephemeral_distributed_factor
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `100`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_export_ephemeral_distributed_factor
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_export_ephemeral_random

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_export_ephemeral_random](../../../config/mds/mds.md#SP_mds_export_ephemeral_random) |

**کارکرد:** allow ephemeral random pinning of the loaded subtrees probabilistically pin the loaded directory inode and the subtree beneath it to an MDS based on the consistent hash of the inode number. The higher this value the more likely the loaded subtrees get pinned

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_export_ephemeral_random false
ceph config get mds mds_export_ephemeral_random
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_export_ephemeral_random
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_export_ephemeral_random_max

| | |
|---|---|
| نوع | Float · default `0.01` · **Advanced** |
| جدول | [mds.md#SP_mds_export_ephemeral_random_max](../../../config/mds/mds.md#SP_mds_export_ephemeral_random_max) |

**کارکرد:** the maximum percent permitted for random ephemeral pin policy

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`mds_export_ephemeral_random`](../../../config/mds/mds.md#SP_mds_export_ephemeral_random)

**مثال:**

```bash
ceph config set mds mds_export_ephemeral_random_max 0.01
ceph config get mds mds_export_ephemeral_random_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.01`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `0`، حداکثر `1`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_export_ephemeral_random_max
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_file_blockdiff_max_concurrent_object_scans

| | |
|---|---|
| نوع | Uint · default `16` · **Advanced** |
| جدول | [mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans](../../../config/mds/mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans) |

**کارکرد:** Maximum number of concurrent object scans Maximum number of concurrent listsnaps operations sent to RADOS.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_file_blockdiff_max_concurrent_object_scans 16
ceph config get mds mds_file_blockdiff_max_concurrent_object_scans
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `—`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_file_blockdiff_max_concurrent_object_scans
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_fscrypt_last_block_max_size

| | |
|---|---|
| نوع | Size · default `4_K` · **Advanced** |
| جدول | [mds.md#SP_mds_fscrypt_last_block_max_size](../../../config/mds/mds.md#SP_mds_fscrypt_last_block_max_size) |

**کارکرد:** Maximum size of the last block without the header along with a truncate request when the fscrypt is enabled.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_fscrypt_last_block_max_size 4_K
ceph config get mds mds_fscrypt_last_block_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_fscrypt_last_block_max_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_go_bad_corrupt_dentry

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_go_bad_corrupt_dentry](../../../config/mds/mds.md#SP_mds_go_bad_corrupt_dentry) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_go_bad_corrupt_dentry false
ceph config get mds mds_go_bad_corrupt_dentry
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_go_bad_corrupt_dentry
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_hack_allow_loading_invalid_metadata

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mds.md#SP_mds_hack_allow_loading_invalid_metadata](../../../config/mds/mds.md#SP_mds_hack_allow_loading_invalid_metadata) |

**کارکرد:** INTENTIONALLY CAUSE DATA LOSS by bypasing checks for invalid metadata on disk. Allows testing repair tools.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_hack_allow_loading_invalid_metadata true
ceph config get mds mds_hack_allow_loading_invalid_metadata
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_hack_allow_loading_invalid_metadata
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_health_cache_threshold

| | |
|---|---|
| نوع | Float · default `1.5` · **Advanced** |
| جدول | [mds.md#SP_mds_health_cache_threshold](../../../config/mds/mds.md#SP_mds_health_cache_threshold) |

**کارکرد:** Threshold for cache size to generate health warning

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_health_cache_threshold 1.5
ceph config get mds mds_health_cache_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_health_cache_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_health_summarize_threshold

| | |
|---|---|
| نوع | Int · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_health_summarize_threshold](../../../config/mds/mds.md#SP_mds_health_summarize_threshold) |

**کارکرد:** Threshold number of clients to summarize late client recall

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_health_summarize_threshold 10
ceph config get mds mds_health_summarize_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_health_summarize_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_heartbeat_grace

| | |
|---|---|
| نوع | Float · default `15` · **Advanced** |
| جدول | [mds.md#SP_mds_heartbeat_grace](../../../config/mds/mds.md#SP_mds_heartbeat_grace) |

**کارکرد:** Tolerance in seconds for MDS internal heartbeats

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_heartbeat_grace 15
ceph config get mds mds_heartbeat_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_heartbeat_grace
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_heartbeat_reset_grace

| | |
|---|---|
| نوع | Uint · default `1000` · **Advanced** |
| جدول | [mds.md#SP_mds_heartbeat_reset_grace](../../../config/mds/mds.md#SP_mds_heartbeat_reset_grace) |

**کارکرد:** Tolerance in seconds for long-running MDS operations which do not periodically reset the heartbeat timeout.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_heartbeat_reset_grace 1000
ceph config get mds mds_heartbeat_reset_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_heartbeat_reset_grace
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_join_fs

| | |
|---|---|
| نوع | Str · default `(empty)` · **Basic** |
| جدول | [mds.md#SP_mds_join_fs](../../../config/mds/mds.md#SP_mds_join_fs) |

**کارکرد:** File system MDS prefers to join This setting indicates which CephFS file system the MDS should prefer to join (affinity). The monitors will try to have the MDS cluster safely reach a state where all MDS have strong affinity, even via failovers to a standby.

**زمان استفاده:** رفتار اصلی MDS — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set mds mds_join_fs "example"
ceph config get mds mds_join_fs
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `(empty)` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_join_fs
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_journal_format

| | |
|---|---|
| نوع | Uint · default `1` · **Dev** |
| جدول | [mds.md#SP_mds_journal_format](../../../config/mds/mds.md#SP_mds_journal_format) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_journal_format 1
ceph config get mds mds_journal_format
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_create_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_create_at](../../../config/mds/mds.md#SP_mds_kill_create_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_create_at 64
ceph config get mds mds_kill_create_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_dirfrag_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_dirfrag_at](../../../config/mds/mds.md#SP_mds_kill_dirfrag_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_dirfrag_at 64
ceph config get mds mds_kill_dirfrag_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_export_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_export_at](../../../config/mds/mds.md#SP_mds_kill_export_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_export_at 64
ceph config get mds mds_kill_export_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_import_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_import_at](../../../config/mds/mds.md#SP_mds_kill_import_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_import_at 64
ceph config get mds mds_kill_import_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_journal_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_journal_at](../../../config/mds/mds.md#SP_mds_kill_journal_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_journal_at 64
ceph config get mds mds_kill_journal_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_journal_expire_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_journal_expire_at](../../../config/mds/mds.md#SP_mds_kill_journal_expire_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_journal_expire_at 64
ceph config get mds mds_kill_journal_expire_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_journal_replay_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_journal_replay_at](../../../config/mds/mds.md#SP_mds_kill_journal_replay_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_journal_replay_at 64
ceph config get mds mds_kill_journal_replay_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_link_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_link_at](../../../config/mds/mds.md#SP_mds_kill_link_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_link_at 64
ceph config get mds mds_kill_link_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_mdstable_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_mdstable_at](../../../config/mds/mds.md#SP_mds_kill_mdstable_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_mdstable_at 64
ceph config get mds mds_kill_mdstable_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_openc_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_openc_at](../../../config/mds/mds.md#SP_mds_kill_openc_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_openc_at 64
ceph config get mds mds_kill_openc_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_rename_at

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_rename_at](../../../config/mds/mds.md#SP_mds_kill_rename_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_rename_at 64
ceph config get mds mds_kill_rename_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_kill_shutdown_at

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_kill_shutdown_at](../../../config/mds/mds.md#SP_mds_kill_shutdown_at) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_kill_shutdown_at 64
ceph config get mds mds_kill_shutdown_at
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_max_completed_flushes

| | |
|---|---|
| نوع | Uint · default `100000` · **Dev** |
| جدول | [mds.md#SP_mds_max_completed_flushes](../../../config/mds/mds.md#SP_mds_max_completed_flushes) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_max_completed_flushes 100000
ceph config get mds mds_max_completed_flushes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`100000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_max_completed_requests

| | |
|---|---|
| نوع | Uint · default `100000` · **Dev** |
| جدول | [mds.md#SP_mds_max_completed_requests](../../../config/mds/mds.md#SP_mds_max_completed_requests) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_max_completed_requests 100000
ceph config get mds mds_max_completed_requests
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`100000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_max_export_size

| | |
|---|---|
| نوع | Size · default `20_M` · **Dev** |
| جدول | [mds.md#SP_mds_max_export_size](../../../config/mds/mds.md#SP_mds_max_export_size) |

**کارکرد:** Maximum size (bytes) of a single subtree export during MDS rebalancing.

**زمان استفاده:** Lower to reduce latency spikes during balance; raise for faster migration on high-bandwidth networks.

**مثال:**

```bash
ceph config set mds mds_max_export_size 20_M
ceph config get mds mds_max_export_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`20_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_max_file_recover

| | |
|---|---|
| نوع | Uint · default `32` · **Advanced** |
| جدول | [mds.md#SP_mds_max_file_recover](../../../config/mds/mds.md#SP_mds_max_file_recover) |

**کارکرد:** Maximum number of files for which to recover file sizes in parallel

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_file_recover 32
ceph config get mds mds_max_file_recover
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_file_recover
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_purge_files

| | |
|---|---|
| نوع | Uint · default `64` · **Advanced** |
| جدول | [mds.md#SP_mds_max_purge_files](../../../config/mds/mds.md#SP_mds_max_purge_files) |

**کارکرد:** maximum number of deleted files to purge in parallel

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_purge_files 64
ceph config get mds mds_max_purge_files
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_purge_files
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_purge_ops

| | |
|---|---|
| نوع | Uint · default `8_K` · **Advanced** |
| جدول | [mds.md#SP_mds_max_purge_ops](../../../config/mds/mds.md#SP_mds_max_purge_ops) |

**کارکرد:** maximum number of purge operations performed in parallel

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_purge_ops 8_K
ceph config get mds mds_max_purge_ops
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_purge_ops
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_purge_ops_per_pg

| | |
|---|---|
| نوع | Float · default `0.5` · **Advanced** |
| جدول | [mds.md#SP_mds_max_purge_ops_per_pg](../../../config/mds/mds.md#SP_mds_max_purge_ops_per_pg) |

**کارکرد:** number of parallel purge operations performed per PG

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_purge_ops_per_pg 0.5
ceph config get mds mds_max_purge_ops_per_pg
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_purge_ops_per_pg
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_scrub_ops_in_progress

| | |
|---|---|
| نوع | Int · default `5` · **Advanced** |
| جدول | [mds.md#SP_mds_max_scrub_ops_in_progress](../../../config/mds/mds.md#SP_mds_max_scrub_ops_in_progress) |

**کارکرد:** maximum number of scrub operations performed in parallel

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_scrub_ops_in_progress 5
ceph config get mds mds_max_scrub_ops_in_progress
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_scrub_ops_in_progress
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_snaps_per_dir

| | |
|---|---|
| نوع | Uint · default `100` · **Advanced** |
| جدول | [mds.md#SP_mds_max_snaps_per_dir](../../../config/mds/mds.md#SP_mds_max_snaps_per_dir) |

**کارکرد:** max snapshots per directory maximum number of snapshots that can be created per directory

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_max_snaps_per_dir 100
ceph config get mds mds_max_snaps_per_dir
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** ظرفیت

1. خط پایه روی `100`.
2. قبل از تغییر مسیرها ظرفیت و چیدمان filesystem را برنامه‌ریزی کنید.
3. مطمئن شوید همه دیمن‌هایی که باید مسیر را share کنند mount یکسان دارند.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_max_snaps_per_dir
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_numa_node

| | |
|---|---|
| نوع | Int · default `-1` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mds.md#SP_mds_numa_node](../../../config/mds/mds.md#SP_mds_numa_node) |

**کارکرد:** Set MDS CPU affinity to a NUMA node (-1 for none)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_numa_node 128
ceph config get mds mds_numa_node
ceph orch restart mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `-1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_numa_node
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_oft_prefetch_dirfrags

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mds.md#SP_mds_oft_prefetch_dirfrags](../../../config/mds/mds.md#SP_mds_oft_prefetch_dirfrags) |

**کارکرد:** prefetch dirfrags recorded in open file table on startup

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_oft_prefetch_dirfrags true
ceph config get mds mds_oft_prefetch_dirfrags
ceph orch restart mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_oft_prefetch_dirfrags
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_complaint_time

| | |
|---|---|
| نوع | Float · default `30` · **Advanced** |
| جدول | [mds.md#SP_mds_op_complaint_time](../../../config/mds/mds.md#SP_mds_op_complaint_time) |

**کارکرد:** time in seconds to consider an operation blocked after no updates

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_op_complaint_time 30
ceph config get mds mds_op_complaint_time
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `30`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_op_complaint_time
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_history_duration

| | |
|---|---|
| نوع | Uint · default `600` · **Advanced** |
| جدول | [mds.md#SP_mds_op_history_duration](../../../config/mds/mds.md#SP_mds_op_history_duration) |

**کارکرد:** expiration time in seconds of historical operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_op_history_duration 600
ceph config get mds mds_op_history_duration
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `600`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_op_history_duration
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_history_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mds.md#SP_mds_op_history_size](../../../config/mds/mds.md#SP_mds_op_history_size) |

**کارکرد:** maximum size for list of historical operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_op_history_size 20
ceph config get mds mds_op_history_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_op_history_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_history_slow_op_size

| | |
|---|---|
| نوع | Uint · default `20` · **Advanced** |
| جدول | [mds.md#SP_mds_op_history_slow_op_size](../../../config/mds/mds.md#SP_mds_op_history_slow_op_size) |

**کارکرد:** maximum size for list of historical slow operations

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_op_history_slow_op_size 20
ceph config get mds mds_op_history_slow_op_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `20`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_op_history_slow_op_size
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_op_history_slow_op_threshold

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_op_history_slow_op_threshold](../../../config/mds/mds.md#SP_mds_op_history_slow_op_threshold) |

**کارکرد:** track the op if over this threshold

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_op_history_slow_op_threshold 10
ceph config get mds mds_op_history_slow_op_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_op_history_slow_op_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_ping_grace

| | |
|---|---|
| نوع | Secs · default `15` · **Advanced** |
| جدول | [mds.md#SP_mds_ping_grace](../../../config/mds/mds.md#SP_mds_ping_grace) |

**کارکرد:** timeout after which an MDS is considered laggy by rank 0 MDS. timeout for replying to a ping message sent by rank 0 after which an active MDS considered laggy (delayed metrics) by rank 0.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_ping_grace 15
ceph config get mds mds_ping_grace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_ping_grace
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_purge_queue_busy_flush_period

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [mds.md#SP_mds_purge_queue_busy_flush_period](../../../config/mds/mds.md#SP_mds_purge_queue_busy_flush_period) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_purge_queue_busy_flush_period 1
ceph config get mds mds_purge_queue_busy_flush_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_recall_global_max_decay_threshold

| | |
|---|---|
| نوع | Size · default `128_K` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_global_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_global_max_decay_threshold) |

**کارکرد:** Decay threshold for throttle on recalled caps globally

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_recall_global_max_decay_threshold 128_K
ceph config get mds mds_recall_global_max_decay_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_global_max_decay_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_max_decay_rate

| | |
|---|---|
| نوع | Float · default `1.5` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_max_decay_rate](../../../config/mds/mds.md#SP_mds_recall_max_decay_rate) |

**کارکرد:** Decay rate for throttle on recalled caps on a session

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_recall_max_decay_rate 1.5
ceph config get mds mds_recall_max_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1.5`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_max_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_max_decay_threshold

| | |
|---|---|
| نوع | Size · default `128_K` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_max_decay_threshold) |

**کارکرد:** Decay threshold for throttle on recalled caps on a session

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_recall_max_decay_threshold 128_K
ceph config get mds mds_recall_max_decay_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_max_decay_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_warning_decay_rate

| | |
|---|---|
| نوع | Float · default `60` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_warning_decay_rate](../../../config/mds/mds.md#SP_mds_recall_warning_decay_rate) |

**کارکرد:** Decay rate for warning on slow session cap recall

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_recall_warning_decay_rate 60
ceph config get mds mds_recall_warning_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `60`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_warning_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_warning_threshold

| | |
|---|---|
| نوع | Size · default `256_K` · **Advanced** |
| جدول | [mds.md#SP_mds_recall_warning_threshold](../../../config/mds/mds.md#SP_mds_recall_warning_threshold) |

**کارکرد:** Decay threshold for warning on slow session cap recall

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_recall_warning_threshold 256_K
ceph config get mds mds_recall_warning_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `256_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_recall_warning_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_replay_unsafe_with_closed_session

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [mds.md#SP_mds_replay_unsafe_with_closed_session](../../../config/mds/mds.md#SP_mds_replay_unsafe_with_closed_session) |

**کارکرد:** complete all the replay request when mds is restarted, no matter the session is closed or not

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_replay_unsafe_with_closed_session true
ceph config get mds mds_replay_unsafe_with_closed_session
ceph orch restart mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_replay_unsafe_with_closed_session
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_request_load_average_decay_rate

| | |
|---|---|
| نوع | Float · default `1_min` · **Advanced** |
| جدول | [mds.md#SP_mds_request_load_average_decay_rate](../../../config/mds/mds.md#SP_mds_request_load_average_decay_rate) |

**کارکرد:** rate of decay in seconds for calculating request load average

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_request_load_average_decay_rate 1_min
ceph config get mds mds_request_load_average_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_request_load_average_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_root_ino_gid

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_root_ino_gid](../../../config/mds/mds.md#SP_mds_root_ino_gid) |

**کارکرد:** default gid for new root directory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_root_ino_gid 64
ceph config get mds mds_root_ino_gid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_root_ino_gid
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_root_ino_uid

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_root_ino_uid](../../../config/mds/mds.md#SP_mds_root_ino_uid) |

**کارکرد:** default uid for new root directory

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_root_ino_uid 64
ceph config get mds mds_root_ino_uid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_root_ino_uid
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_scrub_stats_review_period

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [mds.md#SP_mds_scrub_stats_review_period](../../../config/mds/mds.md#SP_mds_scrub_stats_review_period) |

**کارکرد:** Period for which scrub stats will be available for review. Number of days for which scrub stats will be available for review since start of scrub operation. After this period, the stats will be auto purged. These stats will not be saved to the disk. So any restart or failover of mds will cause stats to be lost forever.

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set mds mds_scrub_stats_review_period 1
ceph config get mds mds_scrub_stats_review_period
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `60`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_scrub_stats_review_period
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_server_dispatch_client_request_delay

| | |
|---|---|
| نوع | Millisecs · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_server_dispatch_client_request_delay](../../../config/mds/mds.md#SP_mds_server_dispatch_client_request_delay) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_server_dispatch_client_request_delay 0
ceph config get mds mds_server_dispatch_client_request_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_server_dispatch_killpoint_random

| | |
|---|---|
| نوع | Float · default `0.0` · **Dev** |
| جدول | [mds.md#SP_mds_server_dispatch_killpoint_random](../../../config/mds/mds.md#SP_mds_server_dispatch_killpoint_random) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_server_dispatch_killpoint_random 0.0
ceph config get mds mds_server_dispatch_killpoint_random
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_session_blocklist_on_evict

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_session_blocklist_on_evict](../../../config/mds/mds.md#SP_mds_session_blocklist_on_evict) |

**کارکرد:** Blocklist clients that have been evicted

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_session_blocklist_on_evict false
ceph config get mds mds_session_blocklist_on_evict
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_blocklist_on_evict
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cache_liveness_decay_rate

| | |
|---|---|
| نوع | Float · default `5_min` · **Advanced** |
| جدول | [mds.md#SP_mds_session_cache_liveness_decay_rate](../../../config/mds/mds.md#SP_mds_session_cache_liveness_decay_rate) |

**کارکرد:** Decay rate for session liveness leading to preemptive cap recall This determines how long a session needs to be quiescent before the MDS begins preemptively recalling capabilities. The default of 5 minutes will cause 10 halvings of the decay counter after 1 hour, or 1/1024. The default magnitude of 10 (1^10 or 1024) is chosen so that the MDS considers a previously chatty session (approximately) to be quiescent after 1 hour.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`mds_session_cache_liveness_magnitude`](../../../config/mds/mds.md#SP_mds_session_cache_liveness_magnitude)

**مثال:**

```bash
ceph config set mds mds_session_cache_liveness_decay_rate 5_min
ceph config get mds mds_session_cache_liveness_decay_rate
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `5_min`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_cache_liveness_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cache_liveness_magnitude

| | |
|---|---|
| نوع | Size · default `10` · **Advanced** |
| جدول | [mds.md#SP_mds_session_cache_liveness_magnitude](../../../config/mds/mds.md#SP_mds_session_cache_liveness_magnitude) |

**کارکرد:** Decay magnitude for preemptively recalling caps on quiet client This is the order of magnitude difference (in base 2) of the internal liveness decay counter and the number of capabilities the session holds. When this difference occurs, the MDS treats the session as quiescent and begins recalling capabilities.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`mds_session_cache_liveness_decay_rate`](../../../config/mds/mds.md#SP_mds_session_cache_liveness_decay_rate)

**مثال:**

```bash
ceph config set mds mds_session_cache_liveness_magnitude 10
ceph config get mds mds_session_cache_liveness_magnitude
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_cache_liveness_magnitude
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_metadata_threshold

| | |
|---|---|
| نوع | Size · default `16_M` · **Advanced** |
| جدول | [mds.md#SP_mds_session_metadata_threshold](../../../config/mds/mds.md#SP_mds_session_metadata_threshold) |

**کارکرد:** Evict non-advancing client-tid sessions exceeding the config size. Evict clients which are not advancing their request tids which causes a large buildup of session metadata (`completed_requests`) in the MDS causing the MDS to go read-only since the RADOS operation exceeds the size threashold. This config is the maximum size (in bytes) that a session metadata (encoded) can grow.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_session_metadata_threshold 16_M
ceph config get mds mds_session_metadata_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `16_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_session_metadata_threshold
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_sessionmap_keys_per_op

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [mds.md#SP_mds_sessionmap_keys_per_op](../../../config/mds/mds.md#SP_mds_sessionmap_keys_per_op) |

**کارکرد:** Number of omap keys to read from the SessionMap in one operation

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set mds mds_sessionmap_keys_per_op 1_K
ceph config get mds mds_sessionmap_keys_per_op
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_sessionmap_keys_per_op
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_shutdown_check

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_shutdown_check](../../../config/mds/mds.md#SP_mds_shutdown_check) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_shutdown_check 64
ceph config get mds mds_shutdown_check
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_skip_ino

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_skip_ino](../../../config/mds/mds.md#SP_mds_skip_ino) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_skip_ino 64
ceph config get mds mds_skip_ino
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_sleep_rank_change

| | |
|---|---|
| نوع | Float · default `0.0` · **Dev** |
| جدول | [mds.md#SP_mds_sleep_rank_change](../../../config/mds/mds.md#SP_mds_sleep_rank_change) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_sleep_rank_change 0.0
ceph config get mds mds_sleep_rank_change
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0.0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_snap_max_uid

| | |
|---|---|
| نوع | Uint · default `4294967294` · **Advanced** |
| جدول | [mds.md#SP_mds_snap_max_uid](../../../config/mds/mds.md#SP_mds_snap_max_uid) |

**کارکرد:** maximum uid of client to perform snapshots

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_snap_max_uid 4294967294
ceph config get mds mds_snap_max_uid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4294967294`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_snap_max_uid
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_snap_min_uid

| | |
|---|---|
| نوع | Uint · default `0` · **Advanced** |
| جدول | [mds.md#SP_mds_snap_min_uid](../../../config/mds/mds.md#SP_mds_snap_min_uid) |

**کارکرد:** minimum uid of client to perform snapshots

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set mds mds_snap_min_uid 64
ceph config get mds mds_snap_min_uid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_snap_min_uid
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_snap_rstat

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [mds.md#SP_mds_snap_rstat](../../../config/mds/mds.md#SP_mds_snap_rstat) |

**کارکرد:** enabled nested rstat for snapshots

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set mds mds_snap_rstat true
ceph config get mds mds_snap_rstat
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_snap_rstat
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_standby_replay_damaged

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_standby_replay_damaged](../../../config/mds/mds.md#SP_mds_standby_replay_damaged) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_standby_replay_damaged true
ceph config get mds mds_standby_replay_damaged
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_symlink_recovery

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_symlink_recovery](../../../config/mds/mds.md#SP_mds_symlink_recovery) |

**کارکرد:** Stores symlink target on the first data object of symlink file. Allows recover of symlink using recovery tools.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_symlink_recovery false
ceph config get mds mds_symlink_recovery
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_symlink_recovery
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_thrash_exports

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_thrash_exports](../../../config/mds/mds.md#SP_mds_thrash_exports) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_thrash_exports 64
ceph config get mds mds_thrash_exports
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_thrash_fragments

| | |
|---|---|
| نوع | Int · default `0` · **Dev** |
| جدول | [mds.md#SP_mds_thrash_fragments](../../../config/mds/mds.md#SP_mds_thrash_fragments) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_thrash_fragments 64
ceph config get mds mds_thrash_fragments
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_use_global_snaprealm_seq_for_subvol

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [mds.md#SP_mds_use_global_snaprealm_seq_for_subvol](../../../config/mds/mds.md#SP_mds_use_global_snaprealm_seq_for_subvol) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set mds mds_use_global_snaprealm_seq_for_subvol false
ceph config get mds mds_use_global_snaprealm_seq_for_subvol
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get mds mds_use_global_snaprealm_seq_for_subvol
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_valgrind_exit

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_valgrind_exit](../../../config/mds/mds.md#SP_mds_valgrind_exit) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_valgrind_exit true
ceph config get mds mds_valgrind_exit
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_verify_backtrace

| | |
|---|---|
| نوع | Uint · default `1` · **Dev** |
| جدول | [mds.md#SP_mds_verify_backtrace](../../../config/mds/mds.md#SP_mds_verify_backtrace) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_verify_backtrace 1
ceph config get mds mds_verify_backtrace
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_verify_scatter

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_verify_scatter](../../../config/mds/mds.md#SP_mds_verify_scatter) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_verify_scatter true
ceph config get mds mds_verify_scatter
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_wipe_ino_prealloc

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_wipe_ino_prealloc](../../../config/mds/mds.md#SP_mds_wipe_ino_prealloc) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_wipe_ino_prealloc true
ceph config get mds mds_wipe_ino_prealloc
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### mds_wipe_sessions

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [mds.md#SP_mds_wipe_sessions](../../../config/mds/mds.md#SP_mds_wipe_sessions) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set mds mds_wipe_sessions true
ceph config get mds mds_wipe_sessions
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---


[← نمای کلی](../OVERVIEW.md)
