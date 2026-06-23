# Lua scripting

RGW config deep dive — 4 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_lua_enable](#rgw_lua_enable) | `True` | Advanced |
| [rgw_lua_max_memory_per_state](#rgw_lua_max_memory_per_state) | `128000` | Advanced |
| [rgw_lua_max_runtime_per_state](#rgw_lua_max_runtime_per_state) | `1000` | Advanced |
| [rgw_luarocks_location](#rgw_luarocks_location) | `/tmp/rgw_luarocks/$name` | Advanced |

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
ceph config set client.rgw rgw_lua_enable True
ceph config get client.rgw rgw_lua_enable
ceph orch restart rgw
```

**Finding optimal value:** Enable when the feature is required; otherwise keep default (`True`) to minimize background threads and memory.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`128000`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Raise only when clients hit documented limits; lower to protect RGW/OSD. Default (`1000`) matches S3 compatibility for most workloads.

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

**Finding optimal value:** Start from upstream default (`/tmp/rgw_luarocks/$name`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
