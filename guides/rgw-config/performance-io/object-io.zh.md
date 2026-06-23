# Object read/write windows

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_get_obj_max_req_size](#rgw_get_obj_max_req_size) | `4_M` | Advanced | Policy |
| [rgw_get_obj_window_size](#rgw_get_obj_window_size) | `16_M` | Advanced | Performance |
| [rgw_put_obj_max_window_size](#rgw_put_obj_max_window_size) | `64_M` | Advanced | Performance |
| [rgw_put_obj_min_window_size](#rgw_put_obj_min_window_size) | `16_M` | Advanced | Performance |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、API 兼容性、租户限制 |
| **Capacity** | 磁盘布局、路径、池容量 |
| **Performance** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **Connectivity** | 最近且稳定的外部端点 |
| **Architecture** | 后端、多站点拓扑 — 非数值扫描 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_get_obj_max_req_size

| | |
|---|---|
| 类型 | Size · default `4_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_get_obj_max_req_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_max_req_size) |

**作用：** RGW object read chunk size

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_get_obj_max_req_size 4_M
ceph config get client.rgw rgw_get_obj_max_req_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `4_M` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_get_obj_window_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_get_obj_window_size](../../../config/rgw/rgw.md#SP_rgw_get_obj_window_size) |

**作用：** RGW object read window size

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_get_obj_window_size 16_M
ceph config get client.rgw rgw_get_obj_window_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_get_obj_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_max_window_size

| | |
|---|---|
| 类型 | Size · default `64_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_put_obj_max_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_max_window_size) |

**作用：** The maximum RADOS write window size (in bytes).

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_put_obj_max_window_size 64_M
ceph config get client.rgw rgw_put_obj_max_window_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `64_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_max_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_put_obj_min_window_size

| | |
|---|---|
| 类型 | Size · default `16_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_put_obj_min_window_size](../../../config/rgw/rgw.md#SP_rgw_put_obj_min_window_size) |

**作用：** The minimum RADOS write window size (in bytes).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_put_obj_min_window_size 16_M
ceph config get client.rgw rgw_put_obj_min_window_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline `16_M` with your object size distribution (small vs large objects).
2. Larger windows/chunks improve throughput for big objects; may hurt small-object latency.
3. Change one step at a time; rerun `cosbench` or `warp` with the same object mix.

**观测信号：** PUT/GET p99 by object size, RADOS op count per MB transferred.

```bash
ceph config get client.rgw rgw_put_obj_min_window_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
