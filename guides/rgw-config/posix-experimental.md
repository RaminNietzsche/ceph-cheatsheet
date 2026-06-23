# POSIX backend (experimental)

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_posix_base_path](#rgw_posix_base_path) | `/tmp/rgw_posix_driver` | Advanced | Architecture |
| [rgw_posix_cache_lanes](#rgw_posix_cache_lanes) | `3` | Advanced | Architecture |
| [rgw_posix_cache_lmdb_count](#rgw_posix_cache_lmdb_count) | `3` | Advanced | Architecture |
| [rgw_posix_cache_max_buckets](#rgw_posix_cache_max_buckets) | `100` | Advanced | Architecture |
| [rgw_posix_cache_partitions](#rgw_posix_cache_partitions) | `3` | Advanced | Architecture |
| [rgw_posix_database_root](#rgw_posix_database_root) | `/var/lib/ceph/radosgw` | Advanced | Architecture |
| [rgw_posix_userdb_dir](#rgw_posix_userdb_dir) | `/var/lib/ceph/radosgw` | Advanced | Architecture |

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

### rgw_posix_base_path

| | |
|---|---|
| Type | Str · default `/tmp/rgw_posix_driver` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_base_path](../../config/rgw/rgw.md#SP_rgw_posix_base_path) |

**What it does:** experimental Option to set base path for POSIX Driver

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_base_path "/tmp/rgw_posix_driver"
ceph config get client.rgw rgw_posix_base_path
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/tmp/rgw_posix_driver` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lanes

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_lanes](../../config/rgw/rgw.md#SP_rgw_posix_cache_lanes) |

**What it does:** experimental Number of lanes in cache LRU

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_lanes 3
ceph config get client.rgw rgw_posix_cache_lanes
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_lmdb_count

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_lmdb_count](../../config/rgw/rgw.md#SP_rgw_posix_cache_lmdb_count) |

**What it does:** experimental Number of lmdb partitions in the ordered listing cache

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_lmdb_count 3
ceph config get client.rgw rgw_posix_cache_lmdb_count
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_max_buckets

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_max_buckets](../../config/rgw/rgw.md#SP_rgw_posix_cache_max_buckets) |

**What it does:** experimental Number of buckets to maintain in the ordered listing cache

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_max_buckets 100
ceph config get client.rgw rgw_posix_cache_max_buckets
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `100` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_cache_partitions

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_partitions](../../config/rgw/rgw.md#SP_rgw_posix_cache_partitions) |

**What it does:** experimental Number of partitions in cache AVL

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_partitions 3
ceph config get client.rgw rgw_posix_cache_partitions
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `3` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_database_root

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_database_root](../../config/rgw/rgw.md#SP_rgw_posix_database_root) |

**What it does:** experimental Path to parent of POSIX Driver LMDB bucket listing cache

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_database_root "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_database_root
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### rgw_posix_userdb_dir

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/radosgw` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_userdb_dir](../../config/rgw/rgw.md#SP_rgw_posix_userdb_dir) |

**What it does:** path for the directory for storing the User db

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_userdb_dir "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_posix_userdb_dir
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `/var/lib/ceph/radosgw` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---


[← RGW config overview](OVERVIEW.md)
