| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_objecter_completion_locks_per_session">objecter_completion_locks_per_session</span> |   | Dev | Uint | 32 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_debug_inject_relock_delay">objecter_debug_inject_relock_delay</span> |   | Dev | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_inflight_op_bytes">objecter_inflight_op_bytes</span> |  Max in-flight data in bytes (both directions) | Advanced | Size | 100_M |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_inflight_ops">objecter_inflight_ops</span> |  Max in-flight operations | Advanced | Uint | 1_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_inject_no_watch_ping">objecter_inject_no_watch_ping</span> |   | Dev | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_retry_writes_after_first_reply">objecter_retry_writes_after_first_reply</span> |   | Dev | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_tick_interval">objecter_tick_interval</span> |   | Dev | Float | 5 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_objecter_timeout">objecter_timeout</span> |  Seconds before in-flight op is considered 'laggy' and we query mon for the latest OSDMap | Advanced | Float | 10 |  |  |  |  |  |  |  |  |  |  |  |
