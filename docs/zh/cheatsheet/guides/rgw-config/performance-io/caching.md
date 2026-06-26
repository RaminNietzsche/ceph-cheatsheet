# Metadata & object caches

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_cache_enabled](#rgw_cache_enabled) | `True` | Advanced | 性能 |
| [rgw_cache_expiry_interval](#rgw_cache_expiry_interval) | `900` | Advanced | 性能 |
| [rgw_cache_lru_size](#rgw_cache_lru_size) | `25000` | Advanced | 性能 |
| [rgw_obj_tombstone_cache_size](#rgw_obj_tombstone_cache_size) | `1000` | Advanced | 性能 |

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

### rgw_cache_enabled

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_cache_enabled) |

**作用：** Enable RGW metadata cache. The metadata cache holds metadata entries that RGW requires for processing requests. Metadata entries can be user info, bucket info, and bucket instance info. If not found in the cache, entries will be fetched from the backing RADOS store.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`rgw_cache_lru_size`](../../../config/rgw/rgw.md#SP_rgw_cache_lru_size)

**示例：**

```bash
ceph config set client.rgw rgw_cache_enabled false
ceph config get client.rgw rgw_cache_enabled
```

**寻找最优值：**

**调优模型：** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_cache_expiry_interval

| | |
|---|---|
| 类型 | Uint · default `900` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_cache_expiry_interval](../../../config/rgw/rgw.md#SP_rgw_cache_expiry_interval) |

**作用：** Number of seconds before entries in the cache are assumed stale and re-fetched. Zero is never. The Rados Gateway stores metadata and objects in an internal cache. This should be kept consistent by the OSD's relaying notify events between multiple watching RGW processes. In the event that this notification protocol fails, bounding the length of time that any data in the cache will be assumed valid will ensure that any RGW instance that falls out of sync will eventually recover. This seems to be an issue mostly for large numbers of RGW instances under heavy use. If you would like to turn off cache expiry, set this value to zero.

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_cache_expiry_interval 900
ceph config get client.rgw rgw_cache_expiry_interval
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `900`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_cache_expiry_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_cache_lru_size

| | |
|---|---|
| 类型 | Int · default `25000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_cache_lru_size](../../../config/rgw/rgw.md#SP_rgw_cache_lru_size) |

**作用：** Max number of items in RGW metadata cache. When full, the RGW metadata cache evicts least recently used entries.

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**相关选项：**

- [`rgw_cache_enabled`](../../../config/rgw/rgw.md#SP_rgw_cache_enabled)

**示例：**

```bash
ceph config set client.rgw rgw_cache_lru_size 25000
ceph config get client.rgw rgw_cache_lru_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `25000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_cache_lru_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_obj_tombstone_cache_size

| | |
|---|---|
| 类型 | Int · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_obj_tombstone_cache_size](../../../config/rgw/rgw.md#SP_rgw_obj_tombstone_cache_size) |

**作用：** Max number of entries to keep in tombstone cache The tombstone cache is used when doing a multi-zone data sync. RGW keeps there information about removed objects which is needed in order to prevent re-syncing of objects that were already removed.

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_obj_tombstone_cache_size 1000
ceph config get client.rgw rgw_obj_tombstone_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_obj_tombstone_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
