# MGR-related settings

MON config deep dive — 6 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_mgr_beacon_grace](#mon_mgr_beacon_grace) | `30` | Advanced | Performance |
| [mon_mgr_blocklist_interval](#mon_mgr_blocklist_interval) | `1_day` | Dev | Dev |
| [mon_mgr_digest_period](#mon_mgr_digest_period) | `5` | Dev | Dev |
| [mon_mgr_inactive_grace](#mon_mgr_inactive_grace) | `1_min` | Advanced | Performance |
| [mon_mgr_mkfs_grace](#mon_mgr_mkfs_grace) | `2_min` | Advanced | Performance |
| [mon_mgr_proxy_client_bytes_ratio](#mon_mgr_proxy_client_bytes_ratio) | `0.3` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_mgr_beacon_grace

| | |
|---|---|
| Type | Secs · default `30` · **Advanced** |
| Table | [mon.md#SP_mon_mgr_beacon_grace](../../../config/mon/mon.md#SP_mon_mgr_beacon_grace) |

**What it does:** Period in seconds from last beacon to monitor marking a manager daemon as failed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_mgr_beacon_grace 30
ceph config get mon mon_mgr_beacon_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_mgr_beacon_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_blocklist_interval

| | |
|---|---|
| Type | Float · default `1_day` · **Dev** |
| Table | [mon.md#SP_mon_mgr_blocklist_interval](../../../config/mon/mon.md#SP_mon_mgr_blocklist_interval) |

**What it does:** Duration in seconds that blocklist entries for mgr daemons remain in the OSD map

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_mgr_blocklist_interval 1_day
ceph config get mon mon_mgr_blocklist_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_day`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_mgr_digest_period

| | |
|---|---|
| Type | Int · default `5` · **Dev** |
| Table | [mon.md#SP_mon_mgr_digest_period](../../../config/mon/mon.md#SP_mon_mgr_digest_period) |

**What it does:** Period in seconds between monitor-to-manager health/status updates

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_mgr_digest_period 5
ceph config get mon mon_mgr_digest_period
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_mgr_inactive_grace

| | |
|---|---|
| Type | Int · default `1_min` · **Advanced** |
| Table | [mon.md#SP_mon_mgr_inactive_grace](../../../config/mon/mon.md#SP_mon_mgr_inactive_grace) |

**What it does:** Period in seconds after cluster creation during which cluster may have no active manager

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_mgr_inactive_grace 1_min
ceph config get mon mon_mgr_inactive_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_mgr_inactive_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_mkfs_grace

| | |
|---|---|
| Type | Int · default `2_min` · **Advanced** |
| Table | [mon.md#SP_mon_mgr_mkfs_grace](../../../config/mon/mon.md#SP_mon_mgr_mkfs_grace) |

**What it does:** Period in seconds that the cluster may have no active manager before this is reported as an ERR rather than a WARN

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_mgr_mkfs_grace 2_min
ceph config get mon mon_mgr_mkfs_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_mgr_mkfs_grace
ceph -s
ceph mon stat
```

---

### mon_mgr_proxy_client_bytes_ratio

| | |
|---|---|
| Type | Float · default `0.3` · **Dev** |
| Table | [mon.md#SP_mon_mgr_proxy_client_bytes_ratio](../../../config/mon/mon.md#SP_mon_mgr_proxy_client_bytes_ratio) |

**What it does:** ratio of mon_client_bytes that can be consumed by proxied mgr commands before we error out to client

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_mgr_proxy_client_bytes_ratio 0.3
ceph config get mon mon_mgr_proxy_client_bytes_ratio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.3`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
