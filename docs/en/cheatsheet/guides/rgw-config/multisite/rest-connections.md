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
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph pg stat
```

---

### rgw_rest_conn_connect_to_resolved_ips

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips) |

**What it does:** When an RGW endpoint hostname resolves to multiple A or AAAA records, libcurl normally connects to only the first address returned by DNS. Enabling this option causes RGW to resolve each configured endpoint into all of its addresses and distribute outgoing requests across them using round-robin, with per-IP health tracking. This applies to multisite replication traffic between zones (via RGWRESTConn). For example, in a multisite deployment where zone endpoints such as "https://zone-a.example.com" map to several backend RGW nodes, this allows inter-zone traffic to be spread across all peers without requiring an external load balancer.

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Related options:**

- [`rgw_rest_conn_ip_fail_timeout_secs`](../../../config/rgw/rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs)

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

**What it does:** IP failure tracking timeout (requires rgw_rest_conn_connect_to_resolved_ips=true) When rgw_rest_conn_connect_to_resolved_ips is enabled, RGW tracks per-IP connection failures by remembering the timestamp of the most recent failure. This option controls how long (in seconds) an IP address remains marked as "failed" before RGW considers it eligible for retry. After this timeout expires, the IP will be tried again in the normal round-robin rotation.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`rgw_rest_conn_connect_to_resolved_ips`](../../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips)

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
radosgw-admin sync status
ceph config show client.rgw.<instance>
ceph -s  # cluster health, slow ops
```

---

### rgw_rest_getusage_op_compat

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_getusage_op_compat](../../../config/rgw/rgw.md#SP_rgw_rest_getusage_op_compat) |

**What it does:** REST GetUsage request backward compatibility

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

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
