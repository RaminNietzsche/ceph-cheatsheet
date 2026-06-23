# Ceph exporter Config — Tuning Quick Reference

All **8** options with tuning model and one-line guidance.

[← Overview](OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`exporter_addr`](topics/exporter.md#exporter_addr) | `0.0.0.0` | Connectivity | Use nearest stable endpoint | [ceph-exporter](topics/exporter.md) |
| [`exporter_cert_file`](topics/exporter.md#exporter_cert_file) | `(empty)` | Capacity | Match filesystem layout and capacity plan | [ceph-exporter](topics/exporter.md) |
| [`exporter_http_port`](topics/exporter.md#exporter_http_port) | `9926` | Performance | Baseline → adjust → validate under load | [ceph-exporter](topics/exporter.md) |
| [`exporter_key_file`](topics/exporter.md#exporter_key_file) | `(empty)` | Capacity | Match filesystem layout and capacity plan | [ceph-exporter](topics/exporter.md) |
| [`exporter_prio_limit`](topics/exporter.md#exporter_prio_limit) | `5` | Performance | Baseline → adjust → validate under load | [ceph-exporter](topics/exporter.md) |
| [`exporter_sock_dir`](topics/exporter.md#exporter_sock_dir) | `/var/run/ceph/` | Capacity | Match filesystem layout and capacity plan | [ceph-exporter](topics/exporter.md) |
| [`exporter_sort_metrics`](topics/exporter.md#exporter_sort_metrics) | `True` | Performance | Enable/disable based on measured need | [ceph-exporter](topics/exporter.md) |
| [`exporter_stats_period`](topics/exporter.md#exporter_stats_period) | `5` | Performance | Baseline → adjust → validate under load | [ceph-exporter](topics/exporter.md) |

[← Overview](OVERVIEW.md)
