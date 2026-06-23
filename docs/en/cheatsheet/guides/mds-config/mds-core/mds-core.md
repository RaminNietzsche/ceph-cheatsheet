# Metadata server core

MDS config deep dive — 138 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
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

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_abort_on_newly_corrupt_dentry

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_abort_on_newly_corrupt_dentry](../../../config/mds/mds.md#SP_mds_abort_on_newly_corrupt_dentry) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_abort_on_newly_corrupt_dentry false
ceph config get mds mds_abort_on_newly_corrupt_dentry
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_action_on_write_error](../../../config/mds/mds.md#SP_mds_action_on_write_error) |

**What it does:** action to take when MDS cannot write to RADOS (0:ignore, 1:read-only, 2:suicide)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_action_on_write_error 1
ceph config get mds mds_action_on_write_error
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_allow_async_dirops](../../../config/mds/mds.md#SP_mds_allow_async_dirops) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_allow_async_dirops false
ceph config get mds mds_allow_async_dirops
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_allow_batched_ops](../../../config/mds/mds.md#SP_mds_allow_batched_ops) |

**What it does:** allow MDS to batch lookup/getattr RPCs

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_allow_batched_ops false
ceph config get mds mds_allow_batched_ops
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `8_K` · **Advanced** |
| Table | [mds.md#SP_mds_alternate_name_max](../../../config/mds/mds.md#SP_mds_alternate_name_max) |

**What it does:** Set the maximum length of alternate names for dentries

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_alternate_name_max 8_K
ceph config get mds mds_alternate_name_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `2` · **Advanced** |
| Table | [mds.md#SP_mds_asio_thread_count](../../../config/mds/mds.md#SP_mds_asio_thread_count) |

**What it does:** Size of thread pool for ASIO completions

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_asio_thread_count 2
ceph config get mds mds_asio_thread_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_bal_export_pin](../../../config/mds/mds.md#SP_mds_bal_export_pin) |

**What it does:** allow setting directory export pins to particular ranks

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_bal_export_pin false
ceph config get mds mds_bal_export_pin
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_bal_fragment_dirs](../../../config/mds/mds.md#SP_mds_bal_fragment_dirs) |

**What it does:** enable directory fragmentation

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_bal_fragment_dirs false
ceph config get mds mds_bal_fragment_dirs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1.5` · **Advanced** |
| Table | [mds.md#SP_mds_bal_fragment_fast_factor](../../../config/mds/mds.md#SP_mds_bal_fragment_fast_factor) |

**What it does:** ratio of mds_bal_split_size at which fast fragment splitting occurs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_fragment_fast_factor 1.5
ceph config get mds mds_bal_fragment_fast_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `100000` · **Advanced** |
| Table | [mds.md#SP_mds_bal_fragment_size_max](../../../config/mds/mds.md#SP_mds_bal_fragment_size_max) |

**What it does:** maximum size of a directory fragment before new creat/links fail

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_fragment_size_max 100000
ceph config get mds mds_bal_fragment_size_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_bal_idle_threshold](../../../config/mds/mds.md#SP_mds_bal_idle_threshold) |

**What it does:** idle metadata popularity threshold before rebalancing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_idle_threshold 0
ceph config get mds mds_bal_idle_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `-1` · **Dev** |
| Table | [mds.md#SP_mds_bal_max](../../../config/mds/mds.md#SP_mds_bal_max) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_max 128
ceph config get mds mds_bal_max
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_max_until

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [mds.md#SP_mds_bal_max_until](../../../config/mds/mds.md#SP_mds_bal_max_until) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_max_until 128
ceph config get mds mds_bal_max_until
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_merge_size

| | |
|---|---|
| Type | Int · default `50` · **Advanced** |
| Table | [mds.md#SP_mds_bal_merge_size](../../../config/mds/mds.md#SP_mds_bal_merge_size) |

**What it does:** size of fragments where merging should occur

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_merge_size 50
ceph config get mds mds_bal_merge_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0.3` · **Dev** |
| Table | [mds.md#SP_mds_bal_midchunk](../../../config/mds/mds.md#SP_mds_bal_midchunk) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_midchunk 0.3
ceph config get mds mds_bal_midchunk
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.3`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_min_rebalance

| | |
|---|---|
| Type | Float · default `0.1` · **Dev** |
| Table | [mds.md#SP_mds_bal_min_rebalance](../../../config/mds/mds.md#SP_mds_bal_min_rebalance) |

**What it does:** amount overloaded over internal target before balancer begins offloading

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_min_rebalance 0.1
ceph config get mds mds_bal_min_rebalance
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_min_start

| | |
|---|---|
| Type | Float · default `0.2` · **Dev** |
| Table | [mds.md#SP_mds_bal_min_start](../../../config/mds/mds.md#SP_mds_bal_min_start) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_min_start 0.2
ceph config get mds mds_bal_min_start
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_minchunk

| | |
|---|---|
| Type | Float · default `0.001` · **Dev** |
| Table | [mds.md#SP_mds_bal_minchunk](../../../config/mds/mds.md#SP_mds_bal_minchunk) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_minchunk 0.001
ceph config get mds mds_bal_minchunk
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.001`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_mode

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_bal_mode](../../../config/mds/mds.md#SP_mds_bal_mode) |

**What it does:** MDS subtree balancer mode (`none`, `normal`, `aggressive`). Controls how aggressively metadata load is migrated between active MDS ranks.

**When to use:** Use `normal` for multi-active CephFS; `none` for single-MDS or while debugging balance churn.

**Example:**

```bash
ceph config set mds mds_bal_mode normal
ceph fs status
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_need_max

| | |
|---|---|
| Type | Float · default `1.2` · **Dev** |
| Table | [mds.md#SP_mds_bal_need_max](../../../config/mds/mds.md#SP_mds_bal_need_max) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_need_max 1.2
ceph config get mds mds_bal_need_max
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1.2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_need_min

| | |
|---|---|
| Type | Float · default `0.8` · **Dev** |
| Table | [mds.md#SP_mds_bal_need_min](../../../config/mds/mds.md#SP_mds_bal_need_min) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_need_min 0.8
ceph config get mds mds_bal_need_min
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.8`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_overload_epochs

| | |
|---|---|
| Type | Int · default `2` · **Dev** |
| Table | [mds.md#SP_mds_bal_overload_epochs](../../../config/mds/mds.md#SP_mds_bal_overload_epochs) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_bal_overload_epochs 2
ceph config get mds mds_bal_overload_epochs
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_bal_replicate_threshold

| | |
|---|---|
| Type | Float · default `8000` · **Advanced** |
| Table | [mds.md#SP_mds_bal_replicate_threshold](../../../config/mds/mds.md#SP_mds_bal_replicate_threshold) |

**What it does:** hot popularity threshold to replicate a subtree

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_replicate_threshold 8000
ceph config get mds mds_bal_replicate_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `3` · **Advanced** |
| Table | [mds.md#SP_mds_bal_split_bits](../../../config/mds/mds.md#SP_mds_bal_split_bits) |

**What it does:** power of two child fragments for a fragment on split

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_split_bits 3
ceph config get mds mds_bal_split_bits
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `24`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `25000` · **Advanced** |
| Table | [mds.md#SP_mds_bal_split_rd](../../../config/mds/mds.md#SP_mds_bal_split_rd) |

**What it does:** hot read popularity threshold for splitting a directory fragment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_split_rd 25000
ceph config get mds mds_bal_split_rd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `25000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `10000` · **Advanced** |
| Table | [mds.md#SP_mds_bal_split_size](../../../config/mds/mds.md#SP_mds_bal_split_size) |

**What it does:** minimum size of directory fragment before splitting

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_split_size 10000
ceph config get mds mds_bal_split_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `10000` · **Advanced** |
| Table | [mds.md#SP_mds_bal_split_wr](../../../config/mds/mds.md#SP_mds_bal_split_wr) |

**What it does:** hot write popularity threshold for splitting a directory fragment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_split_wr 10000
ceph config get mds mds_bal_split_wr
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_bal_target_decay](../../../config/mds/mds.md#SP_mds_bal_target_decay) |

**What it does:** rate of decay for export targets communicated to clients

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_target_decay 10
ceph config get mds mds_bal_target_decay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_bal_unreplicate_threshold](../../../config/mds/mds.md#SP_mds_bal_unreplicate_threshold) |

**What it does:** cold popularity threshold to merge subtrees

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_bal_unreplicate_threshold 0
ceph config get mds mds_bal_unreplicate_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `15` · **Advanced** |
| Table | [mds.md#SP_mds_beacon_grace](../../../config/mds/mds.md#SP_mds_beacon_grace) |

**What it does:** Seconds the monitor waits after a missed MDS beacon before marking the rank laggy/failed.

**When to use:** Increase during network maintenance; decrease for faster MDS failover at the cost of false positives on slow nodes.

**Example:**

```bash
ceph config set mds mds_beacon_grace 15
ceph config get mds mds_beacon_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `4_G` · **Basic** |
| Table | [mds.md#SP_mds_cache_memory_limit](../../../config/mds/mds.md#SP_mds_cache_memory_limit) |

**What it does:** Soft limit on MDS metadata cache memory (bytes). When exceeded, the MDS trims caps and may evict client sessions.

**When to use:** Raise for large working sets and many files; lower if MDS RSS causes OOM on constrained nodes.

**Example:**

```bash
ceph config set mds mds_cache_memory_limit 4_G
ceph config get mds mds_cache_memory_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0.7` · **Advanced** |
| Table | [mds.md#SP_mds_cache_mid](../../../config/mds/mds.md#SP_mds_cache_mid) |

**What it does:** Midpoint for MDS cache LRU

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_mid 0.7
ceph config get mds mds_cache_mid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.7`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_cache_quiesce_decay_rate](../../../config/mds/mds.md#SP_mds_cache_quiesce_decay_rate) |

**What it does:** Decay rate for quiescing inodes throttle

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_quiesce_decay_rate 1
ceph config get mds mds_cache_quiesce_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Millisecs · default `0` · **Dev** |
| Table | [mds.md#SP_mds_cache_quiesce_delay](../../../config/mds/mds.md#SP_mds_cache_quiesce_delay) |

**What it does:** Delay before starting recursive quiesce inode operations

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_cache_quiesce_delay 0
ceph config get mds mds_cache_quiesce_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_cache_quiesce_sleep

| | |
|---|---|
| Type | Millisecs · default `200` · **Advanced** |
| Table | [mds.md#SP_mds_cache_quiesce_sleep](../../../config/mds/mds.md#SP_mds_cache_quiesce_sleep) |

**What it does:** Sleep time for requests after passing the quiesce threshold

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_cache_quiesce_sleep 200
ceph config get mds mds_cache_quiesce_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `512_K` · **Advanced** |
| Table | [mds.md#SP_mds_cache_quiesce_threshold](../../../config/mds/mds.md#SP_mds_cache_quiesce_threshold) |

**What it does:** Threshold for number of inodes that can be quiesced

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_quiesce_threshold 512_K
ceph config get mds mds_cache_quiesce_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0.05` · **Advanced** |
| Table | [mds.md#SP_mds_cache_reservation](../../../config/mds/mds.md#SP_mds_cache_reservation) |

**What it does:** Amount of memory to reserve for future cached objects

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_reservation 0.05
ceph config get mds mds_cache_reservation
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_cache_trim_decay_rate](../../../config/mds/mds.md#SP_mds_cache_trim_decay_rate) |

**What it does:** Decay rate for trimming MDS cache throttle

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_trim_decay_rate 1
ceph config get mds mds_cache_trim_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `256_K` · **Advanced** |
| Table | [mds.md#SP_mds_cache_trim_threshold](../../../config/mds/mds.md#SP_mds_cache_trim_threshold) |

**What it does:** Threshold for number of dentries that can be trimmed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_cache_trim_threshold 256_K
ceph config get mds mds_cache_trim_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `50` · **Advanced** |
| Table | [mds.md#SP_mds_client_delegate_inos_pct](../../../config/mds/mds.md#SP_mds_client_delegate_inos_pct) |

**What it does:** percentage of preallocated inos to delegate to client

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_client_delegate_inos_pct 50
ceph config get mds mds_client_delegate_inos_pct
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `1000` · **Advanced** |
| Table | [mds.md#SP_mds_client_prealloc_inos](../../../config/mds/mds.md#SP_mds_client_prealloc_inos) |

**What it does:** number of unused inodes to pre-allocate to clients for file creation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_client_prealloc_inos 1000
ceph config get mds mds_client_prealloc_inos
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1_K` · **Advanced** |
| Table | [mds.md#SP_mds_client_writeable_range_max_inc_objs](../../../config/mds/mds.md#SP_mds_client_writeable_range_max_inc_objs) |

**What it does:** maximum number of objects in writeable range of a file for a client

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_client_writeable_range_max_inc_objs 1_K
ceph config get mds mds_client_writeable_range_max_inc_objs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_connect_bootstrapping](../../../config/mds/mds.md#SP_mds_connect_bootstrapping) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_connect_bootstrapping true
ceph config get mds mds_connect_bootstrapping
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_damage_table_max_entries

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [mds.md#SP_mds_damage_table_max_entries](../../../config/mds/mds.md#SP_mds_damage_table_max_entries) |

**What it does:** maximum number of damage table entries

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_damage_table_max_entries 10000
ceph config get mds mds_damage_table_max_entries
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Str · default `/var/lib/ceph/mds/$cluster-$id` · **Advanced** |
| Table | [mds.md#SP_mds_data](../../../config/mds/mds.md#SP_mds_data) |

**What it does:** Path to MDS data and keyring

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_data "/var/lib/ceph/mds/$cluster-$id"
ceph config get mds mds_data
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/mds/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_decay_halflife](../../../config/mds/mds.md#SP_mds_decay_halflife) |

**What it does:** Rate of decay for temperature counters on each directory for balancing

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_decay_halflife 5
ceph config get mds mds_decay_halflife
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `2` · **Advanced** |
| Table | [mds.md#SP_mds_default_dir_hash](../../../config/mds/mds.md#SP_mds_default_dir_hash) |

**What it does:** hash function to select directory fragment for dentry name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_default_dir_hash 2
ceph config get mds mds_default_dir_hash
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Dev** |
| Table | [mds.md#SP_mds_defer_session_stale](../../../config/mds/mds.md#SP_mds_defer_session_stale) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_defer_session_stale false
ceph config get mds mds_defer_session_stale
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_delay_journal_replay_for_testing

| | |
|---|---|
| Type | Millisecs · default `0` · **Dev** |
| Table | [mds.md#SP_mds_delay_journal_replay_for_testing](../../../config/mds/mds.md#SP_mds_delay_journal_replay_for_testing) |

**What it does:** Delay the journal replay to verify the replay time estimate

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_delay_journal_replay_for_testing 0
ceph config get mds mds_delay_journal_replay_for_testing
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_deny_all_reconnect

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mds.md#SP_mds_deny_all_reconnect](../../../config/mds/mds.md#SP_mds_deny_all_reconnect) |

**What it does:** flag to deny all client reconnects during failover

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_deny_all_reconnect true
ceph config get mds mds_deny_all_reconnect
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `16384` · **Advanced** |
| Table | [mds.md#SP_mds_dir_keys_per_op](../../../config/mds/mds.md#SP_mds_dir_keys_per_op) |

**What it does:** Number of directory entries to read in one RADOS operation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_dir_keys_per_op 16384
ceph config get mds mds_dir_keys_per_op
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16384`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_dir_max_commit_size](../../../config/mds/mds.md#SP_mds_dir_max_commit_size) |

**What it does:** Maximum size in mebibytes for a RADOS write to a directory

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_dir_max_commit_size 10
ceph config get mds mds_dir_max_commit_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_dir_max_entries](../../../config/mds/mds.md#SP_mds_dir_max_entries) |

**What it does:** maximum number of entries per directory before new creat/links fail

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_dir_max_entries 64
ceph config get mds mds_dir_max_entries
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_dir_prefetch](../../../config/mds/mds.md#SP_mds_dir_prefetch) |

**What it does:** flag to prefetch entire dir

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_dir_prefetch false
ceph config get mds mds_dir_prefetch
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_dump_cache_after_rejoin](../../../config/mds/mds.md#SP_mds_dump_cache_after_rejoin) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_dump_cache_after_rejoin true
ceph config get mds mds_dump_cache_after_rejoin
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_dump_cache_on_map

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_dump_cache_on_map](../../../config/mds/mds.md#SP_mds_dump_cache_on_map) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_dump_cache_on_map true
ceph config get mds mds_dump_cache_on_map
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_dump_cache_threshold_file

| | |
|---|---|
| Type | Size · default `0` · **Dev** |
| Table | [mds.md#SP_mds_dump_cache_threshold_file](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_file) |

**What it does:** threshold for cache usage to disallow "dump cache" operation to file

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_dump_cache_threshold_file 64
ceph config get mds mds_dump_cache_threshold_file
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_dump_cache_threshold_formatter

| | |
|---|---|
| Type | Size · default `1_G` · **Dev** |
| Table | [mds.md#SP_mds_dump_cache_threshold_formatter](../../../config/mds/mds.md#SP_mds_dump_cache_threshold_formatter) |

**What it does:** threshold for cache usage to disallow "dump cache" operation to formatter

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_dump_cache_threshold_formatter 1_G
ceph config get mds mds_dump_cache_threshold_formatter
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_G`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_early_reply

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_early_reply](../../../config/mds/mds.md#SP_mds_early_reply) |

**What it does:** additional reply to clients that metadata requests are complete but not yet durable

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_early_reply false
ceph config get mds mds_early_reply
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_enable_op_tracker](../../../config/mds/mds.md#SP_mds_enable_op_tracker) |

**What it does:** track remote operation progression and statistics

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_enable_op_tracker false
ceph config get mds mds_enable_op_tracker
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_enforce_unique_name](../../../config/mds/mds.md#SP_mds_enforce_unique_name) |

**What it does:** Require unique MDS names

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_enforce_unique_name false
ceph config get mds mds_enforce_unique_name
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_export_ephemeral_distributed](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed) |

**What it does:** allow ephemeral distributed pinning of the loaded subtrees

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_export_ephemeral_distributed false
ceph config get mds mds_export_ephemeral_distributed
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `2` · **Advanced** |
| Table | [mds.md#SP_mds_export_ephemeral_distributed_factor](../../../config/mds/mds.md#SP_mds_export_ephemeral_distributed_factor) |

**What it does:** multiple of max_mds for splitting and distributing directory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_export_ephemeral_distributed_factor 2
ceph config get mds mds_export_ephemeral_distributed_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `100`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_export_ephemeral_random](../../../config/mds/mds.md#SP_mds_export_ephemeral_random) |

**What it does:** allow ephemeral random pinning of the loaded subtrees

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_export_ephemeral_random false
ceph config get mds mds_export_ephemeral_random
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0.01` · **Advanced** |
| Table | [mds.md#SP_mds_export_ephemeral_random_max](../../../config/mds/mds.md#SP_mds_export_ephemeral_random_max) |

**What it does:** the maximum percent permitted for random ephemeral pin policy

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_export_ephemeral_random_max 0.01
ceph config get mds mds_export_ephemeral_random_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.01`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `1`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `16` · **Advanced** |
| Table | [mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans](../../../config/mds/mds.md#SP_mds_file_blockdiff_max_concurrent_object_scans) |

**What it does:** Maximum number of concurrent object scans

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_file_blockdiff_max_concurrent_object_scans 16
ceph config get mds mds_file_blockdiff_max_concurrent_object_scans
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `4_K` · **Advanced** |
| Table | [mds.md#SP_mds_fscrypt_last_block_max_size](../../../config/mds/mds.md#SP_mds_fscrypt_last_block_max_size) |

**What it does:** Maximum size of the last block without the header along with a truncate request when the fscrypt is enabled.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_fscrypt_last_block_max_size 4_K
ceph config get mds mds_fscrypt_last_block_max_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_go_bad_corrupt_dentry](../../../config/mds/mds.md#SP_mds_go_bad_corrupt_dentry) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_go_bad_corrupt_dentry false
ceph config get mds mds_go_bad_corrupt_dentry
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Advanced** |
| Table | [mds.md#SP_mds_hack_allow_loading_invalid_metadata](../../../config/mds/mds.md#SP_mds_hack_allow_loading_invalid_metadata) |

**What it does:** INTENTIONALLY CAUSE DATA LOSS by bypasing checks for invalid metadata on disk. Allows testing repair tools.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_hack_allow_loading_invalid_metadata true
ceph config get mds mds_hack_allow_loading_invalid_metadata
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1.5` · **Advanced** |
| Table | [mds.md#SP_mds_health_cache_threshold](../../../config/mds/mds.md#SP_mds_health_cache_threshold) |

**What it does:** Threshold for cache size to generate health warning

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_health_cache_threshold 1.5
ceph config get mds mds_health_cache_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_health_summarize_threshold](../../../config/mds/mds.md#SP_mds_health_summarize_threshold) |

**What it does:** Threshold number of clients to summarize late client recall

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_health_summarize_threshold 10
ceph config get mds mds_health_summarize_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `15` · **Advanced** |
| Table | [mds.md#SP_mds_heartbeat_grace](../../../config/mds/mds.md#SP_mds_heartbeat_grace) |

**What it does:** Tolerance in seconds for MDS internal heartbeats

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_heartbeat_grace 15
ceph config get mds mds_heartbeat_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1000` · **Advanced** |
| Table | [mds.md#SP_mds_heartbeat_reset_grace](../../../config/mds/mds.md#SP_mds_heartbeat_reset_grace) |

**What it does:** Tolerance in seconds for long-running MDS operations which do not periodically reset the heartbeat timeout.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_heartbeat_reset_grace 1000
ceph config get mds mds_heartbeat_reset_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Str · default `(empty)` · **Basic** |
| Table | [mds.md#SP_mds_join_fs](../../../config/mds/mds.md#SP_mds_join_fs) |

**What it does:** File system MDS prefers to join

**When to use:** Core MDS behavior — review before changing in production.

**Example:**

```bash
ceph config set mds mds_join_fs "example"
ceph config get mds mds_join_fs
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `(empty)` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1` · **Dev** |
| Table | [mds.md#SP_mds_journal_format](../../../config/mds/mds.md#SP_mds_journal_format) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_journal_format 1
ceph config get mds mds_journal_format
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_create_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_create_at](../../../config/mds/mds.md#SP_mds_kill_create_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_create_at 64
ceph config get mds mds_kill_create_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_dirfrag_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_dirfrag_at](../../../config/mds/mds.md#SP_mds_kill_dirfrag_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_dirfrag_at 64
ceph config get mds mds_kill_dirfrag_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_export_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_export_at](../../../config/mds/mds.md#SP_mds_kill_export_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_export_at 64
ceph config get mds mds_kill_export_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_import_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_import_at](../../../config/mds/mds.md#SP_mds_kill_import_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_import_at 64
ceph config get mds mds_kill_import_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_journal_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_journal_at](../../../config/mds/mds.md#SP_mds_kill_journal_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_journal_at 64
ceph config get mds mds_kill_journal_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_journal_expire_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_journal_expire_at](../../../config/mds/mds.md#SP_mds_kill_journal_expire_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_journal_expire_at 64
ceph config get mds mds_kill_journal_expire_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_journal_replay_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_journal_replay_at](../../../config/mds/mds.md#SP_mds_kill_journal_replay_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_journal_replay_at 64
ceph config get mds mds_kill_journal_replay_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_link_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_link_at](../../../config/mds/mds.md#SP_mds_kill_link_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_link_at 64
ceph config get mds mds_kill_link_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_mdstable_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_mdstable_at](../../../config/mds/mds.md#SP_mds_kill_mdstable_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_mdstable_at 64
ceph config get mds mds_kill_mdstable_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_openc_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_openc_at](../../../config/mds/mds.md#SP_mds_kill_openc_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_openc_at 64
ceph config get mds mds_kill_openc_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_rename_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_rename_at](../../../config/mds/mds.md#SP_mds_kill_rename_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_rename_at 64
ceph config get mds mds_kill_rename_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_kill_shutdown_at

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [mds.md#SP_mds_kill_shutdown_at](../../../config/mds/mds.md#SP_mds_kill_shutdown_at) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_kill_shutdown_at 64
ceph config get mds mds_kill_shutdown_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_max_completed_flushes

| | |
|---|---|
| Type | Uint · default `100000` · **Dev** |
| Table | [mds.md#SP_mds_max_completed_flushes](../../../config/mds/mds.md#SP_mds_max_completed_flushes) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_max_completed_flushes 100000
ceph config get mds mds_max_completed_flushes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`100000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_max_completed_requests

| | |
|---|---|
| Type | Uint · default `100000` · **Dev** |
| Table | [mds.md#SP_mds_max_completed_requests](../../../config/mds/mds.md#SP_mds_max_completed_requests) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_max_completed_requests 100000
ceph config get mds mds_max_completed_requests
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`100000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_max_export_size

| | |
|---|---|
| Type | Size · default `20_M` · **Dev** |
| Table | [mds.md#SP_mds_max_export_size](../../../config/mds/mds.md#SP_mds_max_export_size) |

**What it does:** Maximum size (bytes) of a single subtree export during MDS rebalancing.

**When to use:** Lower to reduce latency spikes during balance; raise for faster migration on high-bandwidth networks.

**Example:**

```bash
ceph config set mds mds_max_export_size 20_M
ceph config get mds mds_max_export_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`20_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_max_file_recover

| | |
|---|---|
| Type | Uint · default `32` · **Advanced** |
| Table | [mds.md#SP_mds_max_file_recover](../../../config/mds/mds.md#SP_mds_max_file_recover) |

**What it does:** Maximum number of files for which to recover file sizes in parallel

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_file_recover 32
ceph config get mds mds_max_file_recover
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `64` · **Advanced** |
| Table | [mds.md#SP_mds_max_purge_files](../../../config/mds/mds.md#SP_mds_max_purge_files) |

**What it does:** maximum number of deleted files to purge in parallel

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_purge_files 64
ceph config get mds mds_max_purge_files
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `8_K` · **Advanced** |
| Table | [mds.md#SP_mds_max_purge_ops](../../../config/mds/mds.md#SP_mds_max_purge_ops) |

**What it does:** maximum number of purge operations performed in parallel

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_purge_ops 8_K
ceph config get mds mds_max_purge_ops
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `0.5` · **Advanced** |
| Table | [mds.md#SP_mds_max_purge_ops_per_pg](../../../config/mds/mds.md#SP_mds_max_purge_ops_per_pg) |

**What it does:** number of parallel purge operations performed per PG

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_purge_ops_per_pg 0.5
ceph config get mds mds_max_purge_ops_per_pg
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `5` · **Advanced** |
| Table | [mds.md#SP_mds_max_scrub_ops_in_progress](../../../config/mds/mds.md#SP_mds_max_scrub_ops_in_progress) |

**What it does:** maximum number of scrub operations performed in parallel

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_scrub_ops_in_progress 5
ceph config get mds mds_max_scrub_ops_in_progress
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `100` · **Advanced** |
| Table | [mds.md#SP_mds_max_snaps_per_dir](../../../config/mds/mds.md#SP_mds_max_snaps_per_dir) |

**What it does:** max snapshots per directory

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_snaps_per_dir 100
ceph config get mds mds_max_snaps_per_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `100`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `-1` · **Advanced** · **STARTUP** (restart required) |
| Table | [mds.md#SP_mds_numa_node](../../../config/mds/mds.md#SP_mds_numa_node) |

**What it does:** Set MDS CPU affinity to a NUMA node (-1 for none)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_numa_node 128
ceph config get mds mds_numa_node
ceph orch restart mds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [mds.md#SP_mds_oft_prefetch_dirfrags](../../../config/mds/mds.md#SP_mds_oft_prefetch_dirfrags) |

**What it does:** prefetch dirfrags recorded in open file table on startup

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_oft_prefetch_dirfrags true
ceph config get mds mds_oft_prefetch_dirfrags
ceph orch restart mds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `30` · **Advanced** |
| Table | [mds.md#SP_mds_op_complaint_time](../../../config/mds/mds.md#SP_mds_op_complaint_time) |

**What it does:** time in seconds to consider an operation blocked after no updates

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_op_complaint_time 30
ceph config get mds mds_op_complaint_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `600` · **Advanced** |
| Table | [mds.md#SP_mds_op_history_duration](../../../config/mds/mds.md#SP_mds_op_history_duration) |

**What it does:** expiration time in seconds of historical operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_op_history_duration 600
ceph config get mds mds_op_history_duration
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `600`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `20` · **Advanced** |
| Table | [mds.md#SP_mds_op_history_size](../../../config/mds/mds.md#SP_mds_op_history_size) |

**What it does:** maximum size for list of historical operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_op_history_size 20
ceph config get mds mds_op_history_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `20` · **Advanced** |
| Table | [mds.md#SP_mds_op_history_slow_op_size](../../../config/mds/mds.md#SP_mds_op_history_slow_op_size) |

**What it does:** maximum size for list of historical slow operations

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_op_history_slow_op_size 20
ceph config get mds mds_op_history_slow_op_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `20`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_op_history_slow_op_threshold](../../../config/mds/mds.md#SP_mds_op_history_slow_op_threshold) |

**What it does:** track the op if over this threshold

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_op_history_slow_op_threshold 10
ceph config get mds mds_op_history_slow_op_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Secs · default `15` · **Advanced** |
| Table | [mds.md#SP_mds_ping_grace](../../../config/mds/mds.md#SP_mds_ping_grace) |

**What it does:** timeout after which an MDS is considered laggy by rank 0 MDS.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_ping_grace 15
ceph config get mds mds_ping_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1` · **Dev** |
| Table | [mds.md#SP_mds_purge_queue_busy_flush_period](../../../config/mds/mds.md#SP_mds_purge_queue_busy_flush_period) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_purge_queue_busy_flush_period 1
ceph config get mds mds_purge_queue_busy_flush_period
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_recall_global_max_decay_threshold

| | |
|---|---|
| Type | Size · default `128_K` · **Advanced** |
| Table | [mds.md#SP_mds_recall_global_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_global_max_decay_threshold) |

**What it does:** Decay threshold for throttle on recalled caps globally

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_recall_global_max_decay_threshold 128_K
ceph config get mds mds_recall_global_max_decay_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1.5` · **Advanced** |
| Table | [mds.md#SP_mds_recall_max_decay_rate](../../../config/mds/mds.md#SP_mds_recall_max_decay_rate) |

**What it does:** Decay rate for throttle on recalled caps on a session

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_recall_max_decay_rate 1.5
ceph config get mds mds_recall_max_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `128_K` · **Advanced** |
| Table | [mds.md#SP_mds_recall_max_decay_threshold](../../../config/mds/mds.md#SP_mds_recall_max_decay_threshold) |

**What it does:** Decay threshold for throttle on recalled caps on a session

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_recall_max_decay_threshold 128_K
ceph config get mds mds_recall_max_decay_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `60` · **Advanced** |
| Table | [mds.md#SP_mds_recall_warning_decay_rate](../../../config/mds/mds.md#SP_mds_recall_warning_decay_rate) |

**What it does:** Decay rate for warning on slow session cap recall

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_recall_warning_decay_rate 60
ceph config get mds mds_recall_warning_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `60`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `256_K` · **Advanced** |
| Table | [mds.md#SP_mds_recall_warning_threshold](../../../config/mds/mds.md#SP_mds_recall_warning_threshold) |

**What it does:** Decay threshold for warning on slow session cap recall

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_recall_warning_threshold 256_K
ceph config get mds mds_recall_warning_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [mds.md#SP_mds_replay_unsafe_with_closed_session](../../../config/mds/mds.md#SP_mds_replay_unsafe_with_closed_session) |

**What it does:** complete all the replay request when mds is restarted, no matter the session is closed or not

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_replay_unsafe_with_closed_session true
ceph config get mds mds_replay_unsafe_with_closed_session
ceph orch restart mds
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `1_min` · **Advanced** |
| Table | [mds.md#SP_mds_request_load_average_decay_rate](../../../config/mds/mds.md#SP_mds_request_load_average_decay_rate) |

**What it does:** rate of decay in seconds for calculating request load average

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_request_load_average_decay_rate 1_min
ceph config get mds mds_request_load_average_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_root_ino_gid](../../../config/mds/mds.md#SP_mds_root_ino_gid) |

**What it does:** default gid for new root directory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_root_ino_gid 64
ceph config get mds mds_root_ino_gid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_root_ino_uid](../../../config/mds/mds.md#SP_mds_root_ino_uid) |

**What it does:** default uid for new root directory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_root_ino_uid 64
ceph config get mds mds_root_ino_uid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1` · **Advanced** |
| Table | [mds.md#SP_mds_scrub_stats_review_period](../../../config/mds/mds.md#SP_mds_scrub_stats_review_period) |

**What it does:** Period for which scrub stats will be available for review.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mds mds_scrub_stats_review_period 1
ceph config get mds mds_scrub_stats_review_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `60`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Millisecs · default `0` · **Dev** |
| Table | [mds.md#SP_mds_server_dispatch_client_request_delay](../../../config/mds/mds.md#SP_mds_server_dispatch_client_request_delay) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_server_dispatch_client_request_delay 0
ceph config get mds mds_server_dispatch_client_request_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_server_dispatch_killpoint_random

| | |
|---|---|
| Type | Float · default `0.0` · **Dev** |
| Table | [mds.md#SP_mds_server_dispatch_killpoint_random](../../../config/mds/mds.md#SP_mds_server_dispatch_killpoint_random) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_server_dispatch_killpoint_random 0.0
ceph config get mds mds_server_dispatch_killpoint_random
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_session_blocklist_on_evict

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_session_blocklist_on_evict](../../../config/mds/mds.md#SP_mds_session_blocklist_on_evict) |

**What it does:** Blocklist clients that have been evicted

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_session_blocklist_on_evict false
ceph config get mds mds_session_blocklist_on_evict
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Float · default `5_min` · **Advanced** |
| Table | [mds.md#SP_mds_session_cache_liveness_decay_rate](../../../config/mds/mds.md#SP_mds_session_cache_liveness_decay_rate) |

**What it does:** Decay rate for session liveness leading to preemptive cap recall

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_session_cache_liveness_decay_rate 5_min
ceph config get mds mds_session_cache_liveness_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `10` · **Advanced** |
| Table | [mds.md#SP_mds_session_cache_liveness_magnitude](../../../config/mds/mds.md#SP_mds_session_cache_liveness_magnitude) |

**What it does:** Decay magnitude for preemptively recalling caps on quiet client

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_session_cache_liveness_magnitude 10
ceph config get mds mds_session_cache_liveness_magnitude
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Size · default `16_M` · **Advanced** |
| Table | [mds.md#SP_mds_session_metadata_threshold](../../../config/mds/mds.md#SP_mds_session_metadata_threshold) |

**What it does:** Evict non-advancing client-tid sessions exceeding the config size.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_session_metadata_threshold 16_M
ceph config get mds mds_session_metadata_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `1_K` · **Advanced** |
| Table | [mds.md#SP_mds_sessionmap_keys_per_op](../../../config/mds/mds.md#SP_mds_sessionmap_keys_per_op) |

**What it does:** Number of omap keys to read from the SessionMap in one operation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mds mds_sessionmap_keys_per_op 1_K
ceph config get mds mds_sessionmap_keys_per_op
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_shutdown_check](../../../config/mds/mds.md#SP_mds_shutdown_check) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_shutdown_check 64
ceph config get mds mds_shutdown_check
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_skip_ino

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_skip_ino](../../../config/mds/mds.md#SP_mds_skip_ino) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_skip_ino 64
ceph config get mds mds_skip_ino
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_sleep_rank_change

| | |
|---|---|
| Type | Float · default `0.0` · **Dev** |
| Table | [mds.md#SP_mds_sleep_rank_change](../../../config/mds/mds.md#SP_mds_sleep_rank_change) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_sleep_rank_change 0.0
ceph config get mds mds_sleep_rank_change
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_snap_max_uid

| | |
|---|---|
| Type | Uint · default `4294967294` · **Advanced** |
| Table | [mds.md#SP_mds_snap_max_uid](../../../config/mds/mds.md#SP_mds_snap_max_uid) |

**What it does:** maximum uid of client to perform snapshots

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_snap_max_uid 4294967294
ceph config get mds mds_snap_max_uid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4294967294`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Uint · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_snap_min_uid](../../../config/mds/mds.md#SP_mds_snap_min_uid) |

**What it does:** minimum uid of client to perform snapshots

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_snap_min_uid 64
ceph config get mds mds_snap_min_uid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Advanced** |
| Table | [mds.md#SP_mds_snap_rstat](../../../config/mds/mds.md#SP_mds_snap_rstat) |

**What it does:** enabled nested rstat for snapshots

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_snap_rstat true
ceph config get mds mds_snap_rstat
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_standby_replay_damaged](../../../config/mds/mds.md#SP_mds_standby_replay_damaged) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_standby_replay_damaged true
ceph config get mds mds_standby_replay_damaged
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_symlink_recovery

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_symlink_recovery](../../../config/mds/mds.md#SP_mds_symlink_recovery) |

**What it does:** Stores symlink target on the first data object of symlink file. Allows recover of symlink using recovery tools.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_symlink_recovery false
ceph config get mds mds_symlink_recovery
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_thrash_exports](../../../config/mds/mds.md#SP_mds_thrash_exports) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_thrash_exports 64
ceph config get mds mds_thrash_exports
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_thrash_fragments

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mds.md#SP_mds_thrash_fragments](../../../config/mds/mds.md#SP_mds_thrash_fragments) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_thrash_fragments 64
ceph config get mds mds_thrash_fragments
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_use_global_snaprealm_seq_for_subvol

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_use_global_snaprealm_seq_for_subvol](../../../config/mds/mds.md#SP_mds_use_global_snaprealm_seq_for_subvol) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_use_global_snaprealm_seq_for_subvol false
ceph config get mds mds_use_global_snaprealm_seq_for_subvol
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

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
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_valgrind_exit](../../../config/mds/mds.md#SP_mds_valgrind_exit) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_valgrind_exit true
ceph config get mds mds_valgrind_exit
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_verify_backtrace

| | |
|---|---|
| Type | Uint · default `1` · **Dev** |
| Table | [mds.md#SP_mds_verify_backtrace](../../../config/mds/mds.md#SP_mds_verify_backtrace) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_verify_backtrace 1
ceph config get mds mds_verify_backtrace
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_verify_scatter

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_verify_scatter](../../../config/mds/mds.md#SP_mds_verify_scatter) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_verify_scatter true
ceph config get mds mds_verify_scatter
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_wipe_ino_prealloc

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_wipe_ino_prealloc](../../../config/mds/mds.md#SP_mds_wipe_ino_prealloc) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_wipe_ino_prealloc true
ceph config get mds mds_wipe_ino_prealloc
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_wipe_sessions

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_wipe_sessions](../../../config/mds/mds.md#SP_mds_wipe_sessions) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_wipe_sessions true
ceph config get mds mds_wipe_sessions
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
