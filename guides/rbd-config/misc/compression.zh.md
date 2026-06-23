# Compression

RBD 配置深度指南 — 1 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_compression_hint](#rbd_compression_hint) | `none` | Basic | 策略 |

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

### rbd_compression_hint

| | |
|---|---|
| 类型 | Str · enum: ["none", "compressible", "incompressible"] · default `none` · **Basic** |
| 表格 | [rbd.md#SP_rbd_compression_hint](../../../config/rbd/rbd.md#SP_rbd_compression_hint) |

**作用：** Compression hint to send to the OSDs during writes

**何时使用：** 核心 RBD 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client rbd_compression_hint none
ceph config get client rbd_compression_hint
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `none` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_compression_hint
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
