# BitTorrent

RGW 配置深度指南 — 8 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_torrent_comment](#rgw_torrent_comment) | `(empty)` | Advanced | Performance |
| [rgw_torrent_createby](#rgw_torrent_createby) | `(empty)` | Advanced | Performance |
| [rgw_torrent_encoding](#rgw_torrent_encoding) | `(empty)` | Advanced | Performance |
| [rgw_torrent_flag](#rgw_torrent_flag) | `False` | Advanced | Policy |
| [rgw_torrent_max_size](#rgw_torrent_max_size) | `5_G` | Advanced | Policy |
| [rgw_torrent_origin](#rgw_torrent_origin) | `(empty)` | Advanced | Performance |
| [rgw_torrent_sha_unit](#rgw_torrent_sha_unit) | `512_K` | Advanced | Performance |
| [rgw_torrent_tracker](#rgw_torrent_tracker) | `(empty)` | Advanced | Performance |

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

### rgw_torrent_comment

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_comment](../../../config/rgw/rgw.md#SP_rgw_torrent_comment) |

**作用：** Torrent field comment

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_comment <value>
ceph config get client.rgw rgw_torrent_comment
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_comment
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_createby

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_createby](../../../config/rgw/rgw.md#SP_rgw_torrent_createby) |

**作用：** torrent field created by

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_createby <value>
ceph config get client.rgw rgw_torrent_createby
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_createby
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_encoding

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_encoding](../../../config/rgw/rgw.md#SP_rgw_torrent_encoding) |

**作用：** torrent field encoding

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_encoding <value>
ceph config get client.rgw rgw_torrent_encoding
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_encoding
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_flag

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_flag](../../../config/rgw/rgw.md#SP_rgw_torrent_flag) |

**作用：** When true, uploaded objects will calculate and store a SHA256 hash of object data so the object can be retrieved as a torrent file

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_flag true
ceph config get client.rgw rgw_torrent_flag
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_torrent_max_size

| | |
|---|---|
| 类型 | Size · default `5_G` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_max_size](../../../config/rgw/rgw.md#SP_rgw_torrent_max_size) |

**作用：** Objects over this size will not store torrent info.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_max_size 5_G
ceph config get client.rgw rgw_torrent_max_size
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `5_G` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_torrent_origin

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_origin](../../../config/rgw/rgw.md#SP_rgw_torrent_origin) |

**作用：** Torrent origin

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_origin <value>
ceph config get client.rgw rgw_torrent_origin
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_origin
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_sha_unit

| | |
|---|---|
| 类型 | Size · default `512_K` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_sha_unit](../../../config/rgw/rgw.md#SP_rgw_torrent_sha_unit) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_sha_unit 512_K
ceph config get client.rgw rgw_torrent_sha_unit
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_sha_unit
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_torrent_tracker

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_torrent_tracker](../../../config/rgw/rgw.md#SP_rgw_torrent_tracker) |

**作用：** Torrent field announce and announce list

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_torrent_tracker <value>
ceph config get client.rgw rgw_torrent_tracker
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_torrent_tracker
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
