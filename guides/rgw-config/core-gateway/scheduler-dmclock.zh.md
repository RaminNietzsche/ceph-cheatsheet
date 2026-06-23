# Scheduler & dmclock

RGW 配置深度指南 — 13 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_dmclock_admin_lim](#rgw_dmclock_admin_lim) | `0` | Advanced | 性能 |
| [rgw_dmclock_admin_res](#rgw_dmclock_admin_res) | `100` | Advanced | 性能 |
| [rgw_dmclock_admin_wgt](#rgw_dmclock_admin_wgt) | `100` | Advanced | 性能 |
| [rgw_dmclock_auth_lim](#rgw_dmclock_auth_lim) | `0` | Advanced | 性能 |
| [rgw_dmclock_auth_res](#rgw_dmclock_auth_res) | `200` | Advanced | 性能 |
| [rgw_dmclock_auth_wgt](#rgw_dmclock_auth_wgt) | `100` | Advanced | 性能 |
| [rgw_dmclock_data_lim](#rgw_dmclock_data_lim) | `0` | Advanced | 性能 |
| [rgw_dmclock_data_res](#rgw_dmclock_data_res) | `500` | Advanced | 性能 |
| [rgw_dmclock_data_wgt](#rgw_dmclock_data_wgt) | `500` | Advanced | 性能 |
| [rgw_dmclock_metadata_lim](#rgw_dmclock_metadata_lim) | `0` | Advanced | 性能 |
| [rgw_dmclock_metadata_res](#rgw_dmclock_metadata_res) | `500` | Advanced | 性能 |
| [rgw_dmclock_metadata_wgt](#rgw_dmclock_metadata_wgt) | `500` | Advanced | 性能 |
| [rgw_scheduler_type](#rgw_scheduler_type) | `throttler` | Advanced | 性能 |

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

### rgw_dmclock_admin_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_admin_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_lim) |

**作用：** mclock limit for admin requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_admin_lim 0
ceph config get client.rgw rgw_dmclock_admin_lim
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_res

| | |
|---|---|
| 类型 | Float · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_admin_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_res) |

**作用：** mclock reservation for admin requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_admin_res 100
ceph config get client.rgw rgw_dmclock_admin_res
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_wgt

| | |
|---|---|
| 类型 | Float · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_admin_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_wgt) |

**作用：** mclock weight for admin requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_admin_wgt 100
ceph config get client.rgw rgw_dmclock_admin_wgt
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_auth_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_lim) |

**作用：** mclock limit for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_auth_lim 0
ceph config get client.rgw rgw_dmclock_auth_lim
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_res

| | |
|---|---|
| 类型 | Float · default `200` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_auth_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_res) |

**作用：** mclock reservation for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_auth_res 200
ceph config get client.rgw rgw_dmclock_auth_res
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`200`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_wgt

| | |
|---|---|
| 类型 | Float · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_auth_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_wgt) |

**作用：** mclock weight for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_auth_wgt 100
ceph config get client.rgw rgw_dmclock_auth_wgt
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_data_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_lim) |

**作用：** mclock limit for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_data_lim 0
ceph config get client.rgw rgw_dmclock_data_lim
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_res

| | |
|---|---|
| 类型 | Float · default `500` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_data_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_res) |

**作用：** mclock reservation for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_data_res 500
ceph config get client.rgw rgw_dmclock_data_res
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_wgt

| | |
|---|---|
| 类型 | Float · default `500` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_data_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_wgt) |

**作用：** mclock weight for object data requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_data_wgt 500
ceph config get client.rgw rgw_dmclock_data_wgt
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_lim

| | |
|---|---|
| 类型 | Float · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_metadata_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_lim) |

**作用：** mclock limit for metadata requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_metadata_lim 0
ceph config get client.rgw rgw_dmclock_metadata_lim
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_lim
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_res

| | |
|---|---|
| 类型 | Float · default `500` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_metadata_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_res) |

**作用：** mclock reservation for metadata requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_metadata_res 500
ceph config get client.rgw rgw_dmclock_metadata_res
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_res
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_wgt

| | |
|---|---|
| 类型 | Float · default `500` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dmclock_metadata_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_wgt) |

**作用：** mclock weight for metadata requests

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dmclock_metadata_wgt 500
ceph config get client.rgw rgw_dmclock_metadata_wgt
```

**寻找最优值：**

**调优模型：** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**观测信号：** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_wgt
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_scheduler_type

| | |
|---|---|
| 类型 | Str · default `throttler` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_scheduler_type](../../../config/rgw/rgw.md#SP_rgw_scheduler_type) |

**作用：** Set the type of dmclock scheduler, defaults to throttler. Other valid value is dmclock which is experimental.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_scheduler_type throttler
ceph config get client.rgw rgw_scheduler_type
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `throttler`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_scheduler_type
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
