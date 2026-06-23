<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_public_addr">public_addr</span> |  Public-facing address to which to bind | <span class="badge badge-level-basic">Basic</span> | Addr |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  |  |
| <span id="SP_public_addrv">public_addrv</span> |  Public-facing addresses to which services are to bind | <span class="badge badge-level-basic">Basic</span> | Addrvec |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  |  |
| <span id="SP_public_bind_addr">public_bind_addr</span> |  | <span class="badge badge-level-advanced">Advanced</span> | Addr |  |  |  |  |  |  |  | STARTUP | mon |  |  |  |
| <span id="SP_public_network">public_network</span> |  Network(s) from which to choose a public address to bind to | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  | network |
| <span id="SP_public_network_interface">public_network_interface</span> |  Interface name(s) from which to choose an address from a ``public_network`` to bind to; ``public_network`` must also be specified. | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  | [[public_network](#SP_public_network)] | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  | network |
