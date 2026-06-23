# Quota sync & defaults

RGW 配置深度指南 — 5 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

配额 enforcement 还需每个 zone 至少一个 RGW 启用 `rgw_enable_quota_threads`。见 [rgw_enable_quota_threads](../../../config/rgw/rgw.md#SP_rgw_enable_quota_threads)。

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_account_default_quota_max_objects](#rgw_account_default_quota_max_objects) | `-1` | Basic | Policy |
| [rgw_account_default_quota_max_size](#rgw_account_default_quota_max_size) | `-1` | Basic | Policy |
| [rgw_enable_quota_threads](#rgw_enable_quota_threads) | `True` | Advanced | Policy |
| [rgw_user_default_quota_max_objects](#rgw_user_default_quota_max_objects) | `-1` | Basic | Policy |
| [rgw_user_default_quota_max_size](#rgw_user_default_quota_max_size) | `-1` | Basic | Policy |

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

### rgw_account_default_quota_max_objects

| | |
|---|---|
| 类型 | Int · default `-1` · **Basic** |
| 表格 | [rgw.md#SP_rgw_account_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_objects) |

**作用：** Default cap on **total object count** across all buckets owned by a **new** S3 account. `-1` means unlimited.

**何时使用：** Multi-tenant platforms using the account abstraction. Applies only when accounts are created — existing accounts are unchanged.

**相关选项：**

- `rgw_account_default_quota_max_size`
- `rgw_enable_quota_threads` (required on at least one RGW per zone)

**示例：**

```bash
ceph config set client rgw_account_default_quota_max_objects 1000000
radosgw-admin user create --uid=alice --display-name="Alice"
radosgw-admin quota get --quota-scope=user --uid=alice
```

Set in `[client]` or global so `radosgw-admin` picks it up.

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_account_default_quota_max_size

| | |
|---|---|
| 类型 | Int · default `-1` · **Basic** |
| 表格 | [rgw.md#SP_rgw_account_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_size) |

**作用：** Default cap on **total stored bytes** for a new account.

**何时使用：** 为新用户、账户或 bucket 设置租户/平台默认限制。

**示例：**

```bash
# 10 TiB
ceph config set client rgw_account_default_quota_max_size $((10*1024*1024*1024*1024))
```

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_enable_quota_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_quota_threads](../../../config/rgw/rgw.md#SP_rgw_enable_quota_threads) |

**作用：** Enables the quota maintenance thread.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_quota_threads false
ceph config get client.rgw rgw_enable_quota_threads
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_default_quota_max_objects

| | |
|---|---|
| 类型 | Int · default `-1` · **Basic** |
| 表格 | [rgw.md#SP_rgw_user_default_quota_max_objects](../../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_objects) |

**作用：** User quota max objects

**何时使用：** 为新用户、账户或 bucket 设置租户/平台默认限制。

**示例：**

```bash
ceph config set client rgw_user_default_quota_max_objects 1000000
ceph config get client rgw_user_default_quota_max_objects
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_user_default_quota_max_size

| | |
|---|---|
| 类型 | Int · default `-1` · **Basic** |
| 表格 | [rgw.md#SP_rgw_user_default_quota_max_size](../../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_size) |

**作用：** User quota max size

**何时使用：** 为新用户、账户或 bucket 设置租户/平台默认限制。

**示例：**

```bash
ceph config set client rgw_user_default_quota_max_size $((100*1024*1024*1024))
ceph config get client rgw_user_default_quota_max_size
radosgw-admin quota get --quota-scope=user --uid=testuser
```

**寻找最优值：**

**调优模型：** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user and confirm via `radosgw-admin quota get --quota-scope=user --uid=<uid>`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --quota-scope=user --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---


[← RGW 配置概览](../OVERVIEW.md)
