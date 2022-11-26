## Cephfs

| Param | Default | Min or Valid Range | Description | Long Description |
| ----- | :-----: | --- | ----------- | ---------------- |
| `cephfs_mirror_max_concurrent_directory_syncs` | `3` | `1` | maximum number of concurrent snapshot synchronization threads | maximum number of directory snapshots that can be synchronized concurrently by cephfs-mirror daemon. Controls the number of synchronization threads. | 
| `cephfs_mirror_action_update_interval` | `2` | `1` | interval for driving asynchornous mirror actions | Interval in seconds to process pending mirror update actions. | 
| `cephfs_mirror_restart_mirror_on_blocklist_interval` | `30` | `0` | interval to restart blocklisted instances | Interval in seconds to restart blocklisted mirror instances. Setting to zero (0) disables restarting blocklisted instances. | 
| `cephfs_mirror_max_snapshot_sync_per_cycle` | `3` | `1` | number of snapshots to mirror in one cycle | maximum number of snapshots to mirror when a directory is picked up for mirroring by worker threads. | 
| `cephfs_mirror_directory_scan_interval` | `10` | `1` | interval to scan directories to mirror snapshots | interval in seconds to scan configured directories for snapshot mirroring. | 
| `cephfs_mirror_max_consecutive_failures_per_directory` | `10` | `0` | consecutive failed directory synchronization attempts before marking a directory as \"failed\" | number of consecutive snapshot synchronization failues to mark a directory as \"failed\". failed directories are retried for synchronization less frequently. | 
| `cephfs_mirror_retry_failed_directories_interval` | `60` | `1` | failed directory retry interval for synchronization | interval in seconds to retry synchronization for failed directories. | 
| `cephfs_mirror_restart_mirror_on_failure_interval` | `20` | `0` | interval to restart failed mirror instances | Interval in seconds to restart failed mirror instances. Setting to zero (0) disables restarting failed mirror instances. | 
| `cephfs_mirror_mount_timeout` | `10` | `0` | timeout for mounting primary/seconday ceph file system | Timeout in seconds for mounting primary or secondary (remote) ceph file system by the cephfs-mirror daemon. Setting this to a higher value could result in the mirror daemon getting stalled when mounting a file system if the cluster is not reachable. This option is used to override the usual client_mount_timeout. | 
