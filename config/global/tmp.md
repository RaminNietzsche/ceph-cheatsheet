<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_tmp_dir">tmp_dir</span> |  Path for the 'tmp' directory | <span class="badge badge-level-advanced">Advanced</span> | Str | /tmp |  |  |  |  |  | [[admin_socket](admin.md#SP_admin_socket)] | RUNTIME | common |  |  |  |
| <span id="SP_tmp_file_template">tmp_file_template</span> |  Template for temporary files created by daemons for ceph tell commands | <span class="badge badge-level-advanced">Advanced</span> | Str |  | $tmp_dir/$cluster-$name.XXXXXX |  |  |  |  |  | RUNTIME | ["osd", "mds", "mon"] |  |  The template file name prefix for temporary files. For example, temporary files may be created by 'ceph tell' commands using the --daemon-output-file switch. |  |
