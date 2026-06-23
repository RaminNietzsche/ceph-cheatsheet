# Ceph exporter 配置 — 调优快速参考

全部 **8** 个选项的调优模型与一行建议。

[← 概览](../OVERVIEW.md)

| 选项 | 默认值 | 模型 | 快速建议 | 主题 |
|--------|---------|-------|--------------|-------|
| [`exporter_addr`](topics/exporter.md#exporter_addr) | `0.0.0.0` | Connectivity | 使用最近且稳定的端点 | [ceph-exporter](topics/exporter.md) |
| [`exporter_cert_file`](topics/exporter.md#exporter_cert_file) | `(empty)` | Capacity | 匹配文件系统布局与容量规划 | [ceph-exporter](topics/exporter.md) |
| [`exporter_http_port`](topics/exporter.md#exporter_http_port) | `9926` | Performance | 基线 → 调整 → 负载下验证 | [ceph-exporter](topics/exporter.md) |
| [`exporter_key_file`](topics/exporter.md#exporter_key_file) | `(empty)` | Capacity | 匹配文件系统布局与容量规划 | [ceph-exporter](topics/exporter.md) |
| [`exporter_prio_limit`](topics/exporter.md#exporter_prio_limit) | `5` | Performance | 基线 → 调整 → 负载下验证 | [ceph-exporter](topics/exporter.md) |
| [`exporter_sock_dir`](topics/exporter.md#exporter_sock_dir) | `/var/run/ceph/` | Capacity | 匹配文件系统布局与容量规划 | [ceph-exporter](topics/exporter.md) |
| [`exporter_sort_metrics`](topics/exporter.md#exporter_sort_metrics) | `True` | Performance | 按实测需求启用/禁用 | [ceph-exporter](topics/exporter.md) |
| [`exporter_stats_period`](topics/exporter.md#exporter_stats_period) | `5` | Performance | 基线 → 调整 → 负载下验证 | [ceph-exporter](topics/exporter.md) |

[← 概览](../OVERVIEW.md)
