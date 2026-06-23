# S3 API & auth

RGW 配置深度指南 — 8 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_s3_auth_disable_signature_url](#rgw_s3_auth_disable_signature_url) | `False` | Advanced | Connectivity |
| [rgw_s3_auth_order](#rgw_s3_auth_order) | `sts, external, local` | Advanced | Performance |
| [rgw_s3_auth_use_keystone](#rgw_s3_auth_use_keystone) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_ldap](#rgw_s3_auth_use_ldap) | `False` | Advanced | Policy |
| [rgw_s3_auth_use_rados](#rgw_s3_auth_use_rados) | `True` | Advanced | Policy |
| [rgw_s3_auth_use_sts](#rgw_s3_auth_use_sts) | `False` | Advanced | Policy |
| [rgw_s3_client_max_sig_ver](#rgw_s3_client_max_sig_ver) | `-1` | Advanced | Policy |
| [rgw_s3_success_create_obj_status](#rgw_s3_success_create_obj_status) | `0` | Advanced | Performance |

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

### rgw_s3_auth_disable_signature_url

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_disable_signature_url](../../../config/rgw/rgw.md#SP_rgw_s3_auth_disable_signature_url) |

**作用：** Should authentication with presigned URLs be disabled

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_disable_signature_url true
ceph config get client.rgw rgw_s3_auth_disable_signature_url
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
ceph config get client.rgw rgw_s3_auth_disable_signature_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_order

| | |
|---|---|
| 类型 | Str · default `sts, external, local` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_order](../../../config/rgw/rgw.md#SP_rgw_s3_auth_order) |

**作用：** Authentication strategy order to use for S3

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_order "sts, external, local"
ceph config get client.rgw rgw_s3_auth_order
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `sts, external, local`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_auth_order
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_s3_auth_use_keystone

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_use_keystone](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_keystone) |

**作用：** Specify whether S3 authentication uses Keystone

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_use_keystone true
ceph config get client.rgw rgw_s3_auth_use_keystone
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_s3_auth_use_ldap

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_use_ldap](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_ldap) |

**作用：** Should S3 authentication use LDAP.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_use_ldap true
ceph config get client.rgw rgw_s3_auth_use_ldap
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_rados

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_use_rados](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_rados) |

**作用：** Specify whether S3 authentication uses credentials stored in RADOS

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_use_rados false
ceph config get client.rgw rgw_s3_auth_use_rados
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_auth_use_sts

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_auth_use_sts](../../../config/rgw/rgw.md#SP_rgw_s3_auth_use_sts) |

**作用：** Should S3 authentication use STS.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_s3_auth_use_sts true
ceph config get client.rgw rgw_s3_auth_use_sts
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_s3_client_max_sig_ver

| | |
|---|---|
| 类型 | Int · default `-1` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_client_max_sig_ver](../../../config/rgw/rgw.md#SP_rgw_s3_client_max_sig_ver) |

**作用：** Max S3 authentication signature version

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_s3_client_max_sig_ver -1
ceph config get client.rgw rgw_s3_client_max_sig_ver
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `-1` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_s3_success_create_obj_status

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_s3_success_create_obj_status](../../../config/rgw/rgw.md#SP_rgw_s3_success_create_obj_status) |

**作用：** HTTP return code override for object creation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_s3_success_create_obj_status 0
ceph config get client.rgw rgw_s3_success_create_obj_status
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_s3_success_create_obj_status
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
