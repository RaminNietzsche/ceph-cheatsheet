# Limits & caps

OSD config deep dive — 15 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/osd/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [osd_check_max_object_name_len_on_startup](#osd_check_max_object_name_len_on_startup) | `True` | Dev | Dev |
| [osd_client_message_cap](#osd_client_message_cap) | `256` | Advanced | Performance |
| [osd_client_message_size_cap](#osd_client_message_size_cap) | `500_M` | Advanced | Performance |
| [osd_copyfrom_max_chunk](#osd_copyfrom_max_chunk) | `8_M` | Advanced | Performance |
| [osd_heartbeat_min_peers](#osd_heartbeat_min_peers) | `10` | Advanced | Performance |
| [osd_map_share_max_epochs](#osd_map_share_max_epochs) | `40` | Advanced | Performance |
| [osd_max_markdown_count](#osd_max_markdown_count) | `5` | Advanced | Performance |
| [osd_max_pgls](#osd_max_pgls) | `1_K` | Advanced | Performance |
| [osd_max_push_cost](#osd_max_push_cost) | `8_M` | Advanced | Performance |
| [osd_max_push_objects](#osd_max_push_objects) | `10` | Advanced | Performance |
| [osd_max_write_size](#osd_max_write_size) | `90` | Advanced | Performance |
| [osd_op_pq_max_tokens_per_priority](#osd_op_pq_max_tokens_per_priority) | `4_M` | Advanced | Performance |
| [osd_op_pq_min_cost](#osd_op_pq_min_cost) | `64_K` | Advanced | Performance |
| [osd_pg_epoch_max_lag_factor](#osd_pg_epoch_max_lag_factor) | `2` | Advanced | Performance |
| [set_keepcaps](#set_keepcaps) | `False` | Advanced | Performance |

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
ceph config get <daemon> <option>  # e.g. osd
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### osd_check_max_object_name_len_on_startup

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [osd.md#SP_osd_check_max_object_name_len_on_startup](../../../config/osd/osd.md#SP_osd_check_max_object_name_len_on_startup) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set osd osd_check_max_object_name_len_on_startup false
ceph config get osd osd_check_max_object_name_len_on_startup
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### osd_client_message_cap

| | |
|---|---|
| Type | Uint · default `256` · **Advanced** |
| Table | [osd.md#SP_osd_client_message_cap](../../../config/osd/osd.md#SP_osd_client_message_cap) |

**What it does:** maximum number of in-flight client requests

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_client_message_cap 256
ceph config get osd osd_client_message_cap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `256`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_client_message_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_client_message_size_cap

| | |
|---|---|
| Type | Size · default `500_M` · **Advanced** |
| Table | [osd.md#SP_osd_client_message_size_cap](../../../config/osd/osd.md#SP_osd_client_message_size_cap) |

**What it does:** maximum memory to devote to in-flight client requests

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_client_message_size_cap 500_M
ceph config get osd osd_client_message_size_cap
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `500_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_client_message_size_cap
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_copyfrom_max_chunk

| | |
|---|---|
| Type | Size · default `8_M` · **Advanced** |
| Table | [osd.md#SP_osd_copyfrom_max_chunk](../../../config/osd/osd.md#SP_osd_copyfrom_max_chunk) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_copyfrom_max_chunk 8_M
ceph config get osd osd_copyfrom_max_chunk
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_copyfrom_max_chunk
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_heartbeat_min_peers

| | |
|---|---|
| Type | Int · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_heartbeat_min_peers](../../../config/osd/osd.md#SP_osd_heartbeat_min_peers) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_heartbeat_min_peers 10
ceph config get osd osd_heartbeat_min_peers
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_heartbeat_min_peers
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_map_share_max_epochs

| | |
|---|---|
| Type | Int · default `40` · **Advanced** |
| Table | [osd.md#SP_osd_map_share_max_epochs](../../../config/osd/osd.md#SP_osd_map_share_max_epochs) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_map_share_max_epochs 40
ceph config get osd osd_map_share_max_epochs
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `40`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_map_share_max_epochs
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_markdown_count

| | |
|---|---|
| Type | Int · default `5` · **Advanced** |
| Table | [osd.md#SP_osd_max_markdown_count](../../../config/osd/osd.md#SP_osd_max_markdown_count) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_markdown_count 5
ceph config get osd osd_max_markdown_count
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `5`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_markdown_count
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_pgls

| | |
|---|---|
| Type | Uint · default `1_K` · **Advanced** |
| Table | [osd.md#SP_osd_max_pgls](../../../config/osd/osd.md#SP_osd_max_pgls) |

**What it does:** maximum number of results when listing objects in a pool

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_pgls 1_K
ceph config get osd osd_max_pgls
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `1_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_pgls
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_push_cost

| | |
|---|---|
| Type | Size · default `8_M` · **Advanced** |
| Table | [osd.md#SP_osd_max_push_cost](../../../config/osd/osd.md#SP_osd_max_push_cost) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_push_cost 8_M
ceph config get osd osd_max_push_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `8_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_push_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_push_objects

| | |
|---|---|
| Type | Uint · default `10` · **Advanced** |
| Table | [osd.md#SP_osd_max_push_objects](../../../config/osd/osd.md#SP_osd_max_push_objects) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_push_objects 10
ceph config get osd osd_max_push_objects
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_push_objects
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_max_write_size

| | |
|---|---|
| Type | Size · default `90` · **Advanced** |
| Table | [osd.md#SP_osd_max_write_size](../../../config/osd/osd.md#SP_osd_max_write_size) |

**What it does:** Maximum size of a RADOS write operation in megabytes

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_max_write_size 90
ceph config get osd osd_max_write_size
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `90`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.

**Bounds:** min `4`, max `—`.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_max_write_size
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_op_pq_max_tokens_per_priority

| | |
|---|---|
| Type | Uint · default `4_M` · **Advanced** |
| Table | [osd.md#SP_osd_op_pq_max_tokens_per_priority](../../../config/osd/osd.md#SP_osd_op_pq_max_tokens_per_priority) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_op_pq_max_tokens_per_priority 4_M
ceph config get osd osd_op_pq_max_tokens_per_priority
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `4_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_pq_max_tokens_per_priority
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_op_pq_min_cost

| | |
|---|---|
| Type | Size · default `64_K` · **Advanced** |
| Table | [osd.md#SP_osd_op_pq_min_cost](../../../config/osd/osd.md#SP_osd_op_pq_min_cost) |

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_op_pq_min_cost 64_K
ceph config get osd osd_op_pq_min_cost
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `64_K`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_op_pq_min_cost
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### osd_pg_epoch_max_lag_factor

| | |
|---|---|
| Type | Float · default `2` · **Advanced** |
| Table | [osd.md#SP_osd_pg_epoch_max_lag_factor](../../../config/osd/osd.md#SP_osd_pg_epoch_max_lag_factor) |

**What it does:** Max multiple of the map cache that PGs can lag before we throttle map injest

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set osd osd_pg_epoch_max_lag_factor 2
ceph config get osd osd_pg_epoch_max_lag_factor
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `2`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd osd_pg_epoch_max_lag_factor
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---

### set_keepcaps

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** · **STARTUP** (restart required) |
| Table | [osd.md#SP_set_keepcaps](../../../config/osd/osd.md#SP_set_keepcaps) |

**What it does:** set the keepcaps flag before changing UID, preserving the permitted capability set

**When to use:** Disabled by default; enable when you need the feature and accept its trade-offs.

**Example:**

```bash
ceph config set osd set_keepcaps true
ceph config get osd set_keepcaps
ceph orch restart osd
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `False`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get osd set_keepcaps
ceph -s
ceph daemon osd.<id> perf dump | head
ceph osd pool stats
```

---


[← Overview](../OVERVIEW.md)
