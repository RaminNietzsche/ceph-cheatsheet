# 可观测性概览

## ## 健康与状态

| Source | What |
|--------|------|
| `ceph -s` / `ceph health` | Cluster health affecting RGW |
| `radosgw-admin sync status` | Multisite lag |
| Ops log / usage log | Per-request audit (config dependent) |
| Admin socket `perf dump` | Daemon counters on RGW node |

## ## 关键信号

- **503 SlowDown** — scheduling or rate limits ([dmclock](dmclock-architecture.md), [rate limit](rate-limit-architecture.md))
- **Sync lag** — secondary zone behind primary
- **GC queue depth** — background cleanup backlog
- **Reshard activity** — bucket index migration

## ## 调试

```bash
ceph config set client.rgw debug_rgw 10/5
ceph orch logs rgw.<host>.<id> --follow
```

## 相关

- [Cheatsheet: troubleshooting](../../../cli/troubleshooting.md)
- [Request pipeline](request-pipeline.md)
