# Caches and TTL

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_obj_tombstone_cache_size](#rgw_obj_tombstone_cache_size) | `1000` | Advanced | Performance |
| [rgw_user_counters_cache](#rgw_user_counters_cache) | `False` | Dev | Performance |
| [rgw_user_counters_cache_size](#rgw_user_counters_cache_size) | `10000` | Advanced | Performance |

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

### rgw_obj_tombstone_cache_size

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_obj_tombstone_cache_size](../../config/rgw/rgw.md#SP_rgw_obj_tombstone_cache_size) |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_user_counters_cache

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_user_counters_cache](../../config/rgw/rgw.md#SP_rgw_user_counters_cache) |

**What it does:** enable a rgw perf counters cache for counters with user label

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_user_counters_cache False
ceph config get client.rgw rgw_user_counters_cache
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_user_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_counters_cache_size](../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size) |

**What it does:** Number of labeled perf counters the user perf counters cache can store

**When to use:**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**Example:**

```bash
ceph config set client.rgw rgw_user_counters_cache_size 10000
ceph config get client.rgw rgw_user_counters_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**Signals:** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_user_counters_cache_size
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
