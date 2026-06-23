# Experimental backends

RGW 配置深度指南 — 6 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [daos_pool](#daos_pool) | `tank` | Advanced | Capacity |
| [dbstore_config_uri](#dbstore_config_uri) | `file:/var/lib/ceph/radosgw/dbstore-config.db` | Advanced | Capacity |
| [dbstore_db_dir](#dbstore_db_dir) | `/var/lib/ceph/radosgw` | Advanced | Capacity |
| [dbstore_db_name_prefix](#dbstore_db_name_prefix) | `dbstore` | Advanced | Performance |
| [rgw_backend_store](#rgw_backend_store) | `rados` | Advanced | Architecture |
| [rgw_config_store](#rgw_config_store) | `rados` | Advanced | Architecture |

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

### daos_pool

| | |
|---|---|
| 类型 | Str · default `tank` · **Advanced** |
| 表格 | [rgw.md#SP_daos_pool](../../../config/rgw/rgw.md#SP_daos_pool) |

**作用：** Name of the [DAOS](https://docs.daos.io/) pool RGW connects to when `rgw_backend_store = daos`.

**何时使用：** Experimental DAOS-backed RGW (build with `-DWITH_RADOSGW_DAOS=ON`). Not used in standard Ceph clusters on RADOS.

**示例：**

```ini
[client.rgw]
rgw backend store = daos
daos pool = mypool
```

Provision the DAOS pool with your site DAOS admin tools before setting this option.

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`tank`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw daos_pool)
iostat -x 5  # disk saturation
```

---

### dbstore_config_uri

| | |
|---|---|
| 类型 | Str · default `file:/var/lib/ceph/radosgw/dbstore-config.db` · **Advanced** |
| 表格 | [rgw.md#SP_dbstore_config_uri](../../../config/rgw/rgw.md#SP_dbstore_config_uri) |

**作用：** URI for the **configuration database** when using the experimental **dbstore** backend. URIs starting with `file:` point at a local SQLite file.

**何时使用：** Standalone RGW without MON/OSD. See [dbstore README](https://github.com/ceph/ceph/blob/main/src/rgw/driver/dbstore/README.md).

**相关选项：**

- `rgw_backend_store` = `dbstore`
- `rgw_config_store` = `dbstore`
- `dbstore_db_dir`, `dbstore_db_name_prefix`

**示例：**

```bash
ceph config set client.rgw rgw_backend_store dbstore
ceph config set client.rgw rgw_config_store dbstore
ceph config set client.rgw dbstore_config_uri file:/var/lib/ceph/radosgw/dbstore-config.db
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`file:/var/lib/ceph/radosgw/dbstore-config.db`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw dbstore_config_uri)
iostat -x 5  # disk saturation
```

---

### dbstore_db_dir

| | |
|---|---|
| 类型 | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| 表格 | [rgw.md#SP_dbstore_db_dir](../../../config/rgw/rgw.md#SP_dbstore_db_dir) |

**作用：** Directory where dbstore writes SQLite files for object and metadata storage. Unlike `rados`, dbstore is **stateful** — every RGW instance must see the same files.

**何时使用：** Isolate dbstore data on a dedicated filesystem. cephadm cannot freely move daemons without the data.

**示例：**

```bash
ceph config set client.rgw dbstore_db_dir "/var/lib/ceph/radosgw"
ceph config get client.rgw dbstore_db_dir
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`/var/lib/ceph/radosgw`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw dbstore_db_dir)
iostat -x 5  # disk saturation
```

---

### dbstore_db_name_prefix

| | |
|---|---|
| 类型 | Str · default `dbstore` · **Advanced** |
| 表格 | [rgw.md#SP_dbstore_db_name_prefix](../../../config/rgw/rgw.md#SP_dbstore_db_name_prefix) |

**作用：** prefix to the file names created by db backend store

**何时使用：** Multiple dbstore instances or tenants on one host without filename collisions.

**示例：**

```bash
ceph config set client.rgw dbstore_db_name_prefix dbstore
ceph config get client.rgw dbstore_db_name_prefix
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `dbstore`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw dbstore_db_name_prefix
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_backend_store

| | |
|---|---|
| 类型 | Str · enum: ["rados", "dbstore", "motr", "daos", "posix"] · default `rados` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_backend_store](../../../config/rgw/rgw.md#SP_rgw_backend_store) |

**作用：** Selects the **Storage Abstraction Layer (SAL)** — where RGW stores objects and metadata.

| Value | Role |
|-------|------|
| `rados` | Production default — objects in RADOS pools |
| `dbstore` | Experimental standalone SQLite backend |
| `daos` | Experimental DAOS backend |
| `motr` | Experimental Motr backend |
| `posix` | Experimental POSIX filesystem backend |

**何时使用：** Leave `rados` in production. Other values are for development, testing, or specialized deployments.

**相关选项：**

- `daos_pool`, `dbstore_*`, `rgw_config_store`, `rgw_filter`

**示例：**

```bash
ceph config set client.rgw rgw_backend_store rados
ceph config get client.rgw rgw_backend_store
# Production: keep rados; PoC only: dbstore | daos | motr | posix
```

**寻找最优值：**

**调优模型：** Architecture

1. Production Ceph clusters: `rados` (default).
2. Other values (`dbstore`, `daos`, `motr`, `posix`) are experimental PoC only.
3. Changing backend requires migration — not an in-place performance tune.

---

### rgw_config_store

| | |
|---|---|
| 类型 | Str · enum: ["rados", "dbstore", "json"] · default `rados` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_config_store](../../../config/rgw/rgw.md#SP_rgw_config_store) |

**作用：** Configuration storage backend

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_config_store rados
ceph config get client.rgw rgw_config_store
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["rados", "dbstore", "json"].
2. Default `rados` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---


[← RGW 配置概览](../OVERVIEW.md)
