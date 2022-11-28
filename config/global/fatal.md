| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_fatal_signal_handlers">fatal_signal_handlers</span> |  whether to register signal handlers for SIGABRT etc that dump a stack trace | Advanced | Bool | True |  |  |  |  |  |  | STARTUP | ["mon", "mgr", "osd", "mds"] |  | This is normally true for daemons and values for libraries. | service |
