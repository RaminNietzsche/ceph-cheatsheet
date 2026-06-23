# Defaults

RBD 配置深度指南 — 10 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/rbd/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [rbd_default_clone_format](#rbd_default_clone_format) | `auto` | Advanced | 性能 |
| [rbd_default_data_pool](#rbd_default_data_pool) | `(empty)` | Advanced | 性能 |
| [rbd_default_features](#rbd_default_features) | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` | Advanced | 性能 |
| [rbd_default_format](#rbd_default_format) | `2` | Advanced | 性能 |
| [rbd_default_map_options](#rbd_default_map_options) | `(empty)` | Advanced | 性能 |
| [rbd_default_order](#rbd_default_order) | `22` | Advanced | 性能 |
| [rbd_default_pool](#rbd_default_pool) | `rbd` | Advanced | 性能 |
| [rbd_default_snapshot_quiesce_mode](#rbd_default_snapshot_quiesce_mode) | `required` | Advanced | 性能 |
| [rbd_default_stripe_count](#rbd_default_stripe_count) | `0` | Advanced | 性能 |
| [rbd_default_stripe_unit](#rbd_default_stripe_unit) | `0` | Advanced | 性能 |

## 寻找最优值

| 模型 | 如何选择 |
|-------|---------------|
| **策略** | 安全、兼容性、运维默认值 |
| **容量** | 磁盘布局、路径、容量规划 |
| **性能** | 基线 → 逐步调整 → 监控集群 |
| **连通性** | 最近且稳定的外部端点 |
| **开发** | 生产环境保持 upstream 默认值 |

**常用工具：**

```bash
ceph config get <daemon> <option>  # e.g. rbd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### rbd_default_clone_format

| | |
|---|---|
| 类型 | Str · enum: ["1", "2", "auto"] · default `auto` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_clone_format](../../../config/rbd/rbd.md#SP_rbd_default_clone_format) |

**作用：** default internal format for handling clones

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_clone_format auto
ceph config get client rbd_default_clone_format
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `auto` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_clone_format
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_data_pool

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_data_pool](../../../config/rbd/rbd.md#SP_rbd_default_data_pool) |

**作用：** default pool for storing data blocks for new images &#91;&#93;(std::string *value, std::string *error_message) { std::regex pattern("^&#91;^@/&#93;*$"); if (!std::regex_match (*value, pattern)) { *value = ""; *error_message = "ignoring invalid RBD data pool"; } return 0; }

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_data_pool "example"
ceph config get client rbd_default_data_pool
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_data_pool
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_features

| | |
|---|---|
| 类型 | Str · default `layering,exclusive-lock,object-map,fast-diff,deep-flatten` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_features](../../../config/rbd/rbd.md#SP_rbd_default_features) |

**作用：** default v2 image features for new images &#91;&#93;(std::string *value, std::string *error_message) { std::stringstream ss; uint64_t features = librbd::rbd_features_from_string(*value, &ss); // Leave this in integer form to avoid breaking Cinder. Someday // we would like to present this in string form instead... *value = stringify(features); if (ss.str().size()) { return -EINVAL; } return 0; }

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_features "layering,exclusive-lock,object-map,fast-diff,deep-flatten"
ceph config get client rbd_default_features
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `layering,exclusive-lock,object-map,fast-diff,deep-flatten` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_features
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_format

| | |
|---|---|
| 类型 | Uint · default `2` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_format](../../../config/rbd/rbd.md#SP_rbd_default_format) |

**作用：** default image format for new images

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_format 2
ceph config get client rbd_default_format
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_format
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_map_options

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_map_options](../../../config/rbd/rbd.md#SP_rbd_default_map_options) |

**作用：** default krbd map options

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_map_options "example"
ceph config get client rbd_default_map_options
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_map_options
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_order

| | |
|---|---|
| 类型 | Uint · default `22` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_order](../../../config/rbd/rbd.md#SP_rbd_default_order) |

**作用：** default order (data block object size) for new images

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_order 22
ceph config get client rbd_default_order
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `22` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_order
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_pool

| | |
|---|---|
| 类型 | Str · default `rbd` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_pool](../../../config/rbd/rbd.md#SP_rbd_default_pool) |

**作用：** default pool for storing new images &#91;&#93;(std::string *value, std::string *error_message) { std::regex pattern("^&#91;^@/&#93;+$"); if (!std::regex_match (*value, pattern)) { *value = "rbd"; *error_message = "invalid RBD default pool, resetting to 'rbd'"; } return 0; }

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_pool rbd
ceph config get client rbd_default_pool
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `rbd` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_pool
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_snapshot_quiesce_mode

| | |
|---|---|
| 类型 | Str · enum: ["required", "ignore-error", "skip"] · default `required` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_snapshot_quiesce_mode](../../../config/rbd/rbd.md#SP_rbd_default_snapshot_quiesce_mode) |

**作用：** default snapshot quiesce mode

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_snapshot_quiesce_mode required
ceph config get client rbd_default_snapshot_quiesce_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `required` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_snapshot_quiesce_mode
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_stripe_count

| | |
|---|---|
| 类型 | Uint · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_stripe_count](../../../config/rbd/rbd.md#SP_rbd_default_stripe_count) |

**作用：** default stripe count for new images

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_stripe_count 64
ceph config get client rbd_default_stripe_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_stripe_count
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---

### rbd_default_stripe_unit

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [rbd.md#SP_rbd_default_stripe_unit](../../../config/rbd/rbd.md#SP_rbd_default_stripe_unit) |

**作用：** default stripe width for new images

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set client rbd_default_stripe_unit 64
ceph config get client rbd_default_stripe_unit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get client rbd_default_stripe_unit
ceph -s
# client 选项：在 client 段或 ceph.conf 中设置
```

---


[← 概览](../OVERVIEW.md)
