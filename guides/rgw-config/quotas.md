# Quota sync and defaults

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_enable_quota_threads](#rgw_enable_quota_threads) | `True` | Advanced |
| [rgw_user_default_quota_max_objects](#rgw_user_default_quota_max_objects) | `-1` | Basic |
| [rgw_user_default_quota_max_size](#rgw_user_default_quota_max_size) | `-1` | Basic |

---

### rgw_enable_quota_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_quota_threads](../../config/rgw/rgw.md#SP_rgw_enable_quota_threads) |

**What it does:** Enables the quota maintenance thread.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_quota_threads True
ceph config get client.rgw rgw_enable_quota_threads
```

**Finding optimal value:** Enable when the feature is required; otherwise keep default (`True`) to minimize background threads and memory.

---

### rgw_user_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_user_default_quota_max_objects](../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_objects) |

**What it does:** User quota max objects

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
ceph config set client.rgw rgw_user_default_quota_max_objects -1
ceph config get client.rgw rgw_user_default_quota_max_objects
```

**Finding optimal value:** Derive from product tiers and cluster capacity (leave 20–30% headroom). `-1` means unlimited. Verify with test users via `radosgw-admin quota get`.

---

### rgw_user_default_quota_max_size

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_user_default_quota_max_size](../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_size) |

**What it does:** User quota max size

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
ceph config set client.rgw rgw_user_default_quota_max_size -1
ceph config get client.rgw rgw_user_default_quota_max_size
```

**Finding optimal value:** Derive from product tiers and cluster capacity (leave 20–30% headroom). `-1` means unlimited. Verify with test users via `radosgw-admin quota get`.

---


[← RGW config overview](OVERVIEW.md)
