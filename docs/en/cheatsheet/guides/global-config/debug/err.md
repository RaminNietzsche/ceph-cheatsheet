# Err

Global config deep dive — 4 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [err_to_graylog](#err_to_graylog) | `False` | Basic | Policy |
| [err_to_journald](#err_to_journald) | `False` | Basic | Policy |
| [err_to_stderr](#err_to_stderr) | `True` | Basic | Policy |
| [err_to_syslog](#err_to_syslog) | `False` | Basic | Policy |

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

### err_to_graylog

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [err.md#SP_err_to_graylog](../../../config/global/err.md#SP_err_to_graylog) |

**What it does:** Send critical error log lines to remote Graylog server

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global err_to_graylog true
ceph config get global err_to_graylog
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global err_to_graylog
ceph -s
```

---

### err_to_journald

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [err.md#SP_err_to_journald](../../../config/global/err.md#SP_err_to_journald) |

**What it does:** Send critical error log lines to journald

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global err_to_journald true
ceph config get global err_to_journald
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global err_to_journald
ceph -s
```

---

### err_to_stderr

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [err.md#SP_err_to_stderr](../../../config/global/err.md#SP_err_to_stderr) |

**What it does:** send critical error log lines to stderr

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global err_to_stderr false
ceph config get global err_to_stderr
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global err_to_stderr
ceph -s
```

---

### err_to_syslog

| | |
|---|---|
| Type | Bool · default `False` · **Basic** |
| Table | [err.md#SP_err_to_syslog](../../../config/global/err.md#SP_err_to_syslog) |

**What it does:** Send critical error log lines to syslog facility

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global err_to_syslog true
ceph config get global err_to_syslog
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global err_to_syslog
ceph -s
```

---


[← Overview](../OVERVIEW.md)
