# Observability overview

## Health and status

| Source | What |
|--------|------|
| `ceph -s` / `ceph health` | Cluster health affecting RGW |
| `radosgw-admin sync status` | Multisite lag |
| Ops log / usage log | Per-request audit (config dependent) |
| Admin socket `perf dump` | Daemon counters on RGW node |

## Key signals

- **503 SlowDown** — scheduling or rate limits ([dmclock](dmclock-architecture.md), [rate limit](rate-limit-architecture.md))
- **Sync lag** — secondary zone behind primary
- **GC queue depth** — background cleanup backlog
- **Reshard activity** — bucket index migration

## Debug

```bash
ceph config set client.rgw debug_rgw 10/5
ceph orch logs rgw.<host>.<id> --follow
```

## Related

- [Cheatsheet: troubleshooting](../../../cheatsheet/cli/troubleshooting.md)
- [Request pipeline](request-pipeline.md)
