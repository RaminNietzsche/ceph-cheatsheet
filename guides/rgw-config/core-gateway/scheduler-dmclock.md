# Scheduler & dmclock

RGW config deep dive — 13 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_dmclock_admin_lim](#rgw_dmclock_admin_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_admin_res](#rgw_dmclock_admin_res) | `100` | Advanced | Performance |
| [rgw_dmclock_admin_wgt](#rgw_dmclock_admin_wgt) | `100` | Advanced | Performance |
| [rgw_dmclock_auth_lim](#rgw_dmclock_auth_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_auth_res](#rgw_dmclock_auth_res) | `200` | Advanced | Performance |
| [rgw_dmclock_auth_wgt](#rgw_dmclock_auth_wgt) | `100` | Advanced | Performance |
| [rgw_dmclock_data_lim](#rgw_dmclock_data_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_data_res](#rgw_dmclock_data_res) | `500` | Advanced | Performance |
| [rgw_dmclock_data_wgt](#rgw_dmclock_data_wgt) | `500` | Advanced | Performance |
| [rgw_dmclock_metadata_lim](#rgw_dmclock_metadata_lim) | `0` | Advanced | Performance |
| [rgw_dmclock_metadata_res](#rgw_dmclock_metadata_res) | `500` | Advanced | Performance |
| [rgw_dmclock_metadata_wgt](#rgw_dmclock_metadata_wgt) | `500` | Advanced | Performance |
| [rgw_scheduler_type](#rgw_scheduler_type) | `throttler` | Advanced | Performance |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_dmclock_admin_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_lim) |

**What it does:** mclock limit for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_lim 0
ceph config get client.rgw rgw_dmclock_admin_lim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_lim
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_res

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_res) |

**What it does:** mclock reservation for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_res 100
ceph config get client.rgw rgw_dmclock_admin_res
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_res
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_admin_wgt

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_admin_wgt) |

**What it does:** mclock weight for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_wgt 100
ceph config get client.rgw rgw_dmclock_admin_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_admin_wgt
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_lim) |

**What it does:** mclock limit for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_lim 0
ceph config get client.rgw rgw_dmclock_auth_lim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_lim
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_res

| | |
|---|---|
| Type | Float · default `200` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_res) |

**What it does:** mclock reservation for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_res 200
ceph config get client.rgw rgw_dmclock_auth_res
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`200`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_res
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_auth_wgt

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_auth_wgt) |

**What it does:** mclock weight for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_wgt 100
ceph config get client.rgw rgw_dmclock_auth_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`100`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_auth_wgt
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_lim) |

**What it does:** mclock limit for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_lim 0
ceph config get client.rgw rgw_dmclock_data_lim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_lim
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_res

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_res) |

**What it does:** mclock reservation for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_res 500
ceph config get client.rgw rgw_dmclock_data_res
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_res
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_data_wgt

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_data_wgt) |

**What it does:** mclock weight for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_wgt 500
ceph config get client.rgw rgw_dmclock_data_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_data_wgt
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_lim](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_lim) |

**What it does:** mclock limit for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_lim 0
ceph config get client.rgw rgw_dmclock_metadata_lim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`0`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_lim
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_res

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_res](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_res) |

**What it does:** mclock reservation for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_res 500
ceph config get client.rgw rgw_dmclock_metadata_res
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_res
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_dmclock_metadata_wgt

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_wgt](../../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_wgt) |

**What it does:** mclock weight for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_wgt 500
ceph config get client.rgw rgw_dmclock_metadata_wgt
```

**Finding optimal value:**

**Tuning model:** Performance

1. Tune reservation (`_res`), limit (`_lim`), and weight (`_wgt`) per queue as a set.
2. Start from defaults (`500`); identify saturated queue (admin/auth/data/metadata).
3. Raise reservation for starved client traffic; lower limit if one queue monopolizes OSD I/O.

**Signals:** dmclock perf counters, queue delay histograms, admin API slowdown.

```bash
ceph config get client.rgw rgw_dmclock_metadata_wgt
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
ceph daemon rgw.<id> perf dump | jq 'to_entries[] | select(.key|test("dmclock"))'
```

---

### rgw_scheduler_type

| | |
|---|---|
| Type | Str · default `throttler` · **Advanced** |
| Table | [rgw.md#SP_rgw_scheduler_type](../../../config/rgw/rgw.md#SP_rgw_scheduler_type) |

**What it does:** Set the type of dmclock scheduler, defaults to throttler. Other valid value is dmclock which is experimental.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_scheduler_type throttler
ceph config get client.rgw rgw_scheduler_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `throttler`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_scheduler_type
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
