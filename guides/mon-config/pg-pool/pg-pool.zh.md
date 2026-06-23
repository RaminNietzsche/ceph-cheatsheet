# PG & pool health

MON 配置深度指南 — 14 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/mon/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [mon_allow_pool_size_one](#mon_allow_pool_size_one) | `False` | Advanced | 策略 |
| [mon_clean_pg_upmaps_per_chunk](#mon_clean_pg_upmaps_per_chunk) | `256` | Dev | 开发 |
| [mon_max_pool_pg_num](#mon_max_pool_pg_num) | `64_K` | Advanced | 性能 |
| [mon_osd_prime_pg_temp](#mon_osd_prime_pg_temp) | `True` | Dev | 开发 |
| [mon_osd_prime_pg_temp_max_estimate](#mon_osd_prime_pg_temp_max_estimate) | `0.25` | Advanced | 性能 |
| [mon_osd_prime_pg_temp_max_time](#mon_osd_prime_pg_temp_max_time) | `0.5` | Dev | 开发 |
| [mon_stretch_pool_min_size](#mon_stretch_pool_min_size) | `2` | Dev | 开发 |
| [mon_stretch_pool_size](#mon_stretch_pool_size) | `4` | Dev | 开发 |
| [mon_warn_on_cache_pools_without_hit_sets](#mon_warn_on_cache_pools_without_hit_sets) | `True` | Advanced | 性能 |
| [mon_warn_on_pool_no_redundancy](#mon_warn_on_pool_no_redundancy) | `True` | Advanced | 性能 |
| [mon_warn_on_pool_pg_num_not_power_of_two](#mon_warn_on_pool_pg_num_not_power_of_two) | `True` | Dev | 开发 |
| [pool_availability_update_interval](#pool_availability_update_interval) | `1` | Advanced | 性能 |
| [osd_pool_default_crimson](#osd_pool_default_crimson) | `False` | Advanced | 性能 |
| [osd_pool_erasure_code_stripe_unit](#osd_pool_erasure_code_stripe_unit) | `0` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. mon
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mon_allow_pool_size_one

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [mon.md#SP_mon_allow_pool_size_one](../../../config/mon/mon.md#SP_mon_allow_pool_size_one) |

**作用：** Allow pools with `size=1` (no redundancy).

**何时使用：** Lab only. Keep `false` in production unless you accept data loss risk.

**示例：**

```bash
ceph config set mon mon_allow_pool_size_one true
ceph config get mon mon_allow_pool_size_one
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_allow_pool_size_one
ceph -s
ceph mon stat
```

---

### mon_clean_pg_upmaps_per_chunk

| | |
|---|---|
| 类型 | Uint · default `256` · **Dev** |
| 表格 | [mon.md#SP_mon_clean_pg_upmaps_per_chunk](../../../config/mon/mon.md#SP_mon_clean_pg_upmaps_per_chunk) |

**作用：** granularity of PG upmap validation background work

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_clean_pg_upmaps_per_chunk 256
ceph config get mon mon_clean_pg_upmaps_per_chunk
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`256`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_max_pool_pg_num

| | |
|---|---|
| 类型 | Uint · default `64_K` · **Advanced** |
| 表格 | [mon.md#SP_mon_max_pool_pg_num](../../../config/mon/mon.md#SP_mon_max_pool_pg_num) |

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_max_pool_pg_num 64_K
ceph config get mon mon_max_pool_pg_num
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_max_pool_pg_num
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mon.md#SP_mon_osd_prime_pg_temp](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp) |

**作用：** minimize peering work by priming pg_temp values after a map change

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_osd_prime_pg_temp false
ceph config get mon mon_osd_prime_pg_temp
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_osd_prime_pg_temp_max_estimate

| | |
|---|---|
| 类型 | Float · default `0.25` · **Advanced** |
| 表格 | [mon.md#SP_mon_osd_prime_pg_temp_max_estimate](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_estimate) |

**作用：** calculate all PG mappings if estimated fraction of PGs that change is above this amount

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_estimate 0.25
ceph config get mon mon_osd_prime_pg_temp_max_estimate
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.25` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_osd_prime_pg_temp_max_estimate
ceph -s
ceph mon stat
```

---

### mon_osd_prime_pg_temp_max_time

| | |
|---|---|
| 类型 | Float · default `0.5` · **Dev** |
| 表格 | [mon.md#SP_mon_osd_prime_pg_temp_max_time](../../../config/mon/mon.md#SP_mon_osd_prime_pg_temp_max_time) |

**作用：** maximum time to spend precalculating PG mappings on map change (seconds)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_osd_prime_pg_temp_max_time 0.5
ceph config get mon mon_osd_prime_pg_temp_max_time
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0.5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_stretch_pool_min_size

| | |
|---|---|
| 类型 | Uint · default `2` · **Dev** |
| 表格 | [mon.md#SP_mon_stretch_pool_min_size](../../../config/mon/mon.md#SP_mon_stretch_pool_min_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_stretch_pool_min_size 2
ceph config get mon mon_stretch_pool_min_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`2`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_stretch_pool_size

| | |
|---|---|
| 类型 | Uint · default `4` · **Dev** |
| 表格 | [mon.md#SP_mon_stretch_pool_size](../../../config/mon/mon.md#SP_mon_stretch_pool_size) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_stretch_pool_size 4
ceph config get mon mon_stretch_pool_size
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`4`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### mon_warn_on_cache_pools_without_hit_sets

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_cache_pools_without_hit_sets](../../../config/mon/mon.md#SP_mon_warn_on_cache_pools_without_hit_sets) |

**作用：** issue CACHE_POOL_NO_HIT_SET health warning for cache pools that do not have hit sets configured

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set mon mon_warn_on_cache_pools_without_hit_sets false
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_cache_pools_without_hit_sets
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_no_redundancy

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [mon.md#SP_mon_warn_on_pool_no_redundancy](../../../config/mon/mon.md#SP_mon_warn_on_pool_no_redundancy) |

**作用：** Warn when any pool has no redundancy (`size=1` or `min_size=1`).

**何时使用：** Leave enabled in production.

**示例：**

```bash
ceph config set mon mon_warn_on_pool_no_redundancy false
ceph config get mon mon_warn_on_pool_no_redundancy
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon mon_warn_on_pool_no_redundancy
ceph -s
ceph mon stat
```

---

### mon_warn_on_pool_pg_num_not_power_of_two

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two](../../../config/mon/mon.md#SP_mon_warn_on_pool_pg_num_not_power_of_two) |

**作用：** issue POOL_PG_NUM_NOT_POWER_OF_TWO warning if pool has a non-power-of-two pg_num value

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set mon mon_warn_on_pool_pg_num_not_power_of_two false
ceph config get mon mon_warn_on_pool_pg_num_not_power_of_two
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### pool_availability_update_interval

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [mon.md#SP_pool_availability_update_interval](../../../config/mon/mon.md#SP_pool_availability_update_interval) |

**作用：** Update data availability score at this interval. By default the interval is same as paxos_propose_interval configuration.

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set mon pool_availability_update_interval 1
ceph config get mon pool_availability_update_interval
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get mon pool_availability_update_interval
ceph -s
ceph mon stat
```

---

### osd_pool_default_crimson

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_default_crimson](../../../config/mon/osd.md#SP_osd_pool_default_crimson) |

**作用：** Create pools by default with FLAG_CRIMSON

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set osd osd_pool_default_crimson true
ceph config get osd osd_pool_default_crimson
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_pool_default_crimson
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---

### osd_pool_erasure_code_stripe_unit

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [osd.md#SP_osd_pool_erasure_code_stripe_unit](../../../config/mon/osd.md#SP_osd_pool_erasure_code_stripe_unit) |

**作用：** the amount of data (in bytes) in a data chunk, per stripe

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set osd osd_pool_erasure_code_stripe_unit 64
ceph config get osd osd_pool_erasure_code_stripe_unit
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get osd osd_pool_erasure_code_stripe_unit
ceph -s
ceph daemon osd.<id> perf dump | head
ceph pg stat
```

---


[← 概览](../OVERVIEW.md)
