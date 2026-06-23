# REST connections (multisite)

RGW config deep dive — 3 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_rest_conn_connect_to_resolved_ips](#rgw_rest_conn_connect_to_resolved_ips) | `False` | Advanced |
| [rgw_rest_conn_ip_fail_timeout_secs](#rgw_rest_conn_ip_fail_timeout_secs) | `2` | Advanced |
| [rgw_rest_getusage_op_compat](#rgw_rest_getusage_op_compat) | `False` | Advanced |

---

### rgw_rest_conn_connect_to_resolved_ips

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips](../../config/rgw/rgw.md#SP_rgw_rest_conn_connect_to_resolved_ips) |

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rest_conn_connect_to_resolved_ips False
ceph config get client.rgw rgw_rest_conn_connect_to_resolved_ips
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_rest_conn_ip_fail_timeout_secs

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs](../../config/rgw/rgw.md#SP_rgw_rest_conn_ip_fail_timeout_secs) |

**What it does:** IP failure tracking timeout (requires rgw_rest_conn_connect_to_resolved_ips=true)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_rest_conn_ip_fail_timeout_secs 2
ceph config get client.rgw rgw_rest_conn_ip_fail_timeout_secs
```

**Finding optimal value:** Increase if clients see timeouts under load; decrease to fail fast. Default (`2`) matches typical LAN latency.

---

### rgw_rest_getusage_op_compat

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_rest_getusage_op_compat](../../config/rgw/rgw.md#SP_rgw_rest_getusage_op_compat) |

**What it does:** REST GetUsage request backward compatibility

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_rest_getusage_op_compat False
ceph config get client.rgw rgw_rest_getusage_op_compat
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---


[← RGW config overview](OVERVIEW.md)
