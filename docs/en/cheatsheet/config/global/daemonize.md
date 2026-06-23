<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_daemonize">daemonize</span> |  Whether to daemonize (background) after startup | <span class="badge badge-level-advanced">Advanced</span> | Bool | False | True |  |  |  |  | [[pid_file](pid.md#SP_pid_file), [chdir](chdir.md#SP_chdir)] | NO_MON_UPDATE STARTUP | ["mon", "mgr", "osd", "mds"] |  |  | service |
