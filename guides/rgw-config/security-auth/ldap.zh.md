# LDAP

RGW 配置深度指南 — 6 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_ldap_binddn](#rgw_ldap_binddn) | `uid=admin,cn=users,dc=example,dc=com` | Advanced | Policy |
| [rgw_ldap_dnattr](#rgw_ldap_dnattr) | `uid` | Advanced | Performance |
| [rgw_ldap_searchdn](#rgw_ldap_searchdn) | `cn=users,cn=accounts,dc=example,dc=com` | Advanced | Performance |
| [rgw_ldap_searchfilter](#rgw_ldap_searchfilter) | `(empty)` | Advanced | Performance |
| [rgw_ldap_secret](#rgw_ldap_secret) | `/etc/openldap/secret` | Advanced | Policy |
| [rgw_ldap_uri](#rgw_ldap_uri) | `(empty)` | Advanced | Connectivity |

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

### rgw_ldap_binddn

| | |
|---|---|
| 类型 | Str · default `uid=admin,cn=users,dc=example,dc=com` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_binddn](../../../config/rgw/rgw.md#SP_rgw_ldap_binddn) |

**作用：** LDAP entry RGW will bind with (user match).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_binddn "uid=admin,cn=users,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_binddn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`uid=admin,cn=users,dc=example,dc=com`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_ldap_dnattr

| | |
|---|---|
| 类型 | Str · default `uid` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_dnattr](../../../config/rgw/rgw.md#SP_rgw_ldap_dnattr) |

**作用：** LDAP attribute containing RGW user names (to form binddns).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_dnattr uid
ceph config get client.rgw rgw_ldap_dnattr
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `uid`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_dnattr
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchdn

| | |
|---|---|
| 类型 | Str · default `cn=users,cn=accounts,dc=example,dc=com` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_searchdn](../../../config/rgw/rgw.md#SP_rgw_ldap_searchdn) |

**作用：** LDAP search base (basedn).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_searchdn "cn=users,cn=accounts,dc=example,dc=com"
ceph config get client.rgw rgw_ldap_searchdn
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `cn=users,cn=accounts,dc=example,dc=com`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchdn
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_searchfilter

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_searchfilter](../../../config/rgw/rgw.md#SP_rgw_ldap_searchfilter) |

**作用：** LDAP search filter.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_searchfilter <value>
ceph config get client.rgw rgw_ldap_searchfilter
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_ldap_searchfilter
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_ldap_secret

| | |
|---|---|
| 类型 | Str · default `/etc/openldap/secret` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_secret](../../../config/rgw/rgw.md#SP_rgw_ldap_secret) |

**作用：** Path to file containing credentials for rgw_ldap_binddn.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_secret "/etc/openldap/secret"
ceph config get client.rgw rgw_ldap_secret
ceph config set client.rgw rgw_s3_auth_use_ldap true
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_ldap_uri

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_ldap_uri](../../../config/rgw/rgw.md#SP_rgw_ldap_uri) |

**作用：** Space-separated list of LDAP servers in URI format, e.g., "ldaps://<ldap.your.domain>".

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_ldap_uri "ldaps://ldap.example.com/"
ceph config get client.rgw rgw_ldap_uri
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
ceph config get client.rgw rgw_ldap_uri
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
