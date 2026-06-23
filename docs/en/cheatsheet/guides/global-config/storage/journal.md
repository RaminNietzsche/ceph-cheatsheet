# Journal

Global config deep dive — 17 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [journal_aio](#journal_aio) | `True` | Dev | Dev |
| [journal_align_min_size](#journal_align_min_size) | `64_K` | Dev | Dev |
| [journal_block_align](#journal_block_align) | `True` | Dev | Dev |
| [journal_block_size](#journal_block_size) | `4_K` | Dev | Dev |
| [journal_dio](#journal_dio) | `True` | Dev | Dev |
| [journal_discard](#journal_discard) | `False` | Dev | Dev |
| [journal_force_aio](#journal_force_aio) | `False` | Dev | Dev |
| [journal_ignore_corruption](#journal_ignore_corruption) | `False` | Dev | Dev |
| [journal_max_write_bytes](#journal_max_write_bytes) | `10_M` | Advanced | Performance |
| [journal_max_write_entries](#journal_max_write_entries) | `100` | Advanced | Performance |
| [journal_replay_from](#journal_replay_from) | `0` | Dev | Dev |
| [journal_throttle_high_multiple](#journal_throttle_high_multiple) | `0` | Dev | Dev |
| [journal_throttle_high_threshhold](#journal_throttle_high_threshhold) | `0.9` | Dev | Dev |
| [journal_throttle_low_threshhold](#journal_throttle_low_threshhold) | `0.6` | Dev | Dev |
| [journal_throttle_max_multiple](#journal_throttle_max_multiple) | `0` | Dev | Dev |
| [journal_write_header_frequency](#journal_write_header_frequency) | `0` | Dev | Dev |
| [journal_zero_on_create](#journal_zero_on_create) | `False` | Dev | Dev |

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

### journal_aio

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [journal.md#SP_journal_aio](../../../config/global/journal.md#SP_journal_aio) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_aio false
ceph config get global journal_aio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_align_min_size

| | |
|---|---|
| Type | Size · default `64_K` · **Dev** |
| Table | [journal.md#SP_journal_align_min_size](../../../config/global/journal.md#SP_journal_align_min_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_align_min_size 64_K
ceph config get global journal_align_min_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`64_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_block_align

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [journal.md#SP_journal_block_align](../../../config/global/journal.md#SP_journal_block_align) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_block_align false
ceph config get global journal_block_align
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_block_size

| | |
|---|---|
| Type | Size · default `4_K` · **Dev** |
| Table | [journal.md#SP_journal_block_size](../../../config/global/journal.md#SP_journal_block_size) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_block_size 4_K
ceph config get global journal_block_size
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`4_K`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_dio

| | |
|---|---|
| Type | Bool · default `True` · **Dev** |
| Table | [journal.md#SP_journal_dio](../../../config/global/journal.md#SP_journal_dio) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_dio false
ceph config get global journal_dio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`True`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_discard

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [journal.md#SP_journal_discard](../../../config/global/journal.md#SP_journal_discard) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_discard true
ceph config get global journal_discard
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_force_aio

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [journal.md#SP_journal_force_aio](../../../config/global/journal.md#SP_journal_force_aio) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_force_aio true
ceph config get global journal_force_aio
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_ignore_corruption

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [journal.md#SP_journal_ignore_corruption](../../../config/global/journal.md#SP_journal_ignore_corruption) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_ignore_corruption true
ceph config get global journal_ignore_corruption
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_max_write_bytes

| | |
|---|---|
| Type | Size · default `10_M` · **Advanced** |
| Table | [journal.md#SP_journal_max_write_bytes](../../../config/global/journal.md#SP_journal_max_write_bytes) |

**What it does:** Max bytes in flight to journal

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global journal_max_write_bytes 10_M
ceph config get global journal_max_write_bytes
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `10_M`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global journal_max_write_bytes
ceph -s
```

---

### journal_max_write_entries

| | |
|---|---|
| Type | Int · default `100` · **Advanced** |
| Table | [journal.md#SP_journal_max_write_entries](../../../config/global/journal.md#SP_journal_max_write_entries) |

**What it does:** Max IOs in flight to journal (deprecated)

**When to use:** Adjust when hitting resource limits or protecting cluster capacity.

**Example:**

```bash
ceph config set global journal_max_write_entries 100
ceph config get global journal_max_write_entries
```

**Finding optimal value:**

**Tuning model:** Performance

1. Baseline at upstream default `100`.
2. Change **one** option per test window under representative load.
3. Compare latency, throughput, and background work before/after.
4. Roll back if health degrades or slow ops increase.
**Signals:** `ceph -s`, slow ops, daemon perf counters, recovery/scrub backlog.

```bash
ceph config get global journal_max_write_entries
ceph -s
```

---

### journal_replay_from

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [journal.md#SP_journal_replay_from](../../../config/global/journal.md#SP_journal_replay_from) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_replay_from 64
ceph config get global journal_replay_from
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_throttle_high_multiple

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [journal.md#SP_journal_throttle_high_multiple](../../../config/global/journal.md#SP_journal_throttle_high_multiple) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_throttle_high_multiple 0
ceph config get global journal_throttle_high_multiple
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_throttle_high_threshhold

| | |
|---|---|
| Type | Float · default `0.9` · **Dev** |
| Table | [journal.md#SP_journal_throttle_high_threshhold](../../../config/global/journal.md#SP_journal_throttle_high_threshhold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_throttle_high_threshhold 0.9
ceph config get global journal_throttle_high_threshhold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.9`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_throttle_low_threshhold

| | |
|---|---|
| Type | Float · default `0.6` · **Dev** |
| Table | [journal.md#SP_journal_throttle_low_threshhold](../../../config/global/journal.md#SP_journal_throttle_low_threshhold) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_throttle_low_threshhold 0.6
ceph config get global journal_throttle_low_threshhold
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.6`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_throttle_max_multiple

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [journal.md#SP_journal_throttle_max_multiple](../../../config/global/journal.md#SP_journal_throttle_max_multiple) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_throttle_max_multiple 0
ceph config get global journal_throttle_max_multiple
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_write_header_frequency

| | |
|---|---|
| Type | Uint · default `0` · **Dev** |
| Table | [journal.md#SP_journal_write_header_frequency](../../../config/global/journal.md#SP_journal_write_header_frequency) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_write_header_frequency 64
ceph config get global journal_write_header_frequency
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### journal_zero_on_create

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [journal.md#SP_journal_zero_on_create](../../../config/global/journal.md#SP_journal_zero_on_create) |

**What it does:** Deprecated

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global journal_zero_on_create true
ceph config get global journal_zero_on_create
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
