# Target

Global 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [target_max_misplaced_ratio](#target_max_misplaced_ratio) | `0.05` | Basic | Performance |

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

### target_max_misplaced_ratio

| | |
|---|---|
| 类型 | Float · default `0.05` · **Basic** |
| 表格 | [target.md#SP_target_max_misplaced_ratio](../../../config/global/target.md#SP_target_max_misplaced_ratio) |

**作用：** Max ratio of misplaced RADOS objects to target when scheduling data rebalancing activity. A lower value results in the balancer making smaller, less impactful changes with the tradeoff of decreased efficiency and longer time to converge. When making CRUSH rules or topolgy changes or performing large cluster expansions, a lower value can help avoid transitory nearfull or backfillfull ratio excursions.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global target_max_misplaced_ratio 0.05
ceph config get global target_max_misplaced_ratio
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `0.05` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global target_max_misplaced_ratio
ceph -s
```

---


[← 概览](../OVERVIEW.md)
