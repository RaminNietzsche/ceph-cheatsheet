# Zones, realm & region

RGW 配置深度指南 — 19 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_default_realm_info_oid](#rgw_default_realm_info_oid) | `default.realm` | Advanced | Performance |
| [rgw_default_region_info_oid](#rgw_default_region_info_oid) | `default.region` | Advanced | Performance |
| [rgw_default_zone_info_oid](#rgw_default_zone_info_oid) | `default.zone` | Advanced | Performance |
| [rgw_default_zonegroup_info_oid](#rgw_default_zonegroup_info_oid) | `default.zonegroup` | Advanced | Performance |
| [rgw_period_latest_epoch_info_oid](#rgw_period_latest_epoch_info_oid) | `.latest_epoch` | Dev | Performance |
| [rgw_period_push_interval](#rgw_period_push_interval) | `2` | Advanced | Performance |
| [rgw_period_push_interval_max](#rgw_period_push_interval_max) | `30` | Advanced | Performance |
| [rgw_period_root_pool](#rgw_period_root_pool) | `.rgw.root` | Advanced | Performance |
| [rgw_realm](#rgw_realm) | `(empty)` | Advanced | Architecture |
| [rgw_realm_id](#rgw_realm_id) | `(empty)` | Advanced | Architecture |
| [rgw_realm_root_pool](#rgw_realm_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_region](#rgw_region) | `(empty)` | Advanced | Architecture |
| [rgw_region_root_pool](#rgw_region_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zone](#rgw_zone) | `(empty)` | Advanced | Architecture |
| [rgw_zone_id](#rgw_zone_id) | `(empty)` | Advanced | Architecture |
| [rgw_zone_root_pool](#rgw_zone_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zonegroup](#rgw_zonegroup) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_id](#rgw_zonegroup_id) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_root_pool](#rgw_zonegroup_root_pool) | `.rgw.root` | Advanced | Architecture |

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

### rgw_default_realm_info_oid

| | |
|---|---|
| 类型 | Str · default `default.realm` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_default_realm_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_realm_info_oid) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_default_realm_info_oid "default.realm"
ceph config get client.rgw rgw_default_realm_info_oid
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `default.realm`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_realm_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_region_info_oid

| | |
|---|---|
| 类型 | Str · default `default.region` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_default_region_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_region_info_oid) |

**作用：** Default region info object id

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_default_region_info_oid "default.region"
ceph config get client.rgw rgw_default_region_info_oid
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `default.region`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_region_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zone_info_oid

| | |
|---|---|
| 类型 | Str · default `default.zone` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_default_zone_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_zone_info_oid) |

**作用：** Default zone info object id

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_default_zone_info_oid "default.zone"
ceph config get client.rgw rgw_default_zone_info_oid
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `default.zone`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zone_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_default_zonegroup_info_oid

| | |
|---|---|
| 类型 | Str · default `default.zonegroup` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_default_zonegroup_info_oid](../../../config/rgw/rgw.md#SP_rgw_default_zonegroup_info_oid) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_default_zonegroup_info_oid "default.zonegroup"
ceph config get client.rgw rgw_default_zonegroup_info_oid
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `default.zonegroup`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_default_zonegroup_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_latest_epoch_info_oid

| | |
|---|---|
| 类型 | Str · default `.latest_epoch` · **Dev** |
| 表格 | [rgw.md#SP_rgw_period_latest_epoch_info_oid](../../../config/rgw/rgw.md#SP_rgw_period_latest_epoch_info_oid) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_period_latest_epoch_info_oid ".latest_epoch"
ceph config get client.rgw rgw_period_latest_epoch_info_oid
```

**寻找最优值：**

**调优模型：** Performance

1. Default `.latest_epoch` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_latest_epoch_info_oid
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval

| | |
|---|---|
| 类型 | Float · default `2` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_period_push_interval](../../../config/rgw/rgw.md#SP_rgw_period_push_interval) |

**作用：** Period push interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_period_push_interval 2
ceph config get client.rgw rgw_period_push_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Default `2` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval_max

| | |
|---|---|
| 类型 | Float · default `30` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_period_push_interval_max](../../../config/rgw/rgw.md#SP_rgw_period_push_interval_max) |

**作用：** Period push maximum interval

**何时使用：**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**示例：**

```bash
ceph config set client.rgw rgw_period_push_interval_max 30
ceph config get client.rgw rgw_period_push_interval_max
```

**寻找最优值：**

**调优模型：** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval_max
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_period_root_pool

| | |
|---|---|
| 类型 | Str · default `.rgw.root` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_period_root_pool](../../../config/rgw/rgw.md#SP_rgw_period_root_pool) |

**作用：** Period root pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_period_root_pool ".rgw.root"
ceph config get client.rgw rgw_period_root_pool
```

**寻找最优值：**

**调优模型：** Performance

1. Default `.rgw.root` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**观测信号：** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_root_pool
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_realm

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_realm](../../../config/rgw/rgw.md#SP_rgw_realm) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_realm "default"
ceph config get client.rgw rgw_realm
radosgw-admin realm list
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_realm_id

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_realm_id](../../../config/rgw/rgw.md#SP_rgw_realm_id) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_realm_id <value>
ceph config get client.rgw rgw_realm_id
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_realm_root_pool

| | |
|---|---|
| 类型 | Str · default `.rgw.root` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_realm_root_pool](../../../config/rgw/rgw.md#SP_rgw_realm_root_pool) |

**作用：** Realm root pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_realm_root_pool ".rgw.root"
ceph config get client.rgw rgw_realm_root_pool
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_region

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_region](../../../config/rgw/rgw.md#SP_rgw_region) |

**作用：** Region name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_region "us-east-1"
ceph config get client.rgw rgw_region
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_region_root_pool

| | |
|---|---|
| 类型 | Str · default `.rgw.root` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_region_root_pool](../../../config/rgw/rgw.md#SP_rgw_region_root_pool) |

**作用：** Region root pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_region_root_pool ".rgw.root"
ceph config get client.rgw rgw_region_root_pool
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zone](../../../config/rgw/rgw.md#SP_rgw_zone) |

**作用：** Zone name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zone "us-east-1"
ceph config get client.rgw rgw_zone
ceph config get client.rgw rgw_zone
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone_id

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zone_id](../../../config/rgw/rgw.md#SP_rgw_zone_id) |

**作用：** Zone ID

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zone_id <value>
ceph config get client.rgw rgw_zone_id
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zone_root_pool

| | |
|---|---|
| 类型 | Str · default `.rgw.root` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zone_root_pool](../../../config/rgw/rgw.md#SP_rgw_zone_root_pool) |

**作用：** Zone root pool name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zone_root_pool ".rgw.root"
ceph config get client.rgw rgw_zone_root_pool
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zonegroup](../../../config/rgw/rgw.md#SP_rgw_zonegroup) |

**作用：** Zonegroup name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zonegroup "default"
ceph config get client.rgw rgw_zonegroup
ceph config get client.rgw rgw_zonegroup
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup_id

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zonegroup_id](../../../config/rgw/rgw.md#SP_rgw_zonegroup_id) |

**作用：** Zonegroup ID

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zonegroup_id <value>
ceph config get client.rgw rgw_zonegroup_id
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---

### rgw_zonegroup_root_pool

| | |
|---|---|
| 类型 | Str · default `.rgw.root` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_zonegroup_root_pool](../../../config/rgw/rgw.md#SP_rgw_zonegroup_root_pool) |

**作用：** Zonegroup root pool

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_zonegroup_root_pool ".rgw.root"
ceph config get client.rgw rgw_zonegroup_root_pool
radosgw-admin sync status
```

**寻找最优值：**

**调优模型：** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin sync status
ceph config get client.rgw rgw_zone
```

---


[← RGW 配置概览](../OVERVIEW.md)
