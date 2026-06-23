# Readahead

RBD 配置深度指南 — 3 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_readahead_disable_after_bytes](#rbd_readahead_disable_after_bytes) | `50_M` | Advanced | Performance |
| [rbd_readahead_max_bytes](#rbd_readahead_max_bytes) | `512_K` | Advanced | Performance |
| [rbd_readahead_trigger_requests](#rbd_readahead_trigger_requests) | `10` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_readahead_disable_after_bytes

| | |
|---|---|
| 类型 | Size · default `50_M` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_readahead_disable_after_bytes](../../../config/rbd/rbd.md#SP_rbd_readahead_disable_after_bytes) |

**作用：** how many bytes are read in total before readahead is disabled

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_readahead_disable_after_bytes 50_M
ceph config get client rbd_readahead_disable_after_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `50_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_readahead_disable_after_bytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_readahead_max_bytes

| | |
|---|---|
| 类型 | Size · default `512_K` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_readahead_max_bytes](../../../config/rbd/rbd.md#SP_rbd_readahead_max_bytes) |

**作用：** set to 0 to disable readahead

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set client rbd_readahead_max_bytes 512_K
ceph config get client rbd_readahead_max_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `512_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_readahead_max_bytes
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_readahead_trigger_requests

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_readahead_trigger_requests](../../../config/rbd/rbd.md#SP_rbd_readahead_trigger_requests) |

**作用：** number of sequential requests necessary to trigger readahead

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_readahead_trigger_requests 10
ceph config get client rbd_readahead_trigger_requests
```

**寻找最优值：**

**调优模型：** Performance

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_readahead_trigger_requests
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
