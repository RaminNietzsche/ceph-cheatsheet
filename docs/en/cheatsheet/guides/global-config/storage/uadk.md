# Uadk

Global config deep dive — 2 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [uadk_compressor_enabled](#uadk_compressor_enabled) | `False` | Advanced | Policy |
| [uadk_wd_sync_ctx_num](#uadk_wd_sync_ctx_num) | `2` | Advanced | Performance |

## Finding optimal values

| Model | How to choose |
|-------|---------------|
| **Policy** | Security, compatibility, operational defaults |
| **Capacity** | Disk layout, paths, sizing |
| **Performance** | Baseline → incremental change → monitor cluster |
| **Connectivity** | Nearest stable external endpoint |
| **Dev** | Keep upstream default in production |

**Shared tooling:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### uadk_compressor_enabled

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [uadk.md#SP_uadk_compressor_enabled](../../../config/global/uadk.md#SP_uadk_compressor_enabled) |

**What it does:** Enable UADK acceleration support for compression if available

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set global uadk_compressor_enabled true
ceph config get global uadk_compressor_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global uadk_compressor_enabled
ceph -s
```

---

### uadk_wd_sync_ctx_num

| | |
|---|---|
| Type | Int · default `2` · **Advanced** |
| Table | [uadk.md#SP_uadk_wd_sync_ctx_num](../../../config/global/uadk.md#SP_uadk_wd_sync_ctx_num) |

**What it does:** Set the number of instances in the queue

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set global uadk_wd_sync_ctx_num 2
ceph config get global uadk_wd_sync_ctx_num
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `2`, max `1024`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global uadk_wd_sync_ctx_num
ceph -s
```

---


[← Overview](../OVERVIEW.md)
