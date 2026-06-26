# Auth & capabilities

MDS config deep dive — 12 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mds_cache_quiesce_splitauth](#mds_cache_quiesce_splitauth) | `True` | Advanced | Policy |
| [mds_cap_acquisition_throttle_retry_request_timeout](#mds_cap_acquisition_throttle_retry_request_timeout) | `0.5` | Advanced | Performance |
| [mds_cap_revoke_eviction_timeout](#mds_cap_revoke_eviction_timeout) | `0` | Advanced | Performance |
| [mds_debug_auth_pins](#mds_debug_auth_pins) | `False` | Dev | Dev |
| [mds_forward_all_requests_to_auth](#mds_forward_all_requests_to_auth) | `False` | Advanced | Policy |
| [mds_max_caps_per_client](#mds_max_caps_per_client) | `1_M` | Advanced | Performance |
| [mds_min_caps_per_client](#mds_min_caps_per_client) | `100` | Advanced | Performance |
| [mds_min_caps_working_set](#mds_min_caps_working_set) | `10000` | Advanced | Performance |
| [mds_recall_max_caps](#mds_recall_max_caps) | `30000` | Advanced | Performance |
| [mds_session_cap_acquisition_decay_rate](#mds_session_cap_acquisition_decay_rate) | `30` | Advanced | Performance |
| [mds_session_cap_acquisition_throttle](#mds_session_cap_acquisition_throttle) | `100000` | Advanced | Performance |
| [mds_session_max_caps_throttle_ratio](#mds_session_max_caps_throttle_ratio) | `1.1` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_cache_quiesce_splitauth

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mds.md#SP_mds_cache_quiesce_splitauth](../../../config/mds/mds.md#SP_mds_cache_quiesce_splitauth) |

**What it does:** Allow recursive quiesce across auth boundaries

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mds mds_cache_quiesce_splitauth false
ceph config get mds mds_cache_quiesce_splitauth
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_cache_quiesce_splitauth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_acquisition_throttle_retry_request_timeout

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout](../../../config/mds/mds.md#SP_mds_cap_acquisition_throttle_retry_request_timeout) |

**What it does:** Timeout in seconds after which a client request is retried due to cap acquisition throttling

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_cap_acquisition_throttle_retry_request_timeout 0.5
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_cap_acquisition_throttle_retry_request_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_cap_revoke_eviction_timeout

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [mds.md#SP_mds_cap_revoke_eviction_timeout](../../../config/mds/mds.md#SP_mds_cap_revoke_eviction_timeout) |

**What it does:** Seconds to wait before evicting a client that holds caps after revoke.

**When to use:** Increase for legacy clients that respond slowly to cap revokes; decrease to reclaim metadata cache faster.

**Example:**

```bash
ceph config set mds mds_cap_revoke_eviction_timeout 0
ceph config get mds mds_cap_revoke_eviction_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_cap_revoke_eviction_timeout
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_debug_auth_pins

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_debug_auth_pins](../../../config/mds/mds.md#SP_mds_debug_auth_pins) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_debug_auth_pins true
ceph config get mds mds_debug_auth_pins
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_forward_all_requests_to_auth

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mds.md#SP_mds_forward_all_requests_to_auth](../../../config/mds/mds.md#SP_mds_forward_all_requests_to_auth) |

**What it does:** always process op on auth mds

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mds mds_forward_all_requests_to_auth true
ceph config get mds mds_forward_all_requests_to_auth
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_forward_all_requests_to_auth
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_max_caps_per_client

| | |
|---|---|
| Type | Uint · default `1_M` · **Advanced** |
| Table | [mds.md#SP_mds_max_caps_per_client](../../../config/mds/mds.md#SP_mds_max_caps_per_client) |

**What it does:** maximum number of capabilities a client may hold

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_max_caps_per_client 1_M
ceph config get mds mds_max_caps_per_client
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_max_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_per_client

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [mds.md#SP_mds_min_caps_per_client](../../../config/mds/mds.md#SP_mds_min_caps_per_client) |

**What it does:** minimum number of capabilities a client may hold

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_min_caps_per_client 100
ceph config get mds mds_min_caps_per_client
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_min_caps_per_client
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_min_caps_working_set

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [mds.md#SP_mds_min_caps_working_set](../../../config/mds/mds.md#SP_mds_min_caps_working_set) |

**What it does:** number of capabilities a client may hold without cache pressure warnings generated

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_min_caps_working_set 10000
ceph config get mds mds_min_caps_working_set
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_min_caps_working_set
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_recall_max_caps

| | |
|---|---|
| Type | Size · default `30000` · **Advanced** |
| Table | [mds.md#SP_mds_recall_max_caps](../../../config/mds/mds.md#SP_mds_recall_max_caps) |

**What it does:** Maximum number of caps to recall from a client session in single recall. Note that this is an integer, though the default value may be displayed with a B suffix.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_recall_max_caps 30000
ceph config get mds mds_recall_max_caps
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_recall_max_caps
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_decay_rate

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [mds.md#SP_mds_session_cap_acquisition_decay_rate](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_decay_rate) |

**What it does:** Decay rate for session readdir caps leading to readdir throttle The half-life for the session cap acquisition counter of caps acquired by readdir. This is used for throttling readdir requests from clients.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_session_cap_acquisition_decay_rate 30
ceph config get mds mds_session_cap_acquisition_decay_rate
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_session_cap_acquisition_decay_rate
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_cap_acquisition_throttle

| | |
|---|---|
| Type | Uint · default `100000` · **Advanced** |
| Table | [mds.md#SP_mds_session_cap_acquisition_throttle](../../../config/mds/mds.md#SP_mds_session_cap_acquisition_throttle) |

**What it does:** Throttle cap acquisition rate per client session to protect the MDS.

**When to use:** Tune when clients stampede caps after MDS restart or when many small files are opened concurrently.

**Example:**

```bash
ceph config set mds mds_session_cap_acquisition_throttle 100000
ceph config get mds mds_session_cap_acquisition_throttle
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_session_cap_acquisition_throttle
ceph -s
ceph fs status
ceph mds stat
```

---

### mds_session_max_caps_throttle_ratio

| | |
|---|---|
| Type | Float · default `1.1` · **Advanced** |
| Table | [mds.md#SP_mds_session_max_caps_throttle_ratio](../../../config/mds/mds.md#SP_mds_session_max_caps_throttle_ratio) |

**What it does:** Ratio of mds_max_caps_per_client that client must exceed before readdir may be throttled by cap acquisition throttle

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mds mds_session_max_caps_throttle_ratio 1.1
ceph config get mds mds_session_max_caps_throttle_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mds mds_session_max_caps_throttle_ratio
ceph -s
ceph fs status
ceph mds stat
```

---


[← Overview](../OVERVIEW.md)
