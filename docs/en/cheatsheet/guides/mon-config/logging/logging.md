# Cluster logging

MON config deep dive — 20 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_cluster_log_file](#mon_cluster_log_file) | `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` | Advanced | Capacity |
| [mon_cluster_log_level](#mon_cluster_log_level) | `debug` | Advanced | Performance |
| [mon_cluster_log_to_file](#mon_cluster_log_to_file) | `True` | Advanced | Capacity |
| [mon_cluster_log_to_graylog](#mon_cluster_log_to_graylog) | `false` | Advanced | Performance |
| [mon_cluster_log_to_graylog_host](#mon_cluster_log_to_graylog_host) | `127.0.0.1` | Advanced | Performance |
| [mon_cluster_log_to_graylog_port](#mon_cluster_log_to_graylog_port) | `12201` | Advanced | Performance |
| [mon_cluster_log_to_journald](#mon_cluster_log_to_journald) | `false` | Advanced | Performance |
| [mon_cluster_log_to_stderr](#mon_cluster_log_to_stderr) | `False` | Advanced | Performance |
| [mon_cluster_log_to_syslog](#mon_cluster_log_to_syslog) | `default=false` | Advanced | Performance |
| [mon_cluster_log_to_syslog_facility](#mon_cluster_log_to_syslog_facility) | `daemon` | Advanced | Performance |
| [mon_health_detail_to_clog](#mon_health_detail_to_clog) | `True` | Dev | Dev |
| [mon_health_log_update_period](#mon_health_log_update_period) | `5` | Dev | Dev |
| [mon_health_to_clog](#mon_health_to_clog) | `True` | Advanced | Performance |
| [mon_health_to_clog_interval](#mon_health_to_clog_interval) | `10_min` | Advanced | Performance |
| [mon_health_to_clog_tick_interval](#mon_health_to_clog_tick_interval) | `1_min` | Dev | Dev |
| [mon_log_full_interval](#mon_log_full_interval) | `50` | Advanced | Performance |
| [mon_log_max](#mon_log_max) | `10000` | Advanced | Performance |
| [mon_log_max_summary](#mon_log_max_summary) | `50` | Advanced | Performance |
| [mon_max_log_entries_per_event](#mon_max_log_entries_per_event) | `4096` | Advanced | Performance |
| [mon_op_log_threshold](#mon_op_log_threshold) | `5` | Advanced | Performance |

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

### mon_cluster_log_file

| | |
|---|---|
| Type | Str · default `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_file](../../../config/mon/mon.md#SP_mon_cluster_log_file) |

**What it does:** File(s) to write cluster log to This can either be a simple file name to receive all messages, or a list of key/value pairs where the key is the log channel and the value is the filename, which may include $cluster and $channel metavariables

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_cluster_log_to_file`](../../../config/mon/mon.md#SP_mon_cluster_log_to_file)

**Example:**

```bash
ceph config set mon mon_cluster_log_file "default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log"
ceph config get mon mon_cluster_log_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `default=/var/log/ceph/$cluster.$channel.log cluster=/var/log/ceph/$cluster.log`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_level

| | |
|---|---|
| Type | Str · default `debug` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_level](../../../config/mon/mon.md#SP_mon_cluster_log_level) |

**What it does:** Lowest level to include in cluster log file and/or in external log server Log level to control the cluster log message verbosity for the cluster log file as well as for all external entities.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_cluster_log_file`](../../../config/mon/mon.md#SP_mon_cluster_log_file)

**Example:**

```bash
ceph config set mon mon_cluster_log_level debug
ceph config get mon mon_cluster_log_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `debug`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_level
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_file

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_file](../../../config/mon/mon.md#SP_mon_cluster_log_to_file) |

**What it does:** Make monitor send cluster log messages to file

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`mon_cluster_log_file`](../../../config/mon/mon.md#SP_mon_cluster_log_file)

**Example:**

```bash
ceph config set mon mon_cluster_log_to_file false
ceph config get mon mon_cluster_log_to_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `True`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_file
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog

| | |
|---|---|
| Type | Str · default `false` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_graylog](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog) |

**What it does:** Make monitor send cluster log to graylog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_cluster_log_to_graylog false
ceph config get mon mon_cluster_log_to_graylog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `false`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_graylog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_host

| | |
|---|---|
| Type | Str · default `127.0.0.1` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_graylog_host](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_host) |

**What it does:** Graylog host for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_cluster_log_to_graylog`](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog)

**Example:**

```bash
ceph config set mon mon_cluster_log_to_graylog_host "127.0.0.1"
ceph config get mon mon_cluster_log_to_graylog_host
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_graylog_host
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_graylog_port

| | |
|---|---|
| Type | Str · default `12201` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_graylog_port](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog_port) |

**What it does:** Graylog port for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_cluster_log_to_graylog`](../../../config/mon/mon.md#SP_mon_cluster_log_to_graylog)

**Example:**

```bash
ceph config set mon mon_cluster_log_to_graylog_port 12201
ceph config get mon mon_cluster_log_to_graylog_port
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `12201`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_graylog_port
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_journald

| | |
|---|---|
| Type | Str · default `false` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_journald](../../../config/mon/mon.md#SP_mon_cluster_log_to_journald) |

**What it does:** Make monitor send cluster log to journald

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_cluster_log_to_journald false
ceph config get mon mon_cluster_log_to_journald
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `false`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_journald
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_stderr

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_stderr](../../../config/mon/mon.md#SP_mon_cluster_log_to_stderr) |

**What it does:** Make monitor send cluster log messages to stderr (prefixed by channel)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_cluster_log_to_stderr true
ceph config get mon mon_cluster_log_to_stderr
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_stderr
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog

| | |
|---|---|
| Type | Str · default `default=false` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_syslog](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog) |

**What it does:** Make monitor send cluster log messages to syslog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_cluster_log_to_syslog "default=false"
ceph config get mon mon_cluster_log_to_syslog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default=false`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_syslog
ceph -s
ceph mon stat
```

---

### mon_cluster_log_to_syslog_facility

| | |
|---|---|
| Type | Str · default `daemon` · **Advanced** |
| Table | [mon.md#SP_mon_cluster_log_to_syslog_facility](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog_facility) |

**What it does:** Syslog facility for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_cluster_log_to_syslog`](../../../config/mon/mon.md#SP_mon_cluster_log_to_syslog)

**Example:**

```bash
ceph config set mon mon_cluster_log_to_syslog_facility daemon
ceph config get mon mon_cluster_log_to_syslog_facility
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `daemon`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_cluster_log_to_syslog_facility
ceph -s
ceph mon stat
```

---

### mon_health_detail_to_clog

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [mon.md#SP_mon_health_detail_to_clog](../../../config/mon/mon.md#SP_mon_health_detail_to_clog) |

**What it does:** log health detail to cluster log

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_health_detail_to_clog false
ceph config get mon mon_health_detail_to_clog
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_health_log_update_period

| | |
|---|---|
| Type | Int · default `5` · **Dev** |
| Table | [mon.md#SP_mon_health_log_update_period](../../../config/mon/mon.md#SP_mon_health_log_update_period) |

**What it does:** minimum time in seconds between log messages about each health check

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_health_log_update_period 5
ceph config get mon mon_health_log_update_period
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_health_to_clog

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_health_to_clog](../../../config/mon/mon.md#SP_mon_health_to_clog) |

**What it does:** log monitor health to cluster log

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_health_to_clog false
ceph config get mon mon_health_to_clog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_health_to_clog
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_interval

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [mon.md#SP_mon_health_to_clog_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_interval) |

**What it does:** frequency to log monitor health to cluster log

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Related options:**

- [`mon_health_to_clog`](../../../config/mon/mon.md#SP_mon_health_to_clog)

**Example:**

```bash
ceph config set mon mon_health_to_clog_interval 10_min
ceph config get mon mon_health_to_clog_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_health_to_clog_interval
ceph -s
ceph mon stat
```

---

### mon_health_to_clog_tick_interval

| | |
|---|---|
| Type | Float · default `1_min` · **Dev** |
| Table | [mon.md#SP_mon_health_to_clog_tick_interval](../../../config/mon/mon.md#SP_mon_health_to_clog_tick_interval) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_health_to_clog_tick_interval 1_min
ceph config get mon mon_health_to_clog_tick_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_min`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_log_full_interval

| | |
|---|---|
| Type | Uint · default `50` · **Advanced** |
| Table | [mon.md#SP_mon_log_full_interval](../../../config/mon/mon.md#SP_mon_log_full_interval) |

**What it does:** how many epochs before we encode a full copy of recent log keys

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_log_full_interval 50
ceph config get mon mon_log_full_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_log_full_interval
ceph -s
ceph mon stat
```

---

### mon_log_max

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [mon.md#SP_mon_log_max](../../../config/mon/mon.md#SP_mon_log_max) |

**What it does:** number of recent cluster log messages to retain

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_log_max 10000
ceph config get mon mon_log_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_log_max
ceph -s
ceph mon stat
```

---

### mon_log_max_summary

| | |
|---|---|
| Type | Uint · default `50` · **Advanced** |
| Table | [mon.md#SP_mon_log_max_summary](../../../config/mon/mon.md#SP_mon_log_max_summary) |

**What it does:** number of recent cluster log messages to dedup against

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_log_max_summary 50
ceph config get mon mon_log_max_summary
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `50`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_log_max_summary
ceph -s
ceph mon stat
```

---

### mon_max_log_entries_per_event

| | |
|---|---|
| Type | Int · default `4096` · **Advanced** |
| Table | [mon.md#SP_mon_max_log_entries_per_event](../../../config/mon/mon.md#SP_mon_max_log_entries_per_event) |

**What it does:** max cluster log entries per paxos event

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_log_entries_per_event 4096
ceph config get mon mon_max_log_entries_per_event
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4096`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_log_entries_per_event
ceph -s
ceph mon stat
```

---

### mon_op_log_threshold

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_op_log_threshold](../../../config/mon/mon.md#SP_mon_op_log_threshold) |

**What it does:** max number of slow ops to display

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_op_log_threshold 5
ceph config get mon mon_op_log_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_op_log_threshold
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
