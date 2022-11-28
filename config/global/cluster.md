| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_cluster_addr">cluster_addr</span> |  cluster-facing address to bind to | Basic | Addr |  |  |  |  |  |  |  | STARTUP | osd |  |  | network |
| <span id="SP_cluster_network">cluster_network</span> |  Network(s) from which to choose a cluster address to bind to | Advanced | Str |  |  |  |  |  |  |  | STARTUP | osd |  |  | network |
| <span id="SP_cluster_network_interface">cluster_network_interface</span> |  Interface name(s) from which to choose an address from a cluster_network to bind to; cluster_network must also be specified. | Advanced | Str |  |  |  |  |  |  | [[cluster_network](./global/cluster.md#SP_cluster_network)] | STARTUP | ["mon", "mds", "osd", "mgr"] |  |  | network |
