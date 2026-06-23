# Debug and fault injection

RGW config deep dive — 7 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_debug_inject_latency_bi_unlink](#rgw_debug_inject_latency_bi_unlink) | `0` | Dev |
| [rgw_debug_inject_olh_cancel_modification_err](#rgw_debug_inject_olh_cancel_modification_err) | `False` | Dev |
| [rgw_debug_inject_set_olh_err](#rgw_debug_inject_set_olh_err) | `0` | Dev |
| [rgw_inject_delay_pattern](#rgw_inject_delay_pattern) | `(empty)` | Dev |
| [rgw_inject_delay_sec](#rgw_inject_delay_sec) | `0` | Dev |
| [rgw_mp_lock_inject_delay](#rgw_mp_lock_inject_delay) | `0` | Dev |
| [rgw_mp_lock_inject_renewal_error](#rgw_mp_lock_inject_renewal_error) | `0` | Dev |

---

### rgw_debug_inject_latency_bi_unlink

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_debug_inject_latency_bi_unlink](../../config/rgw/rgw.md#SP_rgw_debug_inject_latency_bi_unlink) |

**What it does:** Latency (in seconds) injected before rgw bucket index unlink op calls to simulate queueing latency and validate behavior of simultaneous delete requests which target the same object.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_debug_inject_latency_bi_unlink 0
ceph config get client.rgw rgw_debug_inject_latency_bi_unlink
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_debug_inject_olh_cancel_modification_err

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err](../../config/rgw/rgw.md#SP_rgw_debug_inject_olh_cancel_modification_err) |

**What it does:** Whether to inject an error to simulate a failure to cancel olh modification. This exists for development and testing purposes.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_debug_inject_olh_cancel_modification_err False
ceph config get client.rgw rgw_debug_inject_olh_cancel_modification_err
```

**Finding optimal value:** Keep the upstream default (`False`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_debug_inject_set_olh_err

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_debug_inject_set_olh_err](../../config/rgw/rgw.md#SP_rgw_debug_inject_set_olh_err) |

**What it does:** Whether to inject errors between rados olh modification initialization and bucket index instance linking. The value determines the error code. This exists for development and testing purposes to help simulate cases where bucket index entries aren't cleaned up by the request thread after an error scenario.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_debug_inject_set_olh_err 0
ceph config get client.rgw rgw_debug_inject_set_olh_err
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_inject_delay_pattern

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [rgw.md#SP_rgw_inject_delay_pattern](../../config/rgw/rgw.md#SP_rgw_inject_delay_pattern) |

**What it does:** select which delay injection points are activated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_inject_delay_pattern <value>
ceph config get client.rgw rgw_inject_delay_pattern
```

**Finding optimal value:** Keep the upstream default (`(empty)`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_inject_delay_sec

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_inject_delay_sec](../../config/rgw/rgw.md#SP_rgw_inject_delay_sec) |

**What it does:** delay duration in seconds for test injection points

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_inject_delay_sec 0
ceph config get client.rgw rgw_inject_delay_sec
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_mp_lock_inject_delay

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_mp_lock_inject_delay](../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_delay) |

**What it does:** Injected delay after acquiring the multipart lock for renewal testing

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_mp_lock_inject_delay 0
ceph config get client.rgw rgw_mp_lock_inject_delay
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---

### rgw_mp_lock_inject_renewal_error

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [rgw.md#SP_rgw_mp_lock_inject_renewal_error](../../config/rgw/rgw.md#SP_rgw_mp_lock_inject_renewal_error) |

**What it does:** Injected error code for multipart lock renewal testing

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set client.rgw rgw_mp_lock_inject_renewal_error 0
ceph config get client.rgw rgw_mp_lock_inject_renewal_error
```

**Finding optimal value:** Keep the upstream default (`0`) in production. Enable or change only during targeted debugging sessions.

---


[← RGW config overview](OVERVIEW.md)
