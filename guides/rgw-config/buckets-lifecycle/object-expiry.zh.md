# Object expiry hints

RGW 配置深度指南 — 2 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_objexp_chunk_size](#rgw_objexp_chunk_size) | `100` | Dev | 性能 |
| [rgw_objexp_hints_num_shards](#rgw_objexp_hints_num_shards) | `127` | Advanced | 策略 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、API 兼容性、租户限制 |
| **容量** | 磁盘布局、路径、池容量 |
| **性能** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **连通性** | 最近且稳定的外部端点 |
| **架构** | 后端、多站点拓扑 — 非数值扫描 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_objexp_chunk_size

| | |
|---|---|
| 类型 | Uint · default `100` · **Dev** |
| 表格 | [rgw.md#SP_rgw_objexp_chunk_size](../../../config/rgw/rgw.md#SP_rgw_objexp_chunk_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_objexp_chunk_size 100
ceph config get client.rgw rgw_objexp_chunk_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `100` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_objexp_chunk_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_hints_num_shards

| | |
|---|---|
| 类型 | Uint · default `127` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_objexp_hints_num_shards](../../../config/rgw/rgw.md#SP_rgw_objexp_hints_num_shards) |

**作用：** Number of object expirer data shards

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_objexp_hints_num_shards 127
ceph config get client.rgw rgw_objexp_hints_num_shards
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `127` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW 配置概览](../OVERVIEW.md)
