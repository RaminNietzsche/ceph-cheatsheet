# Ms

Global config deep dive — 91 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [ms_async_op_threads](#ms_async_op_threads) | `3` | Advanced | Performance |
| [ms_async_rdma_buffer_size](#ms_async_rdma_buffer_size) | `128_K` | Advanced | Performance |
| [ms_async_rdma_cm](#ms_async_rdma_cm) | `False` | Advanced | Performance |
| [ms_async_rdma_device_name](#ms_async_rdma_device_name) | `(empty)` | Advanced | Performance |
| [ms_async_rdma_dscp](#ms_async_rdma_dscp) | `96` | Advanced | Performance |
| [ms_async_rdma_enable_hugepage](#ms_async_rdma_enable_hugepage) | `False` | Advanced | Policy |
| [ms_async_rdma_gid_idx](#ms_async_rdma_gid_idx) | `0` | Advanced | Performance |
| [ms_async_rdma_local_gid](#ms_async_rdma_local_gid) | `(empty)` | Advanced | Performance |
| [ms_async_rdma_polling_us](#ms_async_rdma_polling_us) | `1000` | Advanced | Performance |
| [ms_async_rdma_port_num](#ms_async_rdma_port_num) | `1` | Advanced | Performance |
| [ms_async_rdma_receive_buffers](#ms_async_rdma_receive_buffers) | `32_K` | Advanced | Performance |
| [ms_async_rdma_receive_queue_len](#ms_async_rdma_receive_queue_len) | `4_K` | Advanced | Performance |
| [ms_async_rdma_roce_ver](#ms_async_rdma_roce_ver) | `1` | Advanced | Performance |
| [ms_async_rdma_send_buffers](#ms_async_rdma_send_buffers) | `1_K` | Advanced | Performance |
| [ms_async_rdma_sl](#ms_async_rdma_sl) | `3` | Advanced | Performance |
| [ms_async_rdma_support_srq](#ms_async_rdma_support_srq) | `True` | Advanced | Performance |
| [ms_async_rdma_type](#ms_async_rdma_type) | `ib` | Advanced | Performance |
| [ms_async_reap_threshold](#ms_async_reap_threshold) | `5` | Dev | Dev |
| [ms_bind_before_connect](#ms_bind_before_connect) | `False` | Advanced | Performance |
| [ms_bind_ipv4](#ms_bind_ipv4) | `True` | Advanced | Performance |
| [ms_bind_ipv6](#ms_bind_ipv6) | `False` | Advanced | Performance |
| [ms_bind_msgr1](#ms_bind_msgr1) | `True` | Advanced | Performance |
| [ms_bind_msgr2](#ms_bind_msgr2) | `True` | Advanced | Performance |
| [ms_bind_port_max](#ms_bind_port_max) | `7568` | Advanced | Performance |
| [ms_bind_port_min](#ms_bind_port_min) | `6800` | Advanced | Performance |
| [ms_bind_prefer_ipv4](#ms_bind_prefer_ipv4) | `False` | Advanced | Performance |
| [ms_bind_retry_count](#ms_bind_retry_count) | `0` | Advanced | Performance |
| [ms_bind_retry_delay](#ms_bind_retry_delay) | `0` | Advanced | Performance |
| [ms_blackhole_client](#ms_blackhole_client) | `False` | Dev | Dev |
| [ms_blackhole_mds](#ms_blackhole_mds) | `False` | Dev | Dev |
| [ms_blackhole_mgr](#ms_blackhole_mgr) | `False` | Dev | Dev |
| [ms_blackhole_mon](#ms_blackhole_mon) | `False` | Dev | Dev |
| [ms_blackhole_osd](#ms_blackhole_osd) | `False` | Dev | Dev |
| [ms_client_mode](#ms_client_mode) | `crc secure` | Basic | Policy |
| [ms_client_throttle_retry_time_interval](#ms_client_throttle_retry_time_interval) | `5000` | Dev | Dev |
| [ms_cluster_mode](#ms_cluster_mode) | `crc secure` | Basic | Policy |
| [ms_cluster_type](#ms_cluster_type) | `(empty)` | Advanced | Performance |
| [ms_compress_secure](#ms_compress_secure) | `False` | Advanced | Performance |
| [ms_connection_idle_timeout](#ms_connection_idle_timeout) | `900` | Advanced | Performance |
| [ms_connection_ready_timeout](#ms_connection_ready_timeout) | `10` | Advanced | Performance |
| [ms_crc_data](#ms_crc_data) | `True` | Dev | Dev |
| [ms_crc_header](#ms_crc_header) | `True` | Dev | Dev |
| [ms_die_on_bad_msg](#ms_die_on_bad_msg) | `False` | Dev | Dev |
| [ms_die_on_bug](#ms_die_on_bug) | `False` | Dev | Dev |
| [ms_die_on_old_message](#ms_die_on_old_message) | `False` | Dev | Dev |
| [ms_die_on_skipped_message](#ms_die_on_skipped_message) | `False` | Dev | Dev |
| [ms_die_on_unhandled_msg](#ms_die_on_unhandled_msg) | `False` | Dev | Dev |
| [ms_dispatch_throttle_bytes](#ms_dispatch_throttle_bytes) | `100_M` | Advanced | Performance |
| [ms_dpdk_coremask](#ms_dpdk_coremask) | `0xF` | Advanced | Performance |
| [ms_dpdk_debug_allow_loopback](#ms_dpdk_debug_allow_loopback) | `False` | Dev | Dev |
| [ms_dpdk_devs_allowlist](#ms_dpdk_devs_allowlist) | `(empty)` | Advanced | Performance |
| [ms_dpdk_enable_tso](#ms_dpdk_enable_tso) | `True` | Advanced | Policy |
| [ms_dpdk_gateway_ipv4_addr](#ms_dpdk_gateway_ipv4_addr) | `(empty)` | Advanced | Connectivity |
| [ms_dpdk_host_ipv4_addr](#ms_dpdk_host_ipv4_addr) | `(empty)` | Advanced | Connectivity |
| [ms_dpdk_hugepages](#ms_dpdk_hugepages) | `(empty)` | Advanced | Performance |
| [ms_dpdk_hw_flow_control](#ms_dpdk_hw_flow_control) | `True` | Advanced | Performance |
| [ms_dpdk_hw_queue_weight](#ms_dpdk_hw_queue_weight) | `1` | Advanced | Performance |
| [ms_dpdk_lro](#ms_dpdk_lro) | `True` | Advanced | Performance |
| [ms_dpdk_memory_channel](#ms_dpdk_memory_channel) | `4` | Advanced | Performance |
| [ms_dpdk_netmask_ipv4_addr](#ms_dpdk_netmask_ipv4_addr) | `(empty)` | Advanced | Connectivity |
| [ms_dpdk_pmd](#ms_dpdk_pmd) | `(empty)` | Advanced | Performance |
| [ms_dpdk_port_id](#ms_dpdk_port_id) | `0` | Advanced | Performance |
| [ms_dpdk_rx_buffer_count_per_core](#ms_dpdk_rx_buffer_count_per_core) | `8192` | Advanced | Performance |
| [ms_dump_corrupt_message_level](#ms_dump_corrupt_message_level) | `1` | Advanced | Performance |
| [ms_dump_on_send](#ms_dump_on_send) | `False` | Advanced | Performance |
| [ms_initial_backoff](#ms_initial_backoff) | `0.2` | Advanced | Performance |
| [ms_inject_delay_max](#ms_inject_delay_max) | `1` | Dev | Dev |
| [ms_inject_delay_probability](#ms_inject_delay_probability) | `0` | Dev | Dev |
| [ms_inject_delay_type](#ms_inject_delay_type) | `(empty)` | Dev | Dev |
| [ms_inject_internal_delays](#ms_inject_internal_delays) | `0` | Dev | Dev |
| [ms_inject_network_congestion](#ms_inject_network_congestion) | `0` | Dev | Dev |
| [ms_inject_socket_failures](#ms_inject_socket_failures) | `0` | Dev | Dev |
| [ms_learn_addr_from_peer](#ms_learn_addr_from_peer) | `True` | Advanced | Performance |
| [ms_max_accept_failures](#ms_max_accept_failures) | `4` | Advanced | Performance |
| [ms_max_backoff](#ms_max_backoff) | `15` | Advanced | Performance |
| [ms_mon_client_mode](#ms_mon_client_mode) | `secure crc` | Basic | Policy |
| [ms_mon_cluster_mode](#ms_mon_cluster_mode) | `secure crc` | Basic | Policy |
| [ms_mon_service_mode](#ms_mon_service_mode) | `secure crc` | Basic | Policy |
| [ms_osd_compress_min_size](#ms_osd_compress_min_size) | `1_K` | Advanced | Performance |
| [ms_osd_compress_mode](#ms_osd_compress_mode) | `none` | Advanced | Performance |
| [ms_osd_compression_algorithm](#ms_osd_compression_algorithm) | `snappy` | Advanced | Performance |
| [ms_pq_max_tokens_per_priority](#ms_pq_max_tokens_per_priority) | `16_M` | Dev | Dev |
| [ms_pq_min_cost](#ms_pq_min_cost) | `64_K` | Dev | Dev |
| [ms_public_type](#ms_public_type) | `(empty)` | Advanced | Performance |
| [ms_service_mode](#ms_service_mode) | `crc secure` | Basic | Policy |
| [ms_tcp_listen_backlog](#ms_tcp_listen_backlog) | `512` | Advanced | Performance |
| [ms_tcp_nodelay](#ms_tcp_nodelay) | `True` | Advanced | Performance |
| [ms_tcp_prefetch_max_size](#ms_tcp_prefetch_max_size) | `64_K` | Advanced | Performance |
| [ms_tcp_rcvbuf](#ms_tcp_rcvbuf) | `0` | Advanced | Performance |
| [ms_time_events_min_wait_interval](#ms_time_events_min_wait_interval) | `1000` | Dev | Dev |
| [ms_type](#ms_type) | `async+posix` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### ms_async_op_threads

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [ms.md#SP_ms_async_op_threads](../../../config/global/ms.md#SP_ms_async_op_threads) |

**What it does:** Threadpool size for AsyncMessenger (ms_type=async)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_op_threads 3
ceph config get global ms_async_op_threads
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `24`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_op_threads
ceph -s
```

---

### ms_async_rdma_buffer_size

| | |
|---|---|
| Type | Size · default `128_K` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_buffer_size](../../../config/global/ms.md#SP_ms_async_rdma_buffer_size) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_buffer_size 128_K
ceph config get global ms_async_rdma_buffer_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_buffer_size
ceph -s
```

---

### ms_async_rdma_cm

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_cm](../../../config/global/ms.md#SP_ms_async_rdma_cm) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global ms_async_rdma_cm true
ceph config get global ms_async_rdma_cm
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_cm
ceph -s
```

---

### ms_async_rdma_device_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_device_name](../../../config/global/ms.md#SP_ms_async_rdma_device_name) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_device_name "example"
ceph config get global ms_async_rdma_device_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_device_name
ceph -s
```

---

### ms_async_rdma_dscp

| | |
|---|---|
| Type | Int · default `96` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_dscp](../../../config/global/ms.md#SP_ms_async_rdma_dscp) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_dscp 96
ceph config get global ms_async_rdma_dscp
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `96`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_dscp
ceph -s
```

---

### ms_async_rdma_enable_hugepage

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_enable_hugepage](../../../config/global/ms.md#SP_ms_async_rdma_enable_hugepage) |

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global ms_async_rdma_enable_hugepage true
ceph config get global ms_async_rdma_enable_hugepage
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_enable_hugepage
ceph -s
```

---

### ms_async_rdma_gid_idx

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_gid_idx](../../../config/global/ms.md#SP_ms_async_rdma_gid_idx) |

**What it does:** use gid_idx to select GID for choosing RoCEv1 or RoCEv2

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_gid_idx 64
ceph config get global ms_async_rdma_gid_idx
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_gid_idx
ceph -s
```

---

### ms_async_rdma_local_gid

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_local_gid](../../../config/global/ms.md#SP_ms_async_rdma_local_gid) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_local_gid "example"
ceph config get global ms_async_rdma_local_gid
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_local_gid
ceph -s
```

---

### ms_async_rdma_polling_us

| | |
|---|---|
| Type | Uint · default `1000` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_polling_us](../../../config/global/ms.md#SP_ms_async_rdma_polling_us) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_polling_us 1000
ceph config get global ms_async_rdma_polling_us
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_polling_us
ceph -s
```

---

### ms_async_rdma_port_num

| | |
|---|---|
| Type | Uint · default `1` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_port_num](../../../config/global/ms.md#SP_ms_async_rdma_port_num) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_port_num 1
ceph config get global ms_async_rdma_port_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_port_num
ceph -s
```

---

### ms_async_rdma_receive_buffers

| | |
|---|---|
| Type | Uint · default `32_K` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_receive_buffers](../../../config/global/ms.md#SP_ms_async_rdma_receive_buffers) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_receive_buffers 32_K
ceph config get global ms_async_rdma_receive_buffers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_receive_buffers
ceph -s
```

---

### ms_async_rdma_receive_queue_len

| | |
|---|---|
| Type | Uint · default `4_K` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_receive_queue_len](../../../config/global/ms.md#SP_ms_async_rdma_receive_queue_len) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_receive_queue_len 4_K
ceph config get global ms_async_rdma_receive_queue_len
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_receive_queue_len
ceph -s
```

---

### ms_async_rdma_roce_ver

| | |
|---|---|
| Type | Int · default `1` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_roce_ver](../../../config/global/ms.md#SP_ms_async_rdma_roce_ver) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_roce_ver 1
ceph config get global ms_async_rdma_roce_ver
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_roce_ver
ceph -s
```

---

### ms_async_rdma_send_buffers

| | |
|---|---|
| Type | Uint · default `1_K` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_send_buffers](../../../config/global/ms.md#SP_ms_async_rdma_send_buffers) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_send_buffers 1_K
ceph config get global ms_async_rdma_send_buffers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_send_buffers
ceph -s
```

---

### ms_async_rdma_sl

| | |
|---|---|
| Type | Int · default `3` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_sl](../../../config/global/ms.md#SP_ms_async_rdma_sl) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_sl 3
ceph config get global ms_async_rdma_sl
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_sl
ceph -s
```

---

### ms_async_rdma_support_srq

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_support_srq](../../../config/global/ms.md#SP_ms_async_rdma_support_srq) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_async_rdma_support_srq false
ceph config get global ms_async_rdma_support_srq
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_support_srq
ceph -s
```

---

### ms_async_rdma_type

| | |
|---|---|
| Type | Str · default `ib` · **Advanced** |
| Table | [ms.md#SP_ms_async_rdma_type](../../../config/global/ms.md#SP_ms_async_rdma_type) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_async_rdma_type ib
ceph config get global ms_async_rdma_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `ib`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_async_rdma_type
ceph -s
```

---

### ms_async_reap_threshold

| | |
|---|---|
| Type | Uint · default `5` · **Dev** |
| Table | [ms.md#SP_ms_async_reap_threshold](../../../config/global/ms.md#SP_ms_async_reap_threshold) |

**What it does:** number of deleted connections before we reap

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_async_reap_threshold 5
ceph config get global ms_async_reap_threshold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_bind_before_connect

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_bind_before_connect](../../../config/global/ms.md#SP_ms_bind_before_connect) |

**What it does:** Call bind(2) on client sockets

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global ms_bind_before_connect true
ceph config get global ms_bind_before_connect
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_before_connect
ceph -s
```

---

### ms_bind_ipv4

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_bind_ipv4](../../../config/global/ms.md#SP_ms_bind_ipv4) |

**What it does:** Bind servers to IPv4 address(es)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`ms_bind_ipv6`](../../../config/global/ms.md#SP_ms_bind_ipv6)

**Example:**

```bash
ceph config set global ms_bind_ipv4 false
ceph config get global ms_bind_ipv4
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_ipv4
ceph -s
```

---

### ms_bind_ipv6

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_bind_ipv6](../../../config/global/ms.md#SP_ms_bind_ipv6) |

**What it does:** Bind servers to IPv6 address(es)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`ms_bind_ipv4`](../../../config/global/ms.md#SP_ms_bind_ipv4)

**Example:**

```bash
ceph config set global ms_bind_ipv6 true
ceph config get global ms_bind_ipv6
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_ipv6
ceph -s
```

---

### ms_bind_msgr1

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_bind_msgr1](../../../config/global/ms.md#SP_ms_bind_msgr1) |

**What it does:** Bind servers to msgr1 (legacy) protocol address(es)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`ms_bind_msgr2`](../../../config/global/ms.md#SP_ms_bind_msgr2)

**Example:**

```bash
ceph config set global ms_bind_msgr1 false
ceph config get global ms_bind_msgr1
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_msgr1
ceph -s
```

---

### ms_bind_msgr2

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_bind_msgr2](../../../config/global/ms.md#SP_ms_bind_msgr2) |

**What it does:** Bind servers to msgr2 (nautilus+) protocol address(es)

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Related options:**

- [`ms_bind_msgr1`](../../../config/global/ms.md#SP_ms_bind_msgr1)

**Example:**

```bash
ceph config set global ms_bind_msgr2 false
ceph config get global ms_bind_msgr2
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_msgr2
ceph -s
```

---

### ms_bind_port_max

| | |
|---|---|
| Type | Int · default `7568` · **Advanced** |
| Table | [ms.md#SP_ms_bind_port_max](../../../config/global/ms.md#SP_ms_bind_port_max) |

**What it does:** Highest port number to bind daemon(s) to

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_bind_port_max 7568
ceph config get global ms_bind_port_max
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `7568`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_port_max
ceph -s
```

---

### ms_bind_port_min

| | |
|---|---|
| Type | Int · default `6800` · **Advanced** |
| Table | [ms.md#SP_ms_bind_port_min](../../../config/global/ms.md#SP_ms_bind_port_min) |

**What it does:** Lowest port number to bind daemon(s) to

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_bind_port_min 6800
ceph config get global ms_bind_port_min
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `6800`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_port_min
ceph -s
```

---

### ms_bind_prefer_ipv4

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_bind_prefer_ipv4](../../../config/global/ms.md#SP_ms_bind_prefer_ipv4) |

**What it does:** Prefer IPV4 over IPV6 address(es)

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global ms_bind_prefer_ipv4 true
ceph config get global ms_bind_prefer_ipv4
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_prefer_ipv4
ceph -s
```

---

### ms_bind_retry_count

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [ms.md#SP_ms_bind_retry_count](../../../config/global/ms.md#SP_ms_bind_retry_count) |

**What it does:** Number of attempts to make while bind(2)ing to a port

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_bind_retry_count 64
ceph config get global ms_bind_retry_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_retry_count
ceph -s
```

---

### ms_bind_retry_delay

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [ms.md#SP_ms_bind_retry_delay](../../../config/global/ms.md#SP_ms_bind_retry_delay) |

**What it does:** Delay between bind(2) attempts (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_bind_retry_delay 64
ceph config get global ms_bind_retry_delay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_bind_retry_delay
ceph -s
```

---

### ms_blackhole_client

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_blackhole_client](../../../config/global/ms.md#SP_ms_blackhole_client) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_blackhole_client true
ceph config get global ms_blackhole_client
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_blackhole_mds

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_blackhole_mds](../../../config/global/ms.md#SP_ms_blackhole_mds) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_blackhole_mds true
ceph config get global ms_blackhole_mds
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_blackhole_mgr

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_blackhole_mgr](../../../config/global/ms.md#SP_ms_blackhole_mgr) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_blackhole_mgr true
ceph config get global ms_blackhole_mgr
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_blackhole_mon

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_blackhole_mon](../../../config/global/ms.md#SP_ms_blackhole_mon) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_blackhole_mon true
ceph config get global ms_blackhole_mon
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_blackhole_osd

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_blackhole_osd](../../../config/global/ms.md#SP_ms_blackhole_osd) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_blackhole_osd true
ceph config get global ms_blackhole_osd
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_client_mode

| | |
|---|---|
| Type | Str · default `crc secure` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_client_mode](../../../config/global/ms.md#SP_ms_client_mode) |

**What it does:** Connection modes (crc, secure) for connections from clients in order of preference

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_client_mode "crc secure"
ceph config get global ms_client_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `crc secure` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_client_mode
ceph -s
```

---

### ms_client_throttle_retry_time_interval

| | |
|---|---|
| Type | Uint · default `5000` · **Dev** |
| Table | [ms.md#SP_ms_client_throttle_retry_time_interval](../../../config/global/ms.md#SP_ms_client_throttle_retry_time_interval) |

**What it does:** In microseconds, user client, the time interval between the next retry when the throttle get_or_fail.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_client_throttle_retry_time_interval 5000
ceph config get global ms_client_throttle_retry_time_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`5000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_cluster_mode

| | |
|---|---|
| Type | Str · default `crc secure` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_cluster_mode](../../../config/global/ms.md#SP_ms_cluster_mode) |

**What it does:** Connection modes (crc, secure) for intra-cluster connections in order of preference

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_cluster_mode "crc secure"
ceph config get global ms_cluster_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `crc secure` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_cluster_mode
ceph -s
```

---

### ms_cluster_type

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_cluster_type](../../../config/global/ms.md#SP_ms_cluster_type) |

**What it does:** Messenger implementation to use for the internal cluster network If not specified, use ms_type

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**Example:**

```bash
ceph config set global ms_cluster_type "example"
ceph config get global ms_cluster_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_cluster_type
ceph -s
```

---

### ms_compress_secure

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_compress_secure](../../../config/global/ms.md#SP_ms_compress_secure) |

**What it does:** Allowing compression when on-wire encryption is enabled Combining encryption with compression reduces the level of security of messages between peers. In case both encryption and compression are enabled, compression setting will be ignored and message will not be compressed. This behaviour can be override using this setting.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**Example:**

```bash
ceph config set global ms_compress_secure true
ceph config get global ms_compress_secure
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_compress_secure
ceph -s
```

---

### ms_connection_idle_timeout

| | |
|---|---|
| Type | Uint · default `900` · **Advanced** |
| Table | [ms.md#SP_ms_connection_idle_timeout](../../../config/global/ms.md#SP_ms_connection_idle_timeout) |

**What it does:** Time before an idle connection is closed (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global ms_connection_idle_timeout 900
ceph config get global ms_connection_idle_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `900`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_connection_idle_timeout
ceph -s
```

---

### ms_connection_ready_timeout

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [ms.md#SP_ms_connection_ready_timeout](../../../config/global/ms.md#SP_ms_connection_ready_timeout) |

**What it does:** Time before we declare a not yet ready connection as dead (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set global ms_connection_ready_timeout 10
ceph config get global ms_connection_ready_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_connection_ready_timeout
ceph -s
```

---

### ms_crc_data

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [ms.md#SP_ms_crc_data](../../../config/global/ms.md#SP_ms_crc_data) |

**What it does:** Set and/or verify crc32c checksum on data payload sent over network

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_crc_data false
ceph config get global ms_crc_data
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_crc_header

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [ms.md#SP_ms_crc_header](../../../config/global/ms.md#SP_ms_crc_header) |

**What it does:** Set and/or verify crc32c checksum on header payload sent over network

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_crc_header false
ceph config get global ms_crc_header
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_die_on_bad_msg

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_die_on_bad_msg](../../../config/global/ms.md#SP_ms_die_on_bad_msg) |

**What it does:** Induce a daemon crash/exit when a bad network message is received

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_die_on_bad_msg true
ceph config get global ms_die_on_bad_msg
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_die_on_bug

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_die_on_bug](../../../config/global/ms.md#SP_ms_die_on_bug) |

**What it does:** Induce a crash/exit on various bugs (for testing purposes)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_die_on_bug true
ceph config get global ms_die_on_bug
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_die_on_old_message

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_die_on_old_message](../../../config/global/ms.md#SP_ms_die_on_old_message) |

**What it does:** Induce a daemon crash/exit when a old, undecodable message is received

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_die_on_old_message true
ceph config get global ms_die_on_old_message
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_die_on_skipped_message

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_die_on_skipped_message](../../../config/global/ms.md#SP_ms_die_on_skipped_message) |

**What it does:** Induce a daemon crash/exit if sender skips a message sequence number

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_die_on_skipped_message true
ceph config get global ms_die_on_skipped_message
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_die_on_unhandled_msg

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_die_on_unhandled_msg](../../../config/global/ms.md#SP_ms_die_on_unhandled_msg) |

**What it does:** Induce a daemon crash/exit when an unrecognized message is received

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_die_on_unhandled_msg true
ceph config get global ms_die_on_unhandled_msg
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_dispatch_throttle_bytes

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [ms.md#SP_ms_dispatch_throttle_bytes](../../../config/global/ms.md#SP_ms_dispatch_throttle_bytes) |

**What it does:** Limit messages that are read off the network but still being processed

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dispatch_throttle_bytes 100_M
ceph config get global ms_dispatch_throttle_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dispatch_throttle_bytes
ceph -s
```

---

### ms_dpdk_coremask

| | |
|---|---|
| Type | Str · default `0xF` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_coremask](../../../config/global/ms.md#SP_ms_dpdk_coremask) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`ms_async_op_threads`](../../../config/global/ms.md#SP_ms_async_op_threads)

**Example:**

```bash
ceph config set global ms_dpdk_coremask 0xF
ceph config get global ms_dpdk_coremask
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0xF`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_coremask
ceph -s
```

---

### ms_dpdk_debug_allow_loopback

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [ms.md#SP_ms_dpdk_debug_allow_loopback](../../../config/global/ms.md#SP_ms_dpdk_debug_allow_loopback) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_dpdk_debug_allow_loopback true
ceph config get global ms_dpdk_debug_allow_loopback
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_dpdk_devs_allowlist

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_devs_allowlist](../../../config/global/ms.md#SP_ms_dpdk_devs_allowlist) |

**What it does:** NIC's PCIe address are allowed to use for a single NIC use ms_dpdk_devs_allowlist=-a 0000:7d:010 or --allow=0000:7d:010; for a bond nics use ms_dpdk_devs_allowlist=--allow=0000:7d:01.0 --allow=0000:7d:02.6 --vdev=net_bonding0,mode=2,slave=0000:7d:01.0,slave=0000:7d:02.6.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_devs_allowlist "example"
ceph config get global ms_dpdk_devs_allowlist
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_devs_allowlist
ceph -s
```

---

### ms_dpdk_enable_tso

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_enable_tso](../../../config/global/ms.md#SP_ms_dpdk_enable_tso) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_dpdk_enable_tso false
ceph config get global ms_dpdk_enable_tso
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_enable_tso
ceph -s
```

---

### ms_dpdk_gateway_ipv4_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_gateway_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_gateway_ipv4_addr) |

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global ms_dpdk_gateway_ipv4_addr "example"
ceph config get global ms_dpdk_gateway_ipv4_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_gateway_ipv4_addr
ceph -s
```

---

### ms_dpdk_host_ipv4_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_host_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_host_ipv4_addr) |

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global ms_dpdk_host_ipv4_addr "example"
ceph config get global ms_dpdk_host_ipv4_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_host_ipv4_addr
ceph -s
```

---

### ms_dpdk_hugepages

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_hugepages](../../../config/global/ms.md#SP_ms_dpdk_hugepages) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_hugepages "example"
ceph config get global ms_dpdk_hugepages
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_hugepages
ceph -s
```

---

### ms_dpdk_hw_flow_control

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_hw_flow_control](../../../config/global/ms.md#SP_ms_dpdk_hw_flow_control) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_dpdk_hw_flow_control false
ceph config get global ms_dpdk_hw_flow_control
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_hw_flow_control
ceph -s
```

---

### ms_dpdk_hw_queue_weight

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_hw_queue_weight](../../../config/global/ms.md#SP_ms_dpdk_hw_queue_weight) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_hw_queue_weight 1
ceph config get global ms_dpdk_hw_queue_weight
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_hw_queue_weight
ceph -s
```

---

### ms_dpdk_lro

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_lro](../../../config/global/ms.md#SP_ms_dpdk_lro) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_dpdk_lro false
ceph config get global ms_dpdk_lro
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_lro
ceph -s
```

---

### ms_dpdk_memory_channel

| | |
|---|---|
| Type | Str · default `4` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_memory_channel](../../../config/global/ms.md#SP_ms_dpdk_memory_channel) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_memory_channel 4
ceph config get global ms_dpdk_memory_channel
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_memory_channel
ceph -s
```

---

### ms_dpdk_netmask_ipv4_addr

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_netmask_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_netmask_ipv4_addr) |

**When to use:** Set when integrating with an external service; leave empty if unused.

**Example:**

```bash
ceph config set global ms_dpdk_netmask_ipv4_addr "example"
ceph config get global ms_dpdk_netmask_ipv4_addr
```

**Finding optimal value:**

**Tuning model:** Connectivity

1. List candidate endpoints from your environment.
2. Verify reachability from every node running the daemon.
3. Pick the lowest-latency stable endpoint.
4. Leave empty (`(empty)`) if the integration is disabled.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_netmask_ipv4_addr
ceph -s
```

---

### ms_dpdk_pmd

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_pmd](../../../config/global/ms.md#SP_ms_dpdk_pmd) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_pmd "example"
ceph config get global ms_dpdk_pmd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_pmd
ceph -s
```

---

### ms_dpdk_port_id

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_port_id](../../../config/global/ms.md#SP_ms_dpdk_port_id) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_port_id 64
ceph config get global ms_dpdk_port_id
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_port_id
ceph -s
```

---

### ms_dpdk_rx_buffer_count_per_core

| | |
|---|---|
| Type | Int · default `8192` · **Advanced** |
| Table | [ms.md#SP_ms_dpdk_rx_buffer_count_per_core](../../../config/global/ms.md#SP_ms_dpdk_rx_buffer_count_per_core) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dpdk_rx_buffer_count_per_core 8192
ceph config get global ms_dpdk_rx_buffer_count_per_core
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8192`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dpdk_rx_buffer_count_per_core
ceph -s
```

---

### ms_dump_corrupt_message_level

| | |
|---|---|
| Type | Int · default `1` · **Advanced** |
| Table | [ms.md#SP_ms_dump_corrupt_message_level](../../../config/global/ms.md#SP_ms_dump_corrupt_message_level) |

**What it does:** Log level at which to hexdump corrupt messages we receive

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_dump_corrupt_message_level 1
ceph config get global ms_dump_corrupt_message_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dump_corrupt_message_level
ceph -s
```

---

### ms_dump_on_send

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [ms.md#SP_ms_dump_on_send](../../../config/global/ms.md#SP_ms_dump_on_send) |

**What it does:** Hexdump message to debug log on message send

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global ms_dump_on_send true
ceph config get global ms_dump_on_send
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_dump_on_send
ceph -s
```

---

### ms_initial_backoff

| | |
|---|---|
| Type | Float · default `0.2` · **Advanced** |
| Table | [ms.md#SP_ms_initial_backoff](../../../config/global/ms.md#SP_ms_initial_backoff) |

**What it does:** Initial backoff after a network error is detected (seconds)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_initial_backoff 0.2
ceph config get global ms_initial_backoff
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_initial_backoff
ceph -s
```

---

### ms_inject_delay_max

| | |
|---|---|
| Type | Float · default `1` · **Dev** |
| Table | [ms.md#SP_ms_inject_delay_max](../../../config/global/ms.md#SP_ms_inject_delay_max) |

**What it does:** Max delay to inject

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_delay_max 1
ceph config get global ms_inject_delay_max
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_inject_delay_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [ms.md#SP_ms_inject_delay_probability](../../../config/global/ms.md#SP_ms_inject_delay_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_delay_probability 0
ceph config get global ms_inject_delay_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_inject_delay_type

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [ms.md#SP_ms_inject_delay_type](../../../config/global/ms.md#SP_ms_inject_delay_type) |

**What it does:** Entity type to inject delays for

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_delay_type "example"
ceph config get global ms_inject_delay_type
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_inject_internal_delays

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [ms.md#SP_ms_inject_internal_delays](../../../config/global/ms.md#SP_ms_inject_internal_delays) |

**What it does:** Inject various internal delays to induce races (seconds)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_internal_delays 0
ceph config get global ms_inject_internal_delays
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_inject_network_congestion

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [ms.md#SP_ms_inject_network_congestion](../../../config/global/ms.md#SP_ms_inject_network_congestion) |

**What it does:** Inject a network congestions that stuck with N times operations

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_network_congestion 64
ceph config get global ms_inject_network_congestion
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_inject_socket_failures

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [ms.md#SP_ms_inject_socket_failures](../../../config/global/ms.md#SP_ms_inject_socket_failures) |

**What it does:** Inject a socket failure every Nth socket operation

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_inject_socket_failures 64
ceph config get global ms_inject_socket_failures
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_learn_addr_from_peer

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_learn_addr_from_peer](../../../config/global/ms.md#SP_ms_learn_addr_from_peer) |

**What it does:** Learn address from what IP our first peer thinks we connect from Use the IP address our first peer (usually a monitor) sees that we are connecting from. This is useful if a client is behind some sort of NAT and we want to see it identified by its local (not NATed) address.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_learn_addr_from_peer false
ceph config get global ms_learn_addr_from_peer
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_learn_addr_from_peer
ceph -s
```

---

### ms_max_accept_failures

| | |
|---|---|
| Type | Int · default `4` · **Advanced** |
| Table | [ms.md#SP_ms_max_accept_failures](../../../config/global/ms.md#SP_ms_max_accept_failures) |

**What it does:** The maximum number of consecutive failed accept() calls before considering the daemon is misconfigured and abort it.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global ms_max_accept_failures 4
ceph config get global ms_max_accept_failures
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_max_accept_failures
ceph -s
```

---

### ms_max_backoff

| | |
|---|---|
| Type | Float · default `15` · **Advanced** |
| Table | [ms.md#SP_ms_max_backoff](../../../config/global/ms.md#SP_ms_max_backoff) |

**What it does:** Maximum backoff after a network error before retrying (seconds)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`ms_initial_backoff`](../../../config/global/ms.md#SP_ms_initial_backoff)

**Example:**

```bash
ceph config set global ms_max_backoff 15
ceph config get global ms_max_backoff
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_max_backoff
ceph -s
```

---

### ms_mon_client_mode

| | |
|---|---|
| Type | Str · default `secure crc` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_mon_client_mode](../../../config/global/ms.md#SP_ms_mon_client_mode) |

**What it does:** Connection modes (crc, secure) for connections from clients to monitors in order of preference

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_mon_client_mode "secure crc"
ceph config get global ms_mon_client_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `secure crc` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_mon_client_mode
ceph -s
```

---

### ms_mon_cluster_mode

| | |
|---|---|
| Type | Str · default `secure crc` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_mon_cluster_mode](../../../config/global/ms.md#SP_ms_mon_cluster_mode) |

**What it does:** Connection modes (crc, secure) for intra-mon connections in order of preference

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_mon_cluster_mode "secure crc"
ceph config get global ms_mon_cluster_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `secure crc` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_mon_cluster_mode
ceph -s
```

---

### ms_mon_service_mode

| | |
|---|---|
| Type | Str · default `secure crc` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_mon_service_mode](../../../config/global/ms.md#SP_ms_mon_service_mode) |

**What it does:** Allowed connection modes (crc, secure) for connections to mons

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_mon_service_mode "secure crc"
ceph config get global ms_mon_service_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `secure crc` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_mon_service_mode
ceph -s
```

---

### ms_osd_compress_min_size

| | |
|---|---|
| Type | Uint · default `1_K` · **Advanced** |
| Table | [ms.md#SP_ms_osd_compress_min_size](../../../config/global/ms.md#SP_ms_osd_compress_min_size) |

**What it does:** Minimal message size eligable for on-wire compression

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**Example:**

```bash
ceph config set global ms_osd_compress_min_size 1_K
ceph config get global ms_osd_compress_min_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_osd_compress_min_size
ceph -s
```

---

### ms_osd_compress_mode

| | |
|---|---|
| Type | Str · enum: ["none", "force"] · default `none` · **Advanced** |
| Table | [ms.md#SP_ms_osd_compress_mode](../../../config/global/ms.md#SP_ms_osd_compress_mode) |

**What it does:** Compression policy to use in Messenger for communicating with OSD

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`ms_compress_secure`](../../../config/global/ms.md#SP_ms_compress_secure)

**Example:**

```bash
ceph config set global ms_osd_compress_mode none
ceph config get global ms_osd_compress_mode
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `none`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_osd_compress_mode
ceph -s
```

---

### ms_osd_compression_algorithm

| | |
|---|---|
| Type | Str · default `snappy` · **Advanced** |
| Table | [ms.md#SP_ms_osd_compression_algorithm](../../../config/global/ms.md#SP_ms_osd_compression_algorithm) |

**What it does:** Compression algorithm to use in Messenger when communicating with OSD Compression algorithm for connections with OSD in order of preference Although the default value is set to snappy, a list (like snappy zlib zstd etc.) is acceptable as well.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**Example:**

```bash
ceph config set global ms_osd_compression_algorithm snappy
ceph config get global ms_osd_compression_algorithm
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `snappy`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_osd_compression_algorithm
ceph -s
```

---

### ms_pq_max_tokens_per_priority

| | |
|---|---|
| Type | Uint · default `16_M` · **Dev** |
| Table | [ms.md#SP_ms_pq_max_tokens_per_priority](../../../config/global/ms.md#SP_ms_pq_max_tokens_per_priority) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_pq_max_tokens_per_priority 16_M
ceph config get global ms_pq_max_tokens_per_priority
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`16_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_pq_min_cost

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [ms.md#SP_ms_pq_min_cost](../../../config/global/ms.md#SP_ms_pq_min_cost) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_pq_min_cost 64_K
ceph config get global ms_pq_min_cost
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_public_type

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_public_type](../../../config/global/ms.md#SP_ms_public_type) |

**What it does:** Messenger implementation to use for the public network If not specified, use ms_type

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**Example:**

```bash
ceph config set global ms_public_type "example"
ceph config get global ms_public_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_public_type
ceph -s
```

---

### ms_service_mode

| | |
|---|---|
| Type | Str · default `crc secure` · **Basic** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_service_mode](../../../config/global/ms.md#SP_ms_service_mode) |

**What it does:** Allowed connection modes (crc, secure) for connections to daemons

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set global ms_service_mode "crc secure"
ceph config get global ms_service_mode
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `crc secure` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_service_mode
ceph -s
```

---

### ms_tcp_listen_backlog

| | |
|---|---|
| Type | Int · default `512` · **Advanced** |
| Table | [ms.md#SP_ms_tcp_listen_backlog](../../../config/global/ms.md#SP_ms_tcp_listen_backlog) |

**What it does:** Size of queue of incoming connections for accept(2)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_tcp_listen_backlog 512
ceph config get global ms_tcp_listen_backlog
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `512`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_tcp_listen_backlog
ceph -s
```

---

### ms_tcp_nodelay

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [ms.md#SP_ms_tcp_nodelay](../../../config/global/ms.md#SP_ms_tcp_nodelay) |

**What it does:** Disable Nagle's algorithm and send queued network traffic immediately

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set global ms_tcp_nodelay false
ceph config get global ms_tcp_nodelay
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_tcp_nodelay
ceph -s
```

---

### ms_tcp_prefetch_max_size

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [ms.md#SP_ms_tcp_prefetch_max_size](../../../config/global/ms.md#SP_ms_tcp_prefetch_max_size) |

**What it does:** Maximum amount of data to prefetch out of the socket receive buffer

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global ms_tcp_prefetch_max_size 64_K
ceph config get global ms_tcp_prefetch_max_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_tcp_prefetch_max_size
ceph -s
```

---

### ms_tcp_rcvbuf

| | |
|---|---|
| Type | Size · default `0` · **Advanced** |
| Table | [ms.md#SP_ms_tcp_rcvbuf](../../../config/global/ms.md#SP_ms_tcp_rcvbuf) |

**What it does:** Size of TCP socket receive buffer

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_tcp_rcvbuf 64
ceph config get global ms_tcp_rcvbuf
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_tcp_rcvbuf
ceph -s
```

---

### ms_time_events_min_wait_interval

| | |
|---|---|
| Type | Uint · default `1000` · **Dev** |
| Table | [ms.md#SP_ms_time_events_min_wait_interval](../../../config/global/ms.md#SP_ms_time_events_min_wait_interval) |

**What it does:** In microseconds, msgr-worker's time_events min wait time for epoll_wait timeout

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global ms_time_events_min_wait_interval 1000
ceph config get global ms_time_events_min_wait_interval
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`1000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### ms_type

| | |
|---|---|
| Type | Str · default `async+posix` · **Advanced** · **STARTUP** (restart required) |
| Table | [ms.md#SP_ms_type](../../../config/global/ms.md#SP_ms_type) |

**What it does:** Messenger implementation to use for network communication

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global ms_type async+posix
ceph config get global ms_type
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `async+posix`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global ms_type
ceph -s
```

---


[← Overview](../OVERVIEW.md)
