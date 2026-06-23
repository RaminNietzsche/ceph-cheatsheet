# Motr backend

RGW 配置深度指南 — 7 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [motr_admin_endpoint](#motr_admin_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_admin_fid](#motr_admin_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_ha_endpoint](#motr_ha_endpoint) | `192.168.180.182@tcp:12345:1:1` | Advanced | Architecture |
| [motr_my_endpoint](#motr_my_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_my_fid](#motr_my_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_profile_fid](#motr_profile_fid) | `0x7000000000000001:0x0` | Advanced | Architecture |
| [motr_tracing_enabled](#motr_tracing_enabled) | `False` | Advanced | Dev |

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

### motr_admin_endpoint

| | |
|---|---|
| 类型 | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| 表格 | [motr.md#SP_motr_admin_endpoint](../../../config/rgw/motr.md#SP_motr_admin_endpoint) |

**作用：** experimental Option to set Admin Motr endpoint address

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_admin_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_admin_endpoint
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_admin_fid

| | |
|---|---|
| 类型 | Str · default `0x7200000000000001:0x0` · **Advanced** |
| 表格 | [motr.md#SP_motr_admin_fid](../../../config/rgw/motr.md#SP_motr_admin_fid) |

**作用：** Admin Tool Motr FID for admin-level access.

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_admin_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_admin_fid
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_ha_endpoint

| | |
|---|---|
| 类型 | Str · default `192.168.180.182@tcp:12345:1:1` · **Advanced** |
| 表格 | [motr.md#SP_motr_ha_endpoint](../../../config/rgw/motr.md#SP_motr_ha_endpoint) |

**作用：** experimental Option to set Motr HA agent endpoint address

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_ha_endpoint "192.168.180.182@tcp:12345:1:1"
ceph config get client.rgw motr_ha_endpoint
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:1:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_endpoint

| | |
|---|---|
| 类型 | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| 表格 | [motr.md#SP_motr_my_endpoint](../../../config/rgw/motr.md#SP_motr_my_endpoint) |

**作用：** experimental Option to set my Motr endpoint address

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_my_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_my_endpoint
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_fid

| | |
|---|---|
| 类型 | Str · default `0x7200000000000001:0x0` · **Advanced** |
| 表格 | [motr.md#SP_motr_my_fid](../../../config/rgw/motr.md#SP_motr_my_fid) |

**作用：** experimental Option to set my Motr fid

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_my_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_my_fid
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_profile_fid

| | |
|---|---|
| 类型 | Str · default `0x7000000000000001:0x0` · **Advanced** |
| 表格 | [motr.md#SP_motr_profile_fid](../../../config/rgw/motr.md#SP_motr_profile_fid) |

**作用：** experimental Option to set Motr profile fid

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_profile_fid "0x7000000000000001:0x0"
ceph config get client.rgw motr_profile_fid
```

**寻找最优值：**

**调优模型：** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7000000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_tracing_enabled

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [motr.md#SP_motr_tracing_enabled](../../../config/rgw/motr.md#SP_motr_tracing_enabled) |

**作用：** Set to true when Motr client debugging is needed

**何时使用：** 实验性 Motr/POSIX RGW 后端 — 仅用于专用 PoC 部署。

**示例：**

```bash
ceph config set client.rgw motr_tracing_enabled true
ceph config get client.rgw motr_tracing_enabled
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---


[← RGW 配置概览](../OVERVIEW.md)
