# Small production example

Typical **3–12 nodes**, one datacenter, replica **3**, cephadm-managed.

## Architecture checklist

- 3 MON on separate hosts
- 2 MGR (active + standby)
- One OSD per disk; separate public/cluster networks if possible

## Recommended settings

```ini
[global]
osd_pool_default_size = 3
osd_pool_default_min_size = 2
osd_pool_default_pg_autoscale_mode = on

mon_osd_down_out_interval = 600
mon_osd_min_down_reporters = 2

# Capacity warnings (defaults — verify for your policy)
mon_osd_full_ratio = 0.95
mon_osd_nearfull_ratio = 0.85
mon_osd_backfillfull_ratio = 0.90

public_network = 10.0.1.0/24
cluster_network = 10.0.2.0/24
```

## MGR / cephadm

```ini
[mgr]
mgr/cephadm/autotune = true
```

```bash
ceph orch apply mon --placement="3 host1 host2 host3"
ceph orch apply mgr --placement="2 host1 host2"
ceph orch apply osd --all-available-devices
```

## RGW (single zone)

```bash
ceph orch apply rgw prod --placement="2 host1 host2" --port=8080
ceph config set client.rgw rgw_enable_apis s3
ceph config set client.rgw rgw frontends "beast ssl_port=443 ssl_certificate=/path/cert.pem"
```

## Rationale

| Option | Why |
|--------|-----|
| `size = 3` | Standard durability for production |
| Separate networks | Isolates recovery traffic from client I/O |
| `down_out_interval` | Avoid premature OSD mark-out on brief blips |

See [Small production scale](../../guides/scales/small-production.md).

[← Examples overview](OVERVIEW.md)
