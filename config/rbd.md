
## RDB
| Param | Default | Min or Valid Range | Description | Long Description |
| ----- | ------- | ------------------ | ----------- | ---------------- |
| `rbd_default_pool` | rbd | `regex("^[^@/]+$")`|  default pool for storing new images | | 
| `rbd_default_data_pool` |  | `regex("^[^@/]*$")` | default pool for storing data blocks for new images | |
| `rbd_default_features` | `layering,exclusive-lock,object-map,fast-diff,deep-flatten` |  | default v2 image features for new images | RBD features are only applicable for v2 images. This setting accepts either an integer bitmask value or comma-delimited string of RBD feature names. This setting is always internally stored as an integer bitmask value. The mapping between feature bitmask value and feature name is as follows: +1 -> layering, +2 -> striping, +4 -> exclusive-lock, +8 -> object-map, +16 -> fast-diff, +32 -> deep-flatten, +64 -> journaling, +128 -> data-pool |
| `rbd_op_threads` | `1` | |  number of threads to utilize for internal processing | |
| `rbd_op_thread_timeout` | `60` | | time in seconds for detecting a hung thread | |
| `rbd_disable_zero_copy_writes` | `true` |  | Disable the use of zero-copy writes to ensure unstable writes from clients cannot cause a CRC mismatch |  |
| `rbd_non_blocking_aio` | `true` | | process AIO ops from a dispatch thread to prevent blocking | |
| `rbd_cache` | `true` |  | whether to enable caching (writeback unless rbd_cache_max_dirty is 0) |  |
| `rbd_cache_policy` | writearound | "writethrough", "writeback", "writearound" | cache policy for handling writes. |  |
| `rbd_cache_writethrough_until_flush` | `true` | |  whether to make writeback caching writethrough until flush is called, to be sure the user of librbd will send flushes so that writeback is safe | |
| `rbd_cache_size` | `32_M` | | cache size in bytes | |
| `rbd_cache_max_dirty` | `24_M` |  | dirty limit in bytes - set to 0 for write-through caching | |
| `rbd_cache_target_dirty` | `16_M` |  | target dirty limit in bytes |  |
| `rbd_cache_max_dirty_age` | `1.0` | | seconds in cache before writeback starts | |
| `rbd_cache_max_dirty_object` | `0` | | dirty limit for objects - set to 0 for auto calculate from rbd_cache_size | |
| `rbd_cache_block_writes_upfront` | `false` | | whether to block writes to the cache before the aio_write call completes | |
| `rbd_parent_cache_enabled` | `false`  | | whether to enable rbd shared ro cache |  |
| `rbd_concurrent_management_ops` | `10` | min(`1`) | how many operations can be in flight for a management operation like deleting or resizing an image |  |
| `rbd_balance_snap_reads` | `false` |  | distribute snap read requests to random OSD | |
| `rbd_localize_snap_reads` | `false` |  | localize snap read requests to closest OSD | |
| `rbd_balance_parent_reads` | `false` |  | distribute parent read requests to random OSD | |
| `rbd_localize_parent_reads` | `false` |  | localize parent requests to closest OSD | |
| `rbd_sparse_read_threshold_bytes` | `64_K` |  | threshold for issuing a sparse-read | minimum number of sequential bytes to read against an object before issuing a sparse-read request to the cluster. 0 implies it must be a full object read to issue a sparse-read, 1 implies always use sparse-read, and any value larger than the maximum object size will disable sparse-read for all requests | 
| `rbd_readahead_trigger_requests` | `10` |  | number of sequential requests necessary to trigger readahead | |
| `rbd_readahead_max_bytes` | `512_K` | | set to 0 to disable readahead |  |
| `rbd_readahead_disable_after_bytes` | `50_M` | | how many bytes are read in total before readahead is disabled | |
| `rbd_clone_copy_on_read` | `false` | | copy-up parent image blocks to clone upon read request | |
| `rbd_blocklist_on_break_lock` | `true` | | whether to blocklist clients whose lock was broken | |
| `rbd_blocklist_expire_seconds` | `0` |  | number of seconds to blocklist - set to 0 for OSD default | |
| `rbd_request_timed_out_seconds` | `30` |  | number of seconds before maintenance request times out | |
| `rbd_skip_partial_discard` | `true` | | skip discard (zero) of unaligned extents within an object | |
| `rbd_discard_granularity_bytes` | `64_K`| between(4_K, 32_M) | minimum aligned size of discard operations | |
| `rbd_enable_alloc_hint` | `true` | | when writing a object, it will issue a hint to osd backend to indicate the expected size object need | |
| `rbd_compression_hint` | none | "none", "compressible", "incompressible" | Compression hint to send to the OSDs during writes | |
| `rbd_read_from_replica_policy` | default | "default", "balance", "localize"  | Read replica policy send to the OSDS during reads | |
| `rbd_tracing` | `false` | | true if LTTng-UST tracepoints should be enabled | |
| `rbd_blkin_trace_all` | `false` | | create a blkin trace for all RBD requests | |
| `rbd_validate_pool` | `true` | | validate empty pools for RBD compatibility | |
| `rbd_validate_names` | `true` | | validate new image names for RBD compatibility | |
| `rbd_invalidate_object_map_on_timeout` | `true` | | true if object map should be invalidated when load or update timeout | |
| `rbd_auto_exclusive_lock_until_manual_request` | `true` | | automatically acquire/release exclusive lock until it is explicitly requested | |
| `rbd_move_to_trash_on_remove` | `false` | | automatically move images to the trash when deleted | |
| `rbd_move_to_trash_on_remove_expire_seconds` | `0` | | default number of seconds to protect deleted images in the trash | |
| `rbd_move_parent_to_trash_on_remove` | `false` | | move parent with clone format v2 children to the trash when deleted | |
| `rbd_mirroring_resync_after_disconnect` | `false` | | automatically start image resync after mirroring is disconnected due to being laggy | |
| `rbd_mirroring_delete_delay` | `0` | | time-delay in seconds for rbd-mirror delete propagation | |
| `rbd_mirroring_replay_delay` | `0` | | time-delay in seconds for rbd-mirror asynchronous replication | |
| `rbd_mirroring_max_mirroring_snapshots` | `3` | min(`3`) | mirroring snapshots limit | |
| `rbd_default_format` | `2` | | default image format for new images | |
| `rbd_default_order` | `22` | | default order (data block object size) for new images | |
| `rbd_default_stripe_count` | `0` | | default stripe count for new images | |
| `rbd_default_stripe_unit` | `0` | | default stripe width for new images | |
| `rbd_default_map_options` |  |  | default krbd map options | |
| `rbd_default_clone_format`| auto | "1", "2", "auto" | default internal format for handling clones | This sets the internal format for tracking cloned images. The setting of '1' requires attaching to protected snapshots that cannot be removed until the clone is removed/flattened. The setting of '2' will allow clones to be attached to any snapshot and permits removing in-use parent snapshots but requires Mimic or later clients. The default setting of 'auto' will use the v2 format if the cluster is configured to require mimic or later clients. |
| `rbd_journal_order` | `24` | between(12, 26) | default order (object size) for journal data objects |  |
| `rbd_journal_splay_width` | `4` | | number of active journal objects | |
| `rbd_journal_commit_age` | `5` |  | commit time interval, seconds | |
| `rbd_journal_object_writethrough_until_flush` | `true` | when enabled, the rbd_journal_object_flush* configuration options are ignored until the first flush so that batched journal IO is known to be safe for consistency | |
| `rbd_journal_object_flush_interval` | `0` |  | maximum number of pending commits per journal object | |
| `rbd_journal_object_flush_bytes` | `1_M` |  | maximum number of pending bytes per journal object | |
| `rbd_journal_object_flush_age` | `0` |  | maximum age (in seconds) for pending commits | |
| `rbd_journal_object_max_in_flight_appends` | `0` | | maximum number of in-flight appends per journal object | |
| `rbd_journal_pool` |  |  | pool for journal objects | |
| `rbd_journal_max_payload_bytes` | `16384`  | | maximum journal payload size before splitting |  |
| `rbd_journal_max_concurrent_object_sets` | `0` | | maximum number of object sets a journal client can be behind before it is automatically unregistered | |
| `rbd_qos_iops_limit` | `0` |  | the desired limit of IO operations per second | |
| `rbd_qos_bps_limit` | `0` |  | the desired limit of IO bytes per second | |
| `rbd_qos_read_iops_limit` | `0` |  | the desired limit of read operations per second | |
| `rbd_qos_write_iops_limit` | `0` |  | the desired limit of write operations per second | |
| `rbd_qos_read_bps_limit` | `0` |  | the desired limit of read bytes per second | |
| `rbd_qos_write_bps_limit` | `0` |  | the desired limit of write bytes per second | |
| `rbd_qos_iops_burst` | `0` |  | the desired burst limit of IO operations | |
| `rbd_qos_bps_burst` | `0` |  | the desired burst limit of IO bytes | |
| `rbd_qos_read_iops_burst` | `0` |  | the desired burst limit of read operations | |
| `rbd_qos_write_iops_burst` | `0` |  | the desired burst limit of write operations | |
| `rbd_qos_read_bps_burst` | `0` |  | the desired burst limit of read bytes | |
| `rbd_qos_write_bps_burst` | `0` | | the desired burst limit of write bytes | |
| `rbd_qos_iops_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of IO operations | |
| `rbd_qos_bps_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of IO bytes |  |
| `rbd_qos_read_iops_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of read operations |  |
| `rbd_qos_write_iops_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of write operations |  |
| `rbd_qos_read_bps_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of read bytes |  |
| `rbd_qos_write_bps_burst_seconds` | `1` | min(`1`) | the desired burst duration in seconds of write bytes | |
| `rbd_qos_schedule_tick_min` | `50` | min(`1`) | minimum schedule tick (in milliseconds) for QoS | |
| `rbd_discard_on_zeroed_write_same` | `true` |  | discard data on zeroed write same instead of writing zero |  |
| `rbd_mtime_update_interval` | `60` | min(`0`) | RBD Image modify timestamp refresh interval. Set to 0 to disable modify timestamp update. | |
| `rbd_atime_update_interval` | `60` | min(`0`) | RBD Image access timestamp refresh interval. Set to 0 to disable access timestamp update. | 
| `rbd_io_scheduler` | simple | "none", "simple" | RBD IO scheduler |  |
| `rbd_io_scheduler_simple_max_delay` | `0` | min(`0`) | maximum io delay (in milliseconds) for simple io scheduler (if set to 0 dalay is calculated based on latency stats) |  | 
| `rbd_persistent_cache_mode` | disabled | "disabled", "rwl", "ssd" | enable persistent write back cache for this volume | |
| `rbd_persistent_cache_log_periodic_stats` | `false` |  | emit periodic perf stats to debug log |  |
| `rbd_persistent_cache_size` | `1073741824` | min(`1073741824`) | size of the persistent write back cache for this volume |  |
| `rbd_persistent_cache_path` | `/tmp` | | location of the persistent write back cache in a DAX-enabled filesystem on persistent memory | |
| `rbd_quiesce_notification_attempts` | `10` | `1` | the number of quiesce notification attempts | 
| `rbd_default_snapshot_quiesce_mode` | required | "required", "ignore-error", "skip" | default snapshot quiesce mode | |
| `rbd_plugins` |  | | comma-delimited list of librbd plugins to enable | |
| `rbd_config_pool_override_update_timestamp` | `0` | | timestamp of last update to pool-level config overrides | |
