# Metadata & object caches

RGW config deep dive — 4 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_cache_enabled](#rgw_cache_enabled) | `True` | Advanced | Performance |
| [rgw_cache_expiry_interval](#rgw_cache_expiry_interval) | `900` | Advanced | Performance |
| [rgw_cache_lru_size](#rgw_cache_lru_size) | `25000` | Advanced | Performance |
| [rgw_obj_tombstone_cache_size](#rgw_obj_tombstone_cache_size) | `1000` | Advanced | Performance |

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

### rgw_cache_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_enabled](../../../config/rgw/rgw.md#SP_rgw_cache_enabled) |

**What it does:** Enable RGW metadata cache.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_cache_enabled false
ceph config get client.rgw rgw_cache_enabled
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `True` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_cache_expiry_interval

| | |
|---|---|
| Type | Uint · default `900` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_expiry_interval](../../../config/rgw/rgw.md#SP_rgw_cache_expiry_interval) |

**What it does:** Number of seconds before entries in the cache are assumed stale and re-fetched. Zero is never.

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_cache_expiry_interval 900
ceph config get client.rgw rgw_cache_expiry_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `900`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

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
| Type | Int · default `25000` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_lru_size](../../../config/rgw/rgw.md#SP_rgw_cache_lru_size) |

**What it does:** Max number of items in RGW metadata cache.

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_cache_lru_size 25000
ceph config get client.rgw rgw_cache_lru_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `25000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

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
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_obj_tombstone_cache_size](../../../config/rgw/rgw.md#SP_rgw_obj_tombstone_cache_size) |

**What it does:** Max number of entries to keep in tombstone cache

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_obj_tombstone_cache_size 1000
ceph config get client.rgw rgw_obj_tombstone_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `1000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_obj_tombstone_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
