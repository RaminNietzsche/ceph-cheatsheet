| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_err_to_graylog">err_to_graylog</span> |  send critical error log lines to remote graylog server | Basic | Bool | False |  |  |  |  |  | [[log_to_graylog](./global/log.md#SP_log_to_graylog), [log_graylog_host](./global/log.md#SP_log_graylog_host), [log_graylog_port](./global/log.md#SP_log_graylog_port)] |  |  |  |  |  |
| <span id="SP_err_to_journald">err_to_journald</span> |  send critical error log lines to journald | Basic | Bool | False |  |  |  |  |  | [[log_to_journald](./global/log.md#SP_log_to_journald)] |  |  |  |  |  |
| <span id="SP_err_to_stderr">err_to_stderr</span> |  send critical error log lines to stderr | Basic | Bool | False | True |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_err_to_syslog">err_to_syslog</span> |  send critical error log lines to syslog facility | Basic | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
