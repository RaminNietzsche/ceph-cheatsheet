# QoS & throttling

RBD 配置深度指南 — 20 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_qos_bps_burst](#rbd_qos_bps_burst) | `0` | Advanced | 性能 |
| [rbd_qos_bps_burst_seconds](#rbd_qos_bps_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_bps_limit](#rbd_qos_bps_limit) | `0` | Advanced | 性能 |
| [rbd_qos_exclude_ops](#rbd_qos_exclude_ops) | `(empty)` | Advanced | 性能 |
| [rbd_qos_iops_burst](#rbd_qos_iops_burst) | `0` | Advanced | 性能 |
| [rbd_qos_iops_burst_seconds](#rbd_qos_iops_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_iops_limit](#rbd_qos_iops_limit) | `0` | Advanced | 性能 |
| [rbd_qos_read_bps_burst](#rbd_qos_read_bps_burst) | `0` | Advanced | 性能 |
| [rbd_qos_read_bps_burst_seconds](#rbd_qos_read_bps_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_read_bps_limit](#rbd_qos_read_bps_limit) | `0` | Advanced | 性能 |
| [rbd_qos_read_iops_burst](#rbd_qos_read_iops_burst) | `0` | Advanced | 性能 |
| [rbd_qos_read_iops_burst_seconds](#rbd_qos_read_iops_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_read_iops_limit](#rbd_qos_read_iops_limit) | `0` | Advanced | 性能 |
| [rbd_qos_schedule_tick_min](#rbd_qos_schedule_tick_min) | `50` | Advanced | 性能 |
| [rbd_qos_write_bps_burst](#rbd_qos_write_bps_burst) | `0` | Advanced | 性能 |
| [rbd_qos_write_bps_burst_seconds](#rbd_qos_write_bps_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_write_bps_limit](#rbd_qos_write_bps_limit) | `0` | Advanced | 性能 |
| [rbd_qos_write_iops_burst](#rbd_qos_write_iops_burst) | `0` | Advanced | 性能 |
| [rbd_qos_write_iops_burst_seconds](#rbd_qos_write_iops_burst_seconds) | `1` | Advanced | 性能 |
| [rbd_qos_write_iops_limit](#rbd_qos_write_iops_limit) | `0` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_qos_bps_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst) |

**作用：** the desired burst limit of IO bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_bps_burst 64
ceph config get client rbd_qos_bps_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_bps_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_bps_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_bps_burst_seconds) |

**作用：** the desired burst duration in seconds of IO bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_bps_burst_seconds 1
ceph config get client rbd_qos_bps_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_bps_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_bps_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_bps_limit) |

**作用：** the desired limit of IO bytes per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_bps_limit 64
ceph config get client rbd_qos_bps_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_bps_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_exclude_ops

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_exclude_ops](../../../config/rbd/rbd.md#SP_rbd_qos_exclude_ops) |

**作用：** optionally exclude ops from QoS &#91;&#93;(std::string *value, std::string *error_message) { std::ostringstream ss; uint64_t exclude_ops = librbd::io::rbd_io_operations_from_string(*value, &ss); // Leave this in integer form to avoid breaking Cinder. Someday // we would like to present this in string form instead... *value = stringify(exclude_ops); if (ss.str().size()) { return -EINVAL; } return 0; }

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_exclude_ops "example"
ceph config get client rbd_qos_exclude_ops
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_exclude_ops
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_iops_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst) |

**作用：** the desired burst limit of IO operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_iops_burst 64
ceph config get client rbd_qos_iops_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_iops_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_iops_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_iops_burst_seconds) |

**作用：** the desired burst duration in seconds of IO operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_iops_burst_seconds 1
ceph config get client rbd_qos_iops_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_iops_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_iops_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_iops_limit) |

**作用：** the desired limit of IO operations per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_iops_limit 64
ceph config get client rbd_qos_iops_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_iops_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_bps_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst) |

**作用：** the desired burst limit of read bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_read_bps_burst 64
ceph config get client rbd_qos_read_bps_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_bps_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_bps_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_burst_seconds) |

**作用：** the desired burst duration in seconds of read bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_read_bps_burst_seconds 1
ceph config get client rbd_qos_read_bps_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_bps_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_bps_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_bps_limit) |

**作用：** the desired limit of read bytes per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_read_bps_limit 64
ceph config get client rbd_qos_read_bps_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_bps_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_iops_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst) |

**作用：** the desired burst limit of read operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_read_iops_burst 64
ceph config get client rbd_qos_read_iops_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_iops_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_iops_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_burst_seconds) |

**作用：** the desired burst duration in seconds of read operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_read_iops_burst_seconds 1
ceph config get client rbd_qos_read_iops_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_iops_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_read_iops_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_read_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_read_iops_limit) |

**作用：** the desired limit of read operations per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_read_iops_limit 64
ceph config get client rbd_qos_read_iops_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_read_iops_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_schedule_tick_min

| | |
|---|---|
| 类型 | Uint · default `50` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_schedule_tick_min](../../../config/rbd/rbd.md#SP_rbd_qos_schedule_tick_min) |

**作用：** minimum schedule tick (in milliseconds) for QoS

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_schedule_tick_min 50
ceph config get client rbd_qos_schedule_tick_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `50` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_schedule_tick_min
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_bps_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_bps_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst) |

**作用：** the desired burst limit of write bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_write_bps_burst 64
ceph config get client rbd_qos_write_bps_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_bps_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_bps_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_bps_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_burst_seconds) |

**作用：** the desired burst duration in seconds of write bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_write_bps_burst_seconds 1
ceph config get client rbd_qos_write_bps_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_bps_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_bps_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_bps_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_bps_limit) |

**作用：** the desired limit of write bytes per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_write_bps_limit 64
ceph config get client rbd_qos_write_bps_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_bps_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_iops_burst

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_iops_burst](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst) |

**作用：** the desired burst limit of write operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_write_iops_burst 64
ceph config get client rbd_qos_write_iops_burst
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_iops_burst
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_iops_burst_seconds

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_iops_burst_seconds](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_burst_seconds) |

**作用：** the desired burst duration in seconds of write operations

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_qos_write_iops_burst_seconds 1
ceph config get client rbd_qos_write_iops_burst_seconds
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_iops_burst_seconds
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_qos_write_iops_limit

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_qos_write_iops_limit](../../../config/rbd/rbd.md#SP_rbd_qos_write_iops_limit) |

**作用：** the desired limit of write operations per second

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_qos_write_iops_limit 64
ceph config get client rbd_qos_write_iops_limit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_qos_write_iops_limit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
