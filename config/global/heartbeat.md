| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_heartbeat_file">heartbeat_file</span> |  File to touch on successful internal heartbeat | Advanced | Str |  |  |  |  |  |  | [[heartbeat_interval](~/global/heartbeat.md#SP_heartbeat_interval)] | STARTUP |  |  | If set, this file will be touched every time an internal heartbeat check succeeds. |  |
| <span id="SP_heartbeat_inject_failure">heartbeat_inject_failure</span> |   | Dev | Int | 0 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_heartbeat_interval">heartbeat_interval</span> |  Frequency of internal heartbeat checks (seconds) | Advanced | Int | 5 |  |  |  |  |  |  | STARTUP |  |  |  |  |
