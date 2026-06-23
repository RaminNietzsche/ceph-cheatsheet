# POSIX backend

RGW 配置深度指南 — 7 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_posix_base_path](#rgw_posix_base_path) | `/tmp/rgw_posix_driver` | Advanced | 架构 |
| [rgw_posix_cache_lanes](#rgw_posix_cache_lanes) | `3` | Advanced | 架构 |
| [rgw_posix_cache_lmdb_count](#rgw_posix_cache_lmdb_count) | `3` | Advanced | 架构 |
| [rgw_posix_cache_max_buckets](#rgw_posix_cache_max_buckets) | `100` | Advanced | 架构 |
| [rgw_posix_cache_partitions](#rgw_posix_cache_partitions) | `3` | Advanced | 架构 |
| [rgw_posix_database_root](#rgw_posix_database_root) | `/var/lib/ceph/radosgw` | Advanced | 架构 |
| [rgw_posix_userdb_dir](#rgw_posix_userdb_dir) | `/var/lib/ceph/radosgw` | Advanced | 架构 |

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

### rgw_posix_base_path

| | |
|---|---|
| 类型 | Str · default `/tmp/rgw_posix_driver` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_base_path](../../../config/rgw/rgw.md#SP_rgw_posix_base_path) |

**作用：** experimental Option to set base path for POSIX Driver

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw rgw_posix_base_path "/tmp/rgw_posix_driver"
ceph config get client.rgw rgw_posix_base_path
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/tmp/rgw_posix_driver` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lanes

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_cache_lanes](../../../config/rgw/rgw.md#SP_rgw_posix_cache_lanes) |

**作用：** experimental Number of lanes in cache LRU

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_posix_cache_lanes 3
ceph config get client.rgw rgw_posix_cache_lanes
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lmdb_count

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_cache_lmdb_count](../../../config/rgw/rgw.md#SP_rgw_posix_cache_lmdb_count) |

**作用：** experimental Number of lmdb partitions in the ordered listing cache

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_posix_cache_lmdb_count 3
ceph config get client.rgw rgw_posix_cache_lmdb_count
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_max_buckets

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_cache_max_buckets](../../../config/rgw/rgw.md#SP_rgw_posix_cache_max_buckets) |

**作用：** experimental Number of buckets to maintain in the ordered listing cache

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_posix_cache_max_buckets 100
ceph config get client.rgw rgw_posix_cache_max_buckets
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `100` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_partitions

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_cache_partitions](../../../config/rgw/rgw.md#SP_rgw_posix_cache_partitions) |

**作用：** experimental Number of partitions in cache AVL

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_posix_cache_partitions 3
ceph config get client.rgw rgw_posix_cache_partitions
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_database_root

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_database_root](../../../config/rgw/rgw.md#SP_rgw_posix_database_root) |

**作用：** experimental Path to parent of POSIX Driver LMDB bucket listing cache

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw rgw_posix_database_root "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_database_root
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_userdb_dir

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_posix_userdb_dir](../../../config/rgw/rgw.md#SP_rgw_posix_userdb_dir) |

**作用：** path for the directory for storing the User db

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw rgw_posix_userdb_dir "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_userdb_dir
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---


[← RGW 配置概览](../OVERVIEW.md)
