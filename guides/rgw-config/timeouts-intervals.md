# Timeouts and intervals

RGW config deep dive — 8 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_exit_timeout_secs](#rgw_exit_timeout_secs) | `2_min` | Advanced |
| [rgw_init_timeout](#rgw_init_timeout) | `5_min` | Basic |
| [rgw_objexp_gc_interval](#rgw_objexp_gc_interval) | `600` | Advanced |
| [rgw_olh_pending_timeout_sec](#rgw_olh_pending_timeout_sec) | `1_hr` | Dev |
| [rgw_ratelimit_interval](#rgw_ratelimit_interval) | `60` | Advanced |
| [rgw_read_through_timeout_ms](#rgw_read_through_timeout_ms) | `10000` | Advanced |
| [rgw_restore_debug_interval](#rgw_restore_debug_interval) | `-1` | Dev |
| [rgw_usage_log_tick_interval](#rgw_usage_log_tick_interval) | `30` | Advanced |

---

### rgw_exit_timeout_secs

| | |
|---|---|
| Type | Int · default `2_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_exit_timeout_secs](../../config/rgw/rgw.md#SP_rgw_exit_timeout_secs) |

**What it does:** RGW shutdown timeout

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_exit_timeout_secs 2_min
ceph config get client.rgw rgw_exit_timeout_secs
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`2_min`) matches typical LAN latency.

---

### rgw_init_timeout

| | |
|---|---|
| Type | Int · default `5_min` · **Basic** |
| Table | [rgw.md#SP_rgw_init_timeout](../../config/rgw/rgw.md#SP_rgw_init_timeout) |

**What it does:** Initialization timeout

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_init_timeout 5_min
ceph config get client.rgw rgw_init_timeout
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`5_min`) matches typical LAN latency.

---

### rgw_objexp_gc_interval

| | |
|---|---|
| Type | Uint · default `600` · **Advanced** |
| Table | [rgw.md#SP_rgw_objexp_gc_interval](../../config/rgw/rgw.md#SP_rgw_objexp_gc_interval) |

**What it does:** Swift objects expirer garbage collector interval

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_objexp_gc_interval 600
ceph config get client.rgw rgw_objexp_gc_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`600`) only when logs show sync, cache, or timeout issues.

---

### rgw_olh_pending_timeout_sec

| | |
|---|---|
| Type | Int · default `1_hr` · **Dev** |
| Table | [rgw.md#SP_rgw_olh_pending_timeout_sec](../../config/rgw/rgw.md#SP_rgw_olh_pending_timeout_sec) |

**What it does:** Max time for pending OLH change to complete

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_olh_pending_timeout_sec 1_hr
ceph config get client.rgw rgw_olh_pending_timeout_sec
```

**Finding optimal value:** Keep the upstream default (`1_hr`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_ratelimit_interval

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_ratelimit_interval](../../config/rgw/rgw.md#SP_rgw_ratelimit_interval) |

**What it does:** Time window for rate limiting in seconds

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_ratelimit_interval 60
ceph config get client.rgw rgw_ratelimit_interval
ceph orch restart rgw
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`60`) only when logs show sync, cache, or timeout issues. Valid range: min=1, max=—.

---

### rgw_read_through_timeout_ms

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_read_through_timeout_ms](../../config/rgw/rgw.md#SP_rgw_read_through_timeout_ms) |

**What it does:** Maximum time in milliseconds for read-through GET requests to wait for cloud object restore completion

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_read_through_timeout_ms 10000
ceph config get client.rgw rgw_read_through_timeout_ms
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`10000`) matches typical LAN latency. Valid range: min=0, max=—.

---

### rgw_restore_debug_interval

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [rgw.md#SP_rgw_restore_debug_interval](../../config/rgw/rgw.md#SP_rgw_restore_debug_interval) |

**What it does:** The number of seconds that simulate one "day" in order to debug RGW CloudRestore. Do *not* modify for a production cluster.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_restore_debug_interval -1
ceph config get client.rgw rgw_restore_debug_interval
```

**Finding optimal value:** Keep the upstream default (`-1`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_usage_log_tick_interval

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_tick_interval](../../config/rgw/rgw.md#SP_rgw_usage_log_tick_interval) |

**What it does:** Number of seconds between usage log flush cycles

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_tick_interval 30
ceph config get client.rgw rgw_usage_log_tick_interval
```

**Finding optimal value:** Lower for fresher behavior / faster reaction; higher to reduce background load. Adjust from default (`30`) only when logs show sync, cache, or timeout issues.

---


[← RGW config overview](OVERVIEW.md)
