# Bucket notifications

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_http_notif_connection_timeout](#rgw_http_notif_connection_timeout) | `5` | Advanced |
| [rgw_http_notif_max_inflight](#rgw_http_notif_max_inflight) | `8192` | Advanced |
| [rgw_http_notif_message_timeout](#rgw_http_notif_message_timeout) | `10` | Advanced |
| [rgw_inject_notify_timeout_probability](#rgw_inject_notify_timeout_probability) | `0` | Dev |
| [rgw_kafka_connection_idle](#rgw_kafka_connection_idle) | `300` | Advanced |
| [rgw_kafka_max_batch_size](#rgw_kafka_max_batch_size) | `0` | Advanced |
| [rgw_kafka_message_timeout](#rgw_kafka_message_timeout) | `5000` | Advanced |
| [rgw_kafka_sleep_timeout](#rgw_kafka_sleep_timeout) | `10` | Advanced |
| [rgw_max_notify_retries](#rgw_max_notify_retries) | `10` | Advanced |
| [rgw_topic_persistency_max_retries](#rgw_topic_persistency_max_retries) | `0` | Advanced |
| [rgw_topic_persistency_sleep_duration](#rgw_topic_persistency_sleep_duration) | `0` | Advanced |
| [rgw_topic_persistency_time_to_live](#rgw_topic_persistency_time_to_live) | `0` | Advanced |

---

### rgw_http_notif_connection_timeout

| | |
|---|---|
| Type | Uint · default `5` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_connection_timeout](../../config/rgw/rgw.md#SP_rgw_http_notif_connection_timeout) |

**What it does:** This is the maximum time in seconds to connect to an endpoint

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_connection_timeout 5
ceph config get client.rgw rgw_http_notif_connection_timeout
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`5`) matches typical LAN latency.

---

### rgw_http_notif_max_inflight

| | |
|---|---|
| Type | Uint · default `8192` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_max_inflight](../../config/rgw/rgw.md#SP_rgw_http_notif_max_inflight) |

**What it does:** This is the maximum number of messages in-flight (across all http endpoints)

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_max_inflight 8192
ceph config get client.rgw rgw_http_notif_max_inflight
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`8192`) matches S3 compatibility for most workloads.

---

### rgw_http_notif_message_timeout

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_http_notif_message_timeout](../../config/rgw/rgw.md#SP_rgw_http_notif_message_timeout) |

**What it does:** This is the maximum time in seconds to deliver a notification

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_http_notif_message_timeout 10
ceph config get client.rgw rgw_http_notif_message_timeout
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`10`) matches typical LAN latency.

---

### rgw_inject_notify_timeout_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_inject_notify_timeout_probability](../../config/rgw/rgw.md#SP_rgw_inject_notify_timeout_probability) |

**What it does:** Likelihood of ignoring a notify

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_inject_notify_timeout_probability 0
ceph config get client.rgw rgw_inject_notify_timeout_probability
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_kafka_connection_idle

| | |
|---|---|
| Type | Uint · default `300` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_connection_idle](../../config/rgw/rgw.md#SP_rgw_kafka_connection_idle) |

**What it does:** Time in seconds to delete idle kafka connections

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_connection_idle 300
ceph config get client.rgw rgw_kafka_connection_idle
```

**Finding optimal value:** Start from upstream default (`300`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_kafka_max_batch_size

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_max_batch_size](../../config/rgw/rgw.md#SP_rgw_kafka_max_batch_size) |

**What it does:** This is the maximum size in bytes of a batch of messages sent to kafka

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_max_batch_size 0
ceph config get client.rgw rgw_kafka_max_batch_size
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`0`) matches S3 compatibility for most workloads.

---

### rgw_kafka_message_timeout

| | |
|---|---|
| Type | Uint · default `5000` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_message_timeout](../../config/rgw/rgw.md#SP_rgw_kafka_message_timeout) |

**What it does:** This is the maximum time in milliseconds to deliver a message (including retries)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_message_timeout 5000
ceph config get client.rgw rgw_kafka_message_timeout
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`5000`) matches typical LAN latency.

---

### rgw_kafka_sleep_timeout

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_kafka_sleep_timeout](../../config/rgw/rgw.md#SP_rgw_kafka_sleep_timeout) |

**What it does:** Time in milliseconds to sleep while polling for kafka replies

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_kafka_sleep_timeout 10
ceph config get client.rgw rgw_kafka_sleep_timeout
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`10`) matches typical LAN latency.

---

### rgw_max_notify_retries

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [rgw.md#SP_rgw_max_notify_retries](../../config/rgw/rgw.md#SP_rgw_max_notify_retries) |

**What it does:** Number of attempts to notify peers before giving up.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_max_notify_retries 10
ceph config get client.rgw rgw_max_notify_retries
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`10`) matches S3 compatibility for most workloads.

---

### rgw_topic_persistency_max_retries

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_max_retries](../../config/rgw/rgw.md#SP_rgw_topic_persistency_max_retries) |

**What it does:** The maximum number sending a persistent notification would be tried. Note that the value of one would mean no retries, and the value of zero would mean that the notification would be tried indefinitely

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_max_retries 0
ceph config get client.rgw rgw_topic_persistency_max_retries
ceph orch restart rgw
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`0`) matches S3 compatibility for most workloads.

---

### rgw_topic_persistency_sleep_duration

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_sleep_duration](../../config/rgw/rgw.md#SP_rgw_topic_persistency_sleep_duration) |

**What it does:** The minimum time (in seconds) between two tries of the same persistent notification. note that the actual time between the tries may be longer

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_sleep_duration 0
ceph config get client.rgw rgw_topic_persistency_sleep_duration
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_topic_persistency_time_to_live

| | |
|---|---|
| Type | Uint · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_topic_persistency_time_to_live](../../config/rgw/rgw.md#SP_rgw_topic_persistency_time_to_live) |

**What it does:** The rgw retention of persistent topics by time (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_topic_persistency_time_to_live 0
ceph config get client.rgw rgw_topic_persistency_time_to_live
ceph orch restart rgw
```

**Finding optimal value:** Start from upstream default (`0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
