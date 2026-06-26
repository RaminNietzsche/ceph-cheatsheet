# Mon

Global config deep dive — 74 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mon_allow_pool_delete](#mon_allow_pool_delete) | `False` | Advanced | Policy |
| [mon_client_bytes](#mon_client_bytes) | `100_M` | Advanced | Performance |
| [mon_client_directed_command_retry](#mon_client_directed_command_retry) | `2` | Dev | Dev |
| [mon_client_hunt_interval](#mon_client_hunt_interval) | `3` | Advanced | Performance |
| [mon_client_hunt_interval_backoff](#mon_client_hunt_interval_backoff) | `1.5` | Advanced | Performance |
| [mon_client_hunt_interval_max_multiple](#mon_client_hunt_interval_max_multiple) | `10` | Advanced | Performance |
| [mon_client_hunt_interval_min_multiple](#mon_client_hunt_interval_min_multiple) | `1` | Advanced | Performance |
| [mon_client_hunt_on_resend](#mon_client_hunt_on_resend) | `True` | Advanced | Performance |
| [mon_client_hunt_parallel](#mon_client_hunt_parallel) | `3` | Advanced | Performance |
| [mon_client_log_interval](#mon_client_log_interval) | `1` | Advanced | Performance |
| [mon_client_max_log_entries_per_message](#mon_client_max_log_entries_per_message) | `1000` | Advanced | Performance |
| [mon_client_ping_interval](#mon_client_ping_interval) | `10` | Advanced | Performance |
| [mon_client_ping_timeout](#mon_client_ping_timeout) | `30` | Advanced | Performance |
| [mon_client_target_rank](#mon_client_target_rank) | `-1` | Advanced | Performance |
| [mon_config_key_max_entry_size](#mon_config_key_max_entry_size) | `64_K` | Advanced | Performance |
| [mon_debug_block_osdmap_trim](#mon_debug_block_osdmap_trim) | `False` | Dev | Dev |
| [mon_debug_deprecated_as_obsolete](#mon_debug_deprecated_as_obsolete) | `False` | Dev | Dev |
| [mon_debug_dump_json](#mon_debug_dump_json) | `False` | Dev | Dev |
| [mon_debug_dump_location](#mon_debug_dump_location) | `/var/log/ceph/$cluster-$name.tdump` | Dev | Dev |
| [mon_debug_dump_transactions](#mon_debug_dump_transactions) | `False` | Dev | Dev |
| [mon_debug_extra_checks](#mon_debug_extra_checks) | `False` | Dev | Dev |
| [mon_debug_no_initial_persistent_features](#mon_debug_no_initial_persistent_features) | `False` | Dev | Dev |
| [mon_debug_no_require_bluestore_for_ec_overwrites](#mon_debug_no_require_bluestore_for_ec_overwrites) | `False` | Dev | Dev |
| [mon_debug_no_require_tentacle](#mon_debug_no_require_tentacle) | `False` | Dev | Dev |
| [mon_debug_no_require_umbrella](#mon_debug_no_require_umbrella) | `False` | Dev | Dev |
| [mon_debug_unsafe_allow_tier_with_nonempty_snaps](#mon_debug_unsafe_allow_tier_with_nonempty_snaps) | `False` | Dev | Dev |
| [mon_dns_srv_name](#mon_dns_srv_name) | `ceph-mon` | Advanced | Performance |
| [mon_fake_pool_delete](#mon_fake_pool_delete) | `False` | Advanced | Performance |
| [mon_force_quorum_join](#mon_force_quorum_join) | `False` | Advanced | Performance |
| [mon_globalid_prealloc](#mon_globalid_prealloc) | `10000` | Advanced | Performance |
| [mon_host](#mon_host) | `(empty)` | Basic | Policy |
| [mon_host_override](#mon_host_override) | `(empty)` | Advanced | Performance |
| [mon_initial_members](#mon_initial_members) | `(empty)` | Advanced | Performance |
| [mon_inject_pg_merge_bounce_probability](#mon_inject_pg_merge_bounce_probability) | `0` | Dev | Dev |
| [mon_inject_sync_get_chunk_delay](#mon_inject_sync_get_chunk_delay) | `0` | Dev | Dev |
| [mon_inject_transaction_delay_max](#mon_inject_transaction_delay_max) | `10` | Dev | Dev |
| [mon_inject_transaction_delay_probability](#mon_inject_transaction_delay_probability) | `0` | Dev | Dev |
| [mon_keyvaluedb](#mon_keyvaluedb) | `rocksdb` | Advanced | Performance |
| [mon_max_log_epochs](#mon_max_log_epochs) | `500` | Advanced | Performance |
| [mon_max_mdsmap_epochs](#mon_max_mdsmap_epochs) | `500` | Advanced | Performance |
| [mon_max_mgrmap_epochs](#mon_max_mgrmap_epochs) | `500` | Advanced | Performance |
| [mon_max_nvmeof_epochs](#mon_max_nvmeof_epochs) | `500` | Advanced | Performance |
| [mon_max_osd](#mon_max_osd) | `10000` | Advanced | Performance |
| [mon_max_pg_per_osd](#mon_max_pg_per_osd) | `500` | Advanced | Performance |
| [mon_max_snap_prune_per_epoch](#mon_max_snap_prune_per_epoch) | `100` | Advanced | Performance |
| [mon_min_osdmap_epochs](#mon_min_osdmap_epochs) | `500` | Advanced | Performance |
| [mon_osd_backfillfull_ratio](#mon_osd_backfillfull_ratio) | `0.9` | Advanced | Performance |
| [mon_osd_force_trim_to](#mon_osd_force_trim_to) | `0` | Dev | Dev |
| [mon_osd_full_ratio](#mon_osd_full_ratio) | `0.95` | Advanced | Performance |
| [mon_osd_initial_require_min_compat_client](#mon_osd_initial_require_min_compat_client) | `luminous` | Advanced | Performance |
| [mon_osd_min_down_reporters](#mon_osd_min_down_reporters) | `2` | Advanced | Performance |
| [mon_osd_nearfull_ratio](#mon_osd_nearfull_ratio) | `0.85` | Advanced | Performance |
| [mon_osd_report_timeout](#mon_osd_report_timeout) | `15_min` | Advanced | Performance |
| [mon_osd_reporter_subtree_level](#mon_osd_reporter_subtree_level) | `host` | Advanced | Performance |
| [mon_osd_snap_trim_queue_warn_on](#mon_osd_snap_trim_queue_warn_on) | `32768` | Advanced | Performance |
| [mon_probe_timeout](#mon_probe_timeout) | `2` | Advanced | Performance |
| [mon_scrub_inject_crc_mismatch](#mon_scrub_inject_crc_mismatch) | `0` | Dev | Dev |
| [mon_scrub_inject_missing_keys](#mon_scrub_inject_missing_keys) | `0` | Dev | Dev |
| [mon_scrub_interval](#mon_scrub_interval) | `1_day` | Advanced | Performance |
| [mon_scrub_max_keys](#mon_scrub_max_keys) | `100` | Advanced | Performance |
| [mon_scrub_timeout](#mon_scrub_timeout) | `5_min` | Advanced | Performance |
| [mon_sync_debug](#mon_sync_debug) | `False` | Dev | Dev |
| [mon_sync_max_payload_keys](#mon_sync_max_payload_keys) | `2000` | Advanced | Performance |
| [mon_sync_max_payload_size](#mon_sync_max_payload_size) | `1_M` | Advanced | Performance |
| [mon_sync_provider_kill_at](#mon_sync_provider_kill_at) | `0` | Dev | Dev |
| [mon_sync_requester_kill_at](#mon_sync_requester_kill_at) | `0` | Dev | Dev |
| [mon_sync_timeout](#mon_sync_timeout) | `1_min` | Advanced | Performance |
| [mon_warn_on_insecure_global_id_reclaim](#mon_warn_on_insecure_global_id_reclaim) | `True` | Advanced | Performance |
| [mon_warn_on_insecure_global_id_reclaim_allowed](#mon_warn_on_insecure_global_id_reclaim_allowed) | `True` | Advanced | Policy |
| [mon_warn_on_msgr2_not_enabled](#mon_warn_on_msgr2_not_enabled) | `True` | Advanced | Policy |
| [mon_warn_on_slow_ping_ratio](#mon_warn_on_slow_ping_ratio) | `0.05` | Advanced | Performance |
| [mon_warn_on_slow_ping_time](#mon_warn_on_slow_ping_time) | `0` | Advanced | Performance |
| [mon_warn_pg_not_deep_scrubbed_ratio](#mon_warn_pg_not_deep_scrubbed_ratio) | `0.75` | Advanced | Performance |
| [mon_warn_pg_not_scrubbed_ratio](#mon_warn_pg_not_scrubbed_ratio) | `0.5` | Advanced | Performance |

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

### mon_allow_pool_delete

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_allow_pool_delete](../../../config/global/mon.md#SP_mon_allow_pool_delete) |

**What it does:** allow pool deletions

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_allow_pool_delete true
ceph config get mon mon_allow_pool_delete
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `False` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_allow_pool_delete
ceph -s
ceph mon stat
```

---

### mon_client_bytes

| | |
|---|---|
| Type | Size · default `100_M` · **Advanced** |
| Table | [mon.md#SP_mon_client_bytes](../../../config/global/mon.md#SP_mon_client_bytes) |

**What it does:** Max bytes of outstanding client messages mon will read off the network

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_client_bytes 100_M
ceph config get mon mon_client_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_bytes
ceph -s
ceph mon stat
```

---

### mon_client_directed_command_retry

| | |
|---|---|
| Type | Int · default `2` · **Dev** |
| Table | [mon.md#SP_mon_client_directed_command_retry](../../../config/global/mon.md#SP_mon_client_directed_command_retry) |

**What it does:** Number of times to try sending a command directed at a specific Monitor

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_client_directed_command_retry 2
ceph config get mon mon_client_directed_command_retry
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`2`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_client_hunt_interval

| | |
|---|---|
| Type | Float · default `3` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_interval](../../../config/global/mon.md#SP_mon_client_hunt_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_client_hunt_interval 3
ceph config get mon mon_client_hunt_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_interval
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_backoff

| | |
|---|---|
| Type | Float · default `1.5` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_interval_backoff](../../../config/global/mon.md#SP_mon_client_hunt_interval_backoff) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_client_hunt_interval_backoff 1.5
ceph config get mon mon_client_hunt_interval_backoff
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_interval_backoff
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_max_multiple

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_interval_max_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_max_multiple) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_client_hunt_interval_max_multiple 10
ceph config get mon mon_client_hunt_interval_max_multiple
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_interval_max_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_interval_min_multiple

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_interval_min_multiple](../../../config/global/mon.md#SP_mon_client_hunt_interval_min_multiple) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_client_hunt_interval_min_multiple 1
ceph config get mon mon_client_hunt_interval_min_multiple
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_interval_min_multiple
ceph -s
ceph mon stat
```

---

### mon_client_hunt_on_resend

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_on_resend](../../../config/global/mon.md#SP_mon_client_hunt_on_resend) |

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_client_hunt_on_resend false
ceph config get mon mon_client_hunt_on_resend
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_on_resend
ceph -s
ceph mon stat
```

---

### mon_client_hunt_parallel

| | |
|---|---|
| Type | Uint · default `3` · **Advanced** |
| Table | [mon.md#SP_mon_client_hunt_parallel](../../../config/global/mon.md#SP_mon_client_hunt_parallel) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_client_hunt_parallel 3
ceph config get mon mon_client_hunt_parallel
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `3`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_hunt_parallel
ceph -s
ceph mon stat
```

---

### mon_client_log_interval

| | |
|---|---|
| Type | Float · default `1` · **Advanced** |
| Table | [mon.md#SP_mon_client_log_interval](../../../config/global/mon.md#SP_mon_client_log_interval) |

**What it does:** How frequently we send queued cluster log messages to the Monitors

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_client_log_interval 1
ceph config get mon mon_client_log_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_log_interval
ceph -s
ceph mon stat
```

---

### mon_client_max_log_entries_per_message

| | |
|---|---|
| Type | Int · default `1000` · **Advanced** |
| Table | [mon.md#SP_mon_client_max_log_entries_per_message](../../../config/global/mon.md#SP_mon_client_max_log_entries_per_message) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_client_max_log_entries_per_message 1000
ceph config get mon mon_client_max_log_entries_per_message
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_max_log_entries_per_message
ceph -s
ceph mon stat
```

---

### mon_client_ping_interval

| | |
|---|---|
| Type | Float · default `10` · **Advanced** |
| Table | [mon.md#SP_mon_client_ping_interval](../../../config/global/mon.md#SP_mon_client_ping_interval) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_client_ping_interval 10
ceph config get mon mon_client_ping_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_ping_interval
ceph -s
ceph mon stat
```

---

### mon_client_ping_timeout

| | |
|---|---|
| Type | Float · default `30` · **Advanced** |
| Table | [mon.md#SP_mon_client_ping_timeout](../../../config/global/mon.md#SP_mon_client_ping_timeout) |

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_client_ping_timeout 30
ceph config get mon mon_client_ping_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `30`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_ping_timeout
ceph -s
ceph mon stat
```

---

### mon_client_target_rank

| | |
|---|---|
| Type | Int · default `-1` · **Advanced** |
| Table | [mon.md#SP_mon_client_target_rank](../../../config/global/mon.md#SP_mon_client_target_rank) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_client_target_rank 128
ceph config get mon mon_client_target_rank
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `-1`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `-1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_client_target_rank
ceph -s
ceph mon stat
```

---

### mon_config_key_max_entry_size

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [mon.md#SP_mon_config_key_max_entry_size](../../../config/global/mon.md#SP_mon_config_key_max_entry_size) |

**What it does:** Defines the number of bytes allowed to be held in a single config-key entry

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_config_key_max_entry_size 64_K
ceph config get mon mon_config_key_max_entry_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_config_key_max_entry_size
ceph -s
ceph mon stat
```

---

### mon_debug_block_osdmap_trim

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_block_osdmap_trim](../../../config/global/mon.md#SP_mon_debug_block_osdmap_trim) |

**What it does:** Block OSDMap trimming while the option is enabled. Blocking OSDMap trimming may be quite helpful to easily reproduce states in which the monitor keeps (hundreds of) thousands of osdmaps.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_block_osdmap_trim true
ceph config get mon mon_debug_block_osdmap_trim
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_deprecated_as_obsolete

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_deprecated_as_obsolete](../../../config/global/mon.md#SP_mon_debug_deprecated_as_obsolete) |

**What it does:** Treat deprecated mon commands as obsolete

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_deprecated_as_obsolete true
ceph config get mon mon_debug_deprecated_as_obsolete
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_dump_json

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_dump_json](../../../config/global/mon.md#SP_mon_debug_dump_json) |

**What it does:** Dump paxos transasctions to log as JSON

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`mon_debug_dump_transactions`](../../../config/global/mon.md#SP_mon_debug_dump_transactions)

**Example:**

```bash
ceph config set mon mon_debug_dump_json true
ceph config get mon mon_debug_dump_json
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_dump_location

| | |
|---|---|
| Type | Str · default `/var/log/ceph/$cluster-$name.tdump` · **Dev** |
| Table | [mon.md#SP_mon_debug_dump_location](../../../config/global/mon.md#SP_mon_debug_dump_location) |

**What it does:** File to which to dump Paxos transactions

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`mon_debug_dump_transactions`](../../../config/global/mon.md#SP_mon_debug_dump_transactions)

**Example:**

```bash
ceph config set mon mon_debug_dump_location "/var/log/ceph/$cluster-$name.tdump"
ceph config get mon mon_debug_dump_location
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`/var/log/ceph/$cluster-$name.tdump`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_dump_transactions

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_dump_transactions](../../../config/global/mon.md#SP_mon_debug_dump_transactions) |

**What it does:** Dump Paxos transactions to log

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Related options:**

- [`mon_debug_dump_location`](../../../config/global/mon.md#SP_mon_debug_dump_location)

**Example:**

```bash
ceph config set mon mon_debug_dump_transactions true
ceph config get mon mon_debug_dump_transactions
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_extra_checks

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_extra_checks](../../../config/global/mon.md#SP_mon_debug_extra_checks) |

**What it does:** Enable some additional monitor checks Enable some additional monitor checks that would be too expensive to run on production systems, or would only be relevant while testing or debugging.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_extra_checks true
ceph config get mon mon_debug_extra_checks
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_no_initial_persistent_features

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_no_initial_persistent_features](../../../config/global/mon.md#SP_mon_debug_no_initial_persistent_features) |

**What it does:** Do not set any monmap features for new Monitor clusters

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_no_initial_persistent_features true
ceph config get mon mon_debug_no_initial_persistent_features
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_no_require_bluestore_for_ec_overwrites

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites](../../../config/global/mon.md#SP_mon_debug_no_require_bluestore_for_ec_overwrites) |

**What it does:** Do not require BlueStore OSDs to enable EC overwrites within a RADOS pool

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_no_require_bluestore_for_ec_overwrites true
ceph config get mon mon_debug_no_require_bluestore_for_ec_overwrites
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_no_require_tentacle

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_no_require_tentacle](../../../config/global/mon.md#SP_mon_debug_no_require_tentacle) |

**What it does:** Do not require the Tentacle feature for new Monitor clusters

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_no_require_tentacle true
ceph config get mon mon_debug_no_require_tentacle
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_no_require_umbrella

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_no_require_umbrella](../../../config/global/mon.md#SP_mon_debug_no_require_umbrella) |

**What it does:** Do not require the Umbrella feature for new Monitor clusters

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_no_require_umbrella true
ceph config get mon mon_debug_no_require_umbrella
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_debug_unsafe_allow_tier_with_nonempty_snaps

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps](../../../config/global/mon.md#SP_mon_debug_unsafe_allow_tier_with_nonempty_snaps) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_debug_unsafe_allow_tier_with_nonempty_snaps true
ceph config get mon mon_debug_unsafe_allow_tier_with_nonempty_snaps
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_dns_srv_name

| | |
|---|---|
| Type | Str · default `ceph-mon` · **Advanced** · **STARTUP** (restart required) |
| Table | [mon.md#SP_mon_dns_srv_name](../../../config/global/mon.md#SP_mon_dns_srv_name) |

**What it does:** Name of DNS SRV record to check for monitor addresses

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_host`](../../../config/global/mon.md#SP_mon_host)

**Example:**

```bash
ceph config set mon mon_dns_srv_name "ceph-mon"
ceph config get mon mon_dns_srv_name
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `ceph-mon`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_dns_srv_name
ceph -s
ceph mon stat
```

---

### mon_fake_pool_delete

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_fake_pool_delete](../../../config/global/mon.md#SP_mon_fake_pool_delete) |

**What it does:** Fake pool deletions by renaming the RADOS pool

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_fake_pool_delete true
ceph config get mon mon_fake_pool_delete
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_fake_pool_delete
ceph -s
ceph mon stat
```

---

### mon_force_quorum_join

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [mon.md#SP_mon_force_quorum_join](../../../config/global/mon.md#SP_mon_force_quorum_join) |

**What it does:** Force a Monitor to rejoin the quorum even though it was just removed

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set mon mon_force_quorum_join true
ceph config get mon mon_force_quorum_join
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_force_quorum_join
ceph -s
ceph mon stat
```

---

### mon_globalid_prealloc

| | |
|---|---|
| Type | Uint · default `10000` · **Advanced** |
| Table | [mon.md#SP_mon_globalid_prealloc](../../../config/global/mon.md#SP_mon_globalid_prealloc) |

**What it does:** number of globalid values to preallocate This setting caps how many new clients can authenticate with the cluster before the monitors have to perform a write to preallocate more. Large values burn through the 64-bit ID space more quickly.

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_globalid_prealloc 10000
ceph config get mon mon_globalid_prealloc
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_globalid_prealloc
ceph -s
ceph mon stat
```

---

### mon_host

| | |
|---|---|
| Type | Str · default `(empty)` · **Basic** · **STARTUP** (restart required) |
| Table | [mon.md#SP_mon_host](../../../config/global/mon.md#SP_mon_host) |

**What it does:** List of hosts or addresses to search for a monitor This is a list of IP addresses or hostnames that are separated by commas, whitespace, or semicolons. Hostnames are resolved via DNS. All A and AAAA records are included in the search list.

**When to use:** Core Global behavior — review before changing in production.

**Example:**

```bash
ceph config set mon mon_host "example"
ceph config get mon mon_host
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `(empty)` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_host
ceph -s
ceph mon stat
```

---

### mon_host_override

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** · **STARTUP** (restart required) |
| Table | [mon.md#SP_mon_host_override](../../../config/global/mon.md#SP_mon_host_override) |

**What it does:** Monitor(s) to use overriding the MonMap

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_host_override "example"
ceph config get mon mon_host_override
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_host_override
ceph -s
ceph mon stat
```

---

### mon_initial_members

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [mon.md#SP_mon_initial_members](../../../config/global/mon.md#SP_mon_initial_members) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_initial_members "example"
ceph config get mon mon_initial_members
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `(empty)`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_initial_members
ceph -s
ceph mon stat
```

---

### mon_inject_pg_merge_bounce_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mon.md#SP_mon_inject_pg_merge_bounce_probability](../../../config/global/mon.md#SP_mon_inject_pg_merge_bounce_probability) |

**What it does:** Probability of failing and reverting a pg_num decrement

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_inject_pg_merge_bounce_probability 0
ceph config get mon mon_inject_pg_merge_bounce_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_inject_sync_get_chunk_delay

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mon.md#SP_mon_inject_sync_get_chunk_delay](../../../config/global/mon.md#SP_mon_inject_sync_get_chunk_delay) |

**What it does:** Inject delay during Monitor sync (seconds)

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_inject_sync_get_chunk_delay 0
ceph config get mon mon_inject_sync_get_chunk_delay
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_inject_transaction_delay_max

| | |
|---|---|
| Type | Float · default `10` · **Dev** |
| Table | [mon.md#SP_mon_inject_transaction_delay_max](../../../config/global/mon.md#SP_mon_inject_transaction_delay_max) |

**What it does:** Max duration of injected delay in Paxos

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_inject_transaction_delay_max 10
ceph config get mon mon_inject_transaction_delay_max
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`10`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_inject_transaction_delay_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mon.md#SP_mon_inject_transaction_delay_probability](../../../config/global/mon.md#SP_mon_inject_transaction_delay_probability) |

**What it does:** Probability of injecting a delay in Paxos

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_inject_transaction_delay_probability 0
ceph config get mon mon_inject_transaction_delay_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_keyvaluedb

| | |
|---|---|
| Type | Str · enum: ["rocksdb"] · default `rocksdb` · **Advanced** |
| Table | [mon.md#SP_mon_keyvaluedb](../../../config/global/mon.md#SP_mon_keyvaluedb) |

**What it does:** Database backend to use for the Monitor database

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_keyvaluedb rocksdb
ceph config get mon mon_keyvaluedb
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `rocksdb`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_keyvaluedb
ceph -s
ceph mon stat
```

---

### mon_max_log_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_max_log_epochs](../../../config/global/mon.md#SP_mon_max_log_epochs) |

**What it does:** Max number of past cluster log epochs to store

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_log_epochs 500
ceph config get mon mon_max_log_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_log_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mdsmap_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_max_mdsmap_epochs](../../../config/global/mon.md#SP_mon_max_mdsmap_epochs) |

**What it does:** Max number of FSMaps/MDSMaps to store

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_mdsmap_epochs 500
ceph config get mon mon_max_mdsmap_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_mdsmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_mgrmap_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_max_mgrmap_epochs](../../../config/global/mon.md#SP_mon_max_mgrmap_epochs) |

**What it does:** Max number of MgrMaps to store

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_mgrmap_epochs 500
ceph config get mon mon_max_mgrmap_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_mgrmap_epochs
ceph -s
ceph mon stat
```

---

### mon_max_nvmeof_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_max_nvmeof_epochs](../../../config/global/mon.md#SP_mon_max_nvmeof_epochs) |

**What it does:** Max number of NVMeoF gateway maps to store

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_nvmeof_epochs 500
ceph config get mon mon_max_nvmeof_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_nvmeof_epochs
ceph -s
ceph mon stat
```

---

### mon_max_osd

| | |
|---|---|
| Type | Int · default `10000` · **Advanced** |
| Table | [mon.md#SP_mon_max_osd](../../../config/global/mon.md#SP_mon_max_osd) |

**What it does:** Max number of OSDs in a cluster

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_osd 10000
ceph config get mon mon_max_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_osd
ceph -s
ceph mon stat
```

---

### mon_max_pg_per_osd

| | |
|---|---|
| Type | Uint · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_max_pg_per_osd](../../../config/global/mon.md#SP_mon_max_pg_per_osd) |

**What it does:** Max number of PGs per OSD the cluster will allow If the number of PGs per OSD exceeds this, a health warning will be visible in `ceph status`. This is also used in automated PG management, as the threshold at which some pools' pg_num may be shrunk in order to enable increasing the pg_num of others.

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_pg_per_osd 500
ceph config get mon mon_max_pg_per_osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `1`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_pg_per_osd
ceph -s
ceph mon stat
```

---

### mon_max_snap_prune_per_epoch

| | |
|---|---|
| Type | Uint · default `100` · **Advanced** |
| Table | [mon.md#SP_mon_max_snap_prune_per_epoch](../../../config/global/mon.md#SP_mon_max_snap_prune_per_epoch) |

**What it does:** Max number of pruned snaps we will process in a single OSDMap epoch

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_max_snap_prune_per_epoch 100
ceph config get mon mon_max_snap_prune_per_epoch
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_max_snap_prune_per_epoch
ceph -s
ceph mon stat
```

---

### mon_min_osdmap_epochs

| | |
|---|---|
| Type | Int · default `500` · **Advanced** |
| Table | [mon.md#SP_mon_min_osdmap_epochs](../../../config/global/mon.md#SP_mon_min_osdmap_epochs) |

**What it does:** Min number of OSDMaps to store

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_min_osdmap_epochs 500
ceph config get mon mon_min_osdmap_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_min_osdmap_epochs
ceph -s
ceph mon stat
```

---

### mon_osd_backfillfull_ratio

| | |
|---|---|
| Type | Float · default `0.9` · **Advanced** |
| Table | [mon.md#SP_mon_osd_backfillfull_ratio](../../../config/global/mon.md#SP_mon_osd_backfillfull_ratio) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_backfillfull_ratio 0.9
ceph config get mon mon_osd_backfillfull_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.9`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_backfillfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_force_trim_to

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mon.md#SP_mon_osd_force_trim_to](../../../config/global/mon.md#SP_mon_osd_force_trim_to) |

**What it does:** Force Monitors to trim osdmaps through this epoch

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_osd_force_trim_to 64
ceph config get mon mon_osd_force_trim_to
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_osd_full_ratio

| | |
|---|---|
| Type | Float · default `0.95` · **Advanced** |
| Table | [mon.md#SP_mon_osd_full_ratio](../../../config/global/mon.md#SP_mon_osd_full_ratio) |

**What it does:** Full ratio of OSDs to be set during initial creation of the cluster

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_full_ratio 0.95
ceph config get mon mon_osd_full_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.95`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_full_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_initial_require_min_compat_client

| | |
|---|---|
| Type | Str · default `luminous` · **Advanced** |
| Table | [mon.md#SP_mon_osd_initial_require_min_compat_client](../../../config/global/mon.md#SP_mon_osd_initial_require_min_compat_client) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_osd_initial_require_min_compat_client luminous
ceph config get mon mon_osd_initial_require_min_compat_client
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `luminous`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_initial_require_min_compat_client
ceph -s
ceph mon stat
```

---

### mon_osd_min_down_reporters

| | |
|---|---|
| Type | Uint · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_osd_min_down_reporters](../../../config/global/mon.md#SP_mon_osd_min_down_reporters) |

**What it does:** Number of OSDs from different subtrees who need to report a down OSD for it to count

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Related options:**

- [`mon_osd_reporter_subtree_level`](../../../config/global/mon.md#SP_mon_osd_reporter_subtree_level)

**Example:**

```bash
ceph config set mon mon_osd_min_down_reporters 2
ceph config get mon mon_osd_min_down_reporters
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_min_down_reporters
ceph -s
ceph mon stat
```

---

### mon_osd_nearfull_ratio

| | |
|---|---|
| Type | Float · default `0.85` · **Advanced** |
| Table | [mon.md#SP_mon_osd_nearfull_ratio](../../../config/global/mon.md#SP_mon_osd_nearfull_ratio) |

**What it does:** Nearfull ratio for OSDs to be set during initial creation of cluster

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_nearfull_ratio 0.85
ceph config get mon mon_osd_nearfull_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.85`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_nearfull_ratio
ceph -s
ceph mon stat
```

---

### mon_osd_report_timeout

| | |
|---|---|
| Type | Int · default `15_min` · **Advanced** |
| Table | [mon.md#SP_mon_osd_report_timeout](../../../config/global/mon.md#SP_mon_osd_report_timeout) |

**What it does:** Time before OSDs who do not report to the mons are marked down (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_osd_report_timeout 15_min
ceph config get mon mon_osd_report_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `15_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_report_timeout
ceph -s
ceph mon stat
```

---

### mon_osd_reporter_subtree_level

| | |
|---|---|
| Type | Str · default `host` · **Advanced** |
| Table | [mon.md#SP_mon_osd_reporter_subtree_level](../../../config/global/mon.md#SP_mon_osd_reporter_subtree_level) |

**What it does:** At which level of parent bucket the reporters are counted

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_reporter_subtree_level host
ceph config get mon mon_osd_reporter_subtree_level
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `host`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_reporter_subtree_level
ceph -s
ceph mon stat
```

---

### mon_osd_snap_trim_queue_warn_on

| | |
|---|---|
| Type | Int · default `32768` · **Advanced** |
| Table | [mon.md#SP_mon_osd_snap_trim_queue_warn_on](../../../config/global/mon.md#SP_mon_osd_snap_trim_queue_warn_on) |

**What it does:** Warn when snap trim queue reaches or exceeds this value Warn when snap trim queue length for at least one PG crosses this value, as this is indicator of snap trimmer not keeping up, wasting disk space

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_osd_snap_trim_queue_warn_on 32768
ceph config get mon mon_osd_snap_trim_queue_warn_on
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `32768`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_osd_snap_trim_queue_warn_on
ceph -s
ceph mon stat
```

---

### mon_probe_timeout

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [mon.md#SP_mon_probe_timeout](../../../config/global/mon.md#SP_mon_probe_timeout) |

**What it does:** Timeout for querying other mons during bootstrap pre-election phase (seconds)

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_probe_timeout 2
ceph config get mon mon_probe_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_probe_timeout
ceph -s
ceph mon stat
```

---

### mon_scrub_inject_crc_mismatch

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mon.md#SP_mon_scrub_inject_crc_mismatch](../../../config/global/mon.md#SP_mon_scrub_inject_crc_mismatch) |

**What it does:** Probability for injecting crc mismatches into mon scrub

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_scrub_inject_crc_mismatch 0
ceph config get mon mon_scrub_inject_crc_mismatch
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_scrub_inject_missing_keys

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mon.md#SP_mon_scrub_inject_missing_keys](../../../config/global/mon.md#SP_mon_scrub_inject_missing_keys) |

**What it does:** Probability for injecting missing keys into mon scrub

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_scrub_inject_missing_keys 0
ceph config get mon mon_scrub_inject_missing_keys
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_scrub_interval

| | |
|---|---|
| Type | Secs · default `1_day` · **Advanced** |
| Table | [mon.md#SP_mon_scrub_interval](../../../config/global/mon.md#SP_mon_scrub_interval) |

**What it does:** Frequency for scrubbing the Monitor database

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_scrub_interval 1_day
ceph config get mon mon_scrub_interval
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_day`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_scrub_interval
ceph -s
ceph mon stat
```

---

### mon_scrub_max_keys

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [mon.md#SP_mon_scrub_max_keys](../../../config/global/mon.md#SP_mon_scrub_max_keys) |

**What it does:** Max keys per on scrub chunk/step

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_scrub_max_keys 100
ceph config get mon mon_scrub_max_keys
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_scrub_max_keys
ceph -s
ceph mon stat
```

---

### mon_scrub_timeout

| | |
|---|---|
| Type | Int · default `5_min` · **Advanced** |
| Table | [mon.md#SP_mon_scrub_timeout](../../../config/global/mon.md#SP_mon_scrub_timeout) |

**What it does:** Timeout to restart scrub of mon quorum participant does not respond for the latest chunk

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_scrub_timeout 5_min
ceph config get mon mon_scrub_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_scrub_timeout
ceph -s
ceph mon stat
```

---

### mon_sync_debug

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mon.md#SP_mon_sync_debug](../../../config/global/mon.md#SP_mon_sync_debug) |

**What it does:** Enable extra debugging during mon sync

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_sync_debug true
ceph config get mon mon_sync_debug
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_sync_max_payload_keys

| | |
|---|---|
| Type | Int · default `2000` · **Advanced** |
| Table | [mon.md#SP_mon_sync_max_payload_keys](../../../config/global/mon.md#SP_mon_sync_max_payload_keys) |

**What it does:** Target max keys in message payload for Monitor sync

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_sync_max_payload_keys 2000
ceph config get mon mon_sync_max_payload_keys
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2000`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_sync_max_payload_keys
ceph -s
ceph mon stat
```

---

### mon_sync_max_payload_size

| | |
|---|---|
| Type | Size · default `1_M` · **Advanced** |
| Table | [mon.md#SP_mon_sync_max_payload_size](../../../config/global/mon.md#SP_mon_sync_max_payload_size) |

**What it does:** Target max message payload for mon sync

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set mon mon_sync_max_payload_size 1_M
ceph config get mon mon_sync_max_payload_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_sync_max_payload_size
ceph -s
ceph mon stat
```

---

### mon_sync_provider_kill_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mon.md#SP_mon_sync_provider_kill_at](../../../config/global/mon.md#SP_mon_sync_provider_kill_at) |

**What it does:** Kill mon sync provider at specific point

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_sync_provider_kill_at 64
ceph config get mon mon_sync_provider_kill_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_sync_requester_kill_at

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [mon.md#SP_mon_sync_requester_kill_at](../../../config/global/mon.md#SP_mon_sync_requester_kill_at) |

**What it does:** Kill mon sync requestor at specific point

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mon mon_sync_requester_kill_at 64
ceph config get mon mon_sync_requester_kill_at
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mon_sync_timeout

| | |
|---|---|
| Type | Float · default `1_min` · **Advanced** |
| Table | [mon.md#SP_mon_sync_timeout](../../../config/global/mon.md#SP_mon_sync_timeout) |

**What it does:** Timeout before canceling sync if syncing mon does not respond

**When to use:** Tune background work timing — balance freshness vs cluster load.

**Example:**

```bash
ceph config set mon mon_sync_timeout 1_min
ceph config get mon mon_sync_timeout
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_min`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_sync_timeout
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim) |

**What it does:** Raise the AUTH_INSECURE_GLOBAL_ID_RECLAIM health warning if any connected clients are insecurely reclaiming global_ids

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim false
ceph config get mon mon_warn_on_insecure_global_id_reclaim
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `True`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim
ceph -s
ceph mon stat
```

---

### mon_warn_on_insecure_global_id_reclaim_allowed

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed](../../../config/global/mon.md#SP_mon_warn_on_insecure_global_id_reclaim_allowed) |

**What it does:** issue AUTH_INSECURE_GLOBAL_ID_RECLAIM_ALLOWED health warning if insecure global_id reclaim is allowed

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_insecure_global_id_reclaim_allowed false
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_insecure_global_id_reclaim_allowed
ceph -s
ceph mon stat
```

---

### mon_warn_on_msgr2_not_enabled

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_msgr2_not_enabled](../../../config/global/mon.md#SP_mon_warn_on_msgr2_not_enabled) |

**What it does:** Raise the MON_MSGR2_NOT_ENABLED health warning if monitors are all running Nautilus but not all binding to a msgr2 port

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set mon mon_warn_on_msgr2_not_enabled false
ceph config get mon mon_warn_on_msgr2_not_enabled
```

**Finding optimal value:**

**Tuning model:** Policy

1. Document why `True` is correct for your policy.
2. Change only for compatibility or security requirements.
3. Test client and admin workflows after changes.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_msgr2_not_enabled
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_ratio

| | |
|---|---|
| Type | Float · default `0.05` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_slow_ping_ratio](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_ratio) |

**What it does:** Issue a health warning if heartbeat ping longer than percentage of osd_heartbeat_grace

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_warn_on_slow_ping_ratio 0.05
ceph config get mon mon_warn_on_slow_ping_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.05`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_slow_ping_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_on_slow_ping_time

| | |
|---|---|
| Type | Float · default `0` · **Advanced** |
| Table | [mon.md#SP_mon_warn_on_slow_ping_time](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_time) |

**What it does:** Override mon_warn_on_slow_ping_ratio with specified threshold in milliseconds

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Related options:**

- [`mon_warn_on_slow_ping_ratio`](../../../config/global/mon.md#SP_mon_warn_on_slow_ping_ratio)

**Example:**

```bash
ceph config set mon mon_warn_on_slow_ping_time 0
ceph config get mon mon_warn_on_slow_ping_time
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_on_slow_ping_time
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_deep_scrubbed_ratio

| | |
|---|---|
| Type | Float · default `0.75` · **Advanced** |
| Table | [mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_deep_scrubbed_ratio) |

**What it does:** Percentage of the deep scrub interval past the deep scrub interval to warn - Set this configurable with the command "ceph config set mgr mon_warn_pg_not_deep_scrubbed_ratio <ratio_value>"

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_warn_pg_not_deep_scrubbed_ratio 0.75
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.75`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_pg_not_deep_scrubbed_ratio
ceph -s
ceph mon stat
```

---

### mon_warn_pg_not_scrubbed_ratio

| | |
|---|---|
| Type | Float · default `0.5` · **Advanced** |
| Table | [mon.md#SP_mon_warn_pg_not_scrubbed_ratio](../../../config/global/mon.md#SP_mon_warn_pg_not_scrubbed_ratio) |

**What it does:** Raise a health warning when shallow scrubs are delayed by this percentage of the shallow scrub interval. Note that this must be set at mgr or with global scope. Set this configurable with the command "ceph config set mgr mon_warn_pg_not_scrubbed_ratio <ratio_value>".

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set mon mon_warn_pg_not_scrubbed_ratio 0.5
ceph config get mon mon_warn_pg_not_scrubbed_ratio
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `0.5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `0`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get mon mon_warn_pg_not_scrubbed_ratio
ceph -s
ceph mon stat
```

---


[← Overview](../OVERVIEW.md)
