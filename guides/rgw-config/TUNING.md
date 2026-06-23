# RGW Config — Tuning Quick Reference

All **441** RGW options with tuning model and one-line guidance. Each topic page has step-by-step **Finding optimal value** sections.

[← RGW config overview](OVERVIEW.md) · [Tuning quick reference](TUNING.md)

| Option | Default | Model | Quick answer | Topic |
|--------|---------|-------|--------------|-------|
| [`motr_admin_endpoint`](motr-experimental.md#motr_admin_endpoint) | `192.168.180.182@tcp:12345:4:1` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_admin_fid`](motr-experimental.md#motr_admin_fid) | `0x7200000000000001:0x0` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_ha_endpoint`](motr-experimental.md#motr_ha_endpoint) | `192.168.180.182@tcp:12345:1:1` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_my_endpoint`](motr-experimental.md#motr_my_endpoint) | `192.168.180.182@tcp:12345:4:1` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_my_fid`](motr-experimental.md#motr_my_fid) | `0x7200000000000001:0x0` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_profile_fid`](motr-experimental.md#motr_profile_fid) | `0x7000000000000001:0x0` | Architecture | Match deployment topology; use upstream default | [Motr backend](motr-experimental.md) |
| [`motr_tracing_enabled`](motr-experimental.md#motr_tracing_enabled) | `False` | Dev | Keep `False` in production | [Motr backend](motr-experimental.md) |
| [`d4n_writecache_enabled`](d4n-cache.md#d4n_writecache_enabled) | `False` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`daos_pool`](experimental-backends.md#daos_pool) | `tank` | Capacity | Dedicated fast disk with growth headroom | [Experimental backends](experimental-backends.md) |
| [`dbstore_config_uri`](experimental-backends.md#dbstore_config_uri) | `file:/var/lib/ceph/radosgw/dbstore-config.db` | Capacity | Dedicated fast disk with growth headroom | [Experimental backends](experimental-backends.md) |
| [`dbstore_db_dir`](experimental-backends.md#dbstore_db_dir) | `/var/lib/ceph/radosgw` | Capacity | Dedicated fast disk with growth headroom | [Experimental backends](experimental-backends.md) |
| [`dbstore_db_name_prefix`](experimental-backends.md#dbstore_db_name_prefix) | `dbstore` | Performance | Baseline → adjust → validate under real workload | [Experimental backends](experimental-backends.md) |
| [`rgw_account_default_quota_max_objects`](quotas.md#rgw_account_default_quota_max_objects) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Quota sync & defaults](quotas.md) |
| [`rgw_account_default_quota_max_size`](quotas.md#rgw_account_default_quota_max_size) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Quota sync & defaults](quotas.md) |
| [`rgw_acl_grants_max_num`](api-limits.md#rgw_acl_grants_max_num) | `100` | Policy | Upstream default (`100`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_admin_entry`](api-limits.md#rgw_admin_entry) | `admin` | Policy | Upstream default (`admin`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_allow_notification_secrets_in_cleartext`](notifications.md#rgw_allow_notification_secrets_in_cleartext) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Bucket notifications](notifications.md) |
| [`rgw_asio_assert_yielding`](frontends.md#rgw_asio_assert_yielding) | `False` | Dev | Keep `False` in production | [Frontends & HTTP stack](frontends.md) |
| [`rgw_backend_store`](experimental-backends.md#rgw_backend_store) | `rados` | Architecture | `rados` in production | [Experimental backends](experimental-backends.md) |
| [`rgw_barbican_url`](encryption.md#rgw_barbican_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Encryption & KMS](encryption.md) |
| [`rgw_beast_enable_async`](frontends.md#rgw_beast_enable_async) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Frontends & HTTP stack](frontends.md) |
| [`rgw_bucket_counters_cache`](bucket-ops.md#rgw_bucket_counters_cache) | `False` | Performance | Baseline → adjust → validate under real workload | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_counters_cache_size`](bucket-ops.md#rgw_bucket_counters_cache_size) | `10000` | Performance | Size ≈ active working set; watch RGW memory | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_default_quota_max_objects`](bucket-ops.md#rgw_bucket_default_quota_max_objects) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_default_quota_max_size`](bucket-ops.md#rgw_bucket_default_quota_max_size) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_eexist_override`](bucket-ops.md#rgw_bucket_eexist_override) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_index_max_aio`](bucket-ops.md#rgw_bucket_index_max_aio) | `128` | Performance | Sweep up until OSD slow ops rise | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_index_transaction_instrumentation`](bucket-ops.md#rgw_bucket_index_transaction_instrumentation) | `False` | Dev | Keep `False` in production | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_logging_obj_roll_time`](bucket-ops.md#rgw_bucket_logging_obj_roll_time) | `300` | Performance | Baseline → adjust → validate under real workload | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_persistent_notif_num_shards`](bucket-ops.md#rgw_bucket_persistent_notif_num_shards) | `11` | Policy | Upstream default (`11`) unless client/compliance requires change | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_quota_cache_size`](bucket-ops.md#rgw_bucket_quota_cache_size) | `10000` | Performance | Size ≈ active working set; watch RGW memory | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_quota_ttl`](bucket-ops.md#rgw_bucket_quota_ttl) | `10_min` | Performance | Balance freshness vs background load | [Bucket operations](bucket-ops.md) |
| [`rgw_bucket_sync_spawn_window`](bucket-ops.md#rgw_bucket_sync_spawn_window) | `20` | Performance | Baseline → adjust → validate under real workload | [Bucket operations](bucket-ops.md) |
| [`rgw_cache_enabled`](caching.md#rgw_cache_enabled) | `True` | Performance | Baseline → adjust → validate under real workload | [Metadata & object caches](caching.md) |
| [`rgw_cache_expiry_interval`](caching.md#rgw_cache_expiry_interval) | `900` | Performance | Size ≈ active working set; watch RGW memory | [Metadata & object caches](caching.md) |
| [`rgw_cache_lru_size`](caching.md#rgw_cache_lru_size) | `25000` | Performance | Size ≈ active working set; watch RGW memory | [Metadata & object caches](caching.md) |
| [`rgw_config_store`](experimental-backends.md#rgw_config_store) | `rados` | Architecture | Match deployment topology; use upstream default | [Experimental backends](experimental-backends.md) |
| [`rgw_content_length_compat`](http-compat.md#rgw_content_length_compat) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_copy_obj_progress`](multipart-copy.md#rgw_copy_obj_progress) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Multipart & copy](multipart-copy.md) |
| [`rgw_copy_obj_progress_every_bytes`](multipart-copy.md#rgw_copy_obj_progress_every_bytes) | `1_M` | Performance | Baseline → adjust → validate under real workload | [Multipart & copy](multipart-copy.md) |
| [`rgw_cors_rules_max_num`](api-limits.md#rgw_cors_rules_max_num) | `100` | Policy | Upstream default (`100`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_cross_domain_policy`](http-compat.md#rgw_cross_domain_policy) | `<allow-access-from domain="*" secure="false" />` | Performance | Baseline → adjust → validate under real workload | [HTTP compatibility](http-compat.md) |
| [`rgw_crypt_default_encryption_key`](encryption.md#rgw_crypt_default_encryption_key) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_addr`](encryption.md#rgw_crypt_kmip_addr) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_ca_path`](encryption.md#rgw_crypt_kmip_ca_path) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_client_cert`](encryption.md#rgw_crypt_kmip_client_cert) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_client_key`](encryption.md#rgw_crypt_kmip_client_key) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_kms_key_template`](encryption.md#rgw_crypt_kmip_kms_key_template) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_password`](encryption.md#rgw_crypt_kmip_password) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_s3_key_template`](encryption.md#rgw_crypt_kmip_s3_key_template) | `$keyid` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_kmip_username`](encryption.md#rgw_crypt_kmip_username) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_require_ssl`](encryption.md#rgw_crypt_require_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_backend`](encryption.md#rgw_crypt_s3_kms_backend) | `barbican` | Architecture | Match deployment topology; use upstream default | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_cache_enabled`](encryption.md#rgw_crypt_s3_kms_cache_enabled) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_cache_max_size`](encryption.md#rgw_crypt_s3_kms_cache_max_size) | `128` | Policy | Upstream default (`128`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_cache_negative_ttl`](encryption.md#rgw_crypt_s3_kms_cache_negative_ttl) | `120` | Performance | Size ≈ active working set; watch RGW memory | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_cache_positive_ttl`](encryption.md#rgw_crypt_s3_kms_cache_positive_ttl) | `60` | Performance | Size ≈ active working set; watch RGW memory | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_cache_transient_error_ttl`](encryption.md#rgw_crypt_s3_kms_cache_transient_error_ttl) | `10` | Performance | Size ≈ active working set; watch RGW memory | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_encryption_keys`](encryption.md#rgw_crypt_s3_kms_encryption_keys) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_s3_kms_testing_delay`](encryption.md#rgw_crypt_s3_kms_testing_delay) | `0` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_algorithm`](encryption.md#rgw_crypt_sse_algorithm) | `aes-256-cbc` | Architecture | Match deployment topology; use upstream default | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_backend`](encryption.md#rgw_crypt_sse_s3_backend) | `vault` | Architecture | Match deployment topology; use upstream default | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_key_template`](encryption.md#rgw_crypt_sse_s3_key_template) | `%bucket_id` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_addr`](encryption.md#rgw_crypt_sse_s3_vault_addr) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_auth`](encryption.md#rgw_crypt_sse_s3_vault_auth) | `token` | Architecture | Match deployment topology; use upstream default | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_namespace`](encryption.md#rgw_crypt_sse_s3_vault_namespace) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_prefix`](encryption.md#rgw_crypt_sse_s3_vault_prefix) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_secret_engine`](encryption.md#rgw_crypt_sse_s3_vault_secret_engine) | `transit` | Policy | Upstream default (`transit`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_ssl_cacert`](encryption.md#rgw_crypt_sse_s3_vault_ssl_cacert) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_ssl_clientcert`](encryption.md#rgw_crypt_sse_s3_vault_ssl_clientcert) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_ssl_clientkey`](encryption.md#rgw_crypt_sse_s3_vault_ssl_clientkey) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_token_file`](encryption.md#rgw_crypt_sse_s3_vault_token_file) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_sse_s3_vault_verify_ssl`](encryption.md#rgw_crypt_sse_s3_vault_verify_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_suppress_logs`](encryption.md#rgw_crypt_suppress_logs) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_addr`](encryption.md#rgw_crypt_vault_addr) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_auth`](encryption.md#rgw_crypt_vault_auth) | `token` | Architecture | Match deployment topology; use upstream default | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_namespace`](encryption.md#rgw_crypt_vault_namespace) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_prefix`](encryption.md#rgw_crypt_vault_prefix) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_secret_engine`](encryption.md#rgw_crypt_vault_secret_engine) | `transit` | Policy | Upstream default (`transit`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_ssl_cacert`](encryption.md#rgw_crypt_vault_ssl_cacert) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_ssl_clientcert`](encryption.md#rgw_crypt_vault_ssl_clientcert) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_ssl_clientkey`](encryption.md#rgw_crypt_vault_ssl_clientkey) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_token_file`](encryption.md#rgw_crypt_vault_token_file) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Encryption & KMS](encryption.md) |
| [`rgw_crypt_vault_verify_ssl`](encryption.md#rgw_crypt_vault_verify_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Encryption & KMS](encryption.md) |
| [`rgw_curl_buffersize`](http-curl.md#rgw_curl_buffersize) | `524288` | Performance | Baseline → adjust → validate under real workload | [HTTP / libcurl](http-curl.md) |
| [`rgw_curl_low_speed_limit`](http-curl.md#rgw_curl_low_speed_limit) | `1024` | Policy | Upstream default (`1024`) unless client/compliance requires change | [HTTP / libcurl](http-curl.md) |
| [`rgw_curl_low_speed_time`](http-curl.md#rgw_curl_low_speed_time) | `5_min` | Performance | Baseline → adjust → validate under real workload | [HTTP / libcurl](http-curl.md) |
| [`rgw_curl_tcp_keepalive`](http-curl.md#rgw_curl_tcp_keepalive) | `0` | Architecture | Match deployment topology; use upstream default | [HTTP / libcurl](http-curl.md) |
| [`rgw_curl_wait_timeout_ms`](http-curl.md#rgw_curl_wait_timeout_ms) | `1000` | Performance | Baseline → adjust → validate under real workload | [HTTP / libcurl](http-curl.md) |
| [`rgw_d3n_l1_datacache_persistent_path`](d4n-cache.md#rgw_d3n_l1_datacache_persistent_path) | `/tmp/rgw_datacache/` | Capacity | Dedicated fast disk with growth headroom | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_l1_datacache_size`](d4n-cache.md#rgw_d3n_l1_datacache_size) | `1_G` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_l1_evict_cache_on_start`](d4n-cache.md#rgw_d3n_l1_evict_cache_on_start) | `True` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_l1_eviction_policy`](d4n-cache.md#rgw_d3n_l1_eviction_policy) | `lru` | Architecture | Match deployment topology; use upstream default | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_l1_fadvise`](d4n-cache.md#rgw_d3n_l1_fadvise) | `4` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_l1_local_datacache_enabled`](d4n-cache.md#rgw_d3n_l1_local_datacache_enabled) | `False` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_libaio_aio_num`](d4n-cache.md#rgw_d3n_libaio_aio_num) | `64` | Policy | Upstream default (`64`) unless client/compliance requires change | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d3n_libaio_aio_threads`](d4n-cache.md#rgw_d3n_libaio_aio_threads) | `20` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_address`](d4n-cache.md#rgw_d4n_address) | `127.0.0.1:6379` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_backend_address`](d4n-cache.md#rgw_d4n_backend_address) | `127.0.0.1:6379` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_cache_cleaning_interval`](d4n-cache.md#rgw_d4n_cache_cleaning_interval) | `1000` | Performance | Size ≈ active working set; watch RGW memory | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_datacache_address`](d4n-cache.md#rgw_d4n_l1_datacache_address) | `127.0.0.1:6379` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_datacache_disk_reserve`](d4n-cache.md#rgw_d4n_l1_datacache_disk_reserve) | `1_G` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_datacache_persistent_path`](d4n-cache.md#rgw_d4n_l1_datacache_persistent_path) | `/tmp/rgw_d4n_datacache/` | Capacity | Dedicated fast disk with growth headroom | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_evict_cache_on_start`](d4n-cache.md#rgw_d4n_l1_evict_cache_on_start) | `True` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_fadvise`](d4n-cache.md#rgw_d4n_l1_fadvise) | `4` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_l1_write_open_flags`](d4n-cache.md#rgw_d4n_l1_write_open_flags) | `4096` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_libaio_aio_num`](d4n-cache.md#rgw_d4n_libaio_aio_num) | `64` | Policy | Upstream default (`64`) unless client/compliance requires change | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_libaio_aio_threads`](d4n-cache.md#rgw_d4n_libaio_aio_threads) | `20` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_local_rgw_address`](d4n-cache.md#rgw_d4n_local_rgw_address) | `127.0.0.1:8000` | Performance | Baseline → adjust → validate under real workload | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_d4n_localweight_processing_interval`](d4n-cache.md#rgw_d4n_localweight_processing_interval) | `3600` | Performance | Balance freshness vs background load | [D4N / D3N cache](d4n-cache.md) |
| [`rgw_data`](core-runtime.md#rgw_data) | `/var/lib/ceph/radosgw/$cluster-$id` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_data_log_changes_size`](multisite-sync.md#rgw_data_log_changes_size) | `1000` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_data_log_num_shards`](multisite-sync.md#rgw_data_log_num_shards) | `128` | Policy | Upstream default (`128`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_data_log_window`](multisite-sync.md#rgw_data_log_window) | `30` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_data_notify_interval_msec`](multisite-sync.md#rgw_data_notify_interval_msec) | `0` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_data_sync_poll_interval`](multisite-sync.md#rgw_data_sync_poll_interval) | `20` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_data_sync_spawn_window`](multisite-sync.md#rgw_data_sync_spawn_window) | `20` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_debug_inject_latency_bi_unlink`](debug-inject.md#rgw_debug_inject_latency_bi_unlink) | `0` | Dev | Keep `0` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_debug_inject_olh_cancel_modification_err`](debug-inject.md#rgw_debug_inject_olh_cancel_modification_err) | `False` | Dev | Keep `False` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_debug_inject_set_olh_err`](debug-inject.md#rgw_debug_inject_set_olh_err) | `0` | Dev | Keep `0` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_dedup_min_obj_size_for_dedup`](core-runtime.md#rgw_dedup_min_obj_size_for_dedup) | `64_K` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_dedup_split_obj_head`](core-runtime.md#rgw_dedup_split_obj_head) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_default_realm_info_oid`](multisite-zones.md#rgw_default_realm_info_oid) | `default.realm` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_default_region_info_oid`](multisite-zones.md#rgw_default_region_info_oid) | `default.region` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_default_zone_info_oid`](multisite-zones.md#rgw_default_zone_info_oid) | `default.zone` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_default_zonegroup_info_oid`](multisite-zones.md#rgw_default_zonegroup_info_oid) | `default.zonegroup` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_defer_to_bucket_acls`](http-compat.md#rgw_defer_to_bucket_acls) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [HTTP compatibility](http-compat.md) |
| [`rgw_delete_multi_obj_max_num`](limits-listing.md#rgw_delete_multi_obj_max_num) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_disable_s3select`](feature-toggles.md#rgw_disable_s3select) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_dmclock_admin_lim`](scheduler-dmclock.md#rgw_dmclock_admin_lim) | `0` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_admin_res`](scheduler-dmclock.md#rgw_dmclock_admin_res) | `100` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_admin_wgt`](scheduler-dmclock.md#rgw_dmclock_admin_wgt) | `100` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_auth_lim`](scheduler-dmclock.md#rgw_dmclock_auth_lim) | `0` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_auth_res`](scheduler-dmclock.md#rgw_dmclock_auth_res) | `200` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_auth_wgt`](scheduler-dmclock.md#rgw_dmclock_auth_wgt) | `100` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_data_lim`](scheduler-dmclock.md#rgw_dmclock_data_lim) | `0` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_data_res`](scheduler-dmclock.md#rgw_dmclock_data_res) | `500` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_data_wgt`](scheduler-dmclock.md#rgw_dmclock_data_wgt) | `500` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_metadata_lim`](scheduler-dmclock.md#rgw_dmclock_metadata_lim) | `0` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_metadata_res`](scheduler-dmclock.md#rgw_dmclock_metadata_res) | `500` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dmclock_metadata_wgt`](scheduler-dmclock.md#rgw_dmclock_metadata_wgt) | `500` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_dns_name`](frontends.md#rgw_dns_name) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Frontends & HTTP stack](frontends.md) |
| [`rgw_dns_s3website_name`](frontends.md#rgw_dns_s3website_name) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Frontends & HTTP stack](frontends.md) |
| [`rgw_dynamic_resharding`](resharding.md#rgw_dynamic_resharding) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Dynamic resharding](resharding.md) |
| [`rgw_dynamic_resharding_may_reduce`](resharding.md#rgw_dynamic_resharding_may_reduce) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Dynamic resharding](resharding.md) |
| [`rgw_dynamic_resharding_reduction_wait`](resharding.md#rgw_dynamic_resharding_reduction_wait) | `120` | Performance | Baseline → adjust → validate under real workload | [Dynamic resharding](resharding.md) |
| [`rgw_enable_apis`](feature-toggles.md#rgw_enable_apis) | `s3, s3control, s3website, swift, swift_auth, admin, sts, iam, notifications` | Performance | Baseline → adjust → validate under real workload | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_gc_threads`](feature-toggles.md#rgw_enable_gc_threads) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_jwks_url_verification`](feature-toggles.md#rgw_enable_jwks_url_verification) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_lc_threads`](feature-toggles.md#rgw_enable_lc_threads) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_mdsearch`](feature-toggles.md#rgw_enable_mdsearch) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_ops_log`](feature-toggles.md#rgw_enable_ops_log) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_quota_threads`](quotas.md#rgw_enable_quota_threads) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Quota sync & defaults](quotas.md) |
| [`rgw_enable_restore_threads`](feature-toggles.md#rgw_enable_restore_threads) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_static_website`](feature-toggles.md#rgw_enable_static_website) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enable_usage_log`](feature-toggles.md#rgw_enable_usage_log) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Feature toggles](feature-toggles.md) |
| [`rgw_enforce_swift_acls`](http-compat.md#rgw_enforce_swift_acls) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_exit_timeout_secs`](timeouts-intervals.md#rgw_exit_timeout_secs) | `2_min` | Performance | Baseline → adjust → validate under real workload | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_expose_bucket`](core-runtime.md#rgw_expose_bucket) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_extended_http_attrs`](http-compat.md#rgw_extended_http_attrs) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [HTTP compatibility](http-compat.md) |
| [`rgw_filter`](core-runtime.md#rgw_filter) | `none` | Architecture | Match deployment topology; use upstream default | [Core runtime](core-runtime.md) |
| [`rgw_frontend_defaults`](frontends.md#rgw_frontend_defaults) | `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` | Performance | Baseline → adjust → validate under real workload | [Frontends & HTTP stack](frontends.md) |
| [`rgw_frontends`](frontends.md#rgw_frontends) | `beast port=7480` | Performance | Baseline → adjust → validate under real workload | [Frontends & HTTP stack](frontends.md) |
| [`rgw_gc_max_concurrent_io`](garbage-collection.md#rgw_gc_max_concurrent_io) | `10` | Performance | Sweep up until OSD slow ops rise | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_max_objs`](garbage-collection.md#rgw_gc_max_objs) | `32` | Policy | Upstream default (`32`) unless client/compliance requires change | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_max_queue_size`](garbage-collection.md#rgw_gc_max_queue_size) | `131071_K` | Policy | Upstream default (`131071_K`) unless client/compliance requires change | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_max_trim_chunk`](garbage-collection.md#rgw_gc_max_trim_chunk) | `16` | Policy | Upstream default (`16`) unless client/compliance requires change | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_obj_min_wait`](garbage-collection.md#rgw_gc_obj_min_wait) | `2_hr` | Performance | Baseline → adjust → validate under real workload | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_processor_max_time`](garbage-collection.md#rgw_gc_processor_max_time) | `1_hr` | Policy | Upstream default (`1_hr`) unless client/compliance requires change | [Garbage collection](garbage-collection.md) |
| [`rgw_gc_processor_period`](garbage-collection.md#rgw_gc_processor_period) | `1_hr` | Performance | Baseline → adjust → validate under real workload | [Garbage collection](garbage-collection.md) |
| [`rgw_gcors_allow_headers`](admin-cors.md#rgw_gcors_allow_headers) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Admin CORS](admin-cors.md) |
| [`rgw_gcors_allow_methods`](admin-cors.md#rgw_gcors_allow_methods) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Admin CORS](admin-cors.md) |
| [`rgw_gcors_allow_origins`](admin-cors.md#rgw_gcors_allow_origins) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Admin CORS](admin-cors.md) |
| [`rgw_gcors_expose_headers`](admin-cors.md#rgw_gcors_expose_headers) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Admin CORS](admin-cors.md) |
| [`rgw_get_obj_max_req_size`](object-io.md#rgw_get_obj_max_req_size) | `4_M` | Policy | Upstream default (`4_M`) unless client/compliance requires change | [Object read/write windows](object-io.md) |
| [`rgw_get_obj_window_size`](object-io.md#rgw_get_obj_window_size) | `16_M` | Performance | Baseline → adjust → validate under real workload | [Object read/write windows](object-io.md) |
| [`rgw_graceful_stop`](core-runtime.md#rgw_graceful_stop) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_healthcheck_disabling_path`](core-runtime.md#rgw_healthcheck_disabling_path) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Core runtime](core-runtime.md) |
| [`rgw_http_notif_connection_timeout`](notifications.md#rgw_http_notif_connection_timeout) | `5` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_http_notif_max_inflight`](notifications.md#rgw_http_notif_max_inflight) | `8192` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_http_notif_message_timeout`](notifications.md#rgw_http_notif_message_timeout) | `10` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_ignore_get_invalid_range`](http-compat.md#rgw_ignore_get_invalid_range) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_init_timeout`](timeouts-intervals.md#rgw_init_timeout) | `5_min` | Performance | Baseline → adjust → validate under real workload | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_inject_delay_pattern`](debug-inject.md#rgw_inject_delay_pattern) | `(empty)` | Dev | Keep `(empty)` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_inject_delay_sec`](debug-inject.md#rgw_inject_delay_sec) | `0` | Dev | Keep `0` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_inject_notify_timeout_probability`](notifications.md#rgw_inject_notify_timeout_probability) | `0` | Dev | Keep `0` in production | [Bucket notifications](notifications.md) |
| [`rgw_json_config`](core-runtime.md#rgw_json_config) | `/var/lib/ceph/radosgw/config.json` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_kafka_connection_idle`](notifications.md#rgw_kafka_connection_idle) | `300` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_kafka_max_batch_size`](notifications.md#rgw_kafka_max_batch_size) | `0` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_kafka_message_timeout`](notifications.md#rgw_kafka_message_timeout) | `5000` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_kafka_sleep_timeout`](notifications.md#rgw_kafka_sleep_timeout) | `10` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_keystone_accepted_admin_roles`](keystone-sts.md#rgw_keystone_accepted_admin_roles) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_accepted_reader_roles`](keystone-sts.md#rgw_keystone_accepted_reader_roles) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_accepted_roles`](keystone-sts.md#rgw_keystone_accepted_roles) | `Member, admin` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_domain`](keystone-sts.md#rgw_keystone_admin_domain) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_password`](keystone-sts.md#rgw_keystone_admin_password) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_password_path`](keystone-sts.md#rgw_keystone_admin_password_path) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_project`](keystone-sts.md#rgw_keystone_admin_project) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_tenant`](keystone-sts.md#rgw_keystone_admin_tenant) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_admin_user`](keystone-sts.md#rgw_keystone_admin_user) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_barbican_domain`](keystone-sts.md#rgw_keystone_barbican_domain) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_barbican_password`](keystone-sts.md#rgw_keystone_barbican_password) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_barbican_project`](keystone-sts.md#rgw_keystone_barbican_project) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_barbican_tenant`](keystone-sts.md#rgw_keystone_barbican_tenant) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_barbican_user`](keystone-sts.md#rgw_keystone_barbican_user) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_expired_token_cache_expiration`](keystone-sts.md#rgw_keystone_expired_token_cache_expiration) | `3600` | Performance | Size ≈ active working set; watch RGW memory | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_implicit_tenants`](keystone-sts.md#rgw_keystone_implicit_tenants) | `false` | Architecture | Match deployment topology; use upstream default | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_scope_enabled`](keystone-sts.md#rgw_keystone_scope_enabled) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_scope_include_roles`](keystone-sts.md#rgw_keystone_scope_include_roles) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_scope_include_user`](keystone-sts.md#rgw_keystone_scope_include_user) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_service_token_accepted_roles`](keystone-sts.md#rgw_keystone_service_token_accepted_roles) | `admin` | Policy | Upstream default (`admin`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_service_token_enabled`](keystone-sts.md#rgw_keystone_service_token_enabled) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_token_cache_size`](keystone-sts.md#rgw_keystone_token_cache_size) | `10000` | Performance | Size ≈ active working set; watch RGW memory | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_token_cache_ttl`](keystone-sts.md#rgw_keystone_token_cache_ttl) | `300` | Performance | Size ≈ active working set; watch RGW memory | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_url`](keystone-sts.md#rgw_keystone_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Keystone & STS](keystone-sts.md) |
| [`rgw_keystone_verify_ssl`](keystone-sts.md#rgw_keystone_verify_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_lc_counters_batch_size`](lifecycle.md#rgw_lc_counters_batch_size) | `5000` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_counters_cache`](lifecycle.md#rgw_lc_counters_cache) | `False` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_counters_cache_size`](lifecycle.md#rgw_lc_counters_cache_size) | `10000` | Performance | Size ≈ active working set; watch RGW memory | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_debug_interval`](lifecycle.md#rgw_lc_debug_interval) | `-1` | Dev | Keep `-1` in production | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_list_cnt`](lifecycle.md#rgw_lc_list_cnt) | `1000` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_lock_max_time`](lifecycle.md#rgw_lc_lock_max_time) | `90` | Policy | Upstream default (`90`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_max_objs`](lifecycle.md#rgw_lc_max_objs) | `32` | Policy | Upstream default (`32`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_max_rules`](lifecycle.md#rgw_lc_max_rules) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_max_worker`](lifecycle.md#rgw_lc_max_worker) | `3` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_max_wp_worker`](lifecycle.md#rgw_lc_max_wp_worker) | `128` | Policy | Upstream default (`128`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_ordered_list_threshold`](lifecycle.md#rgw_lc_ordered_list_threshold) | `500` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_lc_thread_delay`](lifecycle.md#rgw_lc_thread_delay) | `0` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_ldap_binddn`](ldap.md#rgw_ldap_binddn) | `uid=admin,cn=users,dc=example,dc=com` | Policy | Upstream default (`uid=admin,cn=users,dc=example,dc=com`) unless client/compliance requires change | [LDAP](ldap.md) |
| [`rgw_ldap_dnattr`](ldap.md#rgw_ldap_dnattr) | `uid` | Performance | Baseline → adjust → validate under real workload | [LDAP](ldap.md) |
| [`rgw_ldap_searchdn`](ldap.md#rgw_ldap_searchdn) | `cn=users,cn=accounts,dc=example,dc=com` | Performance | Baseline → adjust → validate under real workload | [LDAP](ldap.md) |
| [`rgw_ldap_searchfilter`](ldap.md#rgw_ldap_searchfilter) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [LDAP](ldap.md) |
| [`rgw_ldap_secret`](ldap.md#rgw_ldap_secret) | `/etc/openldap/secret` | Policy | Upstream default (`/etc/openldap/secret`) unless client/compliance requires change | [LDAP](ldap.md) |
| [`rgw_ldap_uri`](ldap.md#rgw_ldap_uri) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [LDAP](ldap.md) |
| [`rgw_lfuda_sync_frequency`](multisite-sync.md#rgw_lfuda_sync_frequency) | `60` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_lifecycle_work_time`](lifecycle.md#rgw_lifecycle_work_time) | `00:00-06:00` | Performance | Baseline → adjust → validate under real workload | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_list_bucket_min_readahead`](performance-tuning.md#rgw_list_bucket_min_readahead) | `1000` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_list_buckets_max_chunk`](limits-listing.md#rgw_list_buckets_max_chunk) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_log_http_headers`](logging.md#rgw_log_http_headers) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Access & object logging](logging.md) |
| [`rgw_log_nonexistent_bucket`](logging.md#rgw_log_nonexistent_bucket) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Access & object logging](logging.md) |
| [`rgw_log_object_name`](logging.md#rgw_log_object_name) | `%Y-%m-%d-%H-%i-%n` | Performance | Baseline → adjust → validate under real workload | [Access & object logging](logging.md) |
| [`rgw_log_object_name_utc`](logging.md#rgw_log_object_name_utc) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Access & object logging](logging.md) |
| [`rgw_lua_enable`](lua.md#rgw_lua_enable) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Lua scripting](lua.md) |
| [`rgw_lua_max_memory_per_state`](lua.md#rgw_lua_max_memory_per_state) | `128000` | Policy | Upstream default (`128000`) unless client/compliance requires change | [Lua scripting](lua.md) |
| [`rgw_lua_max_runtime_per_state`](lua.md#rgw_lua_max_runtime_per_state) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Lua scripting](lua.md) |
| [`rgw_luarocks_location`](lua.md#rgw_luarocks_location) | `/tmp/rgw_luarocks/$name` | Performance | Baseline → adjust → validate under real workload | [Lua scripting](lua.md) |
| [`rgw_max_attr_name_len`](limits-listing.md#rgw_max_attr_name_len) | `0` | Policy | Upstream default (`0`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_attr_size`](limits-listing.md#rgw_max_attr_size) | `0` | Policy | Upstream default (`0`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_attrs_num_in_req`](limits-listing.md#rgw_max_attrs_num_in_req) | `0` | Policy | Upstream default (`0`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_chunk_size`](limits-listing.md#rgw_max_chunk_size) | `4_M` | Performance | Baseline → adjust → validate under real workload | [Listing limits](limits-listing.md) |
| [`rgw_max_concurrent_requests`](performance-tuning.md#rgw_max_concurrent_requests) | `1024` | Performance | Sweep up until OSD slow ops rise | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_max_control_aio`](limits-listing.md#rgw_max_control_aio) | `8` | Policy | Upstream default (`8`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_copy_obj_concurrent_io`](performance-tuning.md#rgw_max_copy_obj_concurrent_io) | `10` | Performance | Sweep up until OSD slow ops rise | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_max_dynamic_shards`](limits-listing.md#rgw_max_dynamic_shards) | `1999` | Policy | Upstream default (`1999`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_listing_results`](limits-listing.md#rgw_max_listing_results) | `5000` | Policy | Upstream default (`5000`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_notify_retries`](notifications.md#rgw_max_notify_retries) | `10` | Policy | Upstream default (`10`) unless client/compliance requires change | [Bucket notifications](notifications.md) |
| [`rgw_max_objs_per_shard`](performance-tuning.md#rgw_max_objs_per_shard) | `100000` | Policy | Upstream default (`100000`) unless client/compliance requires change | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_max_put_param_size`](limits-listing.md#rgw_max_put_param_size) | `1_M` | Policy | Upstream default (`1_M`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_put_size`](limits-listing.md#rgw_max_put_size) | `5_G` | Policy | Upstream default (`5_G`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_max_slo_entries`](limits-listing.md#rgw_max_slo_entries) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Listing limits](limits-listing.md) |
| [`rgw_md_log_max_shards`](multisite-sync.md#rgw_md_log_max_shards) | `64` | Policy | Upstream default (`64`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_md_notify_interval_msec`](multisite-sync.md#rgw_md_notify_interval_msec) | `200` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_meta_sync_poll_interval`](multisite-sync.md#rgw_meta_sync_poll_interval) | `20` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_meta_sync_spawn_window`](multisite-sync.md#rgw_meta_sync_spawn_window) | `20` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_mime_types_file`](core-runtime.md#rgw_mime_types_file) | `/etc/mime.types` | Capacity | Dedicated fast disk with growth headroom | [Core runtime](core-runtime.md) |
| [`rgw_mp_lock_inject_delay`](debug-inject.md#rgw_mp_lock_inject_delay) | `0` | Dev | Keep `0` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_mp_lock_inject_renewal_error`](debug-inject.md#rgw_mp_lock_inject_renewal_error) | `0` | Dev | Keep `0` in production | [Debug & fault injection](debug-inject.md) |
| [`rgw_mp_lock_max_time`](lifecycle.md#rgw_mp_lock_max_time) | `10_min` | Policy | Upstream default (`10_min`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_multi_obj_del_max_aio`](performance-tuning.md#rgw_multi_obj_del_max_aio) | `16` | Performance | Sweep up until OSD slow ops rise | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_multipart_min_part_size`](multipart-copy.md#rgw_multipart_min_part_size) | `5_M` | Performance | Baseline → adjust → validate under real workload | [Multipart & copy](multipart-copy.md) |
| [`rgw_multipart_part_upload_limit`](multipart-copy.md#rgw_multipart_part_upload_limit) | `10000` | Policy | Upstream default (`10000`) unless client/compliance requires change | [Multipart & copy](multipart-copy.md) |
| [`rgw_nfs_fhcache_partitions`](nfs.md#rgw_nfs_fhcache_partitions) | `3` | Performance | Size ≈ active working set; watch RGW memory | [NFS gateway](nfs.md) |
| [`rgw_nfs_fhcache_size`](nfs.md#rgw_nfs_fhcache_size) | `2017` | Performance | Size ≈ active working set; watch RGW memory | [NFS gateway](nfs.md) |
| [`rgw_nfs_frontends`](nfs.md#rgw_nfs_frontends) | `rgw-nfs` | Performance | Baseline → adjust → validate under real workload | [NFS gateway](nfs.md) |
| [`rgw_nfs_lru_lane_hiwat`](nfs.md#rgw_nfs_lru_lane_hiwat) | `911` | Performance | Baseline → adjust → validate under real workload | [NFS gateway](nfs.md) |
| [`rgw_nfs_lru_lanes`](nfs.md#rgw_nfs_lru_lanes) | `5` | Performance | Baseline → adjust → validate under real workload | [NFS gateway](nfs.md) |
| [`rgw_nfs_max_gc`](nfs.md#rgw_nfs_max_gc) | `5_min` | Policy | Upstream default (`5_min`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_namespace_expire_secs`](nfs.md#rgw_nfs_namespace_expire_secs) | `5_min` | Performance | Baseline → adjust → validate under real workload | [NFS gateway](nfs.md) |
| [`rgw_nfs_run_gc_threads`](nfs.md#rgw_nfs_run_gc_threads) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_run_lc_threads`](nfs.md#rgw_nfs_run_lc_threads) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_run_quota_threads`](nfs.md#rgw_nfs_run_quota_threads) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_run_restore_threads`](nfs.md#rgw_nfs_run_restore_threads) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_run_sync_thread`](nfs.md#rgw_nfs_run_sync_thread) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_s3_fast_attrs`](nfs.md#rgw_nfs_s3_fast_attrs) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [NFS gateway](nfs.md) |
| [`rgw_nfs_write_completion_interval_s`](nfs.md#rgw_nfs_write_completion_interval_s) | `10` | Performance | Balance freshness vs background load | [NFS gateway](nfs.md) |
| [`rgw_num_async_rados_threads`](performance-tuning.md#rgw_num_async_rados_threads) | `32` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_num_control_oids`](performance-tuning.md#rgw_num_control_oids) | `8` | Policy | Upstream default (`8`) unless client/compliance requires change | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_numa_node`](core-runtime.md#rgw_numa_node) | `-1` | Policy | Upstream default (`-1`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_obj_stripe_size`](performance-tuning.md#rgw_obj_stripe_size) | `4_M` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_obj_tombstone_cache_size`](caching.md#rgw_obj_tombstone_cache_size) | `1000` | Performance | Size ≈ active working set; watch RGW memory | [Metadata & object caches](caching.md) |
| [`rgw_objexp_chunk_size`](object-expiry.md#rgw_objexp_chunk_size) | `100` | Performance | Baseline → adjust → validate under real workload | [Object expiry hints](object-expiry.md) |
| [`rgw_objexp_gc_interval`](timeouts-intervals.md#rgw_objexp_gc_interval) | `600` | Performance | Balance freshness vs background load | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_objexp_hints_num_shards`](object-expiry.md#rgw_objexp_hints_num_shards) | `127` | Policy | Upstream default (`127`) unless client/compliance requires change | [Object expiry hints](object-expiry.md) |
| [`rgw_olh_pending_timeout_sec`](timeouts-intervals.md#rgw_olh_pending_timeout_sec) | `1_hr` | Performance | Baseline → adjust → validate under real workload | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_op_thread_suicide_timeout`](performance-tuning.md#rgw_op_thread_suicide_timeout) | `0` | Dev | Keep `0` in production | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_op_thread_timeout`](performance-tuning.md#rgw_op_thread_timeout) | `10_min` | Dev | Keep `10_min` in production | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_op_tracing`](core-runtime.md#rgw_op_tracing) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_opa_token`](opa-authz.md#rgw_opa_token) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [OPA authorization](opa-authz.md) |
| [`rgw_opa_url`](opa-authz.md#rgw_opa_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [OPA authorization](opa-authz.md) |
| [`rgw_opa_verify_ssl`](opa-authz.md#rgw_opa_verify_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [OPA authorization](opa-authz.md) |
| [`rgw_ops_log_data_backlog`](ops-logging.md#rgw_ops_log_data_backlog) | `5_M` | Performance | Baseline → adjust → validate under real workload | [Ops logging](ops-logging.md) |
| [`rgw_ops_log_file_path`](ops-logging.md#rgw_ops_log_file_path) | `/var/log/ceph/ops-log-$cluster-$name.log` | Capacity | Dedicated fast disk with growth headroom | [Ops logging](ops-logging.md) |
| [`rgw_ops_log_rados`](ops-logging.md#rgw_ops_log_rados) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Ops logging](ops-logging.md) |
| [`rgw_ops_log_socket_path`](ops-logging.md#rgw_ops_log_socket_path) | `(empty)` | Capacity | Dedicated fast disk with growth headroom | [Ops logging](ops-logging.md) |
| [`rgw_override_bucket_index_max_shards`](index-sharding.md#rgw_override_bucket_index_max_shards) | `0` | Policy | Upstream default (`0`) unless client/compliance requires change | [Bucket index & sharding](index-sharding.md) |
| [`rgw_parquet_buffer_size`](core-runtime.md#rgw_parquet_buffer_size) | `16_M` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_pending_bucket_index_op_expiration`](index-sharding.md#rgw_pending_bucket_index_op_expiration) | `120` | Performance | Baseline → adjust → validate under real workload | [Bucket index & sharding](index-sharding.md) |
| [`rgw_period_latest_epoch_info_oid`](multisite-zones.md#rgw_period_latest_epoch_info_oid) | `.latest_epoch` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_period_push_interval`](multisite-zones.md#rgw_period_push_interval) | `2` | Performance | Balance freshness vs background load | [Zones, realm & region](multisite-zones.md) |
| [`rgw_period_push_interval_max`](multisite-zones.md#rgw_period_push_interval_max) | `30` | Performance | Balance freshness vs background load | [Zones, realm & region](multisite-zones.md) |
| [`rgw_period_root_pool`](multisite-zones.md#rgw_period_root_pool) | `.rgw.root` | Performance | Baseline → adjust → validate under real workload | [Zones, realm & region](multisite-zones.md) |
| [`rgw_policy_reject_invalid_principals`](api-limits.md#rgw_policy_reject_invalid_principals) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_posix_base_path`](posix-experimental.md#rgw_posix_base_path) | `/tmp/rgw_posix_driver` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_cache_lanes`](posix-experimental.md#rgw_posix_cache_lanes) | `3` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_cache_lmdb_count`](posix-experimental.md#rgw_posix_cache_lmdb_count) | `3` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_cache_max_buckets`](posix-experimental.md#rgw_posix_cache_max_buckets) | `100` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_cache_partitions`](posix-experimental.md#rgw_posix_cache_partitions) | `3` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_database_root`](posix-experimental.md#rgw_posix_database_root) | `/var/lib/ceph/radosgw` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_posix_userdb_dir`](posix-experimental.md#rgw_posix_userdb_dir) | `/var/lib/ceph/radosgw` | Architecture | Match deployment topology; use upstream default | [POSIX backend](posix-experimental.md) |
| [`rgw_print_continue`](http-compat.md#rgw_print_continue) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_print_prohibited_content_length`](http-compat.md#rgw_print_prohibited_content_length) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_put_obj_max_window_size`](object-io.md#rgw_put_obj_max_window_size) | `64_M` | Performance | Baseline → adjust → validate under real workload | [Object read/write windows](object-io.md) |
| [`rgw_put_obj_min_window_size`](object-io.md#rgw_put_obj_min_window_size) | `16_M` | Performance | Baseline → adjust → validate under real workload | [Object read/write windows](object-io.md) |
| [`rgw_rados_pool_autoscale_bias`](core-runtime.md#rgw_rados_pool_autoscale_bias) | `4` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_rados_pool_recovery_priority`](core-runtime.md#rgw_rados_pool_recovery_priority) | `5` | Performance | Baseline → adjust → validate under real workload | [Core runtime](core-runtime.md) |
| [`rgw_rados_tracing`](core-runtime.md#rgw_rados_tracing) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Core runtime](core-runtime.md) |
| [`rgw_ratelimit_interval`](timeouts-intervals.md#rgw_ratelimit_interval) | `60` | Performance | Balance freshness vs background load | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_read_through_timeout_ms`](timeouts-intervals.md#rgw_read_through_timeout_ms) | `10000` | Performance | Baseline → adjust → validate under real workload | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_realm`](multisite-zones.md#rgw_realm) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_realm_id`](multisite-zones.md#rgw_realm_id) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_realm_root_pool`](multisite-zones.md#rgw_realm_root_pool) | `.rgw.root` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_redis_connection_pool_size`](performance-tuning.md#rgw_redis_connection_pool_size) | `512` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_region`](multisite-zones.md#rgw_region) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_region_root_pool`](multisite-zones.md#rgw_region_root_pool) | `.rgw.root` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_relaxed_region_enforcement`](http-compat.md#rgw_relaxed_region_enforcement) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_relaxed_s3_bucket_names`](http-compat.md#rgw_relaxed_s3_bucket_names) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_relaxed_topic_names`](http-compat.md#rgw_relaxed_topic_names) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_remote_addr_param`](http-compat.md#rgw_remote_addr_param) | `REMOTE_ADDR` | Performance | Baseline → adjust → validate under real workload | [HTTP compatibility](http-compat.md) |
| [`rgw_request_uri`](http-compat.md#rgw_request_uri) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [HTTP compatibility](http-compat.md) |
| [`rgw_reshard_batch_size`](resharding.md#rgw_reshard_batch_size) | `64` | Performance | Baseline → adjust → validate under real workload | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_bucket_lock_duration`](resharding.md#rgw_reshard_bucket_lock_duration) | `360` | Performance | Baseline → adjust → validate under real workload | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_debug_interval`](resharding.md#rgw_reshard_debug_interval) | `-1` | Dev | Keep `-1` in production | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_max_aio`](resharding.md#rgw_reshard_max_aio) | `128` | Performance | Sweep up until OSD slow ops rise | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_num_logs`](resharding.md#rgw_reshard_num_logs) | `16` | Policy | Upstream default (`16`) unless client/compliance requires change | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_progress_judge_interval`](resharding.md#rgw_reshard_progress_judge_interval) | `120` | Performance | Balance freshness vs background load | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_progress_judge_ratio`](resharding.md#rgw_reshard_progress_judge_ratio) | `0.5` | Performance | Baseline → adjust → validate under real workload | [Dynamic resharding](resharding.md) |
| [`rgw_reshard_thread_interval`](resharding.md#rgw_reshard_thread_interval) | `600` | Performance | Balance freshness vs background load | [Dynamic resharding](resharding.md) |
| [`rgw_reshardlog_threshold`](resharding.md#rgw_reshardlog_threshold) | `30000` | Performance | Baseline → adjust → validate under real workload | [Dynamic resharding](resharding.md) |
| [`rgw_resolve_cname`](http-compat.md#rgw_resolve_cname) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_rest_conn_connect_to_resolved_ips`](rest-connections.md#rgw_rest_conn_connect_to_resolved_ips) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [REST connections](rest-connections.md) |
| [`rgw_rest_conn_ip_fail_timeout_secs`](rest-connections.md#rgw_rest_conn_ip_fail_timeout_secs) | `2` | Performance | Baseline → adjust → validate under real workload | [REST connections](rest-connections.md) |
| [`rgw_rest_getusage_op_compat`](rest-connections.md#rgw_rest_getusage_op_compat) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [REST connections](rest-connections.md) |
| [`rgw_restore_debug_interval`](timeouts-intervals.md#rgw_restore_debug_interval) | `-1` | Dev | Keep `-1` in production | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_restore_lock_max_time`](lifecycle.md#rgw_restore_lock_max_time) | `90` | Policy | Upstream default (`90`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgw_restore_max_objs`](performance-tuning.md#rgw_restore_max_objs) | `32` | Policy | Upstream default (`32`) unless client/compliance requires change | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_restore_processor_period`](performance-tuning.md#rgw_restore_processor_period) | `15_min` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_run_sync_thread`](multisite-sync.md#rgw_run_sync_thread) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_s3_auth_disable_signature_url`](s3-api.md#rgw_s3_auth_disable_signature_url) | `False` | Connectivity | Nearest stable endpoint from every RGW node | [S3 API & auth](s3-api.md) |
| [`rgw_s3_auth_order`](s3-api.md#rgw_s3_auth_order) | `sts, external, local` | Performance | Baseline → adjust → validate under real workload | [S3 API & auth](s3-api.md) |
| [`rgw_s3_auth_use_keystone`](s3-api.md#rgw_s3_auth_use_keystone) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [S3 API & auth](s3-api.md) |
| [`rgw_s3_auth_use_ldap`](s3-api.md#rgw_s3_auth_use_ldap) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [S3 API & auth](s3-api.md) |
| [`rgw_s3_auth_use_rados`](s3-api.md#rgw_s3_auth_use_rados) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [S3 API & auth](s3-api.md) |
| [`rgw_s3_auth_use_sts`](s3-api.md#rgw_s3_auth_use_sts) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [S3 API & auth](s3-api.md) |
| [`rgw_s3_client_max_sig_ver`](s3-api.md#rgw_s3_client_max_sig_ver) | `-1` | Policy | Upstream default (`-1`) unless client/compliance requires change | [S3 API & auth](s3-api.md) |
| [`rgw_s3_success_create_obj_status`](s3-api.md#rgw_s3_success_create_obj_status) | `0` | Performance | Baseline → adjust → validate under real workload | [S3 API & auth](s3-api.md) |
| [`rgw_safe_max_objects_per_shard`](index-sharding.md#rgw_safe_max_objects_per_shard) | `102400` | Policy | Upstream default (`102400`) unless client/compliance requires change | [Bucket index & sharding](index-sharding.md) |
| [`rgw_scheduler_type`](scheduler-dmclock.md#rgw_scheduler_type) | `throttler` | Performance | Baseline → adjust → validate under real workload | [Scheduler & dmclock](scheduler-dmclock.md) |
| [`rgw_script_uri`](core-runtime.md#rgw_script_uri) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Core runtime](core-runtime.md) |
| [`rgw_service_provider_name`](http-compat.md#rgw_service_provider_name) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [HTTP compatibility](http-compat.md) |
| [`rgw_shard_warning_threshold`](index-sharding.md#rgw_shard_warning_threshold) | `90` | Performance | Baseline → adjust → validate under real workload | [Bucket index & sharding](index-sharding.md) |
| [`rgw_sts_client_id`](keystone-sts.md#rgw_sts_client_id) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_client_secret`](keystone-sts.md#rgw_sts_client_secret) | `(empty)` | Policy | Upstream default (`(empty)`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_entry`](keystone-sts.md#rgw_sts_entry) | `sts` | Policy | Upstream default (`sts`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_key`](keystone-sts.md#rgw_sts_key) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_max_session_duration`](keystone-sts.md#rgw_sts_max_session_duration) | `43200` | Policy | Upstream default (`43200`) unless client/compliance requires change | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_min_session_duration`](keystone-sts.md#rgw_sts_min_session_duration) | `900` | Performance | Baseline → adjust → validate under real workload | [Keystone & STS](keystone-sts.md) |
| [`rgw_sts_token_introspection_url`](keystone-sts.md#rgw_sts_token_introspection_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Keystone & STS](keystone-sts.md) |
| [`rgw_swift_account_in_url`](swift.md#rgw_swift_account_in_url) | `False` | Connectivity | Nearest stable endpoint from every RGW node | [Swift API](swift.md) |
| [`rgw_swift_auth_entry`](swift.md#rgw_swift_auth_entry) | `auth` | Policy | Upstream default (`auth`) unless client/compliance requires change | [Swift API](swift.md) |
| [`rgw_swift_auth_url`](swift.md#rgw_swift_auth_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Swift API](swift.md) |
| [`rgw_swift_custom_header`](swift.md#rgw_swift_custom_header) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Swift API](swift.md) |
| [`rgw_swift_enforce_content_length`](swift.md#rgw_swift_enforce_content_length) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Swift API](swift.md) |
| [`rgw_swift_need_stats`](swift.md#rgw_swift_need_stats) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Swift API](swift.md) |
| [`rgw_swift_tenant_name`](swift.md#rgw_swift_tenant_name) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [Swift API](swift.md) |
| [`rgw_swift_token_expiration`](swift.md#rgw_swift_token_expiration) | `1_day` | Performance | Baseline → adjust → validate under real workload | [Swift API](swift.md) |
| [`rgw_swift_url`](swift.md#rgw_swift_url) | `(empty)` | Connectivity | Nearest stable endpoint from every RGW node | [Swift API](swift.md) |
| [`rgw_swift_url_prefix`](swift.md#rgw_swift_url_prefix) | `swift` | Performance | Baseline → adjust → validate under real workload | [Swift API](swift.md) |
| [`rgw_swift_versioning_enabled`](swift.md#rgw_swift_versioning_enabled) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Swift API](swift.md) |
| [`rgw_sync_data_full_inject_err_probability`](multisite-sync.md#rgw_sync_data_full_inject_err_probability) | `0` | Dev | Keep `0` in production | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_data_inject_err_probability`](multisite-sync.md#rgw_sync_data_inject_err_probability) | `0` | Dev | Keep `0` in production | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_lease_period`](multisite-sync.md#rgw_sync_lease_period) | `2_min` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_log_trim_concurrent_buckets`](multisite-sync.md#rgw_sync_log_trim_concurrent_buckets) | `4` | Performance | Sweep up until OSD slow ops rise | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_log_trim_interval`](multisite-sync.md#rgw_sync_log_trim_interval) | `20_min` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_log_trim_max_buckets`](multisite-sync.md#rgw_sync_log_trim_max_buckets) | `16` | Policy | Upstream default (`16`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_log_trim_min_cold_buckets`](multisite-sync.md#rgw_sync_log_trim_min_cold_buckets) | `4` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_meta_inject_err_probability`](multisite-sync.md#rgw_sync_meta_inject_err_probability) | `0` | Dev | Keep `0` in production | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_obj_etag_verify`](multisite-sync.md#rgw_sync_obj_etag_verify) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_trace_history_size`](multisite-sync.md#rgw_sync_trace_history_size) | `4_K` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_trace_per_node_log_size`](multisite-sync.md#rgw_sync_trace_per_node_log_size) | `32` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_sync_trace_servicemap_update_interval`](multisite-sync.md#rgw_sync_trace_servicemap_update_interval) | `10` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_thread_pool_size`](performance-tuning.md#rgw_thread_pool_size) | `512` | Performance | Baseline → adjust → validate under real workload | [Concurrency & RADOS I/O](performance-tuning.md) |
| [`rgw_topic_persistency_max_retries`](notifications.md#rgw_topic_persistency_max_retries) | `0` | Policy | Upstream default (`0`) unless client/compliance requires change | [Bucket notifications](notifications.md) |
| [`rgw_topic_persistency_sleep_duration`](notifications.md#rgw_topic_persistency_sleep_duration) | `0` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_topic_persistency_time_to_live`](notifications.md#rgw_topic_persistency_time_to_live) | `0` | Performance | Baseline → adjust → validate under real workload | [Bucket notifications](notifications.md) |
| [`rgw_topic_require_publish_policy`](api-limits.md#rgw_topic_require_publish_policy) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_torrent_comment`](torrent.md#rgw_torrent_comment) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_torrent_createby`](torrent.md#rgw_torrent_createby) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_torrent_encoding`](torrent.md#rgw_torrent_encoding) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_torrent_flag`](torrent.md#rgw_torrent_flag) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [BitTorrent](torrent.md) |
| [`rgw_torrent_max_size`](torrent.md#rgw_torrent_max_size) | `5_G` | Policy | Upstream default (`5_G`) unless client/compliance requires change | [BitTorrent](torrent.md) |
| [`rgw_torrent_origin`](torrent.md#rgw_torrent_origin) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_torrent_sha_unit`](torrent.md#rgw_torrent_sha_unit) | `512_K` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_torrent_tracker`](torrent.md#rgw_torrent_tracker) | `(empty)` | Performance | Baseline → adjust → validate under real workload | [BitTorrent](torrent.md) |
| [`rgw_trust_forwarded_https`](http-compat.md#rgw_trust_forwarded_https) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_usage_log_flush_threshold`](usage-logging.md#rgw_usage_log_flush_threshold) | `1024` | Performance | Baseline → adjust → validate under real workload | [Usage logging](usage-logging.md) |
| [`rgw_usage_log_key_transition`](usage-logging.md#rgw_usage_log_key_transition) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Usage logging](usage-logging.md) |
| [`rgw_usage_log_tick_interval`](timeouts-intervals.md#rgw_usage_log_tick_interval) | `30` | Performance | Balance freshness vs background load | [Timeouts & intervals](timeouts-intervals.md) |
| [`rgw_usage_max_shards`](usage-logging.md#rgw_usage_max_shards) | `32` | Policy | Upstream default (`32`) unless client/compliance requires change | [Usage logging](usage-logging.md) |
| [`rgw_usage_max_user_shards`](usage-logging.md#rgw_usage_max_user_shards) | `1` | Policy | Upstream default (`1`) unless client/compliance requires change | [Usage logging](usage-logging.md) |
| [`rgw_use_opa_authz`](opa-authz.md#rgw_use_opa_authz) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [OPA authorization](opa-authz.md) |
| [`rgw_user_counters_cache`](users-quotas.md#rgw_user_counters_cache) | `False` | Performance | Baseline → adjust → validate under real workload | [Users & per-user settings](users-quotas.md) |
| [`rgw_user_counters_cache_size`](users-quotas.md#rgw_user_counters_cache_size) | `10000` | Performance | Size ≈ active working set; watch RGW memory | [Users & per-user settings](users-quotas.md) |
| [`rgw_user_default_quota_max_objects`](quotas.md#rgw_user_default_quota_max_objects) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Quota sync & defaults](quotas.md) |
| [`rgw_user_default_quota_max_size`](quotas.md#rgw_user_default_quota_max_size) | `-1` | Policy | Cluster capacity ÷ tenant plan; verify with test users | [Quota sync & defaults](quotas.md) |
| [`rgw_user_max_buckets`](users-quotas.md#rgw_user_max_buckets) | `1000` | Policy | Upstream default (`1000`) unless client/compliance requires change | [Users & per-user settings](users-quotas.md) |
| [`rgw_user_policies_max_num`](users-quotas.md#rgw_user_policies_max_num) | `100` | Policy | Upstream default (`100`) unless client/compliance requires change | [Users & per-user settings](users-quotas.md) |
| [`rgw_user_quota_bucket_sync_interval`](multisite-sync.md#rgw_user_quota_bucket_sync_interval) | `3_min` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_user_quota_sync_idle_users`](multisite-sync.md#rgw_user_quota_sync_idle_users) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Replication & sync](multisite-sync.md) |
| [`rgw_user_quota_sync_interval`](multisite-sync.md#rgw_user_quota_sync_interval) | `1_day` | Performance | Balance freshness vs background load | [Replication & sync](multisite-sync.md) |
| [`rgw_user_quota_sync_wait_time`](multisite-sync.md#rgw_user_quota_sync_wait_time) | `1_day` | Performance | Baseline → adjust → validate under real workload | [Replication & sync](multisite-sync.md) |
| [`rgw_user_unique_email`](users-quotas.md#rgw_user_unique_email) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Users & per-user settings](users-quotas.md) |
| [`rgw_verify_ssl`](http-compat.md#rgw_verify_ssl) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [HTTP compatibility](http-compat.md) |
| [`rgw_website_routing_rules_max_num`](api-limits.md#rgw_website_routing_rules_max_num) | `50` | Policy | Upstream default (`50`) unless client/compliance requires change | [API limits & policies](api-limits.md) |
| [`rgw_zone`](multisite-zones.md#rgw_zone) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_zone_id`](multisite-zones.md#rgw_zone_id) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_zone_root_pool`](multisite-zones.md#rgw_zone_root_pool) | `.rgw.root` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_zonegroup`](multisite-zones.md#rgw_zonegroup) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_zonegroup_id`](multisite-zones.md#rgw_zonegroup_id) | `(empty)` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgw_zonegroup_root_pool`](multisite-zones.md#rgw_zonegroup_root_pool) | `.rgw.root` | Architecture | Match deployment topology; use upstream default | [Zones, realm & region](multisite-zones.md) |
| [`rgwlc_auto_session_clear`](lifecycle.md#rgwlc_auto_session_clear) | `True` | Policy | Upstream default (`True`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |
| [`rgwlc_skip_bucket_step`](lifecycle.md#rgwlc_skip_bucket_step) | `False` | Policy | Upstream default (`False`) unless client/compliance requires change | [Lifecycle (LC)](lifecycle.md) |

[← RGW config overview](OVERVIEW.md)
