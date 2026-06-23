# Access & object logging

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_log_http_headers](#rgw_log_http_headers) | `(empty)` | Basic | 性能 |
| [rgw_log_nonexistent_bucket](#rgw_log_nonexistent_bucket) | `False` | Advanced | 策略 |
| [rgw_log_object_name](#rgw_log_object_name) | `%Y-%m-%d-%H-%i-%n` | Advanced | 性能 |
| [rgw_log_object_name_utc](#rgw_log_object_name_utc) | `False` | Advanced | 策略 |

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

### rgw_log_http_headers

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Basic** |
| 表格 | [rgw.md#SP_rgw_log_http_headers](../../../config/rgw/rgw.md#SP_rgw_log_http_headers) |

**作用：** List of HTTP headers to log

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_log_http_headers <value>
ceph config get client.rgw rgw_log_http_headers
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_http_headers
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_log_nonexistent_bucket

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_log_nonexistent_bucket](../../../config/rgw/rgw.md#SP_rgw_log_nonexistent_bucket) |

**作用：** Should RGW log operations on bucket that does not exist

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_log_nonexistent_bucket true
ceph config get client.rgw rgw_log_nonexistent_bucket
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_log_object_name

| | |
|---|---|
| 类型 | Str · default `%Y-%m-%d-%H-%i-%n` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_log_object_name](../../../config/rgw/rgw.md#SP_rgw_log_object_name) |

**作用：** Ops log object name format

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_log_object_name "%Y-%m-%d-%H-%i-%n"
ceph config get client.rgw rgw_log_object_name
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `%Y-%m-%d-%H-%i-%n`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_log_object_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_log_object_name_utc

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_log_object_name_utc](../../../config/rgw/rgw.md#SP_rgw_log_object_name_utc) |

**作用：** Should ops log object name based on UTC

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_log_object_name_utc true
ceph config get client.rgw rgw_log_object_name_utc
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
