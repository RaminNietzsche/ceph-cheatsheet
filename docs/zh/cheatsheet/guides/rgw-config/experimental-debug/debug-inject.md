# Debug & fault injection

RGW 配置深度指南 — 7 个选项。[← RGW 配置概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rgw_debug_inject_latency_bi_unlink](#rgw_debug_inject_latency_bi_unlink) | `0` | Dev | 开发 |
| [rgw_debug_inject_olh_cancel_modification_err](#rgw_debug_inject_olh_cancel_modification_err) | `False` | Dev | 开发 |
| [rgw_debug_inject_set_olh_err](#rgw_debug_inject_set_olh_err) | `0` | Dev | 开发 |
| [rgw_inject_delay_pattern](#rgw_inject_delay_pattern) | `(empty)` | Dev | 开发 |
| [rgw_inject_delay_sec](#rgw_inject_delay_sec) | `0` | Dev | 开发 |
| [rgw_mp_lock_inject_delay](#rgw_mp_lock_inject_delay) | `0` | Dev | 开发 |
| [rgw_mp_lock_inject_renewal_error](#rgw_mp_lock_inject_renewal_error) | `0` | Dev | 开发 |

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

### rgw_debug_inject_latency_bi_unlink

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_debug_inject_latency_bi_unlink](../../../config/rgw/rgw.md#SP_rgw_debug_inject_latency_bi_unlink) |

**作用：** Latency (in seconds) injected before rgw bucket index unlink op calls to simulate queueing latency and validate behavior of simultaneous delete requests which target the same object.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_debug_inject_latency_bi_unlink 0
ceph config get client.rgw rgw_debug_inject_latency_bi_unlink
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_debug_inject_olh_cancel_modification_err

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err](../../../config/rgw/rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err) |

**作用：** Whether to inject an error to simulate a failure to cancel olh modification. This exists for development and testing purposes.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_debug_inject_olh_cancel_modification_err true
ceph config get client.rgw rgw_debug_inject_olh_cancel_modification_err
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_debug_inject_set_olh_err

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_debug_inject_set_olh_err](../../../config/rgw/rgw.md#SP_rgw_debug_inject_set_olh_err) |

**作用：** Whether to inject errors between rados olh modification initialization and bucket index instance linking. The value determines the error code. This exists for development and testing purposes to help simulate cases where bucket index entries aren't cleaned up by the request thread after an error scenario.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_debug_inject_set_olh_err 0
ceph config get client.rgw rgw_debug_inject_set_olh_err
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_inject_delay_pattern

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [rgw.md#SP_rgw_inject_delay_pattern](../../../config/rgw/rgw.md#SP_rgw_inject_delay_pattern) |

**作用：** select which delay injection points are activated Used together with `rgw_inject_delay_sec` to target specific delay injection points within the RGW code. The pattern should match a string associated with one or more delay locations (e.g., "delay_bucket_full_sync_loop") to activate them during testing.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rgw_inject_delay_sec`](../../../config/rgw/rgw.md#SP_rgw_inject_delay_sec)

**示例：**

```bash
ceph config set client.rgw rgw_inject_delay_pattern <value>
ceph config get client.rgw rgw_inject_delay_pattern
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`(empty)`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_inject_delay_sec

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_inject_delay_sec](../../../config/rgw/rgw.md#SP_rgw_inject_delay_sec) |

**作用：** delay duration in seconds for test injection points Intended for integration and stress testing. When set to a positive value, this option introduces an artificial delay at specific code paths to help deterministically reproduce timing-sensitive scenarios. It is used in conjunction with `rgw_inject_delay_pattern` to control which delay points are activated.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**相关选项：**

- [`rgw_inject_delay_pattern`](../../../config/rgw/rgw.md#SP_rgw_inject_delay_pattern)

**示例：**

```bash
ceph config set client.rgw rgw_inject_delay_sec 0
ceph config get client.rgw rgw_inject_delay_sec
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_mp_lock_inject_delay

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_mp_lock_inject_delay](../../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_delay) |

**作用：** Injected delay after acquiring the multipart lock for renewal testing

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_mp_lock_inject_delay 0
ceph config get client.rgw rgw_mp_lock_inject_delay
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---

### rgw_mp_lock_inject_renewal_error

| | |
|---|---|
| 类型 | Int · default `0` · **Dev** |
| 表格 | [rgw.md#SP_rgw_mp_lock_inject_renewal_error](../../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_renewal_error) |

**作用：** Injected error code for multipart lock renewal testing

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set client.rgw rgw_mp_lock_inject_renewal_error 0
ceph config get client.rgw rgw_mp_lock_inject_renewal_error
```

**寻找最优值：**

**调优模型：** Dev

1. Keep the upstream default (`0`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**观测信号：** assertion failures, injected errors, or trace noise in logs.

---


[← RGW 配置概览](../OVERVIEW.md)
