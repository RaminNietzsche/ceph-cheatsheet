# Lab / development example

Single-host or 3-node lab. **Not for production data.**

## Goals

- Minimal resources, fast iteration
- Accept single points of failure

## Key settings

```ini
[global]
# Lab only — never use in production
osd_pool_default_size = 2
osd_pool_default_min_size = 1
mon_allow_pool_size_one = true

osd_pool_default_pg_autoscale_mode = on

# Lower memory if constrained
osd_memory_target = 4294967296   # 4 GiB

# Relaxed scrub (less disk churn)
osd_scrub_begin_hour = 0
osd_scrub_end_hour = 24
```

## cephadm bootstrap (single host)

```bash
cephadm bootstrap --mon-ip <ip> --single-host-defaults
ceph orch apply mon --placement="1"
ceph orch apply mgr --placement="1"
ceph orch apply osd --all-available-devices
```

## RGW (optional)

```bash
ceph orch apply rgw dev --placement="1" --port=7480
ceph config set client.rgw rgw_enable_apis s3
ceph config set client.rgw rgw frontends "beast port=7480"
```

## Rationale

| Option | Why |
|--------|-----|
| `size = 2` | Saves space; OK only on isolated lab network |
| `pg_autoscale_mode = on` | Avoid manual PG math on small pools |
| Lower `osd_memory_target` | Fits small VMs |

See [Lab scale guide](../../guides/scales/lab.md).

[← Examples overview](OVERVIEW.md)
