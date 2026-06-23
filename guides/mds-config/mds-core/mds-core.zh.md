# Metadata server core

MDS 配置深度指南 — 138 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_abort_on_newly_corrupt_dentry](#mds_abort_on_newly_corrupt_dentry) | `True` | Advanced | Performance |
| [mds_action_on_write_error](#mds_action_on_write_error) | `1` | Advanced | Performance |
| [mds_allow_async_dirops](#mds_allow_async_dirops) | `True` | Advanced | Policy |
| [mds_allow_batched_ops](#mds_allow_batched_ops) | `True` | Advanced | Policy |
| [mds_alternate_name_max](#mds_alternate_name_max) | `8_K` | Advanced | Performance |
| [mds_asio_thread_count](#mds_asio_thread_count) | `2` | Advanced | Performance |
| [mds_bal_export_pin](#mds_bal_export_pin) | `True` | Advanced | Performance |
| [mds_bal_fragment_dirs](#mds_bal_fragment_dirs) | `True` | Advanced | Performance |
| [mds_bal_fragment_fast_factor](#mds_bal_fragment_fast_factor) | `1.5` | Advanced | Performance |
| [mds_bal_fragment_size_max](#mds_bal_fragment_size_max) | `100000` | Advanced | Performance |
| [mds_bal_idle_threshold](#mds_bal_idle_threshold) | `0` | Advanced | Performance |
| [mds_bal_max](#mds_bal_max) | `-1` | Dev | Dev |
| [mds_bal_max_until](#mds_bal_max_until) | `-1` | Dev | Dev |
| [mds_bal_merge_size](#mds_bal_merge_size) | `50` | Advanced | Performance |
| [mds_bal_midchunk](#mds_bal_midchunk) | `0.3` | Dev | Dev |
| [mds_bal_min_rebalance](#mds_bal_min_rebalance) | `0.1` | Dev | Dev |
| [mds_bal_min_start](#mds_bal_min_start) | `0.2` | Dev | Dev |
| [mds_bal_minchunk](#mds_bal_minchunk) | `0.001` | Dev | Dev |
| [mds_bal_mode](#mds_bal_mode) | `0` | Dev | Dev |
| [mds_bal_need_max](#mds_bal_need_max) | `1.2` | Dev | Dev |
| [mds_bal_need_min](#mds_bal_need_min) | `0.8` | Dev | Dev |
| [mds_bal_overload_epochs](#mds_bal_overload_epochs) | `2` | Dev | Dev |
| [mds_bal_replicate_threshold](#mds_bal_replicate_threshold) | `8000` | Advanced | Performance |
| [mds_bal_split_bits](#mds_bal_split_bits) | `3` | Advanced | Performance |
| [mds_bal_split_rd](#mds_bal_split_rd) | `25000` | Advanced | Performance |
| [mds_bal_split_size](#mds_bal_split_size) | `10000` | Advanced | Performance |
| [mds_bal_split_wr](#mds_bal_split_wr) | `10000` | Advanced | Performance |
| [mds_bal_target_decay](#mds_bal_target_decay) | `10` | Advanced | Performance |
| [mds_bal_unreplicate_threshold](#mds_bal_unreplicate_threshold) | `0` | Advanced | Performance |
| [mds_beacon_grace](#mds_beacon_grace) | `15` | Advanced | Performance |
| [mds_cache_memory_limit](#mds_cache_memory_limit) | `4_G` | Basic | Performance |
| [mds_cache_mid](#mds_cache_mid) | `0.7` | Advanced | Performance |
| [mds_cache_quiesce_decay_rate](#mds_cache_quiesce_decay_rate) | `1` | Advanced | Performance |
| [mds_cache_quiesce_delay](#mds_cache_quiesce_delay) | `0` | Dev | Dev |
| [mds_cache_quiesce_sleep](#mds_cache_quiesce_sleep) | `200` | Advanced | Performance |
| [mds_cache_quiesce_threshold](#mds_cache_quiesce_threshold) | `512_K` | Advanced | Performance |
| [mds_cache_reservation](#mds_cache_reservation) | `0.05` | Advanced | Performance |
| [mds_cache_trim_decay_rate](#mds_cache_trim_decay_rate) | `1` | Advanced | Performance |
| [mds_cache_trim_threshold](#mds_cache_trim_threshold) | `256_K` | Advanced | Performance |
| [mds_client_delegate_inos_pct](#mds_client_delegate_inos_pct) | `50` | Advanced | Performance |
| [mds_client_prealloc_inos](#mds_client_prealloc_inos) | `1000` | Advanced | Performance |
| [mds_client_writeable_range_max_inc_objs](#mds_client_writeable_range_max_inc_objs) | `1_K` | Advanced | Performance |
| [mds_connect_bootstrapping](#mds_connect_bootstrapping) | `False` | Dev | Dev |
| [mds_damage_table_max_entries](#mds_damage_table_max_entries) | `10000` | Advanced | Performance |
| [mds_data](#mds_data) | `/var/lib/ceph/mds/$cluster-$id` | Advanced | Performance |
| [mds_decay_halflife](#mds_decay_halflife) | `5` | Advanced | Performance |
| [mds_default_dir_hash](#mds_default_dir_hash) | `2` | Advanced | Performance |
| [mds_defer_session_stale](#mds_defer_session_stale) | `True` | Dev | Dev |
| [mds_delay_journal_replay_for_testing](#mds_delay_journal_replay_for_testing) | `0` | Dev | Dev |
| [mds_deny_all_reconnect](#mds_deny_all_reconnect) | `False` | Advanced | Performance |
| [mds_dir_keys_per_op](#mds_dir_keys_per_op) | `16384` | Advanced | Performance |
| [mds_dir_max_commit_size](#mds_dir_max_commit_size) | `10` | Advanced | Performance |
| [mds_dir_max_entries](#mds_dir_max_entries) | `0` | Advanced | Performance |
| [mds_dir_prefetch](#mds_dir_prefetch) | `True` | Advanced | Performance |
| [mds_dump_cache_after_rejoin](#mds_dump_cache_after_rejoin) | `False` | Dev | Dev |
| [mds_dump_cache_on_map](#mds_dump_cache_on_map) | `False` | Dev | Dev |
| [mds_dump_cache_threshold_file](#mds_dump_cache_threshold_file) | `0` | Dev | Dev |
| [mds_dump_cache_threshold_formatter](#mds_dump_cache_threshold_formatter) | `1_G` | Dev | Dev |
| [mds_early_reply](#mds_early_reply) | `True` | Advanced | Performance |
| [mds_enable_op_tracker](#mds_enable_op_tracker) | `True` | Advanced | Policy |
| [mds_enforce_unique_name](#mds_enforce_unique_name) | `True` | Advanced | Policy |
| [mds_export_ephemeral_distributed](#mds_export_ephemeral_distributed) | `True` | Advanced | Performance |
| [mds_export_ephemeral_distributed_factor](#mds_export_ephemeral_distributed_factor) | `2` | Advanced | Performance |
| [mds_export_ephemeral_random](#mds_export_ephemeral_random) | `True` | Advanced | Performance |
| [mds_export_ephemeral_random_max](#mds_export_ephemeral_random_max) | `0.01` | Advanced | Performance |
| [mds_file_blockdiff_max_concurrent_object_scans](#mds_file_blockdiff_max_concurrent_object_scans) | `16` | Advanced | Performance |
| [mds_fscrypt_last_block_max_size](#mds_fscrypt_last_block_max_size) | `4_K` | Advanced | Performance |
| [mds_go_bad_corrupt_dentry](#mds_go_bad_corrupt_dentry) | `True` | Advanced | Performance |
| [mds_hack_allow_loading_invalid_metadata](#mds_hack_allow_loading_invalid_metadata) | `False` | Advanced | Policy |
| [mds_health_cache_threshold](#mds_health_cache_threshold) | `1.5` | Advanced | Performance |
| [mds_health_summarize_threshold](#mds_health_summarize_threshold) | `10` | Advanced | Performance |
| [mds_heartbeat_grace](#mds_heartbeat_grace) | `15` | Advanced | Performance |
| [mds_heartbeat_reset_grace](#mds_heartbeat_reset_grace) | `1000` | Advanced | Performance |
| [mds_join_fs](#mds_join_fs) | `(empty)` | Basic | Policy |
| [mds_journal_format](#mds_journal_format) | `1` | Dev | Dev |
| [mds_kill_create_at](#mds_kill_create_at) | `0` | Dev | Dev |
| [mds_kill_dirfrag_at](#mds_kill_dirfrag_at) | `0` | Dev | Dev |
| [mds_kill_export_at](#mds_kill_export_at) | `0` | Dev | Dev |
| [mds_kill_import_at](#mds_kill_import_at) | `0` | Dev | Dev |
| [mds_kill_journal_at](#mds_kill_journal_at) | `0` | Dev | Dev |
| [mds_kill_journal_expire_at](#mds_kill_journal_expire_at) | `0` | Dev | Dev |
| [mds_kill_journal_replay_at](#mds_kill_journal_replay_at) | `0` | Dev | Dev |
| [mds_kill_link_at](#mds_kill_link_at) | `0` | Dev | Dev |
| [mds_kill_mdstable_at](#mds_kill_mdstable_at) | `0` | Dev | Dev |
| [mds_kill_openc_at](#mds_kill_openc_at) | `0` | Dev | Dev |
| [mds_kill_rename_at](#mds_kill_rename_at) | `0` | Dev | Dev |
| [mds_kill_shutdown_at](#mds_kill_shutdown_at) | `0` | Dev | Dev |
| [mds_max_completed_flushes](#mds_max_completed_flushes) | `100000` | Dev | Dev |
| [mds_max_completed_requests](#mds_max_completed_requests) | `100000` | Dev | Dev |
| [mds_max_export_size](#mds_max_export_size) | `20_M` | Dev | Dev |
| [mds_max_file_recover](#mds_max_file_recover) | `32` | Advanced | Performance |
| [mds_max_purge_files](#mds_max_purge_files) | `64` | Advanced | Performance |
| [mds_max_purge_ops](#mds_max_purge_ops) | `8_K` | Advanced | Performance |
| [mds_max_purge_ops_per_pg](#mds_max_purge_ops_per_pg) | `0.5` | Advanced | Performance |
| [mds_max_scrub_ops_in_progress](#mds_max_scrub_ops_in_progress) | `5` | Advanced | Performance |
| [mds_max_snaps_per_dir](#mds_max_snaps_per_dir) | `100` | Advanced | Capacity |
| [mds_numa_node](#mds_numa_node) | `-1` | Advanced | Performance |
| [mds_oft_prefetch_dirfrags](#mds_oft_prefetch_dirfrags) | `False` | Advanced | Performance |
| [mds_op_complaint_time](#mds_op_complaint_time) | `30` | Advanced | Performance |
| [mds_op_history_duration](#mds_op_history_duration) | `600` | Advanced | Performance |
| [mds_op_history_size](#mds_op_history_size) | `20` | Advanced | Performance |
| [mds_op_history_slow_op_size](#mds_op_history_slow_op_size) | `20` | Advanced | Performance |
| [mds_op_history_slow_op_threshold](#mds_op_history_slow_op_threshold) | `10` | Advanced | Performance |
| [mds_ping_grace](#mds_ping_grace) | `15` | Advanced | Performance |
| [mds_purge_queue_busy_flush_period](#mds_purge_queue_busy_flush_period) | `1` | Dev | Dev |
| [mds_recall_global_max_decay_threshold](#mds_recall_global_max_decay_threshold) | `128_K` | Advanced | Performance |
| [mds_recall_max_decay_rate](#mds_recall_max_decay_rate) | `1.5` | Advanced | Performance |
| [mds_recall_max_decay_threshold](#mds_recall_max_decay_threshold) | `128_K` | Advanced | Performance |
| [mds_recall_warning_decay_rate](#mds_recall_warning_decay_rate) | `60` | Advanced | Performance |
| [mds_recall_warning_threshold](#mds_recall_warning_threshold) | `256_K` | Advanced | Performance |
| [mds_replay_unsafe_with_closed_session](#mds_replay_unsafe_with_closed_session) | `False` | Advanced | Performance |
| [mds_request_load_average_decay_rate](#mds_request_load_average_decay_rate) | `1_min` | Advanced | Performance |
| [mds_root_ino_gid](#mds_root_ino_gid) | `0` | Advanced | Performance |
| [mds_root_ino_uid](#mds_root_ino_uid) | `0` | Advanced | Performance |
| [mds_scrub_stats_review_period](#mds_scrub_stats_review_period) | `1` | Advanced | Performance |
| [mds_server_dispatch_client_request_delay](#mds_server_dispatch_client_request_delay) | `0` | Dev | Dev |
| [mds_server_dispatch_killpoint_random](#mds_server_dispatch_killpoint_random) | `0.0` | Dev | Dev |
| [mds_session_blocklist_on_evict](#mds_session_blocklist_on_evict) | `True` | Advanced | Performance |
| [mds_session_cache_liveness_decay_rate](#mds_session_cache_liveness_decay_rate) | `5_min` | Advanced | Performance |
| [mds_session_cache_liveness_magnitude](#mds_session_cache_liveness_magnitude) | `10` | Advanced | Performance |
| [mds_session_metadata_threshold](#mds_session_metadata_threshold) | `16_M` | Advanced | Performance |
| [mds_sessionmap_keys_per_op](#mds_sessionmap_keys_per_op) | `1_K` | Advanced | Performance |
| [mds_shutdown_check](#mds_shutdown_check) | `0` | Dev | Dev |
| [mds_skip_ino](#mds_skip_ino) | `0` | Dev | Dev |
| [mds_sleep_rank_change](#mds_sleep_rank_change) | `0.0` | Dev | Dev |
| [mds_snap_max_uid](#mds_snap_max_uid) | `4294967294` | Advanced | Performance |
| [mds_snap_min_uid](#mds_snap_min_uid) | `0` | Advanced | Performance |
| [mds_snap_rstat](#mds_snap_rstat) | `False` | Advanced | Performance |
| [mds_standby_replay_damaged](#mds_standby_replay_damaged) | `False` | Dev | Dev |
| [mds_symlink_recovery](#mds_symlink_recovery) | `True` | Advanced | Performance |
| [mds_thrash_exports](#mds_thrash_exports) | `0` | Dev | Dev |
| [mds_thrash_fragments](#mds_thrash_fragments) | `0` | Dev | Dev |
| [mds_use_global_snaprealm_seq_for_subvol](#mds_use_global_snaprealm_seq_for_subvol) | `True` | Advanced | Performance |
| [mds_valgrind_exit](#mds_valgrind_exit) | `False` | Dev | Dev |
| [mds_verify_backtrace](#mds_verify_backtrace) | `1` | Dev | Dev |
| [mds_verify_scatter](#mds_verify_scatter) | `False` | Dev | Dev |
| [mds_wipe_ino_prealloc](#mds_wipe_ino_prealloc) | `False` | Dev | Dev |
| [mds_wipe_sessions](#mds_wipe_sessions) | `False` | Dev | Dev |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、兼容性、运维默认值 |
| **Capacity** | 磁盘布局、路径、容量规划 |
| **Performance** | 基线 → 逐步调整 → 监控集群 |
| **Connectivity** | 最近且稳定的外部端点 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_abort_on_newly_corrupt_dentry

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_abort_on_newly_corrupt_dentry](../../../config/mds/mds.md#SP_mds_abort_on_newly_corrupt_dentry) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_abort_on_newly_corrupt_dentry false
ceph config get mds mds_abort_on_newly_corrupt_dentry
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_action_on_write_error](../../../config/mds/mds.md#SP_mds_action_on_write_error) |

**作用：** action to take when MDS cannot write to RADOS (0:ignore, 1:read-only, 2:suicide)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_action_on_write_error 1
ceph config get mds mds_action_on_write_error
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_allow_async_dirops](../../../config/mds/mds.md#SP_mds_allow_async_dirops) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_allow_async_dirops false
ceph config get mds mds_allow_async_dirops
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_allow_batched_ops](../../../config/mds/mds.md#SP_mds_allow_batched_ops) |

**作用：** allow MDS to batch lookup/getattr RPCs

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_allow_batched_ops false
ceph config get mds mds_allow_batched_ops
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `8_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_alternate_name_max](../../../config/mds/mds.md#SP_mds_alternate_name_max) |

**作用：** Set the maximum length of alternate names for dentries

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_alternate_name_max 8_K
ceph config get mds mds_alternate_name_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `8_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [mds.md#SP_mds_asio_thread_count](../../../config/mds/mds.md#SP_mds_asio_thread_count) |

**作用：** Size of thread pool for ASIO completions

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_asio_thread_count 2
ceph config get mds mds_asio_thread_count
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_export_pin](../../../config/mds/mds.md#SP_mds_bal_export_pin) |

**作用：** allow setting directory export pins to particular ranks

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_bal_export_pin false
ceph config get mds mds_bal_export_pin
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_fragment_dirs](../../../config/mds/mds.md#SP_mds_bal_fragment_dirs) |

**作用：** enable directory fragmentation

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_bal_fragment_dirs false
ceph config get mds mds_bal_fragment_dirs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1.5` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_fragment_fast_factor](../../../config/mds/mds.md#SP_mds_bal_fragment_fast_factor) |

**作用：** ratio of mds_bal_split_size at which fast fragment splitting occurs

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_fragment_fast_factor 1.5
ceph config get mds mds_bal_fragment_fast_factor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `100000` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_fragment_size_max](../../../config/mds/mds.md#SP_mds_bal_fragment_size_max) |

**作用：** maximum size of a directory fragment before new creat/links fail

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_fragment_size_max 100000
ceph config get mds mds_bal_fragment_size_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_idle_threshold](../../../config/mds/mds.md#SP_mds_bal_idle_threshold) |

**作用：** idle metadata popularity threshold before rebalancing

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_idle_threshold 0
ceph config get mds mds_bal_idle_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_max](../../../config/mds/mds.md#SP_mds_bal_max) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_max 128
ceph config get mds mds_bal_max
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`-1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_max_until

| | |
|---|---|
| 类型 | Int · default `-1` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_max_until](../../../config/mds/mds.md#SP_mds_bal_max_until) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_max_until 128
ceph config get mds mds_bal_max_until
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`-1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_merge_size

| | |
|---|---|
| 类型 | Int · default `50` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_merge_size](../../../config/mds/mds.md#SP_mds_bal_merge_size) |

**作用：** size of fragments where merging should occur

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_merge_size 50
ceph config get mds mds_bal_merge_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.3` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_midchunk](../../../config/mds/mds.md#SP_mds_bal_midchunk) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_midchunk 0.3
ceph config get mds mds_bal_midchunk
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.3`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_min_rebalance

| | |
|---|---|
| 类型 | Float · default `0.1` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_min_rebalance](../../../config/mds/mds.md#SP_mds_bal_min_rebalance) |

**作用：** amount overloaded over internal target before balancer begins offloading

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_min_rebalance 0.1
ceph config get mds mds_bal_min_rebalance
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_min_start

| | |
|---|---|
| 类型 | Float · default `0.2` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_min_start](../../../config/mds/mds.md#SP_mds_bal_min_start) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_min_start 0.2
ceph config get mds mds_bal_min_start
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_minchunk

| | |
|---|---|
| 类型 | Float · default `0.001` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_minchunk](../../../config/mds/mds.md#SP_mds_bal_minchunk) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_minchunk 0.001
ceph config get mds mds_bal_minchunk
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.001`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_mode

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_mode](../../../config/mds/mds.md#SP_mds_bal_mode) |

**作用：** MDS subtree balancer mode (`none`, `normal`, `aggressive`). Controls how aggressively metadata load is migrated between active MDS ranks.

**何时使用：** Use `normal` for multi-active CephFS; `none` for single-MDS or while debugging balance churn.

**示例：**

```bash
ceph config set mds mds_bal_mode normal
ceph fs status
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_need_max

| | |
|---|---|
| 类型 | Float · default `1.2` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_need_max](../../../config/mds/mds.md#SP_mds_bal_need_max) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_need_max 1.2
ceph config get mds mds_bal_need_max
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1.2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_need_min

| | |
|---|---|
| 类型 | Float · default `0.8` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_need_min](../../../config/mds/mds.md#SP_mds_bal_need_min) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_need_min 0.8
ceph config get mds mds_bal_need_min
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.8`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_overload_epochs

| | |
|---|---|
| 类型 | Int · default `2` · **Dev** |
| 表格 | [mds.md#SP_mds_bal_overload_epochs](../../../config/mds/mds.md#SP_mds_bal_overload_epochs) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_bal_overload_epochs 2
ceph config get mds mds_bal_overload_epochs
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_bal_replicate_threshold

| | |
|---|---|
| 类型 | Float · default `8000` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_replicate_threshold](../../../config/mds/mds.md#SP_mds_bal_replicate_threshold) |

**作用：** hot popularity threshold to replicate a subtree

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_replicate_threshold 8000
ceph config get mds mds_bal_replicate_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `8000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_split_bits](../../../config/mds/mds.md#SP_mds_bal_split_bits) |

**作用：** power of two child fragments for a fragment on split

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_split_bits 3
ceph config get mds mds_bal_split_bits
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `24`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `25000` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_split_rd](../../../config/mds/mds.md#SP_mds_bal_split_rd) |

**作用：** hot read popularity threshold for splitting a directory fragment

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_split_rd 25000
ceph config get mds mds_bal_split_rd
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `25000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_split_size](../../../config/mds/mds.md#SP_mds_bal_split_size) |

**作用：** minimum size of directory fragment before splitting

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_split_size 10000
ceph config get mds mds_bal_split_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `10000` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_split_wr](../../../config/mds/mds.md#SP_mds_bal_split_wr) |

**作用：** hot write popularity threshold for splitting a directory fragment

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_split_wr 10000
ceph config get mds mds_bal_split_wr
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_target_decay](../../../config/mds/mds.md#SP_mds_bal_target_decay) |

**作用：** rate of decay for export targets communicated to clients

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_target_decay 10
ceph config get mds mds_bal_target_decay
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_bal_unreplicate_threshold](../../../config/mds/mds.md#SP_mds_bal_unreplicate_threshold) |

**作用：** cold popularity threshold to merge subtrees

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_bal_unreplicate_threshold 0
ceph config get mds mds_bal_unreplicate_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `15` · **Advanced** |
| 表格 | [mds.md#SP_mds_beacon_grace](../../../config/mds/mds.md#SP_mds_beacon_grace) |

**作用：** Seconds the monitor waits after a missed MDS beacon before marking the rank laggy/failed.

**何时使用：** Increase during network maintenance; decrease for faster MDS failover at the cost of false positives on slow nodes.

**示例：**

```bash
ceph config set mds mds_beacon_grace 15
ceph config get mds mds_beacon_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `4_G` · **Basic** |
| 表格 | [mds.md#SP_mds_cache_memory_limit](../../../config/mds/mds.md#SP_mds_cache_memory_limit) |

**作用：** Soft limit on MDS metadata cache memory (bytes). When exceeded, the MDS trims caps and may evict client sessions.

**何时使用：** Raise for large working sets and many files; lower if MDS RSS causes OOM on constrained nodes.

**示例：**

```bash
ceph config set mds mds_cache_memory_limit 4_G
ceph config get mds mds_cache_memory_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4_G` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.7` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_mid](../../../config/mds/mds.md#SP_mds_cache_mid) |

**作用：** Midpoint for MDS cache LRU

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_mid 0.7
ceph config get mds mds_cache_mid
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.7` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_quiesce_decay_rate](../../../config/mds/mds.md#SP_mds_cache_quiesce_decay_rate) |

**作用：** Decay rate for quiescing inodes throttle

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_quiesce_decay_rate 1
ceph config get mds mds_cache_quiesce_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Millisecs · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_cache_quiesce_delay](../../../config/mds/mds.md#SP_mds_cache_quiesce_delay) |

**作用：** Delay before starting recursive quiesce inode operations

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_cache_quiesce_delay 0
ceph config get mds mds_cache_quiesce_delay
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_cache_quiesce_sleep

| | |
|---|---|
| 类型 | Millisecs · default `200` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_quiesce_sleep](../../../config/mds/mds.md#SP_mds_cache_quiesce_sleep) |

**作用：** Sleep time for requests after passing the quiesce threshold

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_cache_quiesce_sleep 200
ceph config get mds mds_cache_quiesce_sleep
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `200` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `512_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_quiesce_threshold](../../../config/mds/mds.md#SP_mds_cache_quiesce_threshold) |

**作用：** Threshold for number of inodes that can be quiesced

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_quiesce_threshold 512_K
ceph config get mds mds_cache_quiesce_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `512_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_reservation](../../../config/mds/mds.md#SP_mds_cache_reservation) |

**作用：** Amount of memory to reserve for future cached objects

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_reservation 0.05
ceph config get mds mds_cache_reservation
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_trim_decay_rate](../../../config/mds/mds.md#SP_mds_cache_trim_decay_rate) |

**作用：** Decay rate for trimming MDS cache throttle

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_trim_decay_rate 1
ceph config get mds mds_cache_trim_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `256_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_trim_threshold](../../../config/mds/mds.md#SP_mds_cache_trim_threshold) |

**作用：** Threshold for number of dentries that can be trimmed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_cache_trim_threshold 256_K
ceph config get mds mds_cache_trim_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `256_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [mds.md#SP_mds_client_delegate_inos_pct](../../../config/mds/mds.md#SP_mds_client_delegate_inos_pct) |

**作用：** percentage of preallocated inos to delegate to client

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_client_delegate_inos_pct 50
ceph config get mds mds_client_delegate_inos_pct
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [mds.md#SP_mds_client_prealloc_inos](../../../config/mds/mds.md#SP_mds_client_prealloc_inos) |

**作用：** number of unused inodes to pre-allocate to clients for file creation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_client_prealloc_inos 1000
ceph config get mds mds_client_prealloc_inos
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_client_writeable_range_max_inc_objs](../../../config/mds/mds.md#SP_mds_client_writeable_range_max_inc_objs) |

**作用：** maximum number of objects in writeable range of a file for a client

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_client_writeable_range_max_inc_objs 1_K
ceph config get mds mds_client_writeable_range_max_inc_objs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_connect_bootstrapping](../../../config/mds/mds.md#SP_mds_connect_bootstrapping) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_connect_bootstrapping true
ceph config get mds mds_connect_bootstrapping
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_damage_table_max_entries

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [mds.md#SP_mds_damage_table_max_entries](../../../config/mds/mds.md#SP_mds_damage_table_max_entries) |

**作用：** maximum number of damage table entries

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_damage_table_max_entries 10000
ceph config get mds mds_damage_table_max_entries
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `/var/lib/ceph/mds/$cluster-$id` · **Advanced** |
| 表格 | [mds.md#SP_mds_data](../../../config/mds/mds.md#SP_mds_data) |

**作用：** Path to MDS data and keyring

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_data "/var/lib/ceph/mds/$cluster-$id"
ceph config get mds mds_data
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `/var/lib/ceph/mds/$cluster-$id` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_decay_halflife](../../../config/mds/mds.md#SP_mds_decay_halflife) |

**作用：** Rate of decay for temperature counters on each directory for balancing

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_decay_halflife 5
ceph config get mds mds_decay_halflife
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [mds.md#SP_mds_default_dir_hash](../../../config/mds/mds.md#SP_mds_default_dir_hash) |

**作用：** hash function to select directory fragment for dentry name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_default_dir_hash 2
ceph config get mds mds_default_dir_hash
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mds.md#SP_mds_defer_session_stale](../../../config/mds/mds.md#SP_mds_defer_session_stale) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_defer_session_stale false
ceph config get mds mds_defer_session_stale
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_delay_journal_replay_for_testing

| | |
|---|---|
| 类型 | Millisecs · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_delay_journal_replay_for_testing](../../../config/mds/mds.md#SP_mds_delay_journal_replay_for_testing) |

**作用：** Delay the journal replay to verify the replay time estimate

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_delay_journal_replay_for_testing 0
ceph config get mds mds_delay_journal_replay_for_testing
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_deny_all_reconnect

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mds.md#SP_mds_deny_all_reconnect](../../../config/mds/mds.md#SP_mds_deny_all_reconnect) |

**作用：** flag to deny all client reconnects during failover

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_deny_all_reconnect true
ceph config get mds mds_deny_all_reconnect
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `16384` · **Advanced** |
| 表格 | [mds.md#SP_mds_dir_keys_per_op](../../../config/mds/mds.md#SP_mds_dir_keys_per_op) |

**作用：** Number of directory entries to read in one RADOS operation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_dir_keys_per_op 16384
ceph config get mds mds_dir_keys_per_op
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16384` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_dir_max_commit_size](../../../config/mds/mds.md#SP_mds_dir_max_commit_size) |

**作用：** Maximum size in mebibytes for a RADOS write to a directory

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_dir_max_commit_size 10
ceph config get mds mds_dir_max_commit_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_dir_max_entries](../../../config/mds/mds.md#SP_mds_dir_max_entries) |

**作用：** maximum number of entries per directory before new creat/links fail

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_dir_max_entries 64
ceph config get mds mds_dir_max_entries
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_dir_prefetch](../../../config/mds/mds.md#SP_mds_dir_prefetch) |

**作用：** flag to prefetch entire dir

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_dir_prefetch false
ceph config get mds mds_dir_prefetch
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_dump_cache_after_rejoin](../../../config/mds/mds.md#SP_mds_dump_cache_after_rejoin) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_dump_cache_after_rejoin true
ceph config get mds mds_dump_cache_after_rejoin
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_dump_cache_on_map

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_dump_cache_on_map](../../../config/mds/mds.md#SP_mds_dump_cache_on_map) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_dump_cache_on_map true
ceph config get mds mds_dump_cache_on_map
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_dump_cache_threshold_file

| | |
|---|---|
| 类型 | Size · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_dump_cache_threshold_file](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_file) |

**作用：** threshold for cache usage to disallow "dump cache" operation to file

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_dump_cache_threshold_file 64
ceph config get mds mds_dump_cache_threshold_file
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_dump_cache_threshold_formatter

| | |
|---|---|
| 类型 | Size · default `1_G` · **Dev** |
| 表格 | [mds.md#SP_mds_dump_cache_threshold_formatter](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_formatter) |

**作用：** threshold for cache usage to disallow "dump cache" operation to formatter

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_dump_cache_threshold_formatter 1_G
ceph config get mds mds_dump_cache_threshold_formatter
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1_G`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_early_reply

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_early_reply](../../../config/mds/mds.md#SP_mds_early_reply) |

**作用：** additional reply to clients that metadata requests are complete but not yet durable

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_early_reply false
ceph config get mds mds_early_reply
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_enable_op_tracker](../../../config/mds/mds.md#SP_mds_enable_op_tracker) |

**作用：** track remote operation progression and statistics

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_enable_op_tracker false
ceph config get mds mds_enable_op_tracker
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_enforce_unique_name](../../../config/mds/mds.md#SP_mds_enforce_unique_name) |

**作用：** Require unique MDS names

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_enforce_unique_name false
ceph config get mds mds_enforce_unique_name
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_export_ephemeral_distributed](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed) |

**作用：** allow ephemeral distributed pinning of the loaded subtrees

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_export_ephemeral_distributed false
ceph config get mds mds_export_ephemeral_distributed
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mds.md#SP_mds_export_ephemeral_distributed_factor](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed_factor) |

**作用：** multiple of max_mds for splitting and distributing directory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_export_ephemeral_distributed_factor 2
ceph config get mds mds_export_ephemeral_distributed_factor
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `100`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_export_ephemeral_random](../../../config/mds/mds.md#SP_mds_export_ephemeral_random) |

**作用：** allow ephemeral random pinning of the loaded subtrees

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_export_ephemeral_random false
ceph config get mds mds_export_ephemeral_random
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.01` · **Advanced** |
| 表格 | [mds.md#SP_mds_export_ephemeral_random_max](../../../config/mds/mds.md#SP_mds_export_ephemeral_random_max) |

**作用：** the maximum percent permitted for random ephemeral pin policy

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_export_ephemeral_random_max 0.01
ceph config get mds mds_export_ephemeral_random_max
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.01` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `1`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `16` · **Advanced** |
| 表格 | [mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans](../../../config/mds/mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans) |

**作用：** Maximum number of concurrent object scans

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_file_blockdiff_max_concurrent_object_scans 16
ceph config get mds mds_file_blockdiff_max_concurrent_object_scans
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `4_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_fscrypt_last_block_max_size](../../../config/mds/mds.md#SP_mds_fscrypt_last_block_max_size) |

**作用：** Maximum size of the last block without the header along with a truncate request when the fscrypt is enabled.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_fscrypt_last_block_max_size 4_K
ceph config get mds mds_fscrypt_last_block_max_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_go_bad_corrupt_dentry](../../../config/mds/mds.md#SP_mds_go_bad_corrupt_dentry) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_go_bad_corrupt_dentry false
ceph config get mds mds_go_bad_corrupt_dentry
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mds.md#SP_mds_hack_allow_loading_invalid_metadata](../../../config/mds/mds.md#SP_mds_hack_allow_loading_invalid_metadata) |

**作用：** INTENTIONALLY CAUSE DATA LOSS by bypasing checks for invalid metadata on disk. Allows testing repair tools.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_hack_allow_loading_invalid_metadata true
ceph config get mds mds_hack_allow_loading_invalid_metadata
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1.5` · **Advanced** |
| 表格 | [mds.md#SP_mds_health_cache_threshold](../../../config/mds/mds.md#SP_mds_health_cache_threshold) |

**作用：** Threshold for cache size to generate health warning

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_health_cache_threshold 1.5
ceph config get mds mds_health_cache_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_health_summarize_threshold](../../../config/mds/mds.md#SP_mds_health_summarize_threshold) |

**作用：** Threshold number of clients to summarize late client recall

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_health_summarize_threshold 10
ceph config get mds mds_health_summarize_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `15` · **Advanced** |
| 表格 | [mds.md#SP_mds_heartbeat_grace](../../../config/mds/mds.md#SP_mds_heartbeat_grace) |

**作用：** Tolerance in seconds for MDS internal heartbeats

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_heartbeat_grace 15
ceph config get mds mds_heartbeat_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1000` · **Advanced** |
| 表格 | [mds.md#SP_mds_heartbeat_reset_grace](../../../config/mds/mds.md#SP_mds_heartbeat_reset_grace) |

**作用：** Tolerance in seconds for long-running MDS operations which do not periodically reset the heartbeat timeout.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_heartbeat_reset_grace 1000
ceph config get mds mds_heartbeat_reset_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Str · default `(empty)` · **Basic** |
| 表格 | [mds.md#SP_mds_join_fs](../../../config/mds/mds.md#SP_mds_join_fs) |

**作用：** File system MDS prefers to join

**何时使用：** 核心 MDS 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set mds mds_join_fs "example"
ceph config get mds mds_join_fs
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `(empty)` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Dev** |
| 表格 | [mds.md#SP_mds_journal_format](../../../config/mds/mds.md#SP_mds_journal_format) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_journal_format 1
ceph config get mds mds_journal_format
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_create_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_create_at](../../../config/mds/mds.md#SP_mds_kill_create_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_create_at 64
ceph config get mds mds_kill_create_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_dirfrag_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_dirfrag_at](../../../config/mds/mds.md#SP_mds_kill_dirfrag_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_dirfrag_at 64
ceph config get mds mds_kill_dirfrag_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_export_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_export_at](../../../config/mds/mds.md#SP_mds_kill_export_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_export_at 64
ceph config get mds mds_kill_export_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_import_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_import_at](../../../config/mds/mds.md#SP_mds_kill_import_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_import_at 64
ceph config get mds mds_kill_import_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_journal_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_journal_at](../../../config/mds/mds.md#SP_mds_kill_journal_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_journal_at 64
ceph config get mds mds_kill_journal_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_journal_expire_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_journal_expire_at](../../../config/mds/mds.md#SP_mds_kill_journal_expire_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_journal_expire_at 64
ceph config get mds mds_kill_journal_expire_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_journal_replay_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_journal_replay_at](../../../config/mds/mds.md#SP_mds_kill_journal_replay_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_journal_replay_at 64
ceph config get mds mds_kill_journal_replay_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_link_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_link_at](../../../config/mds/mds.md#SP_mds_kill_link_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_link_at 64
ceph config get mds mds_kill_link_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_mdstable_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_mdstable_at](../../../config/mds/mds.md#SP_mds_kill_mdstable_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_mdstable_at 64
ceph config get mds mds_kill_mdstable_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_openc_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_openc_at](../../../config/mds/mds.md#SP_mds_kill_openc_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_openc_at 64
ceph config get mds mds_kill_openc_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_rename_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_rename_at](../../../config/mds/mds.md#SP_mds_kill_rename_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_rename_at 64
ceph config get mds mds_kill_rename_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_kill_shutdown_at

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_kill_shutdown_at](../../../config/mds/mds.md#SP_mds_kill_shutdown_at) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_kill_shutdown_at 64
ceph config get mds mds_kill_shutdown_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_max_completed_flushes

| | |
|---|---|
| 类型 | Uint · default `100000` · **Dev** |
| 表格 | [mds.md#SP_mds_max_completed_flushes](../../../config/mds/mds.md#SP_mds_max_completed_flushes) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_max_completed_flushes 100000
ceph config get mds mds_max_completed_flushes
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`100000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_max_completed_requests

| | |
|---|---|
| 类型 | Uint · default `100000` · **Dev** |
| 表格 | [mds.md#SP_mds_max_completed_requests](../../../config/mds/mds.md#SP_mds_max_completed_requests) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_max_completed_requests 100000
ceph config get mds mds_max_completed_requests
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`100000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_max_export_size

| | |
|---|---|
| 类型 | Size · default `20_M` · **Dev** |
| 表格 | [mds.md#SP_mds_max_export_size](../../../config/mds/mds.md#SP_mds_max_export_size) |

**作用：** Maximum size (bytes) of a single subtree export during MDS rebalancing.

**何时使用：** Lower to reduce latency spikes during balance; raise for faster migration on high-bandwidth networks.

**示例：**

```bash
ceph config set mds mds_max_export_size 20_M
ceph config get mds mds_max_export_size
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`20_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_max_file_recover

| | |
|---|---|
| 类型 | Uint · default `32` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_file_recover](../../../config/mds/mds.md#SP_mds_max_file_recover) |

**作用：** Maximum number of files for which to recover file sizes in parallel

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_file_recover 32
ceph config get mds mds_max_file_recover
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `32` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `64` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_purge_files](../../../config/mds/mds.md#SP_mds_max_purge_files) |

**作用：** maximum number of deleted files to purge in parallel

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_purge_files 64
ceph config get mds mds_max_purge_files
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `64` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `8_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_purge_ops](../../../config/mds/mds.md#SP_mds_max_purge_ops) |

**作用：** maximum number of purge operations performed in parallel

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_purge_ops 8_K
ceph config get mds mds_max_purge_ops
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `8_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_purge_ops_per_pg](../../../config/mds/mds.md#SP_mds_max_purge_ops_per_pg) |

**作用：** number of parallel purge operations performed per PG

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_purge_ops_per_pg 0.5
ceph config get mds mds_max_purge_ops_per_pg
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_scrub_ops_in_progress](../../../config/mds/mds.md#SP_mds_max_scrub_ops_in_progress) |

**作用：** maximum number of scrub operations performed in parallel

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_scrub_ops_in_progress 5
ceph config get mds mds_max_scrub_ops_in_progress
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_snaps_per_dir](../../../config/mds/mds.md#SP_mds_max_snaps_per_dir) |

**作用：** max snapshots per directory

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_snaps_per_dir 100
ceph config get mds mds_max_snaps_per_dir
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `100` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `-1` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mds.md#SP_mds_numa_node](../../../config/mds/mds.md#SP_mds_numa_node) |

**作用：** Set MDS CPU affinity to a NUMA node (-1 for none)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_numa_node 128
ceph config get mds mds_numa_node
ceph orch restart mds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mds.md#SP_mds_oft_prefetch_dirfrags](../../../config/mds/mds.md#SP_mds_oft_prefetch_dirfrags) |

**作用：** prefetch dirfrags recorded in open file table on startup

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_oft_prefetch_dirfrags true
ceph config get mds mds_oft_prefetch_dirfrags
ceph orch restart mds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [mds.md#SP_mds_op_complaint_time](../../../config/mds/mds.md#SP_mds_op_complaint_time) |

**作用：** time in seconds to consider an operation blocked after no updates

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_op_complaint_time 30
ceph config get mds mds_op_complaint_time
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `600` · **Advanced** |
| 表格 | [mds.md#SP_mds_op_history_duration](../../../config/mds/mds.md#SP_mds_op_history_duration) |

**作用：** expiration time in seconds of historical operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_op_history_duration 600
ceph config get mds mds_op_history_duration
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `600` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mds.md#SP_mds_op_history_size](../../../config/mds/mds.md#SP_mds_op_history_size) |

**作用：** maximum size for list of historical operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_op_history_size 20
ceph config get mds mds_op_history_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `20` · **Advanced** |
| 表格 | [mds.md#SP_mds_op_history_slow_op_size](../../../config/mds/mds.md#SP_mds_op_history_slow_op_size) |

**作用：** maximum size for list of historical slow operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_op_history_slow_op_size 20
ceph config get mds mds_op_history_slow_op_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `20` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_op_history_slow_op_threshold](../../../config/mds/mds.md#SP_mds_op_history_slow_op_threshold) |

**作用：** track the op if over this threshold

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_op_history_slow_op_threshold 10
ceph config get mds mds_op_history_slow_op_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Secs · default `15` · **Advanced** |
| 表格 | [mds.md#SP_mds_ping_grace](../../../config/mds/mds.md#SP_mds_ping_grace) |

**作用：** timeout after which an MDS is considered laggy by rank 0 MDS.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_ping_grace 15
ceph config get mds mds_ping_grace
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1` · **Dev** |
| 表格 | [mds.md#SP_mds_purge_queue_busy_flush_period](../../../config/mds/mds.md#SP_mds_purge_queue_busy_flush_period) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_purge_queue_busy_flush_period 1
ceph config get mds mds_purge_queue_busy_flush_period
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_recall_global_max_decay_threshold

| | |
|---|---|
| 类型 | Size · default `128_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_global_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_global_max_decay_threshold) |

**作用：** Decay threshold for throttle on recalled caps globally

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_recall_global_max_decay_threshold 128_K
ceph config get mds mds_recall_global_max_decay_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `128_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1.5` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_max_decay_rate](../../../config/mds/mds.md#SP_mds_recall_max_decay_rate) |

**作用：** Decay rate for throttle on recalled caps on a session

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_recall_max_decay_rate 1.5
ceph config get mds mds_recall_max_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `128_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_max_decay_threshold) |

**作用：** Decay threshold for throttle on recalled caps on a session

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_recall_max_decay_threshold 128_K
ceph config get mds mds_recall_max_decay_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `128_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `60` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_warning_decay_rate](../../../config/mds/mds.md#SP_mds_recall_warning_decay_rate) |

**作用：** Decay rate for warning on slow session cap recall

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_recall_warning_decay_rate 60
ceph config get mds mds_recall_warning_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `60` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `256_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_warning_threshold](../../../config/mds/mds.md#SP_mds_recall_warning_threshold) |

**作用：** Decay threshold for warning on slow session cap recall

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_recall_warning_threshold 256_K
ceph config get mds mds_recall_warning_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `256_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mds.md#SP_mds_replay_unsafe_with_closed_session](../../../config/mds/mds.md#SP_mds_replay_unsafe_with_closed_session) |

**作用：** complete all the replay request when mds is restarted, no matter the session is closed or not

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_replay_unsafe_with_closed_session true
ceph config get mds mds_replay_unsafe_with_closed_session
ceph orch restart mds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `1_min` · **Advanced** |
| 表格 | [mds.md#SP_mds_request_load_average_decay_rate](../../../config/mds/mds.md#SP_mds_request_load_average_decay_rate) |

**作用：** rate of decay in seconds for calculating request load average

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_request_load_average_decay_rate 1_min
ceph config get mds mds_request_load_average_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_root_ino_gid](../../../config/mds/mds.md#SP_mds_root_ino_gid) |

**作用：** default gid for new root directory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_root_ino_gid 64
ceph config get mds mds_root_ino_gid
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_root_ino_uid](../../../config/mds/mds.md#SP_mds_root_ino_uid) |

**作用：** default uid for new root directory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_root_ino_uid 64
ceph config get mds mds_root_ino_uid
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [mds.md#SP_mds_scrub_stats_review_period](../../../config/mds/mds.md#SP_mds_scrub_stats_review_period) |

**作用：** Period for which scrub stats will be available for review.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mds mds_scrub_stats_review_period 1
ceph config get mds mds_scrub_stats_review_period
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `60`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Millisecs · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_server_dispatch_client_request_delay](../../../config/mds/mds.md#SP_mds_server_dispatch_client_request_delay) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_server_dispatch_client_request_delay 0
ceph config get mds mds_server_dispatch_client_request_delay
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_server_dispatch_killpoint_random

| | |
|---|---|
| 类型 | Float · default `0.0` · **Dev** |
| 表格 | [mds.md#SP_mds_server_dispatch_killpoint_random](../../../config/mds/mds.md#SP_mds_server_dispatch_killpoint_random) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_server_dispatch_killpoint_random 0.0
ceph config get mds mds_server_dispatch_killpoint_random
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_session_blocklist_on_evict

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_blocklist_on_evict](../../../config/mds/mds.md#SP_mds_session_blocklist_on_evict) |

**作用：** Blocklist clients that have been evicted

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_session_blocklist_on_evict false
ceph config get mds mds_session_blocklist_on_evict
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Float · default `5_min` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_cache_liveness_decay_rate](../../../config/mds/mds.md#SP_mds_session_cache_liveness_decay_rate) |

**作用：** Decay rate for session liveness leading to preemptive cap recall

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_session_cache_liveness_decay_rate 5_min
ceph config get mds mds_session_cache_liveness_decay_rate
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `10` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_cache_liveness_magnitude](../../../config/mds/mds.md#SP_mds_session_cache_liveness_magnitude) |

**作用：** Decay magnitude for preemptively recalling caps on quiet client

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_session_cache_liveness_magnitude 10
ceph config get mds mds_session_cache_liveness_magnitude
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_metadata_threshold](../../../config/mds/mds.md#SP_mds_session_metadata_threshold) |

**作用：** Evict non-advancing client-tid sessions exceeding the config size.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_session_metadata_threshold 16_M
ceph config get mds mds_session_metadata_threshold
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `16_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [mds.md#SP_mds_sessionmap_keys_per_op](../../../config/mds/mds.md#SP_mds_sessionmap_keys_per_op) |

**作用：** Number of omap keys to read from the SessionMap in one operation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mds mds_sessionmap_keys_per_op 1_K
ceph config get mds mds_sessionmap_keys_per_op
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_shutdown_check](../../../config/mds/mds.md#SP_mds_shutdown_check) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_shutdown_check 64
ceph config get mds mds_shutdown_check
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_skip_ino

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_skip_ino](../../../config/mds/mds.md#SP_mds_skip_ino) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_skip_ino 64
ceph config get mds mds_skip_ino
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_sleep_rank_change

| | |
|---|---|
| 类型 | Float · default `0.0` · **Dev** |
| 表格 | [mds.md#SP_mds_sleep_rank_change](../../../config/mds/mds.md#SP_mds_sleep_rank_change) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_sleep_rank_change 0.0
ceph config get mds mds_sleep_rank_change
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0.0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_snap_max_uid

| | |
|---|---|
| 类型 | Uint · default `4294967294` · **Advanced** |
| 表格 | [mds.md#SP_mds_snap_max_uid](../../../config/mds/mds.md#SP_mds_snap_max_uid) |

**作用：** maximum uid of client to perform snapshots

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_snap_max_uid 4294967294
ceph config get mds mds_snap_max_uid
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `4294967294` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_snap_min_uid](../../../config/mds/mds.md#SP_mds_snap_min_uid) |

**作用：** minimum uid of client to perform snapshots

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_snap_min_uid 64
ceph config get mds mds_snap_min_uid
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mds.md#SP_mds_snap_rstat](../../../config/mds/mds.md#SP_mds_snap_rstat) |

**作用：** enabled nested rstat for snapshots

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_snap_rstat true
ceph config get mds mds_snap_rstat
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_standby_replay_damaged](../../../config/mds/mds.md#SP_mds_standby_replay_damaged) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_standby_replay_damaged true
ceph config get mds mds_standby_replay_damaged
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_symlink_recovery

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_symlink_recovery](../../../config/mds/mds.md#SP_mds_symlink_recovery) |

**作用：** Stores symlink target on the first data object of symlink file. Allows recover of symlink using recovery tools.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_symlink_recovery false
ceph config get mds mds_symlink_recovery
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_thrash_exports](../../../config/mds/mds.md#SP_mds_thrash_exports) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_thrash_exports 64
ceph config get mds mds_thrash_exports
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_thrash_fragments

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mds.md#SP_mds_thrash_fragments](../../../config/mds/mds.md#SP_mds_thrash_fragments) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_thrash_fragments 64
ceph config get mds mds_thrash_fragments
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_use_global_snaprealm_seq_for_subvol

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_use_global_snaprealm_seq_for_subvol](../../../config/mds/mds.md#SP_mds_use_global_snaprealm_seq_for_subvol) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_use_global_snaprealm_seq_for_subvol false
ceph config get mds mds_use_global_snaprealm_seq_for_subvol
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

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
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_valgrind_exit](../../../config/mds/mds.md#SP_mds_valgrind_exit) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_valgrind_exit true
ceph config get mds mds_valgrind_exit
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_verify_backtrace

| | |
|---|---|
| 类型 | Uint · default `1` · **Dev** |
| 表格 | [mds.md#SP_mds_verify_backtrace](../../../config/mds/mds.md#SP_mds_verify_backtrace) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_verify_backtrace 1
ceph config get mds mds_verify_backtrace
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_verify_scatter

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_verify_scatter](../../../config/mds/mds.md#SP_mds_verify_scatter) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_verify_scatter true
ceph config get mds mds_verify_scatter
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_wipe_ino_prealloc

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_wipe_ino_prealloc](../../../config/mds/mds.md#SP_mds_wipe_ino_prealloc) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_wipe_ino_prealloc true
ceph config get mds mds_wipe_ino_prealloc
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_wipe_sessions

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_wipe_sessions](../../../config/mds/mds.md#SP_mds_wipe_sessions) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_wipe_sessions true
ceph config get mds mds_wipe_sessions
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
