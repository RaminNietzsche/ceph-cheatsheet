# Motr (experimental backend)

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [motr_admin_endpoint](#motr_admin_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced |
| [motr_admin_fid](#motr_admin_fid) | `0x7200000000000001:0x0` | Advanced |
| [motr_ha_endpoint](#motr_ha_endpoint) | `192.168.180.182@tcp:12345:1:1` | Advanced |
| [motr_my_endpoint](#motr_my_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced |
| [motr_my_fid](#motr_my_fid) | `0x7200000000000001:0x0` | Advanced |
| [motr_profile_fid](#motr_profile_fid) | `0x7000000000000001:0x0` | Advanced |
| [motr_tracing_enabled](#motr_tracing_enabled) | `False` | Advanced |

---

### motr_admin_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| Table | [motr.md#SP_motr_admin_endpoint](../../config/rgw/motr.md#SP_motr_admin_endpoint) |

**What it does:** experimental Option to set Admin Motr endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_admin_endpoint 192.168.180.182@tcp:12345:4:1
ceph config get client.rgw motr_admin_endpoint
```

**Finding optimal value:** Start from upstream default (`192.168.180.182@tcp:12345:4:1`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_admin_fid

| | |
|---|---|
| Type | Str · default `0x7200000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_admin_fid](../../config/rgw/motr.md#SP_motr_admin_fid) |

**What it does:** Admin Tool Motr FID for admin-level access.

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_admin_fid 0x7200000000000001:0x0
ceph config get client.rgw motr_admin_fid
```

**Finding optimal value:** Start from upstream default (`0x7200000000000001:0x0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_ha_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:1:1` · **Advanced** |
| Table | [motr.md#SP_motr_ha_endpoint](../../config/rgw/motr.md#SP_motr_ha_endpoint) |

**What it does:** experimental Option to set Motr HA agent endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_ha_endpoint 192.168.180.182@tcp:12345:1:1
ceph config get client.rgw motr_ha_endpoint
```

**Finding optimal value:** Start from upstream default (`192.168.180.182@tcp:12345:1:1`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_my_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| Table | [motr.md#SP_motr_my_endpoint](../../config/rgw/motr.md#SP_motr_my_endpoint) |

**What it does:** experimental Option to set my Motr endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_my_endpoint 192.168.180.182@tcp:12345:4:1
ceph config get client.rgw motr_my_endpoint
```

**Finding optimal value:** Start from upstream default (`192.168.180.182@tcp:12345:4:1`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_my_fid

| | |
|---|---|
| Type | Str · default `0x7200000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_my_fid](../../config/rgw/motr.md#SP_motr_my_fid) |

**What it does:** experimental Option to set my Motr fid

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_my_fid 0x7200000000000001:0x0
ceph config get client.rgw motr_my_fid
```

**Finding optimal value:** Start from upstream default (`0x7200000000000001:0x0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_profile_fid

| | |
|---|---|
| Type | Str · default `0x7000000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_profile_fid](../../config/rgw/motr.md#SP_motr_profile_fid) |

**What it does:** experimental Option to set Motr profile fid

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_profile_fid 0x7000000000000001:0x0
ceph config get client.rgw motr_profile_fid
```

**Finding optimal value:** Start from upstream default (`0x7000000000000001:0x0`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### motr_tracing_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [motr.md#SP_motr_tracing_enabled](../../config/rgw/motr.md#SP_motr_tracing_enabled) |

**What it does:** Set to true when Motr client debugging is needed

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_tracing_enabled False
ceph config get client.rgw motr_tracing_enabled
```

**Finding optimal value:** Enable when the feature is required; otherwise keep default (`False`) to minimize background threads and memory.

---


[← RGW config overview](OVERVIEW.md)
