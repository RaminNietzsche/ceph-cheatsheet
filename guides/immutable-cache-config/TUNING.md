# Immutable cache Config — Tuning Quick Reference

All **13** options with tuning model and one-line guidance.

[← Overview](../OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`immutable_object_cache_client_dedicated_thread_num`](topics/immutable.md#immutable_object_cache_client_dedicated_thread_num) | `2` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_inflight_ops`](topics/immutable.md#immutable_object_cache_max_inflight_ops) | `128` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_max_size`](topics/immutable.md#immutable_object_cache_max_size) | `1_G` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_path`](topics/immutable.md#immutable_object_cache_path) | `/tmp/ceph_immutable_object_cache` | Capacity | Match filesystem layout and capacity plan | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst`](topics/immutable.md#immutable_object_cache_qos_bps_burst) | `0` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_bps_burst_seconds) | `1` | Performance | Stay within documented bounds | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_bps_limit`](topics/immutable.md#immutable_object_cache_qos_bps_limit) | `0` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst`](topics/immutable.md#immutable_object_cache_qos_iops_burst) | `0` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_burst_seconds`](topics/immutable.md#immutable_object_cache_qos_iops_burst_seconds) | `1` | Performance | Stay within documented bounds | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_iops_limit`](topics/immutable.md#immutable_object_cache_qos_iops_limit) | `0` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_qos_schedule_tick_min`](topics/immutable.md#immutable_object_cache_qos_schedule_tick_min) | `50` | Performance | Stay within documented bounds | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_sock`](topics/immutable.md#immutable_object_cache_sock) | `/var/run/ceph/immutable_object_cache_sock` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |
| [`immutable_object_cache_watermark`](topics/immutable.md#immutable_object_cache_watermark) | `0.9` | Performance | Baseline → adjust → validate under load | [Immutable object cache](topics/immutable.md) |

[← Overview](../OVERVIEW.md)
