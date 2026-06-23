# نمودارهای توالی

همه نمودارها با `autonumber` برای ارجاع در متن.

## ۱. S3 GET Object

```mermaid
sequenceDiagram
  autonumber
  participant C as Client
  participant FE as Beast Frontend
  participant PR as process_request
  participant REST as RGWREST
  participant H as RGWHandler_REST_Obj_S3
  participant O as RGWGetObj
  participant SAL as sal::Object
  participant R as RadosStore

  C->>FE: GET /bucket/key
  FE->>PR: process_request
  PR->>REST: get_handler
  REST->>H: S3 handler
  H->>O: get_op
  PR->>O: verify_requester
  PR->>PR: rgw_process_authenticated
  O->>O: read_permissions
  O->>O: verify_permission
  O->>SAL: read
  SAL->>R: RADOS read
  R-->>C: 200 body
```

**توضیح:** مراحل ۷–۱۰ مجوز و ACL/IAM را بارگذاری می‌کنند؛ ۱۱–۱۳ داده از RADOS خوانده می‌شود.

## ۲. S3 PUT Object

```mermaid
sequenceDiagram
  autonumber
  participant C as Client
  participant O as RGWPutObj
  participant DP as DataProcessor chain
  participant SAL as sal::Driver
  participant IDX as Bucket Index CLS

  C->>O: PUT + body stream
  O->>O: verify_permission
  O->>DP: filter pipeline
  DP->>SAL: write stripes
  SAL->>IDX: update index
  O->>C: 200 ETag
```

## ۳. احراز هویت S3 SigV4 (خلاصه)

```mermaid
sequenceDiagram
  autonumber
  participant O as RGWOp
  participant R as StrategyRegistry
  participant S as S3 strategy
  participant I as Identity

  O->>R: verify_requester
  R->>S: authenticate
  S->>I: build Identity
  I-->>O: req_state.auth.identity
```

## ۴. Multisite metadata sync (مفهومی)

```mermaid
sequenceDiagram
  autonumber
  participant ZA as Zone A RGW
  participant MD as mdlog
  participant ZB as Zone B RGW

  ZA->>MD: append metadata change
  ZB->>MD: poll / replicate
  ZB->>ZB: apply to local RADOS
```

## ۵. شکست زودهنگام (abort)

```mermaid
sequenceDiagram
  autonumber
  participant PR as process_request
  participant O as RGWOp
  participant C as Client

  PR->>O: verify_requester
  O-->>PR: -EACCES
  PR->>PR: abort_early
  PR->>C: 403 XML error
```

## classDiagram — لایه REST (بدون کاما در امضاها)

<div class="mermaid" data-mermaid-source="classDiagram&#10;  class RGWREST&#10;  class RGWRESTMgr&#10;  class RGWHandler_REST&#10;  class RGWOp&#10;  class RGWRESTOp&#10;  RGWREST --> RGWRESTMgr&#10;  RGWRESTMgr --> RGWHandler_REST&#10;  RGWHandler_REST --> RGWOp&#10;  RGWRESTOp ..|&gt; RGWOp"></div>

!!! note "رندر classDiagram"
    منبع نمودار کلاس در `data-mermaid-source` قرار دارد تا `&lt;&lt;` در HTML تفسیر نشود.

## مستندات مرتبط

- [خط لوله درخواست](request-pipeline.md)
- [ماژول API پروتکل](../modules/protocol-apis.md)
