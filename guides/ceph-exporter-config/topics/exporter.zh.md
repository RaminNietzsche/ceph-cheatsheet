# ceph-exporter

Ceph exporter 配置深度指南 — 8 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/ceph-exporter/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [exporter_addr](#exporter_addr) | `0.0.0.0` | Advanced | Connectivity |
| [exporter_cert_file](#exporter_cert_file) | `(empty)` | Advanced | Capacity |
| [exporter_http_port](#exporter_http_port) | `9926` | Advanced | Performance |
| [exporter_key_file](#exporter_key_file) | `(empty)` | Advanced | Capacity |
| [exporter_prio_limit](#exporter_prio_limit) | `5` | Advanced | Performance |
| [exporter_sock_dir](#exporter_sock_dir) | `/var/run/ceph/` | Advanced | Capacity |
| [exporter_sort_metrics](#exporter_sort_metrics) | `True` | Advanced | Performance |
| [exporter_stats_period](#exporter_stats_period) | `5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. ceph-exporter
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### exporter_addr

| | |
|---|---|
| 类型 | Str · default `0.0.0.0` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_addr](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_addr) |

**作用：** Host ip address where exporter is deployed

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set mgr exporter_addr "0.0.0.0"
ceph config get mgr exporter_addr
```

**寻找最优值：**

**调优模型：** Connectivity

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`0.0.0.0`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_addr
ceph -s
ceph mgr stat
```

---

### exporter_cert_file

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_cert_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_cert_file) |

**作用：** Certificate file for TLS.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr exporter_cert_file "example"
ceph config get mgr exporter_cert_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `(empty)` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_cert_file
ceph -s
ceph mgr stat
```

---

### exporter_http_port

| | |
|---|---|
| 类型 | Int · default `9926` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_http_port](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_http_port) |

**作用：** Port to deploy exporter on. Default is 9926

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr exporter_http_port 9926
ceph config get mgr exporter_http_port
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `9926` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_http_port
ceph -s
ceph mgr stat
```

---

### exporter_key_file

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_key_file](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_key_file) |

**作用：** Key certificate file for TLS.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr exporter_key_file "example"
ceph config get mgr exporter_key_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `(empty)` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_key_file
ceph -s
ceph mgr stat
```

---

### exporter_prio_limit

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_prio_limit](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_prio_limit) |

**作用：** Only perf counters greater than or equal to exporter_prio_limit are fetched

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mgr exporter_prio_limit 5
ceph config get mgr exporter_prio_limit
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_prio_limit
ceph -s
ceph mgr stat
```

---

### exporter_sock_dir

| | |
|---|---|
| 类型 | Str · default `/var/run/ceph/` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_sock_dir](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sock_dir) |

**作用：** The path to ceph daemons socket files dir

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set mgr exporter_sock_dir "/var/run/ceph/"
ceph config get mgr exporter_sock_dir
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `/var/run/ceph/` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_sock_dir
ceph -s
ceph mgr stat
```

---

### exporter_sort_metrics

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_sort_metrics](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_sort_metrics) |

**作用：** If true it will sort the metrics and group them.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mgr exporter_sort_metrics false
ceph config get mgr exporter_sort_metrics
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_sort_metrics
ceph -s
ceph mgr stat
```

---

### exporter_stats_period

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [ceph-exporter.md#SP_exporter_stats_period](../../../config/ceph-exporter/ceph-exporter.md#SP_exporter_stats_period) |

**作用：** Time to wait before sending requests again to exporter server (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mgr exporter_stats_period 5
ceph config get mgr exporter_stats_period
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mgr exporter_stats_period
ceph -s
ceph mgr stat
```

---


[← 概览](../OVERVIEW.md)
