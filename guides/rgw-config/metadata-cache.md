# RGW metadata cache

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_cache_enabled](#rgw_cache_enabled) | `True` | Advanced |
| [rgw_cache_expiry_interval](#rgw_cache_expiry_interval) | `900` | Advanced |
| [rgw_cache_lru_size](#rgw_cache_lru_size) | `25000` | Advanced |

---

### rgw_cache_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_enabled](../../config/rgw/rgw.md#SP_rgw_cache_enabled) |

**What it does:** Enable RGW metadata cache.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_cache_enabled True
ceph config get client.rgw rgw_cache_enabled
```

**Finding optimal value:** Enable only when the related metrics or correctness path needs it. Default (`True`) is usually optimal for standard deployments.

---

### rgw_cache_expiry_interval

| | |
|---|---|
| Type | Uint · default `900` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_expiry_interval](../../config/rgw/rgw.md#SP_rgw_cache_expiry_interval) |

**What it does:** Number of seconds before entries in the cache are assumed stale and re-fetched. Zero is never.

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_cache_expiry_interval 900
ceph config get client.rgw rgw_cache_expiry_interval
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`900`) while watching RGW RSS.

---

### rgw_cache_lru_size

| | |
|---|---|
| Type | Int · default `25000` · **Advanced** |
| Table | [rgw.md#SP_rgw_cache_lru_size](../../config/rgw/rgw.md#SP_rgw_cache_lru_size) |

**What it does:** Max number of items in RGW metadata cache.

**When to use:** Tune when metadata/quota/token caching affects correctness lag or RGW memory pressure.

**Example:**

```bash
ceph config set client.rgw rgw_cache_lru_size 25000
ceph config get client.rgw rgw_cache_lru_size
```

**Finding optimal value:** Size to active working set (accounts, buckets, or keys you monitor). Sweep around default (`25000`) while watching RGW RSS.

---


[← RGW config overview](OVERVIEW.md)
