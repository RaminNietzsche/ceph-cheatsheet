# 关键缺口与高可用限制

坦诚分析 for capacity and availability planning.

## Potential single points of failure

| Component | Risk | Notes |
|-----------|------|-------|
| MON quorum | High | Lost quorum → cluster unavailable |
| Full pools | High | Writes stop |
| Stale period | Medium | Multisite config mismatch |
| Single master zone | Medium | Some admin ops need master |

## RGW edge HA

**Works well:**

- Multiple `radosgw` behind load balancer
- Rolling restart of instances

**Limited without design:**

- Read-your-writes across zones (sync lag)
- HA without RADOS replication on pools

RGW is **stateless at the edge** — good for horizontal scale.

## Bottlenecks

| Bottleneck | Symptom |
|------------|---------|
| Bucket index hotspot | One bucket, heavy traffic |
| Reshard | Listing delay during resharding |
| Sync lag | Stale data on secondary zone |
| dmclock / rate limit | 503 SlowDown |

## 相关

- [Runtime topology](runtime-topology.md)
- [Multisite module](../modules/multisite.md)
- [dmclock architecture](dmclock-architecture.md)
