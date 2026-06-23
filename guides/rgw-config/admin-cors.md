# Admin CORS

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_gcors_allow_headers](#rgw_gcors_allow_headers) | `(empty)` | Advanced |
| [rgw_gcors_allow_methods](#rgw_gcors_allow_methods) | `(empty)` | Advanced |
| [rgw_gcors_allow_origins](#rgw_gcors_allow_origins) | `(empty)` | Advanced |
| [rgw_gcors_expose_headers](#rgw_gcors_expose_headers) | `(empty)` | Advanced |

---

### rgw_gcors_allow_headers

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_gcors_allow_headers](../../config/rgw/rgw.md#SP_rgw_gcors_allow_headers) |

**What it does:** When not empty, this value is returned as a response header Access-Control-Allow-Headers to preflight requests.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gcors_allow_headers <value>
ceph config get client.rgw rgw_gcors_allow_headers
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_gcors_allow_methods

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_gcors_allow_methods](../../config/rgw/rgw.md#SP_rgw_gcors_allow_methods) |

**What it does:** When not empty, this value is returned as a response header Access-Control-Allow-Methods.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gcors_allow_methods <value>
ceph config get client.rgw rgw_gcors_allow_methods
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_gcors_allow_origins

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_gcors_allow_origins](../../config/rgw/rgw.md#SP_rgw_gcors_allow_origins) |

**What it does:** When not empty, this value is returned as a response header Access-Control-Allow-Origins.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gcors_allow_origins <value>
ceph config get client.rgw rgw_gcors_allow_origins
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_gcors_expose_headers

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_gcors_expose_headers](../../config/rgw/rgw.md#SP_rgw_gcors_expose_headers) |

**What it does:** When not empty, this value is returned as a response header Access-Control-Expose-Headers.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_gcors_expose_headers <value>
ceph config get client.rgw rgw_gcors_expose_headers
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
