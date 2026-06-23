# No

Global 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [no_config_file](#no_config_file) | `False` | Advanced | Capacity |

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

### no_config_file

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [no.md#SP_no_config_file](../../../config/global/no.md#SP_no_config_file) |

**作用：** Signal that we don't require a config file to be present

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global no_config_file true
ceph config get global no_config_file
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `False` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global no_config_file
ceph -s
```

---


[← 概览](../OVERVIEW.md)
