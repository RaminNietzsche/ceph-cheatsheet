# RBD mirror

RBD mirror config deep dive — 24 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rbd-mirror/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rbd_mirror_concurrent_image_deletions](#rbd_mirror_concurrent_image_deletions) | `1` | Advanced | Performance |
| [rbd_mirror_concurrent_image_syncs](#rbd_mirror_concurrent_image_syncs) | `5` | Advanced | Performance |
| [rbd_mirror_delete_retry_interval](#rbd_mirror_delete_retry_interval) | `30` | Advanced | Performance |
| [rbd_mirror_image_perf_stats_prio](#rbd_mirror_image_perf_stats_prio) | `5` | Advanced | Performance |
| [rbd_mirror_image_policy_migration_throttle](#rbd_mirror_image_policy_migration_throttle) | `300` | Advanced | Performance |
| [rbd_mirror_image_policy_rebalance_timeout](#rbd_mirror_image_policy_rebalance_timeout) | `0` | Advanced | Performance |
| [rbd_mirror_image_policy_type](#rbd_mirror_image_policy_type) | `simple` | Advanced | Performance |
| [rbd_mirror_image_policy_update_throttle_interval](#rbd_mirror_image_policy_update_throttle_interval) | `1` | Advanced | Performance |
| [rbd_mirror_image_state_check_interval](#rbd_mirror_image_state_check_interval) | `30` | Advanced | Performance |
| [rbd_mirror_journal_commit_age](#rbd_mirror_journal_commit_age) | `5` | Advanced | Performance |
| [rbd_mirror_journal_poll_age](#rbd_mirror_journal_poll_age) | `5` | Advanced | Performance |
| [rbd_mirror_leader_heartbeat_interval](#rbd_mirror_leader_heartbeat_interval) | `5` | Advanced | Performance |
| [rbd_mirror_leader_max_acquire_attempts_before_break](#rbd_mirror_leader_max_acquire_attempts_before_break) | `3` | Advanced | Performance |
| [rbd_mirror_leader_max_missed_heartbeats](#rbd_mirror_leader_max_missed_heartbeats) | `2` | Advanced | Performance |
| [rbd_mirror_memory_autotune](#rbd_mirror_memory_autotune) | `True` | Dev | Dev |
| [rbd_mirror_memory_base](#rbd_mirror_memory_base) | `768_M` | Dev | Dev |
| [rbd_mirror_memory_cache_autotune_interval](#rbd_mirror_memory_cache_autotune_interval) | `30` | Dev | Dev |
| [rbd_mirror_memory_cache_min](#rbd_mirror_memory_cache_min) | `128_M` | Dev | Dev |
| [rbd_mirror_memory_cache_resize_interval](#rbd_mirror_memory_cache_resize_interval) | `5` | Dev | Dev |
| [rbd_mirror_memory_expected_fragmentation](#rbd_mirror_memory_expected_fragmentation) | `0.15` | Dev | Dev |
| [rbd_mirror_memory_target](#rbd_mirror_memory_target) | `4_G` | Basic | Policy |
| [rbd_mirror_perf_stats_prio](#rbd_mirror_perf_stats_prio) | `5` | Advanced | Performance |
| [rbd_mirror_pool_replayers_refresh_interval](#rbd_mirror_pool_replayers_refresh_interval) | `30` | Advanced | Performance |
| [rbd_mirror_sync_point_update_age](#rbd_mirror_sync_point_update_age) | `30` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. rbd-mirror
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_mirror_concurrent_image_deletions

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_concurrent_image_deletions](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_deletions) |

**What it does:** maximum number of image deletions in parallel

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_concurrent_image_deletions 1
ceph config get client rbd_mirror_concurrent_image_deletions
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_concurrent_image_deletions
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_concurrent_image_syncs

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_concurrent_image_syncs](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_concurrent_image_syncs) |

**What it does:** maximum number of image syncs in parallel

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_concurrent_image_syncs 5
ceph config get client rbd_mirror_concurrent_image_syncs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_concurrent_image_syncs
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_delete_retry_interval

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_delete_retry_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_delete_retry_interval) |

**What it does:** interval to check and retry the failed deletion requests

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_delete_retry_interval 30
ceph config get client rbd_mirror_delete_retry_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_delete_retry_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_perf_stats_prio

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_perf_stats_prio) |

**What it does:** Priority level for mirror daemon per-image replication perf counters

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_image_perf_stats_prio 5
ceph config get client rbd_mirror_image_perf_stats_prio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `11`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_perf_stats_prio
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_policy_migration_throttle

| | |
|---|---|
| Type | Uint · default `300` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_policy_migration_throttle](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_migration_throttle) |

**What it does:** number of seconds after which an image can be reshuffled (migrated) again

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_image_policy_migration_throttle 300
ceph config get client rbd_mirror_image_policy_migration_throttle
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `300`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_policy_migration_throttle
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_policy_rebalance_timeout

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_rebalance_timeout) |

**What it does:** number of seconds policy should be idle before triggering reshuffle (rebalance) of images

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_image_policy_rebalance_timeout 0
ceph config get client rbd_mirror_image_policy_rebalance_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_policy_rebalance_timeout
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_policy_type

| | |
|---|---|
| Type | Str · enum: ["none", "simple"] · default `simple` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_policy_type](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_type) |

**What it does:** active/active policy type for mapping images to instances

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_image_policy_type simple
ceph config get client rbd_mirror_image_policy_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `simple`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_policy_type
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_policy_update_throttle_interval

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_policy_update_throttle_interval) |

**What it does:** interval (in seconds) to throttle images for mirror daemon peer updates

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_image_policy_update_throttle_interval 1
ceph config get client rbd_mirror_image_policy_update_throttle_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_policy_update_throttle_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_image_state_check_interval

| | |
|---|---|
| Type | Uint · default `30` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_image_state_check_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_image_state_check_interval) |

**What it does:** interval to get images from pool watcher and set sources in replayer

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_image_state_check_interval 30
ceph config get client rbd_mirror_image_state_check_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_image_state_check_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_journal_commit_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_journal_commit_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_commit_age) |

**What it does:** commit time interval, seconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_journal_commit_age 5
ceph config get client rbd_mirror_journal_commit_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_journal_commit_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_journal_poll_age

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_journal_poll_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_journal_poll_age) |

**What it does:** maximum age (in seconds) between successive journal polls

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_journal_poll_age 5
ceph config get client rbd_mirror_journal_poll_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_journal_poll_age
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_leader_heartbeat_interval

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_leader_heartbeat_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_heartbeat_interval) |

**What it does:** interval (in seconds) between mirror leader heartbeats

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_leader_heartbeat_interval 5
ceph config get client rbd_mirror_leader_heartbeat_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_leader_heartbeat_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_leader_max_acquire_attempts_before_break

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_acquire_attempts_before_break) |

**What it does:** number of failed attempts to acquire lock after missing heartbeats before breaking lock

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_mirror_leader_max_acquire_attempts_before_break 3
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_leader_max_acquire_attempts_before_break
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_leader_max_missed_heartbeats

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_leader_max_missed_heartbeats) |

**What it does:** number of missed heartbeats for non-lock owner to attempt to acquire lock

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set client rbd_mirror_leader_max_missed_heartbeats 2
ceph config get client rbd_mirror_leader_max_missed_heartbeats
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_leader_max_missed_heartbeats
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_memory_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_autotune](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_autotune) |

**What it does:** Automatically tune the ratio of caches while respecting min values.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_autotune false
ceph config get client rbd_mirror_memory_autotune
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_base

| | |
|---|---|
| Type | Size · default `768_M` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_base](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_base) |

**What it does:** When tcmalloc and cache autotuning is enabled, estimate the minimum amount of memory in bytes the rbd-mirror daemon will need.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_base 768_M
ceph config get client rbd_mirror_memory_base
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`768_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_cache_autotune_interval

| | |
|---|---|
| Type | Float · default `30` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_cache_autotune_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_autotune_interval) |

**What it does:** The number of seconds to wait between rebalances when cache autotune is enabled.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_cache_autotune_interval 30
ceph config get client rbd_mirror_memory_cache_autotune_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`30`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_cache_min

| | |
|---|---|
| Type | Size · default `128_M` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_cache_min](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_min) |

**What it does:** When tcmalloc and cache autotuning is enabled, set the minimum amount of memory used for cache.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_cache_min 128_M
ceph config get client rbd_mirror_memory_cache_min
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_cache_resize_interval

| | |
|---|---|
| Type | Float · default `5` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_cache_resize_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_cache_resize_interval) |

**What it does:** When tcmalloc and cache autotuning is enabled, wait this many seconds between resizing caches.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_cache_resize_interval 5
ceph config get client rbd_mirror_memory_cache_resize_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_expected_fragmentation

| | |
|---|---|
| Type | Float · default `0.15` · **Dev** |
| Table | [rbd.md#SP_rbd_mirror_memory_expected_fragmentation](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_expected_fragmentation) |

**What it does:** When tcmalloc and cache autotuning is enabled, estimate the percent of memory fragmentation.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client rbd_mirror_memory_expected_fragmentation 0.15
ceph config get client rbd_mirror_memory_expected_fragmentation
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.15`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### rbd_mirror_memory_target

| | |
|---|---|
| Type | Size · default `4_G` · **Basic** |
| Table | [rbd.md#SP_rbd_mirror_memory_target](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_memory_target) |

**What it does:** When tcmalloc and cache autotuning is enabled, try to keep this many bytes mapped in memory.

**When to use:** Core RBD mirror behavior — review before changing in production.

**Example:**

```bash
ceph config set client rbd_mirror_memory_target 4_G
ceph config get client rbd_mirror_memory_target
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `4_G` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_memory_target
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_perf_stats_prio

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_perf_stats_prio](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_perf_stats_prio) |

**What it does:** Priority level for mirror daemon replication perf counters

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_perf_stats_prio 5
ceph config get client rbd_mirror_perf_stats_prio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `11`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_perf_stats_prio
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_pool_replayers_refresh_interval

| | |
|---|---|
| Type | Uint · default `30` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_pool_replayers_refresh_interval) |

**What it does:** interval to refresh peers in rbd-mirror daemon

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set client rbd_mirror_pool_replayers_refresh_interval 30
ceph config get client rbd_mirror_pool_replayers_refresh_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_pool_replayers_refresh_interval
ceph -s
# client options: set on client section or ceph.conf
```

---

### rbd_mirror_sync_point_update_age

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [rbd.md#SP_rbd_mirror_sync_point_update_age](../../../config/rbd-mirror/rbd.md#SP_rbd_mirror_sync_point_update_age) |

**What it does:** number of seconds between each update of the image sync point object number

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client rbd_mirror_sync_point_update_age 30
ceph config get client rbd_mirror_sync_point_update_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get client rbd_mirror_sync_point_update_age
ceph -s
# client options: set on client section or ceph.conf
```

---


[← Overview](../OVERVIEW.md)
