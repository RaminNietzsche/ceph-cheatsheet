<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_rados_mon_op_timeout">rados_mon_op_timeout</span> |  Timeout for operations handled by Monitors, for example statfs(). (0 is unlimited) | <span class="badge badge-level-advanced">Advanced</span> | Secs | 0 |  | 0 |  |  |  |  | RUNTIME |  |  |  |  |
| <span id="SP_rados_osd_op_timeout">rados_osd_op_timeout</span> |  Timeout for operations handled by OSDs, for example write(). (0 is unlimited) | <span class="badge badge-level-advanced">Advanced</span> | Secs | 0 |  | 0 |  |  |  |  | RUNTIME |  |  |  |  |
| <span id="SP_rados_replica_read_policy">rados_replica_read_policy</span> |  Read policy for sending read requests to OSD | <span class="badge badge-level-advanced">Advanced</span> | Str | default |  |  |  | ["default", "balance", "localize"] |  |  | RUNTIME |  |  |  |  |
| <span id="SP_rados_replica_read_policy_on_objclass">rados_replica_read_policy_on_objclass</span> |  Enable read policy for sending read requests to OSD on objclass ops | <span class="badge badge-level-advanced">Advanced</span> | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_rados_tracing">rados_tracing</span> |  Should LTTng-UST tracepoints be enabled? | <span class="badge badge-level-advanced">Advanced</span> | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
