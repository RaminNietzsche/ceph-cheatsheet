# 协议 API 模块

## REST 管理器

| API | Main file | Enable via |
|-----|-----------|------------|
| S3 | `rgw_rest_s3.cc` | `rgw_enable_apis` s3 |
| Swift | `rgw_rest_swift.cc` | swift |
| STS | `rgw_rest_sts.cc` | sts |
| IAM | `rgw_rest_iam.cc` | iam |
| Admin | `rgw_rest_admin.h` + driver REST | admin |
| PubSub | `rgw_rest_pubsub.cc` | — |

Registered in `rgw::AppMain::cond_init_apis()` (`rgw_appmain.cc`).

## Handler pattern

`RGWHandler_REST` returns an `RGWOp` per HTTP method:

> **Source:** [`rgw_rest.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L557-L565)

## `RGWRESTOp`

Shared XML/JSON response and `send_response()`:

> **Source:** [`rgw_rest.h`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_rest.h#L540-L555)

## S3 Website

`rgw_rest_s3website.h` — retarget in `handler->retarget()` for static website hosting.

## 相关

- [Sequence diagrams](../architecture/sequence-diagrams.md)
- [Core request path](core-request-path.md)
