# 速率限制架构

Per-user and per-bucket rate limiting in RGW — applied **after authentication** via `ActiveRateLimiter` and token-bucket counters in process memory.

## ## 与 dmclock 对比

| | Rate limit | dmclock / throttler |
|---|------------|---------------------|
| **When** | After `pre_exec` | Before auth |
| **Goal** | Tenant quota | Server QoS / concurrency |
| **Scope** | Per user/bucket keys | Per gateway |

Both may return **503 SlowDown** — distinguish in monitoring.

## Core types

- `RGWRateLimitInfo` — limits encoded on user/bucket/period attrs
- `RateLimiter` / `ActiveRateLimiter` — in-memory counters per gateway
- Op classes: read, write, list, delete (+ bytes)

## ## 运维注意（摘要）

1. **Per-gateway counters** — limit ÷ N RGW instances for cluster-wide caps
2. **LIST vs GET** — list limits only match specific query patterns
3. **`first_run` burst** — new map entries start with full token bucket
4. **Health checks** — not counted against tenant limits
5. **Struct version** — old attrs may leave list/delete limits at 0 (unlimited)

## 完整细节

Extended Persian documentation (21+ operational scenarios) is synced from upstream `docs-extended/pages/architecture/rate-limit-architecture.md`. Switch to **فارسی** locale for the full text on this site.

## 相关

- [dmclock architecture](dmclock-architecture.md)
- [Scheduling architecture](scheduling-architecture.md)
