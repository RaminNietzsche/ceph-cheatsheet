# Tmp

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [tmp_dir](#tmp_dir) | `/tmp` | Advanced | Capacity |
| [tmp_file_template](#tmp_file_template) | `$tmp_dir/$cluster-$name.XXXXXX` | Advanced | Performance |

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

### tmp_dir

| | |
|---|---|
| 类型 | Str · default `/tmp` · **Advanced** |
| 表格 | [tmp.md#SP_tmp_dir](../../../config/global/tmp.md#SP_tmp_dir) |

**作用：** Path for the 'tmp' directory

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global tmp_dir "/tmp"
ceph config get global tmp_dir
```

**寻找最优值：**

**调优模型：** Capacity

1. 以 `/tmp` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global tmp_dir
ceph -s
```

---

### tmp_file_template

| | |
|---|---|
| 类型 | Str · default `$tmp_dir/$cluster-$name.XXXXXX` · **Advanced** |
| 表格 | [tmp.md#SP_tmp_file_template](../../../config/global/tmp.md#SP_tmp_file_template) |

**作用：** Template for temporary files created by daemons for ceph tell commands

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global tmp_file_template "$tmp_dir/$cluster-$name.XXXXXX"
ceph config get global tmp_file_template
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `$tmp_dir/$cluster-$name.XXXXXX` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global tmp_file_template
ceph -s
```

---


[← 概览](../OVERVIEW.md)
