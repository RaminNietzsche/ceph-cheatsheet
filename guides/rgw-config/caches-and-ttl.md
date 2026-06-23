# Caches and TTL

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_obj_tombstone_cache_size](#rgw_obj_tombstone_cache_size) | `1000` | Advanced |
| [rgw_user_counters_cache](#rgw_user_counters_cache) | `False` | Dev |
| [rgw_user_counters_cache_size](#rgw_user_counters_cache_size) | `10000` | Advanced |

---

### rgw_obj_tombstone_cache_size

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_obj_tombstone_cache_size](../../config/rgw/rgw.md#SP_rgw_obj_tombstone_cache_size) |

**What it does:** Max number of entries to keep in tombstone cache

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_obj_tombstone_cache_size 1000
ceph config get client.rgw rgw_obj_tombstone_cache_size
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`1000`) while watching RGW RSS.

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

**Finding optimal value:** Keep the upstream default (`False`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_user_counters_cache_size

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_user_counters_cache_size](../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size) |

**What it does:** Number of labeled perf counters the user perf counters cache can store

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_user_counters_cache_size 10000
ceph config get client.rgw rgw_user_counters_cache_size
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`10000`) while watching RGW RSS.

---


[← RGW config overview](OVERVIEW.md)
