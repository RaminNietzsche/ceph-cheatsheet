# Debug

MDS config deep dive — 9 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/mds/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [mds_debug_frag](#mds_debug_frag) | `False` | Dev | Dev |
| [mds_debug_scatterstat](#mds_debug_scatterstat) | `False` | Dev | Dev |
| [mds_debug_subtrees](#mds_debug_subtrees) | `False` | Dev | Dev |
| [mds_inject_health_dummy](#mds_inject_health_dummy) | `False` | Dev | Dev |
| [mds_inject_journal_corrupt_dentry_first](#mds_inject_journal_corrupt_dentry_first) | `0.0` | Dev | Dev |
| [mds_inject_migrator_session_race](#mds_inject_migrator_session_race) | `False` | Dev | Dev |
| [mds_inject_rename_corrupt_dentry_first](#mds_inject_rename_corrupt_dentry_first) | `0.0` | Dev | Dev |
| [mds_inject_skip_replaying_inotable](#mds_inject_skip_replaying_inotable) | `False` | Dev | Dev |
| [mds_inject_traceless_reply_probability](#mds_inject_traceless_reply_probability) | `0` | Dev | Dev |

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
ceph config get <daemon> <option>  # e.g. mds
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### mds_debug_frag

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_debug_frag](../../../config/mds/mds.md#SP_mds_debug_frag) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_debug_frag true
ceph config get mds mds_debug_frag
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_debug_scatterstat

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_debug_scatterstat](../../../config/mds/mds.md#SP_mds_debug_scatterstat) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_debug_scatterstat true
ceph config get mds mds_debug_scatterstat
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_debug_subtrees

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_debug_subtrees](../../../config/mds/mds.md#SP_mds_debug_subtrees) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_debug_subtrees true
ceph config get mds mds_debug_subtrees
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_health_dummy

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_inject_health_dummy](../../../config/mds/mds.md#SP_mds_inject_health_dummy) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_health_dummy true
ceph config get mds mds_inject_health_dummy
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_journal_corrupt_dentry_first

| | |
|---|---|
| Type | Float · default `0.0` · **Dev** |
| Table | [mds.md#SP_mds_inject_journal_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_journal_corrupt_dentry_first) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_journal_corrupt_dentry_first 0.0
ceph config get mds mds_inject_journal_corrupt_dentry_first
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_migrator_session_race

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_inject_migrator_session_race](../../../config/mds/mds.md#SP_mds_inject_migrator_session_race) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_migrator_session_race true
ceph config get mds mds_inject_migrator_session_race
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_rename_corrupt_dentry_first

| | |
|---|---|
| Type | Float · default `0.0` · **Dev** |
| Table | [mds.md#SP_mds_inject_rename_corrupt_dentry_first](../../../config/mds/mds.md#SP_mds_inject_rename_corrupt_dentry_first) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_rename_corrupt_dentry_first 0.0
ceph config get mds mds_inject_rename_corrupt_dentry_first
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0.0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_skip_replaying_inotable

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [mds.md#SP_mds_inject_skip_replaying_inotable](../../../config/mds/mds.md#SP_mds_inject_skip_replaying_inotable) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_skip_replaying_inotable true
ceph config get mds mds_inject_skip_replaying_inotable
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### mds_inject_traceless_reply_probability

| | |
|---|---|
| Type | Float · default `0` · **Dev** |
| Table | [mds.md#SP_mds_inject_traceless_reply_probability](../../../config/mds/mds.md#SP_mds_inject_traceless_reply_probability) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set mds mds_inject_traceless_reply_probability 0
ceph config get mds mds_inject_traceless_reply_probability
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
