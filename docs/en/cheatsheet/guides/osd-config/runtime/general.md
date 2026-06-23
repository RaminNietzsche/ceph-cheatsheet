# General runtime

OSD config deep dive — 26 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_aggregated_slow_ops_logging](#osd_aggregated_slow_ops_logging) | `True` | Advanced | Performance |
| [osd_compact_on_start](#osd_compact_on_start) | `False` | Advanced | Performance |
| [osd_ec_partial_reads](#osd_ec_partial_reads) | `True` | Advanced | Performance |
| [osd_extblkdev_plugins](#osd_extblkdev_plugins) | `vdo fcm` | Advanced | Performance |
| [osd_find_best_info_ignore_history_les](#osd_find_best_info_ignore_history_les) | `False` | Dev | Dev |
| [osd_journal](#osd_journal) | `/var/lib/ceph/osd/$cluster-$id/journal` | Advanced | Performance |
| [osd_journal_flush_on_shutdown](#osd_journal_flush_on_shutdown) | `True` | Advanced | Performance |
| [osd_journal_size](#osd_journal_size) | `5_K` | Advanced | Performance |
| [osd_map_cache_size](#osd_map_cache_size) | `50` | Advanced | Performance |
| [osd_num_cache_shards](#osd_num_cache_shards) | `32` | Advanced | Performance |
| [osd_numa_auto_affinity](#osd_numa_auto_affinity) | `True` | Advanced | Performance |
| [osd_numa_node](#osd_numa_node) | `-1` | Advanced | Performance |
| [osd_numa_prefer_iface](#osd_numa_prefer_iface) | `True` | Advanced | Performance |
| [osd_op_num_shards](#osd_op_num_shards) | `0` | Advanced | Performance |
| [osd_op_num_shards_hdd](#osd_op_num_shards_hdd) | `1` | Advanced | Performance |
| [osd_op_num_shards_ssd](#osd_op_num_shards_ssd) | `8` | Advanced | Performance |
| [osd_op_num_threads_per_shard](#osd_op_num_threads_per_shard) | `0` | Advanced | Performance |
| [osd_op_num_threads_per_shard_hdd](#osd_op_num_threads_per_shard_hdd) | `5` | Advanced | Performance |
| [osd_op_num_threads_per_shard_ssd](#osd_op_num_threads_per_shard_ssd) | `2` | Advanced | Performance |
| [osd_op_queue](#osd_op_queue) | `mclock_scheduler` | Advanced | Performance |
| [osd_op_queue_cut_off](#osd_op_queue_cut_off) | `high` | Advanced | Performance |
| [osd_os_flags](#osd_os_flags) | `0` | Dev | Dev |
| [osd_push_per_object_cost](#osd_push_per_object_cost) | `1000` | Advanced | Performance |
| [osd_read_ec_check_for_errors](#osd_read_ec_check_for_errors) | `False` | Advanced | Performance |
| [osd_rocksdb_iterator_bounds_enabled](#osd_rocksdb_iterator_bounds_enabled) | `True` | Dev | Dev |
| [osd_uuid](#osd_uuid) | `(empty)` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_aggregated_slow_ops_logging

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_aggregated_slow_ops_logging](../../../config/osd/osd.md#SP_osd_aggregated_slow_ops_logging) |

**What it does:** Allow OSD daemon to send an aggregated slow ops to the cluster log

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_aggregated_slow_ops_logging false
ceph config get osd osd_aggregated_slow_ops_logging
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_aggregated_slow_ops_logging
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_compact_on_start

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_compact_on_start](../../../config/osd/osd.md#SP_osd_compact_on_start) |

**What it does:** compact OSD's object store's OMAP on start

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_compact_on_start true
ceph config get osd osd_compact_on_start
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_compact_on_start
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_ec_partial_reads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_ec_partial_reads](../../../config/osd/osd.md#SP_osd_ec_partial_reads) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_ec_partial_reads false
ceph config get osd osd_ec_partial_reads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_ec_partial_reads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_extblkdev_plugins

| | |
|---|---|
| Type | Str · default `vdo fcm` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_extblkdev_plugins](../../../config/osd/osd.md#SP_osd_extblkdev_plugins) |

**What it does:** extended block device plugins to load, provide compression feedback at runtime

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_extblkdev_plugins "vdo fcm"
ceph config get osd osd_extblkdev_plugins
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `vdo fcm`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_extblkdev_plugins
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_find_best_info_ignore_history_les

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [osd.md#SP_osd_find_best_info_ignore_history_les](../../../config/osd/osd.md#SP_osd_find_best_info_ignore_history_les) |

**What it does:** ignore last_epoch_started value when peering AND PROBABLY LOSE DATA

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_find_best_info_ignore_history_les true
ceph config get osd osd_find_best_info_ignore_history_les
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_journal

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/osd/$cluster-$id/journal` · **Advanced** |
| Table | [osd.md#SP_osd_journal](../../../config/osd/osd.md#SP_osd_journal) |

**What it does:** path to OSD journal (when FileStore backend is in use)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_journal "/var/lib/ceph/osd/$cluster-$id/journal"
ceph config get osd osd_journal
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/osd/$cluster-$id/journal`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_journal
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_flush_on_shutdown

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [osd.md#SP_osd_journal_flush_on_shutdown](../../../config/osd/osd.md#SP_osd_journal_flush_on_shutdown) |

**What it does:** flush FileStore journal contents during clean OSD shutdown

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_journal_flush_on_shutdown false
ceph config get osd osd_journal_flush_on_shutdown
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_journal_flush_on_shutdown
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_journal_size

| | |
|---|---|
| Type | Size · default `5_K` · **Advanced** |
| Table | [osd.md#SP_osd_journal_size](../../../config/osd/osd.md#SP_osd_journal_size) |

**What it does:** size of FileStore journal (in MiB)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_journal_size 5_K
ceph config get osd osd_journal_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_journal_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_map_cache_size

| | |
|---|---|
| Type | Int · default `50` · **Advanced** |
| Table | [osd.md#SP_osd_map_cache_size](../../../config/osd/osd.md#SP_osd_map_cache_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_map_cache_size 50
ceph config get osd osd_map_cache_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_map_cache_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_num_cache_shards

| | |
|---|---|
| Type | Size · default `32` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_num_cache_shards](../../../config/osd/osd.md#SP_osd_num_cache_shards) |

**What it does:** The number of cache shards to use in the object store.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_num_cache_shards 32
ceph config get osd osd_num_cache_shards
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_num_cache_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_auto_affinity

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_numa_auto_affinity](../../../config/osd/osd.md#SP_osd_numa_auto_affinity) |

**What it does:** automatically set affinity to numa node when storage and network match

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_numa_auto_affinity false
ceph config get osd osd_numa_auto_affinity
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_numa_auto_affinity
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_node

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_numa_node](../../../config/osd/osd.md#SP_osd_numa_node) |

**What it does:** set affinity to a numa node (-1 for none)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_numa_node 128
ceph config get osd osd_numa_node
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_numa_node
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_numa_prefer_iface

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_numa_prefer_iface](../../../config/osd/osd.md#SP_osd_numa_prefer_iface) |

**What it does:** prefer IP on network interface on same numa node as storage

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd osd_numa_prefer_iface false
ceph config get osd osd_numa_prefer_iface
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_numa_prefer_iface
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards

| | |
|---|---|
| Type | Int · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_shards](../../../config/osd/osd.md#SP_osd_op_num_shards) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_shards 64
ceph config get osd osd_op_num_shards
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_shards
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_hdd

| | |
|---|---|
| Type | Int · default `1` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_shards_hdd](../../../config/osd/osd.md#SP_osd_op_num_shards_hdd) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_shards_hdd 1
ceph config get osd osd_op_num_shards_hdd
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_shards_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_shards_ssd

| | |
|---|---|
| Type | Int · default `8` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_shards_ssd](../../../config/osd/osd.md#SP_osd_op_num_shards_ssd) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_shards_ssd 8
ceph config get osd osd_op_num_shards_ssd
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_shards_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard

| | |
|---|---|
| Type | Int · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_threads_per_shard](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_threads_per_shard 64
ceph config get osd osd_op_num_threads_per_shard
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_threads_per_shard
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_hdd

| | |
|---|---|
| Type | Int · default `5` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_threads_per_shard_hdd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_hdd) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_threads_per_shard_hdd 5
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_threads_per_shard_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_num_threads_per_shard_ssd

| | |
|---|---|
| Type | Int · default `2` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_osd_op_num_threads_per_shard_ssd](../../../config/osd/osd.md#SP_osd_op_num_threads_per_shard_ssd) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_num_threads_per_shard_ssd 2
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_num_threads_per_shard_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue

| | |
|---|---|
| Type | Str · enum: ["wpq", "mclock_scheduler", "debug_random"] · default `mclock_scheduler` · **Advanced** |
| Table | [osd.md#SP_osd_op_queue](../../../config/osd/osd.md#SP_osd_op_queue) |

**What it does:** OSD operation queue scheduler (`mclock_scheduler`, `wpq`, or `debug_random`). Production clusters should use mClock.

**When to use:** Keep `mclock_scheduler` unless upstream support directs otherwise.

**Example:**

```bash
ceph config set osd osd_op_queue mclock_scheduler
ceph config get osd osd_op_queue
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `mclock_scheduler`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_queue
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_op_queue_cut_off

| | |
|---|---|
| Type | Str · enum: ["low", "high", "debug_random"] · default `high` · **Advanced** |
| Table | [osd.md#SP_osd_op_queue_cut_off](../../../config/osd/osd.md#SP_osd_op_queue_cut_off) |

**What it does:** the threshold between high priority ops and low priority ops

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_op_queue_cut_off high
ceph config get osd osd_op_queue_cut_off
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `high`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_queue_cut_off
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_os_flags

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [osd.md#SP_osd_os_flags](../../../config/osd/osd.md#SP_osd_os_flags) |

**What it does:** flags to skip filestore omap or journal initialization

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_os_flags 64
ceph config get osd osd_os_flags
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_push_per_object_cost

| | |
|---|---|
| Type | Size · default `1000` · **Advanced** |
| Table | [osd.md#SP_osd_push_per_object_cost](../../../config/osd/osd.md#SP_osd_push_per_object_cost) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_push_per_object_cost 1000
ceph config get osd osd_push_per_object_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_push_per_object_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_read_ec_check_for_errors

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [osd.md#SP_osd_read_ec_check_for_errors](../../../config/osd/osd.md#SP_osd_read_ec_check_for_errors) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd osd_read_ec_check_for_errors true
ceph config get osd osd_read_ec_check_for_errors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_read_ec_check_for_errors
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_rocksdb_iterator_bounds_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [osd.md#SP_osd_rocksdb_iterator_bounds_enabled](../../../config/osd/osd.md#SP_osd_rocksdb_iterator_bounds_enabled) |

**What it does:** Whether omap iterator bounds are applied to rocksdb iterator ReadOptions

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_rocksdb_iterator_bounds_enabled false
ceph config get osd osd_rocksdb_iterator_bounds_enabled
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_uuid

| | |
|---|---|
| Type | Uuid · default `(empty)` · **Advanced** |
| Table | [osd.md#SP_osd_uuid](../../../config/osd/osd.md#SP_osd_uuid) |

**What it does:** uuid label for a new OSD

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd osd_uuid (empty)
ceph config get osd osd_uuid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_uuid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
