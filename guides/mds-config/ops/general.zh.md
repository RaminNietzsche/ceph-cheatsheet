# General

MDS 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [defer_client_eviction_on_laggy_osds](#defer_client_eviction_on_laggy_osds) | `False` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### defer_client_eviction_on_laggy_osds

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mds.md#SP_defer_client_eviction_on_laggy_osds](../../../config/mds/mds.md#SP_defer_client_eviction_on_laggy_osds) |

**作用：** Do not evict client if any osd is laggy

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set mds defer_client_eviction_on_laggy_osds true
ceph config get mds defer_client_eviction_on_laggy_osds
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mds defer_client_eviction_on_laggy_osds
ceph -s
ceph fs status
ceph mds stat
```

---


[← 概览](../OVERVIEW.md)
