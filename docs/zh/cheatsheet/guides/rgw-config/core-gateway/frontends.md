# Frontends & HTTP stack

RGW 配置深度指南 — 6 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_asio_assert_yielding](#rgw_asio_assert_yielding) | `False` | Dev | 开发 |
| [rgw_beast_enable_async](#rgw_beast_enable_async) | `True` | Dev | 策略 |
| [rgw_dns_name](#rgw_dns_name) | `(empty)` | Advanced | 性能 |
| [rgw_dns_s3website_name](#rgw_dns_s3website_name) | `(empty)` | Advanced | 性能 |
| [rgw_frontend_defaults](#rgw_frontend_defaults) | `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` | Advanced | 性能 |
| [rgw_frontends](#rgw_frontends) | `beast port=7480` | Basic | 性能 |

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

### rgw_asio_assert_yielding

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rgw.md#SP_rgw_asio_assert_yielding](../../../config/rgw/rgw.md#SP_rgw_asio_assert_yielding) |

**作用：** Triggers an assertion if code on an asio/beast thread would block instead of yielding to coroutines. Development aid for finding blocking calls.

**何时使用：** RGW development/debugging only — keep `false` in production.

**相关选项：**

- `rgw_beast_enable_async`

**示例：**

```bash
ceph config set client.rgw rgw_asio_assert_yielding true
ceph config get client.rgw rgw_asio_assert_yielding
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_beast_enable_async

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [rgw.md#SP_rgw_beast_enable_async](../../../config/rgw/rgw.md#SP_rgw_beast_enable_async) |

**作用：** When `true`, the Beast HTTP frontend processes requests with **coroutines**, allowing multiple concurrent requests per thread.

**何时使用：** Leave `true` for production throughput. Set `false` only when debugging request flow.

**示例：**

```bash
ceph config set client.rgw rgw_beast_enable_async false
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dns_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dns_name](../../../config/rgw/rgw.md#SP_rgw_dns_name) |

**作用：** The host names that RGW uses. A comma-separated list of FQDNs of the served domains. This is needed for virtual hosting of buckets to work properly, unless configured via the hostnames zonegroup configuration.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dns_name "s3.example.com"
ceph config get client.rgw rgw_dns_name
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_dns_s3website_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_dns_s3website_name](../../../config/rgw/rgw.md#SP_rgw_dns_s3website_name) |

**作用：** The host name that RGW uses for static websites (S3) This is needed for virtual hosting of buckets, unless configured via zonegroup configuration.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_dns_s3website_name "website.s3.example.com"
ceph config get client.rgw rgw_dns_s3website_name
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_s3website_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_frontend_defaults

| | |
|---|---|
| 类型 | Str · default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_frontend_defaults](../../../config/rgw/rgw.md#SP_rgw_frontend_defaults) |

**作用：** RGW frontends default configuration A comma delimited list of default frontends configuration.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_frontend_defaults "beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key"
ceph config get client.rgw rgw_frontend_defaults
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontend_defaults
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_frontends

| | |
|---|---|
| 类型 | Str · default `beast port=7480` · **Basic** |
| 表格 | [rgw.md#SP_rgw_frontends](../../../config/rgw/rgw.md#SP_rgw_frontends) |

**作用：** RGW frontends configuration A comma delimited list of frontends configuration. Each configuration contains the type of the frontend followed by an optional space delimited set of key=value config parameters.

**何时使用：** 核心 RGW 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set client.rgw rgw_frontends "beast port=7480"
ceph config get client.rgw rgw_frontends
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `beast port=7480`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontends
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
