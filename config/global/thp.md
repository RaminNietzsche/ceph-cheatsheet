<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_thp">thp</span> |  enable transparent huge page (THP) support | <span class="badge badge-level-dev">Dev</span> | Bool | False |  |  |  |  |  |  | STARTUP |  |  |  Ceph is known to suffer from memory fragmentation due to THP use. This is indicated by RSS usage above configured memory targets. Enabling THP is currently discouraged until selective use of THP by Ceph is implemented. |  |
