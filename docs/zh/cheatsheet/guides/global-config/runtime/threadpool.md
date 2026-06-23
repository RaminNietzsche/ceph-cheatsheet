# Threadpool

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [threadpool_default_timeout](#threadpool_default_timeout) | `1_min` | Advanced | 性能 |
| [threadpool_empty_queue_max_wait](#threadpool_empty_queue_max_wait) | `2` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### threadpool_default_timeout

| | |
|---|---|
| 类型 | Int · default `1_min` · **Advanced** |
| 表格 | [threadpool.md#SP_threadpool_default_timeout](../../../config/global/threadpool.md#SP_threadpool_default_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global threadpool_default_timeout 1_min
ceph config get global threadpool_default_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_min` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global threadpool_default_timeout
ceph -s
```

---

### threadpool_empty_queue_max_wait

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [threadpool.md#SP_threadpool_empty_queue_max_wait](../../../config/global/threadpool.md#SP_threadpool_empty_queue_max_wait) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global threadpool_empty_queue_max_wait 2
ceph config get global threadpool_empty_queue_max_wait
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global threadpool_empty_queue_max_wait
ceph -s
```

---


[← 概览](../OVERVIEW.md)
