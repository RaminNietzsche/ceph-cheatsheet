# Multisite zones and realm

RGW config deep dive — 15 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_period_latest_epoch_info_oid](#rgw_period_latest_epoch_info_oid) | `.latest_epoch` | Dev | Performance |
| [rgw_period_push_interval](#rgw_period_push_interval) | `2` | Advanced | Performance |
| [rgw_period_push_interval_max](#rgw_period_push_interval_max) | `30` | Advanced | Performance |
| [rgw_period_root_pool](#rgw_period_root_pool) | `.rgw.root` | Advanced | Performance |
| [rgw_realm](#rgw_realm) | `(empty)` | Advanced | Architecture |
| [rgw_realm_id](#rgw_realm_id) | `(empty)` | Advanced | Architecture |
| [rgw_realm_root_pool](#rgw_realm_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_region](#rgw_region) | `(empty)` | Advanced | Architecture |
| [rgw_region_root_pool](#rgw_region_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zone](#rgw_zone) | `(empty)` | Advanced | Architecture |
| [rgw_zone_id](#rgw_zone_id) | `(empty)` | Advanced | Architecture |
| [rgw_zone_root_pool](#rgw_zone_root_pool) | `.rgw.root` | Advanced | Architecture |
| [rgw_zonegroup](#rgw_zonegroup) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_id](#rgw_zonegroup_id) | `(empty)` | Advanced | Architecture |
| [rgw_zonegroup_root_pool](#rgw_zonegroup_root_pool) | `.rgw.root` | Advanced | Architecture |

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

**Finding optimal value:**

**Tuning model:** Performance

1. Default `.latest_epoch` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_latest_epoch_info_oid
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [rgw.md#SP_rgw_period_push_interval](../../config/rgw/rgw.md#SP_rgw_period_push_interval) |

**What it does:** Period push interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_period_push_interval 2
ceph config get client.rgw rgw_period_push_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `2` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_period_push_interval_max

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [rgw.md#SP_rgw_period_push_interval_max](../../config/rgw/rgw.md#SP_rgw_period_push_interval_max) |

**What it does:** Period push maximum interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_period_push_interval_max 30
ceph config get client.rgw rgw_period_push_interval_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_push_interval_max
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Performance

1. Default `.rgw.root` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_period_root_pool
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`(empty)` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

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

**Finding optimal value:**

**Tuning model:** Architecture

1. Set via `radosgw-admin realm/zone/period` — do not hand-edit for tuning.
2. Value must match the active period object (`.rgw.root` is the default OID/name).
3. Multisite: keep consistent across all zones in the same realm.

```bash
radosgw-admin realm list
radosgw-admin zone get --rgw-zone=<zone>
```

---


[← RGW config overview](OVERVIEW.md)
