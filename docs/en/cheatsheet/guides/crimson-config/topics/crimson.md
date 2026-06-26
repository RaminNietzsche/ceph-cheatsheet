# Crimson OSD

Crimson config deep dive — 14 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/crimson/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [crimson_allow_pg_split](#crimson_allow_pg_split) | `True` | Advanced | Policy |
| [crimson_bluestore_cpu_set](#crimson_bluestore_cpu_set) | `(empty)` | Advanced | Performance |
| [crimson_bluestore_num_threads](#crimson_bluestore_num_threads) | `6` | Advanced | Performance |
| [crimson_cpu_num](#crimson_cpu_num) | `0` | Advanced | Performance |
| [crimson_cpu_set](#crimson_cpu_set) | `(empty)` | Advanced | Performance |
| [crimson_memory](#crimson_memory) | `0` | Advanced | Performance |
| [crimson_osd_obc_lru_size](#crimson_osd_obc_lru_size) | `512` | Advanced | Performance |
| [crimson_osd_scheduler_concurrency](#crimson_osd_scheduler_concurrency) | `0` | Advanced | Performance |
| [crimson_osd_stat_interval](#crimson_osd_stat_interval) | `0` | Advanced | Performance |
| [crimson_poll_mode](#crimson_poll_mode) | `False` | Advanced | Performance |
| [crimson_reactor_backend](#crimson_reactor_backend) | `(empty)` | Advanced | Performance |
| [crimson_reactor_idle_poll_time_us](#crimson_reactor_idle_poll_time_us) | `200` | Advanced | Performance |
| [crimson_reactor_io_latency_goal_ms](#crimson_reactor_io_latency_goal_ms) | `0` | Advanced | Performance |
| [crimson_reactor_task_quota_ms](#crimson_reactor_task_quota_ms) | `0.5` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. crimson
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### crimson_allow_pg_split

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [crimson.md#SP_crimson_allow_pg_split](../../../config/crimson/crimson.md#SP_crimson_allow_pg_split) |

**What it does:** Allow Crimson pools to increase their PG count (split) When enabled, allows the monitor to increase pg_num for pools using the crimson flag.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set osd crimson_allow_pg_split false
ceph config get osd crimson_allow_pg_split
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_allow_pg_split
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_cpu_set

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_bluestore_cpu_set](../../../config/crimson/crimson.md#SP_crimson_bluestore_cpu_set) |

**What it does:** CPU cores on which POSIX threads alienized to seastar will run in cpuset(7) format

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_bluestore_cpu_set "example"
ceph config get osd crimson_bluestore_cpu_set
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_bluestore_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_bluestore_num_threads

| | |
|---|---|
| Type | Uint · default `6` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_bluestore_num_threads](../../../config/crimson/crimson.md#SP_crimson_bluestore_num_threads) |

**What it does:** The number of POSIX threads alienized to seastar for serving Bluestore

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_bluestore_num_threads 6
ceph config get osd crimson_bluestore_num_threads
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_bluestore_num_threads
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_num

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_cpu_num](../../../config/crimson/crimson.md#SP_crimson_cpu_num) |

**What it does:** The number of CPUs to use for serving seastar reactors per OSD without CPU pinning. The number of CPUs to use for serving seastar reactors per OSD without CPU pinning. overridden if crimson_cpu_set is set. smp::count is deduced from this option.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_cpu_num 64
ceph config get osd crimson_cpu_num
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `32`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_cpu_num
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_cpu_set

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_cpu_set](../../../config/crimson/crimson.md#SP_crimson_cpu_set) |

**What it does:** CPU cores on which seastar reactor threads will run in cpuset(7) format per OSD with pinning. CPU cores on which seastar reactor threads will run in cpuset(7) format per OSD with pinning. overrides crimson_cpu_num. smp::count is deduced from this option

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_cpu_set "example"
ceph config get osd crimson_cpu_set
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_cpu_set
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_memory

| | |
|---|---|
| Type | Size · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_memory](../../../config/crimson/crimson.md#SP_crimson_memory) |

**What it does:** Total memory to use for the seastar allocator per OSD. Total memory to use for the seastar allocator per OSD. Maps to seastar's --memory flag. 0 means use seastar's default (all available memory minus a reserve).

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_memory 64
ceph config get osd crimson_memory
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
ceph config get osd crimson_memory
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_obc_lru_size

| | |
|---|---|
| Type | Uint · default `512` · **Advanced** |
| Table | [crimson.md#SP_crimson_osd_obc_lru_size](../../../config/crimson/crimson.md#SP_crimson_osd_obc_lru_size) |

**What it does:** Number of obcs to cache

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_osd_obc_lru_size 512
ceph config get osd crimson_osd_obc_lru_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_osd_obc_lru_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_scheduler_concurrency

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [crimson.md#SP_crimson_osd_scheduler_concurrency](../../../config/crimson/crimson.md#SP_crimson_osd_scheduler_concurrency) |

**What it does:** The maximum number concurrent IO operations, 0 for unlimited

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_osd_scheduler_concurrency 64
ceph config get osd crimson_osd_scheduler_concurrency
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_osd_scheduler_concurrency
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_osd_stat_interval

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [crimson.md#SP_crimson_osd_stat_interval](../../../config/crimson/crimson.md#SP_crimson_osd_stat_interval) |

**What it does:** Report OSD status periodically in seconds, 0 to disable

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd crimson_osd_stat_interval 64
ceph config get osd crimson_osd_stat_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_osd_stat_interval
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_poll_mode

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_poll_mode](../../../config/crimson/crimson.md#SP_crimson_poll_mode) |

**What it does:** Let the seastar reactor poll continuously without sleeping at the expense of 100% cpu usage.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd crimson_poll_mode true
ceph config get osd crimson_poll_mode
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_poll_mode
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_backend

| | |
|---|---|
| Type | Str · enum: ["io_uring", "linux-aio", "epoll"] · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_reactor_backend](../../../config/crimson/crimson.md#SP_crimson_reactor_backend) |

**What it does:** Select which Seastar's internal reactor implementation Controls which asynchronous I/O engine the Seastar reactor will use during OSD startup. Different backends have different performance characteristics and require different kernel capabilities. Note, If none is non is selected, let seastar choose.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_reactor_backend "example"
ceph config get osd crimson_reactor_backend
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_reactor_backend
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_idle_poll_time_us

| | |
|---|---|
| Type | Uint · default `200` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_reactor_idle_poll_time_us](../../../config/crimson/crimson.md#SP_crimson_reactor_idle_poll_time_us) |

**What it does:** Seastar's reactor idle polling time (ms) before going back to sleep. Seastar's reactor idle polling time (ms) before going back to sleep. Longer reactor poll time will result in larger CPU utilization.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_reactor_idle_poll_time_us 200
ceph config get osd crimson_reactor_idle_poll_time_us
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `200`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_reactor_idle_poll_time_us
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_io_latency_goal_ms

| | |
|---|---|
| Type | Float · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_reactor_io_latency_goal_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_io_latency_goal_ms) |

**What it does:** The maximum time (ms) Seastar's reactor IO operations must take. If not set(0 mean not set), defaults to 1.5 * crimson_reactor_task_quota_ms The maximum time (ms) Seastar's reactor IO operations must take. If not set, defaults to 1.5 * crimson_reactor_task_quota_ms. Increasing this value will allow more IO requests to be dispatched concurrently.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_reactor_io_latency_goal_ms 0
ceph config get osd crimson_reactor_io_latency_goal_ms
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
ceph config get osd crimson_reactor_io_latency_goal_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### crimson_reactor_task_quota_ms

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** · **STARTUP** (restart required) |
| Table | [crimson.md#SP_crimson_reactor_task_quota_ms](../../../config/crimson/crimson.md#SP_crimson_reactor_task_quota_ms) |

**What it does:** The maximum time (ms) Seastar reactors will wait between polls. The maximum time (ms) Seastar reactors will wait between polls. Shorter time between pools will result in larger CPU utilization.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set osd crimson_reactor_task_quota_ms 0.5
ceph config get osd crimson_reactor_task_quota_ms
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd crimson_reactor_task_quota_ms
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← Overview](../OVERVIEW.md)
