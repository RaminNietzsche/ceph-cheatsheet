# RBD mirror Config — Tuning Quick Reference

All **24** options with tuning model and one-line guidance.

[← Overview](OVERVIEW.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`rbd_mirror_concurrent_image_deletions`](topics/mirror.md#rbd_mirror_concurrent_image_deletions) | `1` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_concurrent_image_syncs`](topics/mirror.md#rbd_mirror_concurrent_image_syncs) | `5` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_delete_retry_interval`](topics/mirror.md#rbd_mirror_delete_retry_interval) | `30` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_perf_stats_prio`](topics/mirror.md#rbd_mirror_image_perf_stats_prio) | `5` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_migration_throttle`](topics/mirror.md#rbd_mirror_image_policy_migration_throttle) | `300` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_rebalance_timeout`](topics/mirror.md#rbd_mirror_image_policy_rebalance_timeout) | `0` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_type`](topics/mirror.md#rbd_mirror_image_policy_type) | `simple` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_policy_update_throttle_interval`](topics/mirror.md#rbd_mirror_image_policy_update_throttle_interval) | `1` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_image_state_check_interval`](topics/mirror.md#rbd_mirror_image_state_check_interval) | `30` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_journal_commit_age`](topics/mirror.md#rbd_mirror_journal_commit_age) | `5` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_journal_poll_age`](topics/mirror.md#rbd_mirror_journal_poll_age) | `5` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_heartbeat_interval`](topics/mirror.md#rbd_mirror_leader_heartbeat_interval) | `5` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_max_acquire_attempts_before_break`](topics/mirror.md#rbd_mirror_leader_max_acquire_attempts_before_break) | `3` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_leader_max_missed_heartbeats`](topics/mirror.md#rbd_mirror_leader_max_missed_heartbeats) | `2` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_autotune`](topics/mirror.md#rbd_mirror_memory_autotune) | `True` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_base`](topics/mirror.md#rbd_mirror_memory_base) | `768_M` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_autotune_interval`](topics/mirror.md#rbd_mirror_memory_cache_autotune_interval) | `30` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_min`](topics/mirror.md#rbd_mirror_memory_cache_min) | `128_M` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_cache_resize_interval`](topics/mirror.md#rbd_mirror_memory_cache_resize_interval) | `5` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_expected_fragmentation`](topics/mirror.md#rbd_mirror_memory_expected_fragmentation) | `0.15` | Dev | Keep upstream default in production | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_memory_target`](topics/mirror.md#rbd_mirror_memory_target) | `4_G` | Policy | Align with security and compatibility policy | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_perf_stats_prio`](topics/mirror.md#rbd_mirror_perf_stats_prio) | `5` | Performance | Stay within documented bounds | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_pool_replayers_refresh_interval`](topics/mirror.md#rbd_mirror_pool_replayers_refresh_interval) | `30` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |
| [`rbd_mirror_sync_point_update_age`](topics/mirror.md#rbd_mirror_sync_point_update_age) | `30` | Performance | Baseline → adjust → validate under load | [RBD mirror](topics/mirror.md) |

[← Overview](OVERVIEW.md)
