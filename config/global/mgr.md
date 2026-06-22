| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_mgr_client_service_daemon_unregister_timeout">mgr_client_service_daemon_unregister_timeout</span> |  Time to wait during shutdown to deregister a service with the Manager | Dev | Float | 1 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_connect_retry_interval">mgr_connect_retry_interval</span> |  Manager reconnect retry interval | Dev | Float | 1 |  |  |  |  |  |  |  | common |  |  |  |
| <span id="SP_mgr_enable_op_tracker">mgr_enable_op_tracker</span> |  Enable / disable the Manager op tracker | Advanced | Bool | True |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_map_cache_enabled">mgr_map_cache_enabled</span> |  Enable the manager's map cache for API calls | Dev | Bool | True |  |  |  |  |  |  | RUNTIME | mgr |  |  |  |
| <span id="SP_mgr_num_op_tracker_shard">mgr_num_op_tracker_shard</span> |  The number of shards for Manager ops | Advanced | Uint | 32 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_complaint_time">mgr_op_complaint_time</span> |  A Manager operation becomes complaint-worthy after the specified number of seconds have elapsed. | Advanced | Float | 30 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_history_duration">mgr_op_history_duration</span> |  The oldest completed Manager operation to track. | Advanced | Uint | 600 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_history_size">mgr_op_history_size</span> |  | Advanced | Uint | 20 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_history_slow_op_size">mgr_op_history_slow_op_size</span> |  Max number of slow Manager ops to track | Advanced | Uint | 20 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_history_slow_op_threshold">mgr_op_history_slow_op_threshold</span> |  Duration of a Manager op to be considered as a historical slow op | Advanced | Float | 10 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_mgr_op_log_threshold">mgr_op_log_threshold</span> |  | Advanced | Int | 5 |  |  |  |  |  |  |  |  |  |  |  |
