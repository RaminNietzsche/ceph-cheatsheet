# Log

Global config deep dive — 14 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [log_coarse_timestamps](#log_coarse_timestamps) | `True` | Advanced | Performance |
| [log_file](#log_file) | `/var/log/ceph/$cluster-$name.log` | Basic | Capacity |
| [log_flush_on_exit](#log_flush_on_exit) | `False` | Advanced | Performance |
| [log_graylog_host](#log_graylog_host) | `127.0.0.1` | Basic | Policy |
| [log_graylog_port](#log_graylog_port) | `12201` | Basic | Policy |
| [log_max_new](#log_max_new) | `1000` | Advanced | Performance |
| [log_max_recent](#log_max_recent) | `10000` | Advanced | Performance |
| [log_stderr_prefix](#log_stderr_prefix) | `(empty)` | Advanced | Performance |
| [log_stop_at_utilization](#log_stop_at_utilization) | `0.97` | Basic | Policy |
| [log_to_file](#log_to_file) | `True` | Basic | Capacity |
| [log_to_graylog](#log_to_graylog) | `False` | Basic | Policy |
| [log_to_journald](#log_to_journald) | `False` | Basic | Policy |
| [log_to_stderr](#log_to_stderr) | `False` | Basic | Policy |
| [log_to_syslog](#log_to_syslog) | `False` | Basic | Policy |

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

### log_coarse_timestamps

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [log.md#SP_log_coarse_timestamps](../../../config/global/log.md#SP_log_coarse_timestamps) |

**What it does:** Timestamp log entries from coarse system clock to improve performance

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global log_coarse_timestamps false
ceph config get global log_coarse_timestamps
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_coarse_timestamps
ceph -s
```

---

### log_file

| | |
|---|---|
| Type | Str · default `/var/log/ceph/$cluster-$name.log` · **Basic** |
| Table | [log.md#SP_log_file](../../../config/global/log.md#SP_log_file) |

**What it does:** path to log file

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global log_file "/var/log/ceph/$cluster-$name.log"
ceph config get global log_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/var/log/ceph/$cluster-$name.log`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_file
ceph -s
```

---

### log_flush_on_exit

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [log.md#SP_log_flush_on_exit](../../../config/global/log.md#SP_log_flush_on_exit) |

**What it does:** Set a process exit handler to ensure the log is flushed on exit

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global log_flush_on_exit true
ceph config get global log_flush_on_exit
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_flush_on_exit
ceph -s
```

---

### log_graylog_host

| | |
|---|---|
| Type | Str · default `127.0.0.1` · **Basic** |
| Table | [log.md#SP_log_graylog_host](../../../config/global/log.md#SP_log_graylog_host) |

**What it does:** Address or hostname of Graylog server to log to

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global log_graylog_host "127.0.0.1"
ceph config get global log_graylog_host
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `127.0.0.1` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_graylog_host
ceph -s
```

---

### log_graylog_port

| | |
|---|---|
| Type | Int · default `12201` · **Basic** |
| Table | [log.md#SP_log_graylog_port](../../../config/global/log.md#SP_log_graylog_port) |

**What it does:** TCP port number for the remote Graylog server

**When to use:** Core Global behavior — review before changing in production.

**Related options:**

- [`log_graylog_host`](../../../config/global/log.md#SP_log_graylog_host)

**Example:**

```bash
ceph config set global log_graylog_port 12201
ceph config get global log_graylog_port
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `12201` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_graylog_port
ceph -s
```

---

### log_max_new

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [log.md#SP_log_max_new](../../../config/global/log.md#SP_log_max_new) |

**What it does:** Max unwritten log entries to allow before flushing

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`log_max_recent`](../../../config/global/log.md#SP_log_max_recent)

**Example:**

```bash
ceph config set global log_max_new 1000
ceph config get global log_max_new
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_max_new
ceph -s
```

---

### log_max_recent

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [log.md#SP_log_max_recent](../../../config/global/log.md#SP_log_max_recent) |

**What it does:** Recent log entries to keep in memory to dump in the event of a crash The purpose of this option is to log at a higher debug level only to the in-memory buffer, and write out the detailed log messages only if there is a crash. Only log entries below the lower log level will be written unconditionally to the log. For example, debug_osd=1/5 will write everything <= 1 to the log unconditionally but keep entries at levels 2-5 in memory. If there is a seg fault or assertion failure, all entries will be dumped to the log.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global log_max_recent 10000
ceph config get global log_max_recent
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_max_recent
ceph -s
```

---

### log_stderr_prefix

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [log.md#SP_log_stderr_prefix](../../../config/global/log.md#SP_log_stderr_prefix) |

**What it does:** String to prefix log messages with when sent to stderr This is useful in container environments when combined with mon_cluster_log_to_stderr. The mon log prefixes each line with the channel name (e.g., 'default', 'audit'), while log_stderr_prefix can be set to 'debug '.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global log_stderr_prefix "example"
ceph config get global log_stderr_prefix
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_stderr_prefix
ceph -s
```

---

### log_stop_at_utilization

| | |
|---|---|
| Type | Float · default `0.97` · **Basic** |
| Table | [log.md#SP_log_stop_at_utilization](../../../config/global/log.md#SP_log_stop_at_utilization) |

**What it does:** Stop writing to the log file when device utilization reaches this ratio

**When to use:** Core Global behavior — review before changing in production.

**Related options:**

- [`log_file`](../../../config/global/log.md#SP_log_file)

**Example:**

```bash
ceph config set global log_stop_at_utilization 0.97
ceph config get global log_stop_at_utilization
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `0.97` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_stop_at_utilization
ceph -s
```

---

### log_to_file

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [log.md#SP_log_to_file](../../../config/global/log.md#SP_log_to_file) |

**What it does:** send log lines to a file

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`log_file`](../../../config/global/log.md#SP_log_file)

**Example:**

```bash
ceph config set global log_to_file false
ceph config get global log_to_file
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `True`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_to_file
ceph -s
```

---

### log_to_graylog

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [log.md#SP_log_to_graylog](../../../config/global/log.md#SP_log_to_graylog) |

**What it does:** Send log lines to remote Graylog server

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global log_to_graylog true
ceph config get global log_to_graylog
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_to_graylog
ceph -s
```

---

### log_to_journald

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [log.md#SP_log_to_journald](../../../config/global/log.md#SP_log_to_journald) |

**What it does:** Send log lines to journald

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global log_to_journald true
ceph config get global log_to_journald
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_to_journald
ceph -s
```

---

### log_to_stderr

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [log.md#SP_log_to_stderr](../../../config/global/log.md#SP_log_to_stderr) |

**What it does:** send log lines to stderr When Ceph runs as a library (e.g., librados), the default value set to false because stderr may not be writable by the application. For daemons, the daemon_default of false is used instead.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global log_to_stderr true
ceph config get global log_to_stderr
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_to_stderr
ceph -s
```

---

### log_to_syslog

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [log.md#SP_log_to_syslog](../../../config/global/log.md#SP_log_to_syslog) |

**What it does:** Send log lines to syslog facility

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global log_to_syslog true
ceph config get global log_to_syslog
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global log_to_syslog
ceph -s
```

---


[← Overview](../OVERVIEW.md)
