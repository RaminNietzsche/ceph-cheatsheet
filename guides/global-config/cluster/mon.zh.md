# Mon

Global 配置深度指南 — 74 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_allow_pool_delete

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_allow_pool_delete](../../../config/global/mon.md#SP_mon_allow_pool_delete) |

**作用：** allow pool deletions

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_allow_pool_delete true
ceph config get mon mon_allow_pool_delete
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_allow_pool_delete
ceph -s
ceph mon stat
```

---

### mon_client_bytes

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_bytes](../../../config/global/mon.md#SP_mon_client_bytes) |

**作用：** Max bytes of outstanding client messages mon will read off the network

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_client_bytes 100_M
ceph config get mon mon_client_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_bytes
ceph -s
ceph mon stat
```

---

### mon_client_directed_command_retry

| | |
|---|---|
| 类型 | Int · default `2` · **Dev** |
| 表格 | [mon.md#SP_mon_client_directed_command_retry](../../../config/global/mon.md#SP_mon_client_directed_command_retry) |

**作用：** Number of times to try sending a command directed at a specific Monitor

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_client_directed_command_retry 2
ceph config get mon mon_client_directed_command_retry
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_client_hunt_interval

| | |
|---|---|
| 类型 | Float · default `3` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_interval](../../../config/global/mon.md#SP_mon_client_hunt_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_client_hunt_interval 3
ceph config get mon mon_client_hunt_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_interval
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_backoff

| | |
|---|---|
| 类型 | Float · default `1.5` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_interval_backoff](../../../config/global/mon.md#SP_mon_client_hunt_interval_backoff) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_client_hunt_interval_backoff 1.5
ceph config get mon mon_client_hunt_interval_backoff
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_interval_backoff
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_max_multiple

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_interval_max_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_max_multiple) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_client_hunt_interval_max_multiple 10
ceph config get mon mon_client_hunt_interval_max_multiple
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_interval_max_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_min_multiple

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_interval_min_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_min_multiple) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_client_hunt_interval_min_multiple 1
ceph config get mon mon_client_hunt_interval_min_multiple
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_interval_min_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_on_resend

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_on_resend](../../../config/global/mon.md#SP_mon_client_hunt_on_resend) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_client_hunt_on_resend false
ceph config get mon mon_client_hunt_on_resend
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_on_resend
ceph -s
ceph mon stat
```

---

### mon_client_hunt_parallel

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_hunt_parallel](../../../config/global/mon.md#SP_mon_client_hunt_parallel) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_client_hunt_parallel 3
ceph config get mon mon_client_hunt_parallel
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_hunt_parallel
ceph -s
ceph mon stat
```

---

### mon_client_log_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_log_interval](../../../config/global/mon.md#SP_mon_client_log_interval) |

**作用：** How frequently we send queued cluster log messages to the Monitors

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_client_log_interval 1
ceph config get mon mon_client_log_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_log_interval
ceph -s
ceph mon stat
```

---

### mon_client_max_log_entries_per_message

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_max_log_entries_per_message](../../../config/global/mon.md#SP_mon_client_max_log_entries_per_message) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_client_max_log_entries_per_message 1000
ceph config get mon mon_client_max_log_entries_per_message
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_max_log_entries_per_message
ceph -s
ceph mon stat
```

---

### mon_client_ping_interval

| | |
|---|---|
| 类型 | Float · default `10` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_ping_interval](../../../config/global/mon.md#SP_mon_client_ping_interval) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_client_ping_interval 10
ceph config get mon mon_client_ping_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_ping_interval
ceph -s
ceph mon stat
```

---

### mon_client_ping_timeout

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_ping_timeout](../../../config/global/mon.md#SP_mon_client_ping_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_client_ping_timeout 30
ceph config get mon mon_client_ping_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_client_target_rank

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [mon.md#SP_mon_client_target_rank](../../../config/global/mon.md#SP_mon_client_target_rank) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_client_target_rank 128
ceph config get mon mon_client_target_rank
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `-1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `-1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_client_target_rank
ceph -s
ceph mon stat
```

---

### mon_config_key_max_entry_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [mon.md#SP_mon_config_key_max_entry_size](../../../config/global/mon.md#SP_mon_config_key_max_entry_size) |

**作用：** Defines the number of bytes allowed to be held in a single config-key entry

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_config_key_max_entry_size 64_K
ceph config get mon mon_config_key_max_entry_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_config_key_max_entry_size
ceph -s
ceph mon stat
```

---

### mon_debug_block_osdmap_trim

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_block_osdmap_trim](../../../config/global/mon.md#SP_mon_debug_block_osdmap_trim) |

**作用：** Block OSDMap trimming while the option is enabled.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_block_osdmap_trim true
ceph config get mon mon_debug_block_osdmap_trim
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_deprecated_as_obsolete

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_deprecated_as_obsolete](../../../config/global/mon.md#SP_mon_debug_deprecated_as_obsolete) |

**作用：** Treat deprecated mon commands as obsolete

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_deprecated_as_obsolete true
ceph config get mon mon_debug_deprecated_as_obsolete
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_dump_json

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_dump_json](../../../config/global/mon.md#SP_mon_debug_dump_json) |

**作用：** Dump paxos transasctions to log as JSON

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_dump_json true
ceph config get mon mon_debug_dump_json
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_dump_location

| | |
|---|---|
| 类型 | Str · default `/var/log/ceph/$cluster-$name.tdump` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_dump_location](../../../config/global/mon.md#SP_mon_debug_dump_location) |

**作用：** File to which to dump Paxos transactions

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_dump_location "/var/log/ceph/$cluster-$name.tdump"
ceph config get mon mon_debug_dump_location
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`/var/log/ceph/$cluster-$name.tdump`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_dump_transactions

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_dump_transactions](../../../config/global/mon.md#SP_mon_debug_dump_transactions) |

**作用：** Dump Paxos transactions to log

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_dump_transactions true
ceph config get mon mon_debug_dump_transactions
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_extra_checks

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_extra_checks](../../../config/global/mon.md#SP_mon_debug_extra_checks) |

**作用：** Enable some additional monitor checks

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_extra_checks true
ceph config get mon mon_debug_extra_checks
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_no_initial_persistent_features

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_no_initial_persistent_features](../../../config/global/mon.md#SP_mon_debug_no_initial_persistent_features) |

**作用：** Do not set any monmap features for new Monitor clusters

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_no_initial_persistent_features true
ceph config get mon mon_debug_no_initial_persistent_features
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_no_require_bluestore_for_ec_overwrites

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites](../../../config/global/mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites) |

**作用：** Do not require BlueStore OSDs to enable EC overwrites within a RADOS pool

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_no_require_bluestore_for_ec_overwrites true
ceph config get mon mon_debug_no_require_bluestore_for_ec_overwrites
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_no_require_tentacle

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_no_require_tentacle](../../../config/global/mon.md#SP_mon_debug_no_require_tentacle) |

**作用：** Do not require the Tentacle feature for new Monitor clusters

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_no_require_tentacle true
ceph config get mon mon_debug_no_require_tentacle
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_no_require_umbrella

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_no_require_umbrella](../../../config/global/mon.md#SP_mon_debug_no_require_umbrella) |

**作用：** Do not require the Umbrella feature for new Monitor clusters

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_no_require_umbrella true
ceph config get mon mon_debug_no_require_umbrella
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_debug_unsafe_allow_tier_with_nonempty_snaps

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps](../../../config/global/mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_debug_unsafe_allow_tier_with_nonempty_snaps true
ceph config get mon mon_debug_unsafe_allow_tier_with_nonempty_snaps
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_dns_srv_name

| | |
|---|---|
| 类型 | Str · default `ceph-mon` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mon.md#SP_mon_dns_srv_name](../../../config/global/mon.md#SP_mon_dns_srv_name) |

**作用：** Name of DNS SRV record to check for monitor addresses

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_dns_srv_name "ceph-mon"
ceph config get mon mon_dns_srv_name
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `ceph-mon` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_dns_srv_name
ceph -s
ceph mon stat
```

---

### mon_fake_pool_delete

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_fake_pool_delete](../../../config/global/mon.md#SP_mon_fake_pool_delete) |

**作用：** Fake pool deletions by renaming the RADOS pool

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_fake_pool_delete true
ceph config get mon mon_fake_pool_delete
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_fake_pool_delete
ceph -s
ceph mon stat
```

---

### mon_force_quorum_join

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_force_quorum_join](../../../config/global/mon.md#SP_mon_force_quorum_join) |

**作用：** Force a Monitor to rejoin the quorum even though it was just removed

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mon mon_force_quorum_join true
ceph config get mon mon_force_quorum_join
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_force_quorum_join
ceph -s
ceph mon stat
```

---

### mon_globalid_prealloc

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [mon.md#SP_mon_globalid_prealloc](../../../config/global/mon.md#SP_mon_globalid_prealloc) |

**作用：** number of globalid values to preallocate

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_globalid_prealloc 10000
ceph config get mon mon_globalid_prealloc
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_globalid_prealloc
ceph -s
ceph mon stat
```

---

### mon_host

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Basic** · **STARTUP**（需重启） |
| 表格 | [mon.md#SP_mon_host](../../../config/global/mon.md#SP_mon_host) |

**作用：** List of hosts or addresses to search for a monitor

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set mon mon_host "example"
ceph config get mon mon_host
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `(empty)` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_host
ceph -s
ceph mon stat
```

---

### mon_host_override

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [mon.md#SP_mon_host_override](../../../config/global/mon.md#SP_mon_host_override) |

**作用：** Monitor(s) to use overriding the MonMap

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_host_override "example"
ceph config get mon mon_host_override
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_host_override
ceph -s
ceph mon stat
```

---

### mon_initial_members

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [mon.md#SP_mon_initial_members](../../../config/global/mon.md#SP_mon_initial_members) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_initial_members "example"
ceph config get mon mon_initial_members
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_initial_members
ceph -s
ceph mon stat
```

---

### mon_inject_pg_merge_bounce_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_inject_pg_merge_bounce_probability](../../../config/global/mon.md#SP_mon_inject_pg_merge_bounce_probability) |

**作用：** Probability of failing and reverting a pg_num decrement

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_inject_pg_merge_bounce_probability 0
ceph config get mon mon_inject_pg_merge_bounce_probability
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_inject_sync_get_chunk_delay

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_inject_sync_get_chunk_delay](../../../config/global/mon.md#SP_mon_inject_sync_get_chunk_delay) |

**作用：** Inject delay during Monitor sync (seconds)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_inject_sync_get_chunk_delay 0
ceph config get mon mon_inject_sync_get_chunk_delay
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_inject_transaction_delay_max

| | |
|---|---|
| 类型 | Float · default `10` · **Dev** |
| 表格 | [mon.md#SP_mon_inject_transaction_delay_max](../../../config/global/mon.md#SP_mon_inject_transaction_delay_max) |

**作用：** Max duration of injected delay in Paxos

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_inject_transaction_delay_max 10
ceph config get mon mon_inject_transaction_delay_max
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`10`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_inject_transaction_delay_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_inject_transaction_delay_probability](../../../config/global/mon.md#SP_mon_inject_transaction_delay_probability) |

**作用：** Probability of injecting a delay in Paxos

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_inject_transaction_delay_probability 0
ceph config get mon mon_inject_transaction_delay_probability
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_keyvaluedb

| | |
|---|---|
| 类型 | Str · enum: ["rocksdb"] · default `rocksdb` · **Advanced** |
| 表格 | [mon.md#SP_mon_keyvaluedb](../../../config/global/mon.md#SP_mon_keyvaluedb) |

**作用：** Database backend to use for the Monitor database

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_keyvaluedb rocksdb
ceph config get mon mon_keyvaluedb
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `rocksdb` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_keyvaluedb
ceph -s
ceph mon stat
```

---

### mon_max_log_epochs

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_log_epochs](../../../config/global/mon.md#SP_mon_max_log_epochs) |

**作用：** Max number of past cluster log epochs to store

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_log_epochs 500
ceph config get mon mon_max_log_epochs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_log_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mdsmap_epochs

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_mdsmap_epochs](../../../config/global/mon.md#SP_mon_max_mdsmap_epochs) |

**作用：** Max number of FSMaps/MDSMaps to store

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_mdsmap_epochs 500
ceph config get mon mon_max_mdsmap_epochs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_mdsmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mgrmap_epochs

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_mgrmap_epochs](../../../config/global/mon.md#SP_mon_max_mgrmap_epochs) |

**作用：** Max number of MgrMaps to store

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_mgrmap_epochs 500
ceph config get mon mon_max_mgrmap_epochs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_mgrmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_nvmeof_epochs

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_nvmeof_epochs](../../../config/global/mon.md#SP_mon_max_nvmeof_epochs) |

**作用：** Max number of NVMeoF gateway maps to store

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_nvmeof_epochs 500
ceph config get mon mon_max_nvmeof_epochs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_nvmeof_epochs
ceph -s
ceph mon stat
```

---

### mon_max_osd

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_osd](../../../config/global/mon.md#SP_mon_max_osd) |

**作用：** Max number of OSDs in a cluster

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_osd 10000
ceph config get mon mon_max_osd
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_osd
ceph -s
ceph mon stat
```

---

### mon_max_pg_per_osd

| | |
|---|---|
| 类型 | Uint · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_pg_per_osd](../../../config/global/mon.md#SP_mon_max_pg_per_osd) |

**作用：** Max number of PGs per OSD the cluster will allow

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_pg_per_osd 500
ceph config get mon mon_max_pg_per_osd
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_max_snap_prune_per_epoch

| | |
|---|---|
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_snap_prune_per_epoch](../../../config/global/mon.md#SP_mon_max_snap_prune_per_epoch) |

**作用：** Max number of pruned snaps we will process in a single OSDMap epoch

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_snap_prune_per_epoch 100
ceph config get mon mon_max_snap_prune_per_epoch
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_snap_prune_per_epoch
ceph -s
ceph mon stat
```

---

### mon_min_osdmap_epochs

| | |
|---|---|
| 类型 | Int · default `500` · **Advanced** |
| 表格 | [mon.md#SP_mon_min_osdmap_epochs](../../../config/global/mon.md#SP_mon_min_osdmap_epochs) |

**作用：** Min number of OSDMaps to store

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_min_osdmap_epochs 500
ceph config get mon mon_min_osdmap_epochs
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `500` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_min_osdmap_epochs
ceph -s
ceph mon stat
```

---

### mon_osd_backfillfull_ratio

| | |
|---|---|
| 类型 | Float · default `0.9` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_backfillfull_ratio](../../../config/global/mon.md#SP_mon_osd_backfillfull_ratio) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_backfillfull_ratio 0.9
ceph config get mon mon_osd_backfillfull_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.9` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_backfillfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_force_trim_to

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_osd_force_trim_to](../../../config/global/mon.md#SP_mon_osd_force_trim_to) |

**作用：** Force Monitors to trim osdmaps through this epoch

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_osd_force_trim_to 64
ceph config get mon mon_osd_force_trim_to
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_osd_full_ratio

| | |
|---|---|
| 类型 | Float · default `0.95` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_full_ratio](../../../config/global/mon.md#SP_mon_osd_full_ratio) |

**作用：** Full ratio of OSDs to be set during initial creation of the cluster

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_full_ratio 0.95
ceph config get mon mon_osd_full_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.95` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_full_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_initial_require_min_compat_client

| | |
|---|---|
| 类型 | Str · default `luminous` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_initial_require_min_compat_client](../../../config/global/mon.md#SP_mon_osd_initial_require_min_compat_client) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_osd_initial_require_min_compat_client luminous
ceph config get mon mon_osd_initial_require_min_compat_client
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `luminous` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_initial_require_min_compat_client
ceph -s
ceph mon stat
```

---

### mon_osd_min_down_reporters

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_min_down_reporters](../../../config/global/mon.md#SP_mon_osd_min_down_reporters) |

**作用：** Number of OSDs from different subtrees who need to report a down OSD for it to count

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_osd_min_down_reporters 2
ceph config get mon mon_osd_min_down_reporters
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_min_down_reporters
ceph -s
ceph mon stat
```

---

### mon_osd_nearfull_ratio

| | |
|---|---|
| 类型 | Float · default `0.85` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_nearfull_ratio](../../../config/global/mon.md#SP_mon_osd_nearfull_ratio) |

**作用：** Nearfull ratio for OSDs to be set during initial creation of cluster

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_nearfull_ratio 0.85
ceph config get mon mon_osd_nearfull_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.85` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_nearfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_report_timeout

| | |
|---|---|
| 类型 | Int · default `15_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_report_timeout](../../../config/global/mon.md#SP_mon_osd_report_timeout) |

**作用：** Time before OSDs who do not report to the mons are marked down (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_osd_report_timeout 15_min
ceph config get mon mon_osd_report_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `15_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_report_timeout
ceph -s
ceph mon stat
```

---

### mon_osd_reporter_subtree_level

| | |
|---|---|
| 类型 | Str · default `host` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_reporter_subtree_level](../../../config/global/mon.md#SP_mon_osd_reporter_subtree_level) |

**作用：** At which level of parent bucket the reporters are counted

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_reporter_subtree_level host
ceph config get mon mon_osd_reporter_subtree_level
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `host` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_reporter_subtree_level
ceph -s
ceph mon stat
```

---

### mon_osd_snap_trim_queue_warn_on

| | |
|---|---|
| 类型 | Int · default `32768` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_snap_trim_queue_warn_on](../../../config/global/mon.md#SP_mon_osd_snap_trim_queue_warn_on) |

**作用：** Warn when snap trim queue reaches or exceeds this value

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_osd_snap_trim_queue_warn_on 32768
ceph config get mon mon_osd_snap_trim_queue_warn_on
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `32768` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_snap_trim_queue_warn_on
ceph -s
ceph mon stat
```

---

### mon_probe_timeout

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [mon.md#SP_mon_probe_timeout](../../../config/global/mon.md#SP_mon_probe_timeout) |

**作用：** Timeout for querying other mons during bootstrap pre-election phase (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_probe_timeout 2
ceph config get mon mon_probe_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_probe_timeout
ceph -s
ceph mon stat
```

---

### mon_scrub_inject_crc_mismatch

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_scrub_inject_crc_mismatch](../../../config/global/mon.md#SP_mon_scrub_inject_crc_mismatch) |

**作用：** Probability for injecting crc mismatches into mon scrub

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_scrub_inject_crc_mismatch 0
ceph config get mon mon_scrub_inject_crc_mismatch
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_scrub_inject_missing_keys

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_scrub_inject_missing_keys](../../../config/global/mon.md#SP_mon_scrub_inject_missing_keys) |

**作用：** Probability for injecting missing keys into mon scrub

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_scrub_inject_missing_keys 0
ceph config get mon mon_scrub_inject_missing_keys
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_scrub_interval

| | |
|---|---|
| 类型 | Secs · default `1_day` · **Advanced** |
| 表格 | [mon.md#SP_mon_scrub_interval](../../../config/global/mon.md#SP_mon_scrub_interval) |

**作用：** Frequency for scrubbing the Monitor database

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_scrub_interval 1_day
ceph config get mon mon_scrub_interval
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_day` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_scrub_interval
ceph -s
ceph mon stat
```

---

### mon_scrub_max_keys

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [mon.md#SP_mon_scrub_max_keys](../../../config/global/mon.md#SP_mon_scrub_max_keys) |

**作用：** Max keys per on scrub chunk/step

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_scrub_max_keys 100
ceph config get mon mon_scrub_max_keys
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_scrub_max_keys
ceph -s
ceph mon stat
```

---

### mon_scrub_timeout

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_scrub_timeout](../../../config/global/mon.md#SP_mon_scrub_timeout) |

**作用：** Timeout to restart scrub of mon quorum participant does not respond for the latest chunk

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_scrub_timeout 5_min
ceph config get mon mon_scrub_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_scrub_timeout
ceph -s
ceph mon stat
```

---

### mon_sync_debug

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mon.md#SP_mon_sync_debug](../../../config/global/mon.md#SP_mon_sync_debug) |

**作用：** Enable extra debugging during mon sync

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_sync_debug true
ceph config get mon mon_sync_debug
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_sync_max_payload_keys

| | |
|---|---|
| 类型 | Int · default `2000` · **Advanced** |
| 表格 | [mon.md#SP_mon_sync_max_payload_keys](../../../config/global/mon.md#SP_mon_sync_max_payload_keys) |

**作用：** Target max keys in message payload for Monitor sync

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_sync_max_payload_keys 2000
ceph config get mon mon_sync_max_payload_keys
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_sync_max_payload_keys
ceph -s
ceph mon stat
```

---

### mon_sync_max_payload_size

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [mon.md#SP_mon_sync_max_payload_size](../../../config/global/mon.md#SP_mon_sync_max_payload_size) |

**作用：** Target max message payload for mon sync

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_sync_max_payload_size 1_M
ceph config get mon mon_sync_max_payload_size
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_sync_max_payload_size
ceph -s
ceph mon stat
```

---

### mon_sync_provider_kill_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_sync_provider_kill_at](../../../config/global/mon.md#SP_mon_sync_provider_kill_at) |

**作用：** Kill mon sync provider at specific point

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_sync_provider_kill_at 64
ceph config get mon mon_sync_provider_kill_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_sync_requester_kill_at

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [mon.md#SP_mon_sync_requester_kill_at](../../../config/global/mon.md#SP_mon_sync_requester_kill_at) |

**作用：** Kill mon sync requestor at specific point

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_sync_requester_kill_at 64
ceph config get mon mon_sync_requester_kill_at
```

**寻找最优值：**

**调优模型：** Dev

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_sync_timeout

| | |
|---|---|
| 类型 | Float · default `1_min` · **Advanced** |
| 表格 | [mon.md#SP_mon_sync_timeout](../../../config/global/mon.md#SP_mon_sync_timeout) |

**作用：** Timeout before canceling sync if syncing mon does not respond

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon mon_sync_timeout 1_min
ceph config get mon mon_sync_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_sync_timeout
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim) |

**作用：** Raise the AUTH_INSECURE_GLOBAL_ID_RECLAIM health warning if any connected clients are insecurely reclaiming global_ids

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim false
ceph config get mon mon_warn_on_insecure_global_id_reclaim
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim_allowed

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed) |

**作用：** issue AUTH_INSECURE_GLOBAL_ID_RECLAIM_ALLOWED health warning if insecure global_id reclaim is allowed

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim_allowed false
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
ceph -s
ceph mon stat
```

---

### mon_warn_on_msgr2_not_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_msgr2_not_enabled](../../../config/global/mon.md#SP_mon_warn_on_msgr2_not_enabled) |

**作用：** Raise the MON_MSGR2_NOT_ENABLED health warning if monitors are all running Nautilus but not all binding to a msgr2 port

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_msgr2_not_enabled false
ceph config get mon mon_warn_on_msgr2_not_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_msgr2_not_enabled
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_ratio

| | |
|---|---|
| 类型 | Float · default `0.05` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_slow_ping_ratio](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_ratio) |

**作用：** Issue a health warning if heartbeat ping longer than percentage of osd_heartbeat_grace

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_warn_on_slow_ping_ratio 0.05
ceph config get mon mon_warn_on_slow_ping_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_slow_ping_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_time

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_slow_ping_time](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_time) |

**作用：** Override mon_warn_on_slow_ping_ratio with specified threshold in milliseconds

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_warn_on_slow_ping_time 0
ceph config get mon mon_warn_on_slow_ping_time
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_slow_ping_time
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_deep_scrubbed_ratio

| | |
|---|---|
| 类型 | Float · default `0.75` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio) |

**作用：** Percentage of the deep scrub interval past the deep scrub interval to warn - Set this configurable with the command "ceph config set mgr mon_warn_pg_not_deep_scrubbed_ratio <ratio_value>"

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_warn_pg_not_deep_scrubbed_ratio 0.75
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.75` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_scrubbed_ratio

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_pg_not_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_scrubbed_ratio) |

**作用：** Raise a health warning when shallow scrubs are delayed by this percentage of the shallow scrub interval. Note that this must be set at mgr or with global scope. Set this configurable with the command "ceph config set mgr mon_warn_pg_not_scrubbed_ratio <ratio_value>".

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mon mon_warn_pg_not_scrubbed_ratio 0.5
ceph config get mon mon_warn_pg_not_scrubbed_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_pg_not_scrubbed_ratio
ceph -s
ceph mon stat
```

---


[← 概览](../OVERVIEW.md)
