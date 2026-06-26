# Bdev

Global config deep dive — 31 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [bdev_aio](#bdev_aio) | `True` | Advanced | Performance |
| [bdev_aio_max_queue_depth](#bdev_aio_max_queue_depth) | `1024` | Advanced | Performance |
| [bdev_aio_poll_ms](#bdev_aio_poll_ms) | `250` | Advanced | Performance |
| [bdev_aio_reap_max](#bdev_aio_reap_max) | `16` | Advanced | Performance |
| [bdev_aio_submit_retry_initial_delay_us](#bdev_aio_submit_retry_initial_delay_us) | `125` | Advanced | Performance |
| [bdev_aio_submit_retry_max](#bdev_aio_submit_retry_max) | `16` | Advanced | Performance |
| [bdev_async_discard](#bdev_async_discard) | `False` | Advanced | Performance |
| [bdev_async_discard_max_pending](#bdev_async_discard_max_pending) | `1000000` | Advanced | Performance |
| [bdev_async_discard_threads](#bdev_async_discard_threads) | `0` | Advanced | Performance |
| [bdev_block_size](#bdev_block_size) | `4_K` | Advanced | Performance |
| [bdev_debug_aio](#bdev_debug_aio) | `False` | Dev | Dev |
| [bdev_debug_aio_log_age](#bdev_debug_aio_log_age) | `5` | Dev | Dev |
| [bdev_debug_aio_suicide_timeout](#bdev_debug_aio_suicide_timeout) | `1_min` | Dev | Dev |
| [bdev_debug_discard_sleep](#bdev_debug_discard_sleep) | `0` | Dev | Dev |
| [bdev_debug_inflight_ios](#bdev_debug_inflight_ios) | `False` | Dev | Dev |
| [bdev_discard_max_bytes](#bdev_discard_max_bytes) | `10_G` | Advanced | Performance |
| [bdev_enable_discard](#bdev_enable_discard) | `False` | Advanced | Policy |
| [bdev_flock_retry](#bdev_flock_retry) | `3` | Advanced | Performance |
| [bdev_flock_retry_interval](#bdev_flock_retry_interval) | `0.1` | Advanced | Performance |
| [bdev_inject_crash](#bdev_inject_crash) | `0` | Dev | Dev |
| [bdev_inject_crash_flush_delay](#bdev_inject_crash_flush_delay) | `2` | Dev | Dev |
| [bdev_ioring](#bdev_ioring) | `False` | Advanced | Performance |
| [bdev_ioring_hipri](#bdev_ioring_hipri) | `False` | Advanced | Performance |
| [bdev_ioring_sqthread_poll](#bdev_ioring_sqthread_poll) | `False` | Advanced | Performance |
| [bdev_max_discard_length](#bdev_max_discard_length) | `2147483648` | Advanced | Performance |
| [bdev_nvme_unbind_from_kernel](#bdev_nvme_unbind_from_kernel) | `False` | Advanced | Performance |
| [bdev_read_buffer_alignment](#bdev_read_buffer_alignment) | `4_K` | Advanced | Performance |
| [bdev_read_preallocated_huge_buffers](#bdev_read_preallocated_huge_buffers) | `(empty)` | Advanced | Performance |
| [bdev_stalled_read_warn_lifetime](#bdev_stalled_read_warn_lifetime) | `86400` | Advanced | Performance |
| [bdev_stalled_read_warn_threshold](#bdev_stalled_read_warn_threshold) | `1` | Advanced | Performance |
| [bdev_type](#bdev_type) | `(empty)` | Advanced | Performance |

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

### bdev_aio

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio](../../../config/global/bdev.md#SP_bdev_aio) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global bdev_aio false
ceph config get global bdev_aio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio
ceph -s
```

---

### bdev_aio_max_queue_depth

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio_max_queue_depth](../../../config/global/bdev.md#SP_bdev_aio_max_queue_depth) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global bdev_aio_max_queue_depth 1024
ceph config get global bdev_aio_max_queue_depth
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio_max_queue_depth
ceph -s
```

---

### bdev_aio_poll_ms

| | |
|---|---|
| Type | Int · default `250` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio_poll_ms](../../../config/global/bdev.md#SP_bdev_aio_poll_ms) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_aio_poll_ms 250
ceph config get global bdev_aio_poll_ms
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `250`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio_poll_ms
ceph -s
```

---

### bdev_aio_reap_max

| | |
|---|---|
| Type | Int · default `16` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio_reap_max](../../../config/global/bdev.md#SP_bdev_aio_reap_max) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_aio_reap_max 16
ceph config get global bdev_aio_reap_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio_reap_max
ceph -s
```

---

### bdev_aio_submit_retry_initial_delay_us

| | |
|---|---|
| Type | Int · default `125` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio_submit_retry_initial_delay_us](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_initial_delay_us) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_aio_submit_retry_initial_delay_us 125
ceph config get global bdev_aio_submit_retry_initial_delay_us
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `125`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio_submit_retry_initial_delay_us
ceph -s
```

---

### bdev_aio_submit_retry_max

| | |
|---|---|
| Type | Int · default `16` · **Advanced** |
| Table | [bdev.md#SP_bdev_aio_submit_retry_max](../../../config/global/bdev.md#SP_bdev_aio_submit_retry_max) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_aio_submit_retry_max 16
ceph config get global bdev_aio_submit_retry_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_aio_submit_retry_max
ceph -s
```

---

### bdev_async_discard

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_async_discard](../../../config/global/bdev.md#SP_bdev_async_discard) |

**What it does:** When set this works like an alias for 'bdev_async_discard_threads = 1" mode to avoid implicit async discard mode disablement after upgrade. Ignored if 'dev_asunc_discard_threads' is greater than zero. This parameter is DEPRECATED and provided for backward compatibility for Squid minor releases only. PLEASE SWITCH TO 'bdev_async_discard_threads' USE.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_async_discard true
ceph config get global bdev_async_discard
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_async_discard
ceph -s
```

---

### bdev_async_discard_max_pending

| | |
|---|---|
| Type | Uint · default `1000000` · **Advanced** |
| Table | [bdev.md#SP_bdev_async_discard_max_pending](../../../config/global/bdev.md#SP_bdev_async_discard_max_pending) |

**What it does:** maximum number of pending discards The maximum number of pending async discards that can be queued and not claimed by an async discard thread. Discards will not be issued once the queue is full and blocks will be freed back to the allocator immediately instead. This is useful if you have a device with slow discard performance that can't keep up to a consistently high write workload. 0 means 'unlimited'.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`bdev_async_discard_threads`](../../../config/global/bdev.md#SP_bdev_async_discard_threads)

**Example:**

```bash
ceph config set global bdev_async_discard_max_pending 1000000
ceph config get global bdev_async_discard_max_pending
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_async_discard_max_pending
ceph -s
```

---

### bdev_async_discard_threads

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [bdev.md#SP_bdev_async_discard_threads](../../../config/global/bdev.md#SP_bdev_async_discard_threads) |

**What it does:** Number of discard threads used to issue discards to the device

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_async_discard_threads 64
ceph config get global bdev_async_discard_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_async_discard_threads
ceph -s
```

---

### bdev_block_size

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [bdev.md#SP_bdev_block_size](../../../config/global/bdev.md#SP_bdev_block_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_block_size 4_K
ceph config get global bdev_block_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_block_size
ceph -s
```

---

### bdev_debug_aio

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bdev.md#SP_bdev_debug_aio](../../../config/global/bdev.md#SP_bdev_debug_aio) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_debug_aio true
ceph config get global bdev_debug_aio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_debug_aio_log_age

| | |
|---|---|
| Type | Float · default `5` · **Dev** |
| Table | [bdev.md#SP_bdev_debug_aio_log_age](../../../config/global/bdev.md#SP_bdev_debug_aio_log_age) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_debug_aio_log_age 5
ceph config get global bdev_debug_aio_log_age
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_debug_aio_suicide_timeout

| | |
|---|---|
| Type | Float · default `1_min` · **Dev** |
| Table | [bdev.md#SP_bdev_debug_aio_suicide_timeout](../../../config/global/bdev.md#SP_bdev_debug_aio_suicide_timeout) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_debug_aio_suicide_timeout 1_min
ceph config get global bdev_debug_aio_suicide_timeout
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_min`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_debug_discard_sleep

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [bdev.md#SP_bdev_debug_discard_sleep](../../../config/global/bdev.md#SP_bdev_debug_discard_sleep) |

**What it does:** A debugging tool to simulate slow discard operations by introducing a delay of `bdev_debug_discard_sleep` milliseconds

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_debug_discard_sleep 64
ceph config get global bdev_debug_discard_sleep
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_debug_inflight_ios

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [bdev.md#SP_bdev_debug_inflight_ios](../../../config/global/bdev.md#SP_bdev_debug_inflight_ios) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_debug_inflight_ios true
ceph config get global bdev_debug_inflight_ios
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_discard_max_bytes

| | |
|---|---|
| Type | Size · default `10_G` · **Advanced** |
| Table | [bdev.md#SP_bdev_discard_max_bytes](../../../config/global/bdev.md#SP_bdev_discard_max_bytes) |

**What it does:** Discard queue size in bytes that triggers health warning This parameter sets a threshold for the discard queue size (in bytes), triggering a health warning when the queue exceeds the specified limit. This is particularly useful for devices with slow discard operations, as a large backlog in the queue can block disk space that is marked as free but not yet available for allocation, impacting system performance and storage efficiency. `bdev_async_discard_max_pending` is measured in items, not bytes, so its value does not directly correspond to the discard queue size in bytes.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`bdev_async_discard_max_pending`](../../../config/global/bdev.md#SP_bdev_async_discard_max_pending)

**Example:**

```bash
ceph config set global bdev_discard_max_bytes 10_G
ceph config get global bdev_discard_max_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_G`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_discard_max_bytes
ceph -s
```

---

### bdev_enable_discard

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_enable_discard](../../../config/global/bdev.md#SP_bdev_enable_discard) |

**What it does:** Enable OSD devices trimming during in runtime

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_enable_discard true
ceph config get global bdev_enable_discard
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_enable_discard
ceph -s
```

---

### bdev_flock_retry

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [bdev.md#SP_bdev_flock_retry](../../../config/global/bdev.md#SP_bdev_flock_retry) |

**What it does:** times to retry the flock The number of times to retry on getting the block device lock. Programs such as systemd-udevd may compete with Ceph for this lock. 0 means 'unlimited'.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_flock_retry 3
ceph config get global bdev_flock_retry
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_flock_retry
ceph -s
```

---

### bdev_flock_retry_interval

| | |
|---|---|
| Type | Float · default `0.1` · **Advanced** |
| Table | [bdev.md#SP_bdev_flock_retry_interval](../../../config/global/bdev.md#SP_bdev_flock_retry_interval) |

**What it does:** Interval after which to retry flock

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global bdev_flock_retry_interval 0.1
ceph config get global bdev_flock_retry_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_flock_retry_interval
ceph -s
```

---

### bdev_inject_crash

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [bdev.md#SP_bdev_inject_crash](../../../config/global/bdev.md#SP_bdev_inject_crash) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_inject_crash 64
ceph config get global bdev_inject_crash
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_inject_crash_flush_delay

| | |
|---|---|
| Type | Int · default `2` · **Dev** |
| Table | [bdev.md#SP_bdev_inject_crash_flush_delay](../../../config/global/bdev.md#SP_bdev_inject_crash_flush_delay) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global bdev_inject_crash_flush_delay 2
ceph config get global bdev_inject_crash_flush_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### bdev_ioring

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_ioring](../../../config/global/bdev.md#SP_bdev_ioring) |

**What it does:** Enables the Linux io_uring API instead of libaio

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_ioring true
ceph config get global bdev_ioring
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_ioring
ceph -s
```

---

### bdev_ioring_hipri

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_ioring_hipri](../../../config/global/bdev.md#SP_bdev_ioring_hipri) |

**What it does:** Enables Linux io_uring API Use polled IO completions

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_ioring_hipri true
ceph config get global bdev_ioring_hipri
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_ioring_hipri
ceph -s
```

---

### bdev_ioring_sqthread_poll

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_ioring_sqthread_poll](../../../config/global/bdev.md#SP_bdev_ioring_sqthread_poll) |

**What it does:** Enables Linux io_uring API Offload submission/completion to kernel thread

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_ioring_sqthread_poll true
ceph config get global bdev_ioring_sqthread_poll
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_ioring_sqthread_poll
ceph -s
```

---

### bdev_max_discard_length

| | |
|---|---|
| Type | Uint · default `2147483648` · **Advanced** |
| Table | [bdev.md#SP_bdev_max_discard_length](../../../config/global/bdev.md#SP_bdev_max_discard_length) |

**What it does:** Maximum length of a single discard request

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`bdev_enable_discard`](../../../config/global/bdev.md#SP_bdev_enable_discard)

**Example:**

```bash
ceph config set global bdev_max_discard_length 2147483648
ceph config get global bdev_max_discard_length
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2147483648`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_max_discard_length
ceph -s
```

---

### bdev_nvme_unbind_from_kernel

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [bdev.md#SP_bdev_nvme_unbind_from_kernel](../../../config/global/bdev.md#SP_bdev_nvme_unbind_from_kernel) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global bdev_nvme_unbind_from_kernel true
ceph config get global bdev_nvme_unbind_from_kernel
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_nvme_unbind_from_kernel
ceph -s
```

---

### bdev_read_buffer_alignment

| | |
|---|---|
| Type | Size · default `4_K` · **Advanced** |
| Table | [bdev.md#SP_bdev_read_buffer_alignment](../../../config/global/bdev.md#SP_bdev_read_buffer_alignment) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_read_buffer_alignment 4_K
ceph config get global bdev_read_buffer_alignment
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_read_buffer_alignment
ceph -s
```

---

### bdev_read_preallocated_huge_buffers

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [bdev.md#SP_bdev_read_preallocated_huge_buffers](../../../config/global/bdev.md#SP_bdev_read_preallocated_huge_buffers) |

**What it does:** description of pools arrangement for huge page-based read buffers Arrangement of preallocated, huge pages-based pools for reading from a KernelDevice. Applied to minimize size of scatter-gather lists sent to NICs. Targets really big buffers (>= 2 or 4 MBs). Keep in mind the system must be configured accordingly (see /proc/sys/vm/nr_hugepages). Otherwise the OSD wil fail early. Beware that BlueStore, by default, stores large chunks across many smaller blobs. Increasing bluestore_max_blob_size changes that, and thus allows the data to be read back into small number of huge page-backed buffers.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_read_preallocated_huge_buffers "example"
ceph config get global bdev_read_preallocated_huge_buffers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_read_preallocated_huge_buffers
ceph -s
```

---

### bdev_stalled_read_warn_lifetime

| | |
|---|---|
| Type | Uint · default `86400` · **Advanced** |
| Table | [bdev.md#SP_bdev_stalled_read_warn_lifetime](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_lifetime) |

**What it does:** A configurable duration for a stalled read warning to be raised when the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_stalled_read_warn_lifetime 86400
ceph config get global bdev_stalled_read_warn_lifetime
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `86400`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_stalled_read_warn_lifetime
ceph -s
```

---

### bdev_stalled_read_warn_threshold

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [bdev.md#SP_bdev_stalled_read_warn_threshold](../../../config/global/bdev.md#SP_bdev_stalled_read_warn_threshold) |

**What it does:** A configurable number for stalled read warnings to be raised if the number of stalled reads passes the `bdev_stalled_read_warn_threshold` in `bdev_stalled_read_warn_lifetime` seconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_stalled_read_warn_threshold 1
ceph config get global bdev_stalled_read_warn_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_stalled_read_warn_threshold
ceph -s
```

---

### bdev_type

| | |
|---|---|
| Type | Str · enum: ["aio", "spdk", "pmem"] · default `(empty)` · **Advanced** |
| Table | [bdev.md#SP_bdev_type](../../../config/global/bdev.md#SP_bdev_type) |

**What it does:** Explicitly set the device type to select the driver if needed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global bdev_type "example"
ceph config get global bdev_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global bdev_type
ceph -s
```

---


[← Overview](../OVERVIEW.md)
