# Multipart & copy

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_copy_obj_progress](#rgw_copy_obj_progress) | `True` | Advanced | 策略 |
| [rgw_copy_obj_progress_every_bytes](#rgw_copy_obj_progress_every_bytes) | `1_M` | Advanced | 性能 |
| [rgw_multipart_min_part_size](#rgw_multipart_min_part_size) | `5_M` | Advanced | 性能 |
| [rgw_multipart_part_upload_limit](#rgw_multipart_part_upload_limit) | `10000` | Advanced | 策略 |

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

### rgw_copy_obj_progress

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_copy_obj_progress](../../../config/rgw/rgw.md#SP_rgw_copy_obj_progress) |

**作用：** Send progress report through copy operation If true, RGW will send progress information when copy operation is executed.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_copy_obj_progress false
ceph config get client.rgw rgw_copy_obj_progress
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_copy_obj_progress_every_bytes

| | |
|---|---|
| 类型 | Size · default `1_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_copy_obj_progress_every_bytes](../../../config/rgw/rgw.md#SP_rgw_copy_obj_progress_every_bytes) |

**作用：** Send copy-object progress info after these many bytes

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_copy_obj_progress_every_bytes 1_M
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_copy_obj_progress_every_bytes
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_min_part_size

| | |
|---|---|
| 类型 | Size · default `5_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_multipart_min_part_size](../../../config/rgw/rgw.md#SP_rgw_multipart_min_part_size) |

**作用：** Minimum S3 multipart-upload part size When doing a multipart upload, each part (other than the last part) must be at least this size.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_multipart_min_part_size 5_M
ceph config get client.rgw rgw_multipart_min_part_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_multipart_min_part_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_multipart_part_upload_limit

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_multipart_part_upload_limit](../../../config/rgw/rgw.md#SP_rgw_multipart_part_upload_limit) |

**作用：** Max number of parts in multipart upload

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_multipart_part_upload_limit 10000
ceph config get client.rgw rgw_multipart_part_upload_limit
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`10000`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---


[← RGW 配置概览](../OVERVIEW.md)
