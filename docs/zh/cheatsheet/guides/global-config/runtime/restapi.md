# Restapi

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [restapi_base_url](#restapi_base_url) | `(empty)` | Advanced | 连通性 |
| [restapi_log_level](#restapi_log_level) | `(empty)` | Advanced | 性能 |

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

### restapi_base_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [restapi.md#SP_restapi_base_url](../../../config/global/restapi.md#SP_restapi_base_url) |

**作用：** default set by python code

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global restapi_base_url "https://example.com/"
ceph config get global restapi_base_url
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global restapi_base_url
ceph -s
```

---

### restapi_log_level

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [restapi.md#SP_restapi_log_level](../../../config/global/restapi.md#SP_restapi_log_level) |

**作用：** default set by python code

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global restapi_log_level "example"
ceph config get global restapi_log_level
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global restapi_log_level
ceph -s
```

---


[← 概览](../OVERVIEW.md)
