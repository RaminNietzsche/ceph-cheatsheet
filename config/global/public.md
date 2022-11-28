| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_public_addr">public_addr</span> |  public-facing address to bind to | Basic | Addr |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  |  |
| <span id="SP_public_addrv">public_addrv</span> |  public-facing address to bind to | Basic | Addrvec |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  |  |
| <span id="SP_public_bind_addr">public_bind_addr</span> |   | Advanced | Addr |  |  |  |  |  |  |  | STARTUP | mon |  |  |  |
| <span id="SP_public_network">public_network</span> |  Network(s) from which to choose a public address to bind to | Advanced | Str |  |  |  |  |  |  |  | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  | network |
| <span id="SP_public_network_interface">public_network_interface</span> |  Interface name(s) from which to choose an address from a public_network to bind to; public_network must also be specified. | Advanced | Str |  |  |  |  |  |  | [[public_network](~/global/public.md#SP_public_network)] | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  | network |
