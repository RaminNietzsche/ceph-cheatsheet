# Users & per-user settings

RGW 配置深度指南 — 5 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_user_counters_cache](#rgw_user_counters_cache) | `False` | Dev | Performance |
| [rgw_user_counters_cache_size](#rgw_user_counters_cache_size) | `10000` | Advanced | Performance |
| [rgw_user_max_buckets](#rgw_user_max_buckets) | `1000` | Basic | Policy |
| [rgw_user_policies_max_num](#rgw_user_policies_max_num) | `100` | Advanced | Policy |
| [rgw_user_unique_email](#rgw_user_unique_email) | `True` | Basic | Policy |

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

### rgw_user_counters_cache

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rgw.md#SP_rgw_user_counters_cache](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache) |

**作用：** enable a rgw perf counters cache for counters with user label

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_user_counters_cache true
ceph config get client.rgw rgw_user_counters_cache
ceph config set client.rgw rgw_user_counters_cache_size 20000
```

**寻找最优值：**

**调优模型：** Performance

1. Default `False` — enable only when you consume the related per-label metrics.
2. If enabling, set the paired `*_cache_size` to match monitored entities.
3. Disable if memory is constrained and metrics are unused.

---

### rgw_user_counters_cache_size

| | |
|---|---|
| 类型 | Uint · default `10000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_counters_cache_size](../../../config/rgw/rgw.md#SP_rgw_user_counters_cache_size) |

**作用：** Number of labeled perf counters the user perf counters cache can store

**何时使用：**

- **Increase** when monitoring many active buckets/users and cache misses are visible.
- **Decrease** when RGW memory is constrained.

**示例：**

```bash
ceph config set client.rgw rgw_user_counters_cache_size 10000
ceph config get client.rgw rgw_user_counters_cache_size
```

**寻找最优值：**

**调优模型：** Performance

1. Size to the **active** working set (monitored buckets/users/tokens), not total catalog size.
2. Start at `10000`; sweep upward in ~2× steps.
3. Watch RGW RSS and cache hit behavior; use smallest size that avoids hot-path misses.

**观测信号：** rising RGW memory, repeated metadata lookups in logs.

```bash
ceph config get client.rgw rgw_user_counters_cache_size
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_user_max_buckets

| | |
|---|---|
| 类型 | Int · default `1000` · **Basic** |
| 表格 | [rgw.md#SP_rgw_user_max_buckets](../../../config/rgw/rgw.md#SP_rgw_user_max_buckets) |

**作用：** Max number of buckets per user

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_user_max_buckets 1000
ceph config get client.rgw rgw_user_max_buckets
radosgw-admin user create --uid=newuser --display-name="New User"
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_policies_max_num

| | |
|---|---|
| 类型 | Int · default `100` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_user_policies_max_num](../../../config/rgw/rgw.md#SP_rgw_user_policies_max_num) |

**作用：** The maximum number of IAM user policies for a single user.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_user_policies_max_num 100
ceph config get client.rgw rgw_user_policies_max_num
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `100` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_user_unique_email

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [rgw.md#SP_rgw_user_unique_email](../../../config/rgw/rgw.md#SP_rgw_user_unique_email) |

**作用：** Require local RGW users to have unique email addresses

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_user_unique_email false
ceph config get client.rgw rgw_user_unique_email
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
