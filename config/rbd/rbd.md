| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_rbd_atime_update_interval">rbd_atime_update_interval</span> |  RBD Image access timestamp refresh interval. Set to 0 to disable access timestamp update. | Advanced | Uint | 60 |  | 0 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_auto_exclusive_lock_until_manual_request">rbd_auto_exclusive_lock_until_manual_request</span> |  automatically acquire/release exclusive lock until it is explicitly requested | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_balance_parent_reads">rbd_balance_parent_reads</span> |  distribute parent read requests to random OSD | Advanced | Bool | False |  |  |  |  |  | [[rbd_read_from_replica_policy](/rbd/rbd.md#SP_rbd_read_from_replica_policy)] |  | rbd |  |  |  |
| <span id="SP_rbd_balance_snap_reads">rbd_balance_snap_reads</span> |  distribute snap read requests to random OSD | Advanced | Bool | False |  |  |  |  |  | [[rbd_read_from_replica_policy](/rbd/rbd.md#SP_rbd_read_from_replica_policy)] |  | rbd |  |  |  |
| <span id="SP_rbd_blkin_trace_all">rbd_blkin_trace_all</span> |  create a blkin trace for all RBD requests | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_blocklist_expire_seconds">rbd_blocklist_expire_seconds</span> |  number of seconds to blocklist - set to 0 for OSD default | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_blocklist_on_break_lock">rbd_blocklist_on_break_lock</span> |  whether to blocklist clients whose lock was broken | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache">rbd_cache</span> |  whether to enable caching (writeback unless rbd_cache_max_dirty is 0) | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_block_writes_upfront">rbd_cache_block_writes_upfront</span> |  whether to block writes to the cache before the aio_write call completes | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_max_dirty">rbd_cache_max_dirty</span> |  dirty limit in bytes - set to 0 for write-through caching | Advanced | Size | 24_M |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_max_dirty_age">rbd_cache_max_dirty_age</span> |  seconds in cache before writeback starts | Advanced | Float | 1 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_max_dirty_object">rbd_cache_max_dirty_object</span> |  dirty limit for objects - set to 0 for auto calculate from rbd_cache_size | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_policy">rbd_cache_policy</span> |  cache policy for handling writes. | Advanced | Str | writearound |  |  |  | ["writethrough", "writeback", "writearound"] |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_size">rbd_cache_size</span> |  cache size in bytes | Advanced | Size | 32_M |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_target_dirty">rbd_cache_target_dirty</span> |  target dirty limit in bytes | Advanced | Size | 16_M |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_cache_writethrough_until_flush">rbd_cache_writethrough_until_flush</span> |  whether to make writeback caching writethrough until flush is called, to be sure the user of librbd will send flushes so that writeback is safe | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_clone_copy_on_read">rbd_clone_copy_on_read</span> |  copy-up parent image blocks to clone upon read request | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_compression_hint">rbd_compression_hint</span> |  Compression hint to send to the OSDs during writes | Basic | Str | none |  |  |  | ["none", "compressible", "incompressible"] |  |  | RUNTIME | rbd |  |  |  |
| <span id="SP_rbd_concurrent_management_ops">rbd_concurrent_management_ops</span> |  how many operations can be in flight for a management operation like deleting or resizing an image | Advanced | Uint | 10 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_config_pool_override_update_timestamp">rbd_config_pool_override_update_timestamp</span> |  timestamp of last update to pool-level config overrides | Dev | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_default_clone_format">rbd_default_clone_format</span> |  default internal format for handling clones | Advanced | Str | auto |  |  |  | ["1", "2", "auto"] |  |  | RUNTIME | rbd |  | This sets the internal format for tracking cloned images. The setting of '1' requires attaching to protected snapshots that cannot be removed until the clone is removed/flattened. The setting of '2' will allow clones to be attached to any snapshot and permits removing in-use parent snapshots but requires Mimic or later clients. The default setting of 'auto' will use the v2 format if the cluster is configured to require mimic or later clients. |  |
| <span id="SP_rbd_default_data_pool">rbd_default_data_pool</span> |  default pool for storing data blocks for new images | Advanced | Str |  |  |  |  |  |  |  |  | rbd | [](std::string *value, std::string *error_message) {
  std::regex pattern("^[^@/]*$");
  if (!std::regex_match (*value, pattern)) {
    *value = "";
    *error_message = "ignoring invalid RBD data pool";
  }
  return 0;
} |  |  |
| <span id="SP_rbd_default_features">rbd_default_features</span> |  default v2 image features for new images | Advanced | Str | layering,exclusive-lock,object-map,fast-diff,deep-flatten |  |  |  |  |  |  | RUNTIME | rbd | [](std::string *value, std::string *error_message) {
  std::stringstream ss;
  uint64_t features = librbd::rbd_features_from_string(*value, &ss);
  // Leave this in integer form to avoid breaking Cinder.  Someday
  // we would like to present this in string form instead...
  *value = stringify(features);
  if (ss.str().size()) {
    return -EINVAL;
  }
  return 0;
} | RBD features are only applicable for v2 images. This setting accepts either an integer bitmask value or comma-delimited string of RBD feature names. This setting is always internally stored as an integer bitmask value. The mapping between feature bitmask value and feature name is as follows: +1 -> layering, +2 -> striping, +4 -> exclusive-lock, +8 -> object-map, +16 -> fast-diff, +32 -> deep-flatten, +64 -> journaling, +128 -> data-pool |  |
| <span id="SP_rbd_default_format">rbd_default_format</span> |  default image format for new images | Advanced | Uint | 2 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_default_map_options">rbd_default_map_options</span> |  default krbd map options | Advanced | Str |  |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_default_order">rbd_default_order</span> |  default order (data block object size) for new images | Advanced | Uint | 22 |  |  |  |  |  |  |  | rbd |  | This configures the default object size for new images. The value is used as a power of two, meaning ``default_object_size = 2 ^ rbd_default_order``. Configure a value between 12 and 25 (inclusive), translating to 4KiB lower and 32MiB upper limit. |  |
| <span id="SP_rbd_default_pool">rbd_default_pool</span> |  default pool for storing new images | Advanced | Str | rbd |  |  |  |  |  |  |  | rbd | [](std::string *value, std::string *error_message) {
  std::regex pattern("^[^@/]+$");
  if (!std::regex_match (*value, pattern)) {
    *value = "rbd";
    *error_message = "invalid RBD default pool, resetting to 'rbd'";
  }
  return 0;
} |  |  |
| <span id="SP_rbd_default_snapshot_quiesce_mode">rbd_default_snapshot_quiesce_mode</span> |  default snapshot quiesce mode | Advanced | Str | required |  |  |  | ["required", "ignore-error", "skip"] |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_default_stripe_count">rbd_default_stripe_count</span> |  default stripe count for new images | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_default_stripe_unit">rbd_default_stripe_unit</span> |  default stripe width for new images | Advanced | Size | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_disable_zero_copy_writes">rbd_disable_zero_copy_writes</span> |  Disable the use of zero-copy writes to ensure unstable writes from clients cannot cause a CRC mismatch | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_discard_granularity_bytes">rbd_discard_granularity_bytes</span> |  minimum aligned size of discard operations | Advanced | Uint | 64_K |  | 4_K | 32_M |  |  |  |  | rbd | [](std::string *value, std::string *error_message) {
  uint64_t f = strict_si_cast<uint64_t>(*value, error_message);
  if (!error_message->empty()) {
    return -EINVAL;
  } else if (!isp2(f)) {
    *error_message = "value must be a power of two";
    return -EINVAL;
  }
  return 0;
} |  |  |
| <span id="SP_rbd_discard_on_zeroed_write_same">rbd_discard_on_zeroed_write_same</span> |  discard data on zeroed write same instead of writing zero | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_enable_alloc_hint">rbd_enable_alloc_hint</span> |  when writing a object, it will issue a hint to osd backend to indicate the expected size object need | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_invalidate_object_map_on_timeout">rbd_invalidate_object_map_on_timeout</span> |  true if object map should be invalidated when load or update timeout | Dev | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_io_scheduler">rbd_io_scheduler</span> |  RBD IO scheduler | Advanced | Str | simple |  |  |  | ["none", "simple"] |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_io_scheduler_simple_max_delay">rbd_io_scheduler_simple_max_delay</span> |  maximum io delay (in milliseconds) for simple io scheduler (if set to 0 dalay is calculated based on latency stats) | Advanced | Uint | 0 |  | 0 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_commit_age">rbd_journal_commit_age</span> |  commit time interval, seconds | Advanced | Float | 5 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_max_concurrent_object_sets">rbd_journal_max_concurrent_object_sets</span> |  maximum number of object sets a journal client can be behind before it is automatically unregistered | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_max_payload_bytes">rbd_journal_max_payload_bytes</span> |  maximum journal payload size before splitting | Advanced | Size | 16_K |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_object_flush_age">rbd_journal_object_flush_age</span> |  maximum age (in seconds) for pending commits | Advanced | Float | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_object_flush_bytes">rbd_journal_object_flush_bytes</span> |  maximum number of pending bytes per journal object | Advanced | Size | 1_M |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_object_flush_interval">rbd_journal_object_flush_interval</span> |  maximum number of pending commits per journal object | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_object_max_in_flight_appends">rbd_journal_object_max_in_flight_appends</span> |  maximum number of in-flight appends per journal object | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_object_writethrough_until_flush">rbd_journal_object_writethrough_until_flush</span> |  when enabled, the rbd_journal_object_flush* configuration options are ignored until the first flush so that batched journal IO is known to be safe for consistency | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_order">rbd_journal_order</span> |  default order (object size) for journal data objects | Advanced | Uint | 24 |  | 12 | 26 |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_pool">rbd_journal_pool</span> |  pool for journal objects | Advanced | Str |  |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_journal_splay_width">rbd_journal_splay_width</span> |  number of active journal objects | Advanced | Uint | 4 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_localize_parent_reads">rbd_localize_parent_reads</span> |  localize parent requests to closest OSD | Advanced | Bool | False |  |  |  |  |  | [[rbd_read_from_replica_policy](/rbd/rbd.md#SP_rbd_read_from_replica_policy)] |  | rbd |  |  |  |
| <span id="SP_rbd_localize_snap_reads">rbd_localize_snap_reads</span> |  localize snap read requests to closest OSD | Advanced | Bool | False |  |  |  |  |  | [[rbd_read_from_replica_policy](/rbd/rbd.md#SP_rbd_read_from_replica_policy)] |  | rbd |  |  |  |
| <span id="SP_rbd_mirroring_delete_delay">rbd_mirroring_delete_delay</span> |  time-delay in seconds for rbd-mirror delete propagation | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_mirroring_max_mirroring_snapshots">rbd_mirroring_max_mirroring_snapshots</span> |  mirroring snapshots limit | Advanced | Uint | 3 |  | 3 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_mirroring_replay_delay">rbd_mirroring_replay_delay</span> |  time-delay in seconds for rbd-mirror asynchronous replication | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_mirroring_resync_after_disconnect">rbd_mirroring_resync_after_disconnect</span> |  automatically start image resync after mirroring is disconnected due to being laggy | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_move_parent_to_trash_on_remove">rbd_move_parent_to_trash_on_remove</span> |  move parent with clone format v2 children to the trash when deleted | Basic | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_move_to_trash_on_remove">rbd_move_to_trash_on_remove</span> |  automatically move images to the trash when deleted | Basic | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_move_to_trash_on_remove_expire_seconds">rbd_move_to_trash_on_remove_expire_seconds</span> |  default number of seconds to protect deleted images in the trash | Basic | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_mtime_update_interval">rbd_mtime_update_interval</span> |  RBD Image modify timestamp refresh interval. Set to 0 to disable modify timestamp update. | Advanced | Uint | 60 |  | 0 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_non_blocking_aio">rbd_non_blocking_aio</span> |  process AIO ops from a dispatch thread to prevent blocking | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_op_thread_timeout">rbd_op_thread_timeout</span> |  time in seconds for detecting a hung thread | Advanced | Uint | 60 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_op_threads">rbd_op_threads</span> |  number of threads to utilize for internal processing | Advanced | Uint | 1 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_parent_cache_enabled">rbd_parent_cache_enabled</span> |  whether to enable rbd shared ro cache | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_persistent_cache_log_periodic_stats">rbd_persistent_cache_log_periodic_stats</span> |  emit periodic perf stats to debug log | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_persistent_cache_mode">rbd_persistent_cache_mode</span> |  enable persistent write back cache for this volume | Advanced | Str | disabled |  |  |  | ["disabled", "rwl", "ssd"] |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_persistent_cache_path">rbd_persistent_cache_path</span> |  location of the persistent write back cache in a DAX-enabled filesystem on persistent memory | Advanced | Str | /tmp |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_persistent_cache_size">rbd_persistent_cache_size</span> |  size of the persistent write back cache for this volume | Advanced | Uint | 1_G |  | 1_G |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_plugins">rbd_plugins</span> |  comma-delimited list of librbd plugins to enable | Advanced | Str |  |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_bps_burst">rbd_qos_bps_burst</span> |  the desired burst limit of IO bytes | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_bps_burst_seconds">rbd_qos_bps_burst_seconds</span> |  the desired burst duration in seconds of IO bytes | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_bps_limit">rbd_qos_bps_limit</span> |  the desired limit of IO bytes per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_exclude_ops">rbd_qos_exclude_ops</span> |  optionally exclude ops from QoS | Advanced | Str |  |  |  |  |  |  |  | RUNTIME | rbd | [](std::string *value, std::string *error_message) {
    std::ostringstream ss;
    uint64_t exclude_ops = librbd::io::rbd_io_operations_from_string(*value, &ss);
    // Leave this in integer form to avoid breaking Cinder.  Someday
    // we would like to present this in string form instead...
    *value = stringify(exclude_ops);
    if (ss.str().size()) {
      return -EINVAL;
    }
    return 0;
} | Optionally exclude ops from QoS. This setting accepts either an integer bitmask value or comma-delimited string of op names. This setting is always internally stored as an integer bitmask value. The mapping between op bitmask value and op name is as follows: +1 -> read, +2 -> write, +4 -> discard, +8 -> write_same, +16 -> compare_and_write |  |
| <span id="SP_rbd_qos_iops_burst">rbd_qos_iops_burst</span> |  the desired burst limit of IO operations | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_iops_burst_seconds">rbd_qos_iops_burst_seconds</span> |  the desired burst duration in seconds of IO operations | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_iops_limit">rbd_qos_iops_limit</span> |  the desired limit of IO operations per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_bps_burst">rbd_qos_read_bps_burst</span> |  the desired burst limit of read bytes | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_bps_burst_seconds">rbd_qos_read_bps_burst_seconds</span> |  the desired burst duration in seconds of read bytes | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_bps_limit">rbd_qos_read_bps_limit</span> |  the desired limit of read bytes per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_iops_burst">rbd_qos_read_iops_burst</span> |  the desired burst limit of read operations | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_iops_burst_seconds">rbd_qos_read_iops_burst_seconds</span> |  the desired burst duration in seconds of read operations | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_read_iops_limit">rbd_qos_read_iops_limit</span> |  the desired limit of read operations per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_schedule_tick_min">rbd_qos_schedule_tick_min</span> |  minimum schedule tick (in milliseconds) for QoS | Advanced | Uint | 50 |  | 1 |  |  |  |  |  | rbd |  | This determines the minimum time (in milliseconds) at which I/Os can become unblocked if the limit of a throttle is hit. In terms of the token bucket algorithm, this is the minimum interval at which tokens are added to the bucket. |  |
| <span id="SP_rbd_qos_write_bps_burst">rbd_qos_write_bps_burst</span> |  the desired burst limit of write bytes | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_write_bps_burst_seconds">rbd_qos_write_bps_burst_seconds</span> |  the desired burst duration in seconds of write bytes | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_write_bps_limit">rbd_qos_write_bps_limit</span> |  the desired limit of write bytes per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_write_iops_burst">rbd_qos_write_iops_burst</span> |  the desired burst limit of write operations | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_write_iops_burst_seconds">rbd_qos_write_iops_burst_seconds</span> |  the desired burst duration in seconds of write operations | Advanced | Uint | 1 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_qos_write_iops_limit">rbd_qos_write_iops_limit</span> |  the desired limit of write operations per second | Advanced | Uint | 0 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_quiesce_notification_attempts">rbd_quiesce_notification_attempts</span> |  the number of quiesce notification attempts | Dev | Uint | 10 |  | 1 |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_read_from_replica_policy">rbd_read_from_replica_policy</span> |  Read replica policy send to the OSDS during reads | Basic | Str | default |  |  |  | ["default", "balance", "localize"] |  |  | RUNTIME | rbd |  |  |  |
| <span id="SP_rbd_readahead_disable_after_bytes">rbd_readahead_disable_after_bytes</span> |  how many bytes are read in total before readahead is disabled | Advanced | Size | 50_M |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_readahead_max_bytes">rbd_readahead_max_bytes</span> |  set to 0 to disable readahead | Advanced | Size | 512_K |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_readahead_trigger_requests">rbd_readahead_trigger_requests</span> |  number of sequential requests necessary to trigger readahead | Advanced | Uint | 10 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_request_timed_out_seconds">rbd_request_timed_out_seconds</span> |  number of seconds before maintenance request times out | Advanced | Uint | 30 |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_skip_partial_discard">rbd_skip_partial_discard</span> |  skip discard (zero) of unaligned extents within an object | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_sparse_read_threshold_bytes">rbd_sparse_read_threshold_bytes</span> |  threshold for issuing a sparse-read | Advanced | Size | 64_K |  |  |  |  |  |  |  | rbd |  | minimum number of sequential bytes to read against an object before issuing a sparse-read request to the cluster. 0 implies it must be a full object read to issue a sparse-read, 1 implies always use sparse-read, and any value larger than the maximum object size will disable sparse-read for all requests |  |
| <span id="SP_rbd_tracing">rbd_tracing</span> |  true if LTTng-UST tracepoints should be enabled | Advanced | Bool | False |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_validate_names">rbd_validate_names</span> |  validate new image names for RBD compatibility | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
| <span id="SP_rbd_validate_pool">rbd_validate_pool</span> |  validate empty pools for RBD compatibility | Advanced | Bool | True |  |  |  |  |  |  |  | rbd |  |  |  |
