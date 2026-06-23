# Plugin

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [plugin_crypto_accelerator](#plugin_crypto_accelerator) | `crypto_isal` | Advanced | 性能 |
| [plugin_dir](#plugin_dir) | `0` | Advanced | 容量 |

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

### plugin_crypto_accelerator

| | |
|---|---|
| 类型 | Str · default `crypto_isal` · **Advanced** |
| 表格 | [plugin.md#SP_plugin_crypto_accelerator](../../../config/global/plugin.md#SP_plugin_crypto_accelerator) |

**作用：** Crypto accelerator library to use

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global plugin_crypto_accelerator crypto_isal
ceph config get global plugin_crypto_accelerator
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `crypto_isal` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global plugin_crypto_accelerator
ceph -s
```

---

### plugin_dir

| | |
|---|---|
| 类型 | Str · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [plugin.md#SP_plugin_dir](../../../config/global/plugin.md#SP_plugin_dir) |

**作用：** Base directory for dynamically loaded plugins

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global plugin_dir "/var/lib/ceph/example"
ceph config get global plugin_dir
```

**寻找最优值：**

**调优模型：** 容量

1. 以 `0` 为基线。
2. 变更路径前规划容量与文件系统布局。
3. 确保需共享路径的守护进程使用相同挂载。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global plugin_dir
ceph -s
```

---


[← 概览](../OVERVIEW.md)
