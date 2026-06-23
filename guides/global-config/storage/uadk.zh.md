# Uadk

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [uadk_compressor_enabled](#uadk_compressor_enabled) | `False` | Advanced | Policy |
| [uadk_wd_sync_ctx_num](#uadk_wd_sync_ctx_num) | `2` | Advanced | Performance |

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

### uadk_compressor_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [uadk.md#SP_uadk_compressor_enabled](../../../config/global/uadk.md#SP_uadk_compressor_enabled) |

**作用：** Enable UADK acceleration support for compression if available

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global uadk_compressor_enabled true
ceph config get global uadk_compressor_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global uadk_compressor_enabled
ceph -s
```

---

### uadk_wd_sync_ctx_num

| | |
|---|---|
| 类型 | Int · default `2` · **Advanced** |
| 表格 | [uadk.md#SP_uadk_wd_sync_ctx_num](../../../config/global/uadk.md#SP_uadk_wd_sync_ctx_num) |

**作用：** Set the number of instances in the queue

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global uadk_wd_sync_ctx_num 2
ceph config get global uadk_wd_sync_ctx_num
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `2`，最大 `1024`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global uadk_wd_sync_ctx_num
ceph -s
```

---


[← 概览](../OVERVIEW.md)
