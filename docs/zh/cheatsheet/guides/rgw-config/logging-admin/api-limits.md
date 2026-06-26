# API limits & policies

RGW 配置深度指南 — 6 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_acl_grants_max_num](#rgw_acl_grants_max_num) | `100` | Advanced | 策略 |
| [rgw_admin_entry](#rgw_admin_entry) | `admin` | Advanced | 策略 |
| [rgw_cors_rules_max_num](#rgw_cors_rules_max_num) | `100` | Advanced | 策略 |
| [rgw_policy_reject_invalid_principals](#rgw_policy_reject_invalid_principals) | `True` | Basic | 策略 |
| [rgw_topic_require_publish_policy](#rgw_topic_require_publish_policy) | `False` | Basic | 策略 |
| [rgw_website_routing_rules_max_num](#rgw_website_routing_rules_max_num) | `50` | Advanced | 策略 |

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

**何时使用：** 多站点复制与同步调优 — 延迟或同步负载异常时调整。

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

**作用：** Whether to reject policies with invalid principals If true, policies with invalid principals will be rejected. We don't support Canonical User identifiers or some other form of policies that Amazon does, so if you are mirroring policies between RGW and AWS, you may wish to set this to false.

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

**作用：** Whether to validate user permissions to publish notifications to topics. If true, all users (other then the owner of the topic) will need to have a policy to publish notifications to topics. The topic policy can be set by owner via CreateTopic() or SetTopicAttribute(). Following permissions can be granted "sns:Publish", "sns:GetTopicAttributes", "sns:SetTopicAttributes", "sns:DeleteTopic" and "sns:CreateTopic" via Policy. NOTE that even if set to "false" topics will still follow the policies if set on them.

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
