# Timeouts & intervals

RGW config deep dive — 8 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_exit_timeout_secs](#rgw_exit_timeout_secs) | `2_min` | Advanced | Performance |
| [rgw_init_timeout](#rgw_init_timeout) | `5_min` | Basic | Performance |
| [rgw_objexp_gc_interval](#rgw_objexp_gc_interval) | `600` | Advanced | Performance |
| [rgw_olh_pending_timeout_sec](#rgw_olh_pending_timeout_sec) | `1_hr` | Dev | Performance |
| [rgw_ratelimit_interval](#rgw_ratelimit_interval) | `60` | Advanced | Performance |
| [rgw_read_through_timeout_ms](#rgw_read_through_timeout_ms) | `10000` | Advanced | Performance |
| [rgw_restore_debug_interval](#rgw_restore_debug_interval) | `-1` | Dev | Dev |
| [rgw_usage_log_tick_interval](#rgw_usage_log_tick_interval) | `30` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_exit_timeout_secs

| | |
|---|---|
| Type | Int · default `2_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_exit_timeout_secs](../../../config/rgw/rgw.md#SP_rgw_exit_timeout_secs) |

**What it does:** RGW shutdown timeout

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_exit_timeout_secs 2_min
ceph config get client.rgw rgw_exit_timeout_secs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `2_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_exit_timeout_secs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_init_timeout

| | |
|---|---|
| Type | Int · default `5_min` · **Basic** |
| Table | [rgw.md#SP_rgw_init_timeout](../../../config/rgw/rgw.md#SP_rgw_init_timeout) |

**What it does:** Initialization timeout

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_init_timeout 5_min
ceph config get client.rgw rgw_init_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `5_min` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_init_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_objexp_gc_interval

| | |
|---|---|
| Type | Uint · default `600` · **Advanced** |
| Table | [rgw.md#SP_rgw_objexp_gc_interval](../../../config/rgw/rgw.md#SP_rgw_objexp_gc_interval) |

**What it does:** Swift objects expirer garbage collector interval

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_objexp_gc_interval 600
ceph config get client.rgw rgw_objexp_gc_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `600` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_objexp_gc_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_olh_pending_timeout_sec

| | |
|---|---|
| Type | Int · default `1_hr` · **Dev** |
| Table | [rgw.md#SP_rgw_olh_pending_timeout_sec](../../../config/rgw/rgw.md#SP_rgw_olh_pending_timeout_sec) |

**What it does:** Max time for pending OLH change to complete

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_olh_pending_timeout_sec 1_hr
ceph config get client.rgw rgw_olh_pending_timeout_sec
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `1_hr` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_olh_pending_timeout_sec
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ratelimit_interval

| | |
|---|---|
| Type | Uint · default `60` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_ratelimit_interval](../../../config/rgw/rgw.md#SP_rgw_ratelimit_interval) |

**What it does:** Time window for rate limiting in seconds

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_ratelimit_interval 60
ceph config get client.rgw rgw_ratelimit_interval
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `60` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_ratelimit_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `1`, max `—`.

---

### rgw_read_through_timeout_ms

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [rgw.md#SP_rgw_read_through_timeout_ms](../../../config/rgw/rgw.md#SP_rgw_read_through_timeout_ms) |

**What it does:** Maximum time in milliseconds for read-through GET requests to wait for cloud object restore completion

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_read_through_timeout_ms 10000
ceph config get client.rgw rgw_read_through_timeout_ms
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_read_through_timeout_ms
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**Bounds:** min `0`, max `—`.

---

### rgw_restore_debug_interval

| | |
|---|---|
| Type | Int · default `-1` · **Dev** |
| Table | [rgw.md#SP_rgw_restore_debug_interval](../../../config/rgw/rgw.md#SP_rgw_restore_debug_interval) |

**What it does:** The number of seconds that simulate one "day" in order to debug RGW CloudRestore. Do *not* modify for a production cluster.

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_restore_debug_interval -1
ceph config get client.rgw rgw_restore_debug_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`-1`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_usage_log_tick_interval

| | |
|---|---|
| Type | Int · default `30` · **Advanced** |
| Table | [rgw.md#SP_rgw_usage_log_tick_interval](../../../config/rgw/rgw.md#SP_rgw_usage_log_tick_interval) |

**What it does:** Number of seconds between usage log flush cycles

**When to use:**

- **Shorten** for fresher stats or faster enforcement.
- **Lengthen** to reduce background sync or GC cost.

**Example:**

```bash
ceph config set client.rgw rgw_usage_log_tick_interval 30
ceph config get client.rgw rgw_usage_log_tick_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `30` balances freshness vs background CPU/network.
2. **Shorten** if stale stats cause late quota enforcement or visible sync lag.
3. **Lengthen** if background sync/GC/LC dominates RGW CPU.

**Signals:** quota overshoot window, multisite lag dashboards, LC backlog.

```bash
ceph config get client.rgw rgw_usage_log_tick_interval
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
