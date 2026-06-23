# Intervals & throttling

OSD 配置深度指南 — 12 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [osd_delete_sleep](#osd_delete_sleep) | `0` | Advanced | 性能 |
| [osd_delete_sleep_hdd](#osd_delete_sleep_hdd) | `5` | Advanced | 性能 |
| [osd_delete_sleep_hybrid](#osd_delete_sleep_hybrid) | `1` | Advanced | 性能 |
| [osd_delete_sleep_ssd](#osd_delete_sleep_ssd) | `1` | Advanced | 性能 |
| [osd_max_markdown_period](#osd_max_markdown_period) | `10_min` | Advanced | 性能 |
| [osd_op_thread_suicide_timeout](#osd_op_thread_suicide_timeout) | `150` | Advanced | 性能 |
| [osd_op_thread_timeout](#osd_op_thread_timeout) | `15` | Advanced | 性能 |
| [osd_smart_report_timeout](#osd_smart_report_timeout) | `5` | Advanced | 性能 |
| [osd_snap_trim_sleep](#osd_snap_trim_sleep) | `0` | Advanced | 性能 |
| [osd_snap_trim_sleep_hdd](#osd_snap_trim_sleep_hdd) | `5` | Advanced | 性能 |
| [osd_snap_trim_sleep_hybrid](#osd_snap_trim_sleep_hybrid) | `2` | Advanced | 性能 |
| [osd_snap_trim_sleep_ssd](#osd_snap_trim_sleep_ssd) | `0` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_delete_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_delete_sleep](../../../config/osd/osd.md#SP_osd_delete_sleep) |

**作用：** Time in seconds to sleep before next removal transaction. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_delete_sleep 0
ceph config get osd osd_delete_sleep
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_delete_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_hdd

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_delete_sleep_hdd](../../../config/osd/osd.md#SP_osd_delete_sleep_hdd) |

**作用：** Time in seconds to sleep before next removal transaction for HDDs.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_delete_sleep_hdd 5
ceph config get osd osd_delete_sleep_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_delete_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_hybrid

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_delete_sleep_hybrid](../../../config/osd/osd.md#SP_osd_delete_sleep_hybrid) |

**作用：** Time in seconds to sleep before next removal transaction when OSD data is on HDD and OSD journal or WAL+DB is on SSD

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_delete_sleep_hybrid 1
ceph config get osd osd_delete_sleep_hybrid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_delete_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_delete_sleep_ssd

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [osd.md#SP_osd_delete_sleep_ssd](../../../config/osd/osd.md#SP_osd_delete_sleep_ssd) |

**作用：** Time in seconds to sleep before next removal transaction for SSDs

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_delete_sleep_ssd 1
ceph config get osd osd_delete_sleep_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_delete_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_max_markdown_period

| | |
|---|---|
| 类型 | Int · default `10_min` · **Advanced** |
| 表格 | [osd.md#SP_osd_max_markdown_period](../../../config/osd/osd.md#SP_osd_max_markdown_period) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set osd osd_max_markdown_period 10_min
ceph config get osd osd_max_markdown_period
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_max_markdown_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_thread_suicide_timeout

| | |
|---|---|
| 类型 | Int · default `150` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_thread_suicide_timeout](../../../config/osd/osd.md#SP_osd_op_thread_suicide_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_op_thread_suicide_timeout 150
ceph config get osd osd_op_thread_suicide_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `150` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_thread_suicide_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_thread_timeout

| | |
|---|---|
| 类型 | Int · default `15` · **Advanced** |
| 表格 | [osd.md#SP_osd_op_thread_timeout](../../../config/osd/osd.md#SP_osd_op_thread_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_op_thread_timeout 15
ceph config get osd osd_op_thread_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_op_thread_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_smart_report_timeout

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_smart_report_timeout](../../../config/osd/osd.md#SP_osd_smart_report_timeout) |

**作用：** Timeout (in seconds) for smartctl to run, default is set to 5

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_smart_report_timeout 5
ceph config get osd osd_smart_report_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_smart_report_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_sleep](../../../config/osd/osd.md#SP_osd_snap_trim_sleep) |

**作用：** Time in seconds to sleep before next snap trim. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_snap_trim_sleep 0
ceph config get osd osd_snap_trim_sleep
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_snap_trim_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_hdd

| | |
|---|---|
| 类型 | Float · default `5` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_sleep_hdd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hdd) |

**作用：** Time in seconds to sleep before next snap trim for HDDs

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_snap_trim_sleep_hdd 5
ceph config get osd osd_snap_trim_sleep_hdd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_snap_trim_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_hybrid

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_sleep_hybrid](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hybrid) |

**作用：** Time in seconds to sleep before next snap trim when data is on HDD and journal is on SSD

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_snap_trim_sleep_hybrid 2
ceph config get osd osd_snap_trim_sleep_hybrid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_snap_trim_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_snap_trim_sleep_ssd

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_snap_trim_sleep_ssd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_ssd) |

**作用：** Time in seconds to sleep before next snap trim for SSDs

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set osd osd_snap_trim_sleep_ssd 0
ceph config get osd osd_snap_trim_sleep_ssd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_snap_trim_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
