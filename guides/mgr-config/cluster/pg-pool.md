# PG & pool settings

MGR config deep dive — 11 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_pg_check_down_all_threshold](#mon_pg_check_down_all_threshold) | `0.5` | Advanced | Performance |
| [mon_pg_stuck_threshold](#mon_pg_stuck_threshold) | `1_min` | Advanced | Performance |
| [mon_pg_warn_max_object_skew](#mon_pg_warn_max_object_skew) | `10` | Advanced | Performance |
| [mon_pg_warn_min_objects](#mon_pg_warn_min_objects) | `10000` | Advanced | Performance |
| [mon_pg_warn_min_per_osd](#mon_pg_warn_min_per_osd) | `0` | Advanced | Performance |
| [mon_pg_warn_min_pool_objects](#mon_pg_warn_min_pool_objects) | `1000` | Advanced | Performance |
| [mon_pool_quota_crit_threshold](#mon_pool_quota_crit_threshold) | `0` | Advanced | Performance |
| [mon_pool_quota_warn_threshold](#mon_pool_quota_warn_threshold) | `0` | Advanced | Performance |
| [mon_target_pg_per_osd](#mon_target_pg_per_osd) | `200` | Advanced | Performance |
| [mon_warn_on_pool_no_app](#mon_warn_on_pool_no_app) | `True` | Dev | Dev |
| [mon_warn_on_pool_no_app_grace](#mon_warn_on_pool_no_app_grace) | `5_min` | Dev | Dev |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_pg_check_down_all_threshold

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [mon.md#SP_mon_pg_check_down_all_threshold](../../../config/mgr/mon.md#SP_mon_pg_check_down_all_threshold) |

**What it does:** threshold of down osds after which we check all pgs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_pg_check_down_all_threshold 0.5
ceph config get mon mon_pg_check_down_all_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_check_down_all_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_stuck_threshold

| | |
|---|---|
| Type | Int · default `1_min` · **Advanced** |
| Table | [mon.md#SP_mon_pg_stuck_threshold](../../../config/mgr/mon.md#SP_mon_pg_stuck_threshold) |

**What it does:** number of seconds after which pgs can be considered stuck inactive, unclean, etc

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_pg_stuck_threshold 1_min
ceph config get mon mon_pg_stuck_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_stuck_threshold
ceph -s
ceph mon stat
```

---

### mon_pg_warn_max_object_skew

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_pg_warn_max_object_skew](../../../config/mgr/mon.md#SP_mon_pg_warn_max_object_skew) |

**What it does:** max skew few average in objects per pg

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_pg_warn_max_object_skew 10
ceph config get mon mon_pg_warn_max_object_skew
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_warn_max_object_skew
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_objects

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [mon.md#SP_mon_pg_warn_min_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_objects) |

**What it does:** do not warn below this object #

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_pg_warn_min_objects 10000
ceph config get mon mon_pg_warn_min_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_warn_min_objects
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_per_osd

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_pg_warn_min_per_osd](../../../config/mgr/mon.md#SP_mon_pg_warn_min_per_osd) |

**What it does:** minimal number PGs per (in) osd before we warn the admin

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_pg_warn_min_per_osd 64
ceph config get mon mon_pg_warn_min_per_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_warn_min_per_osd
ceph -s
ceph mon stat
```

---

### mon_pg_warn_min_pool_objects

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [mon.md#SP_mon_pg_warn_min_pool_objects](../../../config/mgr/mon.md#SP_mon_pg_warn_min_pool_objects) |

**What it does:** do not warn on pools below this object #

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_pg_warn_min_pool_objects 1000
ceph config get mon mon_pg_warn_min_pool_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pg_warn_min_pool_objects
ceph -s
ceph mon stat
```

---

### mon_pool_quota_crit_threshold

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_pool_quota_crit_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_crit_threshold) |

**What it does:** percent of quota at which to issue errors

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_pool_quota_crit_threshold 64
ceph config get mon mon_pool_quota_crit_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pool_quota_crit_threshold
ceph -s
ceph mon stat
```

---

### mon_pool_quota_warn_threshold

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_pool_quota_warn_threshold](../../../config/mgr/mon.md#SP_mon_pool_quota_warn_threshold) |

**What it does:** percent of quota at which to issue warnings

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_pool_quota_warn_threshold 64
ceph config get mon mon_pool_quota_warn_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_pool_quota_warn_threshold
ceph -s
ceph mon stat
```

---

### mon_target_pg_per_osd

| | |
|---|---|
| Type | Uint · default `200` · **Advanced** |
| Table | [mon.md#SP_mon_target_pg_per_osd](../../../config/mgr/mon.md#SP_mon_target_pg_per_osd) |

**What it does:** Target number of PG replicas per OSD

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_target_pg_per_osd 200
ceph config get mon mon_target_pg_per_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_target_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_app

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mon.md#SP_mon_warn_on_pool_no_app](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app) |

**What it does:** issue POOL_APP_NOT_ENABLED health warning if pool has not application enabled

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_warn_on_pool_no_app false
ceph config get mon mon_warn_on_pool_no_app
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_warn_on_pool_no_app_grace

| | |
|---|---|
| Type | Secs · default `5_min` · **Dev** |
| Table | [mon.md#SP_mon_warn_on_pool_no_app_grace](../../../config/mgr/mon.md#SP_mon_warn_on_pool_no_app_grace) |

**What it does:** time after which POOL_APP_NOT_ENABLED health warning is issued

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_warn_on_pool_no_app_grace 5_min
ceph config get mon mon_warn_on_pool_no_app_grace
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5_min`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
