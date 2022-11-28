| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_clog_to_graylog">clog_to_graylog</span> |  Make daemons send cluster log to graylog | Advanced | Str | false |  |  |  |  |  |  | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_graylog_host">clog_to_graylog_host</span> |  Graylog host to cluster log messages | Advanced | Str | 127.0.0.1 |  |  |  |  |  | [[clog_to_graylog](~/config/global/clog#SP_clog_to_graylog)] | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_graylog_port">clog_to_graylog_port</span> |  Graylog port number for cluster log messages | Advanced | Str | 12201 |  |  |  |  |  | [[clog_to_graylog](~/config/global/clog#SP_clog_to_graylog)] | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_monitors">clog_to_monitors</span> |  Make daemons send cluster log messages to monitors | Advanced | Str | default=true |  |  |  |  |  |  | RUNTIME | ["mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_syslog">clog_to_syslog</span> |  Make daemons send cluster log messages to syslog | Advanced | Str | false |  |  |  |  |  |  | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_syslog_facility">clog_to_syslog_facility</span> |  Syslog facility for cluster log messages | Advanced | Str | default=daemon audit=local0 |  |  |  |  |  | [[clog_to_syslog](~/config/global/clog#SP_clog_to_syslog)] | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |
| <span id="SP_clog_to_syslog_level">clog_to_syslog_level</span> |  Syslog level for cluster log messages | Advanced | Str | info |  |  |  |  |  | [[clog_to_syslog](~/config/global/clog#SP_clog_to_syslog)] | RUNTIME | ["mon", "mgr", "osd", "mds"] |  |  |  |