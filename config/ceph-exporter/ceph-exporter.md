<div class="level-legend"><span class="badge badge-level-basic">Basic</span><span class="badge badge-level-advanced">Advanced</span><span class="badge badge-level-dev">Dev</span></div>

| Name | Desc | Level | Type | non-Daemon Default | Daemon Default | Min | Max | Valid Values | verbatim | See also | Flags | Services | Validator | Long Desc | Tags |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <span id="SP_exporter_addr">exporter_addr</span> |  Host ip address where exporter is deployed | <span class="badge badge-level-advanced">Advanced</span> | Str | 0.0.0.0 |  |  |  |  |  |  |  | ceph-exporter |  |  |  |
| <span id="SP_exporter_cert_file">exporter_cert_file</span> |  Certificate file for TLS. | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  |  |  | ceph-exporter |  |  |  |
| <span id="SP_exporter_http_port">exporter_http_port</span> |  Port to deploy exporter on. Default is 9926 | <span class="badge badge-level-advanced">Advanced</span> | Int | 9926 |  |  |  |  |  |  |  | ceph-exporter |  |  |  |
| <span id="SP_exporter_key_file">exporter_key_file</span> |  Key certificate file for TLS. | <span class="badge badge-level-advanced">Advanced</span> | Str |  |  |  |  |  |  |  |  | ceph-exporter |  |  |  |
| <span id="SP_exporter_prio_limit">exporter_prio_limit</span> |  Only perf counters greater than or equal to exporter_prio_limit are fetched | <span class="badge badge-level-advanced">Advanced</span> | Int | 5 |  |  |  |  |  |  | RUNTIME | ceph-exporter |  |  |  |
| <span id="SP_exporter_sock_dir">exporter_sock_dir</span> |  The path to ceph daemons socket files dir | <span class="badge badge-level-advanced">Advanced</span> | Str | /var/run/ceph/ |  |  |  |  |  |  | RUNTIME | ceph-exporter |  |  |  |
| <span id="SP_exporter_sort_metrics">exporter_sort_metrics</span> |  If true it will sort the metrics and group them. | <span class="badge badge-level-advanced">Advanced</span> | Bool | True |  |  |  |  |  |  | RUNTIME | ceph-exporter |  |  |  |
| <span id="SP_exporter_stats_period">exporter_stats_period</span> |  Time to wait before sending requests again to exporter server (seconds) | <span class="badge badge-level-advanced">Advanced</span> | Int | 5 |  |  |  |  |  |  | RUNTIME | ceph-exporter |  |  |  |
