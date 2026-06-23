# Run

Global 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [run_dir](#run_dir) | `/var/run/ceph` | Advanced | 容量 |

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

### run_dir

| | |
|---|---|
| 类型 | Str · default `/var/run/ceph` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [run.md#SP_run_dir](../../../config/global/run.md#SP_run_dir) |

**作用：** Path for the 'run' directory for storing pid and socket files

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global run_dir "/var/run/ceph"
ceph config get global run_dir
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `/var/run/ceph` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global run_dir
ceph -s
```

---


[← 概览](../OVERVIEW.md)
