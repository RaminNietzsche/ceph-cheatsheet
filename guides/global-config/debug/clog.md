# Clog

Global config deep dive — 7 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [clog_to_graylog](#clog_to_graylog) | `false` | Advanced | Performance |
| [clog_to_graylog_host](#clog_to_graylog_host) | `127.0.0.1` | Advanced | Performance |
| [clog_to_graylog_port](#clog_to_graylog_port) | `12201` | Advanced | Performance |
| [clog_to_monitors](#clog_to_monitors) | `default=true` | Advanced | Performance |
| [clog_to_syslog](#clog_to_syslog) | `false` | Advanced | Performance |
| [clog_to_syslog_facility](#clog_to_syslog_facility) | `default=daemon audit=local0` | Advanced | Performance |
| [clog_to_syslog_level](#clog_to_syslog_level) | `info` | Advanced | Performance |

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

### clog_to_graylog

| | |
|---|---|
| Type | Str · default `false` · **Advanced** |
| Table | [clog.md#SP_clog_to_graylog](../../../config/global/clog.md#SP_clog_to_graylog) |

**What it does:** Make daemons send cluster log to graylog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_graylog false
ceph config get global clog_to_graylog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `false`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_graylog
ceph -s
```

---

### clog_to_graylog_host

| | |
|---|---|
| Type | Str · default `127.0.0.1` · **Advanced** |
| Table | [clog.md#SP_clog_to_graylog_host](../../../config/global/clog.md#SP_clog_to_graylog_host) |

**What it does:** Graylog host to cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_graylog_host "127.0.0.1"
ceph config get global clog_to_graylog_host
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `127.0.0.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_graylog_host
ceph -s
```

---

### clog_to_graylog_port

| | |
|---|---|
| Type | Str · default `12201` · **Advanced** |
| Table | [clog.md#SP_clog_to_graylog_port](../../../config/global/clog.md#SP_clog_to_graylog_port) |

**What it does:** Graylog port number for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_graylog_port 12201
ceph config get global clog_to_graylog_port
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `12201`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_graylog_port
ceph -s
```

---

### clog_to_monitors

| | |
|---|---|
| Type | Str · default `default=true` · **Advanced** |
| Table | [clog.md#SP_clog_to_monitors](../../../config/global/clog.md#SP_clog_to_monitors) |

**What it does:** Make daemons send cluster log messages to monitors

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_monitors "default=true"
ceph config get global clog_to_monitors
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default=true`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_monitors
ceph -s
```

---

### clog_to_syslog

| | |
|---|---|
| Type | Str · default `false` · **Advanced** |
| Table | [clog.md#SP_clog_to_syslog](../../../config/global/clog.md#SP_clog_to_syslog) |

**What it does:** Make daemons send cluster log messages to syslog

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_syslog false
ceph config get global clog_to_syslog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `false`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_syslog
ceph -s
```

---

### clog_to_syslog_facility

| | |
|---|---|
| Type | Str · default `default=daemon audit=local0` · **Advanced** |
| Table | [clog.md#SP_clog_to_syslog_facility](../../../config/global/clog.md#SP_clog_to_syslog_facility) |

**What it does:** Syslog facility for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_syslog_facility "default=daemon audit=local0"
ceph config get global clog_to_syslog_facility
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `default=daemon audit=local0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_syslog_facility
ceph -s
```

---

### clog_to_syslog_level

| | |
|---|---|
| Type | Str · default `info` · **Advanced** |
| Table | [clog.md#SP_clog_to_syslog_level](../../../config/global/clog.md#SP_clog_to_syslog_level) |

**What it does:** Syslog level for cluster log messages

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global clog_to_syslog_level info
ceph config get global clog_to_syslog_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `info`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global clog_to_syslog_level
ceph -s
```

---


[← Overview](../OVERVIEW.md)
