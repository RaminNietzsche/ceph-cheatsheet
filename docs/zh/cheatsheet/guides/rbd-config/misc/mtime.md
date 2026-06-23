# Mtime

RBD 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_mtime_update_interval](#rbd_mtime_update_interval) | `60` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_mtime_update_interval

| | |
|---|---|
| 类型 | Uint · default `60` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_mtime_update_interval](../../../config/rbd/rbd.md#SP_rbd_mtime_update_interval) |

**作用：** RBD Image modify timestamp refresh interval. Set to 0 to disable modify timestamp update.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set client rbd_mtime_update_interval 60
ceph config get client rbd_mtime_update_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `60` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `0`，最大 `—`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_mtime_update_interval
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
