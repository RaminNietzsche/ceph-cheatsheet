# Bucket notifications

RGW 配置深度指南 — 13 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_allow_notification_secrets_in_cleartext](#rgw_allow_notification_secrets_in_cleartext) | `False` | Advanced | 策略 |
| [rgw_http_notif_connection_timeout](#rgw_http_notif_connection_timeout) | `5` | Advanced | 性能 |
| [rgw_http_notif_max_inflight](#rgw_http_notif_max_inflight) | `8192` | Advanced | 性能 |
| [rgw_http_notif_message_timeout](#rgw_http_notif_message_timeout) | `10` | Advanced | 性能 |
| [rgw_inject_notify_timeout_probability](#rgw_inject_notify_timeout_probability) | `0` | Dev | 开发 |
| [rgw_kafka_connection_idle](#rgw_kafka_connection_idle) | `300` | Advanced | 性能 |
| [rgw_kafka_max_batch_size](#rgw_kafka_max_batch_size) | `0` | Advanced | 性能 |
| [rgw_kafka_message_timeout](#rgw_kafka_message_timeout) | `5000` | Advanced | 性能 |
| [rgw_kafka_sleep_timeout](#rgw_kafka_sleep_timeout) | `10` | Advanced | 性能 |
| [rgw_max_notify_retries](#rgw_max_notify_retries) | `10` | Advanced | 策略 |
| [rgw_topic_persistency_max_retries](#rgw_topic_persistency_max_retries) | `0` | Advanced | 策略 |
| [rgw_topic_persistency_sleep_duration](#rgw_topic_persistency_sleep_duration) | `0` | Advanced | 性能 |
| [rgw_topic_persistency_time_to_live](#rgw_topic_persistency_time_to_live) | `0` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、API 兼容性、租户限制 |
| **容量** | 磁盘布局、路径、池容量 |
| **性能** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **连通性** | 最近且稳定的外部端点 |
| **架构** | 后端、多站点拓扑 — 非数值扫描 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

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
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_allow_notification_secrets_in_cleartext](../../../config/rgw/rgw.md#SP_rgw_allow_notification_secrets_in_cleartext) |

**作用：** When `true`, allows bucket notification topics with broker passwords/secrets over plain HTTP. Default requires HTTPS for topics with secrets.

**何时使用：** Trusted private lab only. **Never** enable on internet-facing or untrusted networks.

**相关选项：**

- `rgw_trust_forwarded_https` (if TLS terminates at a proxy)

**示例：**

```bash
ceph config set client.rgw rgw_allow_notification_secrets_in_cleartext true
ceph config get client.rgw rgw_allow_notification_secrets_in_cleartext
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_http_notif_connection_timeout

| | |
|---|---|
| 类型 | Uint · default `5` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_http_notif_connection_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_connection_timeout) |

**作用：** This is the maximum time in seconds to connect to an endpoint

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_http_notif_connection_timeout 5
ceph config get client.rgw rgw_http_notif_connection_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. Default `5` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

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
| 类型 | Uint · default `8192` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_http_notif_max_inflight](../../../config/rgw/rgw.md#SP_rgw_http_notif_max_inflight) |

**作用：** This is the maximum number of messages in-flight (across all http endpoints)

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_http_notif_max_inflight 8192
ceph config get client.rgw rgw_http_notif_max_inflight
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `8192`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_http_notif_message_timeout](../../../config/rgw/rgw.md#SP_rgw_http_notif_message_timeout) |

**作用：** This is the maximum time in seconds to deliver a notification

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_http_notif_message_timeout 10
ceph config get client.rgw rgw_http_notif_message_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

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
| 类型 | Float · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_inject_notify_timeout_probability](../../../config/rgw/rgw.md#SP_rgw_inject_notify_timeout_probability) |

**作用：** Likelihood of ignoring a notify

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_inject_notify_timeout_probability 0
ceph config get client.rgw rgw_inject_notify_timeout_probability
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_kafka_connection_idle

| | |
|---|---|
| 类型 | Uint · default `300` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_kafka_connection_idle](../../../config/rgw/rgw.md#SP_rgw_kafka_connection_idle) |

**作用：** Time in seconds to delete idle kafka connections

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_kafka_connection_idle 300
ceph config get client.rgw rgw_kafka_connection_idle
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `300`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_kafka_max_batch_size](../../../config/rgw/rgw.md#SP_rgw_kafka_max_batch_size) |

**作用：** This is the maximum size in bytes of a batch of messages sent to kafka

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_kafka_max_batch_size 128
ceph config get client.rgw rgw_kafka_max_batch_size
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Uint · default `5000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_kafka_message_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_message_timeout) |

**作用：** This is the maximum time in milliseconds to deliver a message (including retries)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_kafka_message_timeout 5000
ceph config get client.rgw rgw_kafka_message_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. Default `5000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

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
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_kafka_sleep_timeout](../../../config/rgw/rgw.md#SP_rgw_kafka_sleep_timeout) |

**作用：** Time in milliseconds to sleep while polling for kafka replies

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_kafka_sleep_timeout 10
ceph config get client.rgw rgw_kafka_sleep_timeout
```

**寻找最优值：**

**调优模型：** Performance

1. Default `10` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

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
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_max_notify_retries](../../../config/rgw/rgw.md#SP_rgw_max_notify_retries) |

**作用：** Number of attempts to notify peers before giving up.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_max_notify_retries 10
ceph config get client.rgw rgw_max_notify_retries
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `10` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_max_retries

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_topic_persistency_max_retries](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_max_retries) |

**作用：** The maximum number sending a persistent notification would be tried. Note that the value of one would mean no retries, and the value of zero would mean that the notification would be tried indefinitely

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_topic_persistency_max_retries 128
ceph config get client.rgw rgw_topic_persistency_max_retries
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `0` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_topic_persistency_sleep_duration

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_topic_persistency_sleep_duration](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_sleep_duration) |

**作用：** The minimum time (in seconds) between two tries of the same persistent notification. note that the actual time between the tries may be longer

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_topic_persistency_sleep_duration 0
ceph config get client.rgw rgw_topic_persistency_sleep_duration
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

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
| 类型 | Uint · default `0` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_topic_persistency_time_to_live](../../../config/rgw/rgw.md#SP_rgw_topic_persistency_time_to_live) |

**作用：** The rgw retention of persistent topics by time (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_topic_persistency_time_to_live 0
ceph config get client.rgw rgw_topic_persistency_time_to_live
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_topic_persistency_time_to_live
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
