# API limits & policies

RGW 配置深度指南 — 6 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | Policy |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | Policy |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | Policy |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | Policy |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | Policy |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced | Policy |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **Policy** | 安全、API 兼容性、租户限制 |
| **Capacity** | 磁盘布局、路径、池容量 |
| **Performance** | 基线 → 逐步调整 → 监控 OSD/RGW |
| **Connectivity** | 最近且稳定的外部端点 |
| **Architecture** | 后端、多站点拓扑 — 非数值扫描 |
| **Dev** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get client.rgw <option>
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_acl_grants_max_num

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_acl_grants_max_num](../../../config/rgw/rgw.md#SP_rgw_acl_grants_max_num) |

**作用：** Maximum number of ACL grants in a single PutBucketAcl / PutObjectAcl request (aligned with S3 limits).

**何时使用：** Raise only if clients legitimately need more grants; lowering hardens against oversized ACL payloads.

**相关选项：**

- `rgw_cors_rules_max_num`, `rgw_user_policies_max_num`

**示例：**

```bash
ceph config set client.rgw rgw_acl_grants_max_num 100
ceph config get client.rgw rgw_acl_grants_max_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_admin_entry

| | |
|---|---|
| 类型 | Str · default `admin` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_admin_entry](../../../config/rgw/rgw.md#SP_rgw_admin_entry) |

**作用：** URL path prefix for the **RGW Admin Ops REST API** (bucket/user introspection, usage, etc.). **Not runtime-updatable.**

**Important:** Multisite replication **requires** the value `admin`. Do not change it on multisite clusters.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
# GET https://rgw.example.com/admin/bucket?bucket=mybucket&format=json
curl -s -H "Authorization: AWS ..." \
  "https://rgw.example.com/admin/bucket?bucket=mybucket&format=json"
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`admin`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_cors_rules_max_num

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_cors_rules_max_num](../../../config/rgw/rgw.md#SP_rgw_cors_rules_max_num) |

**作用：** The maximum number of CORS rules in a single request.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_cors_rules_max_num 100
ceph config get client.rgw rgw_cors_rules_max_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_policy_reject_invalid_principals

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [rgw.md#SP_rgw_policy_reject_invalid_principals](../../../config/rgw/rgw.md#SP_rgw_policy_reject_invalid_principals) |

**作用：** Whether to reject policies with invalid principals

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_policy_reject_invalid_principals false
ceph config get client.rgw rgw_policy_reject_invalid_principals
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_topic_require_publish_policy

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [rgw.md#SP_rgw_topic_require_publish_policy](../../../config/rgw/rgw.md#SP_rgw_topic_require_publish_policy) |

**作用：** Whether to validate user permissions to publish notifications to topics.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_topic_require_publish_policy true
ceph config get client.rgw rgw_topic_require_publish_policy
```

**寻找最优值：**

**调优模型：** Policy

1. Production: prefer secure default (`False` for most security options).
2. Relax only on trusted private networks with documented risk acceptance.
3. Test client behavior (HTTPS redirects, presigned URLs) after changes.

---

### rgw_website_routing_rules_max_num

| | |
|---|---|
| 类型 | Int · default `50` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_website_routing_rules_max_num](../../../config/rgw/rgw.md#SP_rgw_website_routing_rules_max_num) |

**作用：** The maximum number of website routing rules in a single request.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_website_routing_rules_max_num 50
ceph config get client.rgw rgw_website_routing_rules_max_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `50` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---


[← RGW 配置概览](../OVERVIEW.md)
