# Debug

Global config deep dive — 5 options. [← Overview](../OVERVIEW.md) · [Tuning index](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [debug_asok_assert_abort](#debug_asok_assert_abort) | `False` | Dev | Dev |
| [debug_asserts_on_shutdown](#debug_asserts_on_shutdown) | `False` | Dev | Dev |
| [debug_deliberately_leak_memory](#debug_deliberately_leak_memory) | `False` | Dev | Dev |
| [debug_disable_randomized_ping](#debug_disable_randomized_ping) | `False` | Dev | Dev |
| [debug_heartbeat_testing_span](#debug_heartbeat_testing_span) | `0` | Dev | Dev |

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

### debug_asok_assert_abort

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [debug.md#SP_debug_asok_assert_abort](../../../config/global/debug.md#SP_debug_asok_assert_abort) |

**What it does:** Enable the admin socket commands 'assert' and 'abort' testing crash dumps etc.

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global debug_asok_assert_abort true
ceph config get global debug_asok_assert_abort
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### debug_asserts_on_shutdown

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [debug.md#SP_debug_asserts_on_shutdown](../../../config/global/debug.md#SP_debug_asserts_on_shutdown) |

**What it does:** Enable certain assertions to check for refcounting bugs on shutdown; see http://tracker.ceph.com/issues/21738

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global debug_asserts_on_shutdown true
ceph config get global debug_asserts_on_shutdown
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### debug_deliberately_leak_memory

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [debug.md#SP_debug_deliberately_leak_memory](../../../config/global/debug.md#SP_debug_deliberately_leak_memory) |

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global debug_deliberately_leak_memory true
ceph config get global debug_deliberately_leak_memory
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### debug_disable_randomized_ping

| | |
|---|---|
| Type | Bool · default `False` · **Dev** |
| Table | [debug.md#SP_debug_disable_randomized_ping](../../../config/global/debug.md#SP_debug_disable_randomized_ping) |

**What it does:** Disable heartbeat ping randomization for testing purposes

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global debug_disable_randomized_ping true
ceph config get global debug_disable_randomized_ping
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`False`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---

### debug_heartbeat_testing_span

| | |
|---|---|
| Type | Int · default `0` · **Dev** |
| Table | [debug.md#SP_debug_heartbeat_testing_span](../../../config/global/debug.md#SP_debug_heartbeat_testing_span) |

**What it does:** Override 60 second periods for testing only

**When to use:** Development, testing, or upstream debugging only — not for production tuning.

**Example:**

```bash
ceph config set global debug_heartbeat_testing_span 64
ceph config get global debug_heartbeat_testing_span
```

**Finding optimal value:**

**Tuning model:** Dev

1. Keep the upstream default (`0`) in production.
2. Change only in a lab while reproducing a specific issue.
3. Revert before returning the node to the production pool.

---


[← Overview](../OVERVIEW.md)
