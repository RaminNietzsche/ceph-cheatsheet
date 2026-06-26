# Feature toggles

RGW 配置深度指南 — 10 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_disable_s3select](#rgw_disable_s3select) | `False` | Advanced | 策略 |
| [rgw_enable_apis](#rgw_enable_apis) | `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` | Advanced | 性能 |
| [rgw_enable_gc_threads](#rgw_enable_gc_threads) | `True` | Advanced | 策略 |
| [rgw_enable_jwks_url_verification](#rgw_enable_jwks_url_verification) | `False` | Advanced | 策略 |
| [rgw_enable_lc_threads](#rgw_enable_lc_threads) | `True` | Advanced | 策略 |
| [rgw_enable_mdsearch](#rgw_enable_mdsearch) | `True` | Basic | 策略 |
| [rgw_enable_ops_log](#rgw_enable_ops_log) | `False` | Advanced | 策略 |
| [rgw_enable_restore_threads](#rgw_enable_restore_threads) | `True` | Advanced | 策略 |
| [rgw_enable_static_website](#rgw_enable_static_website) | `False` | Basic | 策略 |
| [rgw_enable_usage_log](#rgw_enable_usage_log) | `False` | Advanced | 策略 |

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

### rgw_disable_s3select

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_disable_s3select](../../../config/rgw/rgw.md#SP_rgw_disable_s3select) |

**作用：** disable the s3select operation; RGW will report an error and will return ERR_INVALID_REQUEST.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_disable_s3select true
ceph config get client.rgw rgw_disable_s3select
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_apis

| | |
|---|---|
| 类型 | Str · default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_apis](../../../config/rgw/rgw.md#SP_rgw_enable_apis) |

**作用：** A list of RESTful APIs for RGW to enable

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_enable_apis "s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications"
ceph config get client.rgw rgw_enable_apis
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_enable_apis
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_enable_gc_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_gc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_gc_threads) |

**作用：** Enables the garbage collection maintenance thread. The garbage collection maintenance thread is responsible for garbage collector maintenance work. The thread itself can be disabled, but in order for garbage collection to work correctly, at least one RGW in each zone needs to have this thread running. Having the thread enabled on multiple RGW processes within the same zone can spread some of the maintenance work between them.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_gc_threads false
ceph config get client.rgw rgw_enable_gc_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_jwks_url_verification

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_jwks_url_verification](../../../config/rgw/rgw.md#SP_rgw_enable_jwks_url_verification) |

**作用：** Enable JWKS url verification for AWS compliance Verifies the security of the JWKS url endpoint using the client provided thumbprints for AWS compliance. If turned on, the legacy verification option of using thumbprints to verify JWT x5c certs is disabled.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_jwks_url_verification true
ceph config get client.rgw rgw_enable_jwks_url_verification
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_lc_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_lc_threads](../../../config/rgw/rgw.md#SP_rgw_enable_lc_threads) |

**作用：** Enables the lifecycle maintenance thread. This is required on at least one RGW daemon for each zone. The lifecycle maintenance thread is responsible for lifecycle related maintenance work. The thread itself can be disabled, but in order for lifecycle to work correctly, at least one RGW in each zone needs to have this thread running. Having the thread enabled on multiple RGW processes within the same zone can spread some of the maintenance work between them.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_lc_threads false
ceph config get client.rgw rgw_enable_lc_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_mdsearch

| | |
|---|---|
| 类型 | Bool · default `True` · **Basic** |
| 表格 | [rgw.md#SP_rgw_enable_mdsearch](../../../config/rgw/rgw.md#SP_rgw_enable_mdsearch) |

**作用：** Enable elastic metadata search APIs This configurable controls whether RGW enables the elastic metadata search APIs.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_mdsearch false
ceph config get client.rgw rgw_enable_mdsearch
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_ops_log

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_ops_log](../../../config/rgw/rgw.md#SP_rgw_enable_ops_log) |

**作用：** Enable ops log

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_ops_log true
ceph config get client.rgw rgw_enable_ops_log
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_restore_threads

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_restore_threads](../../../config/rgw/rgw.md#SP_rgw_enable_restore_threads) |

**作用：** Enables the objects' restore maintenance thread. The objects restore maintenance thread is responsible for all the objects restoration related maintenance work. The thread itself can be disabled, but in order for the restore from the cloud to work correctly, at least one RGW in each zone needs to have this thread running. Having the thread enabled on multiple RGW processes within the same zone can spread some of the maintenance work between them.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_restore_threads false
ceph config get client.rgw rgw_enable_restore_threads
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_static_website

| | |
|---|---|
| 类型 | Bool · default `False` · **Basic** |
| 表格 | [rgw.md#SP_rgw_enable_static_website](../../../config/rgw/rgw.md#SP_rgw_enable_static_website) |

**作用：** Enable static website APIs This configurable controls whether RGW enables the website control APIs. RGW can serve static websites if S3 website hostnames are configured.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set client.rgw rgw_enable_static_website true
ceph config get client.rgw rgw_enable_static_website
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_enable_usage_log

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_enable_usage_log](../../../config/rgw/rgw.md#SP_rgw_enable_usage_log) |

**作用：** Enable the usage log

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**相关选项：**

- [`rgw_usage_max_shards`](../../../config/rgw/rgw.md#SP_rgw_usage_max_shards)

**示例：**

```bash
ceph config set client.rgw rgw_enable_usage_log true
ceph config get client.rgw rgw_enable_usage_log
```

**寻找最优值：**

**调优模型：** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW 配置概览](../OVERVIEW.md)
