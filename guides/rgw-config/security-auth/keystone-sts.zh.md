# Keystone & STS

RGW 配置深度指南 — 32 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_keystone_accepted_admin_roles](#rgw_keystone_accepted_admin_roles) | `(empty)` | Advanced | Performance |
| [rgw_keystone_accepted_reader_roles](#rgw_keystone_accepted_reader_roles) | `(empty)` | Advanced | Performance |
| [rgw_keystone_accepted_roles](#rgw_keystone_accepted_roles) | `Member, admin` | Advanced | Performance |
| [rgw_keystone_admin_domain](#rgw_keystone_admin_domain) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_password](#rgw_keystone_admin_password) | `(empty)` | Advanced | Policy |
| [rgw_keystone_admin_password_path](#rgw_keystone_admin_password_path) | `(empty)` | Advanced | Capacity |
| [rgw_keystone_admin_project](#rgw_keystone_admin_project) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_tenant](#rgw_keystone_admin_tenant) | `(empty)` | Advanced | Performance |
| [rgw_keystone_admin_user](#rgw_keystone_admin_user) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_domain](#rgw_keystone_barbican_domain) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_password](#rgw_keystone_barbican_password) | `(empty)` | Advanced | Policy |
| [rgw_keystone_barbican_project](#rgw_keystone_barbican_project) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_tenant](#rgw_keystone_barbican_tenant) | `(empty)` | Advanced | Performance |
| [rgw_keystone_barbican_user](#rgw_keystone_barbican_user) | `(empty)` | Advanced | Performance |
| [rgw_keystone_expired_token_cache_expiration](#rgw_keystone_expired_token_cache_expiration) | `3600` | Advanced | Performance |
| [rgw_keystone_implicit_tenants](#rgw_keystone_implicit_tenants) | `false` | Advanced | Architecture |
| [rgw_keystone_scope_enabled](#rgw_keystone_scope_enabled) | `False` | Advanced | Policy |
| [rgw_keystone_scope_include_roles](#rgw_keystone_scope_include_roles) | `True` | Advanced | Policy |
| [rgw_keystone_scope_include_user](#rgw_keystone_scope_include_user) | `False` | Advanced | Policy |
| [rgw_keystone_service_token_accepted_roles](#rgw_keystone_service_token_accepted_roles) | `admin` | Advanced | Policy |
| [rgw_keystone_service_token_enabled](#rgw_keystone_service_token_enabled) | `False` | Advanced | Policy |
| [rgw_keystone_token_cache_size](#rgw_keystone_token_cache_size) | `10000` | Advanced | Performance |
| [rgw_keystone_token_cache_ttl](#rgw_keystone_token_cache_ttl) | `300` | Advanced | Performance |
| [rgw_keystone_url](#rgw_keystone_url) | `(empty)` | Basic | Connectivity |
| [rgw_keystone_verify_ssl](#rgw_keystone_verify_ssl) | `True` | Advanced | Policy |
| [rgw_sts_client_id](#rgw_sts_client_id) | `(empty)` | Advanced | Policy |
| [rgw_sts_client_secret](#rgw_sts_client_secret) | `(empty)` | Advanced | Policy |
| [rgw_sts_entry](#rgw_sts_entry) | `sts` | Advanced | Policy |
| [rgw_sts_key](#rgw_sts_key) | `(empty)` | Advanced | Performance |
| [rgw_sts_max_session_duration](#rgw_sts_max_session_duration) | `43200` | Advanced | Policy |
| [rgw_sts_min_session_duration](#rgw_sts_min_session_duration) | `900` | Advanced | Performance |
| [rgw_sts_token_introspection_url](#rgw_sts_token_introspection_url) | `(empty)` | Advanced | Connectivity |

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

### rgw_keystone_accepted_admin_roles

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_accepted_admin_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_admin_roles) |

**作用：** List of roles allowing user to gain admin privileges (Keystone).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_accepted_admin_roles <value>
ceph config get client.rgw rgw_keystone_accepted_admin_roles
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_admin_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_reader_roles

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_accepted_reader_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_reader_roles) |

**作用：** List of roles that can only be used for reads (Keystone).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_accepted_reader_roles <value>
ceph config get client.rgw rgw_keystone_accepted_reader_roles
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_reader_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_accepted_roles

| | |
|---|---|
| 类型 | Str · default `Member, admin` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_accepted_roles) |

**作用：** Only users with one of these roles will be served when doing Keystone authentication.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_accepted_roles "Member, admin"
ceph config get client.rgw rgw_keystone_accepted_roles
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `Member, admin`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_accepted_roles
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_domain

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_domain) |

**作用：** Keystone admin user domain (for Keystone v3).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_domain <value>
ceph config get client.rgw rgw_keystone_admin_domain
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_password

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_password](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password) |

**作用：** DEPRECATED: Keystone admin password.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_admin_password
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_admin_password_path

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_password_path](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_password_path) |

**作用：** Path to a file containing the Keystone admin password.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_password_path "/var/lib/ceph/radosgw"
ceph config get client.rgw rgw_keystone_admin_password_path
```

**寻找最优值：**

**调优模型：** Capacity

1. Prefer a dedicated volume (NVMe/SSD) — not the root filesystem.
2. Size for metadata growth + 30% free space (`df -h`, `iowait`).
3. Default path (`(empty)`) is fine when it already sits on fast storage.
4. dbstore/POSIX: all RGW instances sharing data must see the same path.

```bash
df -h $(ceph config get client.rgw rgw_keystone_admin_password_path)
iostat -x 5  # disk saturation
```

---

### rgw_keystone_admin_project

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_project](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_project) |

**作用：** Keystone admin user project (for Keystone v3).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_project <value>
ceph config get client.rgw rgw_keystone_admin_project
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_tenant

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_tenant) |

**作用：** Keystone admin user tenant.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_tenant <value>
ceph config get client.rgw rgw_keystone_admin_tenant
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_admin_user

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_admin_user](../../../config/rgw/rgw.md#SP_rgw_keystone_admin_user) |

**作用：** Keystone admin user.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_admin_user <value>
ceph config get client.rgw rgw_keystone_admin_user
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_admin_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_domain

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_barbican_domain](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_domain) |

**作用：** Keystone barbican user domain.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_barbican_domain <value>
ceph config get client.rgw rgw_keystone_barbican_domain
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_domain
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_password

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_barbican_password](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_password) |

**作用：** Keystone password for barbican user.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_barbican_password "<from-secrets-manager>"
ceph config get client.rgw rgw_keystone_barbican_password
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_barbican_project

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_barbican_project](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_project) |

**作用：** Keystone barbican user project (Keystone v3).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_barbican_project <value>
ceph config get client.rgw rgw_keystone_barbican_project
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_project
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_tenant

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_barbican_tenant](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_tenant) |

**作用：** Keystone barbican user tenant (Keystone v2.0).

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_barbican_tenant <value>
ceph config get client.rgw rgw_keystone_barbican_tenant
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_tenant
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_barbican_user

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_barbican_user](../../../config/rgw/rgw.md#SP_rgw_keystone_barbican_user) |

**作用：** Keystone user to access barbican secrets.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_barbican_user <value>
ceph config get client.rgw rgw_keystone_barbican_user
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_keystone_barbican_user
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_expired_token_cache_expiration

| | |
|---|---|
| 类型 | Int · default `3600` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_expired_token_cache_expiration](../../../config/rgw/rgw.md#SP_rgw_keystone_expired_token_cache_expiration) |

**作用：** The number of seconds to add to current time for expired token expiration

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_keystone_expired_token_cache_expiration 3600
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `3600`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_expired_token_cache_expiration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_implicit_tenants

| | |
|---|---|
| 类型 | Str · enum: ["false", "true", "swift", "s3", "both", "0", "1", "none"] · default `false` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_implicit_tenants](../../../config/rgw/rgw.md#SP_rgw_keystone_implicit_tenants) |

**作用：** RGW Keystone implicit tenants creation

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_implicit_tenants false
ceph config get client.rgw rgw_keystone_implicit_tenants
```

**寻找最优值：**

**调优模型：** Architecture

1. Valid values: ["false", "true", "swift", "s3", "both", "0", "1", "none"].
2. Default `false` matches standard Ceph packaging.
3. Change only when your integration or backend explicitly requires another value.

---

### rgw_keystone_scope_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_scope_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_enabled) |

**作用：** Enable logging of Keystone scope information in ops log

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_scope_enabled true
ceph config get client.rgw rgw_keystone_scope_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_roles

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_scope_include_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_roles) |

**作用：** Include role names in Keystone scope logs

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_scope_include_roles false
ceph config get client.rgw rgw_keystone_scope_include_roles
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_scope_include_user

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_scope_include_user](../../../config/rgw/rgw.md#SP_rgw_keystone_scope_include_user) |

**作用：** Include human-readable identity names in Keystone scope logs

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_scope_include_user true
ceph config get client.rgw rgw_keystone_scope_include_user
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_accepted_roles

| | |
|---|---|
| 类型 | Str · default `admin` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_service_token_accepted_roles](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_accepted_roles) |

**作用：** Only users with one of these roles will be valid for service users.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_service_token_accepted_roles admin
ceph config get client.rgw rgw_keystone_service_token_accepted_roles
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_service_token_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_service_token_enabled](../../../config/rgw/rgw.md#SP_rgw_keystone_service_token_enabled) |

**作用：** Service tokens allowing the usage of expired Keystone auth tokens

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_service_token_enabled true
ceph config get client.rgw rgw_keystone_service_token_enabled
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_keystone_token_cache_size

| | |
|---|---|
| 类型 | Int · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_token_cache_size](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_size) |

**作用：** Keystone token cache size

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_keystone_token_cache_size 10000
ceph config get client.rgw rgw_keystone_token_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_token_cache_ttl

| | |
|---|---|
| 类型 | Int · default `300` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_token_cache_ttl](../../../config/rgw/rgw.md#SP_rgw_keystone_token_cache_ttl) |

**作用：** Keystone token secret key cache TTL

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_keystone_token_cache_ttl 300
ceph config get client.rgw rgw_keystone_token_cache_ttl
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `300`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_keystone_token_cache_ttl
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Basic** |
| 表格 | [rgw.md#SP_rgw_keystone_url](../../../config/rgw/rgw.md#SP_rgw_keystone_url) |

**作用：** The URL to the Keystone server.

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_url "https://keystone.example.com:5000/v3/"
ceph config get client.rgw rgw_keystone_url
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
ceph config get client.rgw rgw_keystone_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_keystone_verify_ssl

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_keystone_verify_ssl](../../../config/rgw/rgw.md#SP_rgw_keystone_verify_ssl) |

**作用：** Should RGW verify the Keystone server SSL certificate.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_keystone_verify_ssl false
ceph config get client.rgw rgw_keystone_verify_ssl
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_client_id

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_client_id](../../../config/rgw/rgw.md#SP_rgw_sts_client_id) |

**作用：** Client Id

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_sts_client_id <value>
ceph config get client.rgw rgw_sts_client_id
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`(empty)`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_client_secret

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_client_secret](../../../config/rgw/rgw.md#SP_rgw_sts_client_secret) |

**作用：** Client Secret

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_sts_client_secret "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_client_secret
```

**寻找最优值：**

**调优模型：** Policy

1. Not tuned numerically — supply from your secrets manager.
2. Rotate on schedule; never store in git or plain `ceph.conf`.
3. Use `ceph config set` at runtime or cephadm secrets where supported.

---

### rgw_sts_entry

| | |
|---|---|
| 类型 | Str · default `sts` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_entry](../../../config/rgw/rgw.md#SP_rgw_sts_entry) |

**作用：** STS URL prefix

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_sts_entry sts
ceph config get client.rgw rgw_sts_entry
```

**寻找最优值：**

**调优模型：** Policy

1. Upstream default (`sts`) is the compatibility baseline.
2. Change only for documented client or compliance requirements.
3. Multisite: verify `rgw_admin_entry` and similar IDs stay at required values.

---

### rgw_sts_key

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_key](../../../config/rgw/rgw.md#SP_rgw_sts_key) |

**作用：** STS Key

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_sts_key "<from-secrets-manager>"
ceph config get client.rgw rgw_sts_key
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_key
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_max_session_duration

| | |
|---|---|
| 类型 | Uint · default `43200` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_max_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_max_session_duration) |

**作用：** Session token max duration

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_sts_max_session_duration 43200
ceph config get client.rgw rgw_sts_max_session_duration
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `43200` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_sts_min_session_duration

| | |
|---|---|
| 类型 | Uint · default `900` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_min_session_duration](../../../config/rgw/rgw.md#SP_rgw_sts_min_session_duration) |

**作用：** Minimum allowed duration of a session

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_sts_min_session_duration 900
ceph config get client.rgw rgw_sts_min_session_duration
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `900`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_sts_min_session_duration
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_sts_token_introspection_url

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_sts_token_introspection_url](../../../config/rgw/rgw.md#SP_rgw_sts_token_introspection_url) |

**作用：** STS Web Token introspection URL

**何时使用：** 与外部服务集成时设置；未使用该功能时留空。

**示例：**

```bash
ceph config set client.rgw rgw_sts_token_introspection_url "https://idp.example.com/oauth2/introspect"
ceph config get client.rgw rgw_sts_token_introspection_url
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
ceph config get client.rgw rgw_sts_token_introspection_url
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
