# Quota sync & defaults

RGW config deep dive — 5 options. [← RGW config overview](OVERVIEW.md) · [Tuning index](TUNING.md) · [INDEX](../../config/rgw/INDEX.md)

Quota enforcement also requires `rgw_enable_quota_threads` on at least one RGW per zone. See [rgw_enable_quota_threads](../../config/rgw/rgw.md#SP_rgw_enable_quota_threads).

| Option | Default | Level | Tuning |
|--------|---------|-------|--------|
| [rgw_account_default_quota_max_objects](#rgw_account_default_quota_max_objects) | `-1` | Basic | Policy |
| [rgw_account_default_quota_max_size](#rgw_account_default_quota_max_size) | `-1` | Basic | Policy |
| [rgw_enable_quota_threads](#rgw_enable_quota_threads) | `True` | Advanced | Policy |
| [rgw_user_default_quota_max_objects](#rgw_user_default_quota_max_objects) | `-1` | Basic | Policy |
| [rgw_user_default_quota_max_size](#rgw_user_default_quota_max_size) | `-1` | Basic | Policy |

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

### rgw_account_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_account_default_quota_max_objects](../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_objects) |

**What it does:** Default cap on **total object count** across all buckets owned by a **new** S3 account. `-1` means unlimited.

**When to use:** Multi-tenant platforms using the account abstraction. Applies only when accounts are created — existing accounts are unchanged.

**Related options:**

- `rgw_account_default_quota_max_size`
- `rgw_enable_quota_threads` (required on at least one RGW per zone)

**Example:**

```bash
ceph config set client rgw_account_default_quota_max_objects 1000000
radosgw-admin account create --account-id=acme --account-name="ACME Corp"
```

Set in `[client]` or global so `radosgw-admin` picks it up.

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_account_default_quota_max_size

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_account_default_quota_max_size](../../config/rgw/rgw.md#SP_rgw_account_default_quota_max_size) |

**What it does:** Default cap on **total stored bytes** for a new account.

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
# 10 TiB
ceph config set client rgw_account_default_quota_max_size $((10*1024*1024*1024*1024))
```

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_enable_quota_threads

| | |
|---|---|
| Type | Bool · default `True` · **Advanced** |
| Table | [rgw.md#SP_rgw_enable_quota_threads](../../config/rgw/rgw.md#SP_rgw_enable_quota_threads) |

**What it does:** Enables the quota maintenance thread.

**When to use:** Enabled by default; disable only when troubleshooting the related feature.

**Example:**

```bash
ceph config set client.rgw rgw_enable_quota_threads True
ceph config get client.rgw rgw_enable_quota_threads
```

**Finding optimal value:**

**Tuning model:** Policy

1. Default `True` matches upstream/AWS-compatible behavior.
2. Test with your S3/Swift SDKs and automation before changing.
3. Optimal = contract your clients expect, not maximum throughput.

---

### rgw_user_default_quota_max_objects

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_user_default_quota_max_objects](../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_objects) |

**What it does:** User quota max objects

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
ceph config set client.rgw rgw_user_default_quota_max_objects -1
ceph config get client.rgw rgw_user_default_quota_max_objects
```

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---

### rgw_user_default_quota_max_size

| | |
|---|---|
| Type | Int · default `-1` · **Basic** |
| Table | [rgw.md#SP_rgw_user_default_quota_max_size](../../config/rgw/rgw.md#SP_rgw_user_default_quota_max_size) |

**What it does:** User quota max size

**When to use:** Set tenant or platform default limits for new users, accounts, or buckets.

**Example:**

```bash
ceph config set client.rgw rgw_user_default_quota_max_size -1
ceph config get client.rgw rgw_user_default_quota_max_size
```

**Finding optimal value:**

**Tuning model:** Policy

1. `ceph df detail` — usable cluster capacity.
2. Divide by expected tenants/accounts; leave 20–30% headroom for GC and bursts.
3. Set limit; `-1` means unlimited. Default: `-1`.
4. Create a test user/account and confirm via `radosgw-admin quota get`.
5. Existing users/accounts are **not** retroactively changed.

```bash
ceph df detail
radosgw-admin quota get --uid=testuser
radosgw-admin bucket stats --bucket=testbucket
```

---


[← RGW config overview](OVERVIEW.md)
