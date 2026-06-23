# OSD-related settings

MON config deep dive — 28 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_osd_adjust_down_out_interval](#mon_osd_adjust_down_out_interval) | `True` | Advanced | Performance |
| [mon_osd_adjust_heartbeat_grace](#mon_osd_adjust_heartbeat_grace) | `True` | Advanced | Performance |
| [mon_osd_auto_mark_auto_out_in](#mon_osd_auto_mark_auto_out_in) | `True` | Advanced | Performance |
| [mon_osd_auto_mark_in](#mon_osd_auto_mark_in) | `False` | Advanced | Performance |
| [mon_osd_auto_mark_new_in](#mon_osd_auto_mark_new_in) | `True` | Advanced | Performance |
| [mon_osd_blocklist_default_expire](#mon_osd_blocklist_default_expire) | `1_hr` | Advanced | Performance |
| [mon_osd_cache_size](#mon_osd_cache_size) | `500` | Advanced | Performance |
| [mon_osd_cache_size_min](#mon_osd_cache_size_min) | `128_M` | Advanced | Performance |
| [mon_osd_crush_smoke_test](#mon_osd_crush_smoke_test) | `True` | Advanced | Performance |
| [mon_osd_destroyed_out_interval](#mon_osd_destroyed_out_interval) | `10_min` | Advanced | Performance |
| [mon_osd_down_out_interval](#mon_osd_down_out_interval) | `10_min` | Advanced | Performance |
| [mon_osd_down_out_subtree_limit](#mon_osd_down_out_subtree_limit) | `rack` | Advanced | Performance |
| [mon_osd_laggy_halflife](#mon_osd_laggy_halflife) | `1_hr` | Advanced | Performance |
| [mon_osd_laggy_max_interval](#mon_osd_laggy_max_interval) | `5_min` | Advanced | Performance |
| [mon_osd_laggy_weight](#mon_osd_laggy_weight) | `0.3` | Advanced | Performance |
| [mon_osd_mapping_pgs_per_chunk](#mon_osd_mapping_pgs_per_chunk) | `4096` | Dev | Dev |
| [mon_osd_max_initial_pgs](#mon_osd_max_initial_pgs) | `1024` | Advanced | Performance |
| [mon_osd_min_in_ratio](#mon_osd_min_in_ratio) | `0.75` | Advanced | Performance |
| [mon_osd_min_up_ratio](#mon_osd_min_up_ratio) | `0.3` | Advanced | Performance |
| [mon_osd_warn_num_repaired](#mon_osd_warn_num_repaired) | `10` | Advanced | Performance |
| [mon_osd_warn_op_age](#mon_osd_warn_op_age) | `32` | Advanced | Performance |
| [mon_osdmap_full_prune_enabled](#mon_osdmap_full_prune_enabled) | `True` | Advanced | Policy |
| [mon_osdmap_full_prune_interval](#mon_osdmap_full_prune_interval) | `10` | Advanced | Performance |
| [mon_osdmap_full_prune_min](#mon_osdmap_full_prune_min) | `10000` | Advanced | Performance |
| [mon_osdmap_full_prune_txsize](#mon_osdmap_full_prune_txsize) | `100` | Advanced | Performance |
| [mon_warn_on_filestore_osds](#mon_warn_on_filestore_osds) | `True` | Dev | Dev |
| [mon_warn_on_osd_down_out_interval_zero](#mon_warn_on_osd_down_out_interval_zero) | `True` | Advanced | Performance |
| [osd_crush_update_weight_set](#osd_crush_update_weight_set) | `True` | Advanced | Performance |

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

### mon_osd_adjust_down_out_interval

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osd_adjust_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_adjust_down_out_interval) |

**What it does:** increase the mon_osd_down_out_interval if an OSD appears to be laggy

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osd_adjust_down_out_interval false
ceph config get mon mon_osd_adjust_down_out_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_adjust_down_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_adjust_heartbeat_grace

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osd_adjust_heartbeat_grace](../../../config/mon/mon.md#SP_mon_osd_adjust_heartbeat_grace) |

**What it does:** increase OSD heartbeat grace if peers appear to be laggy

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osd_adjust_heartbeat_grace false
ceph config get mon mon_osd_adjust_heartbeat_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_adjust_heartbeat_grace
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_auto_out_in

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osd_auto_mark_auto_out_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_auto_out_in) |

**What it does:** mark any OSD that comes up that was automatically marked 'out' back 'in'

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osd_auto_mark_auto_out_in false
ceph config get mon mon_osd_auto_mark_auto_out_in
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_auto_mark_auto_out_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_in

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_osd_auto_mark_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_in) |

**What it does:** mark any OSD that comes up 'in'

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_osd_auto_mark_in true
ceph config get mon mon_osd_auto_mark_in
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_auto_mark_in
ceph -s
ceph mon stat
```

---

### mon_osd_auto_mark_new_in

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osd_auto_mark_new_in](../../../config/mon/mon.md#SP_mon_osd_auto_mark_new_in) |

**What it does:** mark any new OSD that comes up 'in'

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osd_auto_mark_new_in false
ceph config get mon mon_osd_auto_mark_new_in
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_auto_mark_new_in
ceph -s
ceph mon stat
```

---

### mon_osd_blocklist_default_expire

| | |
|---|---|
| Type | Float · default `1_hr` · **Advanced** |
| Table | [mon.md#SP_mon_osd_blocklist_default_expire](../../../config/mon/mon.md#SP_mon_osd_blocklist_default_expire) |

**What it does:** Duration in seconds that blocklist entries for clients remain in the OSD map

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_blocklist_default_expire 1_hr
ceph config get mon mon_osd_blocklist_default_expire
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_blocklist_default_expire
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_osd_cache_size](../../../config/mon/mon.md#SP_mon_osd_cache_size) |

**What it does:** maximum number of OSDMaps to cache in memory

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_cache_size 500
ceph config get mon mon_osd_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_cache_size
ceph -s
ceph mon stat
```

---

### mon_osd_cache_size_min

| | |
|---|---|
| Type | Size · default `128_M` · **Advanced** |
| Table | [mon.md#SP_mon_osd_cache_size_min](../../../config/mon/mon.md#SP_mon_osd_cache_size_min) |

**What it does:** The minimum amount of bytes to be kept mapped in memory for osd monitor caches.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_cache_size_min 128_M
ceph config get mon mon_osd_cache_size_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_cache_size_min
ceph -s
ceph mon stat
```

---

### mon_osd_crush_smoke_test

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osd_crush_smoke_test](../../../config/mon/mon.md#SP_mon_osd_crush_smoke_test) |

**What it does:** perform a smoke test on any new CRUSH map before accepting changes

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osd_crush_smoke_test false
ceph config get mon mon_osd_crush_smoke_test
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_crush_smoke_test
ceph -s
ceph mon stat
```

---

### mon_osd_destroyed_out_interval

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [mon.md#SP_mon_osd_destroyed_out_interval](../../../config/mon/mon.md#SP_mon_osd_destroyed_out_interval) |

**What it does:** mark any OSD 'out' that has been 'destroy'ed for this long (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_osd_destroyed_out_interval 10_min
ceph config get mon mon_osd_destroyed_out_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_destroyed_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_down_out_interval

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [mon.md#SP_mon_osd_down_out_interval](../../../config/mon/mon.md#SP_mon_osd_down_out_interval) |

**What it does:** mark any OSD 'out' that has been 'down' for this long (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_osd_down_out_interval 10_min
ceph config get mon mon_osd_down_out_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_down_out_interval
ceph -s
ceph mon stat
```

---

### mon_osd_down_out_subtree_limit

| | |
|---|---|
| Type | Str · default `rack` · **Advanced** |
| Table | [mon.md#SP_mon_osd_down_out_subtree_limit](../../../config/mon/mon.md#SP_mon_osd_down_out_subtree_limit) |

**What it does:** do not automatically mark OSDs 'out' if an entire subtree of this size is down

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_down_out_subtree_limit rack
ceph config get mon mon_osd_down_out_subtree_limit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `rack`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_down_out_subtree_limit
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_halflife

| | |
|---|---|
| Type | Int · default `1_hr` · **Advanced** |
| Table | [mon.md#SP_mon_osd_laggy_halflife](../../../config/mon/mon.md#SP_mon_osd_laggy_halflife) |

**What it does:** halflife of OSD 'lagginess' factor

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_laggy_halflife 1_hr
ceph config get mon mon_osd_laggy_halflife
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_hr`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_laggy_halflife
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_max_interval

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [mon.md#SP_mon_osd_laggy_max_interval](../../../config/mon/mon.md#SP_mon_osd_laggy_max_interval) |

**What it does:** cap value for period for OSD to be marked for laggy_interval calculation

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_laggy_max_interval 5_min
ceph config get mon mon_osd_laggy_max_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_laggy_max_interval
ceph -s
ceph mon stat
```

---

### mon_osd_laggy_weight

| | |
|---|---|
| Type | Float · default `0.3` · **Advanced** |
| Table | [mon.md#SP_mon_osd_laggy_weight](../../../config/mon/mon.md#SP_mon_osd_laggy_weight) |

**What it does:** how heavily to weight OSD marking itself back up in overall laggy_probability

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_laggy_weight 0.3
ceph config get mon mon_osd_laggy_weight
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `1`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_laggy_weight
ceph -s
ceph mon stat
```

---

### mon_osd_mapping_pgs_per_chunk

| | |
|---|---|
| Type | Int · default `4096` · **Dev** |
| Table | [mon.md#SP_mon_osd_mapping_pgs_per_chunk](../../../config/mon/mon.md#SP_mon_osd_mapping_pgs_per_chunk) |

**What it does:** granularity of PG placement calculation background work

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_osd_mapping_pgs_per_chunk 4096
ceph config get mon mon_osd_mapping_pgs_per_chunk
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4096`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_osd_max_initial_pgs

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [mon.md#SP_mon_osd_max_initial_pgs](../../../config/mon/mon.md#SP_mon_osd_max_initial_pgs) |

**What it does:** maximum number of PGs a pool will created with

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_max_initial_pgs 1024
ceph config get mon mon_osd_max_initial_pgs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_max_initial_pgs
ceph -s
ceph mon stat
```

---

### mon_osd_min_in_ratio

| | |
|---|---|
| Type | Float · default `0.75` · **Advanced** |
| Table | [mon.md#SP_mon_osd_min_in_ratio](../../../config/mon/mon.md#SP_mon_osd_min_in_ratio) |

**What it does:** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'in'

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_min_in_ratio 0.75
ceph config get mon mon_osd_min_in_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.75`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_min_in_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_min_up_ratio

| | |
|---|---|
| Type | Float · default `0.3` · **Advanced** |
| Table | [mon.md#SP_mon_osd_min_up_ratio](../../../config/mon/mon.md#SP_mon_osd_min_up_ratio) |

**What it does:** do not automatically mark OSDs 'out' if fewer than this many OSDs are 'up'

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_min_up_ratio 0.3
ceph config get mon mon_osd_min_up_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_min_up_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_warn_num_repaired

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_osd_warn_num_repaired](../../../config/mon/mon.md#SP_mon_osd_warn_num_repaired) |

**What it does:** issue OSD_TOO_MANY_REPAIRS health warning if an OSD has more than this many read repairs

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_warn_num_repaired 10
ceph config get mon mon_osd_warn_num_repaired
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_warn_num_repaired
ceph -s
ceph mon stat
```

---

### mon_osd_warn_op_age

| | |
|---|---|
| Type | Float · default `32` · **Advanced** |
| Table | [mon.md#SP_mon_osd_warn_op_age](../../../config/mon/mon.md#SP_mon_osd_warn_op_age) |

**What it does:** issue REQUEST_SLOW health warning if OSD ops are slower than this age (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_warn_op_age 32
ceph config get mon mon_osd_warn_op_age
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_warn_op_age
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_osdmap_full_prune_enabled](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_enabled) |

**What it does:** enables pruning full osdmap versions when we go over a given number of maps

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_osdmap_full_prune_enabled false
ceph config get mon mon_osdmap_full_prune_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osdmap_full_prune_enabled
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_interval

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_osdmap_full_prune_interval](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_interval) |

**What it does:** interval between maps that will not be pruned; maps in the middle will be pruned.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_osdmap_full_prune_interval 10
ceph config get mon mon_osdmap_full_prune_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osdmap_full_prune_interval
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_min

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [mon.md#SP_mon_osdmap_full_prune_min](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_min) |

**What it does:** minimum number of versions in the store to trigger full map pruning

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osdmap_full_prune_min 10000
ceph config get mon mon_osdmap_full_prune_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osdmap_full_prune_min
ceph -s
ceph mon stat
```

---

### mon_osdmap_full_prune_txsize

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [mon.md#SP_mon_osdmap_full_prune_txsize](../../../config/mon/mon.md#SP_mon_osdmap_full_prune_txsize) |

**What it does:** number of maps we will prune per iteration

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osdmap_full_prune_txsize 100
ceph config get mon mon_osdmap_full_prune_txsize
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osdmap_full_prune_txsize
ceph -s
ceph mon stat
```

---

### mon_warn_on_filestore_osds

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mon.md#SP_mon_warn_on_filestore_osds](../../../config/mon/mon.md#SP_mon_warn_on_filestore_osds) |

**What it does:** log health warn for filestore OSDs

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_warn_on_filestore_osds false
ceph config get mon mon_warn_on_filestore_osds
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_warn_on_osd_down_out_interval_zero

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_osd_down_out_interval_zero](../../../config/mon/mon.md#SP_mon_warn_on_osd_down_out_interval_zero) |

**What it does:** issue OSD_NO_DOWN_OUT_INTERVAL health warning if mon_osd_down_out_interval is zero

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_osd_down_out_interval_zero false
ceph config get mon mon_warn_on_osd_down_out_interval_zero
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_osd_down_out_interval_zero
ceph -s
ceph mon stat
```

---

### osd_crush_update_weight_set

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_crush_update_weight_set](../../../config/mon/osd.md#SP_osd_crush_update_weight_set) |

**What it does:** update CRUSH weight-set weights when updating weights

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_crush_update_weight_set false
ceph config get osd osd_crush_update_weight_set
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_crush_update_weight_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
