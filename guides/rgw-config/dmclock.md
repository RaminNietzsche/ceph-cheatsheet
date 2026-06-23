# dmclock scheduler

RGW config deep dive — 12 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_dmclock_admin_lim](#rgw_dmclock_admin_lim) | `0` | Advanced |
| [rgw_dmclock_admin_res](#rgw_dmclock_admin_res) | `100` | Advanced |
| [rgw_dmclock_admin_wgt](#rgw_dmclock_admin_wgt) | `100` | Advanced |
| [rgw_dmclock_auth_lim](#rgw_dmclock_auth_lim) | `0` | Advanced |
| [rgw_dmclock_auth_res](#rgw_dmclock_auth_res) | `200` | Advanced |
| [rgw_dmclock_auth_wgt](#rgw_dmclock_auth_wgt) | `100` | Advanced |
| [rgw_dmclock_data_lim](#rgw_dmclock_data_lim) | `0` | Advanced |
| [rgw_dmclock_data_res](#rgw_dmclock_data_res) | `500` | Advanced |
| [rgw_dmclock_data_wgt](#rgw_dmclock_data_wgt) | `500` | Advanced |
| [rgw_dmclock_metadata_lim](#rgw_dmclock_metadata_lim) | `0` | Advanced |
| [rgw_dmclock_metadata_res](#rgw_dmclock_metadata_res) | `500` | Advanced |
| [rgw_dmclock_metadata_wgt](#rgw_dmclock_metadata_wgt) | `500` | Advanced |

---

### rgw_dmclock_admin_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_lim](../../config/rgw/rgw.md#SP_rgw_dmclock_admin_lim) |

**What it does:** mclock limit for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_lim 0
ceph config get client.rgw rgw_dmclock_admin_lim
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`0`).

---

### rgw_dmclock_admin_res

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_res](../../config/rgw/rgw.md#SP_rgw_dmclock_admin_res) |

**What it does:** mclock reservation for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_res 100
ceph config get client.rgw rgw_dmclock_admin_res
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`100`).

---

### rgw_dmclock_admin_wgt

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_admin_wgt](../../config/rgw/rgw.md#SP_rgw_dmclock_admin_wgt) |

**What it does:** mclock weight for admin requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_admin_wgt 100
ceph config get client.rgw rgw_dmclock_admin_wgt
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`100`).

---

### rgw_dmclock_auth_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_lim](../../config/rgw/rgw.md#SP_rgw_dmclock_auth_lim) |

**What it does:** mclock limit for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_lim 0
ceph config get client.rgw rgw_dmclock_auth_lim
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`0`).

---

### rgw_dmclock_auth_res

| | |
|---|---|
| Type | Float · default `200` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_res](../../config/rgw/rgw.md#SP_rgw_dmclock_auth_res) |

**What it does:** mclock reservation for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_res 200
ceph config get client.rgw rgw_dmclock_auth_res
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`200`).

---

### rgw_dmclock_auth_wgt

| | |
|---|---|
| Type | Float · default `100` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_auth_wgt](../../config/rgw/rgw.md#SP_rgw_dmclock_auth_wgt) |

**What it does:** mclock weight for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_auth_wgt 100
ceph config get client.rgw rgw_dmclock_auth_wgt
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`100`).

---

### rgw_dmclock_data_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_lim](../../config/rgw/rgw.md#SP_rgw_dmclock_data_lim) |

**What it does:** mclock limit for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_lim 0
ceph config get client.rgw rgw_dmclock_data_lim
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`0`).

---

### rgw_dmclock_data_res

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_res](../../config/rgw/rgw.md#SP_rgw_dmclock_data_res) |

**What it does:** mclock reservation for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_res 500
ceph config get client.rgw rgw_dmclock_data_res
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`500`).

---

### rgw_dmclock_data_wgt

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_data_wgt](../../config/rgw/rgw.md#SP_rgw_dmclock_data_wgt) |

**What it does:** mclock weight for object data requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_data_wgt 500
ceph config get client.rgw rgw_dmclock_data_wgt
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`500`).

---

### rgw_dmclock_metadata_lim

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_lim](../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_lim) |

**What it does:** mclock limit for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_lim 0
ceph config get client.rgw rgw_dmclock_metadata_lim
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`0`).

---

### rgw_dmclock_metadata_res

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_res](../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_res) |

**What it does:** mclock reservation for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_res 500
ceph config get client.rgw rgw_dmclock_metadata_res
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`500`).

---

### rgw_dmclock_metadata_wgt

| | |
|---|---|
| Type | Float · default `500` · **Advanced** |
| Table | [rgw.md#SP_rgw_dmclock_metadata_wgt](../../config/rgw/rgw.md#SP_rgw_dmclock_metadata_wgt) |

**What it does:** mclock weight for metadata requests

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_dmclock_metadata_wgt 500
ceph config get client.rgw rgw_dmclock_metadata_wgt
```

**Finding optimal value:** Tune reservation/limit/weight together per queue (admin, auth, data, metadata). Use `ceph daemon rgw.<id> perf dump` and dmclock stats; start from defaults (`500`).

---


[← RGW config overview](OVERVIEW.md)
