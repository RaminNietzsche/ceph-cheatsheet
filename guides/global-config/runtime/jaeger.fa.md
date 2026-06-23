# Jaeger

deep dive پیکربندی Global — 2 گزینه. [← نمای کلی](../OVERVIEW.md) · [فهرست تنظیم](../TUNING.md) · [INDEX](../../../config/global/INDEX.md)

| گزینه | پیش‌فرض | سطح | تنظیم |
|--------|---------|-------|--------|
| [jaeger_agent_port](#jaeger_agent_port) | `6799` | Advanced | Performance |
| [jaeger_tracing_enable](#jaeger_tracing_enable) | `False` | Advanced | Policy |

## یافتن مقادیر بهینه

| مدل | نحوه انتخاب |
|-------|---------------|
| **Policy** | امنیت، سازگاری، پیش‌فرض‌های عملیاتی |
| **Capacity** | چیدمان دیسک، مسیرها، اندازه‌گیری |
| **Performance** | خط پایه → تغییر تدریجی → پایش کلاستر |
| **Connectivity** | نزدیک‌ترین endpoint پایدار خارجی |
| **Dev** | پیش‌فرض upstream در production |

**ابزارهای مشترک:**

```bash
ceph config get <daemon> <option>  # e.g. global
ceph -s
./scripts/lookup-config.sh <option-name>
```

---

### jaeger_agent_port

| | |
|---|---|
| نوع | Int · default `6799` · **Advanced** |
| جدول | [jaeger.md#SP_jaeger_agent_port](../../../config/global/jaeger.md#SP_jaeger_agent_port) |

**کارکرد:** TCP port number of the Jaeger agent

**زمان استفاده:** تنظیم پیشرفته — فقط با workload اندازه‌گیری‌شده و برنامه rollback از پیش‌فرض upstream تغییر دهید.

**مثال:**

```bash
ceph config set global jaeger_agent_port 6799
ceph config get global jaeger_agent_port
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Performance

1. خط پایه روی پیش‌فرض upstream `6799`.
2. در هر پنجره تست تحت بار نماینده **یک** گزینه را تغییر دهید.
3. latency، throughput و کار پس‌زمینه را قبل/بعد مقایسه کنید.
4. اگر health بدتر شد یا slow ops افزایش یافت rollback کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global jaeger_agent_port
ceph -s
```

---

### jaeger_tracing_enable

| | |
|---|---|
| نوع | Bool · default `False` · **Advanced** |
| جدول | [jaeger.md#SP_jaeger_tracing_enable](../../../config/global/jaeger.md#SP_jaeger_tracing_enable) |

**کارکرد:** Ceph should use the Jaeger tracing system

**زمان استفاده:** به‌طور پیش‌فرض غیرفعال است؛ وقتی به قابلیت نیاز دارید و trade-off را می‌پذیرید فعال کنید.

**مثال:**

```bash
ceph config set global jaeger_tracing_enable true
ceph config get global jaeger_tracing_enable
```

**یافتن مقدار بهینه:**

**مدل تنظیم:** Policy

1. مستند کنید چرا `False` برای سیاست شما درست است.
2. فقط برای الزامات سازگاری یا امنیت تغییر دهید.
3. پس از تغییرات workflow کلاینت و admin را تست کنید.
**سیگنال‌ها:** `ceph -s`، slow ops، شمارنده‌های perf دیمن، backlog بازیابی/scrub.

```bash
ceph config get global jaeger_tracing_enable
ceph -s
```

---


[← نمای کلی](../OVERVIEW.md)
