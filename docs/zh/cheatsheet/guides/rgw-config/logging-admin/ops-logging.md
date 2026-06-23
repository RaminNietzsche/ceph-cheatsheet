# Ops logging

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_ops_log_data_backlog](#rgw_ops_log_data_backlog) | `5_M` | Advanced | 性能 |
| [rgw_ops_log_file_path](#rgw_ops_log_file_path) | `/var/log/ceph/ops-log-$cluster-$name.log` | Advanced | 容量 |
| [rgw_ops_log_rados](#rgw_ops_log_rados) | `False` | Advanced | 策略 |
| [rgw_ops_log_socket_path](#rgw_ops_log_socket_path) | `(empty)` | Advanced | 容量 |

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

### rgw_ops_log_data_backlog

| | |
|---|---|
| 类型 | Size · default `5_M` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ops_log_data_backlog](../../../config/rgw/rgw.md#SP_rgw_ops_log_data_backlog) |

**作用：** Ops log socket backlog

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ops_log_data_backlog 5_M
ceph config get client.rgw rgw_ops_log_data_backlog
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5_M`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ops_log_data_backlog
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ops_log_file_path

| | |
|---|---|
| 类型 | Str · default `/var/log/ceph/ops-log-$cluster-$name.log` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ops_log_file_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_file_path) |

**作用：** File-system path for ops log.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ops_log_file_path "/var/log/ceph/ops-log-$cluster-$name.log"
ceph config get client.rgw rgw_ops_log_file_path
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/var/log/ceph/ops-log-$cluster-$name.log`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_file_path)
iostat -x 5  # disk saturation
```

---

### rgw_ops_log_rados

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ops_log_rados](../../../config/rgw/rgw.md#SP_rgw_ops_log_rados) |

**作用：** Use RADOS for ops log

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_ops_log_rados true
ceph config get client.rgw rgw_ops_log_rados
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_ops_log_socket_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ops_log_socket_path](../../../config/rgw/rgw.md#SP_rgw_ops_log_socket_path) |

**作用：** Unix domain socket path for ops log.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ops_log_socket_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_ops_log_socket_path
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_ops_log_socket_path)
iostat -x 5  # disk saturation
```

---


[← RGW 配置概览](../OVERVIEW.md)
