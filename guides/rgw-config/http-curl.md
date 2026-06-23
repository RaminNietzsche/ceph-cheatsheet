# HTTP / libcurl

RGW config deep dive — 5 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_curl_buffersize](#rgw_curl_buffersize) | `524288` | Dev |
| [rgw_curl_low_speed_limit](#rgw_curl_low_speed_limit) | `1024` | Advanced |
| [rgw_curl_low_speed_time](#rgw_curl_low_speed_time) | `5_min` | Advanced |
| [rgw_curl_tcp_keepalive](#rgw_curl_tcp_keepalive) | `0` | Advanced |
| [rgw_curl_wait_timeout_ms](#rgw_curl_wait_timeout_ms) | `1000` | Dev |

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

**Finding optimal value:** Keep the upstream default (`524288`) in production. Enable or change only during targeted debugging sessions.

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

**Finding optimal value:** Start from upstream default (`1024`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

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

**Finding optimal value:** Start from upstream default (`5_min`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_curl_tcp_keepalive

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_curl_tcp_keepalive](../../config/rgw/rgw.md#SP_rgw_curl_tcp_keepalive) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_curl_tcp_keepalive 0
ceph config get client.rgw rgw_curl_tcp_keepalive
```

**Finding optimal value:** Choose from valid values ["0", "1"]. Default `0` is optimal unless your backend or integration requires another value.

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

**Finding optimal value:** Keep the upstream default (`1000`) in production. Enable or change only during targeted debugging sessions.

---


[← RGW config overview](OVERVIEW.md)
