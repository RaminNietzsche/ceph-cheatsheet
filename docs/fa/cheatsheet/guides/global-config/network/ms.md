# Ms

راهنمای عمیق پیکربندی Global — 91 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [ms_async_op_threads](#ms_async_op_threads) | `3` | Advanced | عملکرد |
| [ms_async_rdma_buffer_size](#ms_async_rdma_buffer_size) | `128_K` | Advanced | عملکرد |
| [ms_async_rdma_cm](#ms_async_rdma_cm) | `False` | Advanced | عملکرد |
| [ms_async_rdma_device_name](#ms_async_rdma_device_name) | `(empty)` | Advanced | عملکرد |
| [ms_async_rdma_dscp](#ms_async_rdma_dscp) | `96` | Advanced | عملکرد |
| [ms_async_rdma_enable_hugepage](#ms_async_rdma_enable_hugepage) | `False` | Advanced | سیاست |
| [ms_async_rdma_gid_idx](#ms_async_rdma_gid_idx) | `0` | Advanced | عملکرد |
| [ms_async_rdma_local_gid](#ms_async_rdma_local_gid) | `(empty)` | Advanced | عملکرد |
| [ms_async_rdma_polling_us](#ms_async_rdma_polling_us) | `1000` | Advanced | عملکرد |
| [ms_async_rdma_port_num](#ms_async_rdma_port_num) | `1` | Advanced | عملکرد |
| [ms_async_rdma_receive_buffers](#ms_async_rdma_receive_buffers) | `32_K` | Advanced | عملکرد |
| [ms_async_rdma_receive_queue_len](#ms_async_rdma_receive_queue_len) | `4_K` | Advanced | عملکرد |
| [ms_async_rdma_roce_ver](#ms_async_rdma_roce_ver) | `1` | Advanced | عملکرد |
| [ms_async_rdma_send_buffers](#ms_async_rdma_send_buffers) | `1_K` | Advanced | عملکرد |
| [ms_async_rdma_sl](#ms_async_rdma_sl) | `3` | Advanced | عملکرد |
| [ms_async_rdma_support_srq](#ms_async_rdma_support_srq) | `True` | Advanced | عملکرد |
| [ms_async_rdma_type](#ms_async_rdma_type) | `ib` | Advanced | عملکرد |
| [ms_async_reap_threshold](#ms_async_reap_threshold) | `5` | Dev | توسعه |
| [ms_bind_before_connect](#ms_bind_before_connect) | `False` | Advanced | عملکرد |
| [ms_bind_ipv4](#ms_bind_ipv4) | `True` | Advanced | عملکرد |
| [ms_bind_ipv6](#ms_bind_ipv6) | `False` | Advanced | عملکرد |
| [ms_bind_msgr1](#ms_bind_msgr1) | `True` | Advanced | عملکرد |
| [ms_bind_msgr2](#ms_bind_msgr2) | `True` | Advanced | عملکرد |
| [ms_bind_port_max](#ms_bind_port_max) | `7568` | Advanced | عملکرد |
| [ms_bind_port_min](#ms_bind_port_min) | `6800` | Advanced | عملکرد |
| [ms_bind_prefer_ipv4](#ms_bind_prefer_ipv4) | `False` | Advanced | عملکرد |
| [ms_bind_retry_count](#ms_bind_retry_count) | `0` | Advanced | عملکرد |
| [ms_bind_retry_delay](#ms_bind_retry_delay) | `0` | Advanced | عملکرد |
| [ms_blackhole_client](#ms_blackhole_client) | `False` | Dev | توسعه |
| [ms_blackhole_mds](#ms_blackhole_mds) | `False` | Dev | توسعه |
| [ms_blackhole_mgr](#ms_blackhole_mgr) | `False` | Dev | توسعه |
| [ms_blackhole_mon](#ms_blackhole_mon) | `False` | Dev | توسعه |
| [ms_blackhole_osd](#ms_blackhole_osd) | `False` | Dev | توسعه |
| [ms_client_mode](#ms_client_mode) | `crc secure` | Basic | سیاست |
| [ms_client_throttle_retry_time_interval](#ms_client_throttle_retry_time_interval) | `5000` | Dev | توسعه |
| [ms_cluster_mode](#ms_cluster_mode) | `crc secure` | Basic | سیاست |
| [ms_cluster_type](#ms_cluster_type) | `(empty)` | Advanced | عملکرد |
| [ms_compress_secure](#ms_compress_secure) | `False` | Advanced | عملکرد |
| [ms_connection_idle_timeout](#ms_connection_idle_timeout) | `900` | Advanced | عملکرد |
| [ms_connection_ready_timeout](#ms_connection_ready_timeout) | `10` | Advanced | عملکرد |
| [ms_crc_data](#ms_crc_data) | `True` | Dev | توسعه |
| [ms_crc_header](#ms_crc_header) | `True` | Dev | توسعه |
| [ms_die_on_bad_msg](#ms_die_on_bad_msg) | `False` | Dev | توسعه |
| [ms_die_on_bug](#ms_die_on_bug) | `False` | Dev | توسعه |
| [ms_die_on_old_message](#ms_die_on_old_message) | `False` | Dev | توسعه |
| [ms_die_on_skipped_message](#ms_die_on_skipped_message) | `False` | Dev | توسعه |
| [ms_die_on_unhandled_msg](#ms_die_on_unhandled_msg) | `False` | Dev | توسعه |
| [ms_dispatch_throttle_bytes](#ms_dispatch_throttle_bytes) | `100_M` | Advanced | عملکرد |
| [ms_dpdk_coremask](#ms_dpdk_coremask) | `0xF` | Advanced | عملکرد |
| [ms_dpdk_debug_allow_loopback](#ms_dpdk_debug_allow_loopback) | `False` | Dev | توسعه |
| [ms_dpdk_devs_allowlist](#ms_dpdk_devs_allowlist) | `(empty)` | Advanced | عملکرد |
| [ms_dpdk_enable_tso](#ms_dpdk_enable_tso) | `True` | Advanced | سیاست |
| [ms_dpdk_gateway_ipv4_addr](#ms_dpdk_gateway_ipv4_addr) | `(empty)` | Advanced | اتصال |
| [ms_dpdk_host_ipv4_addr](#ms_dpdk_host_ipv4_addr) | `(empty)` | Advanced | اتصال |
| [ms_dpdk_hugepages](#ms_dpdk_hugepages) | `(empty)` | Advanced | عملکرد |
| [ms_dpdk_hw_flow_control](#ms_dpdk_hw_flow_control) | `True` | Advanced | عملکرد |
| [ms_dpdk_hw_queue_weight](#ms_dpdk_hw_queue_weight) | `1` | Advanced | عملکرد |
| [ms_dpdk_lro](#ms_dpdk_lro) | `True` | Advanced | عملکرد |
| [ms_dpdk_memory_channel](#ms_dpdk_memory_channel) | `4` | Advanced | عملکرد |
| [ms_dpdk_netmask_ipv4_addr](#ms_dpdk_netmask_ipv4_addr) | `(empty)` | Advanced | اتصال |
| [ms_dpdk_pmd](#ms_dpdk_pmd) | `(empty)` | Advanced | عملکرد |
| [ms_dpdk_port_id](#ms_dpdk_port_id) | `0` | Advanced | عملکرد |
| [ms_dpdk_rx_buffer_count_per_core](#ms_dpdk_rx_buffer_count_per_core) | `8192` | Advanced | عملکرد |
| [ms_dump_corrupt_message_level](#ms_dump_corrupt_message_level) | `1` | Advanced | عملکرد |
| [ms_dump_on_send](#ms_dump_on_send) | `False` | Advanced | عملکرد |
| [ms_initial_backoff](#ms_initial_backoff) | `0.2` | Advanced | عملکرد |
| [ms_inject_delay_max](#ms_inject_delay_max) | `1` | Dev | توسعه |
| [ms_inject_delay_probability](#ms_inject_delay_probability) | `0` | Dev | توسعه |
| [ms_inject_delay_type](#ms_inject_delay_type) | `(empty)` | Dev | توسعه |
| [ms_inject_internal_delays](#ms_inject_internal_delays) | `0` | Dev | توسعه |
| [ms_inject_network_congestion](#ms_inject_network_congestion) | `0` | Dev | توسعه |
| [ms_inject_socket_failures](#ms_inject_socket_failures) | `0` | Dev | توسعه |
| [ms_learn_addr_from_peer](#ms_learn_addr_from_peer) | `True` | Advanced | عملکرد |
| [ms_max_accept_failures](#ms_max_accept_failures) | `4` | Advanced | عملکرد |
| [ms_max_backoff](#ms_max_backoff) | `15` | Advanced | عملکرد |
| [ms_mon_client_mode](#ms_mon_client_mode) | `secure crc` | Basic | سیاست |
| [ms_mon_cluster_mode](#ms_mon_cluster_mode) | `secure crc` | Basic | سیاست |
| [ms_mon_service_mode](#ms_mon_service_mode) | `secure crc` | Basic | سیاست |
| [ms_osd_compress_min_size](#ms_osd_compress_min_size) | `1_K` | Advanced | عملکرد |
| [ms_osd_compress_mode](#ms_osd_compress_mode) | `none` | Advanced | عملکرد |
| [ms_osd_compression_algorithm](#ms_osd_compression_algorithm) | `snappy` | Advanced | عملکرد |
| [ms_pq_max_tokens_per_priority](#ms_pq_max_tokens_per_priority) | `16_M` | Dev | توسعه |
| [ms_pq_min_cost](#ms_pq_min_cost) | `64_K` | Dev | توسعه |
| [ms_public_type](#ms_public_type) | `(empty)` | Advanced | عملکرد |
| [ms_service_mode](#ms_service_mode) | `crc secure` | Basic | سیاست |
| [ms_tcp_listen_backlog](#ms_tcp_listen_backlog) | `512` | Advanced | عملکرد |
| [ms_tcp_nodelay](#ms_tcp_nodelay) | `True` | Advanced | عملکرد |
| [ms_tcp_prefetch_max_size](#ms_tcp_prefetch_max_size) | `64_K` | Advanced | عملکرد |
| [ms_tcp_rcvbuf](#ms_tcp_rcvbuf) | `0` | Advanced | عملکرد |
| [ms_time_events_min_wait_interval](#ms_time_events_min_wait_interval) | `1000` | Dev | توسعه |
| [ms_type](#ms_type) | `async+posix` | Advanced | عملکرد |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **سیاست** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **ظرفیت** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **عملکرد** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **اتصال** | نزدیک‌ترین نقطهٔ پایانی پایدار خارجی |
| **توسعه** | در محیط عملیاتی همان پیش‌فرض upstream |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### ms_async_op_threads

| | |
|---|---|
| نوع | Uint · default `3` · **Advanced** |
| جدول | [ms.md#SP_ms_async_op_threads](../../../config/global/ms.md#SP_ms_async_op_threads) |

**کارکرد:** Threadpool size for AsyncMessenger (ms_type=async)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_op_threads 3
ceph config get global ms_async_op_threads
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.

**محدوده:** حداقل `1`، حداکثر `24`.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_op_threads
ceph -s
```

---

### ms_async_rdma_buffer_size

| | |
|---|---|
| نوع | Size · default `128_K` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_buffer_size](../../../config/global/ms.md#SP_ms_async_rdma_buffer_size) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_buffer_size 128_K
ceph config get global ms_async_rdma_buffer_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `128_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_buffer_size
ceph -s
```

---

### ms_async_rdma_cm

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_cm](../../../config/global/ms.md#SP_ms_async_rdma_cm) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global ms_async_rdma_cm true
ceph config get global ms_async_rdma_cm
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_cm
ceph -s
```

---

### ms_async_rdma_device_name

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_device_name](../../../config/global/ms.md#SP_ms_async_rdma_device_name) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_device_name "example"
ceph config get global ms_async_rdma_device_name
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_device_name
ceph -s
```

---

### ms_async_rdma_dscp

| | |
|---|---|
| نوع | Int · default `96` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_dscp](../../../config/global/ms.md#SP_ms_async_rdma_dscp) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_dscp 96
ceph config get global ms_async_rdma_dscp
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `96`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_dscp
ceph -s
```

---

### ms_async_rdma_enable_hugepage

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_enable_hugepage](../../../config/global/ms.md#SP_ms_async_rdma_enable_hugepage) |

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global ms_async_rdma_enable_hugepage true
ceph config get global ms_async_rdma_enable_hugepage
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_enable_hugepage
ceph -s
```

---

### ms_async_rdma_gid_idx

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_gid_idx](../../../config/global/ms.md#SP_ms_async_rdma_gid_idx) |

**کارکرد:** use gid_idx to select GID for choosing RoCEv1 or RoCEv2

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_gid_idx 64
ceph config get global ms_async_rdma_gid_idx
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_gid_idx
ceph -s
```

---

### ms_async_rdma_local_gid

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_local_gid](../../../config/global/ms.md#SP_ms_async_rdma_local_gid) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_local_gid "example"
ceph config get global ms_async_rdma_local_gid
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_local_gid
ceph -s
```

---

### ms_async_rdma_polling_us

| | |
|---|---|
| نوع | Uint · default `1000` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_polling_us](../../../config/global/ms.md#SP_ms_async_rdma_polling_us) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_polling_us 1000
ceph config get global ms_async_rdma_polling_us
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1000`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_polling_us
ceph -s
```

---

### ms_async_rdma_port_num

| | |
|---|---|
| نوع | Uint · default `1` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_port_num](../../../config/global/ms.md#SP_ms_async_rdma_port_num) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_port_num 1
ceph config get global ms_async_rdma_port_num
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_port_num
ceph -s
```

---

### ms_async_rdma_receive_buffers

| | |
|---|---|
| نوع | Uint · default `32_K` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_receive_buffers](../../../config/global/ms.md#SP_ms_async_rdma_receive_buffers) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_receive_buffers 32_K
ceph config get global ms_async_rdma_receive_buffers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `32_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_receive_buffers
ceph -s
```

---

### ms_async_rdma_receive_queue_len

| | |
|---|---|
| نوع | Uint · default `4_K` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_receive_queue_len](../../../config/global/ms.md#SP_ms_async_rdma_receive_queue_len) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_receive_queue_len 4_K
ceph config get global ms_async_rdma_receive_queue_len
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_receive_queue_len
ceph -s
```

---

### ms_async_rdma_roce_ver

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_roce_ver](../../../config/global/ms.md#SP_ms_async_rdma_roce_ver) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_roce_ver 1
ceph config get global ms_async_rdma_roce_ver
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_roce_ver
ceph -s
```

---

### ms_async_rdma_send_buffers

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_send_buffers](../../../config/global/ms.md#SP_ms_async_rdma_send_buffers) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_send_buffers 1_K
ceph config get global ms_async_rdma_send_buffers
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_send_buffers
ceph -s
```

---

### ms_async_rdma_sl

| | |
|---|---|
| نوع | Int · default `3` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_sl](../../../config/global/ms.md#SP_ms_async_rdma_sl) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_sl 3
ceph config get global ms_async_rdma_sl
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `3`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_sl
ceph -s
```

---

### ms_async_rdma_support_srq

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_support_srq](../../../config/global/ms.md#SP_ms_async_rdma_support_srq) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_async_rdma_support_srq false
ceph config get global ms_async_rdma_support_srq
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_support_srq
ceph -s
```

---

### ms_async_rdma_type

| | |
|---|---|
| نوع | Str · default `ib` · **Advanced** |
| جدول | [ms.md#SP_ms_async_rdma_type](../../../config/global/ms.md#SP_ms_async_rdma_type) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_async_rdma_type ib
ceph config get global ms_async_rdma_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `ib`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_async_rdma_type
ceph -s
```

---

### ms_async_reap_threshold

| | |
|---|---|
| نوع | Uint · default `5` · **Dev** |
| جدول | [ms.md#SP_ms_async_reap_threshold](../../../config/global/ms.md#SP_ms_async_reap_threshold) |

**کارکرد:** number of deleted connections before we reap

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_async_reap_threshold 5
ceph config get global ms_async_reap_threshold
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_bind_before_connect

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_before_connect](../../../config/global/ms.md#SP_ms_bind_before_connect) |

**کارکرد:** Call bind(2) on client sockets

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global ms_bind_before_connect true
ceph config get global ms_bind_before_connect
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_before_connect
ceph -s
```

---

### ms_bind_ipv4

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_ipv4](../../../config/global/ms.md#SP_ms_bind_ipv4) |

**کارکرد:** Bind servers to IPv4 address(es)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`ms_bind_ipv6`](../../../config/global/ms.md#SP_ms_bind_ipv6)

**مثال:**

```bash
ceph config set global ms_bind_ipv4 false
ceph config get global ms_bind_ipv4
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_ipv4
ceph -s
```

---

### ms_bind_ipv6

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_ipv6](../../../config/global/ms.md#SP_ms_bind_ipv6) |

**کارکرد:** Bind servers to IPv6 address(es)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`ms_bind_ipv4`](../../../config/global/ms.md#SP_ms_bind_ipv4)

**مثال:**

```bash
ceph config set global ms_bind_ipv6 true
ceph config get global ms_bind_ipv6
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_ipv6
ceph -s
```

---

### ms_bind_msgr1

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_msgr1](../../../config/global/ms.md#SP_ms_bind_msgr1) |

**کارکرد:** Bind servers to msgr1 (legacy) protocol address(es)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`ms_bind_msgr2`](../../../config/global/ms.md#SP_ms_bind_msgr2)

**مثال:**

```bash
ceph config set global ms_bind_msgr1 false
ceph config get global ms_bind_msgr1
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_msgr1
ceph -s
```

---

### ms_bind_msgr2

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_msgr2](../../../config/global/ms.md#SP_ms_bind_msgr2) |

**کارکرد:** Bind servers to msgr2 (nautilus+) protocol address(es)

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**گزینه‌های مرتبط:**

- [`ms_bind_msgr1`](../../../config/global/ms.md#SP_ms_bind_msgr1)

**مثال:**

```bash
ceph config set global ms_bind_msgr2 false
ceph config get global ms_bind_msgr2
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_msgr2
ceph -s
```

---

### ms_bind_port_max

| | |
|---|---|
| نوع | Int · default `7568` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_port_max](../../../config/global/ms.md#SP_ms_bind_port_max) |

**کارکرد:** Highest port number to bind daemon(s) to

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_bind_port_max 7568
ceph config get global ms_bind_port_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `7568`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_port_max
ceph -s
```

---

### ms_bind_port_min

| | |
|---|---|
| نوع | Int · default `6800` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_port_min](../../../config/global/ms.md#SP_ms_bind_port_min) |

**کارکرد:** Lowest port number to bind daemon(s) to

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_bind_port_min 6800
ceph config get global ms_bind_port_min
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `6800`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_port_min
ceph -s
```

---

### ms_bind_prefer_ipv4

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_prefer_ipv4](../../../config/global/ms.md#SP_ms_bind_prefer_ipv4) |

**کارکرد:** Prefer IPV4 over IPV6 address(es)

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global ms_bind_prefer_ipv4 true
ceph config get global ms_bind_prefer_ipv4
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_prefer_ipv4
ceph -s
```

---

### ms_bind_retry_count

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_retry_count](../../../config/global/ms.md#SP_ms_bind_retry_count) |

**کارکرد:** Number of attempts to make while bind(2)ing to a port

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_bind_retry_count 64
ceph config get global ms_bind_retry_count
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_retry_count
ceph -s
```

---

### ms_bind_retry_delay

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [ms.md#SP_ms_bind_retry_delay](../../../config/global/ms.md#SP_ms_bind_retry_delay) |

**کارکرد:** Delay between bind(2) attempts (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_bind_retry_delay 64
ceph config get global ms_bind_retry_delay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_bind_retry_delay
ceph -s
```

---

### ms_blackhole_client

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_blackhole_client](../../../config/global/ms.md#SP_ms_blackhole_client) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_blackhole_client true
ceph config get global ms_blackhole_client
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_blackhole_mds

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_blackhole_mds](../../../config/global/ms.md#SP_ms_blackhole_mds) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_blackhole_mds true
ceph config get global ms_blackhole_mds
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_blackhole_mgr

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_blackhole_mgr](../../../config/global/ms.md#SP_ms_blackhole_mgr) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_blackhole_mgr true
ceph config get global ms_blackhole_mgr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_blackhole_mon

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_blackhole_mon](../../../config/global/ms.md#SP_ms_blackhole_mon) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_blackhole_mon true
ceph config get global ms_blackhole_mon
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_blackhole_osd

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_blackhole_osd](../../../config/global/ms.md#SP_ms_blackhole_osd) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_blackhole_osd true
ceph config get global ms_blackhole_osd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_client_mode

| | |
|---|---|
| نوع | Str · default `crc secure` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_client_mode](../../../config/global/ms.md#SP_ms_client_mode) |

**کارکرد:** Connection modes (crc, secure) for connections from clients in order of preference

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_client_mode "crc secure"
ceph config get global ms_client_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `crc secure` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_client_mode
ceph -s
```

---

### ms_client_throttle_retry_time_interval

| | |
|---|---|
| نوع | Uint · default `5000` · **Dev** |
| جدول | [ms.md#SP_ms_client_throttle_retry_time_interval](../../../config/global/ms.md#SP_ms_client_throttle_retry_time_interval) |

**کارکرد:** In microseconds, user client, the time interval between the next retry when the throttle get_or_fail.

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_client_throttle_retry_time_interval 5000
ceph config get global ms_client_throttle_retry_time_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`5000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_cluster_mode

| | |
|---|---|
| نوع | Str · default `crc secure` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_cluster_mode](../../../config/global/ms.md#SP_ms_cluster_mode) |

**کارکرد:** Connection modes (crc, secure) for intra-cluster connections in order of preference

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_cluster_mode "crc secure"
ceph config get global ms_cluster_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `crc secure` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_cluster_mode
ceph -s
```

---

### ms_cluster_type

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_cluster_type](../../../config/global/ms.md#SP_ms_cluster_type) |

**کارکرد:** Messenger implementation to use for the internal cluster network If not specified, use ms_type

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**مثال:**

```bash
ceph config set global ms_cluster_type "example"
ceph config get global ms_cluster_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_cluster_type
ceph -s
```

---

### ms_compress_secure

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_compress_secure](../../../config/global/ms.md#SP_ms_compress_secure) |

**کارکرد:** Allowing compression when on-wire encryption is enabled Combining encryption with compression reduces the level of security of messages between peers. In case both encryption and compression are enabled, compression setting will be ignored and message will not be compressed. This behaviour can be override using this setting.

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**گزینه‌های مرتبط:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**مثال:**

```bash
ceph config set global ms_compress_secure true
ceph config get global ms_compress_secure
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_compress_secure
ceph -s
```

---

### ms_connection_idle_timeout

| | |
|---|---|
| نوع | Uint · default `900` · **Advanced** |
| جدول | [ms.md#SP_ms_connection_idle_timeout](../../../config/global/ms.md#SP_ms_connection_idle_timeout) |

**کارکرد:** Time before an idle connection is closed (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global ms_connection_idle_timeout 900
ceph config get global ms_connection_idle_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `900`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_connection_idle_timeout
ceph -s
```

---

### ms_connection_ready_timeout

| | |
|---|---|
| نوع | Uint · default `10` · **Advanced** |
| جدول | [ms.md#SP_ms_connection_ready_timeout](../../../config/global/ms.md#SP_ms_connection_ready_timeout) |

**کارکرد:** Time before we declare a not yet ready connection as dead (seconds)

**زمان استفاده:** زمان‌بندی کار پس‌زمینه را تنظیم کنید — تعادل بین تازگی و بار کلاستر.

**مثال:**

```bash
ceph config set global ms_connection_ready_timeout 10
ceph config get global ms_connection_ready_timeout
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `10`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_connection_ready_timeout
ceph -s
```

---

### ms_crc_data

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [ms.md#SP_ms_crc_data](../../../config/global/ms.md#SP_ms_crc_data) |

**کارکرد:** Set and/or verify crc32c checksum on data payload sent over network

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_crc_data false
ceph config get global ms_crc_data
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_crc_header

| | |
|---|---|
| نوع | Bool · default `True` · **Dev** |
| جدول | [ms.md#SP_ms_crc_header](../../../config/global/ms.md#SP_ms_crc_header) |

**کارکرد:** Set and/or verify crc32c checksum on header payload sent over network

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_crc_header false
ceph config get global ms_crc_header
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`True`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_die_on_bad_msg

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_die_on_bad_msg](../../../config/global/ms.md#SP_ms_die_on_bad_msg) |

**کارکرد:** Induce a daemon crash/exit when a bad network message is received

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_die_on_bad_msg true
ceph config get global ms_die_on_bad_msg
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_die_on_bug

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_die_on_bug](../../../config/global/ms.md#SP_ms_die_on_bug) |

**کارکرد:** Induce a crash/exit on various bugs (for testing purposes)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_die_on_bug true
ceph config get global ms_die_on_bug
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_die_on_old_message

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_die_on_old_message](../../../config/global/ms.md#SP_ms_die_on_old_message) |

**کارکرد:** Induce a daemon crash/exit when a old, undecodable message is received

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_die_on_old_message true
ceph config get global ms_die_on_old_message
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_die_on_skipped_message

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_die_on_skipped_message](../../../config/global/ms.md#SP_ms_die_on_skipped_message) |

**کارکرد:** Induce a daemon crash/exit if sender skips a message sequence number

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_die_on_skipped_message true
ceph config get global ms_die_on_skipped_message
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_die_on_unhandled_msg

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_die_on_unhandled_msg](../../../config/global/ms.md#SP_ms_die_on_unhandled_msg) |

**کارکرد:** Induce a daemon crash/exit when an unrecognized message is received

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_die_on_unhandled_msg true
ceph config get global ms_die_on_unhandled_msg
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_dispatch_throttle_bytes

| | |
|---|---|
| نوع | Size · default `100_M` · **Advanced** |
| جدول | [ms.md#SP_ms_dispatch_throttle_bytes](../../../config/global/ms.md#SP_ms_dispatch_throttle_bytes) |

**کارکرد:** Limit messages that are read off the network but still being processed

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dispatch_throttle_bytes 100_M
ceph config get global ms_dispatch_throttle_bytes
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `100_M`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dispatch_throttle_bytes
ceph -s
```

---

### ms_dpdk_coremask

| | |
|---|---|
| نوع | Str · default `0xF` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_coremask](../../../config/global/ms.md#SP_ms_dpdk_coremask) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`ms_async_op_threads`](../../../config/global/ms.md#SP_ms_async_op_threads)

**مثال:**

```bash
ceph config set global ms_dpdk_coremask 0xF
ceph config get global ms_dpdk_coremask
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0xF`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_coremask
ceph -s
```

---

### ms_dpdk_debug_allow_loopback

| | |
|---|---|
| نوع | Bool · default `False` · **Dev** |
| جدول | [ms.md#SP_ms_dpdk_debug_allow_loopback](../../../config/global/ms.md#SP_ms_dpdk_debug_allow_loopback) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_dpdk_debug_allow_loopback true
ceph config get global ms_dpdk_debug_allow_loopback
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`False`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_dpdk_devs_allowlist

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_devs_allowlist](../../../config/global/ms.md#SP_ms_dpdk_devs_allowlist) |

**کارکرد:** NIC's PCIe address are allowed to use for a single NIC use ms_dpdk_devs_allowlist=-a 0000:7d:010 or --allow=0000:7d:010; for a bond nics use ms_dpdk_devs_allowlist=--allow=0000:7d:01.0 --allow=0000:7d:02.6 --vdev=net_bonding0,mode=2,slave=0000:7d:01.0,slave=0000:7d:02.6.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_devs_allowlist "example"
ceph config get global ms_dpdk_devs_allowlist
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_devs_allowlist
ceph -s
```

---

### ms_dpdk_enable_tso

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_enable_tso](../../../config/global/ms.md#SP_ms_dpdk_enable_tso) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_dpdk_enable_tso false
ceph config get global ms_dpdk_enable_tso
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `True` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_enable_tso
ceph -s
```

---

### ms_dpdk_gateway_ipv4_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_gateway_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_gateway_ipv4_addr) |

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global ms_dpdk_gateway_ipv4_addr "example"
ceph config get global ms_dpdk_gateway_ipv4_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** اتصال

1. نقاط پایانی (endpoint) کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. پایدارترین نقطهٔ پایانی با کمترین تأخیر (latency) را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_gateway_ipv4_addr
ceph -s
```

---

### ms_dpdk_host_ipv4_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_host_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_host_ipv4_addr) |

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global ms_dpdk_host_ipv4_addr "example"
ceph config get global ms_dpdk_host_ipv4_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** اتصال

1. نقاط پایانی (endpoint) کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. پایدارترین نقطهٔ پایانی با کمترین تأخیر (latency) را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_host_ipv4_addr
ceph -s
```

---

### ms_dpdk_hugepages

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_hugepages](../../../config/global/ms.md#SP_ms_dpdk_hugepages) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_hugepages "example"
ceph config get global ms_dpdk_hugepages
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_hugepages
ceph -s
```

---

### ms_dpdk_hw_flow_control

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_hw_flow_control](../../../config/global/ms.md#SP_ms_dpdk_hw_flow_control) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_dpdk_hw_flow_control false
ceph config get global ms_dpdk_hw_flow_control
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_hw_flow_control
ceph -s
```

---

### ms_dpdk_hw_queue_weight

| | |
|---|---|
| نوع | Float · default `1` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_hw_queue_weight](../../../config/global/ms.md#SP_ms_dpdk_hw_queue_weight) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_hw_queue_weight 1
ceph config get global ms_dpdk_hw_queue_weight
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_hw_queue_weight
ceph -s
```

---

### ms_dpdk_lro

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_lro](../../../config/global/ms.md#SP_ms_dpdk_lro) |

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_dpdk_lro false
ceph config get global ms_dpdk_lro
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_lro
ceph -s
```

---

### ms_dpdk_memory_channel

| | |
|---|---|
| نوع | Str · default `4` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_memory_channel](../../../config/global/ms.md#SP_ms_dpdk_memory_channel) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_memory_channel 4
ceph config get global ms_dpdk_memory_channel
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_memory_channel
ceph -s
```

---

### ms_dpdk_netmask_ipv4_addr

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_netmask_ipv4_addr](../../../config/global/ms.md#SP_ms_dpdk_netmask_ipv4_addr) |

**زمان استفاده:** هنگام یکپارچه‌سازی با سرویس خارجی تنظیم کنید؛ اگر استفاده نمی‌شود خالی بگذارید.

**مثال:**

```bash
ceph config set global ms_dpdk_netmask_ipv4_addr "example"
ceph config get global ms_dpdk_netmask_ipv4_addr
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** اتصال

1. نقاط پایانی (endpoint) کاندید را از محیط خود فهرست کنید.
2. دسترسی‌پذیری از هر نودی که دیمن روی آن اجرا می‌شود را بررسی کنید.
3. پایدارترین نقطهٔ پایانی با کمترین تأخیر (latency) را انتخاب کنید.
4. اگر یکپارچه‌سازی غیرفعال است خالی (`(empty)`) بگذارید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_netmask_ipv4_addr
ceph -s
```

---

### ms_dpdk_pmd

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_pmd](../../../config/global/ms.md#SP_ms_dpdk_pmd) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_pmd "example"
ceph config get global ms_dpdk_pmd
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_pmd
ceph -s
```

---

### ms_dpdk_port_id

| | |
|---|---|
| نوع | Int · default `0` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_port_id](../../../config/global/ms.md#SP_ms_dpdk_port_id) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_port_id 64
ceph config get global ms_dpdk_port_id
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_port_id
ceph -s
```

---

### ms_dpdk_rx_buffer_count_per_core

| | |
|---|---|
| نوع | Int · default `8192` · **Advanced** |
| جدول | [ms.md#SP_ms_dpdk_rx_buffer_count_per_core](../../../config/global/ms.md#SP_ms_dpdk_rx_buffer_count_per_core) |

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dpdk_rx_buffer_count_per_core 8192
ceph config get global ms_dpdk_rx_buffer_count_per_core
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `8192`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dpdk_rx_buffer_count_per_core
ceph -s
```

---

### ms_dump_corrupt_message_level

| | |
|---|---|
| نوع | Int · default `1` · **Advanced** |
| جدول | [ms.md#SP_ms_dump_corrupt_message_level](../../../config/global/ms.md#SP_ms_dump_corrupt_message_level) |

**کارکرد:** Log level at which to hexdump corrupt messages we receive

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_dump_corrupt_message_level 1
ceph config get global ms_dump_corrupt_message_level
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dump_corrupt_message_level
ceph -s
```

---

### ms_dump_on_send

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [ms.md#SP_ms_dump_on_send](../../../config/global/ms.md#SP_ms_dump_on_send) |

**کارکرد:** Hexdump message to debug log on message send

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به این قابلیت نیاز دارید و مبادله‌های آن را می‌پذیرید، فعال کنید.

**مثال:**

```bash
ceph config set global ms_dump_on_send true
ceph config get global ms_dump_on_send
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `False`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_dump_on_send
ceph -s
```

---

### ms_initial_backoff

| | |
|---|---|
| نوع | Float · default `0.2` · **Advanced** |
| جدول | [ms.md#SP_ms_initial_backoff](../../../config/global/ms.md#SP_ms_initial_backoff) |

**کارکرد:** Initial backoff after a network error is detected (seconds)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_initial_backoff 0.2
ceph config get global ms_initial_backoff
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0.2`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_initial_backoff
ceph -s
```

---

### ms_inject_delay_max

| | |
|---|---|
| نوع | Float · default `1` · **Dev** |
| جدول | [ms.md#SP_ms_inject_delay_max](../../../config/global/ms.md#SP_ms_inject_delay_max) |

**کارکرد:** Max delay to inject

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_delay_max 1
ceph config get global ms_inject_delay_max
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_inject_delay_probability

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [ms.md#SP_ms_inject_delay_probability](../../../config/global/ms.md#SP_ms_inject_delay_probability) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_delay_probability 0
ceph config get global ms_inject_delay_probability
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_inject_delay_type

| | |
|---|---|
| نوع | Str · default `(empty)` · **Dev** |
| جدول | [ms.md#SP_ms_inject_delay_type](../../../config/global/ms.md#SP_ms_inject_delay_type) |

**کارکرد:** Entity type to inject delays for

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_delay_type "example"
ceph config get global ms_inject_delay_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`(empty)`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_inject_internal_delays

| | |
|---|---|
| نوع | Float · default `0` · **Dev** |
| جدول | [ms.md#SP_ms_inject_internal_delays](../../../config/global/ms.md#SP_ms_inject_internal_delays) |

**کارکرد:** Inject various internal delays to induce races (seconds)

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_internal_delays 0
ceph config get global ms_inject_internal_delays
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_inject_network_congestion

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [ms.md#SP_ms_inject_network_congestion](../../../config/global/ms.md#SP_ms_inject_network_congestion) |

**کارکرد:** Inject a network congestions that stuck with N times operations

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_network_congestion 64
ceph config get global ms_inject_network_congestion
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_inject_socket_failures

| | |
|---|---|
| نوع | Uint · default `0` · **Dev** |
| جدول | [ms.md#SP_ms_inject_socket_failures](../../../config/global/ms.md#SP_ms_inject_socket_failures) |

**کارکرد:** Inject a socket failure every Nth socket operation

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_inject_socket_failures 64
ceph config get global ms_inject_socket_failures
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`0`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_learn_addr_from_peer

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_learn_addr_from_peer](../../../config/global/ms.md#SP_ms_learn_addr_from_peer) |

**کارکرد:** Learn address from what IP our first peer thinks we connect from Use the IP address our first peer (usually a monitor) sees that we are connecting from. This is useful if a client is behind some sort of NAT and we want to see it identified by its local (not NATed) address.

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_learn_addr_from_peer false
ceph config get global ms_learn_addr_from_peer
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_learn_addr_from_peer
ceph -s
```

---

### ms_max_accept_failures

| | |
|---|---|
| نوع | Int · default `4` · **Advanced** |
| جدول | [ms.md#SP_ms_max_accept_failures](../../../config/global/ms.md#SP_ms_max_accept_failures) |

**کارکرد:** The maximum number of consecutive failed accept() calls before considering the daemon is misconfigured and abort it.

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global ms_max_accept_failures 4
ceph config get global ms_max_accept_failures
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `4`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_max_accept_failures
ceph -s
```

---

### ms_max_backoff

| | |
|---|---|
| نوع | Float · default `15` · **Advanced** |
| جدول | [ms.md#SP_ms_max_backoff](../../../config/global/ms.md#SP_ms_max_backoff) |

**کارکرد:** Maximum backoff after a network error before retrying (seconds)

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`ms_initial_backoff`](../../../config/global/ms.md#SP_ms_initial_backoff)

**مثال:**

```bash
ceph config set global ms_max_backoff 15
ceph config get global ms_max_backoff
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `15`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_max_backoff
ceph -s
```

---

### ms_mon_client_mode

| | |
|---|---|
| نوع | Str · default `secure crc` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_mon_client_mode](../../../config/global/ms.md#SP_ms_mon_client_mode) |

**کارکرد:** Connection modes (crc, secure) for connections from clients to monitors in order of preference

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_mon_client_mode "secure crc"
ceph config get global ms_mon_client_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `secure crc` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_mon_client_mode
ceph -s
```

---

### ms_mon_cluster_mode

| | |
|---|---|
| نوع | Str · default `secure crc` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_mon_cluster_mode](../../../config/global/ms.md#SP_ms_mon_cluster_mode) |

**کارکرد:** Connection modes (crc, secure) for intra-mon connections in order of preference

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_mon_cluster_mode "secure crc"
ceph config get global ms_mon_cluster_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `secure crc` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_mon_cluster_mode
ceph -s
```

---

### ms_mon_service_mode

| | |
|---|---|
| نوع | Str · default `secure crc` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_mon_service_mode](../../../config/global/ms.md#SP_ms_mon_service_mode) |

**کارکرد:** Allowed connection modes (crc, secure) for connections to mons

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_mon_service_mode "secure crc"
ceph config get global ms_mon_service_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `secure crc` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_mon_service_mode
ceph -s
```

---

### ms_osd_compress_min_size

| | |
|---|---|
| نوع | Uint · default `1_K` · **Advanced** |
| جدول | [ms.md#SP_ms_osd_compress_min_size](../../../config/global/ms.md#SP_ms_osd_compress_min_size) |

**کارکرد:** Minimal message size eligable for on-wire compression

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**گزینه‌های مرتبط:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**مثال:**

```bash
ceph config set global ms_osd_compress_min_size 1_K
ceph config get global ms_osd_compress_min_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `1_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_osd_compress_min_size
ceph -s
```

---

### ms_osd_compress_mode

| | |
|---|---|
| نوع | Str · enum: ["none", "force"] · default `none` · **Advanced** |
| جدول | [ms.md#SP_ms_osd_compress_mode](../../../config/global/ms.md#SP_ms_osd_compress_mode) |

**کارکرد:** Compression policy to use in Messenger for communicating with OSD

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`ms_compress_secure`](../../../config/global/ms.md#SP_ms_compress_secure)

**مثال:**

```bash
ceph config set global ms_osd_compress_mode none
ceph config get global ms_osd_compress_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `none`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_osd_compress_mode
ceph -s
```

---

### ms_osd_compression_algorithm

| | |
|---|---|
| نوع | Str · default `snappy` · **Advanced** |
| جدول | [ms.md#SP_ms_osd_compression_algorithm](../../../config/global/ms.md#SP_ms_osd_compression_algorithm) |

**کارکرد:** Compression algorithm to use in Messenger when communicating with OSD Compression algorithm for connections with OSD in order of preference Although the default value is set to snappy, a list (like snappy zlib zstd etc.) is acceptable as well.

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`ms_osd_compress_mode`](../../../config/global/ms.md#SP_ms_osd_compress_mode)

**مثال:**

```bash
ceph config set global ms_osd_compression_algorithm snappy
ceph config get global ms_osd_compression_algorithm
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `snappy`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_osd_compression_algorithm
ceph -s
```

---

### ms_pq_max_tokens_per_priority

| | |
|---|---|
| نوع | Uint · default `16_M` · **Dev** |
| جدول | [ms.md#SP_ms_pq_max_tokens_per_priority](../../../config/global/ms.md#SP_ms_pq_max_tokens_per_priority) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_pq_max_tokens_per_priority 16_M
ceph config get global ms_pq_max_tokens_per_priority
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`16_M`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_pq_min_cost

| | |
|---|---|
| نوع | Size · default `64_K` · **Dev** |
| جدول | [ms.md#SP_ms_pq_min_cost](../../../config/global/ms.md#SP_ms_pq_min_cost) |

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_pq_min_cost 64_K
ceph config get global ms_pq_min_cost
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`64_K`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_public_type

| | |
|---|---|
| نوع | Str · default `(empty)` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_public_type](../../../config/global/ms.md#SP_ms_public_type) |

**کارکرد:** Messenger implementation to use for the public network If not specified, use ms_type

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**گزینه‌های مرتبط:**

- [`ms_type`](../../../config/global/ms.md#SP_ms_type)

**مثال:**

```bash
ceph config set global ms_public_type "example"
ceph config get global ms_public_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `(empty)`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_public_type
ceph -s
```

---

### ms_service_mode

| | |
|---|---|
| نوع | Str · default `crc secure` · **Basic** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_service_mode](../../../config/global/ms.md#SP_ms_service_mode) |

**کارکرد:** Allowed connection modes (crc, secure) for connections to daemons

**زمان استفاده:** رفتار اصلی Global — پیش از تغییر در محیط عملیاتی بررسی کنید.

**مثال:**

```bash
ceph config set global ms_service_mode "crc secure"
ceph config get global ms_service_mode
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** سیاست

1. مستند کنید چرا `crc secure` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات، روندهای کاری کلاینت و مدیر را آزمایش کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_service_mode
ceph -s
```

---

### ms_tcp_listen_backlog

| | |
|---|---|
| نوع | Int · default `512` · **Advanced** |
| جدول | [ms.md#SP_ms_tcp_listen_backlog](../../../config/global/ms.md#SP_ms_tcp_listen_backlog) |

**کارکرد:** Size of queue of incoming connections for accept(2)

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_tcp_listen_backlog 512
ceph config get global ms_tcp_listen_backlog
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `512`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_tcp_listen_backlog
ceph -s
```

---

### ms_tcp_nodelay

| | |
|---|---|
| نوع | Bool · default `True` · **Advanced** |
| جدول | [ms.md#SP_ms_tcp_nodelay](../../../config/global/ms.md#SP_ms_tcp_nodelay) |

**کارکرد:** Disable Nagle's algorithm and send queued network traffic immediately

**زمان استفاده:** به‌طور پیش‌فرض فعال است؛ فقط هنگام عیب‌یابی قابلیت مرتبط غیرفعال کنید.

**مثال:**

```bash
ceph config set global ms_tcp_nodelay false
ceph config get global ms_tcp_nodelay
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `True`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_tcp_nodelay
ceph -s
```

---

### ms_tcp_prefetch_max_size

| | |
|---|---|
| نوع | Size · default `64_K` · **Advanced** |
| جدول | [ms.md#SP_ms_tcp_prefetch_max_size](../../../config/global/ms.md#SP_ms_tcp_prefetch_max_size) |

**کارکرد:** Maximum amount of data to prefetch out of the socket receive buffer

**زمان استفاده:** وقتی به محدودیت منابع می‌رسید یا ظرفیت کلاستر را محافظت می‌کنید تنظیم کنید.

**مثال:**

```bash
ceph config set global ms_tcp_prefetch_max_size 64_K
ceph config get global ms_tcp_prefetch_max_size
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `64_K`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_tcp_prefetch_max_size
ceph -s
```

---

### ms_tcp_rcvbuf

| | |
|---|---|
| نوع | Size · default `0` · **Advanced** |
| جدول | [ms.md#SP_ms_tcp_rcvbuf](../../../config/global/ms.md#SP_ms_tcp_rcvbuf) |

**کارکرد:** Size of TCP socket receive buffer

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_tcp_rcvbuf 64
ceph config get global ms_tcp_rcvbuf
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `0`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_tcp_rcvbuf
ceph -s
```

---

### ms_time_events_min_wait_interval

| | |
|---|---|
| نوع | Uint · default `1000` · **Dev** |
| جدول | [ms.md#SP_ms_time_events_min_wait_interval](../../../config/global/ms.md#SP_ms_time_events_min_wait_interval) |

**کارکرد:** In microseconds, msgr-worker's time_events min wait time for epoll_wait timeout

**زمان استفاده:** فقط برای توسعه، آزمایش یا اشکال‌زدایی upstream — نه برای تنظیم در محیط عملیاتی.

**مثال:**

```bash
ceph config set global ms_time_events_min_wait_interval 1000
ceph config get global ms_time_events_min_wait_interval
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** توسعه

1. پیش‌فرض upstream (`1000`) را در محیط عملیاتی نگه دارید.
2. فقط در آزمایشگاه (lab) هنگام بازتولید یک مشکل مشخص تغییر دهید.
3. پیش از بازگرداندن نود به مجموعهٔ عملیاتی، مقدار را برگردانید.

---

### ms_type

| | |
|---|---|
| نوع | Str · default `async+posix` · **Advanced** · **STARTUP** (نیاز به راه‌اندازی مجدد) |
| جدول | [ms.md#SP_ms_type](../../../config/global/ms.md#SP_ms_type) |

**کارکرد:** Messenger implementation to use for network communication

**زمان استفاده:** تنظیم پیشرفته — فقط با بار کاری اندازه‌گیری‌شده و برنامهٔ بازگشت (rollback) از پیش‌فرض upstream فاصله بگیرید.

**مثال:**

```bash
ceph config set global ms_type async+posix
ceph config get global ms_type
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** عملکرد

1. خط پایه روی پیش‌فرض upstream `async+posix`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. تأخیر (latency)، توان عملیاتی (throughput) و کار پس‌زمینه را قبل و بعد مقایسه کنید.
4. اگر سلامت کلاستر بدتر شد یا slow ops افزایش یافت، بازگشت (rollback) کنید.
**شاخص‌های پایش:** `ceph -s`، slow ops، شمارنده‌های عملکرد دیمن، صف بازیابی و scrub.

```bash
ceph config get global ms_type
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
