# Lua scripting

RGW 配置深度指南 — 4 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_lua_enable](#rgw_lua_enable) | `True` | Advanced | 策略 |
| [rgw_lua_max_memory_per_state](#rgw_lua_max_memory_per_state) | `128000` | Advanced | 策略 |
| [rgw_lua_max_runtime_per_state](#rgw_lua_max_runtime_per_state) | `1000` | Advanced | 策略 |
| [rgw_luarocks_location](#rgw_luarocks_location) | `/tmp/rgw_luarocks/$name` | Advanced | 性能 |

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

### rgw_lua_enable

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_lua_enable](../../../config/rgw/rgw.md#SP_rgw_lua_enable) |

**作用：** Enable lua scripting.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set client.rgw rgw_lua_enable false
ceph config get client.rgw rgw_lua_enable
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_lua_max_memory_per_state

| | |
|---|---|
| 类型 | Uint · default `128000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lua_max_memory_per_state](../../../config/rgw/rgw.md#SP_rgw_lua_max_memory_per_state) |

**作用：** Max size of memory used by a single lua state This is the maximum size in bytes that a lua state can allocate for its own use. Note that this does not include any memory that can be accessed from lua, but managed by the RGW. If not set, it would use a default of 128K. If set to zero, the amount of memory would only be limited by the system.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lua_max_memory_per_state 128000
ceph config get client.rgw rgw_lua_max_memory_per_state
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `128000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lua_max_runtime_per_state

| | |
|---|---|
| 类型 | Uint · default `1000` · **Advanced** |
| 表格 | [rgw.md#SP_rgw_lua_max_runtime_per_state](../../../config/rgw/rgw.md#SP_rgw_lua_max_runtime_per_state) |

**作用：** Maximum runtime for each Lua state in milliseconds Sets the maximum runtime for each Lua state in milliseconds. If exceeded, the script will be terminated. Defaults to 1000 milliseconds (1 second). If set to zero, there is no limit.

**何时使用：** 客户端触及请求大小/并发限制，或保护集群资源时调整。

**示例：**

```bash
ceph config set client.rgw rgw_lua_max_runtime_per_state 1000
ceph config get client.rgw rgw_lua_max_runtime_per_state
```

**寻找最优值：**

**调优模型：** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_luarocks_location

| | |
|---|---|
| 类型 | Str · default `/tmp/rgw_luarocks/$name` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [rgw.md#SP_rgw_luarocks_location](../../../config/rgw/rgw.md#SP_rgw_luarocks_location) |

**作用：** Directory where luarocks install packages from allowlist

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client.rgw rgw_luarocks_location "/tmp/rgw_luarocks/$name"
ceph config get client.rgw rgw_luarocks_location
ceph orch restart rgw
```

**寻找最优值：**

**调优模型：** Performance

1. Baseline at upstream default `/tmp/rgw_luarocks/$name`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**观测信号：** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_luarocks_location
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---


[← RGW 配置概览](../OVERVIEW.md)
