# Experimental backends

RGW config deep dive — 6 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [daos_pool](#daos_pool) | `tank` | Advanced | Capacity |
| [dbstore_config_uri](#dbstore_config_uri) | `file:/var/lib/ceph/radosgw/dbstore-config.db` | Advanced | Capacity |
| [dbstore_db_dir](#dbstore_db_dir) | `/var/lib/ceph/radosgw` | Advanced | Capacity |
| [dbstore_db_name_prefix](#dbstore_db_name_prefix) | `dbstore` | Advanced | Performance |
| [rgw_backend_store](#rgw_backend_store) | `rados` | Advanced | Architecture |
| [rgw_config_store](#rgw_config_store) | `rados` | Advanced | Architecture |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

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
| Type | Str · default `tank` · **Advanced** |
| Table | [rgw.md#SP_daos_pool](../../../config/rgw/rgw.md#SP_daos_pool) |

**What it does:** Name of the [DAOS](https://docs.daos.io/) pool RGW connects to when `rgw_backend_store = daos`.

**When to use:** Experimental DAOS-backed RGW (build with `-DWITH_RADOSGW_DAOS=ON`). Not used in standard Ceph clusters on RADOS.

**Example:**

```ini
[client.rgw]
rgw backend store = daos
daos pool = mypool
```

Provision the DAOS pool with your site DAOS admin tools before setting this option.

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Str · default `file:/var/lib/ceph/radosgw/dbstore-config.db` · **Advanced** |
| Table | [rgw.md#SP_dbstore_config_uri](../../../config/rgw/rgw.md#SP_dbstore_config_uri) |

**What it does:** URI for the **configuration database** when using the experimental **dbstore** backend. URIs starting with `file:` point at a local SQLite file.

**When to use:** Standalone RGW without MON/OSD. See [dbstore README](https://github.com/ceph/ceph/blob/main/src/rgw/driver/dbstore/README.md).

**Related options:**

- `rgw_backend_store` = `dbstore`
- `rgw_config_store` = `dbstore`
- `dbstore_db_dir`, `dbstore_db_name_prefix`

**Example:**

```bash
ceph config set client.rgw rgw_backend_store dbstore
ceph config set client.rgw rgw_config_store dbstore
ceph config set client.rgw dbstore_config_uri file:/var/lib/ceph/radosgw/dbstore-config.db
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| Table | [rgw.md#SP_dbstore_db_dir](../../../config/rgw/rgw.md#SP_dbstore_db_dir) |

**What it does:** Directory where dbstore writes SQLite files for object and metadata storage. Unlike `rados`, dbstore is **stateful** — every RGW instance must see the same files.

**When to use:** Isolate dbstore data on a dedicated filesystem. cephadm cannot freely move daemons without the data.

**Example:**

```bash
ceph config set client.rgw dbstore_db_dir "/var/lib/ceph/radosgw"
ceph config get client.rgw dbstore_db_dir
```

**Finding optimal value:**

**Tuning model:** Capacity

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
| Type | Str · default `dbstore` · **Advanced** |
| Table | [rgw.md#SP_dbstore_db_name_prefix](../../../config/rgw/rgw.md#SP_dbstore_db_name_prefix) |

**What it does:** prefix to the file names created by db backend store

**When to use:** Multiple dbstore instances or tenants on one host without filename collisions.

**Example:**

```bash
ceph config set client.rgw dbstore_db_name_prefix dbstore
ceph config get client.rgw dbstore_db_name_prefix
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `dbstore`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| Type | Str · enum: ["rados", "dbstore", "motr", "daos", "posix"] · default `rados` · **Advanced** |
| Table | [rgw.md#SP_rgw_backend_store](../../../config/rgw/rgw.md#SP_rgw_backend_store) |

**What it does:** Selects the **Storage Abstraction Layer (SAL)** — where RGW stores objects and metadata.

| Value | Role |
|-------|------|
| `rados` | Production default — objects in RADOS pools |
| `dbstore` | Experimental standalone SQLite backend |
| `daos` | Experimental DAOS backend |
| `motr` | Experimental Motr backend |
| `posix` | Experimental POSIX filesystem backend |

**When to use:** Leave `rados` in production. Other values are for development, testing, or specialized deployments.

**Related options:**

- `daos_pool`, `dbstore_*`, `rgw_config_store`, `rgw_filter`

**Example:**

```bash
ceph config set client.rgw rgw_backend_store rados
ceph config get client.rgw rgw_backend_store
# Production: keep rados; PoC only: dbstore | daos | motr | posix
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Production Ceph clusters: `rados` (default).
2. Other values (`dbstore`, `daos`, `motr`, `posix`) are experimental PoC only.
3. Changing backend requires migration — not an in-place performance tune.

---

### rgw_config_store

| | |
|---|---|
| Type | Str · enum: ["rados", "dbstore", "json"] · default `rados` · **Advanced** |
| Table | [rgw.md#SP_rgw_config_store](../../../config/rgw/rgw.md#SP_rgw_config_store) |

**What it does:** Configuration storage backend

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_config_store rados
ceph config get client.rgw rgw_config_store
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["rados", "dbstore", "json"].
2. Default `rados` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---


[← RGW config overview](../OVERVIEW.md)
