<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_admin_socket">admin_socket</span> |  Path for the runtime control socket file, used by the 'ceph daemon' command | <span class="badge badge-level-advanced">Advanced</span> | Str |  | $run_dir/$cluster-$name.asok |  |  |  |  |  | STARTUP | common |  |  |  |
| <span id="SP_admin_socket_mode">admin_socket_mode</span> |  File mode to set for the admin socket, e.g, '0755' | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  | [[admin_socket](#SP_admin_socket)] | STARTUP | common |  |  |  |
