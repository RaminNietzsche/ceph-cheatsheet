# HTTP request pipeline

## Stages

From edge to storage:

1. **Parse HTTP** — `RGWEnv`, headers, URI
2. **REST routing** — `RGWREST::get_handler()`
3. **Select operation** — `RGWHandler_REST::get_op()`
4. **Lua hook** — `preRequest` (optional)
5. **dmclock** — `schedule_request()`
6. **Authentication** — `verify_requester()`
7. **After auth** — `rgw_process_authenticated()`
8. **Response & logging** — `complete()`, ops log, `postRequest`

## Entry point

> **Source:** [`rgw_process.cc`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_process.cc#L278-L325)

## After authentication

> **Source:** [`rgw_process.cc`](https://github.com/ceph/ceph/blob/main/src/rgw/rgw_process.cc#L175-L275)

## Idempotency

| Operation | Behavior |
|-----------|----------|
| GET/HEAD | Idempotent |
| PUT object | Overwrite same key |
| Multipart Complete | Atomic index commit |
| DELETE | Logical/physical per versioning |

In multisite, **bilog / datalog** supports replay; duplicate HTTP requests may rewrite unless client conditions (e.g. `If-Match`) apply.

## Commit and consistency

- Object write: head + stripes in RADOS, then bucket index update (CLS)
- `CompleteMultipart`: assemble manifest then single index commit

## Related

- [Scheduling architecture](scheduling-architecture.md)
- [Core request path module](../modules/core-request-path.md)
