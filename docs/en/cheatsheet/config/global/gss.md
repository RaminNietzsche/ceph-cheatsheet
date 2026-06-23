<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_gss_ktab_client_file">gss_ktab_client_file</span> |  GSS/KRB5 Keytab file for client authentication | <span class="badge badge-level-advanced">Advanced</span> | Str | /var/lib/ceph/$name/gss_client_$name.ktab |  |  |  |  |  |  |  | ["mon", "osd"] |  |  This sets the full path for the GSS/Kerberos client keytab file location. |  |
| <span id="SP_gss_target_name">gss_target_name</span> |  | <span class="badge badge-level-advanced">Advanced</span> | Str | ceph |  |  |  |  |  |  |  | ["mon", "osd"] |  |  This sets the GSS target service name. |  |
