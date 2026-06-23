# Intervals & timeouts

MON config deep dive — 17 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_con_tracker_persist_interval](#mon_con_tracker_persist_interval) | `10` | Advanced | Performance |
| [mon_elector_ping_timeout](#mon_elector_ping_timeout) | `2` | Advanced | Performance |
| [mon_lease_ack_timeout_factor](#mon_lease_ack_timeout_factor) | `2` | Advanced | Performance |
| [mon_lease_renew_interval_factor](#mon_lease_renew_interval_factor) | `0.6` | Advanced | Performance |
| [mon_mds_blocklist_interval](#mon_mds_blocklist_interval) | `1_day` | Dev | Dev |
| [mon_netsplit_grace_period](#mon_netsplit_grace_period) | `9` | Advanced | Performance |
| [mon_nvmeofgw_failback_delay](#mon_nvmeofgw_failback_delay) | `0` | Advanced | Performance |
| [mon_nvmeofgw_skip_failovers_interval](#mon_nvmeofgw_skip_failovers_interval) | `16` | Advanced | Performance |
| [mon_session_timeout](#mon_session_timeout) | `5_min` | Advanced | Performance |
| [mon_smart_report_timeout](#mon_smart_report_timeout) | `5` | Advanced | Performance |
| [mon_subscribe_interval](#mon_subscribe_interval) | `1_day` | Dev | Dev |
| [mon_tick_interval](#mon_tick_interval) | `5` | Advanced | Performance |
| [mon_timecheck_interval](#mon_timecheck_interval) | `5_min` | Advanced | Performance |
| [mon_timecheck_skew_interval](#mon_timecheck_skew_interval) | `30` | Advanced | Performance |
| [mon_use_min_delay_socket](#mon_use_min_delay_socket) | `False` | Advanced | Performance |
| [mon_warn_older_version_delay](#mon_warn_older_version_delay) | `7_day` | Advanced | Performance |
| [nvmeof_mon_client_tick_period](#nvmeof_mon_client_tick_period) | `1` | Advanced | Performance |

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

### mon_con_tracker_persist_interval

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_con_tracker_persist_interval](../../../config/mon/mon.md#SP_mon_con_tracker_persist_interval) |

**What it does:** how many updates the ConnectionTracker takes before it persists to disk

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_con_tracker_persist_interval 10
ceph config get mon mon_con_tracker_persist_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `100000`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_con_tracker_persist_interval
ceph -s
ceph mon stat
```

---

### mon_elector_ping_timeout

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_elector_ping_timeout](../../../config/mon/mon.md#SP_mon_elector_ping_timeout) |

**What it does:** The time after which a ping 'times out' and a connection is considered down

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_elector_ping_timeout 2
ceph config get mon mon_elector_ping_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_elector_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_lease_ack_timeout_factor

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_lease_ack_timeout_factor](../../../config/mon/mon.md#SP_mon_lease_ack_timeout_factor) |

**What it does:** multiple of mon_lease for the lease ack interval before calling new election

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_lease_ack_timeout_factor 2
ceph config get mon mon_lease_ack_timeout_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1.0001`, max `100`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_lease_ack_timeout_factor
ceph -s
ceph mon stat
```

---

### mon_lease_renew_interval_factor

| | |
|---|---|
| Type | Float · default `0.6` · **Advanced** |
| Table | [mon.md#SP_mon_lease_renew_interval_factor](../../../config/mon/mon.md#SP_mon_lease_renew_interval_factor) |

**What it does:** multiple of mon_lease for the lease renewal interval

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_lease_renew_interval_factor 0.6
ceph config get mon mon_lease_renew_interval_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.6`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `0.9999999`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_lease_renew_interval_factor
ceph -s
ceph mon stat
```

---

### mon_mds_blocklist_interval

| | |
|---|---|
| Type | Float · default `1_day` · **Dev** |
| Table | [mon.md#SP_mon_mds_blocklist_interval](../../../config/mon/mon.md#SP_mon_mds_blocklist_interval) |

**What it does:** Duration in seconds that blocklist entries for MDS daemons remain in the OSD map

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_mds_blocklist_interval 1_day
ceph config get mon mon_mds_blocklist_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_day`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_netsplit_grace_period

| | |
|---|---|
| Type | Secs · default `9` · **Advanced** |
| Table | [mon.md#SP_mon_netsplit_grace_period](../../../config/mon/mon.md#SP_mon_netsplit_grace_period) |

**What it does:** Time (in seconds) to wait before emitting a MON_NETSPLIT health warning.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_netsplit_grace_period 9
ceph config get mon mon_netsplit_grace_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `9`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_netsplit_grace_period
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_failback_delay

| | |
|---|---|
| Type | Secs · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_failback_delay](../../../config/mon/mon.md#SP_mon_nvmeofgw_failback_delay) |

**What it does:** Period in seconds to delay HA failback of the gateway

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_failback_delay 0
ceph config get mon mon_nvmeofgw_failback_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_failback_delay
ceph -s
ceph mon stat
```

---

### mon_nvmeofgw_skip_failovers_interval

| | |
|---|---|
| Type | Secs · default `16` · **Advanced** |
| Table | [mon.md#SP_mon_nvmeofgw_skip_failovers_interval](../../../config/mon/mon.md#SP_mon_nvmeofgw_skip_failovers_interval) |

**What it does:** Period in seconds in which no failovers are performed in GW's pool-group this is equal to max GW redeploy interval

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_nvmeofgw_skip_failovers_interval 16
ceph config get mon mon_nvmeofgw_skip_failovers_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `16`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_nvmeofgw_skip_failovers_interval
ceph -s
ceph mon stat
```

---

### mon_session_timeout

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [mon.md#SP_mon_session_timeout](../../../config/mon/mon.md#SP_mon_session_timeout) |

**What it does:** close inactive mon client connections after this many seconds

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_session_timeout 5_min
ceph config get mon mon_session_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_session_timeout
ceph -s
ceph mon stat
```

---

### mon_smart_report_timeout

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_smart_report_timeout](../../../config/mon/mon.md#SP_mon_smart_report_timeout) |

**What it does:** Timeout (in seconds) for smartctl to run, default is set to 5

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_smart_report_timeout 5
ceph config get mon mon_smart_report_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_smart_report_timeout
ceph -s
ceph mon stat
```

---

### mon_subscribe_interval

| | |
|---|---|
| Type | Float · default `1_day` · **Dev** |
| Table | [mon.md#SP_mon_subscribe_interval](../../../config/mon/mon.md#SP_mon_subscribe_interval) |

**What it does:** subscribe interval for pre-jewel clients

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_subscribe_interval 1_day
ceph config get mon mon_subscribe_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1_day`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_tick_interval

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mon.md#SP_mon_tick_interval](../../../config/mon/mon.md#SP_mon_tick_interval) |

**What it does:** interval for internal mon background checks

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_tick_interval 5
ceph config get mon mon_tick_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_tick_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_interval

| | |
|---|---|
| Type | Float · default `5_min` · **Advanced** |
| Table | [mon.md#SP_mon_timecheck_interval](../../../config/mon/mon.md#SP_mon_timecheck_interval) |

**What it does:** frequency of clock synchronization checks between monitors (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_timecheck_interval 5_min
ceph config get mon mon_timecheck_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_timecheck_interval
ceph -s
ceph mon stat
```

---

### mon_timecheck_skew_interval

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [mon.md#SP_mon_timecheck_skew_interval](../../../config/mon/mon.md#SP_mon_timecheck_skew_interval) |

**What it does:** frequency of clock synchronization (re)checks between monitors while clocks are believed to be skewed (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_timecheck_skew_interval 30
ceph config get mon mon_timecheck_skew_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_timecheck_skew_interval
ceph -s
ceph mon stat
```

---

### mon_use_min_delay_socket

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_use_min_delay_socket](../../../config/mon/mon.md#SP_mon_use_min_delay_socket) |

**What it does:** priority packets between mons

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_use_min_delay_socket true
ceph config get mon mon_use_min_delay_socket
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_use_min_delay_socket
ceph -s
ceph mon stat
```

---

### mon_warn_older_version_delay

| | |
|---|---|
| Type | Secs · default `7_day` · **Advanced** |
| Table | [mon.md#SP_mon_warn_older_version_delay](../../../config/mon/mon.md#SP_mon_warn_older_version_delay) |

**What it does:** issue DAEMON_OLD_VERSION health warning after this amount of time has elapsed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_warn_older_version_delay 7_day
ceph config get mon mon_warn_older_version_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7_day`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_older_version_delay
ceph -s
ceph mon stat
```

---

### nvmeof_mon_client_tick_period

| | |
|---|---|
| Type | Secs · default `1` · **Advanced** |
| Table | [mon.md#SP_nvmeof_mon_client_tick_period](../../../config/mon/mon.md#SP_nvmeof_mon_client_tick_period) |

**What it does:** Period in seconds of nvmeof gateway beacon messages to monitor

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon nvmeof_mon_client_tick_period 1
ceph config get mon nvmeof_mon_client_tick_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon nvmeof_mon_client_tick_period
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
