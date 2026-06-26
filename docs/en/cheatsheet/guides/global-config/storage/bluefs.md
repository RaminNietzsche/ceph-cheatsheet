# Bluefs

Global config deep dive — 24 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [bluefs_alloc_size](#bluefs_alloc_size) | `1_M` | Advanced | Performance |
| [bluefs_allocator](#bluefs_allocator) | `hybrid` | Dev | Dev |
| [bluefs_buffered_io](#bluefs_buffered_io) | `True` | Advanced | Performance |
| [bluefs_check_for_zeros](#bluefs_check_for_zeros) | `False` | Dev | Dev |
| [bluefs_check_volume_selector_often](#bluefs_check_volume_selector_often) | `False` | Dev | Dev |
| [bluefs_check_volume_selector_on_mount](#bluefs_check_volume_selector_on_mount) | `False` | Dev | Dev |
| [bluefs_compact_log_sync](#bluefs_compact_log_sync) | `False` | Advanced | Performance |
| [bluefs_debug_force_slow](#bluefs_debug_force_slow) | `False` | Dev | Dev |
| [bluefs_failed_shared_alloc_cooldown](#bluefs_failed_shared_alloc_cooldown) | `600` | Advanced | Performance |
| [bluefs_log_compact_min_ratio](#bluefs_log_compact_min_ratio) | `5` | Advanced | Performance |
| [bluefs_log_compact_min_size](#bluefs_log_compact_min_size) | `16_M` | Advanced | Performance |
| [bluefs_log_replay_check_allocations](#bluefs_log_replay_check_allocations) | `True` | Advanced | Performance |
| [bluefs_max_log_runway](#bluefs_max_log_runway) | `4_M` | Advanced | Performance |
| [bluefs_max_prefetch](#bluefs_max_prefetch) | `1_M` | Advanced | Performance |
| [bluefs_min_flush_size](#bluefs_min_flush_size) | `512_K` | Advanced | Performance |
| [bluefs_min_log_runway](#bluefs_min_log_runway) | `1_M` | Advanced | Performance |
| [bluefs_replay_recovery](#bluefs_replay_recovery) | `False` | Dev | Dev |
| [bluefs_replay_recovery_disable_compact](#bluefs_replay_recovery_disable_compact) | `False` | Advanced | Policy |
| [bluefs_shared_alloc_size](#bluefs_shared_alloc_size) | `64_K` | Advanced | Performance |
| [bluefs_spillover_cleaner](#bluefs_spillover_cleaner) | `False` | Advanced | Performance |
| [bluefs_spillover_cleaner_work_ratio](#bluefs_spillover_cleaner_work_ratio) | `0.1` | Advanced | Performance |
| [bluefs_spillover_idle_time](#bluefs_spillover_idle_time) | `1200` | Advanced | Performance |
| [bluefs_sync_write](#bluefs_sync_write) | `False` | Advanced | Performance |
| [bluefs_wal_envelope_mode](#bluefs_wal_envelope_mode) | `True` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### bluefs_alloc_size

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_alloc_size](../../../config/global/bluefs.md#SP_bluefs_alloc_size) |

**What it does:** Allocation unit size for DB and WAL devices

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluefs_alloc_size 1_M
ceph config get global bluefs_alloc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_alloc_size
ceph -s
```

---

### bluefs_allocator

| | |
|---|---|
| Type | Str · enum: ["bitmap", "stupid", "avl", "btree", "hybrid", "hybrid_btree2"] · default `hybrid` · **Dev** |
| Table | [bluefs.md#SP_bluefs_allocator](../../../config/global/bluefs.md#SP_bluefs_allocator) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluefs_allocator hybrid
ceph config get global bluefs_allocator
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`hybrid`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_buffered_io

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_buffered_io](../../../config/global/bluefs.md#SP_bluefs_buffered_io) |

**What it does:** Enabled buffered IO for BlueFS reads. When this option is enabled, BlueFS will in some cases perform buffered reads. This allows the kernel page cache to act as a secondary cache for things like RocksDB block reads. For example, if the RocksDB block cache isn't large enough to hold all blocks during omap iteration, it may be possible to read them from page cache instead of from the device. This can dramatically improve performance when the osd_memory_target is too small to hold all entries in block cache but it does come with downsides. It has been reported to occasionally cause excessive kernel swapping (and associated stalls) under certain workloads. Currently the best and most consistent performing combination appears to be enabling bluefs_buffered_io and disabling system level swap. It is possible that this recommendation may change in the future however.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluefs_buffered_io false
ceph config get global bluefs_buffered_io
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_buffered_io
ceph -s
```

---

### bluefs_check_for_zeros

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluefs.md#SP_bluefs_check_for_zeros](../../../config/global/bluefs.md#SP_bluefs_check_for_zeros) |

**What it does:** Check data read for suspicious pages Looks into data read to check if there is a 4K block entirely filled with zeros. If this happens, we re-read data. If there is difference, we print error to log.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluefs_check_for_zeros true
ceph config get global bluefs_check_for_zeros
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_check_volume_selector_often

| | |
|---|---|
| Type | Bool · default `False` · **Dev** · **STARTUP** (restart required) |
| Table | [bluefs.md#SP_bluefs_check_volume_selector_often](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_often) |

**What it does:** Periodically check validity of volume selector Periodically checks if current volume selector does not diverge from the valid state. Reference is constructed from bluefs inode table. Asserts on inconsistency. This is debug feature.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`bluefs_check_volume_selector_on_mount`](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_on_mount)

**Example:**

```bash
ceph config set global bluefs_check_volume_selector_often true
ceph config get global bluefs_check_volume_selector_often
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_check_volume_selector_on_mount

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluefs.md#SP_bluefs_check_volume_selector_on_mount](../../../config/global/bluefs.md#SP_bluefs_check_volume_selector_on_mount) |

**What it does:** Check validity of volume selector on mount/umount Checks if volume selector did not diverge from the state it should be in. Reference is constructed from bluefs inode table. Asserts on inconsistency.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluefs_check_volume_selector_on_mount true
ceph config get global bluefs_check_volume_selector_on_mount
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_compact_log_sync

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_compact_log_sync](../../../config/global/bluefs.md#SP_bluefs_compact_log_sync) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluefs_compact_log_sync true
ceph config get global bluefs_compact_log_sync
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_compact_log_sync
ceph -s
```

---

### bluefs_debug_force_slow

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluefs.md#SP_bluefs_debug_force_slow](../../../config/global/bluefs.md#SP_bluefs_debug_force_slow) |

**What it does:** For testing. Force BlueFS to allocate files on slow device. When enabled, the RocksDBBlueFSVolumeSelector will ignore normal placement policy and redirect allocations to slow device.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluefs_debug_force_slow true
ceph config get global bluefs_debug_force_slow
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_failed_shared_alloc_cooldown

| | |
|---|---|
| Type | Float · default `600` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_failed_shared_alloc_cooldown](../../../config/global/bluefs.md#SP_bluefs_failed_shared_alloc_cooldown) |

**What it does:** duration(in seconds) untill the next attempt to use 'bluefs_shared_alloc_size' after facing ENOSPC failure. Cooldown period(in seconds) when BlueFS uses shared/slow device allocation size instead of "bluefs_shared_alloc_size' one after facing recoverable (via fallback to smaller chunk size) ENOSPC failure. Intended primarily to avoid repetitive unsuccessful allocations which might be expensive.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluefs_failed_shared_alloc_cooldown 600
ceph config get global bluefs_failed_shared_alloc_cooldown
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `600`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_failed_shared_alloc_cooldown
ceph -s
```

---

### bluefs_log_compact_min_ratio

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_log_compact_min_ratio](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_ratio) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_log_compact_min_ratio 5
ceph config get global bluefs_log_compact_min_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_log_compact_min_ratio
ceph -s
```

---

### bluefs_log_compact_min_size

| | |
|---|---|
| Type | Size · default `16_M` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_log_compact_min_size](../../../config/global/bluefs.md#SP_bluefs_log_compact_min_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_log_compact_min_size 16_M
ceph config get global bluefs_log_compact_min_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_log_compact_min_size
ceph -s
```

---

### bluefs_log_replay_check_allocations

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_log_replay_check_allocations](../../../config/global/bluefs.md#SP_bluefs_log_replay_check_allocations) |

**What it does:** Enables checks for allocations consistency during log replay

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluefs_log_replay_check_allocations false
ceph config get global bluefs_log_replay_check_allocations
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_log_replay_check_allocations
ceph -s
```

---

### bluefs_max_log_runway

| | |
|---|---|
| Type | Size · default `4_M` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_max_log_runway](../../../config/global/bluefs.md#SP_bluefs_max_log_runway) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_max_log_runway 4_M
ceph config get global bluefs_max_log_runway
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_max_log_runway
ceph -s
```

---

### bluefs_max_prefetch

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_max_prefetch](../../../config/global/bluefs.md#SP_bluefs_max_prefetch) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_max_prefetch 1_M
ceph config get global bluefs_max_prefetch
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_max_prefetch
ceph -s
```

---

### bluefs_min_flush_size

| | |
|---|---|
| Type | Size · default `512_K` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_min_flush_size](../../../config/global/bluefs.md#SP_bluefs_min_flush_size) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_min_flush_size 512_K
ceph config get global bluefs_min_flush_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_min_flush_size
ceph -s
```

---

### bluefs_min_log_runway

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_min_log_runway](../../../config/global/bluefs.md#SP_bluefs_min_log_runway) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bluefs_min_log_runway 1_M
ceph config get global bluefs_min_log_runway
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_min_log_runway
ceph -s
```

---

### bluefs_replay_recovery

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bluefs.md#SP_bluefs_replay_recovery](../../../config/global/bluefs.md#SP_bluefs_replay_recovery) |

**What it does:** Attempt to read bluefs log so large that it became unreadable. If BlueFS log grows to extreme sizes (200GB+) it is likely that it becames unreadable. This options enables heuristics that scans devices for missing data. DO NOT ENABLE BY DEFAULT

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bluefs_replay_recovery true
ceph config get global bluefs_replay_recovery
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bluefs_replay_recovery_disable_compact

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_replay_recovery_disable_compact](../../../config/global/bluefs.md#SP_bluefs_replay_recovery_disable_compact) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluefs_replay_recovery_disable_compact true
ceph config get global bluefs_replay_recovery_disable_compact
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_replay_recovery_disable_compact
ceph -s
```

---

### bluefs_shared_alloc_size

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_shared_alloc_size](../../../config/global/bluefs.md#SP_bluefs_shared_alloc_size) |

**What it does:** Allocation unit size for primary/shared device

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluefs_shared_alloc_size 64_K
ceph config get global bluefs_shared_alloc_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_shared_alloc_size
ceph -s
```

---

### bluefs_spillover_cleaner

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_spillover_cleaner](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner) |

**What it does:** Enable Background BlueFS Spillover cleaner thread Enables a background cleaner thread in BlueFS that periodically scans files that spilled over to the slow device and attempts to migrate them back to the BlueFS DB device

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluefs_spillover_cleaner true
ceph config get global bluefs_spillover_cleaner
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_spillover_cleaner
ceph -s
```

---

### bluefs_spillover_cleaner_work_ratio

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_spillover_cleaner_work_ratio](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner_work_ratio) |

**What it does:** Fraction of time the BlueFS spillover cleaner spends performing work. Controls the rate of spillover migration work. After each migration step, the cleaner targets to sleep proportionally to the time spent doing work This reduces interference with foreground IO. For example, if a migration step took 10 ms and the ratio is 0.1, the cleaner sleeps for ~90 ms before the next step. This results in approximately 10% work time and 90% sleep time.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bluefs_spillover_cleaner_work_ratio 0.1
ceph config get global bluefs_spillover_cleaner_work_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_spillover_cleaner_work_ratio
ceph -s
```

---

### bluefs_spillover_idle_time

| | |
|---|---|
| Type | Uint · default `1200` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_spillover_idle_time](../../../config/global/bluefs.md#SP_bluefs_spillover_idle_time) |

**What it does:** Idle time in seconds before the BlueFS spillover cleaner wakes up for the next scan cycle. When no spillover files remain to migrate, the cleaner enters an idle sleep state for this duration. Once the idle period expires, it wakes up, scans for spillover files, and resumes migration if needed.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`bluefs_spillover_cleaner`](../../../config/global/bluefs.md#SP_bluefs_spillover_cleaner)

**Example:**

```bash
ceph config set global bluefs_spillover_idle_time 1200
ceph config get global bluefs_spillover_idle_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_spillover_idle_time
ceph -s
```

---

### bluefs_sync_write

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_sync_write](../../../config/global/bluefs.md#SP_bluefs_sync_write) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bluefs_sync_write true
ceph config get global bluefs_sync_write
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_sync_write
ceph -s
```

---

### bluefs_wal_envelope_mode

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bluefs.md#SP_bluefs_wal_envelope_mode](../../../config/global/bluefs.md#SP_bluefs_wal_envelope_mode) |

**What it does:** Enables a faster backend in BlueFS for WAL writes. In envelope mode BlueFS files do not need to update metadata. When applied to RocksDB WAL files, it reduces by ~50% the amount of fdatasync syscalls. Downgrading from an envelope mode to legacy mode requires `ceph-bluestore-tool --command downgrade-wal-to-v1`.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bluefs_wal_envelope_mode false
ceph config get global bluefs_wal_envelope_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bluefs_wal_envelope_mode
ceph -s
```

---


[← Overview](../OVERVIEW.md)
