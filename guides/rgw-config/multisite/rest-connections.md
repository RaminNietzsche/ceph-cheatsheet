# REST connections

RGW config deep dive — 3 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_rest_conn_connect_to_resolved_ips](#rgw_rest_conn_connect_to_resolved_ips) | `False` | Advanced | Policy |
| [rgw_rest_conn_ip_fail_timeout_secs](#rgw_rest_conn_ip_fail_timeout_secs) | `2` | Advanced | Performance |
| [rgw_rest_getusage_op_compat](#rgw_rest_getusage_op_compat) | `False` | Advanced | Policy |

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

### rgw_rest_conn_connect_to_resolved_ips

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips) |

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rest_conn_connect_to_resolved_ips true
ceph config get client.rgw rgw_rest_conn_connect_to_resolved_ips
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_rest_conn_ip_fail_timeout_secs

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs](../../../config/rgw/rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs) |

**What it does:** IP failure tracking timeout (requires rgw_rest_conn_connect_to_resolved_ips=true)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_rest_conn_ip_fail_timeout_secs 2
ceph config get client.rgw rgw_rest_conn_ip_fail_timeout_secs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Default `2` suits LAN RTT; WAN needs higher values.
2. **Increase** when logs show client/broker timeouts under load.
3. **Decrease** to fail fast and trigger retries upstream.

**Signals:** `curl`/`aws` timeout errors, Kafka/HTTP notification failures.

```bash
ceph config get client.rgw rgw_rest_conn_ip_fail_timeout_secs
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---

### rgw_rest_getusage_op_compat

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_getusage_op_compat](../../../config/rgw/rgw.md#SP_rgw_rest_getusage_op_compat) |

**What it does:** REST GetUsage request backward compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rest_getusage_op_compat true
ceph config get client.rgw rgw_rest_getusage_op_compat
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `False` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---


[← RGW config overview](../OVERVIEW.md)
