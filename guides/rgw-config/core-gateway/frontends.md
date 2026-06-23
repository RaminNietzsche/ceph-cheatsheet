# Frontends & HTTP stack

RGW config deep dive — 6 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_asio_assert_yielding](#rgw_asio_assert_yielding) | `False` | Dev | Dev |
| [rgw_beast_enable_async](#rgw_beast_enable_async) | `True` | Dev | Policy |
| [rgw_dns_name](#rgw_dns_name) | `(empty)` | Advanced | Performance |
| [rgw_dns_s3website_name](#rgw_dns_s3website_name) | `(empty)` | Advanced | Performance |
| [rgw_frontend_defaults](#rgw_frontend_defaults) | `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` | Advanced | Performance |
| [rgw_frontends](#rgw_frontends) | `beast port=7480` | Basic | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, API compatibility, tenant limits |
| **Capacity** | Disk layout, paths, pool sizing |
| **Performance** | Baseline → incremental change → monitor OSD/RGW |
| **Connectivity** | Nearest stable external endpoint |
| **Architecture** | Backend, multisite topology — not numeric sweeps |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get client.rgw <option>
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_asio_assert_yielding

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_asio_assert_yielding](../../../config/rgw/rgw.md#SP_rgw_asio_assert_yielding) |

**What it does:** Triggers an assertion if code on an asio/beast thread would block instead of yielding to coroutines. Development aid for finding blocking calls.

**When to use:** RGW development/debugging only — keep `false` in production.

**Related options:**

- `rgw_beast_enable_async`

**Example:**

```bash
ceph config set client.rgw rgw_asio_assert_yielding true
ceph config get client.rgw rgw_asio_assert_yielding
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---

### rgw_beast_enable_async

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [rgw.md#SP_rgw_beast_enable_async](../../../config/rgw/rgw.md#SP_rgw_beast_enable_async) |

**What it does:** When `true`, the Beast HTTP frontend processes requests with **coroutines**, allowing multiple concurrent requests per thread.

**When to use:** Leave `true` for production throughput. Set `false` only when debugging request flow.

**Example:**

```bash
ceph config set client.rgw rgw_beast_enable_async false
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_dns_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_dns_name](../../../config/rgw/rgw.md#SP_rgw_dns_name) |

**What it does:** The host names that RGW uses.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dns_name "s3.example.com"
ceph config get client.rgw rgw_dns_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_name
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_dns_s3website_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_dns_s3website_name](../../../config/rgw/rgw.md#SP_rgw_dns_s3website_name) |

**What it does:** The host name that RGW uses for static websites (S3)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dns_s3website_name "website.s3.example.com"
ceph config get client.rgw rgw_dns_s3website_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_dns_s3website_name
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_frontend_defaults

| | |
|---|---|
| Type | Str · default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key` · **Advanced** |
| Table | [rgw.md#SP_rgw_frontend_defaults](../../../config/rgw/rgw.md#SP_rgw_frontend_defaults) |

**What it does:** RGW frontends default configuration

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_frontend_defaults "beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key"
ceph config get client.rgw rgw_frontend_defaults
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `beast ssl_certificate=config://rgw/cert/$realm/$zone.crt ssl_private_key=config://rgw/cert/$realm/$zone.key`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontend_defaults
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_frontends

| | |
|---|---|
| Type | Str · default `beast port=7480` · **Basic** |
| Table | [rgw.md#SP_rgw_frontends](../../../config/rgw/rgw.md#SP_rgw_frontends) |

**What it does:** RGW frontends configuration

**When to use:** Core RGW behavior — review before changing in production.

**Example:**

```bash
ceph config set client.rgw rgw_frontends "beast port=7480"
ceph config get client.rgw rgw_frontends
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `beast port=7480`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_frontends
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](../OVERVIEW.md)
