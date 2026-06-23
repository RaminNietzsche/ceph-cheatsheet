# Auth & capabilities

MDS 配置深度指南 — 12 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mds_cache_quiesce_splitauth](#mds_cache_quiesce_splitauth) | `True` | Advanced | 策略 |
| [mds_cap_acquisition_throttle_retry_request_timeout](#mds_cap_acquisition_throttle_retry_request_timeout) | `0.5` | Advanced | 性能 |
| [mds_cap_revoke_eviction_timeout](#mds_cap_revoke_eviction_timeout) | `0` | Advanced | 性能 |
| [mds_debug_auth_pins](#mds_debug_auth_pins) | `False` | Dev | 开发 |
| [mds_forward_all_requests_to_auth](#mds_forward_all_requests_to_auth) | `False` | Advanced | 策略 |
| [mds_max_caps_per_client](#mds_max_caps_per_client) | `1_M` | Advanced | 性能 |
| [mds_min_caps_per_client](#mds_min_caps_per_client) | `100` | Advanced | 性能 |
| [mds_min_caps_working_set](#mds_min_caps_working_set) | `10000` | Advanced | 性能 |
| [mds_recall_max_caps](#mds_recall_max_caps) | `30000` | Advanced | 性能 |
| [mds_session_cap_acquisition_decay_rate](#mds_session_cap_acquisition_decay_rate) | `30` | Advanced | 性能 |
| [mds_session_cap_acquisition_throttle](#mds_session_cap_acquisition_throttle) | `100000` | Advanced | 性能 |
| [mds_session_max_caps_throttle_ratio](#mds_session_max_caps_throttle_ratio) | `1.1` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、兼容性、运维默认值 |
| **容量** | 磁盘布局、路径、容量规划 |
| **性能** | 基线 → 逐步调整 → 监控集群 |
| **连通性** | 最近且稳定的外部端点 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_cache_quiesce_splitauth

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mds.md#SP_mds_cache_quiesce_splitauth](../../../config/mds/mds.md#SP_mds_cache_quiesce_splitauth) |

**作用：** Allow recursive quiesce across auth boundaries

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mds mds_cache_quiesce_splitauth false
ceph config get mds mds_cache_quiesce_splitauth
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_cache_quiesce_splitauth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_acquisition_throttle_retry_request_timeout

| | |
|---|---|
| 类型 | Float · default `0.5` · **Advanced** |
| 表格 | [mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout](../../../config/mds/mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout) |

**作用：** Timeout in seconds after which a client request is retried due to cap acquisition throttling

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_cap_acquisition_throttle_retry_request_timeout 0.5
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_revoke_eviction_timeout

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [mds.md#SP_mds_cap_revoke_eviction_timeout](../../../config/mds/mds.md#SP_mds_cap_revoke_eviction_timeout) |

**作用：** Seconds to wait before evicting a client that holds caps after revoke.

**何时使用：** Increase for legacy clients that respond slowly to cap revokes; decrease to reclaim metadata cache faster.

**示例：**

```bash
ceph config set mds mds_cap_revoke_eviction_timeout 0
ceph config get mds mds_cap_revoke_eviction_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_cap_revoke_eviction_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_debug_auth_pins

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [mds.md#SP_mds_debug_auth_pins](../../../config/mds/mds.md#SP_mds_debug_auth_pins) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mds mds_debug_auth_pins true
ceph config get mds mds_debug_auth_pins
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mds_forward_all_requests_to_auth

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mds.md#SP_mds_forward_all_requests_to_auth](../../../config/mds/mds.md#SP_mds_forward_all_requests_to_auth) |

**作用：** always process op on auth mds

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds mds_forward_all_requests_to_auth true
ceph config get mds mds_forward_all_requests_to_auth
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_forward_all_requests_to_auth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_caps_per_client

| | |
|---|---|
| 类型 | Uint · default `1_M` · **Advanced** |
| 表格 | [mds.md#SP_mds_max_caps_per_client](../../../config/mds/mds.md#SP_mds_max_caps_per_client) |

**作用：** maximum number of capabilities a client may hold

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_max_caps_per_client 1_M
ceph config get mds mds_max_caps_per_client
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_max_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_per_client

| | |
|---|---|
| 类型 | Uint · default `100` · **Advanced** |
| 表格 | [mds.md#SP_mds_min_caps_per_client](../../../config/mds/mds.md#SP_mds_min_caps_per_client) |

**作用：** minimum number of capabilities a client may hold

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_min_caps_per_client 100
ceph config get mds mds_min_caps_per_client
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_min_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_working_set

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [mds.md#SP_mds_min_caps_working_set](../../../config/mds/mds.md#SP_mds_min_caps_working_set) |

**作用：** number of capabilities a client may hold without cache pressure warnings generated

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_min_caps_working_set 10000
ceph config get mds mds_min_caps_working_set
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_min_caps_working_set
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_max_caps

| | |
|---|---|
| 类型 | Size · default `30000` · **Advanced** |
| 表格 | [mds.md#SP_mds_recall_max_caps](../../../config/mds/mds.md#SP_mds_recall_max_caps) |

**作用：** Maximum number of caps to recall from a client session in single recall. Note that this is an integer, though the default value may be displayed with a B suffix.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_recall_max_caps 30000
ceph config get mds mds_recall_max_caps
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_recall_max_caps
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_decay_rate

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_cap_acquisition_decay_rate](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_decay_rate) |

**作用：** Decay rate for session readdir caps leading to readdir throttle

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_session_cap_acquisition_decay_rate 30
ceph config get mds mds_session_cap_acquisition_decay_rate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `30` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_session_cap_acquisition_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_throttle

| | |
|---|---|
| 类型 | Uint · default `100000` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_cap_acquisition_throttle](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_throttle) |

**作用：** Throttle cap acquisition rate per client session to protect the MDS.

**何时使用：** Tune when clients stampede caps after MDS restart or when many small files are opened concurrently.

**示例：**

```bash
ceph config set mds mds_session_cap_acquisition_throttle 100000
ceph config get mds mds_session_cap_acquisition_throttle
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_session_cap_acquisition_throttle
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_max_caps_throttle_ratio

| | |
|---|---|
| 类型 | Float · default `1.1` · **Advanced** |
| 表格 | [mds.md#SP_mds_session_max_caps_throttle_ratio](../../../config/mds/mds.md#SP_mds_session_max_caps_throttle_ratio) |

**作用：** Ratio of mds_max_caps_per_client that client must exceed before readdir may be throttled by cap acquisition throttle

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mds mds_session_max_caps_throttle_ratio 1.1
ceph config get mds mds_session_max_caps_throttle_ratio
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1.1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds mds_session_max_caps_throttle_ratio
ceph -s
ceph fs status
ceph mds stat
```

---


[← 概览](../OVERVIEW.md)
