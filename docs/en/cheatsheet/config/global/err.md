<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_err_to_graylog">err_to_graylog</span> |  Send critical error log lines to remote Graylog server | <span class="badge badge-level-basic">Basic</span> | Bool | False |  |  |  |  |  | [[log_to_graylog](log.md#SP_log_to_graylog), [log_graylog_host](log.md#SP_log_graylog_host), [log_graylog_port](log.md#SP_log_graylog_port)] |  |  |  |  |  |
| <span id="SP_err_to_journald">err_to_journald</span> |  Send critical error log lines to journald | <span class="badge badge-level-basic">Basic</span> | Bool | False |  |  |  |  |  | [[log_to_journald](log.md#SP_log_to_journald)] |  |  |  |  |  |
| <span id="SP_err_to_stderr">err_to_stderr</span> |  send critical error log lines to stderr | <span class="badge badge-level-basic">Basic</span> | Bool | False | True |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_err_to_syslog">err_to_syslog</span> |  Send critical error log lines to syslog facility | <span class="badge badge-level-basic">Basic</span> | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
