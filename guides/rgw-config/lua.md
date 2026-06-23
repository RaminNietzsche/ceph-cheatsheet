# Lua scripting

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_lua_enable](#rgw_lua_enable) | `True` | Advanced | Policy |
| [rgw_lua_max_memory_per_state](#rgw_lua_max_memory_per_state) | `128000` | Advanced | Policy |
| [rgw_lua_max_runtime_per_state](#rgw_lua_max_runtime_per_state) | `1000` | Advanced | Policy |
| [rgw_luarocks_location](#rgw_luarocks_location) | `/tmp/rgw_luarocks/$name` | Advanced | Performance |

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
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph osd pool stats
```

---

### rgw_lua_enable

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_lua_enable](../../config/rgw/rgw.md#SP_rgw_lua_enable) |

**What it does:** Enable lua scripting.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_lua_enable false
ceph config get client.rgw rgw_lua_enable
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_lua_max_memory_per_state

| | |
|---|---|
| Type | Uint · default `128000` · **Advanced** |
| Table | [rgw.md#SP_rgw_lua_max_memory_per_state](../../config/rgw/rgw.md#SP_rgw_lua_max_memory_per_state) |

**What it does:** Max size of memory used by a single lua state

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lua_max_memory_per_state 128000
ceph config get client.rgw rgw_lua_max_memory_per_state
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `128000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_lua_max_runtime_per_state

| | |
|---|---|
| Type | Uint · default `1000` · **Advanced** |
| Table | [rgw.md#SP_rgw_lua_max_runtime_per_state](../../config/rgw/rgw.md#SP_rgw_lua_max_runtime_per_state) |

**What it does:** Maximum runtime for each Lua state in milliseconds

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_lua_max_runtime_per_state 1000
ceph config get client.rgw rgw_lua_max_runtime_per_state
```

**Finding optimal value:**

**Tuning model:** Policy

1. Start at `1000` (S3/AWS-aligned for most limits).
2. Raise only when clients return explicit limit errors in RGW logs.
3. Lower to harden against oversized requests or DoS.

---

### rgw_luarocks_location

| | |
|---|---|
| Type | Str · default `/tmp/rgw_luarocks/$name` · **Advanced** · **STARTUP** (restart required) |
| Table | [rgw.md#SP_rgw_luarocks_location](../../config/rgw/rgw.md#SP_rgw_luarocks_location) |

**What it does:** Directory where luarocks install packages from allowlist

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_luarocks_location "/tmp/rgw_luarocks/$name"
ceph config get client.rgw rgw_luarocks_location
ceph orch restart rgw
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/tmp/rgw_luarocks/$name`.
2. Change **one** option per test window under representative load.
3. Compare p50/p99 latency and throughput before/after.
4. Roll back if OSD slow ops, recovery backlog, or error rate increases.

**Signals:** client errors, `ceph -s` HEALTH_WARN, RGW perf counter deltas.

```bash
ceph config get client.rgw rgw_luarocks_location
ceph daemon rgw.<id> perf dump | jq '.rgw' | head
radosgw-admin perf stats
ceph -s  # cluster health, slow ops
```

---


[← RGW config overview](OVERVIEW.md)
