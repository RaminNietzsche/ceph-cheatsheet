# Crush

Global 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [crush_location](#crush_location) | `(empty)` | Advanced | 性能 |
| [crush_location_hook](#crush_location_hook) | `(empty)` | Advanced | 性能 |
| [crush_location_hook_timeout](#crush_location_hook_timeout) | `10` | Advanced | 性能 |

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

### crush_location

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [crush.md#SP_crush_location](../../../config/global/crush.md#SP_crush_location) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global crush_location "example"
ceph config get global crush_location
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global crush_location
ceph -s
```

---

### crush_location_hook

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [crush.md#SP_crush_location_hook](../../../config/global/crush.md#SP_crush_location_hook) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global crush_location_hook "example"
ceph config get global crush_location_hook
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global crush_location_hook
ceph -s
```

---

### crush_location_hook_timeout

| | |
|---|---|
| 类型 | Int · default `10` · **Advanced** |
| 表格 | [crush.md#SP_crush_location_hook_timeout](../../../config/global/crush.md#SP_crush_location_hook_timeout) |

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global crush_location_hook_timeout 10
ceph config get global crush_location_hook_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global crush_location_hook_timeout
ceph -s
```

---


[← 概览](../OVERVIEW.md)
