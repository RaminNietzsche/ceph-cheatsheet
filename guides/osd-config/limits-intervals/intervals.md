# Intervals & throttling

OSD config deep dive — 12 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_delete_sleep](#osd_delete_sleep) | `0` | Advanced | Performance |
| [osd_delete_sleep_hdd](#osd_delete_sleep_hdd) | `5` | Advanced | Performance |
| [osd_delete_sleep_hybrid](#osd_delete_sleep_hybrid) | `1` | Advanced | Performance |
| [osd_delete_sleep_ssd](#osd_delete_sleep_ssd) | `1` | Advanced | Performance |
| [osd_max_markdown_period](#osd_max_markdown_period) | `10_min` | Advanced | Performance |
| [osd_op_thread_suicide_timeout](#osd_op_thread_suicide_timeout) | `150` | Advanced | Performance |
| [osd_op_thread_timeout](#osd_op_thread_timeout) | `15` | Advanced | Performance |
| [osd_smart_report_timeout](#osd_smart_report_timeout) | `5` | Advanced | Performance |
| [osd_snap_trim_sleep](#osd_snap_trim_sleep) | `0` | Advanced | Performance |
| [osd_snap_trim_sleep_hdd](#osd_snap_trim_sleep_hdd) | `5` | Advanced | Performance |
| [osd_snap_trim_sleep_hybrid](#osd_snap_trim_sleep_hybrid) | `2` | Advanced | Performance |
| [osd_snap_trim_sleep_ssd](#osd_snap_trim_sleep_ssd) | `0` | Advanced | Performance |

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

### osd_delete_sleep

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_delete_sleep](../../../config/osd/osd.md#SP_osd_delete_sleep) |

**What it does:** Time in seconds to sleep before next removal transaction. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_delete_sleep 0
ceph config get osd osd_delete_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_delete_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_delete_sleep_hdd

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_delete_sleep_hdd](../../../config/osd/osd.md#SP_osd_delete_sleep_hdd) |

**What it does:** Time in seconds to sleep before next removal transaction for HDDs.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_delete_sleep_hdd 5
ceph config get osd osd_delete_sleep_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_delete_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_delete_sleep_hybrid

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_delete_sleep_hybrid](../../../config/osd/osd.md#SP_osd_delete_sleep_hybrid) |

**What it does:** Time in seconds to sleep before next removal transaction when OSD data is on HDD and OSD journal or WAL+DB is on SSD

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_delete_sleep_hybrid 1
ceph config get osd osd_delete_sleep_hybrid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_delete_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_delete_sleep_ssd

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [osd.md#SP_osd_delete_sleep_ssd](../../../config/osd/osd.md#SP_osd_delete_sleep_ssd) |

**What it does:** Time in seconds to sleep before next removal transaction for SSDs

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_delete_sleep_ssd 1
ceph config get osd osd_delete_sleep_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_delete_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_markdown_period

| | |
|---|---|
| Type | Int · default `10_min` · **Advanced** |
| Table | [osd.md#SP_osd_max_markdown_period](../../../config/osd/osd.md#SP_osd_max_markdown_period) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_markdown_period 10_min
ceph config get osd osd_max_markdown_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_markdown_period
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_op_thread_suicide_timeout

| | |
|---|---|
| Type | Int · default `150` · **Advanced** |
| Table | [osd.md#SP_osd_op_thread_suicide_timeout](../../../config/osd/osd.md#SP_osd_op_thread_suicide_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_op_thread_suicide_timeout 150
ceph config get osd osd_op_thread_suicide_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `150`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_thread_suicide_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_op_thread_timeout

| | |
|---|---|
| Type | Int · default `15` · **Advanced** |
| Table | [osd.md#SP_osd_op_thread_timeout](../../../config/osd/osd.md#SP_osd_op_thread_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_op_thread_timeout 15
ceph config get osd osd_op_thread_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_thread_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_smart_report_timeout

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_smart_report_timeout](../../../config/osd/osd.md#SP_osd_smart_report_timeout) |

**What it does:** Timeout (in seconds) for smartctl to run, default is set to 5

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_smart_report_timeout 5
ceph config get osd osd_smart_report_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_smart_report_timeout
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_snap_trim_sleep

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_sleep](../../../config/osd/osd.md#SP_osd_snap_trim_sleep) |

**What it does:** Time in seconds to sleep before next snap trim. This setting overrides _ssd, _hdd, and _hybrid if non-zero.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_snap_trim_sleep 0
ceph config get osd osd_snap_trim_sleep
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_sleep
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_snap_trim_sleep_hdd

| | |
|---|---|
| Type | Float · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_sleep_hdd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hdd) |

**What it does:** Time in seconds to sleep before next snap trim for HDDs

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_snap_trim_sleep_hdd 5
ceph config get osd osd_snap_trim_sleep_hdd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_sleep_hdd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_snap_trim_sleep_hybrid

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_sleep_hybrid](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_hybrid) |

**What it does:** Time in seconds to sleep before next snap trim when data is on HDD and journal is on SSD

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_snap_trim_sleep_hybrid 2
ceph config get osd osd_snap_trim_sleep_hybrid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_sleep_hybrid
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_snap_trim_sleep_ssd

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [osd.md#SP_osd_snap_trim_sleep_ssd](../../../config/osd/osd.md#SP_osd_snap_trim_sleep_ssd) |

**What it does:** Time in seconds to sleep before next snap trim for SSDs

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set osd osd_snap_trim_sleep_ssd 0
ceph config get osd osd_snap_trim_sleep_ssd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_snap_trim_sleep_ssd
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
