# Jaeger

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [jaeger_agent_port](#jaeger_agent_port) | `6799` | Advanced | Performance |
| [jaeger_tracing_enable](#jaeger_tracing_enable) | `False` | Advanced | Policy |

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

### jaeger_agent_port

| | |
|---|---|
| 类型 | Int · default `6799` · **Advanced** |
| 表格 | [jaeger.md#SP_jaeger_agent_port](../../../config/global/jaeger.md#SP_jaeger_agent_port) |

**作用：** TCP port number of the Jaeger agent

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global jaeger_agent_port 6799
ceph config get global jaeger_agent_port
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `6799` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global jaeger_agent_port
ceph -s
```

---

### jaeger_tracing_enable

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [jaeger.md#SP_jaeger_tracing_enable](../../../config/global/jaeger.md#SP_jaeger_tracing_enable) |

**作用：** Ceph should use the Jaeger tracing system

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global jaeger_tracing_enable true
ceph config get global jaeger_tracing_enable
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global jaeger_tracing_enable
ceph -s
```

---


[← 概览](../OVERVIEW.md)
