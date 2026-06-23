# Experimental backends

RGW config deep dive — 6 options. [← RGW config overview](OVERVIEW.md) · [Curated batch 1](../rgw-config-options.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### daos_pool

| | |
|---|---|
| Type | Str · default `tank` · **Advanced** |
| Table | [rgw.md#SP_daos_pool](../../config/rgw/rgw.md#SP_daos_pool) |

**What it does:** DAOS Pool to use

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw daos_pool tank
ceph config get client.rgw daos_pool
```

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
| Table | [rgw.md#SP_dbstore_config_uri](../../config/rgw/rgw.md#SP_dbstore_config_uri) |

**What it does:** Config database URI. URIs beginning with file: refer to local files opened with SQLite.

**When to use:** Set when integrating with an external service; leave empty if the feature is unused.

**Example:**

```bash
ceph config set client.rgw dbstore_config_uri "file:/var/lib/ceph/radosgw/dbstore-config.db"
ceph config get client.rgw dbstore_config_uri
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
| Table | [rgw.md#SP_dbstore_db_dir](../../config/rgw/rgw.md#SP_dbstore_db_dir) |

**What it does:** path for the directory for storing the db backend store data

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

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
| Table | [rgw.md#SP_dbstore_db_name_prefix](../../config/rgw/rgw.md#SP_dbstore_db_name_prefix) |

**What it does:** prefix to the file names created by db backend store

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_backend_store

| | |
|---|---|
| Type | Str · default `rados` · **Advanced** |
| Table | [rgw.md#SP_rgw_backend_store](../../config/rgw/rgw.md#SP_rgw_backend_store) |

**What it does:** experimental Option to set backend store type

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_backend_store rados
ceph config get client.rgw rgw_backend_store
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
| Type | Str · default `rados` · **Advanced** |
| Table | [rgw.md#SP_rgw_config_store](../../config/rgw/rgw.md#SP_rgw_config_store) |

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


[← RGW config overview](OVERVIEW.md)
