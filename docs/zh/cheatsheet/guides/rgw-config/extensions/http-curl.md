# HTTP / libcurl

RGW 配置深度指南 — 5 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_curl_buffersize](#rgw_curl_buffersize) | `524288` | Dev | 性能 |
| [rgw_curl_low_speed_limit](#rgw_curl_low_speed_limit) | `1024` | Advanced | 策略 |
| [rgw_curl_low_speed_time](#rgw_curl_low_speed_time) | `5_min` | Advanced | 性能 |
| [rgw_curl_tcp_keepalive](#rgw_curl_tcp_keepalive) | `0` | Advanced | 架构 |
| [rgw_curl_wait_timeout_ms](#rgw_curl_wait_timeout_ms) | `1000` | Dev | 性能 |

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

### rgw_curl_buffersize

| | |
|---|---|
| 类型 | Int · default `524288` · **Dev** |
| 表格 | [rgw.md#SP_rgw_curl_buffersize](../../../config/rgw/rgw.md#SP_rgw_curl_buffersize) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_curl_buffersize 524288
ceph config get client.rgw rgw_curl_buffersize
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `524288`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_buffersize
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

**边界：** min `1024`, max `524288`.

---

### rgw_curl_low_speed_limit

| | |
|---|---|
| 类型 | Int · default `1024` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_curl_low_speed_limit](../../../config/rgw/rgw.md#SP_rgw_curl_low_speed_limit) |

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_curl_low_speed_limit 1024
ceph config get client.rgw rgw_curl_low_speed_limit
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`1024`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_curl_low_speed_time

| | |
|---|---|
| 类型 | Int · default `5_min` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_curl_low_speed_time](../../../config/rgw/rgw.md#SP_rgw_curl_low_speed_time) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_curl_low_speed_time 5_min
ceph config get client.rgw rgw_curl_low_speed_time
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_curl_low_speed_time
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_curl_tcp_keepalive

| | |
|---|---|
| 类型 | Int · enum: ["0", "1"] · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_curl_tcp_keepalive](../../../config/rgw/rgw.md#SP_rgw_curl_tcp_keepalive) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_curl_tcp_keepalive 0
ceph config get client.rgw rgw_curl_tcp_keepalive
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["0", "1"].
2. Default `0` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_curl_wait_timeout_ms

| | |
|---|---|
| 类型 | Int · default `1000` · **Dev** |
| 表格 | [rgw.md#SP_rgw_curl_wait_timeout_ms](../../../config/rgw/rgw.md#SP_rgw_curl_wait_timeout_ms) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_curl_wait_timeout_ms 1000
ceph config get client.rgw rgw_curl_wait_timeout_ms
```

**寻找最优值：**

**调优模型：** Performance

1. Default `1000` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**观测信号：** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_curl_wait_timeout_ms
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
