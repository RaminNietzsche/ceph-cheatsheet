# HTTP / libcurl

RGW config deep dive — 5 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_curl_buffersize](#rgw_curl_buffersize) | `524288` | Dev | Performance |
| [rgw_curl_low_speed_limit](#rgw_curl_low_speed_limit) | `1024` | Advanced | Policy |
| [rgw_curl_low_speed_time](#rgw_curl_low_speed_time) | `5_min` | Advanced | Performance |
| [rgw_curl_tcp_keepalive](#rgw_curl_tcp_keepalive) | `0` | Advanced | Architecture |
| [rgw_curl_wait_timeout_ms](#rgw_curl_wait_timeout_ms) | `1000` | Dev | Performance |

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

### rgw_curl_buffersize

| | |
|---|---|
| Type | Int · default `524288` · **Dev** |
| Table | [rgw.md#SP_rgw_curl_buffersize](../../config/rgw/rgw.md#SP_rgw_curl_buffersize) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_curl_buffersize 524288
ceph config get client.rgw rgw_curl_buffersize
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `524288`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_buffersize
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

**Bounds:** min `1024`, max `524288`.

---

### rgw_curl_low_speed_limit

| | |
|---|---|
| Type | Int · default `1024` · **Advanced** |
| Table | [rgw.md#SP_rgw_curl_low_speed_limit](../../config/rgw/rgw.md#SP_rgw_curl_low_speed_limit) |

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_curl_low_speed_limit 1024
ceph config get client.rgw rgw_curl_low_speed_limit
```

**Finding optimal value:**

**Tuning model:** Policy

1. Upstream default (`1024`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_curl_low_speed_time

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [rgw.md#SP_rgw_curl_low_speed_time](../../config/rgw/rgw.md#SP_rgw_curl_low_speed_time) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_curl_low_speed_time 5_min
ceph config get client.rgw rgw_curl_low_speed_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_low_speed_time
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_curl_tcp_keepalive

| | |
|---|---|
| Type | Int · enum: ["0", "1"] · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_curl_tcp_keepalive](../../config/rgw/rgw.md#SP_rgw_curl_tcp_keepalive) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_curl_tcp_keepalive 0
ceph config get client.rgw rgw_curl_tcp_keepalive
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Valid values: ["0", "1"].
2. Default `0` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_curl_wait_timeout_ms

| | |
|---|---|
| Type | Int · default `1000` · **Dev** |
| Table | [rgw.md#SP_rgw_curl_wait_timeout_ms](../../config/rgw/rgw.md#SP_rgw_curl_wait_timeout_ms) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_curl_wait_timeout_ms 1000
ceph config get client.rgw rgw_curl_wait_timeout_ms
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `1000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_curl_wait_timeout_ms
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
