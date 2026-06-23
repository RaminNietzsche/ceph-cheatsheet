# Request scheduler

RGW config deep dive — 1 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_scheduler_type](#rgw_scheduler_type) | `throttler` | Advanced |

---

### rgw_scheduler_type

| | |
|---|---|
| Type | Str · default `throttler` · **Advanced** |
| Table | [rgw.md#SP_rgw_scheduler_type](../../config/rgw/rgw.md#SP_rgw_scheduler_type) |

**What it does:** Set the type of dmclock scheduler, defaults to throttler. Other valid value is dmclock which is experimental.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_scheduler_type throttler
ceph config get client.rgw rgw_scheduler_type
```

**Finding optimal value:** Start from upstream default (`throttler`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
