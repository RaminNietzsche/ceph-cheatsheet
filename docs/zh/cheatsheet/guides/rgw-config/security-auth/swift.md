# Swift API

RGW 配置深度指南 — 11 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_swift_account_in_url](#rgw_swift_account_in_url) | `False` | Advanced | 连通性 |
| [rgw_swift_auth_entry](#rgw_swift_auth_entry) | `auth` | Advanced | 策略 |
| [rgw_swift_auth_url](#rgw_swift_auth_url) | `(empty)` | Advanced | 连通性 |
| [rgw_swift_custom_header](#rgw_swift_custom_header) | `(empty)` | Advanced | 性能 |
| [rgw_swift_enforce_content_length](#rgw_swift_enforce_content_length) | `False` | Advanced | 策略 |
| [rgw_swift_need_stats](#rgw_swift_need_stats) | `True` | Advanced | 策略 |
| [rgw_swift_tenant_name](#rgw_swift_tenant_name) | `(empty)` | Advanced | 性能 |
| [rgw_swift_token_expiration](#rgw_swift_token_expiration) | `1_day` | Advanced | 性能 |
| [rgw_swift_url](#rgw_swift_url) | `(empty)` | Advanced | 连通性 |
| [rgw_swift_url_prefix](#rgw_swift_url_prefix) | `swift` | Advanced | 性能 |
| [rgw_swift_versioning_enabled](#rgw_swift_versioning_enabled) | `False` | Advanced | 策略 |

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

### rgw_swift_account_in_url

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_account_in_url](../../../config/rgw/rgw.md#SP_rgw_swift_account_in_url) |

**作用：** Swift account encoded in URL

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_swift_account_in_url true
ceph config get client.rgw rgw_swift_account_in_url
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`False`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_account_in_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_auth_entry

| | |
|---|---|
| 类型 | Str · default `auth` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_auth_entry](../../../config/rgw/rgw.md#SP_rgw_swift_auth_entry) |

**作用：** Swift auth URL prefix

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_swift_auth_entry auth
ceph config get client.rgw rgw_swift_auth_entry
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`auth`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_swift_auth_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_auth_url](../../../config/rgw/rgw.md#SP_rgw_swift_auth_url) |

**作用：** Swift auth URL

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_swift_auth_url "https://swift.example.com/auth/v1.0"
ceph config get client.rgw rgw_swift_auth_url
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_auth_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_custom_header

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_custom_header](../../../config/rgw/rgw.md#SP_rgw_swift_custom_header) |

**作用：** Enable swift custom header

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_swift_custom_header <value>
ceph config get client.rgw rgw_swift_custom_header
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_custom_header
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_enforce_content_length

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_enforce_content_length](../../../config/rgw/rgw.md#SP_rgw_swift_enforce_content_length) |

**作用：** Send content length when listing containers (Swift)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_swift_enforce_content_length true
ceph config get client.rgw rgw_swift_enforce_content_length
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_need_stats

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_need_stats](../../../config/rgw/rgw.md#SP_rgw_swift_need_stats) |

**作用：** Enable stats on bucket listing in Swift

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_swift_need_stats false
ceph config get client.rgw rgw_swift_need_stats
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_swift_tenant_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_tenant_name](../../../config/rgw/rgw.md#SP_rgw_swift_tenant_name) |

**作用：** Swift tenant name

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_swift_tenant_name <value>
ceph config get client.rgw rgw_swift_tenant_name
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_tenant_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_token_expiration

| | |
|---|---|
| 类型 | Int · default `1_day` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_token_expiration](../../../config/rgw/rgw.md#SP_rgw_swift_token_expiration) |

**作用：** Expiration time (in seconds) for token generated through RGW Swift auth.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_swift_token_expiration 1_day
ceph config get client.rgw rgw_swift_token_expiration
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `1_day`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_token_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_url](../../../config/rgw/rgw.md#SP_rgw_swift_url) |

**作用：** Swift-auth storage URL

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_swift_url "https://swift.example.com/auth/v1.0"
ceph config get client.rgw rgw_swift_url
# curl -k <url>  # from each RGW node
```

**寻找最优值：**

**调优模型：** Connectivity

1. List candidate endpoints from your provider (Barbican, Keystone, Vault, KMIP, LDAP).
2. From **each** RGW node: `curl -k <url>` or vendor health check.
3. Pick the lowest-latency endpoint that stays healthy over 24h.
4. Measure p99 of operations that call this service (e.g. SSE-KMS PUT).
5. Leave empty (`(empty)`) if the integration is disabled.

```bash
ceph config get client.rgw rgw_swift_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_url_prefix

| | |
|---|---|
| 类型 | Str · default `swift` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_url_prefix](../../../config/rgw/rgw.md#SP_rgw_swift_url_prefix) |

**作用：** Swift URL prefix

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_swift_url_prefix swift
ceph config get client.rgw rgw_swift_url_prefix
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `swift`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_swift_url_prefix
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_swift_versioning_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_swift_versioning_enabled](../../../config/rgw/rgw.md#SP_rgw_swift_versioning_enabled) |

**作用：** Enable Swift versioning

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_swift_versioning_enabled true
ceph config get client.rgw rgw_swift_versioning_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
