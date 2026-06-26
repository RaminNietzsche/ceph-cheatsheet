# Bucket notifications

RGW config deep dive — 13 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_allow_notification_secrets_in_cleartext](#rgw_allow_notification_secrets_in_cleartext) | `False` | Advanced | Policy |
| [rgw_http_notif_connection_timeout](#rgw_http_notif_connection_timeout) | `5` | Advanced | Performance |
| [rgw_http_notif_max_inflight](#rgw_http_notif_max_inflight) | `8192` | Advanced | Performance |
| [rgw_http_notif_message_timeout](#rgw_http_notif_message_timeout) | `10` | Advanced | Performance |
| [rgw_inject_notify_timeout_probability](#rgw_inject_notify_timeout_probability) | `0` | Dev | Dev |
| [rgw_kafka_connection_idle](#rgw_kafka_connection_idle) | `300` | Advanced | Performance |
| [rgw_kafka_max_batch_size](#rgw_kafka_max_batch_size) | `0` | Advanced | Performance |
| [rgw_kafka_message_timeout](#rgw_kafka_message_timeout) | `5000` | Advanced | Performance |
| [rgw_kafka_sleep_timeout](#rgw_kafka_sleep_timeout) | `10` | Advanced | Performance |
| [rgw_max_notify_retries](#rgw_max_notify_retries) | `10` | Advanced | Policy |
| [rgw_topic_persistency_max_retries](#rgw_topic_persistency_max_retries) | `0` | Advanced | Policy |
| [rgw_topic_persistency_sleep_duration](#rgw_topic_persistency_sleep_duration) | `0` | Advanced | Performance |
| [rgw_topic_persistency_time_to_live](#rgw_topic_persistency_time_to_live) | `0` | Advanced | Performance |

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

### rgw_allow_notification_secrets_in_cleartext

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_allow_notification_secrets_in_cleartext](../../../config/rgw/rgw.md#SP_rgw_allow_notification_secrets_in_cleartext) |

**What it does:** When `true`, allows bucket notification topics with broker passwords/secrets over plain HTTP. Default requires HTTPS for topics with secrets.

**When to use:** Trusted private lab only. **Never** enable on internet-facing or untrusted networks.

**Related options:**

- `rgw_trust_forwarded_https` (if TLS terminates at a proxy)
- [`rgw_trust_forwarded_https`](../../../config/rgw/rgw.md#SP_rgw_trust_forwarded_https)

**Example:**

```bash
ceph config set client.rgw rgw_allow_notification_secrets_in_cleartext true
ceph config get client.rgw rgw_allow_notification_secrets_in_cleartext
```

**Finding optimal value:**

**Tuning model:** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_http_notif_connection_timeout

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_connection_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_connection_timeout) |

**What it does:** This is the maximum time in seconds to connect to an endpoint This is the maximum time in seconds to connect to an endpoint. Delivery error occurs when the message timeout is exceeded. If set to zero the default value of 300 seconds will be used. see https://curl.se/libcurl/c/CURLOPT_CONNECTTIMEOUT.html

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_connection_timeout 5
ceph config get client.rgw rgw_http_notif_connection_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `5` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_http_notif_connection_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_http_notif_max_inflight

| | |
|---|---|
| Type | Uint · default `8192` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_max_inflight](../../../config/rgw/rgw.md#SP_rgw_http_notif_max_inflight) |

**What it does:** This is the maximum number of messages in-flight (across all http endpoints) This is the maximum number of messages in-flight (across all http endpoints). Delivery error (BUSY) occurs when the number of messages is exceeded. If set to zero there is no limit on the number of messages in-flight.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_max_inflight 8192
ceph config get client.rgw rgw_http_notif_max_inflight
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8192`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_http_notif_max_inflight
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_http_notif_message_timeout

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_message_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_message_timeout) |

**What it does:** This is the maximum time in seconds to deliver a notification This is the maximum time in seconds to deliver a notification. Delivery error occurs when the message timeout is exceeded. This value includes the connection time, and hence must be larger than rgw_http_notif_connection_timeout. If set to zero the http client will wait indefinitely. see https://curl.se/libcurl/c/CURLOPT_TIMEOUT.html

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_message_timeout 10
ceph config get client.rgw rgw_http_notif_message_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_http_notif_message_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_inject_notify_timeout_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_inject_notify_timeout_probability](../../../config/rgw/rgw.md#SP_rgw_inject_notify_timeout_probability) |

**What it does:** Likelihood of ignoring a notify This is the probability that the RGW cache will ignore a cache notify message. It exists to help with the development and testing of cache consistency and recovery improvements. Please do not set it in a production cluster, as it actively causes failures. Set this to a floating point value between 0 and 1.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_inject_notify_timeout_probability 0
ceph config get client.rgw rgw_inject_notify_timeout_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_kafka_connection_idle

| | |
|---|---|
| Type | Uint · default `300` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_connection_idle](../../../config/rgw/rgw.md#SP_rgw_kafka_connection_idle) |

**What it does:** Time in seconds to delete idle kafka connections A connection will be considered "idle" if no messages are sent to it for more than the time defined. Note that the connection will not be considered idle, even if it is down, as long as there are attempts to send messages to it.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_connection_idle 300
ceph config get client.rgw rgw_kafka_connection_idle
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `300`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_kafka_connection_idle
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_max_batch_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_max_batch_size](../../../config/rgw/rgw.md#SP_rgw_kafka_max_batch_size) |

**What it does:** This is the maximum size in bytes of a batch of messages sent to kafka This is the maximum size in bytes of a batch of messages sent to kafka. Messages will be sent in batches to improve performance, and this option sets the maximum size of those batches. If set to zero, the value is not set and the default batch size will be used.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_max_batch_size 128
ceph config get client.rgw rgw_kafka_max_batch_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_kafka_max_batch_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_message_timeout

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_message_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_message_timeout) |

**What it does:** This is the maximum time in milliseconds to deliver a message (including retries) Delivery error occurs when the message timeout is exceeded. Value must be greater than zero, if set to zero, a value of 1 millisecond will be used.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_message_timeout 5000
ceph config get client.rgw rgw_kafka_message_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `5000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_kafka_message_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_kafka_sleep_timeout

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_sleep_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_sleep_timeout) |

**What it does:** Time in milliseconds to sleep while polling for kafka replies This will be used to prevent busy waiting for the kafka replies As well as for the cases where the broker is down and we try to reconnect. The same values times 3 will be used to sleep if there were no messages sent or received across all kafka connections

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_sleep_timeout 10
ceph config get client.rgw rgw_kafka_sleep_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_kafka_sleep_timeout
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_max_notify_retries

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_notify_retries](../../../config/rgw/rgw.md#SP_rgw_max_notify_retries) |

**What it does:** Number of attempts to notify peers before giving up. The number of times we will attempt to update a peer's cache in the event of error before giving up. This is unlikely to be an issue unless your cluster is very heavily loaded. Beware that increasing this value may cause some operations to take longer in exceptional cases and thus may, rarely, cause clients to time out.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_notify_retries 10
ceph config get client.rgw rgw_max_notify_retries
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `10` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_max_retries

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_max_retries](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_max_retries) |

**What it does:** The maximum number sending a persistent notification would be tried. Note that the value of one would mean no retries, and the value of zero would mean that the notification would be tried indefinitely

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_max_retries 128
ceph config get client.rgw rgw_topic_persistency_max_retries
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_sleep_duration

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_sleep_duration](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_sleep_duration) |

**What it does:** The minimum time (in seconds) between two tries of the same persistent notification. note that the actual time between the tries may be longer

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_sleep_duration 0
ceph config get client.rgw rgw_topic_persistency_sleep_duration
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_topic_persistency_sleep_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_topic_persistency_time_to_live

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_time_to_live](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_time_to_live) |

**What it does:** The rgw retention of persistent topics by time (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_time_to_live 0
ceph config get client.rgw rgw_topic_persistency_time_to_live
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_topic_persistency_time_to_live
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
