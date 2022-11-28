| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_admin_socket">admin_socket</span> |  path for the runtime control socket file, used by the 'ceph daemon' command | Advanced | Str |  | $run_dir/$cluster-$name.asok |  |  |  |  |  | STARTUP | common |  |  |  |
| <span id="SP_admin_socket_mode">admin_socket_mode</span> |  file mode to set for the admin socket file, e.g, '0755' | Advanced | Str |  |  |  |  |  |  | [[admin_socket](/config/global/admin.md#SP_admin_socket)] | STARTUP | common |  |  |  |
