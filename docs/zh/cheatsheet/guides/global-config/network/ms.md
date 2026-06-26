# Ms

Global 配置深度指南 — 91 个选项。[← 概览](../OVERVIEW.md) · [调优索引](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| 选项 | 默认值 | 级别 | 调优 |
|--------|---------|-------|--------|
| [ms_async_op_threads](#ms_async_op_threads) | `3` | Advanced | 性能 |
| [ms_async_rdma_buffer_size](#ms_async_rdma_buffer_size) | `128_K` | Advanced | 性能 |
| [ms_async_rdma_cm](#ms_async_rdma_cm) | `False` | Advanced | 性能 |
| [ms_async_rdma_device_name](#ms_async_rdma_device_name) | `(empty)` | Advanced | 性能 |
| [ms_async_rdma_dscp](#ms_async_rdma_dscp) | `96` | Advanced | 性能 |
| [ms_async_rdma_enable_hugepage](#ms_async_rdma_enable_hugepage) | `False` | Advanced | 策略 |
| [ms_async_rdma_gid_idx](#ms_async_rdma_gid_idx) | `0` | Advanced | 性能 |
| [ms_async_rdma_local_gid](#ms_async_rdma_local_gid) | `(empty)` | Advanced | 性能 |
| [ms_async_rdma_polling_us](#ms_async_rdma_polling_us) | `1000` | Advanced | 性能 |
| [ms_async_rdma_port_num](#ms_async_rdma_port_num) | `1` | Advanced | 性能 |
| [ms_async_rdma_receive_buffers](#ms_async_rdma_receive_buffers) | `32_K` | Advanced | 性能 |
| [ms_async_rdma_receive_queue_len](#ms_async_rdma_receive_queue_len) | `4_K` | Advanced | 性能 |
| [ms_async_rdma_roce_ver](#ms_async_rdma_roce_ver) | `1` | Advanced | 性能 |
| [ms_async_rdma_send_buffers](#ms_async_rdma_send_buffers) | `1_K` | Advanced | 性能 |
| [ms_async_rdma_sl](#ms_async_rdma_sl) | `3` | Advanced | 性能 |
| [ms_async_rdma_support_srq](#ms_async_rdma_support_srq) | `True` | Advanced | 性能 |
| [ms_async_rdma_type](#ms_async_rdma_type) | `ib` | Advanced | 性能 |
| [ms_async_reap_threshold](#ms_async_reap_threshold) | `5` | Dev | 开发 |
| [ms_bind_before_connect](#ms_bind_before_connect) | `False` | Advanced | 性能 |
| [ms_bind_ipv4](#ms_bind_ipv4) | `True` | Advanced | 性能 |
| [ms_bind_ipv6](#ms_bind_ipv6) | `False` | Advanced | 性能 |
| [ms_bind_msgr1](#ms_bind_msgr1) | `True` | Advanced | 性能 |
| [ms_bind_msgr2](#ms_bind_msgr2) | `True` | Advanced | 性能 |
| [ms_bind_port_max](#ms_bind_port_max) | `7568` | Advanced | 性能 |
| [ms_bind_port_min](#ms_bind_port_min) | `6800` | Advanced | 性能 |
| [ms_bind_prefer_ipv4](#ms_bind_prefer_ipv4) | `False` | Advanced | 性能 |
| [ms_bind_retry_count](#ms_bind_retry_count) | `0` | Advanced | 性能 |
| [ms_bind_retry_delay](#ms_bind_retry_delay) | `0` | Advanced | 性能 |
| [ms_blackhole_client](#ms_blackhole_client) | `False` | Dev | 开发 |
| [ms_blackhole_mds](#ms_blackhole_mds) | `False` | Dev | 开发 |
| [ms_blackhole_mgr](#ms_blackhole_mgr) | `False` | Dev | 开发 |
| [ms_blackhole_mon](#ms_blackhole_mon) | `False` | Dev | 开发 |
| [ms_blackhole_osd](#ms_blackhole_osd) | `False` | Dev | 开发 |
| [ms_client_mode](#ms_client_mode) | `crc secure` | Basic | 策略 |
| [ms_client_throttle_retry_time_interval](#ms_client_throttle_retry_time_interval) | `5000` | Dev | 开发 |
| [ms_cluster_mode](#ms_cluster_mode) | `crc secure` | Basic | 策略 |
| [ms_cluster_type](#ms_cluster_type) | `(empty)` | Advanced | 性能 |
| [ms_compress_secure](#ms_compress_secure) | `False` | Advanced | 性能 |
| [ms_connection_idle_timeout](#ms_connection_idle_timeout) | `900` | Advanced | 性能 |
| [ms_connection_ready_timeout](#ms_connection_ready_timeout) | `10` | Advanced | 性能 |
| [ms_crc_data](#ms_crc_data) | `True` | Dev | 开发 |
| [ms_crc_header](#ms_crc_header) | `True` | Dev | 开发 |
| [ms_die_on_bad_msg](#ms_die_on_bad_msg) | `False` | Dev | 开发 |
| [ms_die_on_bug](#ms_die_on_bug) | `False` | Dev | 开发 |
| [ms_die_on_old_message](#ms_die_on_old_message) | `False` | Dev | 开发 |
| [ms_die_on_skipped_message](#ms_die_on_skipped_message) | `False` | Dev | 开发 |
| [ms_die_on_unhandled_msg](#ms_die_on_unhandled_msg) | `False` | Dev | 开发 |
| [ms_dispatch_throttle_bytes](#ms_dispatch_throttle_bytes) | `100_M` | Advanced | 性能 |
| [ms_dpdk_coremask](#ms_dpdk_coremask) | `0xF` | Advanced | 性能 |
| [ms_dpdk_debug_allow_loopback](#ms_dpdk_debug_allow_loopback) | `False` | Dev | 开发 |
| [ms_dpdk_devs_allowlist](#ms_dpdk_devs_allowlist) | `(empty)` | Advanced | 性能 |
| [ms_dpdk_enable_tso](#ms_dpdk_enable_tso) | `True` | Advanced | 策略 |
| [ms_dpdk_gateway_ipv4_addr](#ms_dpdk_gateway_ipv4_addr) | `(empty)` | Advanced | 连通性 |
| [ms_dpdk_host_ipv4_addr](#ms_dpdk_host_ipv4_addr) | `(empty)` | Advanced | 连通性 |
| [ms_dpdk_hugepages](#ms_dpdk_hugepages) | `(empty)` | Advanced | 性能 |
| [ms_dpdk_hw_flow_control](#ms_dpdk_hw_flow_control) | `True` | Advanced | 性能 |
| [ms_dpdk_hw_queue_weight](#ms_dpdk_hw_queue_weight) | `1` | Advanced | 性能 |
| [ms_dpdk_lro](#ms_dpdk_lro) | `True` | Advanced | 性能 |
| [ms_dpdk_memory_channel](#ms_dpdk_memory_channel) | `4` | Advanced | 性能 |
| [ms_dpdk_netmask_ipv4_addr](#ms_dpdk_netmask_ipv4_addr) | `(empty)` | Advanced | 连通性 |
| [ms_dpdk_pmd](#ms_dpdk_pmd) | `(empty)` | Advanced | 性能 |
| [ms_dpdk_port_id](#ms_dpdk_port_id) | `0` | Advanced | 性能 |
| [ms_dpdk_rx_buffer_count_per_core](#ms_dpdk_rx_buffer_count_per_core) | `8192` | Advanced | 性能 |
| [ms_dump_corrupt_message_level](#ms_dump_corrupt_message_level) | `1` | Advanced | 性能 |
| [ms_dump_on_send](#ms_dump_on_send) | `False` | Advanced | 性能 |
| [ms_initial_backoff](#ms_initial_backoff) | `0.2` | Advanced | 性能 |
| [ms_inject_delay_max](#ms_inject_delay_max) | `1` | Dev | 开发 |
| [ms_inject_delay_probability](#ms_inject_delay_probability) | `0` | Dev | 开发 |
| [ms_inject_delay_type](#ms_inject_delay_type) | `(empty)` | Dev | 开发 |
| [ms_inject_internal_delays](#ms_inject_internal_delays) | `0` | Dev | 开发 |
| [ms_inject_network_congestion](#ms_inject_network_congestion) | `0` | Dev | 开发 |
| [ms_inject_socket_failures](#ms_inject_socket_failures) | `0` | Dev | 开发 |
| [ms_learn_addr_from_peer](#ms_learn_addr_from_peer) | `True` | Advanced | 性能 |
| [ms_max_accept_failures](#ms_max_accept_failures) | `4` | Advanced | 性能 |
| [ms_max_backoff](#ms_max_backoff) | `15` | Advanced | 性能 |
| [ms_mon_client_mode](#ms_mon_client_mode) | `secure crc` | Basic | 策略 |
| [ms_mon_cluster_mode](#ms_mon_cluster_mode) | `secure crc` | Basic | 策略 |
| [ms_mon_service_mode](#ms_mon_service_mode) | `secure crc` | Basic | 策略 |
| [ms_osd_compress_min_size](#ms_osd_compress_min_size) | `1_K` | Advanced | 性能 |
| [ms_osd_compress_mode](#ms_osd_compress_mode) | `none` | Advanced | 性能 |
| [ms_osd_compression_algorithm](#ms_osd_compression_algorithm) | `snappy` | Advanced | 性能 |
| [ms_pq_max_tokens_per_priority](#ms_pq_max_tokens_per_priority) | `16_M` | Dev | 开发 |
| [ms_pq_min_cost](#ms_pq_min_cost) | `64_K` | Dev | 开发 |
| [ms_public_type](#ms_public_type) | `(empty)` | Advanced | 性能 |
| [ms_service_mode](#ms_service_mode) | `crc secure` | Basic | 策略 |
| [ms_tcp_listen_backlog](#ms_tcp_listen_backlog) | `512` | Advanced | 性能 |
| [ms_tcp_nodelay](#ms_tcp_nodelay) | `True` | Advanced | 性能 |
| [ms_tcp_prefetch_max_size](#ms_tcp_prefetch_max_size) | `64_K` | Advanced | 性能 |
| [ms_tcp_rcvbuf](#ms_tcp_rcvbuf) | `0` | Advanced | 性能 |
| [ms_time_events_min_wait_interval](#ms_time_events_min_wait_interval) | `1000` | Dev | 开发 |
| [ms_type](#ms_type) | `async+posix` | Advanced | 性能 |

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
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### ms_async_op_threads

| | |
|---|---|
| 类型 | Uint · default `3` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_op_threads](../../../config/global/ms.md#SP_ms_async_op_threads) |

**作用：** Threadpool size for AsyncMessenger (ms_type=async)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_op_threads 3
ceph config get global ms_async_op_threads
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。

**边界：** 最小 `1`，最大 `24`。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_op_threads
ceph -s
```

---

### ms_async_rdma_buffer_size

| | |
|---|---|
| 类型 | Size · default `128_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_buffer_size](../../../config/global/ms.md#SP_ms_async_rdma_buffer_size) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_buffer_size 128_K
ceph config get global ms_async_rdma_buffer_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `128_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_buffer_size
ceph -s
```

---

### ms_async_rdma_cm

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_cm](../../../config/global/ms.md#SP_ms_async_rdma_cm) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global ms_async_rdma_cm true
ceph config get global ms_async_rdma_cm
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_cm
ceph -s
```

---

### ms_async_rdma_device_name

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_device_name](../../../config/global/ms.md#SP_ms_async_rdma_device_name) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_device_name "example"
ceph config get global ms_async_rdma_device_name
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_device_name
ceph -s
```

---

### ms_async_rdma_dscp

| | |
|---|---|
| 类型 | Int · default `96` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_dscp](../../../config/global/ms.md#SP_ms_async_rdma_dscp) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_dscp 96
ceph config get global ms_async_rdma_dscp
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `96` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_dscp
ceph -s
```

---

### ms_async_rdma_enable_hugepage

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_enable_hugepage](../../../config/global/ms.md#SP_ms_async_rdma_enable_hugepage) |

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global ms_async_rdma_enable_hugepage true
ceph config get global ms_async_rdma_enable_hugepage
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `False` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_enable_hugepage
ceph -s
```

---

### ms_async_rdma_gid_idx

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_gid_idx](../../../config/global/ms.md#SP_ms_async_rdma_gid_idx) |

**作用：** use gid_idx to select GID for choosing RoCEv1 or RoCEv2

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_gid_idx 64
ceph config get global ms_async_rdma_gid_idx
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_gid_idx
ceph -s
```

---

### ms_async_rdma_local_gid

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_local_gid](../../../config/global/ms.md#SP_ms_async_rdma_local_gid) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_local_gid "example"
ceph config get global ms_async_rdma_local_gid
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_local_gid
ceph -s
```

---

### ms_async_rdma_polling_us

| | |
|---|---|
| 类型 | Uint · default `1000` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_polling_us](../../../config/global/ms.md#SP_ms_async_rdma_polling_us) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_polling_us 1000
ceph config get global ms_async_rdma_polling_us
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1000` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_polling_us
ceph -s
```

---

### ms_async_rdma_port_num

| | |
|---|---|
| 类型 | Uint · default `1` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_port_num](../../../config/global/ms.md#SP_ms_async_rdma_port_num) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_port_num 1
ceph config get global ms_async_rdma_port_num
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_port_num
ceph -s
```

---

### ms_async_rdma_receive_buffers

| | |
|---|---|
| 类型 | Uint · default `32_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_receive_buffers](../../../config/global/ms.md#SP_ms_async_rdma_receive_buffers) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_receive_buffers 32_K
ceph config get global ms_async_rdma_receive_buffers
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `32_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_receive_buffers
ceph -s
```

---

### ms_async_rdma_receive_queue_len

| | |
|---|---|
| 类型 | Uint · default `4_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_receive_queue_len](../../../config/global/ms.md#SP_ms_async_rdma_receive_queue_len) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_receive_queue_len 4_K
ceph config get global ms_async_rdma_receive_queue_len
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_receive_queue_len
ceph -s
```

---

### ms_async_rdma_roce_ver

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_roce_ver](../../../config/global/ms.md#SP_ms_async_rdma_roce_ver) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_roce_ver 1
ceph config get global ms_async_rdma_roce_ver
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_roce_ver
ceph -s
```

---

### ms_async_rdma_send_buffers

| | |
|---|---|
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_send_buffers](../../../config/global/ms.md#SP_ms_async_rdma_send_buffers) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_send_buffers 1_K
ceph config get global ms_async_rdma_send_buffers
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_send_buffers
ceph -s
```

---

### ms_async_rdma_sl

| | |
|---|---|
| 类型 | Int · default `3` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_sl](../../../config/global/ms.md#SP_ms_async_rdma_sl) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_sl 3
ceph config get global ms_async_rdma_sl
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `3` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_sl
ceph -s
```

---

### ms_async_rdma_support_srq

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_support_srq](../../../config/global/ms.md#SP_ms_async_rdma_support_srq) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_async_rdma_support_srq false
ceph config get global ms_async_rdma_support_srq
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_support_srq
ceph -s
```

---

### ms_async_rdma_type

| | |
|---|---|
| 类型 | Str · default `ib` · **Advanced** |
| 表格 | [ms.md#SP_ms_async_rdma_type](../../../config/global/ms.md#SP_ms_async_rdma_type) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_async_rdma_type ib
ceph config get global ms_async_rdma_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `ib` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_async_rdma_type
ceph -s
```

---

### ms_async_reap_threshold

| | |
|---|---|
| 类型 | Uint · default `5` · **Dev** |
| 表格 | [ms.md#SP_ms_async_reap_threshold](../../../config/global/ms.md#SP_ms_async_reap_threshold) |

**作用：** number of deleted connections before we reap

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_async_reap_threshold 5
ceph config get global ms_async_reap_threshold
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_bind_before_connect

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_before_connect](../../../config/global/ms.md#SP_ms_bind_before_connect) |

**作用：** Call bind(2) on client sockets

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global ms_bind_before_connect true
ceph config get global ms_bind_before_connect
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_before_connect
ceph -s
```

---

### ms_bind_ipv4

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_ipv4](../../../config/global/ms.md#SP_ms_bind_ipv4) |

**作用：** Bind servers to IPv4 address(es)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`ms_bind_ipv6`](../../../config/global/ms.md#SP_ms_bind_ipv6)

**示例：**

```bash
ceph config set global ms_bind_ipv4 false
ceph config get global ms_bind_ipv4
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_ipv4
ceph -s
```

---

### ms_bind_ipv6

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_ipv6](../../../config/global/ms.md#SP_ms_bind_ipv6) |

**作用：** Bind servers to IPv6 address(es)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**相关选项：**

- [`ms_bind_ipv4`](../../../config/global/ms.md#SP_ms_bind_ipv4)

**示例：**

```bash
ceph config set global ms_bind_ipv6 true
ceph config get global ms_bind_ipv6
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_ipv6
ceph -s
```

---

### ms_bind_msgr1

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_msgr1](../../../config/global/ms.md#SP_ms_bind_msgr1) |

**作用：** Bind servers to msgr1 (legacy) protocol address(es)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`ms_bind_msgr2`](../../../config/global/ms.md#SP_ms_bind_msgr2)

**示例：**

```bash
ceph config set global ms_bind_msgr1 false
ceph config get global ms_bind_msgr1
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_msgr1
ceph -s
```

---

### ms_bind_msgr2

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_msgr2](../../../config/global/ms.md#SP_ms_bind_msgr2) |

**作用：** Bind servers to msgr2 (nautilus+) protocol address(es)

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**相关选项：**

- [`ms_bind_msgr1`](../../../config/global/ms.md#SP_ms_bind_msgr1)

**示例：**

```bash
ceph config set global ms_bind_msgr2 false
ceph config get global ms_bind_msgr2
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_msgr2
ceph -s
```

---

### ms_bind_port_max

| | |
|---|---|
| 类型 | Int · default `7568` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_port_max](../../../config/global/ms.md#SP_ms_bind_port_max) |

**作用：** Highest port number to bind daemon(s) to

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_bind_port_max 7568
ceph config get global ms_bind_port_max
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `7568` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_port_max
ceph -s
```

---

### ms_bind_port_min

| | |
|---|---|
| 类型 | Int · default `6800` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_port_min](../../../config/global/ms.md#SP_ms_bind_port_min) |

**作用：** Lowest port number to bind daemon(s) to

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_bind_port_min 6800
ceph config get global ms_bind_port_min
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `6800` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_port_min
ceph -s
```

---

### ms_bind_prefer_ipv4

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_prefer_ipv4](../../../config/global/ms.md#SP_ms_bind_prefer_ipv4) |

**作用：** Prefer IPV4 over IPV6 address(es)

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global ms_bind_prefer_ipv4 true
ceph config get global ms_bind_prefer_ipv4
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_prefer_ipv4
ceph -s
```

---

### ms_bind_retry_count

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_retry_count](../../../config/global/ms.md#SP_ms_bind_retry_count) |

**作用：** Number of attempts to make while bind(2)ing to a port

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_bind_retry_count 64
ceph config get global ms_bind_retry_count
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_retry_count
ceph -s
```

---

### ms_bind_retry_delay

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [ms.md#SP_ms_bind_retry_delay](../../../config/global/ms.md#SP_ms_bind_retry_delay) |

**作用：** Delay between bind(2) attempts (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_bind_retry_delay 64
ceph config get global ms_bind_retry_delay
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_bind_retry_delay
ceph -s
```

---

### ms_blackhole_client

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_blackhole_client](../../../config/global/ms.md#SP_ms_blackhole_client) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_blackhole_client true
ceph config get global ms_blackhole_client
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_blackhole_mds

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_blackhole_mds](../../../config/global/ms.md#SP_ms_blackhole_mds) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_blackhole_mds true
ceph config get global ms_blackhole_mds
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_blackhole_mgr

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_blackhole_mgr](../../../config/global/ms.md#SP_ms_blackhole_mgr) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_blackhole_mgr true
ceph config get global ms_blackhole_mgr
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_blackhole_mon

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_blackhole_mon](../../../config/global/ms.md#SP_ms_blackhole_mon) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_blackhole_mon true
ceph config get global ms_blackhole_mon
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_blackhole_osd

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_blackhole_osd](../../../config/global/ms.md#SP_ms_blackhole_osd) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_blackhole_osd true
ceph config get global ms_blackhole_osd
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_client_mode

| | |
|---|---|
| 类型 | Str · default `crc secure` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_client_mode](../../../config/global/ms.md#SP_ms_client_mode) |

**作用：** Connection modes (crc, secure) for connections from clients in order of preference

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_client_mode "crc secure"
ceph config get global ms_client_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `crc secure` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_client_mode
ceph -s
```

---

### ms_client_throttle_retry_time_interval

| | |
|---|---|
| 类型 | Uint · default `5000` · **Dev** |
| 表格 | [ms.md#SP_ms_client_throttle_retry_time_interval](../../../config/global/ms.md#SP_ms_client_throttle_retry_time_interval) |

**作用：** In microseconds, user client, the time interval between the next retry when the throttle get_or_fail.

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_client_throttle_retry_time_interval 5000
ceph config get global ms_client_throttle_retry_time_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`5000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_cluster_mode

| | |
|---|---|
| 类型 | Str · default `crc secure` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_cluster_mode](../../../config/global/ms.md#SP_ms_cluster_mode) |

**作用：** Connection modes (crc, secure) for intra-cluster connections in order of preference

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_cluster_mode "crc secure"
ceph config get global ms_cluster_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `crc secure` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_cluster_mode
ceph -s
```

---

### ms_cluster_type

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_cluster_type](../../../config/global/ms.md#SP_ms_cluster_type) |

**作用：** Messenger implementation to use for the internal cluster network If not specified, use ms_type

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**示例：**

```bash
ceph config set global ms_cluster_type "example"
ceph config get global ms_cluster_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_cluster_type
ceph -s
```

---

### ms_compress_secure

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_compress_secure](../../../config/global/ms.md#SP_ms_compress_secure) |

**作用：** Allowing compression when on-wire encryption is enabled Combining encryption with compression reduces the level of security of messages between peers. In case both encryption and compression are enabled, compression setting will be ignored and message will not be compressed. This behaviour can be override using this setting.

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**相关选项：**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**示例：**

```bash
ceph config set global ms_compress_secure true
ceph config get global ms_compress_secure
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_compress_secure
ceph -s
```

---

### ms_connection_idle_timeout

| | |
|---|---|
| 类型 | Uint · default `900` · **Advanced** |
| 表格 | [ms.md#SP_ms_connection_idle_timeout](../../../config/global/ms.md#SP_ms_connection_idle_timeout) |

**作用：** Time before an idle connection is closed (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global ms_connection_idle_timeout 900
ceph config get global ms_connection_idle_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `900` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_connection_idle_timeout
ceph -s
```

---

### ms_connection_ready_timeout

| | |
|---|---|
| 类型 | Uint · default `10` · **Advanced** |
| 表格 | [ms.md#SP_ms_connection_ready_timeout](../../../config/global/ms.md#SP_ms_connection_ready_timeout) |

**作用：** Time before we declare a not yet ready connection as dead (seconds)

**何时使用：** 调整后台任务时序 — 在新鲜度与集群负载间平衡。

**示例：**

```bash
ceph config set global ms_connection_ready_timeout 10
ceph config get global ms_connection_ready_timeout
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `10` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_connection_ready_timeout
ceph -s
```

---

### ms_crc_data

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [ms.md#SP_ms_crc_data](../../../config/global/ms.md#SP_ms_crc_data) |

**作用：** Set and/or verify crc32c checksum on data payload sent over network

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_crc_data false
ceph config get global ms_crc_data
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_crc_header

| | |
|---|---|
| 类型 | Bool · default `True` · **Dev** |
| 表格 | [ms.md#SP_ms_crc_header](../../../config/global/ms.md#SP_ms_crc_header) |

**作用：** Set and/or verify crc32c checksum on header payload sent over network

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_crc_header false
ceph config get global ms_crc_header
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`True`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_die_on_bad_msg

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_die_on_bad_msg](../../../config/global/ms.md#SP_ms_die_on_bad_msg) |

**作用：** Induce a daemon crash/exit when a bad network message is received

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_die_on_bad_msg true
ceph config get global ms_die_on_bad_msg
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_die_on_bug

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_die_on_bug](../../../config/global/ms.md#SP_ms_die_on_bug) |

**作用：** Induce a crash/exit on various bugs (for testing purposes)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_die_on_bug true
ceph config get global ms_die_on_bug
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_die_on_old_message

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_die_on_old_message](../../../config/global/ms.md#SP_ms_die_on_old_message) |

**作用：** Induce a daemon crash/exit when a old, undecodable message is received

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_die_on_old_message true
ceph config get global ms_die_on_old_message
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_die_on_skipped_message

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_die_on_skipped_message](../../../config/global/ms.md#SP_ms_die_on_skipped_message) |

**作用：** Induce a daemon crash/exit if sender skips a message sequence number

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_die_on_skipped_message true
ceph config get global ms_die_on_skipped_message
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_die_on_unhandled_msg

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_die_on_unhandled_msg](../../../config/global/ms.md#SP_ms_die_on_unhandled_msg) |

**作用：** Induce a daemon crash/exit when an unrecognized message is received

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_die_on_unhandled_msg true
ceph config get global ms_die_on_unhandled_msg
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_dispatch_throttle_bytes

| | |
|---|---|
| 类型 | Size · default `100_M` · **Advanced** |
| 表格 | [ms.md#SP_ms_dispatch_throttle_bytes](../../../config/global/ms.md#SP_ms_dispatch_throttle_bytes) |

**作用：** Limit messages that are read off the network but still being processed

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dispatch_throttle_bytes 100_M
ceph config get global ms_dispatch_throttle_bytes
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `100_M` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dispatch_throttle_bytes
ceph -s
```

---

### ms_dpdk_coremask

| | |
|---|---|
| 类型 | Str · default `0xF` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_coremask](../../../config/global/ms.md#SP_ms_dpdk_coremask) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`ms_async_op_threads`](../../../config/global/ms.md#SP_ms_async_op_threads)

**示例：**

```bash
ceph config set global ms_dpdk_coremask 0xF
ceph config get global ms_dpdk_coremask
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0xF` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_coremask
ceph -s
```

---

### ms_dpdk_debug_allow_loopback

| | |
|---|---|
| 类型 | Bool · default `False` · **Dev** |
| 表格 | [ms.md#SP_ms_dpdk_debug_allow_loopback](../../../config/global/ms.md#SP_ms_dpdk_debug_allow_loopback) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_dpdk_debug_allow_loopback true
ceph config get global ms_dpdk_debug_allow_loopback
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`False`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_dpdk_devs_allowlist

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_devs_allowlist](../../../config/global/ms.md#SP_ms_dpdk_devs_allowlist) |

**作用：** NIC's PCIe address are allowed to use for a single NIC use ms_dpdk_devs_allowlist=-a 0000:7d:010 or --allow=0000:7d:010; for a bond nics use ms_dpdk_devs_allowlist=--allow=0000:7d:01.0 --allow=0000:7d:02.6 --vdev=net_bonding0,mode=2,slave=0000:7d:01.0,slave=0000:7d:02.6.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_devs_allowlist "example"
ceph config get global ms_dpdk_devs_allowlist
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_devs_allowlist
ceph -s
```

---

### ms_dpdk_enable_tso

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_enable_tso](../../../config/global/ms.md#SP_ms_dpdk_enable_tso) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_dpdk_enable_tso false
ceph config get global ms_dpdk_enable_tso
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `True` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_enable_tso
ceph -s
```

---

### ms_dpdk_gateway_ipv4_addr

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_gateway_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_gateway_ipv4_addr) |

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global ms_dpdk_gateway_ipv4_addr "example"
ceph config get global ms_dpdk_gateway_ipv4_addr
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_gateway_ipv4_addr
ceph -s
```

---

### ms_dpdk_host_ipv4_addr

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_host_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_host_ipv4_addr) |

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global ms_dpdk_host_ipv4_addr "example"
ceph config get global ms_dpdk_host_ipv4_addr
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_host_ipv4_addr
ceph -s
```

---

### ms_dpdk_hugepages

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_hugepages](../../../config/global/ms.md#SP_ms_dpdk_hugepages) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_hugepages "example"
ceph config get global ms_dpdk_hugepages
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_hugepages
ceph -s
```

---

### ms_dpdk_hw_flow_control

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_hw_flow_control](../../../config/global/ms.md#SP_ms_dpdk_hw_flow_control) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_dpdk_hw_flow_control false
ceph config get global ms_dpdk_hw_flow_control
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_hw_flow_control
ceph -s
```

---

### ms_dpdk_hw_queue_weight

| | |
|---|---|
| 类型 | Float · default `1` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_hw_queue_weight](../../../config/global/ms.md#SP_ms_dpdk_hw_queue_weight) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_hw_queue_weight 1
ceph config get global ms_dpdk_hw_queue_weight
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_hw_queue_weight
ceph -s
```

---

### ms_dpdk_lro

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_lro](../../../config/global/ms.md#SP_ms_dpdk_lro) |

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_dpdk_lro false
ceph config get global ms_dpdk_lro
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_lro
ceph -s
```

---

### ms_dpdk_memory_channel

| | |
|---|---|
| 类型 | Str · default `4` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_memory_channel](../../../config/global/ms.md#SP_ms_dpdk_memory_channel) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_memory_channel 4
ceph config get global ms_dpdk_memory_channel
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_memory_channel
ceph -s
```

---

### ms_dpdk_netmask_ipv4_addr

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_netmask_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_netmask_ipv4_addr) |

**何时使用：** 与外部服务集成时设置；未使用时留空。

**示例：**

```bash
ceph config set global ms_dpdk_netmask_ipv4_addr "example"
ceph config get global ms_dpdk_netmask_ipv4_addr
```

**寻找最优值：**

**调优模型：** 连通性

1. 列出环境中的候选端点。
2. 从运行守护进程的每个节点验证可达性。
3. 选择延迟最低且稳定的端点。
4. 未启用集成时留空（`(empty)`）。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_netmask_ipv4_addr
ceph -s
```

---

### ms_dpdk_pmd

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_pmd](../../../config/global/ms.md#SP_ms_dpdk_pmd) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_pmd "example"
ceph config get global ms_dpdk_pmd
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_pmd
ceph -s
```

---

### ms_dpdk_port_id

| | |
|---|---|
| 类型 | Int · default `0` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_port_id](../../../config/global/ms.md#SP_ms_dpdk_port_id) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_port_id 64
ceph config get global ms_dpdk_port_id
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_port_id
ceph -s
```

---

### ms_dpdk_rx_buffer_count_per_core

| | |
|---|---|
| 类型 | Int · default `8192` · **Advanced** |
| 表格 | [ms.md#SP_ms_dpdk_rx_buffer_count_per_core](../../../config/global/ms.md#SP_ms_dpdk_rx_buffer_count_per_core) |

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dpdk_rx_buffer_count_per_core 8192
ceph config get global ms_dpdk_rx_buffer_count_per_core
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `8192` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dpdk_rx_buffer_count_per_core
ceph -s
```

---

### ms_dump_corrupt_message_level

| | |
|---|---|
| 类型 | Int · default `1` · **Advanced** |
| 表格 | [ms.md#SP_ms_dump_corrupt_message_level](../../../config/global/ms.md#SP_ms_dump_corrupt_message_level) |

**作用：** Log level at which to hexdump corrupt messages we receive

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_dump_corrupt_message_level 1
ceph config get global ms_dump_corrupt_message_level
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dump_corrupt_message_level
ceph -s
```

---

### ms_dump_on_send

| | |
|---|---|
| 类型 | Bool · default `False` · **Advanced** |
| 表格 | [ms.md#SP_ms_dump_on_send](../../../config/global/ms.md#SP_ms_dump_on_send) |

**作用：** Hexdump message to debug log on message send

**何时使用：** 默认禁用；需要该功能并接受其权衡时启用。

**示例：**

```bash
ceph config set global ms_dump_on_send true
ceph config get global ms_dump_on_send
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `False` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_dump_on_send
ceph -s
```

---

### ms_initial_backoff

| | |
|---|---|
| 类型 | Float · default `0.2` · **Advanced** |
| 表格 | [ms.md#SP_ms_initial_backoff](../../../config/global/ms.md#SP_ms_initial_backoff) |

**作用：** Initial backoff after a network error is detected (seconds)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_initial_backoff 0.2
ceph config get global ms_initial_backoff
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0.2` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_initial_backoff
ceph -s
```

---

### ms_inject_delay_max

| | |
|---|---|
| 类型 | Float · default `1` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_delay_max](../../../config/global/ms.md#SP_ms_inject_delay_max) |

**作用：** Max delay to inject

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_delay_max 1
ceph config get global ms_inject_delay_max
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_inject_delay_probability

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_delay_probability](../../../config/global/ms.md#SP_ms_inject_delay_probability) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_delay_probability 0
ceph config get global ms_inject_delay_probability
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_inject_delay_type

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_delay_type](../../../config/global/ms.md#SP_ms_inject_delay_type) |

**作用：** Entity type to inject delays for

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_delay_type "example"
ceph config get global ms_inject_delay_type
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`(empty)`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_inject_internal_delays

| | |
|---|---|
| 类型 | Float · default `0` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_internal_delays](../../../config/global/ms.md#SP_ms_inject_internal_delays) |

**作用：** Inject various internal delays to induce races (seconds)

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_internal_delays 0
ceph config get global ms_inject_internal_delays
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_inject_network_congestion

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_network_congestion](../../../config/global/ms.md#SP_ms_inject_network_congestion) |

**作用：** Inject a network congestions that stuck with N times operations

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_network_congestion 64
ceph config get global ms_inject_network_congestion
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_inject_socket_failures

| | |
|---|---|
| 类型 | Uint · default `0` · **Dev** |
| 表格 | [ms.md#SP_ms_inject_socket_failures](../../../config/global/ms.md#SP_ms_inject_socket_failures) |

**作用：** Inject a socket failure every Nth socket operation

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_inject_socket_failures 64
ceph config get global ms_inject_socket_failures
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`0`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_learn_addr_from_peer

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_learn_addr_from_peer](../../../config/global/ms.md#SP_ms_learn_addr_from_peer) |

**作用：** Learn address from what IP our first peer thinks we connect from Use the IP address our first peer (usually a monitor) sees that we are connecting from. This is useful if a client is behind some sort of NAT and we want to see it identified by its local (not NATed) address.

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_learn_addr_from_peer false
ceph config get global ms_learn_addr_from_peer
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_learn_addr_from_peer
ceph -s
```

---

### ms_max_accept_failures

| | |
|---|---|
| 类型 | Int · default `4` · **Advanced** |
| 表格 | [ms.md#SP_ms_max_accept_failures](../../../config/global/ms.md#SP_ms_max_accept_failures) |

**作用：** The maximum number of consecutive failed accept() calls before considering the daemon is misconfigured and abort it.

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global ms_max_accept_failures 4
ceph config get global ms_max_accept_failures
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `4` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_max_accept_failures
ceph -s
```

---

### ms_max_backoff

| | |
|---|---|
| 类型 | Float · default `15` · **Advanced** |
| 表格 | [ms.md#SP_ms_max_backoff](../../../config/global/ms.md#SP_ms_max_backoff) |

**作用：** Maximum backoff after a network error before retrying (seconds)

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`ms_initial_backoff`](../../../config/global/ms.md#SP_ms_initial_backoff)

**示例：**

```bash
ceph config set global ms_max_backoff 15
ceph config get global ms_max_backoff
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `15` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_max_backoff
ceph -s
```

---

### ms_mon_client_mode

| | |
|---|---|
| 类型 | Str · default `secure crc` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_mon_client_mode](../../../config/global/ms.md#SP_ms_mon_client_mode) |

**作用：** Connection modes (crc, secure) for connections from clients to monitors in order of preference

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_mon_client_mode "secure crc"
ceph config get global ms_mon_client_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `secure crc` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_mon_client_mode
ceph -s
```

---

### ms_mon_cluster_mode

| | |
|---|---|
| 类型 | Str · default `secure crc` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_mon_cluster_mode](../../../config/global/ms.md#SP_ms_mon_cluster_mode) |

**作用：** Connection modes (crc, secure) for intra-mon connections in order of preference

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_mon_cluster_mode "secure crc"
ceph config get global ms_mon_cluster_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `secure crc` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_mon_cluster_mode
ceph -s
```

---

### ms_mon_service_mode

| | |
|---|---|
| 类型 | Str · default `secure crc` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_mon_service_mode](../../../config/global/ms.md#SP_ms_mon_service_mode) |

**作用：** Allowed connection modes (crc, secure) for connections to mons

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_mon_service_mode "secure crc"
ceph config get global ms_mon_service_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `secure crc` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_mon_service_mode
ceph -s
```

---

### ms_osd_compress_min_size

| | |
|---|---|
| 类型 | Uint · default `1_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_osd_compress_min_size](../../../config/global/ms.md#SP_ms_osd_compress_min_size) |

**作用：** Minimal message size eligable for on-wire compression

**何时使用：** 触及资源限制或保护集群容量时调整。

**相关选项：**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**示例：**

```bash
ceph config set global ms_osd_compress_min_size 1_K
ceph config get global ms_osd_compress_min_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `1_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_osd_compress_min_size
ceph -s
```

---

### ms_osd_compress_mode

| | |
|---|---|
| 类型 | Str · enum: ["none", "force"] · default `none` · **Advanced** |
| 表格 | [ms.md#SP_ms_osd_compress_mode](../../../config/global/ms.md#SP_ms_osd_compress_mode) |

**作用：** Compression policy to use in Messenger for communicating with OSD

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`ms_compress_secure`](../../../config/global/ms.md#SP_ms_compress_secure)

**示例：**

```bash
ceph config set global ms_osd_compress_mode none
ceph config get global ms_osd_compress_mode
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `none` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_osd_compress_mode
ceph -s
```

---

### ms_osd_compression_algorithm

| | |
|---|---|
| 类型 | Str · default `snappy` · **Advanced** |
| 表格 | [ms.md#SP_ms_osd_compression_algorithm](../../../config/global/ms.md#SP_ms_osd_compression_algorithm) |

**作用：** Compression algorithm to use in Messenger when communicating with OSD Compression algorithm for connections with OSD in order of preference Although the default value is set to snappy, a list (like snappy zlib zstd etc.) is acceptable as well.

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**示例：**

```bash
ceph config set global ms_osd_compression_algorithm snappy
ceph config get global ms_osd_compression_algorithm
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `snappy` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_osd_compression_algorithm
ceph -s
```

---

### ms_pq_max_tokens_per_priority

| | |
|---|---|
| 类型 | Uint · default `16_M` · **Dev** |
| 表格 | [ms.md#SP_ms_pq_max_tokens_per_priority](../../../config/global/ms.md#SP_ms_pq_max_tokens_per_priority) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_pq_max_tokens_per_priority 16_M
ceph config get global ms_pq_max_tokens_per_priority
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`16_M`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_pq_min_cost

| | |
|---|---|
| 类型 | Size · default `64_K` · **Dev** |
| 表格 | [ms.md#SP_ms_pq_min_cost](../../../config/global/ms.md#SP_ms_pq_min_cost) |

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_pq_min_cost 64_K
ceph config get global ms_pq_min_cost
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`64_K`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_public_type

| | |
|---|---|
| 类型 | Str · default `(empty)` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_public_type](../../../config/global/ms.md#SP_ms_public_type) |

**作用：** Messenger implementation to use for the public network If not specified, use ms_type

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**相关选项：**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**示例：**

```bash
ceph config set global ms_public_type "example"
ceph config get global ms_public_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `(empty)` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_public_type
ceph -s
```

---

### ms_service_mode

| | |
|---|---|
| 类型 | Str · default `crc secure` · **Basic** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_service_mode](../../../config/global/ms.md#SP_ms_service_mode) |

**作用：** Allowed connection modes (crc, secure) for connections to daemons

**何时使用：** 核心 Global 行为 — 生产环境变更前请审阅。

**示例：**

```bash
ceph config set global ms_service_mode "crc secure"
ceph config get global ms_service_mode
```

**寻找最优值：**

**调优模型：** 策略

1. 记录 `crc secure` 为何符合您的策略。
2. 仅为兼容性或安全要求而变更。
3. 变更后测试客户端与管理流程。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_service_mode
ceph -s
```

---

### ms_tcp_listen_backlog

| | |
|---|---|
| 类型 | Int · default `512` · **Advanced** |
| 表格 | [ms.md#SP_ms_tcp_listen_backlog](../../../config/global/ms.md#SP_ms_tcp_listen_backlog) |

**作用：** Size of queue of incoming connections for accept(2)

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_tcp_listen_backlog 512
ceph config get global ms_tcp_listen_backlog
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `512` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_tcp_listen_backlog
ceph -s
```

---

### ms_tcp_nodelay

| | |
|---|---|
| 类型 | Bool · default `True` · **Advanced** |
| 表格 | [ms.md#SP_ms_tcp_nodelay](../../../config/global/ms.md#SP_ms_tcp_nodelay) |

**作用：** Disable Nagle's algorithm and send queued network traffic immediately

**何时使用：** 默认启用；仅在排查相关功能问题时禁用。

**示例：**

```bash
ceph config set global ms_tcp_nodelay false
ceph config get global ms_tcp_nodelay
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `True` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_tcp_nodelay
ceph -s
```

---

### ms_tcp_prefetch_max_size

| | |
|---|---|
| 类型 | Size · default `64_K` · **Advanced** |
| 表格 | [ms.md#SP_ms_tcp_prefetch_max_size](../../../config/global/ms.md#SP_ms_tcp_prefetch_max_size) |

**作用：** Maximum amount of data to prefetch out of the socket receive buffer

**何时使用：** 触及资源限制或保护集群容量时调整。

**示例：**

```bash
ceph config set global ms_tcp_prefetch_max_size 64_K
ceph config get global ms_tcp_prefetch_max_size
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `64_K` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_tcp_prefetch_max_size
ceph -s
```

---

### ms_tcp_rcvbuf

| | |
|---|---|
| 类型 | Size · default `0` · **Advanced** |
| 表格 | [ms.md#SP_ms_tcp_rcvbuf](../../../config/global/ms.md#SP_ms_tcp_rcvbuf) |

**作用：** Size of TCP socket receive buffer

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_tcp_rcvbuf 64
ceph config get global ms_tcp_rcvbuf
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `0` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_tcp_rcvbuf
ceph -s
```

---

### ms_time_events_min_wait_interval

| | |
|---|---|
| 类型 | Uint · default `1000` · **Dev** |
| 表格 | [ms.md#SP_ms_time_events_min_wait_interval](../../../config/global/ms.md#SP_ms_time_events_min_wait_interval) |

**作用：** In microseconds, msgr-worker's time_events min wait time for epoll_wait timeout

**何时使用：** 仅用于开发、测试或 upstream 调试 — 不可用于生产调优。

**示例：**

```bash
ceph config set global ms_time_events_min_wait_interval 1000
ceph config get global ms_time_events_min_wait_interval
```

**寻找最优值：**

**调优模型：** 开发

1. 生产环境保持 upstream 默认值（`1000`）。
2. 仅在实验室复现特定问题时修改。
3. 节点回到生产池前请还原。

---

### ms_type

| | |
|---|---|
| 类型 | Str · default `async+posix` · **Advanced** · **STARTUP**（需重启） |
| 表格 | [ms.md#SP_ms_type](../../../config/global/ms.md#SP_ms_type) |

**作用：** Messenger implementation to use for network communication

**何时使用：** 高级调优 — 仅在可测量负载与回滚计划下偏离 upstream 默认值。

**示例：**

```bash
ceph config set global ms_type async+posix
ceph config get global ms_type
```

**寻找最优值：**

**调优模型：** 性能

1. 以 upstream 默认值 `async+posix` 为基线。
2. 在代表性负载下每个测试窗口只改 **一个** 选项。
3. 对比变更前后的延迟、吞吐与后台任务。
4. 健康度下降或 slow ops 增加时回滚。
**观测信号：** `ceph -s`、slow ops、守护进程 perf 计数器、恢复/scrub 积压。

```bash
ceph config get global ms_type
ceph -s
```

---


[← 概览](../OVERVIEW.md)
