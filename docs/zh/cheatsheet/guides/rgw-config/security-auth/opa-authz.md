# OPA authorization

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_opa_token](#rgw_opa_token) | `(empty)` | Advanced | 策略 |
| [rgw_opa_url](#rgw_opa_url) | `(empty)` | Advanced | 连通性 |
| [rgw_opa_verify_ssl](#rgw_opa_verify_ssl) | `True` | Advanced | 策略 |
| [rgw_use_opa_authz](#rgw_use_opa_authz) | `False` | Advanced | 策略 |

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

### rgw_opa_token

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_opa_token](../../../config/rgw/rgw.md#SP_rgw_opa_token) |

**作用：** The Bearer token OPA uses to authenticate client requests.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_opa_token <value>
ceph config get client.rgw rgw_opa_token
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_opa_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_opa_url](../../../config/rgw/rgw.md#SP_rgw_opa_url) |

**作用：** URL to OPA server.

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_opa_url "https://opa.example.com:8181/v1/data/ceph/authz"
ceph config get client.rgw rgw_opa_url
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
ceph config get client.rgw rgw_opa_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_opa_verify_ssl

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_opa_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_opa_verify_ssl) |

**作用：** Should RGW verify the OPA server SSL certificate.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_opa_verify_ssl false
ceph config get client.rgw rgw_opa_verify_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`True` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_use_opa_authz

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_use_opa_authz](../../../config/rgw/rgw.md#SP_rgw_use_opa_authz) |

**作用：** Should OPA be used to authorize client requests.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_use_opa_authz true
ceph config get client.rgw rgw_use_opa_authz
ceph config set client.rgw rgw_opa_url "https://opa.example.com:8181/v1/data/ceph/authz"
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
