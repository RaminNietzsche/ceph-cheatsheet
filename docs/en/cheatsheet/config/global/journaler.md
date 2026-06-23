<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_journaler_prefetch_periods">journaler_prefetch_periods</span> |  Number of striping periods to prefetch while reading MDS journal | <span class="badge badge-level-advanced">Advanced</span> | Uint | 10 |  | 2 |  |  |  |  |  |  |  |  |  |
| <span id="SP_journaler_prezero_periods">journaler_prezero_periods</span> |  Number of striping periods to zero head of MDS journal write position | <span class="badge badge-level-advanced">Advanced</span> | Uint | 5 |  | 2 |  |  |  |  |  |  |  |  |  |
| <span id="SP_journaler_write_head_interval">journaler_write_head_interval</span> |  Interval in seconds between journal header updates (to help bound replay time) | <span class="badge badge-level-advanced">Advanced</span> | Int | 15 |  |  |  |  |  |  |  |  |  |  |  |
