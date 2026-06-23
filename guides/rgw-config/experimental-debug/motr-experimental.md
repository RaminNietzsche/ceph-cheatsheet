# Motr backend

RGW config deep dive — 7 options. [← RGW config overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [motr_admin_endpoint](#motr_admin_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_admin_fid](#motr_admin_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_ha_endpoint](#motr_ha_endpoint) | `192.168.180.182@tcp:12345:1:1` | Advanced | Architecture |
| [motr_my_endpoint](#motr_my_endpoint) | `192.168.180.182@tcp:12345:4:1` | Advanced | Architecture |
| [motr_my_fid](#motr_my_fid) | `0x7200000000000001:0x0` | Advanced | Architecture |
| [motr_profile_fid](#motr_profile_fid) | `0x7000000000000001:0x0` | Advanced | Architecture |
| [motr_tracing_enabled](#motr_tracing_enabled) | `False` | Advanced | Dev |

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

### motr_admin_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| Table | [motr.md#SP_motr_admin_endpoint](../../../config/rgw/motr.md#SP_motr_admin_endpoint) |

**What it does:** experimental Option to set Admin Motr endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_admin_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_admin_endpoint
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_admin_fid

| | |
|---|---|
| Type | Str · default `0x7200000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_admin_fid](../../../config/rgw/motr.md#SP_motr_admin_fid) |

**What it does:** Admin Tool Motr FID for admin-level access.

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_admin_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_admin_fid
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_ha_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:1:1` · **Advanced** |
| Table | [motr.md#SP_motr_ha_endpoint](../../../config/rgw/motr.md#SP_motr_ha_endpoint) |

**What it does:** experimental Option to set Motr HA agent endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_ha_endpoint "192.168.180.182@tcp:12345:1:1"
ceph config get client.rgw motr_ha_endpoint
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:1:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_endpoint

| | |
|---|---|
| Type | Str · default `192.168.180.182@tcp:12345:4:1` · **Advanced** |
| Table | [motr.md#SP_motr_my_endpoint](../../../config/rgw/motr.md#SP_motr_my_endpoint) |

**What it does:** experimental Option to set my Motr endpoint address

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_my_endpoint "192.168.180.182@tcp:12345:4:1"
ceph config get client.rgw motr_my_endpoint
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `192.168.180.182@tcp:12345:4:1` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_my_fid

| | |
|---|---|
| Type | Str · default `0x7200000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_my_fid](../../../config/rgw/motr.md#SP_motr_my_fid) |

**What it does:** experimental Option to set my Motr fid

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_my_fid "0x7200000000000001:0x0"
ceph config get client.rgw motr_my_fid
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7200000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_profile_fid

| | |
|---|---|
| Type | Str · default `0x7000000000000001:0x0` · **Advanced** |
| Table | [motr.md#SP_motr_profile_fid](../../../config/rgw/motr.md#SP_motr_profile_fid) |

**What it does:** experimental Option to set Motr profile fid

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_profile_fid "0x7000000000000001:0x0"
ceph config get client.rgw motr_profile_fid
```

**Finding optimal value:**

**Tuning model:** Architecture

1. Treat as deployment metadata, not a throughput knob.
2. Keep `0x7000000000000001:0x0` unless documentation for your topology says otherwise.
3. Document the chosen value in runbooks — changing it can break multisite or auth.

---

### motr_tracing_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [motr.md#SP_motr_tracing_enabled](../../../config/rgw/motr.md#SP_motr_tracing_enabled) |

**What it does:** Set to true when Motr client debugging is needed

**When to use:** Experimental Motr/POSIX RGW backends — use only in specialized PoC deployments.

**Example:**

```bash
ceph config set client.rgw motr_tracing_enabled true
ceph config get client.rgw motr_tracing_enabled
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) on every production RGW.
2. Enable or change only in a lab while reproducing a specific bug.
3. Revert before returning the node to the production pool.

**Signals:** assertion failures, injected errors, or trace noise in logs.

---


[← RGW config overview](../OVERVIEW.md)
