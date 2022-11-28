| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_fuse_allow_other">fuse_allow_other</span> |  pass allow_other to FUSE on mount | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_atomic_o_trunc">fuse_atomic_o_trunc</span> |  pass atomic_o_trunc flag to FUSE on mount | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_big_writes">fuse_big_writes</span> |  big_writes is deprecated in libfuse 3.0.0 | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_debug">fuse_debug</span> |  enable debugging for the libfuse | Advanced | Bool | False |  |  |  |  |  |  | NO_MON_UPDATESTARTUP | mds_client |  |  |  |
| <span id="SP_fuse_default_permissions">fuse_default_permissions</span> |  pass default_permisions to FUSE on mount | Advanced | Bool | False |  |  |  |  |  |  | STARTUP | mds_client |  |  |  |
| <span id="SP_fuse_disable_pagecache">fuse_disable_pagecache</span> |  disable page caching in the kernel for this FUSE mount | Advanced | Bool | False |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_max_write">fuse_max_write</span> |  set the maximum number of bytes in a single write operation | Advanced | Size | 0 |  |  |  |  |  |  |  | mds_client |  | Set the maximum number of bytes in a single write operation that may pass atomically through FUSE. The FUSE default is 128kB and may be indicated by setting this option to 0. |  |
| <span id="SP_fuse_multithreaded">fuse_multithreaded</span> |  allow parallel processing through FUSE library | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_require_active_mds">fuse_require_active_mds</span> |  require active MDSs in the file system when mounting | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_set_user_groups">fuse_set_user_groups</span> |  check for ceph-fuse to consider supplementary groups for permissions | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_splice_move">fuse_splice_move</span> |  enable splice move to reduce the memory copies | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_splice_read">fuse_splice_read</span> |  enable splice read to reduce the memory copies | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_splice_write">fuse_splice_write</span> |  enable splice write to reduce the memory copies | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_syncfs_on_mksnap">fuse_syncfs_on_mksnap</span> |  synchronize all local metadata/file changes after snapshot | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
| <span id="SP_fuse_use_invalidate_cb">fuse_use_invalidate_cb</span> |  use fuse 2.8+ invalidate callback to keep page cache consistent | Advanced | Bool | True |  |  |  |  |  |  |  | mds_client |  |  |  |
