# SAL (Store Abstraction Layer) module

## Purpose

Decouple HTTP protocol logic from storage backends. All data operations go through `rgw::sal::*`.

## Key files

| File | Role |
|------|------|
| `rgw_sal.h` | Core API: `Driver`, `User`, `Bucket`, `Object` |
| `rgw_sal.cc` | `DriverManager`, driver selection |
| `rgw_sal_filter.h` | Filter stack layers |
| `driver/*/rgw_sal_*.h` | Backend implementations |

## Source reference

> **Source:** [`rgw_sal.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_sal.h#L98-L126)

## `DriverManager`

Selects backend from config (`rgw_store`) and optional D4N filter when compiled:

> **Source:** [`rgw_sal.cc`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_sal.cc#L60-L79)

## SAL class diagram

```mermaid
classDiagram
  class Driver
  class User
  class Bucket
  class Object
  class DataProcessor
  Driver --> User
  Driver --> Bucket
  Bucket --> Object
  Object --> DataProcessor
```

## Interaction

- **Upstream:** `RGWOp`, `rgw_process`
- **Downstream:** `RadosStore`, `DBStore`, …

## Architecture docs

- [System overview](../architecture/system-overview.md)
