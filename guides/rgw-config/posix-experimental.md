# POSIX backend (experimental)

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_posix_base_path](#rgw_posix_base_path) | `/tmp/rgw_posix_driver` | Advanced |
| [rgw_posix_cache_lanes](#rgw_posix_cache_lanes) | `3` | Advanced |
| [rgw_posix_cache_lmdb_count](#rgw_posix_cache_lmdb_count) | `3` | Advanced |
| [rgw_posix_cache_max_buckets](#rgw_posix_cache_max_buckets) | `100` | Advanced |
| [rgw_posix_cache_partitions](#rgw_posix_cache_partitions) | `3` | Advanced |
| [rgw_posix_database_root](#rgw_posix_database_root) | `/var/lib/ceph/radosgw` | Advanced |
| [rgw_posix_userdb_dir](#rgw_posix_userdb_dir) | `/var/lib/ceph/radosgw` | Advanced |

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

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/tmp/rgw_posix_driver`) is fine when that path is on a separate volume.

---

### rgw_posix_cache_lanes

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_lanes](../../config/rgw/rgw.md#SP_rgw_posix_cache_lanes) |

**What it does:** experimental Number of lanes in cache LRU

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_lanes 3
ceph config get client.rgw rgw_posix_cache_lanes
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`3`) while watching RGW RSS.

---

### rgw_posix_cache_lmdb_count

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_lmdb_count](../../config/rgw/rgw.md#SP_rgw_posix_cache_lmdb_count) |

**What it does:** experimental Number of lmdb partitions in the ordered listing cache

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_lmdb_count 3
ceph config get client.rgw rgw_posix_cache_lmdb_count
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`3`) while watching RGW RSS.

---

### rgw_posix_cache_max_buckets

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_max_buckets](../../config/rgw/rgw.md#SP_rgw_posix_cache_max_buckets) |

**What it does:** experimental Number of buckets to maintain in the ordered listing cache

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_max_buckets 100
ceph config get client.rgw rgw_posix_cache_max_buckets
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`100`) while watching RGW RSS.

---

### rgw_posix_cache_partitions

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [rgw.md#SP_rgw_posix_cache_partitions](../../config/rgw/rgw.md#SP_rgw_posix_cache_partitions) |

**What it does:** experimental Number of partitions in cache AVL

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw rgw_posix_cache_partitions 3
ceph config get client.rgw rgw_posix_cache_partitions
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`3`) while watching RGW RSS.

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

**Finding optimal value:** Start from upstream default (`/var/lib/ceph/radosgw`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Place on fast, dedicated storage with sufficient free space. Default (`/var/lib/ceph/radosgw`) is fine when that path is on a separate volume.

---


[← RGW config overview](OVERVIEW.md)
