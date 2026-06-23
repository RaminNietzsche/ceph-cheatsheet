# Immutable cache 配置 — 调优快速参考

全部 **13** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`immutable_object_cache_client_dedicated_thread_num`](topics/immutable.md#immutable_object_cache_client_dedicated_thread_num) | `2` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_inflight_ops`](topics/immutable.md#immutable_object_cache_max_inflight_ops) | `128` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_size`](topics/immutable.md#immutable_object_cache_max_size) | `1_G` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_path`](topics/immutable.md#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | 容量 | 匹配文件系统布局与容量规划 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst`](topics/immutable.md#immutable_object_cache_qos_bps_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_bps_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_limit`](topics/immutable.md#immutable_object_cache_qos_bps_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst`](topics/immutable.md#immutable_object_cache_qos_iops_burst) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_iops_burst_seconds) | `1` | 性能 | 保持在文档边界内 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_limit`](topics/immutable.md#immutable_object_cache_qos_iops_limit) | `0` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_schedule_tick_min`](topics/immutable.md#immutable_object_cache_qos_schedule_tick_min) | `50` | 性能 | 保持在文档边界内 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_sock`](topics/immutable.md#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_watermark`](topics/immutable.md#immutable_object_cache_watermark) | `0.9` | 性能 | 基线 → 调整 → 负载下验证 | [Immutable object cache](topics/immutable.md) |

[← 概览](../OVERVIEW.md)
