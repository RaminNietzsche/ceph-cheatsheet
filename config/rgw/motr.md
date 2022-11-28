| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_motr_ha_endpoint">motr_ha_endpoint</span> |  experimental Option to set Motr HA agent endpoint address | Advanced | Str | 192.168.180.182@tcp:12345:1:1 |  |  |  |  |  |  |  | rgw |  | example value 192.168.180.182@tcp:12345:1:1 |  |
| <span id="SP_motr_my_endpoint">motr_my_endpoint</span> |  experimental Option to set my Motr endpoint address | Advanced | Str | 192.168.180.182@tcp:12345:4:1 |  |  |  |  |  |  |  | rgw |  | example value 192.168.180.182@tcp:12345:4:1 |  |
| <span id="SP_motr_my_fid">motr_my_fid</span> |  experimental Option to set my Motr fid | Advanced | Str | 0x7200000000000001:0x0 |  |  |  |  |  |  |  | rgw |  | example value 0x7200000000000001:0x29 |  |
| <span id="SP_motr_profile_fid">motr_profile_fid</span> |  experimental Option to set Motr profile fid | Advanced | Str | 0x7000000000000001:0x0 |  |  |  |  |  |  |  | rgw |  | example value 0x7000000000000001:0x4f |  |
| <span id="SP_motr_tracing_enabled">motr_tracing_enabled</span> |  Set to true when Motr client debugging is needed | Advanced | Bool | False |  |  |  |  |  |  |  | rgw |  |  |  |
