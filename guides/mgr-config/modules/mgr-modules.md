# Manager & cephadm modules

MGR config deep dive — 31 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mgr/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [cephadm_path](#cephadm_path) | `/usr/sbin/cephadm` | Advanced | Capacity |
| [mgr_client_bytes](#mgr_client_bytes) | `128_M` | Dev | Dev |
| [mgr_client_messages](#mgr_client_messages) | `512` | Dev | Dev |
| [mgr_data](#mgr_data) | `/var/lib/ceph/mgr/$cluster-$id` | Advanced | Performance |
| [mgr_debug_aggressive_pg_num_changes](#mgr_debug_aggressive_pg_num_changes) | `False` | Dev | Dev |
| [mgr_disabled_modules](#mgr_disabled_modules) | `0` | Advanced | Performance |
| [mgr_initial_modules](#mgr_initial_modules) | `iostat nfs nvmeof` | Basic | Policy |
| [mgr_max_pg_creating](#mgr_max_pg_creating) | `1024` | Advanced | Performance |
| [mgr_max_pg_num_change](#mgr_max_pg_num_change) | `128` | Advanced | Performance |
| [mgr_mds_bytes](#mgr_mds_bytes) | `128_M` | Dev | Dev |
| [mgr_mds_messages](#mgr_mds_messages) | `128` | Dev | Dev |
| [mgr_module_load_delay](#mgr_module_load_delay) | `0` | Dev | Dev |
| [mgr_module_load_delay_name](#mgr_module_load_delay_name) | `(empty)` | Dev | Dev |
| [mgr_module_load_expiration](#mgr_module_load_expiration) | `20000` | Dev | Dev |
| [mgr_module_monitor_interval](#mgr_module_monitor_interval) | `5` | Advanced | Performance |
| [mgr_module_path](#mgr_module_path) | `0/mgr` | Advanced | Capacity |
| [mgr_mon_bytes](#mgr_mon_bytes) | `128_M` | Dev | Dev |
| [mgr_mon_messages](#mgr_mon_messages) | `128` | Dev | Dev |
| [mgr_osd_bytes](#mgr_osd_bytes) | `512_M` | Dev | Dev |
| [mgr_osd_messages](#mgr_osd_messages) | `8_K` | Dev | Dev |
| [mgr_osd_upgrade_check_convergence_factor](#mgr_osd_upgrade_check_convergence_factor) | `0.8` | Advanced | Performance |
| [mgr_pool](#mgr_pool) | `True` | Dev | Dev |
| [mgr_service_beacon_grace](#mgr_service_beacon_grace) | `1_min` | Advanced | Performance |
| [mgr_standby_modules](#mgr_standby_modules) | `True` | Advanced | Performance |
| [mgr_stats_period](#mgr_stats_period) | `5` | Basic | Policy |
| [mgr_stats_period_autotune](#mgr_stats_period_autotune) | `True` | Basic | Policy |
| [mgr_stats_period_autotune_queue_threshold](#mgr_stats_period_autotune_queue_threshold) | `100` | Advanced | Performance |
| [mgr_stats_threshold](#mgr_stats_threshold) | `5` | Advanced | Performance |
| [mgr_subinterpreter_modules](#mgr_subinterpreter_modules) | `0` | Advanced | Performance |
| [mgr_test_metadata_error](#mgr_test_metadata_error) | `False` | Dev | Dev |
| [mgr_tick_period](#mgr_tick_period) | `2` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. mgr
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### cephadm_path

| | |
|---|---|
| Type | Str · default `/usr/sbin/cephadm` · **Advanced** |
| Table | [cephadm.md#SP_cephadm_path](../../../config/mgr/cephadm.md#SP_cephadm_path) |

**What it does:** Path to cephadm utility

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr cephadm_path "/usr/sbin/cephadm"
ceph config get mgr cephadm_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `/usr/sbin/cephadm`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr cephadm_path
ceph -s
ceph mgr dump
```

---

### mgr_client_bytes

| | |
|---|---|
| Type | Size · default `128_M` · **Dev** |
| Table | [mgr.md#SP_mgr_client_bytes](../../../config/mgr/mgr.md#SP_mgr_client_bytes) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_client_bytes 128_M
ceph config get mgr mgr_client_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_client_messages

| | |
|---|---|
| Type | Uint · default `512` · **Dev** |
| Table | [mgr.md#SP_mgr_client_messages](../../../config/mgr/mgr.md#SP_mgr_client_messages) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_client_messages 512
ceph config get mgr mgr_client_messages
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`512`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_data

| | |
|---|---|
| Type | Str · default `/var/lib/ceph/mgr/$cluster-$id` · **Advanced** |
| Table | [mgr.md#SP_mgr_data](../../../config/mgr/mgr.md#SP_mgr_data) |

**What it does:** Filesystem path to the Manager's data directory, which contains keyrings and other data

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_data "/var/lib/ceph/mgr/$cluster-$id"
ceph config get mgr mgr_data
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `/var/lib/ceph/mgr/$cluster-$id`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_data
ceph -s
ceph mgr dump
```

---

### mgr_debug_aggressive_pg_num_changes

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mgr.md#SP_mgr_debug_aggressive_pg_num_changes](../../../config/mgr/mgr.md#SP_mgr_debug_aggressive_pg_num_changes) |

**What it does:** Bypass most throttling and safety checks in pg&#91;p&#93;_num controller

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_debug_aggressive_pg_num_changes true
ceph config get mgr mgr_debug_aggressive_pg_num_changes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_disabled_modules

| | |
|---|---|
| Type | Str · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [mgr.md#SP_mgr_disabled_modules](../../../config/mgr/mgr.md#SP_mgr_disabled_modules) |

**What it does:** List of manager modules never get loaded

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_disabled_modules "example"
ceph config get mgr mgr_disabled_modules
ceph orch restart mgr
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_disabled_modules
ceph -s
ceph mgr dump
```

---

### mgr_initial_modules

| | |
|---|---|
| Type | Str · default `iostat nfs nvmeof` · **Basic** |
| Table | [mgr.md#SP_mgr_initial_modules](../../../config/mgr/mgr.md#SP_mgr_initial_modules) |

**What it does:** List of manager modules to enable when the cluster is first started

**When to use:** Core MGR behavior — review before changing in production.

**Example:**

```bash
ceph config set mgr mgr_initial_modules "iostat nfs nvmeof"
ceph config get mgr mgr_initial_modules
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `iostat nfs nvmeof` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_initial_modules
ceph -s
ceph mgr dump
```

---

### mgr_max_pg_creating

| | |
|---|---|
| Type | Uint · default `1024` · **Advanced** |
| Table | [mgr.md#SP_mgr_max_pg_creating](../../../config/mgr/mgr.md#SP_mgr_max_pg_creating) |

**What it does:** bound on max creating pgs when acting to create more pgs

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mgr mgr_max_pg_creating 1024
ceph config get mgr mgr_max_pg_creating
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1024`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_max_pg_creating
ceph -s
ceph mgr dump
```

---

### mgr_max_pg_num_change

| | |
|---|---|
| Type | Int · default `128` · **Advanced** |
| Table | [mgr.md#SP_mgr_max_pg_num_change](../../../config/mgr/mgr.md#SP_mgr_max_pg_num_change) |

**What it does:** maximum change in pg_num

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mgr mgr_max_pg_num_change 128
ceph config get mgr mgr_max_pg_num_change
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `128`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_max_pg_num_change
ceph -s
ceph mgr dump
```

---

### mgr_mds_bytes

| | |
|---|---|
| Type | Size · default `128_M` · **Dev** |
| Table | [mgr.md#SP_mgr_mds_bytes](../../../config/mgr/mgr.md#SP_mgr_mds_bytes) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_mds_bytes 128_M
ceph config get mgr mgr_mds_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_mds_messages

| | |
|---|---|
| Type | Uint · default `128` · **Dev** |
| Table | [mgr.md#SP_mgr_mds_messages](../../../config/mgr/mgr.md#SP_mgr_mds_messages) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_mds_messages 128
ceph config get mgr mgr_mds_messages
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_module_load_delay

| | |
|---|---|
| Type | Millisecs · default `0` · **Dev** |
| Table | [mgr.md#SP_mgr_module_load_delay](../../../config/mgr/mgr.md#SP_mgr_module_load_delay) |

**What it does:** Number of milliseconds for Manager modules to delay loading. For testing purposes only.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_module_load_delay 0
ceph config get mgr mgr_module_load_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_module_load_delay_name

| | |
|---|---|
| Type | Str · default `(empty)` · **Dev** |
| Table | [mgr.md#SP_mgr_module_load_delay_name](../../../config/mgr/mgr.md#SP_mgr_module_load_delay_name) |

**What it does:** Specify which Manager module is to delay loading by mgr_module_load_delay milliseconds. For testing purposes only.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_module_load_delay_name "example"
ceph config get mgr mgr_module_load_delay_name
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`(empty)`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_module_load_expiration

| | |
|---|---|
| Type | Millisecs · default `20000` · **Dev** |
| Table | [mgr.md#SP_mgr_module_load_expiration](../../../config/mgr/mgr.md#SP_mgr_module_load_expiration) |

**What it does:** Maximum number of milliseconds the active mgr is allowed to load the mgr modules before declaring availability.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_module_load_expiration 20000
ceph config get mgr mgr_module_load_expiration
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`20000`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_module_monitor_interval

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mgr.md#SP_mgr_module_monitor_interval](../../../config/mgr/mgr.md#SP_mgr_module_monitor_interval) |

**What it does:** Period in seconds for collecting Manager modules cpu and memory performance counters.

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mgr mgr_module_monitor_interval 5
ceph config get mgr mgr_module_monitor_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_module_monitor_interval
ceph -s
ceph mgr dump
```

---

### mgr_module_path

| | |
|---|---|
| Type | Str · default `0/mgr` · **Advanced** |
| Table | [mgr.md#SP_mgr_module_path](../../../config/mgr/mgr.md#SP_mgr_module_path) |

**What it does:** Filesystem path to manager modules.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_module_path "0/mgr"
ceph config get mgr mgr_module_path
```

**Finding optimal value:**

**Tuning model:** Capacity

1. Baseline at `0/mgr`.
2. Plan capacity and filesystem layout before changing paths.
3. Ensure all daemons that must share the path see the same mount.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_module_path
ceph -s
ceph mgr dump
```

---

### mgr_mon_bytes

| | |
|---|---|
| Type | Size · default `128_M` · **Dev** |
| Table | [mgr.md#SP_mgr_mon_bytes](../../../config/mgr/mgr.md#SP_mgr_mon_bytes) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_mon_bytes 128_M
ceph config get mgr mgr_mon_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_mon_messages

| | |
|---|---|
| Type | Uint · default `128` · **Dev** |
| Table | [mgr.md#SP_mgr_mon_messages](../../../config/mgr/mgr.md#SP_mgr_mon_messages) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_mon_messages 128
ceph config get mgr mgr_mon_messages
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`128`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_osd_bytes

| | |
|---|---|
| Type | Size · default `512_M` · **Dev** |
| Table | [mgr.md#SP_mgr_osd_bytes](../../../config/mgr/mgr.md#SP_mgr_osd_bytes) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_osd_bytes 512_M
ceph config get mgr mgr_osd_bytes
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`512_M`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_osd_messages

| | |
|---|---|
| Type | Uint · default `8_K` · **Dev** |
| Table | [mgr.md#SP_mgr_osd_messages](../../../config/mgr/mgr.md#SP_mgr_osd_messages) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_osd_messages 8_K
ceph config get mgr mgr_osd_messages
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`8_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_osd_upgrade_check_convergence_factor

| | |
|---|---|
| Type | Float · default `0.8` · **Advanced** |
| Table | [mgr.md#SP_mgr_osd_upgrade_check_convergence_factor](../../../config/mgr/mgr.md#SP_mgr_osd_upgrade_check_convergence_factor) |

**What it does:** The factor used to converge to a subset of OSDs within a CRUSH bucket that can be upgraded without affecting immediate data availability.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_osd_upgrade_check_convergence_factor 0.8
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.8`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0.1`, max `0.9`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_osd_upgrade_check_convergence_factor
ceph -s
ceph mgr dump
```

---

### mgr_pool

| | |
|---|---|
| Type | Bool · default `True` · **Dev** · **STARTUP** (restart required) |
| Table | [mgr.md#SP_mgr_pool](../../../config/mgr/mgr.md#SP_mgr_pool) |

**What it does:** Allow use/creation of .mgr pool.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_pool false
ceph config get mgr mgr_pool
ceph orch restart mgr
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_service_beacon_grace

| | |
|---|---|
| Type | Float · default `1_min` · **Advanced** |
| Table | [mgr.md#SP_mgr_service_beacon_grace](../../../config/mgr/mgr.md#SP_mgr_service_beacon_grace) |

**What it does:** Period in seconds from last beacon to manager dropping state about a monitored service (RGW, rbd-mirror etc)

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_service_beacon_grace 1_min
ceph config get mgr mgr_service_beacon_grace
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_service_beacon_grace
ceph -s
ceph mgr dump
```

---

### mgr_standby_modules

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mgr.md#SP_mgr_standby_modules](../../../config/mgr/mgr.md#SP_mgr_standby_modules) |

**What it does:** Start modules in standby (redirect) mode when mgr is standby

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mgr mgr_standby_modules false
ceph config get mgr mgr_standby_modules
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_standby_modules
ceph -s
ceph mgr dump
```

---

### mgr_stats_period

| | |
|---|---|
| Type | Int · default `5` · **Basic** |
| Table | [mgr.md#SP_mgr_stats_period](../../../config/mgr/mgr.md#SP_mgr_stats_period) |

**What it does:** Period in seconds of OSD/MDS stats reports to manager

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mgr mgr_stats_period 5
ceph config get mgr mgr_stats_period
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `5` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_stats_period
ceph -s
ceph mgr dump
```

---

### mgr_stats_period_autotune

| | |
|---|---|
| Type | Bool · default `True` · **Basic** |
| Table | [mgr.md#SP_mgr_stats_period_autotune](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune) |

**What it does:** Automatically adjust mgr_stats_period based on Manager message queue depth

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mgr mgr_stats_period_autotune false
ceph config get mgr mgr_stats_period_autotune
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_stats_period_autotune
ceph -s
ceph mgr dump
```

---

### mgr_stats_period_autotune_queue_threshold

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [mgr.md#SP_mgr_stats_period_autotune_queue_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_period_autotune_queue_threshold) |

**What it does:** Message queue depth that triggers automatic increase of mgr_stats_period

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mgr mgr_stats_period_autotune_queue_threshold 100
ceph config get mgr mgr_stats_period_autotune_queue_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_stats_period_autotune_queue_threshold
ceph -s
ceph mgr dump
```

---

### mgr_stats_threshold

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [mgr.md#SP_mgr_stats_threshold](../../../config/mgr/mgr.md#SP_mgr_stats_threshold) |

**What it does:** Lowest perfcounter priority collected by mgr

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_stats_threshold 5
ceph config get mgr mgr_stats_threshold
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `11`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_stats_threshold
ceph -s
ceph mgr dump
```

---

### mgr_subinterpreter_modules

| | |
|---|---|
| Type | Str · default `0` · **Advanced** · **STARTUP** (restart required) |
| Table | [mgr.md#SP_mgr_subinterpreter_modules](../../../config/mgr/mgr.md#SP_mgr_subinterpreter_modules) |

**What it does:** List of manager modules to load in independent subinterpreters

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mgr mgr_subinterpreter_modules "example"
ceph config get mgr mgr_subinterpreter_modules
ceph orch restart mgr
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_subinterpreter_modules
ceph -s
ceph mgr dump
```

---

### mgr_test_metadata_error

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mgr.md#SP_mgr_test_metadata_error](../../../config/mgr/mgr.md#SP_mgr_test_metadata_error) |

**What it does:** Used for simulating errors during operations involving metadata.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mgr mgr_test_metadata_error true
ceph config get mgr mgr_test_metadata_error
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mgr_tick_period

| | |
|---|---|
| Type | Secs · default `2` · **Advanced** |
| Table | [mgr.md#SP_mgr_tick_period](../../../config/mgr/mgr.md#SP_mgr_tick_period) |

**What it does:** Period in seconds of beacon messages to monitor

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mgr mgr_tick_period 2
ceph config get mgr mgr_tick_period
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mgr mgr_tick_period
ceph -s
ceph mgr dump
```

---


[← Overview](../OVERVIEW.md)
