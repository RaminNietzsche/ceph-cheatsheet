# Compressor

Global 配置深度指南 — 4 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [compressor_zlib_isal](#compressor_zlib_isal) | `False` | Advanced | 性能 |
| [compressor_zlib_level](#compressor_zlib_level) | `5` | Advanced | 性能 |
| [compressor_zlib_winsize](#compressor_zlib_winsize) | `-15` | Advanced | 性能 |
| [compressor_zstd_level](#compressor_zstd_level) | `1` | Advanced | 性能 |

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

### compressor_zlib_isal

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [compressor.md#SP_compressor_zlib_isal](../../../config/global/compressor.md#SP_compressor_zlib_isal) |

**作用：** Use Intel ISA-L accelerated zlib implementation if available

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global compressor_zlib_isal true
ceph config get global compressor_zlib_isal
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global compressor_zlib_isal
ceph -s
```

---

### compressor_zlib_level

| | |
|---|---|
| 类型 | Int · default `5` · **Advanced** |
| 表格 | [compressor.md#SP_compressor_zlib_level](../../../config/global/compressor.md#SP_compressor_zlib_level) |

**作用：** Zlib compression level to use

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global compressor_zlib_level 5
ceph config get global compressor_zlib_level
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `5` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global compressor_zlib_level
ceph -s
```

---

### compressor_zlib_winsize

| | |
|---|---|
| 类型 | Int · default `-15` · **Advanced** |
| 表格 | [compressor.md#SP_compressor_zlib_winsize](../../../config/global/compressor.md#SP_compressor_zlib_winsize) |

**作用：** Zlib compression winsize to use

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global compressor_zlib_winsize -15
ceph config get global compressor_zlib_winsize
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `-15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `-15`，最大 `32`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global compressor_zlib_winsize
ceph -s
```

---

### compressor_zstd_level

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** |
| 表格 | [compressor.md#SP_compressor_zstd_level](../../../config/global/compressor.md#SP_compressor_zstd_level) |

**作用：** Zstd compression level to use

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global compressor_zstd_level 1
ceph config get global compressor_zstd_level
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global compressor_zstd_level
ceph -s
```

---


[← 概览](../OVERVIEW.md)
