# HTTP compatibility

RGW 配置深度指南 — 17 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_content_length_compat](#rgw_content_length_compat) | `False` | Advanced | 策略 |
| [rgw_cross_domain_policy](#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Advanced | 性能 |
| [rgw_defer_to_bucket_acls](#rgw_defer_to_bucket_acls) | `(empty)` | Advanced | 性能 |
| [rgw_enforce_swift_acls](#rgw_enforce_swift_acls) | `True` | Advanced | 策略 |
| [rgw_extended_http_attrs](#rgw_extended_http_attrs) | `(empty)` | Advanced | 性能 |
| [rgw_ignore_get_invalid_range](#rgw_ignore_get_invalid_range) | `False` | Advanced | 策略 |
| [rgw_print_continue](#rgw_print_continue) | `True` | Advanced | 策略 |
| [rgw_print_prohibited_content_length](#rgw_print_prohibited_content_length) | `False` | Advanced | 策略 |
| [rgw_relaxed_region_enforcement](#rgw_relaxed_region_enforcement) | `False` | Advanced | 策略 |
| [rgw_relaxed_s3_bucket_names](#rgw_relaxed_s3_bucket_names) | `False` | Advanced | 策略 |
| [rgw_relaxed_topic_names](#rgw_relaxed_topic_names) | `False` | Advanced | 策略 |
| [rgw_remote_addr_param](#rgw_remote_addr_param) | `REMOTE_ADDR` | Advanced | 性能 |
| [rgw_request_uri](#rgw_request_uri) | `(empty)` | Dev | 连通性 |
| [rgw_resolve_cname](#rgw_resolve_cname) | `False` | Advanced | 策略 |
| [rgw_service_provider_name](#rgw_service_provider_name) | `(empty)` | Advanced | 性能 |
| [rgw_trust_forwarded_https](#rgw_trust_forwarded_https) | `False` | Advanced | 策略 |
| [rgw_verify_ssl](#rgw_verify_ssl) | `True` | Advanced | 策略 |

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

### rgw_content_length_compat

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_content_length_compat](../../../config/rgw/rgw.md#SP_rgw_content_length_compat) |

**作用：** Multiple content length headers compatibility Try to handle requests with ambiguous multiple content length headers (Content-Length, Http-Content-Length).

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_content_length_compat true
ceph config get client.rgw rgw_content_length_compat
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_cross_domain_policy

| | |
|---|---|
| 类型 | Str · default `<allow-access-from domain="*" secure="false" />` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_cross_domain_policy](../../../config/rgw/rgw.md#SP_rgw_cross_domain_policy) |

**作用：** RGW handle cross domain policy Returned cross domain policy when accessing the crossdomain.xml resource (Swift compatibility).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_cross_domain_policy "<allow-access-from domain="*" secure="false" />"
ceph config get client.rgw rgw_cross_domain_policy
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `<allow-access-from domain="*" secure="false" />`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_cross_domain_policy
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_defer_to_bucket_acls

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_defer_to_bucket_acls](../../../config/rgw/rgw.md#SP_rgw_defer_to_bucket_acls) |

**作用：** Bucket ACLs override object ACLs If not empty, a string that selects that mode of operation. 'recurse' will use bucket's ACL for the authorization. 'full-control' will allow users that users that have full control permission on the bucket have access to the object.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_defer_to_bucket_acls <value>
ceph config get client.rgw rgw_defer_to_bucket_acls
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_defer_to_bucket_acls
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_enforce_swift_acls

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enforce_swift_acls](../../../config/rgw/rgw.md#SP_rgw_enforce_swift_acls) |

**作用：** RGW enforce swift acls Should RGW enforce special Swift-only ACLs. Swift has a special ACL that gives permission to access all objects in a container.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enforce_swift_acls false
ceph config get client.rgw rgw_enforce_swift_acls
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_extended_http_attrs

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_extended_http_attrs](../../../config/rgw/rgw.md#SP_rgw_extended_http_attrs) |

**作用：** RGW support extended HTTP attrs Add new set of attributes that could be set on an object. These extra attributes can be set through HTTP header fields when putting the objects. If set, these attributes will return as HTTP fields when doing GET/HEAD on the object.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_extended_http_attrs <value>
ceph config get client.rgw rgw_extended_http_attrs
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_extended_http_attrs
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ignore_get_invalid_range

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ignore_get_invalid_range](../../../config/rgw/rgw.md#SP_rgw_ignore_get_invalid_range) |

**作用：** Treat invalid (e.g., negative) range request as full Treat invalid (e.g., negative) range request as request for the full object (AWS compatibility)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_ignore_get_invalid_range true
ceph config get client.rgw rgw_ignore_get_invalid_range
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_continue

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_print_continue](../../../config/rgw/rgw.md#SP_rgw_print_continue) |

**作用：** RGW support of 100-continue Should RGW explicitly send 100 (continue) responses. This is mainly relevant when using FastCGI, as some FastCGI modules do not fully support this feature.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_print_continue false
ceph config get client.rgw rgw_print_continue
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_print_prohibited_content_length

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_print_prohibited_content_length](../../../config/rgw/rgw.md#SP_rgw_print_prohibited_content_length) |

**作用：** RGW RFC-7230 compatibility Specifies whether RGW violates RFC 7230 and sends Content-Length with 204 or 304 statuses.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_print_prohibited_content_length true
ceph config get client.rgw rgw_print_prohibited_content_length
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_region_enforcement

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_relaxed_region_enforcement](../../../config/rgw/rgw.md#SP_rgw_relaxed_region_enforcement) |

**作用：** Disable region constraint enforcement Enable requests such as bucket creation to succeed irrespective of region restrictions (Jewel compat).

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_relaxed_region_enforcement true
ceph config get client.rgw rgw_relaxed_region_enforcement
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_s3_bucket_names

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_relaxed_s3_bucket_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_s3_bucket_names) |

**作用：** RGW enable relaxed S3 bucket names RGW enable relaxed S3 bucket name rules for US region buckets.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_relaxed_s3_bucket_names true
ceph config get client.rgw rgw_relaxed_s3_bucket_names
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_relaxed_topic_names

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_relaxed_topic_names](../../../config/rgw/rgw.md#SP_rgw_relaxed_topic_names) |

**作用：** RGW enable relaxed topic names RGW enable relaxed topic names to allow changing existing topics that were created before validation rules were implemented. This also allows re-creating topics that were deleted, but match names that are already used externally (e.g. in Kafka)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_relaxed_topic_names true
ceph config get client.rgw rgw_relaxed_topic_names
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_remote_addr_param

| | |
|---|---|
| 类型 | Str · default `REMOTE_ADDR` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_remote_addr_param](../../../config/rgw/rgw.md#SP_rgw_remote_addr_param) |

**作用：** HTTP header that holds the remote address in incoming requests. RGW will use this header to extract requests origin. When RGW runs behind a reverse proxy, the remote address header will point at the proxy's address and not at the originator's address. Therefore it is sometimes possible to have the proxy add the originator's address in a separate HTTP header, which will allow RGW to log it correctly.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`rgw_enable_ops_log`](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log)

**示例：**

```bash
ceph config set client.rgw rgw_remote_addr_param REMOTE_ADDR
ceph config get client.rgw rgw_remote_addr_param
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `REMOTE_ADDR`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_remote_addr_param
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_request_uri

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_request_uri](../../../config/rgw/rgw.md#SP_rgw_request_uri) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_request_uri "https://service.example.com/"
ceph config get client.rgw rgw_request_uri
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
ceph config get client.rgw rgw_request_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_resolve_cname

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_resolve_cname](../../../config/rgw/rgw.md#SP_rgw_resolve_cname) |

**作用：** Support vanity domain names via CNAME If true, RGW will query DNS when detecting that it's serving a request that was sent to a host in another domain. If a CNAME record is configured for that domain it will use it instead. This gives user to have the ability of creating a unique domain of their own to point at data in their bucket.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_resolve_cname true
ceph config get client.rgw rgw_resolve_cname
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_service_provider_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_service_provider_name](../../../config/rgw/rgw.md#SP_rgw_service_provider_name) |

**作用：** Service provider name which is contained in http response headers As S3 or other cloud storage providers do, http response headers should contain the name of the provider. This name will be placed in http header 'Server'.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_service_provider_name <value>
ceph config get client.rgw rgw_service_provider_name
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_service_provider_name
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_trust_forwarded_https

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_trust_forwarded_https](../../../config/rgw/rgw.md#SP_rgw_trust_forwarded_https) |

**作用：** Trust Forwarded and X-Forwarded-Proto headers When a proxy in front of radosgw is used for ssl termination, radosgw does not know whether incoming http connections are secure. Enable this option to trust the Forwarded and X-Forwarded-Proto headers sent by the proxy when determining whether the connection is secure. This is required for some features, such as server side encryption. (Never enable this setting if you do not have a trusted proxy in front of radosgw, or else malicious users will be able to set these headers in any request.)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**相关选项：**

- [`rgw_crypt_require_ssl`](../../../config/rgw/rgw.md#SP_rgw_crypt_require_ssl)

**示例：**

```bash
ceph config set client.rgw rgw_trust_forwarded_https true
ceph config get client.rgw rgw_trust_forwarded_https
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_verify_ssl

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_verify_ssl) |

**作用：** Should RGW verify SSL when connecting to a remote HTTP server RGW can send requests to other RGW servers (e.g., in multi-site sync work). This configurable selects whether RGW should verify the certificate for the remote peer and host.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`rgw_keystone_verify_ssl`](../../../config/rgw/rgw.md#SP_rgw_keystone_verify_ssl)

**示例：**

```bash
ceph config set client.rgw rgw_verify_ssl false
ceph config get client.rgw rgw_verify_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---


[← RGW 配置概览](../OVERVIEW.md)
