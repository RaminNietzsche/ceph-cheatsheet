# BitTorrent

RGW config deep dive — 8 options. [← RGW config overview](OVERVIEW.md) · [Handwritten batch](../rgw-config-options.md) · [INDEX](../../config/rgw/INDEX.md)

| Option | Default | Level |
|--------|---------|-------|
| [rgw_torrent_comment](#rgw_torrent_comment) | `(empty)` | Advanced |
| [rgw_torrent_createby](#rgw_torrent_createby) | `(empty)` | Advanced |
| [rgw_torrent_encoding](#rgw_torrent_encoding) | `(empty)` | Advanced |
| [rgw_torrent_flag](#rgw_torrent_flag) | `False` | Advanced |
| [rgw_torrent_max_size](#rgw_torrent_max_size) | `5_G` | Advanced |
| [rgw_torrent_origin](#rgw_torrent_origin) | `(empty)` | Advanced |
| [rgw_torrent_sha_unit](#rgw_torrent_sha_unit) | `512_K` | Advanced |
| [rgw_torrent_tracker](#rgw_torrent_tracker) | `(empty)` | Advanced |

---

### rgw_torrent_comment

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_comment](../../config/rgw/rgw.md#SP_rgw_torrent_comment) |

**What it does:** Torrent field comment

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_comment <value>
ceph config get client.rgw rgw_torrent_comment
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_createby

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_createby](../../config/rgw/rgw.md#SP_rgw_torrent_createby) |

**What it does:** torrent field created by

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_createby <value>
ceph config get client.rgw rgw_torrent_createby
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_encoding

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_encoding](../../config/rgw/rgw.md#SP_rgw_torrent_encoding) |

**What it does:** torrent field encoding

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_encoding <value>
ceph config get client.rgw rgw_torrent_encoding
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_flag

| | |
|---|---|
| Type | Bool · default `False` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_flag](../../config/rgw/rgw.md#SP_rgw_torrent_flag) |

**What it does:** When true, uploaded objects will calculate and store a SHA256 hash of object data so the object can be retrieved as a torrent file

**When to use:** Disabled by default; enable when you need the related feature and accept its trade-offs.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_flag False
ceph config get client.rgw rgw_torrent_flag
```

**Finding optimal value:** Policy choice aligned with client API expectations. Test with your S3/Swift clients; default (`False`) matches upstream.

---

### rgw_torrent_max_size

| | |
|---|---|
| Type | Size · default `5_G` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_max_size](../../config/rgw/rgw.md#SP_rgw_torrent_max_size) |

**What it does:** Objects over this size will not store torrent info.

**When to use:** Adjust when clients hit request-size or concurrency limits, or to protect cluster resources.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_max_size 5_G
ceph config get client.rgw rgw_torrent_max_size
```

**Finding optimal value:** Start from upstream default (`5_G`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_origin

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_origin](../../config/rgw/rgw.md#SP_rgw_torrent_origin) |

**What it does:** Torrent origin

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_origin <value>
ceph config get client.rgw rgw_torrent_origin
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_sha_unit

| | |
|---|---|
| Type | Size · default `512_K` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_sha_unit](../../config/rgw/rgw.md#SP_rgw_torrent_sha_unit) |

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_sha_unit 512_K
ceph config get client.rgw rgw_torrent_sha_unit
```

**Finding optimal value:** Start from upstream default (`512_K`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---

### rgw_torrent_tracker

| | |
|---|---|
| Type | Str · default `(empty)` · **Advanced** |
| Table | [rgw.md#SP_rgw_torrent_tracker](../../config/rgw/rgw.md#SP_rgw_torrent_tracker) |

**What it does:** Torrent field announce and announce list

**When to use:** Advanced tuning — change from upstream default only with a measured workload and rollback plan.

**Example:**

```bash
ceph config set client.rgw rgw_torrent_tracker <value>
ceph config get client.rgw rgw_torrent_tracker
```

**Finding optimal value:** Start from upstream default (`(empty)`). Change one option at a time under representative load; use `ceph config get client.rgw` and RGW perf counters to validate.

---


[← RGW config overview](OVERVIEW.md)
