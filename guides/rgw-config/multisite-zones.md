# Multisite zones and realm

RGW config deep dive — 15 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_period_latest_epoch_info_oid](#rgw_period_latest_epoch_info_oid) | `.latest_epoch` | Dev |
| [rgw_period_push_interval](#rgw_period_push_interval) | `2` | Advanced |
| [rgw_period_push_interval_max](#rgw_period_push_interval_max) | `30` | Advanced |
| [rgw_period_root_pool](#rgw_period_root_pool) | `.rgw.root` | Advanced |
| [rgw_realm](#rgw_realm) | `(empty)` | Advanced |
| [rgw_realm_id](#rgw_realm_id) | `(empty)` | Advanced |
| [rgw_realm_root_pool](#rgw_realm_root_pool) | `.rgw.root` | Advanced |
| [rgw_region](#rgw_region) | `(empty)` | Advanced |
| [rgw_region_root_pool](#rgw_region_root_pool) | `.rgw.root` | Advanced |
| [rgw_zone](#rgw_zone) | `(empty)` | Advanced |
| [rgw_zone_id](#rgw_zone_id) | `(empty)` | Advanced |
| [rgw_zone_root_pool](#rgw_zone_root_pool) | `.rgw.root` | Advanced |
| [rgw_zonegroup](#rgw_zonegroup) | `(empty)` | Advanced |
| [rgw_zonegroup_id](#rgw_zonegroup_id) | `(empty)` | Advanced |
| [rgw_zonegroup_root_pool](#rgw_zonegroup_root_pool) | `.rgw.root` | Advanced |

---

### rgw_period_latest_epoch_info_oid

| | |
|---|---|
| Type | Str · default `.latest_epoch` · **Dev** |
| Table | [rgw.md#SP_rgw_period_latest_epoch_info_oid](../../config/rgw/rgw.md#SP_rgw_period_latest_epoch_info_oid) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_period_latest_epoch_info_oid .latest_epoch
ceph config get client.rgw rgw_period_latest_epoch_info_oid
```

**Finding optimal value:** Keep the upstream default (`.latest_epoch`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_period_push_interval

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [rgw.md#SP_rgw_period_push_interval](../../config/rgw/rgw.md#SP_rgw_period_push_interval) |

**What it does:** Period push interval

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_period_push_interval 2
ceph config get client.rgw rgw_period_push_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`2`) only when logs show sync, cache, or timeout issues.

---

### rgw_period_push_interval_max

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [rgw.md#SP_rgw_period_push_interval_max](../../config/rgw/rgw.md#SP_rgw_period_push_interval_max) |

**What it does:** Period push maximum interval

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_period_push_interval_max 30
ceph config get client.rgw rgw_period_push_interval_max
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`30`) only when logs show sync, cache, or timeout issues.

---

### rgw_period_root_pool

| | |
|---|---|
| Type | Str · default `.rgw.root` · **Advanced** |
| Table | [rgw.md#SP_rgw_period_root_pool](../../config/rgw/rgw.md#SP_rgw_period_root_pool) |

**What it does:** Period root pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_period_root_pool .rgw.root
ceph config get client.rgw rgw_period_root_pool
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`.rgw.root`) only when logs show sync, cache, or timeout issues.

---

### rgw_realm

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_realm](../../config/rgw/rgw.md#SP_rgw_realm) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_realm <value>
ceph config get client.rgw rgw_realm
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_realm_id

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_realm_id](../../config/rgw/rgw.md#SP_rgw_realm_id) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_realm_id <value>
ceph config get client.rgw rgw_realm_id
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_realm_root_pool

| | |
|---|---|
| Type | Str · default `.rgw.root` · **Advanced** |
| Table | [rgw.md#SP_rgw_realm_root_pool](../../config/rgw/rgw.md#SP_rgw_realm_root_pool) |

**What it does:** Realm root pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_realm_root_pool .rgw.root
ceph config get client.rgw rgw_realm_root_pool
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `.rgw.root`.

---

### rgw_region

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_region](../../config/rgw/rgw.md#SP_rgw_region) |

**What it does:** Region name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_region <value>
ceph config get client.rgw rgw_region
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_region_root_pool

| | |
|---|---|
| Type | Str · default `.rgw.root` · **Advanced** |
| Table | [rgw.md#SP_rgw_region_root_pool](../../config/rgw/rgw.md#SP_rgw_region_root_pool) |

**What it does:** Region root pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_region_root_pool .rgw.root
ceph config get client.rgw rgw_region_root_pool
```

**Finding optimal value:** Start from upstream default (`.rgw.root`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_zone

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_zone](../../config/rgw/rgw.md#SP_rgw_zone) |

**What it does:** Zone name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zone <value>
ceph config get client.rgw rgw_zone
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_zone_id

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_zone_id](../../config/rgw/rgw.md#SP_rgw_zone_id) |

**What it does:** Zone ID

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zone_id <value>
ceph config get client.rgw rgw_zone_id
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_zone_root_pool

| | |
|---|---|
| Type | Str · default `.rgw.root` · **Advanced** |
| Table | [rgw.md#SP_rgw_zone_root_pool](../../config/rgw/rgw.md#SP_rgw_zone_root_pool) |

**What it does:** Zone root pool name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zone_root_pool .rgw.root
ceph config get client.rgw rgw_zone_root_pool
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `.rgw.root`.

---

### rgw_zonegroup

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_zonegroup](../../config/rgw/rgw.md#SP_rgw_zonegroup) |

**What it does:** Zonegroup name

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zonegroup <value>
ceph config get client.rgw rgw_zonegroup
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_zonegroup_id

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_zonegroup_id](../../config/rgw/rgw.md#SP_rgw_zonegroup_id) |

**What it does:** Zonegroup ID

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zonegroup_id <value>
ceph config get client.rgw rgw_zonegroup_id
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `(empty)`.

---

### rgw_zonegroup_root_pool

| | |
|---|---|
| Type | Str · default `.rgw.root` · **Advanced** |
| Table | [rgw.md#SP_rgw_zonegroup_root_pool](../../config/rgw/rgw.md#SP_rgw_zonegroup_root_pool) |

**What it does:** Zonegroup root pool

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_zonegroup_root_pool .rgw.root
ceph config get client.rgw rgw_zonegroup_root_pool
```

**Finding optimal value:** Set by `radosgw-admin realm/zone` workflows — not hand-tuned numerically. Must match multisite period configuration; default OID/name: `.rgw.root`.

---


[← RGW config overview](OVERVIEW.md)
