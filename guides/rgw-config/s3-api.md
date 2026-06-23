# S3 API behavior

RGW config deep dive — 8 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_s3_auth_disable_signature_url](#rgw_s3_auth_disable_signature_url) | `False` | Advanced |
| [rgw_s3_auth_order](#rgw_s3_auth_order) | `sts, external, local` | Advanced |
| [rgw_s3_auth_use_keystone](#rgw_s3_auth_use_keystone) | `False` | Advanced |
| [rgw_s3_auth_use_ldap](#rgw_s3_auth_use_ldap) | `False` | Advanced |
| [rgw_s3_auth_use_rados](#rgw_s3_auth_use_rados) | `True` | Advanced |
| [rgw_s3_auth_use_sts](#rgw_s3_auth_use_sts) | `False` | Advanced |
| [rgw_s3_client_max_sig_ver](#rgw_s3_client_max_sig_ver) | `-1` | Advanced |
| [rgw_s3_success_create_obj_status](#rgw_s3_success_create_obj_status) | `0` | Advanced |

---

### rgw_s3_auth_disable_signature_url

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_disable_signature_url](../../config/rgw/rgw.md#SP_rgw_s3_auth_disable_signature_url) |

**What it does:** Should authentication with presigned URLs be disabled

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_disable_signature_url False
ceph config get client.rgw rgw_s3_auth_disable_signature_url
```

**Finding optimal value:** Use the nearest stable endpoint reachable from every RGW node. Verify with curl from each host; measure p99 latency of dependent operations and keep the default (`False`) if the integration is unused.

---

### rgw_s3_auth_order

| | |
|---|---|
| Type | Str · default `sts, external, local` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_order](../../config/rgw/rgw.md#SP_rgw_s3_auth_order) |

**What it does:** Authentication strategy order to use for S3

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_order "sts, external, local"
ceph config get client.rgw rgw_s3_auth_order
```

**Finding optimal value:** Start from upstream default (`sts, external, local`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_s3_auth_use_keystone

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_keystone](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_keystone) |

**What it does:** Specify whether S3 authentication uses Keystone

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_keystone False
ceph config get client.rgw rgw_s3_auth_use_keystone
```

**Finding optimal value:** Not a performance knob — use credentials from your identity/KMS provider. Rotate via secrets management; never commit values to config repos.

---

### rgw_s3_auth_use_ldap

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_ldap](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_ldap) |

**What it does:** Should S3 authentication use LDAP.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_ldap False
ceph config get client.rgw rgw_s3_auth_use_ldap
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_s3_auth_use_rados

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_rados](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_rados) |

**What it does:** Specify whether S3 authentication uses credentials stored in RADOS

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_rados True
ceph config get client.rgw rgw_s3_auth_use_rados
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`True`) matches upstream.

---

### rgw_s3_auth_use_sts

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_auth_use_sts](../../config/rgw/rgw.md#SP_rgw_s3_auth_use_sts) |

**What it does:** Should S3 authentication use STS.

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_s3_auth_use_sts False
ceph config get client.rgw rgw_s3_auth_use_sts
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_s3_client_max_sig_ver

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_client_max_sig_ver](../../config/rgw/rgw.md#SP_rgw_s3_client_max_sig_ver) |

**What it does:** Max S3 authentication signature version

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_s3_client_max_sig_ver -1
ceph config get client.rgw rgw_s3_client_max_sig_ver
```

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`-1`) matches S3 compatibility for most workloads.

---

### rgw_s3_success_create_obj_status

| | |
|---|---|
| Type | Int · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_s3_success_create_obj_status](../../config/rgw/rgw.md#SP_rgw_s3_success_create_obj_status) |

**What it does:** HTTP return code override for object creation

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_s3_success_create_obj_status 0
ceph config get client.rgw rgw_s3_success_create_obj_status
```

**Finding optimal value:** Start from upstream default (`0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
