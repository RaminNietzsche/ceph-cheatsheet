| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_gss_ktab_client_file">gss_ktab_client_file</span> |  GSS/KRB5 Keytab file for client authentication | Advanced | Str | /var/lib/ceph/$name/gss_client_$name.ktab |  |  |  |  |  |  |  | ["mon", "osd"] |  | This sets the full path for the GSS/Kerberos client keytab file location. |  |
| <span id="SP_gss_target_name">gss_target_name</span> |   | Advanced | Str | ceph |  |  |  |  |  |  |  | ["mon", "osd"] |  | This sets the gss target service name. |  |
