| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_kstore_backend">kstore_backend</span> |   | Advanced | Str | rocksdb |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_default_stripe_size">kstore_default_stripe_size</span> |   | Advanced | Size | 64_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_fsck_on_mount">kstore_fsck_on_mount</span> |  Whether or not to run fsck on mount for kstore. | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_fsck_on_mount_deep">kstore_fsck_on_mount_deep</span> |  Whether or not to run deep fsck on mount for kstore | Advanced | Bool | True |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_max_bytes">kstore_max_bytes</span> |   | Advanced | Size | 64_M |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_max_ops">kstore_max_ops</span> |   | Advanced | Uint | 512 |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_nid_prealloc">kstore_nid_prealloc</span> |   | Advanced | Uint | 1_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_onode_map_size">kstore_onode_map_size</span> |   | Advanced | Uint | 1_K |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_rocksdb_options">kstore_rocksdb_options</span> |  Options to pass through when RocksDB is used as the KeyValueDB for kstore. | Advanced | Str | compression=kNoCompression |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_sync_submit_transaction">kstore_sync_submit_transaction</span> |   | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
| <span id="SP_kstore_sync_transaction">kstore_sync_transaction</span> |   | Advanced | Bool | False |  |  |  |  |  |  |  |  |  |  |  |
