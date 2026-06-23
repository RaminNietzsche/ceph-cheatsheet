<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_fatal_signal_handlers">fatal_signal_handlers</span> |  Whether to register signal handlers for SIGABRT etc that dump a stack trace | <span class="badge badge-level-advanced">Advanced</span> | Bool | True |  |  |  |  |  |  | STARTUP | ["mon", "mgr", "osd", "mds"] |  |  This is normally true for daemons and values for libraries. | service |
