# RGW optimized example

Settings for a **production object gateway** cluster (single or multisite).

## Frontends & APIs

```ini
[client.rgw]
rgw frontends = beast ssl_port=443 ssl_certificate=/etc/ceph/ssl/rgw.pem ssl_private_key=/etc/ceph/ssl/rgw.key
rgw enable_apis = s3
rgw dns name = s3.example.com
```

Restrict APIs to what you expose publicly.

## Performance & caching

```ini
[client.rgw]
rgw_cache_enabled = true
rgw_cache_lru_size = 10000
rgw_thread_pool_size = 512
rgw_num_rados_handles = 256
```

Tune based on workload; monitor `l_rgw_qlen` and latency.

## Rate limiting (optional)

```ini
[client.rgw]
rgw_enable_rate_limit = true
rgw_max_put_size = 5368709120
```

See [Rate limit architecture](../../../arch/rgw/architecture/rate-limit-architecture.md).

## Logging & metrics

```ini
[client.rgw]
rgw_enable_ops_log = true
rgw_ops_log_rados = true
```

Enable mgr prometheus module for `rgw_perf_counters`.

## Security notes

| Setting | Production impact |
|---------|-------------------|
| `rgw enable apis` | Exposing admin/swift increases attack surface |
| TLS termination | Prefer real certs or LB termination |
| `rgw crypt` options | Review compliance requirements |

Deep dives: [RGW config guide](../../guides/rgw-config/OVERVIEW.md) · [RGW admin role](../../guides/roles/rgw-admin.md).

[← Examples overview](OVERVIEW.md)
