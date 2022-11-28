| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_bdev_aio">bdev_aio</span> |   | Advanced | Bool | True |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_aio_max_queue_depth">bdev_aio_max_queue_depth</span> |   | Advanced | Int | 1024 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_aio_poll_ms">bdev_aio_poll_ms</span> |   | Advanced | Int | 250 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_aio_reap_max">bdev_aio_reap_max</span> |   | Advanced | Int | 16 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_async_discard">bdev_async_discard</span> |   | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_block_size">bdev_block_size</span> |   | Advanced | Size | 4_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_debug_aio">bdev_debug_aio</span> |   | Dev | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_debug_aio_log_age">bdev_debug_aio_log_age</span> |   | Dev | Float | 5 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_debug_aio_suicide_timeout">bdev_debug_aio_suicide_timeout</span> |   | Dev | Float | 1_min |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_debug_inflight_ios">bdev_debug_inflight_ios</span> |   | Dev | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_enable_discard">bdev_enable_discard</span> |   | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_flock_retry">bdev_flock_retry</span> |  times to retry the flock | Advanced | Uint | 3 |  |  |  |  |  |  |  |  |  | The number of times to retry on getting the block device lock. Programs such as systemd-udevd may compete with Ceph for this lock. 0 means 'unlimited'. |  |
| <span id="SP_bdev_flock_retry_interval">bdev_flock_retry_interval</span> |  interval to retry the flock | Advanced | Float | 0.1 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_inject_crash">bdev_inject_crash</span> |   | Dev | Int | 0 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_inject_crash_flush_delay">bdev_inject_crash_flush_delay</span> |   | Dev | Int | 2 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_ioring">bdev_ioring</span> |  Enables Linux io_uring API instead of libaio | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_ioring_hipri">bdev_ioring_hipri</span> |  Enables Linux io_uring API Use polled IO completions | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_ioring_sqthread_poll">bdev_ioring_sqthread_poll</span> |  Enables Linux io_uring API Offload submission/completion to kernel thread | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_nvme_unbind_from_kernel">bdev_nvme_unbind_from_kernel</span> |   | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_read_buffer_alignment">bdev_read_buffer_alignment</span> |   | Advanced | Size | 4_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_bdev_read_preallocated_huge_buffers">bdev_read_preallocated_huge_buffers</span> |  description of pools arrangement for huge page-based read buffers | Advanced | Str |  |  |  |  |  |  | [[bluestore_max_blob_size](./global/bluestore.md#SP_bluestore_max_blob_size)] |  |  |  | Arrangement of preallocated, huge pages-based pools for reading from a KernelDevice. Applied to minimize size of scatter-gather lists sent to NICs. Targets really  big buffers (>= 2 or 4 MBs). Keep in mind the system must be configured accordingly (see /proc/sys/vm/nr_hugepages). Otherwise the OSD wil fail early. Beware BlueStore, by default, stores large chunks across many smaller blobs. Increasing bluestore_max_blob_size changes that, and thus allows the data to be read back into small number of huge page-backed buffers. |  |
| <span id="SP_bdev_type">bdev_type</span> |  Explicitly set the device type to select the driver if it's needed | Advanced | Str |  |  |  |  | ["aio", "spdk", "pmem", "hm_smr"] |  |  |  |  |  |  |  |
