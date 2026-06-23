# فاز ۰ — شرح روایی کلاس‌ها و توابع

این سند **روایت فنی** است: برای هر کلاس و تابع مهم فاز ۰ توضیح می‌دهد *چرا وجود دارد*، *چه زمانی* در مسیر درخواست اجرا می‌شود، *منطق داخلی* چیست، *چه خطاهایی* برمی‌گرداند، و *چه FIXME/TODO*‌هایی در کد دیده می‌شود.

!!! info "نحوه استفاده"
    - جداول snippet و ردیابی: اسناد verb ([GET](full-request-path.md)، [PUT](full-request-path-put.md)، …).
    - لایه‌های ۰–۶ خلاصه: [shared-layers-reference.md](shared-layers-reference.md).
    - cluster: [rados-osd-mon-stack.md](rados-osd-mon-stack.md).
    - این صفحه برای **خواندن پیوسته** و فهم «داستان» هر نماد است.

---

## فهرست

1. کلاس‌ها و ساختارهای داده
2. لایه ۰ — بوت
3. لایه ۱ — Beast
4. لایه ۲ — `process_request`
5. لایه ۳ — REST
6. لایه ۵–۶ — auth و authenticated
7. عملیات GET و HEAD
8. عملیات PUT و COPY
9. عملیات DELETE
10. عملیات LIST
11. عملیات POST
12. لایه RADOS / SAL
13. شرح روایی تابع‌به‌تابع (جزئیات)
14. مشکلات و FIXME جمع‌بندی

---

## کلاس‌ها و ساختارهای داده

### `RGWProcessEnv`

**جایگاه:** ساختار ثابت در طول عمر فرآیند `radosgw`؛ هر thread پردازش درخواست به آن اشاره دارد.

**روایت:** وقتی `radosgw` بالا می‌آید، یک بار `init_storage` و `cond_init_apis` اجرا می‌شود و نتیجه در `env` ذخیره می‌گردد. این «جعبه ابزار» است که به هر درخواست HTTP می‌گوید: از کدام **driver** (معمولاً `RadosStore`) استفاده کن، از کدام درخت **REST** (`RGWREST`) مسیریابی کن، موتور **auth** کدام استراتژی‌ها را دارد، و آیا **Lua** یا **rate limit** فعال است. بدون `penv` هیچ `process_request`ی معنا ندارد — درخواست orphan می‌ماند.

| عضو | روایت کوتاه |
|-----|-------------|
| `driver` | دروازه SAL به RADOS؛ تمام bucket/object از اینجا |
| `rest` | ریشه handlerهای S3/Swift/admin |
| `auth_registry` | لیست engineهای SigV4، STS، anonymous |
| `ratelimiting` | سهمیه بعد از auth |
| `lua.manager` | اسکریپت pre/post روی درخواست |
| `site` / `cfgstore` | realm، zone، multisite |

**مشکل رایج:** اگر `driver` null باشد (شکست `init_storage`)، frontend بالا می‌آید ولی هر درخواست فوراً crash یا خطای داخلی می‌دهد — همیشه لاگ بوت را چک کنید.

---

### `req_state`

**جایگاه:** stack object در `process_request` — **تمام state یک درخواست HTTP** تا پایان پاسخ.

**روایت:** تصور کنید یک پروندهٔ پرونده روی میز اپراتور: در ابتدا فقط method و URI روی جلد است (`info` از `preprocess`). بعد از auth نام کاربر روی پرونده می‌خورد (`user`, `identity`). بعد bucket و object از RADOS بارگذاری می‌شوند (`bucket`, `object`). در پایان خطا یا موفقیت در `s->err` و HTTP status ثبت می‌شود. وقتی `process_request` تمام شد، پرونده دور انداخته می‌شود — هیچ اشاره‌ای بین درخواست‌ها share نمی‌شود (thread-safe بودن به این شکل است).

**فیلدهای حساس:**

- `request_uri_aws4` — URI برای امضا؛ اگر با URI rewrite شده قاطی شود SigV4 می‌شکند.
- `yield` — اگر Beast async باشد، تمام `librados` با coroutine yield می‌کند نه block.
- `auth.identity` — بعد از `verify_requester`؛ قبل از آن نباید برای IAM به آن تکیه کرد.

---

### `RGWRequest`

**روایت:** شناسهٔ سبک‌وزن frontend: فقط `id` عددی و اشارهٔ `op` پس از انتخاب. ops log و trace از `id` و `trans_id` استفاده می‌کنند. جدا از `req_state` است تا لایه Beast کمتر به جزئیات S3 وابسته بماند.

---

### `RGWOp` (کلاس پایه)

**روایت:** هر عملیات S3 یک **دستور** است: GetObj، PutObj، ListBucket، … . `RGWOp` الگوی Template Method را پیاده می‌کند — ترتیب مراحل ثابت است، محتوای هر مرحله در subclass.

| متد مجازی | روایت |
|-----------|--------|
| `verify_requester` | «این درخواست از کیست؟» — معمولاً delegate به handler → `RGW_Auth_S3` |
| `init_permissions` | بار bucket، zone policy |
| `read_permissions` | ساخت `object`، ACL شیء |
| `verify_permission` | «آیا حق این action را دارد؟» — IAM/ACL |
| `verify_params` | query، Range، versionId |
| `pre_exec` | hook کوچک قبل از کار سنگین |
| `execute` | قلب عملیات — I/O |
| `complete` | اغلب `send_response()` |

**چرا جدا؟** تاریخچه: ابتدا REST و auth جدا بودند؛ حالا همه از یک چرخه عبور می‌کنند تا باگ «auth شده ولی execute نشده» کمتر شود.

---

### `RGWHandler_REST` و زیرکلاس‌ها

**روایت:** Handler نقش **مترجم HTTP → C++ op** را دارد. `RGWHandler_REST_Obj_S3` می‌داند `PUT` روی `/bucket/key` یعنی `op_put()` که یا `RGWPutObj` یا `RGWCopyObj` برمی‌گرداند. Handler خودش execute نمی‌کند — فقط factory و `postauth_init` (پارس bucket با tenant کاربر).

| Handler | URI | factory اصلی |
|---------|-----|--------------|
| `RGWHandler_REST_Service_S3` | `/` | ListBuckets |
| `RGWHandler_REST_Bucket_S3` | `/bucket` | ListObjects، subresource |
| `RGWHandler_REST_Obj_S3` | `/bucket/key` | Get/Put/Delete/Post |

---

### `RGWGetObj` و سلسله‌مراتب

**روایت:** وقتی کلاینت می‌خواهد بایت بخواند، این کلاس فعال می‌شود. `RGWGetObj_ObjStore_S3` لایه S3 است: `get_params` برای Range و `send_response` برای هدرهای `x-amz-*`. منطق خواندن در `execute`: `prepare` (metadata) سپس شاید `iterate` (stripeها).

**HEAD:** همان کلاس با `get_data=false` — `execute` بعد از `prepare` برمی‌گردد؛ body از RADOS خوانده نمی‌شود.

---

### `RGWPutObj` و سلسله‌مراتب

**روایت:** آپلود یعنی **خواندن از socket** و **نوشتن به RADOS** هم‌زمان (streaming). `ofs` offset در فیلتر chain را نگه می‌دارد. `multipart_upload_id` اگر پر باشد Writer part است نه atomic object. `copy_source` اگر پر باشد body از socket خالی است و داده از ReadOp منبع می‌آید.

اعضای مهم از دید داستان:

- `supplied_md5_b64` — وعدهٔ کلاینت؛ در پایان با hash محلی مقایسه می‌شود.
- `attrs` — قبل از `complete` پر می‌شود (ETag، ACL، compression).
- `processor` — `unique_ptr<Writer>`؛ زندگی‌اش فقط یک execute است.

---

### `RGWDeleteObj`

**روایت:** حذف در S3 اغلب **حذف نام در index** است نه فوراً پاک کردن دیسک. `delete_marker` می‌گوید آیا پاسخ باید به کلاینت بگوید «این یک marker است». `bypass_governance_mode` مسیر قانونی دور زدن retention با IAM جدا. `load_obj_state` قبل از حذف واقعی — اگر object lock اجازه ندهد، هیچ CLSای اجرا نمی‌شود.

---

### `RGWListBucket`

**روایت:** لیست یعنی **گشتن در دفتر فهرست** (bucket index) نه باز کردن هر فایل. `prefix` و `delimiter` نحوهٔ ورق زدن دفتر را تعیین می‌کنند. `marker` و `next_marker` صفحه‌بندی. `objs` vector نتیجهٔ یک صفحه است — ممکن است هزاران key در bucket باشد ولی هر پاسخ HTTP محدود به `max-keys` است.

---

### `RGWCopyObj`

**روایت:** از نظر کد subclass یا شاخهٔ `RGWPutObj` است — کلاینت PUT می‌زند ولی body نمی‌فرستد. RGW خودش از منبع می‌خواند و در مقصد می‌نویسد. داستان امنیتی: دو مجوز (Get + Put) در یک درخواست.

---

### `RadosStore` / `RadosObject` / `RadosReadOp` / `RadosAtomicWriter`

**روایت:** SAL می‌گوید «من Object می‌شناسم نه pool». `RadosObject::get_read_op()` یک `RadosReadOp` می‌سازد که داخلش `RGWRados::Object::Read` است. `RadosAtomicWriter` wrapper روی `putobj::AtomicObjectProcessor` — جایی که head و stripe واقعاً نوشته می‌شوند.

---

## لایه ۰ — بوت

### `main` (`rgw_main.cc`)

**روایت:** نقطهٔ ورود OS. Ceph را به‌عنوان **client** initialize می‌کند (نه OSD). `AppMain` را می‌سازد، frontendها را listen می‌کند، تا signal shutdown می‌خوابد. هیچ درخواست S3 اینجا پردازش نمی‌شود — فقط زیرساخت.

### `rgw_global_init`

**روایت:** `CephContext` را می‌سازد — config (`ceph.conf`)، subsys log، perf counter. اگر اینجا fail شود کل daemon بالا نمی‌آید.

### `AppMain::init_storage`

**روایت:** **مهم‌ترین خط بوت برای داده.** `DriverManager::get_storage` فایل‌های `rgw_sal_rados` را load می‌کند، `RGWRados::init_rados` → `connect` به MON، poolها را باز می‌کند، threadهای GC/LC/sync را (در صورت config) start می‌کند. `env.driver` از اینجا می‌آید.

**مشکل:** zone/realm اشتباه → bucket در cluster دیگر دیده نمی‌شود؛ علامت: ListBuckets خالی یا 404 همه جا.

### `cond_init_apis` / `init_frontends2`

**روایت:** درخت REST S3 را به `RGWREST` وصل می‌کند (`rgw_enable_apis`). سپس Beast (یا civetweb) روی پورت bind می‌شود. از این لحظه `handle_connection` می‌تواند صدا زده شود.

---

## لایه ۱ — Beast

### `handle_connection`

**روایت:** هر TCP connection یک **حلقه** است. یک درخواست HTTP می‌خواند، `process_request` را صدا می‌زند، پاسخ می‌نویسد، اگر keep-alive باشد دوباره header می‌خواند. coroutine (`yield`) اجازه می‌دهد هزاران connection بدون thread per connection block نشوند.

**منطق I/O chain:** raw socket → controlling length → chunk decoding → buffering → reordering → `RGWRestfulIO`. هر لایه یک مشکل HTTP واقعی را حل می‌کند (chunked، expect-100، …).

**خطا:** parse بد → 400؛ reset → خاموش بدون log spam. **امنیت:** هیچ SigV4 اینجا نیست — فقط bytes.

---

## لایه ۲ — `process_request`

### `process_request`

**روایت:** **کارگردان ارکستر.** خودش object نمی‌خواند؛ ترتیب را enforce می‌کند:

1. `req_state` بساز.
2. handler پیدا کن — وگرنه 405/404.
3. op بگیر — وگرنه MethodNotAllowed.
4. (شاید) Lua pre.
5. dmclock — شاید 503 SlowDown **قبل** RADOS.
6. auth — شاید 403 **قبل** bucket load سنگین.
7. `postauth_init` — نام bucket درست شود.
8. `rgw_process_authenticated` — مجوز + execute.
9. cleanup: Lua post، ops log، free op.

**FIXME (388):** اگر handler قدیمی identity نسازد، `transform_old_authinfo` پر می‌کند — مسیر در حال حذف.

### `rgw_process_authenticated`

**روایت:** همان چرخه `RGWOp` برای همه verbها. نکتهٔ DELETE/PUT: `init_processing` گاهی **قبل** `init_permissions` در مسیر op صدا زده می‌شود (بسته به override). admin فقط برخی `-EACCES` را override می‌کند — نه `-ENOENT`.

### `abort_early`

**روایت:** وقتی جایی `ret < 0` شد، داستان درخواست تمام می‌شود: dialect خطا را به XML S3 map می‌کند، HTTP status set می‌شود، body خطا نوشته می‌شود، perf «failed request» ++. op ممکن است نیمه‌کاره مانده باشد — destructorها writer را cancel می‌کنند.

---

## لایه ۳ — REST

### `RGWREST::preprocess`

**روایت:** اولین جایی که **HTTP خام** به **معنی S3** تبدیل می‌شود. method → `s->op`. URI decode. `\0` در URL → رد (امنیت). **قبل** از rewrite subdomain، `request_uri_aws4` ذخیره می‌شود — داستان امضای SigV4.

### `RGWREST::get_handler`

**روایت:** درخت managerها (service / bucket / object) را طی می‌کند تا handler مناسب پیدا شود. `init` handler را به `req_state` وصل می‌کند. `init_meta_info` پارامترهای S3-specific.

### `RGWHandler_REST_Obj_S3::op_get` / `op_put` / `op_delete` / `op_post` / `op_head`

**روایت:** هر کدام **شاخه‌ای از query و subresource** است:

- `op_get` + `uploadId` → ListMultipart (نه download).
- `op_put` + copy source → CopyObj.
- `op_delete` + `uploadId` → AbortMultipart.
- `op_post` + `uploads` → InitMultipart؛ + `uploadId` → Complete.

factory اشتباه = op اشتباه = باگ «چرا DELETE multipart لیست می‌کند».

### `postauth_init`

**روایت:** پس از دانستن user، bucket name از URI با **tenant** درست استخراج می‌شود. object name validate می‌شود. MFA header ممکن است اینجا چک شود.

---

## لایه ۵–۶ — auth و authenticated

### `RGWOp::verify_requester`

**روایت:** thin wrapper: `dialect_handler->authorize`. برای S3 → `RGW_Auth_S3::authorize`.

### `RGW_Auth_S3::authorize`

**روایت:** اگر هیچ backend فعال نباشد → `-EPERM`. `Strategy::apply` روی `auth_registry.get_s3_main()` — ترتیب engineها (STS، external، local) از config.

### `Strategy::apply` / `LocalEngine::authenticate`

**روایت:** برای SigV4 کلاسیک:

1. access key → user در RADOS.
2. canonical request بساز (همان کلاینت).
3. signing key از secret.
4. signature مقایسه — constant-time مهم نیست همیشه ولی باید match باشد.
5. presigned expiry چک.

**خطاهای داستان‌دار:** skew time → RequestTimeTooSkewed؛ URI اشتباه → SignatureDoesNotMatch؛ key نیست → InvalidAccessKey.

### `verify_permission` (پایه و per-op)

**روایت:** IAM policy + ACL legacy + conditions (`s3:prefix` در LIST). هر op action متفاوت دارد — GetObject vs PutObject vs ListBucket.

---

## عملیات GET و HEAD

### `RGWGetObj::verify_permission`

**روایت:** replication system request شاخهٔ گسترده‌تر دارد. GET عادی: `s3GetObject` یا `s3GetObjectVersion`. requester pays و expected bucket owner اینجا یا در helper.

### `RGWGetObj::execute`

**روایت:**

1. `get_read_op()` — factory.
2. `get_params` — Range، If-Match.
3. `init_common` — ofs/end.
4. `prepare` — **یک سفر RADOS برای head** — size، etag، manifest.
5. اگر STAT/HEAD → برگشت.
6. فیلتر chain: decrypt ← decompress ← lua.
7. `iterate` — حلقه stripe؛ aio window.
8. `send_response_data` — به socket.
9. خطا → `send_response_data_error`.

**مشکل:** manifest بزرگ → prepare گران؛ Range اشتباه → 416.

### `RGWGetObj_ObjStore_S3::send_response`

**روایت:** هدرهای S3، ETag در quotes، SSE headers، 206 Partial Content اگر Range.

---

## عملیات PUT و COPY

### `RGWPutObj::init_processing`

**روایت:** اگر `x-amz-copy-source` هست، الان parse می‌شود (bucket، key، versionId، tenant). سپس `get_params`. body هنوز consume نشده.

### `RGWPutObj_ObjStore_S3::get_params`

**روایت:** chunked بدون length مجاز. policy ACL از هدر. Object Lock. multipart part number. append position. هر خطا اینجا → قبل از نوشتن یک byte.

### `get_data` (زنجیره)

**روایت:** `recv_body` از `RGWRestfulIO` تا `max_chunk_size`. S3 بعد از هر chunk موفق SigV4 payload را verify می‌کند (`do_aws4_auth_completion`). copy از منبع: `get_data(fst,lst)` داخلی ReadOp.

### `RGWPutObj::execute` — داستان کامل

**فاز اعتبارسنجی:** bucket هست؟ quota؟ MD5 format؟ versioning instance؟

**فاز writer:** multipart / append / atomic — سه داستان متفاوت.

**فاز فیلتر:** encrypt، compress، checksum، lua — آخرین اضافه‌شده اول اجرا.

**فاز transfer:** while read from socket → process → ofs++.

**فاز نهایی:** MD5 vs Content-MD5؛ attrs؛ `processor->complete` — **لحظهٔ حقیقی commit**؛ notification.

**مشکل:** `ofs != content_length` → timeout؛ complete fail → object نیمه‌کاره + GC.

### `RGWCopyObj`

**روایت:** همان execute با `copy_source` پر — verify_permission دو بار جهان (منبع + مقصد). cloud-tiered source → InvalidObjectState.

---

## عملیات DELETE

### `RGWDeleteObj::init_processing`

**روایت:** query parameters: versionId، bypass retention، if-match، MFA-related prep.

### `RGWDeleteObj::verify_permission`

**روایت:** MFA برای versioned delete. bypass governance IAM جدا.

### `RGWDeleteObj::execute`

**روایت:**

1. bucket exists.
2. `load_obj_state` — اگر نیست شاید 404 یا expiration semantics.
3. object lock — شاید stop.
4. notification reserve.
5. `get_delete_op()->delete_obj` — CLS index + remove.
6. logging (شکست log حذف را لغو نمی‌کند).

**versioning:** بدون versionId → marker؛ با versionId → حذف آن نسخه.

---

## عملیات LIST

### `RGWListBucket::verify_permission`

**روایت:** `get_params` اول — prefix/delimiter در env برای IAM. `ListBucket` vs `ListBucketVersions`.

### `RGWListBucket::parse_max_keys`

**روایت:** سقف امنیتی — کلاینت نمی‌تواند با max-keys بی‌نهایت OSD را بکشد.

### `RGWListBucket::execute`

**روایت:** `bucket->list` → `RGWRados::Bucket::List::list_objects` → `cls_rgw_bucket_list_op` روی shard. نتیجه XML در `send_response`.

### `RGWListBuckets`

**روایت:** سطح account — metadata bucketها در root pool؛ نه index shard.

---

## عملیات POST

### `RGWInitMultipart_ObjStore_S3`

**روایت:** session آپلود می‌سازد — uploadId برمی‌گرداند. هنوز part نیست.

### `RGWCompleteMultipart_ObjStore_S3`

**روایت:** XML partها + ETagها verify → compose object → index commit → multipart session پاک.

### `RGWPostObj_ObjStore_S3`

**روایت:** form policy (HMAC) به‌جای header SigV4. **FIXME:** browser auth «makeshift». policy ضعیف = آپلود arbitrary key.

### `RGWAbortMultipart`

**روایت:** DELETE با uploadId — partهای نیمه‌کاره برای GC.

---

## لایه RADOS / SAL

### `RGWRados::init_rados` / `init_complete`

**روایت:** اتصال librados؛ باز کردن poolهای سیستمی؛ start GC thread. بدون MON → connect fail.

### `rgw_rados_operate`

**روایت:** sync یا `async_operate` با yield — یک oid در یک pool. تمام read/write/cls از اینجا عبور می‌کند.

### `RGWRados::Object::Read::prepare`

**روایت:** head object را می‌خواند؛ manifest decode؛ attrs به `RGWObjState`.

### `RGWRados::Object::Read::iterate` / `iterate_obj`

**روایت:** برای هر بازه در manifest یک read RADOS schedule می‌کند. throttle window محدودیت هم‌زمانی.

### `get_obj_iterate_cb`

**روایت:** `op.read(ofs,len)` را به aio می‌دهد؛ وقتی complete شد callback به فیلتر RGW. cancel → drain بدون send به client.

### `cls_rgw_bucket_list_op`

**روایت:** **مغز LIST** — روی OSD اجرا می‌شود؛ omap bucket index را walk می‌کند.

### `putobj::AtomicObjectProcessor::complete`

**روایت:** head نهایی + link در index — object برای LIST visible می‌شود.

### `DeleteOp::delete_obj`

**روایت:** unlink index؛ marker یا remove؛ stripeها ممکن است async GC شوند.

---

## شرح روایی تابع‌به‌تابع (جزئیات)

در ادامه برای هر تابع، روایت کامل‌تر (ورودی، منطق، خروجی، خطا، ارتباط) آمده است.

### `process_request` — روایت گام‌به‌گام

وقتی Beast یک درخواست آماده کرد، `process_request` اول `client_io->init` را صدا می‌زند تا بافر پاسخ خالی ساخته شود. سپس `req_state` روی stack ساخته می‌شود — این تصمیم مهمی است: هیچ `new req_state` per request در heap نیست مگر در مسیرهای خاص. `get_user` با user خالی صدا زده می‌شود تا بعداً identity جایگزین شود.

`rest->get_handler` ممکن است null برگرداند — مثلاً URI اصلاً S3 نیست یا subresource ناشناخته است. در این حالت قبل از auth خارج می‌شویم چون نمی‌دانیم dialect خطا چیست.

`handler->get_op()` op را می‌سازد — **ownership** به `req` و `unique_ptr` در process_request منتقل می‌شود. اگر method روی resource غیرمجاز باشد (مثلاً PATCH روی object بدون op)، 405 می‌گیریم.

Lua `preRequest` اگر fail شود فقط log warning است — طراحی عمدی: اسکریپت ادمین نباید کل سرویس را down کند، ولی این یعنی policy امنیتی Lua ضعیف خطرناک است.

`schedule_request` با dmclock اگر `-EAGAIN` دهد، درخواست **قبل از auth** رد می‌شود — کلاینت باید retry کند. این برای محافظت OSD در overload است.

`verify_requester` اولین بار است که secret و signature دیده می‌شود. fail → `abort_early` بدون `s->bucket` پر شده — در حالت ideal anonymous هم identity «ناشناس» ساخته می‌شود.

`postauth_init` bucket را با tenant درست می‌کشد — اگر اینجا fail شود، execute هرگز اجرا نمی‌شود و object name ممکن است invalid باشد.

`rgw_process_authenticated` تمام policy load و execute را انجام می‌دهد. return منفی → همان `abort_early`.

در `done:` ops log نوشته می‌شود — برای audit S3. `handler->put_op(op)` op را آزاد می‌کند.

---

### `rgw_process_authenticated` — روایت هر مرحله

**`init_permissions`:** handler ممکن است bucket را از RADOS بخواند (`rgw_build_bucket_policies`). اگر bucket نباشد، GET/PUT ممکن است بعداً 404 بدهد؛ LIST همین جا متوقف می‌شود.

**`retarget`:** website mode ممکن است op را عوض کند — مثلاً GET به index.html static. برای API معمولی skip می‌شود.

**`read_permissions`:** برای GET/PUT/DELETE روی object، `s->object` ساخته می‌شود و ACL شیء load می‌شود. برای LIST فقط bucket کافی است.

**`init_processing`:** op-specific — PUT اینجا copy source parse می‌کند.

**`verify_op_mask`:** آیا این op با نوع API سازگار است (read vs write).

**`verify_permission`:** داستان اصلی مجوز — IAM evaluation.

**`verify_params`:** Range معتبر؟ versionId وجود دارد؟

**`rate_limit`:** سهمیه per-user/bucket بعد از مجوز، قبل از I/O.

**`execute`:** I/O سنگین.

**`complete`:** پاسخ HTTP — حتی اگر execute خطای داخلی در `op_ret` گذاشته باشد، complete ممکن است status را بنویسد (بسته به op).

---

### `RGWREST::preprocess` — روایت

درخواست خام HTTP وارد می‌شود. method به `s->op` map می‌شود. URI decode می‌شود — کاراکترهای escape شده به byte واقعی. اگر NUL در path باشد، اینجا کشف می‌شود چون OSD و RADOS با string C-safe کار می‌کنند.

`request_uri_aws4` **قبل** از اینکه virtual-hosted-style bucket را از host جدا کنیم ذخیره می‌شود. داستان واقعی دیباگ: مشتری `mybucket.s3.amazonaws.com` می‌زند، RGW path را rewrite می‌کند، اگر امضا روی path rewrite شده ساخته نشده باشد SigV4 fail می‌شود — مگر این فیلد حفظ شده باشد.

Content-Length و Transfer-Encoding تفسیر می‌شوند — برای PUT بعداً `s->content_length` مهم است.

---

### `LocalEngine::authenticate` (SigV4) — روایت

موتور local فرض می‌کند access key در zone فعلی در RADOS lookup می‌شود. user record secret دارد. سپس string-to-sign از canonical request ساخته می‌شود — **هر byte** در canonical باید با کلاینت یکی باشد: method، URI، query sorted، headers signed، payload hash.

signing key زنجیره HMAC است — تاریخ روز اشتباه → کل chain اشتباه → SignatureDoesNotMatch.

اگر presigned است، expiry و conditionهای اضافی چک می‌شوند.

خروجی: `Identity` با perm mask و user id — `s->auth.identity` مالک درخواست برای IAM بعدی است.

---

### `RGWGetObj::execute` — روایت تابع‌به‌تابع

**`get_read_op`:** abstraction — فردا اگر driver عوض شود همین API می‌ماند.

**`prepare`:** سفر به RADOS برای head. اگر object نیست `-ENOENT` قبل از iterate. اگر delete marker و GET بدون version شاید 404. manifest اگر باشد برای iterate لازم است.

**چک STAT:** اگر HEAD، اینجا داستان تمام است — client فقط هدر می‌گیرد.

**فیلتر decrypt:** اگر SSE-C/SSE-KMS، کلید یا KMS باید در دسترس باشد — وگرنه execute fail بعد از prepare.

**`iterate`:** برای هر chunk از OSD، callback به HTTP. اگر client connection قطع شود، cancel aio ولی ممکن است OSD read ادامه یابد تا drain — هزینه داخلی.

**`send_response_data`:** Content-Range برای partial GET.

---

### `RGWPutObj::execute` — روایت تابع‌به‌تابع

**quota اول:** قبل از خواندن body — اگر Content-Length از سقف بیشتر باشد زود fail.

**انتخاب writer:** multipart یعنی part جدا در pool و index جدا تا Complete. atomic یعنی یک object یک manifest.

**`prepare` writer:** رزرو نام در index (بسته به versioning) — race با concurrent PUT روی همان key ممکن است.

**حلقه `get_data` / `process`:** backpressure — اگر OSD کند باشد socket buffer پر می‌شود و TCP window به client سیگنال می‌دهد.

**MD5 نهایی:** اگر Content-MD5 فرستاده شده و match نباشد، object نباید commit شود — `complete` fail.

**`processor->complete`:** لحظه‌ای که object برای GET بعدی visible می‌شود (modulo caching).

**notification:** شکست publish بعد از commit فقط log است — داده commit شده (at-least-once notification).

---

### `RGWDeleteObj::execute` — روایت تابع‌به‌تابع

**`load_obj_state`:** اگر object قبلاً delete marker خورده، رفتار S3 خاص — ممکن است 404.

**`verify_object_lock`:** COMPLIANCE mode بدون bypass غیرقابل حذف تا expiry.

**`delete_obj`:** CLS روی index shard — اگر concurrent LIST باشد ممکن است entry ghost ببیند تا settle شود.

**Swift versioning restore:** شاخهٔ خاص — اگر restore انجام شود DELETE ممکن است فقط marker بزند.

---

### `RGWListBucket::execute` — روایت

**`bucket->list`:** ممکن است چند shard index را sequential بخواند — bucket بزرگ + prefix خالی = گران.

**`is_truncated`:** به کلاینت می‌گوید ContinuationToken بفرستد.

**unordered listing:** برای perf؛ با delimiter ناسازگار — خطای EINVAL.

---

### `cls_rgw_bucket_list_op` — روایت (RADOS)

این تابع client-side در RGW است که CLS method را روی oid shard index می‌فرستد. OSD primary آن PG omap را scan می‌کند. pending entries ممکن است نیاز به `check_disk_state` داشته باشد — داستان eventual consistency بین index و data.

---

### `putobj::AtomicObjectProcessor::complete` — روایت

head object با attrs نهایی نوشته می‌شود. سپس entry در bucket index link می‌شود. اگر بین write stripe و link crash شود، GC object یتیم می‌سازد — thread GC بعداً تمیز می‌کند.

---

## مشکلات و FIXME جمع‌بندی

| محل | داستان مشکل | اثر |
|-----|-------------|-----|
| `rgw_process.cc:388` | auth legacy | identity غیرمنتظره |
| `rgw_rest_s3.cc:6301` | anon در get_auth_data | anonymous ناقص |
| `rgw_rest_s3.cc:3377` | browser POST | امنیت policy |
| `rgw_rest_s3.cc:6094` | website retarget | handle object اشتباه |
| `rgw_auth_s3.cc:1487` | chunked length | PUT aws-chunked |
| `rgw_rest.cc:737` | error headers | کلاینت‌های header-only |
| `rgw_op.cc:2423` | range prefetch | کارایی GET |

---

## چگونه این سند را با کد بخوانید

1. یک verb را در [index](index.md) انتخاب کنید.
2. «داستان» کلاس اصلی را **اینجا** بخوانید.
3. snippet و ردیابی را در سند verb دنبال کنید.
4. زیر RADOS را در [rados-osd-mon-stack](rados-osd-mon-stack.md) ببینید.
5. با `gdb` روی همان ترتیب trace table بریک‌پوینت بگذارید.

---

## پیوندها

→ [فهرست فاز ۰](index.md) · [لایه‌های مشترک](shared-layers-reference.md) · [GET](full-request-path.md)
