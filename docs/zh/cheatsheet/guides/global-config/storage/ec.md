# Ec

Global 配置深度指南 — 2 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [ec_extent_cache_size](#ec_extent_cache_size) | `10485760` | Advanced | 性能 |
| [ec_pdw_write_mode](#ec_pdw_write_mode) | `0` | Dev | 开发 |

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

### ec_extent_cache_size

| | |
|---|---|
| 类型 | Uint · default `10485760` · **Advanced** |
| 表格 | [ec.md#SP_ec_extent_cache_size](../../../config/global/ec.md#SP_ec_extent_cache_size) |

**作用：** Size of the per-shard extent cache

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ec_extent_cache_size 10485760
ceph config get global ec_extent_cache_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10485760` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ec_extent_cache_size
ceph -s
```

---

### ec_pdw_write_mode

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [ec.md#SP_ec_pdw_write_mode](../../../config/global/ec.md#SP_ec_pdw_write_mode) |

**作用：** When EC writes should generate PDWs (development only) 0=optimal 1=never 2=when possible

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ec_pdw_write_mode 64
ceph config get global ec_pdw_write_mode
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---


[← 概览](../OVERVIEW.md)
