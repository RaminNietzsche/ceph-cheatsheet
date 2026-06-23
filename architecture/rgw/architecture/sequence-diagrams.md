# Sequence diagrams

High-level HTTP flows (see also [Request pipeline](request-pipeline.md)).

## GET object

```mermaid
sequenceDiagram
  autonumber
  participant C as Client
  participant FE as Frontend
  participant PR as process_request
  participant OP as RGWGetObj
  participant SAL as sal::Object
  participant RAD as RADOS

  C->>FE: GET /bucket/object
  FE->>PR: parse + route
  PR->>PR: auth
  PR->>OP: execute
  OP->>SAL: read
  SAL->>RAD: RADOS read
  RAD-->>C: 200 + body
```

## PUT object (summary)

```mermaid
sequenceDiagram
  participant C as Client
  participant OP as RGWPutObj
  participant SAL as sal
  participant RAD as RADOS

  C->>OP: PUT
  OP->>SAL: write pipeline
  SAL->>RAD: data + index update
  RAD-->>C: 200
```

## Auth check

See [Authentication module](../modules/auth.md).

## Full diagrams

Additional sequence diagrams and HTTP method variants are in upstream `docs-extended/pages/architecture/sequence-diagrams.md` (Persian, **فارسی** locale on this site).
