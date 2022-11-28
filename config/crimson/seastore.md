| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_seastore_block_create">seastore_block_create</span> |  Create SegmentManager file if it doesn't exist | Dev | Bool | True |  |  |  |  |  | [[seastore_device_size](~/crimson/seastore.md#SP_seastore_device_size)] |  |  |  |  |  |
| <span id="SP_seastore_cache_lru_size">seastore_cache_lru_size</span> |  Size in bytes of extents to keep in cache. | Advanced | Size | 64_M |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_default_max_object_size">seastore_default_max_object_size</span> |  default logical address space reservation for seastore objects' data | Dev | Uint | 16 M (uint) |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_default_object_metadata_reservation">seastore_default_object_metadata_reservation</span> |  default logical address space reservation for seastore objects' metadata | Dev | Uint | 16 M (uint) |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_device_size">seastore_device_size</span> |  Total size to use for SegmentManager block file if created | Dev | Size | 50_G |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_journal_batch_capacity">seastore_journal_batch_capacity</span> |  The number limit of records in a journal batch | Dev | Uint | 16 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_journal_batch_flush_size">seastore_journal_batch_flush_size</span> |  The size threshold to force flush a journal batch | Dev | Size | 16_M |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_journal_batch_preferred_fullness">seastore_journal_batch_preferred_fullness</span> |  The record fullness threshold to flush a journal batch | Dev | Float | 0.95 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_journal_iodepth_limit">seastore_journal_iodepth_limit</span> |  The io depth limit to submit journal records | Dev | Uint | 5 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_seastore_segment_size">seastore_segment_size</span> |  Segment size to use for SegmentManager | Advanced | Size | 64_M |  |  |  |  |  |  |  |  |  |  |  |
