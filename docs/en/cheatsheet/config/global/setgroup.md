<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_setgroup">setgroup</span> |  GID or group name to switch to on startup | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  | [[setuser](setuser.md#SP_setuser)] | STARTUP | ["mon", "mgr", "osd", "mds"] |  |  This is normally specified by the systemd unit file. | service |
