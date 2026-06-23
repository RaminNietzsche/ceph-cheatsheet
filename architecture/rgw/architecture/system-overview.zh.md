# 系统概览

## ## RGW 是什么？

**RADOS Gateway (RGW)** is Ceph’s object gateway. It exposes **Amazon S3**, **OpenStack Swift**, and related APIs (STS, IAM, Admin) on a Ceph cluster. Clients send HTTP requests; RGW handles auth, authorization, and mapping to storage operations.

## 主要层次

| Layer | Responsibility | Approximate code |
|-------|----------------|------------------|
| Frontend | HTTP accept, parse | `rgw_asio_frontend.cc` |
| Request processing | `req_state` lifecycle | `rgw_process.cc` |
| REST / protocol | URI → `RGWOp` | `rgw_rest*.cc` |
| Operations | S3/Swift/Admin logic | `rgw_op.cc` |
| Auth | `StrategyRegistry` | `rgw_auth*.cc` |
| SAL | `User` / `Bucket` / `Object` | `rgw_sal.h` |
| Driver | RADOS and other backends | `driver/` |
| Services | Internal RADOS services | `services/` |

```mermaid
flowchart TB
  subgraph edge [Edge]
    FE[Frontend Beast]
  end
  subgraph logic [Protocol logic]
    PR[process_request]
    REST[RGWREST]
    OP[RGWOp]
    AUTH[Auth]
  end
  subgraph data [Data]
    SAL[sal::Driver]
    RAD[RadosStore]
    OSD[RADOS Cluster]
  end
  FE --> PR --> REST --> OP
  PR --> AUTH
  OP --> SAL --> RAD --> OSD
```

## 数据实体

- **User** — data owner, keys, quota
- **Bucket** — flat namespace for objects
- **Object** — bytes + metadata + attrs

> **Source:** [`rgw_sal.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_sal.h#L98-L126)

## 可部署单元

| Binary | Role |
|--------|------|
| `radosgw` | Main HTTP daemon |
| `radosgw-admin` | CLI admin tool |
| `librgw` | Embedded C API |

## 外部依赖

- **librados** — production storage
- **Boost.Beast / ASIO** — default HTTP server
- **OpenSSL** — signing and encryption
- **Lua** — request hooks (optional)

## 相关

- [Runtime topology](runtime-topology.md)
- [Request pipeline](request-pipeline.md)
- [Core request path module](../modules/core-request-path.md)
