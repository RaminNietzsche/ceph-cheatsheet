import { useState, useEffect, useCallback, useRef } from "react";

// ─── Raw pages data (406 pages) ──────────────────────────────────────────────
const RAW_PAGES = [{"path":"AGENTS.md","cat":"Agents.Md","subcat":"","title":"Agent instructions","preview":"This repository is **ceph-cheatsheet** — an offline Ceph CLI and config reference. 1. Read `.cursor/skills/ceph-cheatsheet/SKILL.md` 2. Follow `.curso","chars":931,"status":"pending","note":"","rating":0},{"path":"REFERENCE.md","cat":"Reference.Md","subcat":"","title":"Ceph Reference","preview":"Simple, offline-friendly reference for Ceph administrators — organized by **role**, **scale**, **CLI**, and **config**. **Source:** [ceph/ceph](https:","chars":5286,"status":"pending","note":"","rating":0},{"path":"arch/index.md","cat":"Architecture","subcat":"","title":"Architecture","preview":"[← Home](../index.md) How Ceph subsystems work — request paths, storage layers, and code landmarks. More subsystems may be added later (OSD, MON, …).","chars":333,"status":"pending","note":"","rating":0},{"path":"arch/rgw/OVERVIEW.md","cat":"Architecture","subcat":"rgw","title":"Ceph RADOS Gateway — technical documentation","preview":"Developer documentation for the Ceph **RADOS Gateway (RGW)**. It explains architecture, request flow, storage layers, and code landmarks **without bro","chars":1209,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/critical-gaps-and-ha-limitations.md","cat":"Architecture","subcat":"rgw","title":"Critical gaps and HA limitations","preview":"Honest analysis for capacity and availability planning.","chars":1083,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/deployment-architecture.md","cat":"Architecture","subcat":"rgw","title":"Deployment architecture","preview":"flowchart TB LB[Load balancer] --> RGW1[radosgw] LB --> RGW2[radosgw] RGW1 --> RADOS[RADOS cluster] RGW2 --> RADOS - **Stateless gateways**","chars":948,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/dmclock-architecture.md","cat":"Architecture","subcat":"rgw","title":"dmclock / scheduler architecture","preview":"Scheduling and QoS at the RGW edge: from **SimpleThrottler** (production default) to **dmclock** (experimental).","chars":1820,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/object-lifecycle.md","cat":"Architecture","subcat":"rgw","title":"Object lifecycle","preview":"stateDiagram-v2 [*] --> Absent Absent --> Present: PUT / CompleteMultipart Present --> Present: PUT overwrite","chars":1255,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/observability-overview.md","cat":"Architecture","subcat":"rgw","title":"Observability overview","preview":"503 SlowDown — scheduling or rate limits. Sync lag — secondary zones falling behind.","chars":839,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/rate-limit-architecture.md","cat":"Architecture","subcat":"rgw","title":"Rate limit architecture","preview":"Per-user and per-bucket rate limiting in RGW — applied after authentication via ActiveRateLimiter and token-bucket counters in process memory.","chars":1419,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/request-pipeline.md","cat":"Architecture","subcat":"rgw","title":"HTTP request pipeline","preview":"From edge to storage: 1. Parse HTTP — RGWEnv, headers, URI 2. REST routing — RGWREST::get_handler() 3. Select operation","chars":1352,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/runtime-topology.md","cat":"Architecture","subcat":"rgw","title":"Runtime topology","preview":"A typical radosgw process: connects to Ceph cluster (MON+OSD), loads realm/period/zone, builds SAL driver stack.","chars":1669,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/scheduling-architecture.md","cat":"Architecture","subcat":"rgw","title":"Scheduling and QoS architecture","preview":"RGW has three concurrency limit layers at different pipeline points.","chars":1309,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/sequence-diagrams.md","cat":"Architecture","subcat":"rgw","title":"Sequence diagrams","preview":"High-level HTTP flows. sequenceDiagram autonumber participant C as Client participant FE as Frontend","chars":998,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/system-overview.md","cat":"Architecture","subcat":"rgw","title":"System overview","preview":"RADOS Gateway (RGW) is Ceph's object gateway. It exposes Amazon S3, OpenStack Swift, and related APIs on a Ceph cluster.","chars":1918,"status":"pending","note":"","rating":0},{"path":"arch/rgw/architecture/worker-architecture.md","cat":"Architecture","subcat":"rgw","title":"Worker and request queue architecture","preview":"RGW follows Frontend → Processor → Handler → Operation pipeline.","chars":1317,"status":"pending","note":"","rating":0},{"path":"cli/OVERVIEW.md","cat":"CLI","subcat":"","title":"CLI Command Reference","preview":"Essential Ceph commands for day-to-day cluster administration.","chars":2506,"status":"pending","note":"","rating":0},{"path":"cli/cephadm.md","cat":"CLI","subcat":"","title":"Cephadm & Orchestrator Commands","preview":"cephadm bootstrap --mon-ip <ip> [--cluster-network …] [--single-host-defaults]","chars":1679,"status":"pending","note":"","rating":0},{"path":"cli/cephfs.md","cat":"CLI","subcat":"","title":"CephFS Commands","preview":"ceph fs ls | ceph fs volume ls | ceph fs new <fs-name> <metadata-pool> <data-pool>","chars":1549,"status":"pending","note":"","rating":0},{"path":"cli/cluster.md","cat":"CLI","subcat":"","title":"Cluster & Monitor Commands","preview":"ceph status | ceph -w | ceph health | ceph health detail","chars":1951,"status":"pending","note":"","rating":0},{"path":"cli/config.md","cat":"CLI","subcat":"","title":"Configuration Commands","preview":"Runtime config is stored in the monitor config database.","chars":1744,"status":"pending","note":"","rating":0},{"path":"cli/osd-pool.md","cat":"CLI","subcat":"","title":"OSD, Pool & PG Commands","preview":"ceph osd tree | ceph osd ls | ceph osd find <id>","chars":2472,"status":"pending","note":"","rating":0},{"path":"cli/rados.md","cat":"CLI","subcat":"","title":"RADOS Commands","preview":"Low-level object storage interface. Pool name usually required via -p or --pool.","chars":1541,"status":"pending","note":"","rating":0},{"path":"cli/rbd.md","cat":"CLI","subcat":"","title":"RBD Commands","preview":"rbd ls [-p pool] | rbd ls -l [-p pool] | rbd info <pool>/<image>","chars":2211,"status":"pending","note":"","rating":0},{"path":"cli/rgw.md","cat":"CLI","subcat":"","title":"RGW (S3) Commands","preview":"RGW admin uses radosgw-admin. Gateway daemons are managed via cephadm.","chars":2174,"status":"pending","note":"","rating":0},{"path":"cli/troubleshooting.md","cat":"CLI","subcat":"","title":"Troubleshooting Commands","preview":"ceph log last [n] | ceph log dump | journalctl -u ceph-osd@<id> -f","chars":2001,"status":"pending","note":"","rating":0},{"path":"config/OVERVIEW.md","cat":"Config Tables","subcat":"","title":"Ceph Configuration Reference","preview":"Browse by subsystem. Each section has an option index and detailed tables.","chars":3491,"status":"pending","note":"","rating":0},{"path":"config/examples/OVERVIEW.md","cat":"Config Tables","subcat":"examples","title":"Production configuration examples","preview":"Commented ceph.conf fragments and rationale for common deployment scales.","chars":739,"status":"pending","note":"","rating":0},{"path":"config/examples/lab.md","cat":"Config Tables","subcat":"examples","title":"Lab / development example","preview":"Single-host or 3-node lab. Not for production data.","chars":1247,"status":"pending","note":"","rating":0},{"path":"config/examples/large-production.md","cat":"Config Tables","subcat":"examples","title":"Large production example","preview":"12+ nodes, many OSDs, strict SLAs, performance tuning.","chars":1382,"status":"pending","note":"","rating":0},{"path":"config/examples/multisite.md","cat":"Config Tables","subcat":"examples","title":"Multisite example","preview":"RGW realm → zonegroup → zones across datacenters.","chars":1574,"status":"pending","note":"","rating":0},{"path":"config/examples/rgw-optimized.md","cat":"Config Tables","subcat":"examples","title":"RGW optimized example","preview":"Settings for a production object gateway cluster (single or multisite).","chars":1354,"status":"pending","note":"","rating":0},{"path":"config/examples/small-production.md","cat":"Config Tables","subcat":"examples","title":"Small production example","preview":"Typical 3–12 nodes, one datacenter, replica 3, cephadm-managed.","chars":1466,"status":"pending","note":"","rating":0},{"path":"docs/compatibility.md","cat":"Docs","subcat":"","title":"Ceph version compatibility","preview":"This repository tracks Ceph upstream main by default.","chars":2058,"status":"pending","note":"","rating":0},{"path":"docs/index.md","cat":"Docs","subcat":"","title":"Hub homepage","preview":"Main hub page with navigation to all sections.","chars":7882,"status":"pending","note":"","rating":0},{"path":"docs/version.md","cat":"Docs","subcat":"","title":"Upstream source","preview":"Config tables are generated from Ceph upstream YAML. ref: main, generated: 2026-06-23.","chars":164,"status":"pending","note":"","rating":0},{"path":"guides/OVERVIEW.md","cat":"Guides","subcat":"","title":"Guides","preview":"Task-oriented documentation organized by role and cluster scale.","chars":2726,"status":"pending","note":"","rating":0},{"path":"guides/config-lookup.md","cat":"Guides","subcat":"","title":"Using the Config Reference","preview":"The config section is auto-generated from Ceph upstream YAML. Each option is a row in a Markdown table.","chars":1834,"status":"pending","note":"","rating":0},{"path":"guides/contributing.md","cat":"Guides","subcat":"","title":"Contributing to the Reference","preview":"How this repository is structured, maintained, and extended.","chars":2852,"status":"pending","note":"","rating":0},{"path":"guides/getting-started.md","cat":"Guides","subcat":"","title":"Getting Started","preview":"New to Ceph? Start here before diving into config tables or RGW internals.","chars":2711,"status":"pending","note":"","rating":0},{"path":"guides/quickstart.md","cat":"Guides","subcat":"","title":"Quick Start — Daily Admin Workflow","preview":"A minimal workflow for operating a Ceph cluster.","chars":1737,"status":"pending","note":"","rating":0},{"path":"guides/troubleshooting-guide.md","cat":"Guides","subcat":"","title":"Troubleshooting Guide","preview":"Structured diagnosis for common production issues.","chars":3201,"status":"pending","note":"","rating":0},{"path":"guides/roles/cephfs-admin.md","cat":"Guides","subcat":"roles","title":"CephFS Admin","preview":"Manage Ceph file systems, metadata servers (MDS), subvolumes, and mirroring.","chars":1613,"status":"pending","note":"","rating":0},{"path":"guides/roles/cluster-admin.md","cat":"Guides","subcat":"roles","title":"Cluster Admin","preview":"Manage monitors, managers, orchestration, cluster health, auth, and upgrades.","chars":2108,"status":"pending","note":"","rating":0},{"path":"guides/roles/rgw-admin.md","cat":"Guides","subcat":"roles","title":"RGW Admin","preview":"Manage RADOS Gateway — S3/Swift, users, buckets, quotas, and multisite.","chars":3011,"status":"pending","note":"","rating":0},{"path":"guides/roles/storage-operator.md","cat":"Guides","subcat":"roles","title":"Storage Operator","preview":"Manage OSDs, pools, placement groups, CRUSH, recovery, and scrub.","chars":1926,"status":"pending","note":"","rating":0},{"path":"guides/scales/lab.md","cat":"Guides","subcat":"scales","title":"Lab / Development Scale","preview":"1–3 nodes, testing, learning, CI — not for production data.","chars":1911,"status":"pending","note":"","rating":0},{"path":"guides/scales/large-production.md","cat":"Guides","subcat":"scales","title":"Large Production Scale","preview":"12+ nodes, many OSDs, strict SLAs, separate networks, performance tuning.","chars":2107,"status":"pending","note":"","rating":0},{"path":"guides/scales/multisite.md","cat":"Guides","subcat":"scales","title":"Multisite Scale","preview":"Multiple datacenters or regions — RGW zones, optional RBD / CephFS mirroring.","chars":2415,"status":"pending","note":"","rating":0},{"path":"guides/scales/small-production.md","cat":"Guides","subcat":"scales","title":"Small Production Scale","preview":"Typically 3–12 nodes, one datacenter, replica 3, cephadm-managed.","chars":1892,"status":"pending","note":"","rating":0},{"path":"guides/osd-config/OVERVIEW.md","cat":"Guides","subcat":"osd-config","title":"OSD Config Deep Dive — All Options","preview":"Extended reference for all 158 OSD options with Finding optimal value guidance.","chars":1290,"status":"pending","note":"","rating":0},{"path":"guides/osd-config/TUNING.md","cat":"Guides","subcat":"osd-config","title":"OSD Config — Tuning Quick Reference","preview":"All 158 options with tuning model and one-line guidance.","chars":29489,"status":"pending","note":"","rating":0},{"path":"guides/osd-config/recovery/recovery.md","cat":"Guides","subcat":"osd-config","title":"Recovery & backfill","preview":"OSD config deep dive — 28 options.","chars":32322,"status":"pending","note":"","rating":0},{"path":"guides/osd-config/scrub/scrub.md","cat":"Guides","subcat":"osd-config","title":"Scrub","preview":"OSD config deep dive — 39 options.","chars":44097,"status":"pending","note":"","rating":0},{"path":"guides/osd-config/mclock/mclock.md","cat":"Guides","subcat":"osd-config","title":"mClock scheduler","preview":"OSD config deep dive — 18 options.","chars":23839,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/OVERVIEW.md","cat":"Guides","subcat":"rgw-config","title":"RGW Config Deep Dive — All Options","preview":"Extended reference for all 441 RGW options with Finding optimal value guidance.","chars":4080,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/TUNING.md","cat":"Guides","subcat":"rgw-config","title":"RGW Config — Tuning Quick Reference","preview":"All 441 RGW options with tuning model and one-line guidance.","chars":97244,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/core-gateway/frontends.md","cat":"Guides","subcat":"rgw-config","title":"Frontends & HTTP stack","preview":"RGW config deep dive — 6 options.","chars":7593,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/core-gateway/feature-toggles.md","cat":"Guides","subcat":"rgw-config","title":"Feature toggles","preview":"RGW config deep dive — 10 options.","chars":9691,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/core-gateway/scheduler-dmclock.md","cat":"Guides","subcat":"rgw-config","title":"Scheduler & dmclock","preview":"RGW config deep dive — 13 options.","chars":16856,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/performance-io/performance-tuning.md","cat":"Guides","subcat":"rgw-config","title":"Concurrency & RADOS I/O","preview":"RGW config deep dive — 14 options.","chars":16113,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/security-auth/encryption.md","cat":"Guides","subcat":"rgw-config","title":"Encryption & KMS","preview":"RGW config deep dive — 43 options.","chars":49173,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/security-auth/keystone-sts.md","cat":"Guides","subcat":"rgw-config","title":"Keystone & STS","preview":"RGW config deep dive — 32 options.","chars":35080,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/buckets-lifecycle/lifecycle.md","cat":"Guides","subcat":"rgw-config","title":"Lifecycle (LC)","preview":"RGW config deep dive — 17 options.","chars":17232,"status":"pending","note":"","rating":0},{"path":"guides/rgw-config/notifications/notifications.md","cat":"Guides","subcat":"rgw-config","title":"Bucket notifications","preview":"RGW config deep dive — 13 options.","chars":15692,"status":"pending","note":"","rating":0},{"path":"guides/mon-config/OVERVIEW.md","cat":"Guides","subcat":"mon-config","title":"MON Config Deep Dive — All Options","preview":"Extended reference for all 156 MON options.","chars":1276,"status":"pending","note":"","rating":0},{"path":"guides/mon-config/quorum/quorum-paxos.md","cat":"Guides","subcat":"mon-config","title":"Quorum & Paxos","preview":"MON config deep dive — 14 options.","chars":14017,"status":"pending","note":"","rating":0},{"path":"guides/global-config/OVERVIEW.md","cat":"Guides","subcat":"global-config","title":"Global Config Deep Dive — All Options","preview":"Extended reference for all 852 Global options.","chars":3393,"status":"pending","note":"","rating":0},{"path":"guides/mds-config/OVERVIEW.md","cat":"Guides","subcat":"mds-config","title":"MDS Config Deep Dive — All Options","preview":"Extended reference for all 194 MDS options.","chars":850,"status":"pending","note":"","rating":0},{"path":"guides/rbd-config/OVERVIEW.md","cat":"Guides","subcat":"rbd-config","title":"RBD Config Deep Dive — All Options","preview":"Extended reference for all 97 RBD options.","chars":1793,"status":"pending","note":"","rating":0}];

const STORAGE_KEY = "ceph_review_v3";
const CATS = ["همه", "CLI", "Config Tables", "Guides", "Architecture", "Docs"];
const STATUS_OPTS = ["همه", "pending", "approved", "needs-fix", "skip"];

const STATUS_META = {
  pending:    { label: "بررسی نشده", color: "#64748b", bg: "#1e293b" },
  approved:   { label: "✓ تأیید شد",  color: "#22c55e", bg: "#052e16" },
  "needs-fix":{ label: "⚠ نیاز به اصلاح", color: "#f59e0b", bg: "#451a03" },
  skip:       { label: "↷ رد شد",     color: "#94a3b8", bg: "#0f172a" },
};

const GITHUB_BASE = "https://github.com/RaminNietzsche/ceph-cheatsheet/blob/main/";

function loadData() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) {
      const saved = JSON.parse(raw);
      return RAW_PAGES.map(p => ({
        ...p,
        ...(saved[p.path] || {}),
      }));
    }
  } catch {}
  return RAW_PAGES.map(p => ({ ...p }));
}

function saveData(pages) {
  const obj = {};
  pages.forEach(p => {
    obj[p.path] = { status: p.status, note: p.note, rating: p.rating };
  });
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(obj)); } catch {}
}

export default function App() {
  const [pages, setPages] = useState(() => loadData());
  const [selected, setSelected] = useState(null);
  const [filterCat, setFilterCat] = useState("همه");
  const [filterStatus, setFilterStatus] = useState("همه");
  const [search, setSearch] = useState("");
  const [aiLoading, setAiLoading] = useState(false);
  const [aiResult, setAiResult] = useState(null);
  const [noteText, setNoteText] = useState("");
  const [view, setView] = useState("list"); // list | detail
  const noteRef = useRef(null);

  const updatePage = useCallback((path, changes) => {
    setPages(prev => {
      const next = prev.map(p => p.path === path ? { ...p, ...changes } : p);
      saveData(next);
      return next;
    });
    if (selected?.path === path) {
      setSelected(p => ({ ...p, ...changes }));
    }
  }, [selected]);

  const filtered = pages.filter(p => {
    if (filterCat !== "همه" && p.cat !== filterCat) return false;
    if (filterStatus !== "همه" && p.status !== filterStatus) return false;
    if (search && !p.title.toLowerCase().includes(search.toLowerCase()) &&
        !p.path.toLowerCase().includes(search.toLowerCase())) return false;
    return true;
  });

  const stats = {
    total: pages.length,
    approved: pages.filter(p => p.status === "approved").length,
    needsFix: pages.filter(p => p.status === "needs-fix").length,
    skip: pages.filter(p => p.status === "skip").length,
    pending: pages.filter(p => p.status === "pending").length,
  };

  const pct = Math.round((stats.approved + stats.needsFix + stats.skip) / stats.total * 100);

  const openPage = (page) => {
    setSelected(page);
    setNoteText(page.note || "");
    setAiResult(null);
    setView("detail");
  };

  const goBack = () => { setView("list"); setSelected(null); setAiResult(null); };

  const nextPage = () => {
    if (!selected) return;
    const idx = filtered.findIndex(p => p.path === selected.path);
    if (idx < filtered.length - 1) openPage(filtered[idx + 1]);
  };
  const prevPage = () => {
    if (!selected) return;
    const idx = filtered.findIndex(p => p.path === selected.path);
    if (idx > 0) openPage(filtered[idx - 1]);
  };

  const setStatus = (status) => {
    if (!selected) return;
    updatePage(selected.path, { status, note: noteText });
  };

  const saveNote = () => {
    if (!selected) return;
    updatePage(selected.path, { note: noteText });
  };

  const runAI = async () => {
    if (!selected) return;
    setAiLoading(true);
    setAiResult(null);
    try {
      const prompt = `You are a senior Ceph SRE and technical writer reviewing documentation pages for the "ceph-cheatsheet" open source project.

Page path: ${selected.path}
Category: ${selected.cat} / ${selected.subcat || "—"}
Title: ${selected.title}
Size: ${selected.chars} characters

Preview content:
${selected.preview}

Review this documentation page and provide a structured assessment with these sections:

1. **خلاصه محتوا** (1-2 جمله فارسی: این صفحه چه می‌گوید؟)
2. **مشکلات احتمالی** (لیست نقاط ضعف محتوایی، فنی، یا ساختاری)  
3. **پیشنهاد بهبود** (اقدامات مشخص که می‌توان انجام داد)
4. **وضعیت پیشنهادی**: یکی از: approved / needs-fix / skip

پاسخ را به فارسی بده. اگر صفحه کوچک و auto-generated است (مثل config table)، آن را سریع بررسی کن.`;

      const res = await fetch("https://api.anthropic.com/v1/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          model: "claude-sonnet-4-6",
          max_tokens: 1000,
          messages: [{ role: "user", content: prompt }],
        }),
      });
      const data = await res.json();
      const text = data.content?.map(b => b.text || "").join("") || "خطا در دریافت پاسخ";
      setAiResult(text);

      // Auto-extract suggested status
      const lower = text.toLowerCase();
      if (lower.includes("needs-fix") || lower.includes("نیاز به اصلاح")) {
        // Don't auto-apply, let user decide
      }
    } catch (e) {
      setAiResult("⚠ خطا در ارتباط با API: " + e.message);
    } finally {
      setAiLoading(false);
    }
  };

  const exportCSV = () => {
    const rows = [["path", "title", "cat", "status", "rating", "note"]];
    pages.forEach(p => {
      rows.push([p.path, p.title, p.cat, p.status, p.rating, (p.note || "").replace(/,/g, ";")]);
    });
    const csv = rows.map(r => r.join(",")).join("\n");
    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a"); a.href = url; a.download = "ceph-review.csv"; a.click();
  };

  const resetAll = () => {
    if (confirm("تمام بررسی‌ها پاک شود؟")) {
      const reset = RAW_PAGES.map(p => ({ ...p }));
      setPages(reset);
      saveData(reset);
      setSelected(null); setView("list");
    }
  };

  // ── Styles ──────────────────────────────────────────────────────────────────
  const s = {
    app: {
      minHeight: "100vh", background: "#060d1a", color: "#e2e8f0",
      fontFamily: "'JetBrains Mono', 'Fira Code', monospace",
      direction: "rtl",
    },
    header: {
      background: "#0a1628", borderBottom: "1px solid #1e3a5f",
      padding: "12px 20px", display: "flex", alignItems: "center", gap: 12,
      position: "sticky", top: 0, zIndex: 100,
    },
    logo: {
      fontSize: 20, fontWeight: 700, color: "#38bdf8",
      letterSpacing: "-0.5px", fontFamily: "inherit",
    },
    badge: (color, bg) => ({
      background: bg, color: color, fontSize: 11, padding: "2px 8px",
      borderRadius: 4, fontWeight: 600, border: `1px solid ${color}22`,
    }),
    progressBar: {
      flex: 1, height: 6, background: "#1e293b", borderRadius: 3, overflow: "hidden",
    },
    progressFill: {
      height: "100%", width: pct + "%",
      background: "linear-gradient(90deg, #0ea5e9, #22d3ee)",
      borderRadius: 3, transition: "width 0.4s",
    },
    sidebar: {
      width: 320, background: "#080f1c", borderLeft: "1px solid #1e3a5f",
      height: "calc(100vh - 53px)", overflowY: "auto", position: "sticky", top: 53,
      flexShrink: 0,
    },
    main: { flex: 1, padding: 20, overflowY: "auto", height: "calc(100vh - 53px)" },
    filterBar: {
      background: "#0a1628", border: "1px solid #1e3a5f", borderRadius: 8,
      padding: 12, marginBottom: 16, display: "flex", gap: 8, flexWrap: "wrap",
      alignItems: "center",
    },
    input: {
      background: "#060d1a", border: "1px solid #1e3a5f", color: "#e2e8f0",
      padding: "6px 10px", borderRadius: 6, fontSize: 13, outline: "none",
      fontFamily: "inherit",
    },
    select: {
      background: "#060d1a", border: "1px solid #1e3a5f", color: "#e2e8f0",
      padding: "6px 10px", borderRadius: 6, fontSize: 12, fontFamily: "inherit",
    },
    card: (status) => ({
      background: STATUS_META[status]?.bg || "#0a1628",
      border: `1px solid ${status === "approved" ? "#22c55e33" : status === "needs-fix" ? "#f59e0b33" : "#1e3a5f"}`,
      borderRadius: 8, padding: "10px 14px", cursor: "pointer", marginBottom: 6,
      transition: "border-color 0.15s",
    }),
    cardTitle: { fontSize: 13, fontWeight: 600, color: "#f1f5f9", marginBottom: 3 },
    cardMeta: { fontSize: 11, color: "#64748b", display: "flex", gap: 8 },
    btn: (color = "#0ea5e9", bg = "#0c3a5f") => ({
      background: bg, color: color, border: `1px solid ${color}44`,
      padding: "7px 14px", borderRadius: 6, cursor: "pointer", fontSize: 12,
      fontWeight: 600, fontFamily: "inherit", transition: "background 0.15s",
    }),
    btnGroup: { display: "flex", gap: 8, flexWrap: "wrap" },
    detailBox: {
      background: "#0a1628", border: "1px solid #1e3a5f", borderRadius: 8, padding: 16,
    },
    tag: (color) => ({
      background: color + "22", color, border: `1px solid ${color}44`,
      fontSize: 11, padding: "2px 8px", borderRadius: 4, fontWeight: 600,
    }),
    aiBox: {
      background: "#060d1a", border: "1px solid #1e3a5f", borderRadius: 8,
      padding: 14, marginTop: 12, fontSize: 13, lineHeight: 1.8, whiteSpace: "pre-wrap",
      color: "#cbd5e1",
    },
    textarea: {
      width: "100%", minHeight: 80, background: "#060d1a", border: "1px solid #1e3a5f",
      color: "#e2e8f0", padding: 10, borderRadius: 6, fontSize: 13, fontFamily: "inherit",
      resize: "vertical", outline: "none", boxSizing: "border-box",
    },
    statRow: {
      display: "flex", gap: 12, marginBottom: 16, flexWrap: "wrap",
    },
    stat: (color) => ({
      background: "#0a1628", border: `1px solid ${color}33`, borderRadius: 8,
      padding: "8px 14px", color, fontSize: 13, fontWeight: 700, flex: "1 1 80px",
      textAlign: "center",
    }),
  };

  // ── List View ────────────────────────────────────────────────────────────────
  const ListView = () => (
    <div style={{ display: "flex", gap: 0 }}>
      {/* List */}
      <div style={s.sidebar}>
        <div style={{ padding: "10px 12px", borderBottom: "1px solid #1e3a5f", fontSize: 12, color: "#64748b" }}>
          {filtered.length} صفحه
        </div>
        {filtered.map((p, i) => {
          const sm = STATUS_META[p.status] || STATUS_META.pending;
          return (
            <div key={p.path} style={s.card(p.status)} onClick={() => openPage(p)}>
              <div style={s.cardTitle}>{p.title}</div>
              <div style={s.cardMeta}>
                <span style={{ color: sm.color, fontSize: 10, fontWeight: 700 }}>{sm.label}</span>
                <span>{p.cat}</span>
                <span>{(p.chars / 1000).toFixed(1)}k</span>
              </div>
            </div>
          );
        })}
      </div>

      {/* Main stats */}
      <div style={s.main}>
        <div style={s.statRow}>
          <div style={s.stat("#38bdf8")}><div style={{ fontSize: 22 }}>{stats.total}</div><div style={{ fontSize: 10, marginTop: 2, color: "#94a3b8" }}>کل صفحات</div></div>
          <div style={s.stat("#22c55e")}><div style={{ fontSize: 22 }}>{stats.approved}</div><div style={{ fontSize: 10, marginTop: 2, color: "#94a3b8" }}>تأیید شده</div></div>
          <div style={s.stat("#f59e0b")}><div style={{ fontSize: 22 }}>{stats.needsFix}</div><div style={{ fontSize: 10, marginTop: 2, color: "#94a3b8" }}>نیاز به اصلاح</div></div>
          <div style={s.stat("#64748b")}><div style={{ fontSize: 22 }}>{stats.skip}</div><div style={{ fontSize: 10, marginTop: 2, color: "#94a3b8" }}>رد شده</div></div>
          <div style={s.stat("#818cf8")}><div style={{ fontSize: 22 }}>{stats.pending}</div><div style={{ fontSize: 10, marginTop: 2, color: "#94a3b8" }}>بررسی نشده</div></div>
        </div>

        <div style={{ ...s.detailBox, marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
            <span style={{ fontSize: 13, color: "#94a3b8" }}>پیشرفت بررسی</span>
            <span style={{ fontSize: 13, color: "#38bdf8", fontWeight: 700 }}>{pct}%</span>
          </div>
          <div style={s.progressBar}><div style={s.progressFill} /></div>
          <div style={{ fontSize: 11, color: "#475569", marginTop: 6 }}>
            {stats.approved + stats.needsFix + stats.skip} از {stats.total} صفحه بررسی شده
          </div>
        </div>

        <div style={{ ...s.detailBox, padding: "10px 14px", marginBottom: 16 }}>
          <div style={{ fontSize: 12, color: "#64748b", marginBottom: 8 }}>توزیع بر اساس دسته</div>
          {["CLI", "Config Tables", "Guides", "Architecture", "Docs"].map(cat => {
            const total = pages.filter(p => p.cat === cat).length;
            const done = pages.filter(p => p.cat === cat && p.status !== "pending").length;
            return (
              <div key={cat} style={{ marginBottom: 6 }}>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 12, marginBottom: 2 }}>
                  <span style={{ color: "#cbd5e1" }}>{cat}</span>
                  <span style={{ color: "#64748b" }}>{done}/{total}</span>
                </div>
                <div style={{ height: 4, background: "#1e293b", borderRadius: 2 }}>
                  <div style={{ height: "100%", width: (total ? done / total * 100 : 0) + "%", background: "#0ea5e9", borderRadius: 2 }} />
                </div>
              </div>
            );
          })}
        </div>

        <div style={s.btnGroup}>
          <button style={s.btn("#38bdf8", "#0c3a5f")} onClick={exportCSV}>⬇ خروجی CSV</button>
          <button style={s.btn("#f87171", "#2d0a0a")} onClick={resetAll}>↺ ریست همه</button>
        </div>

        <div style={{ marginTop: 16, fontSize: 12, color: "#475569", lineHeight: 1.7 }}>
          💡 از سایدبار صفحه را انتخاب کنید یا روی کارت کلیک کنید تا جزئیات و بررسی AI را ببینید.
        </div>
      </div>
    </div>
  );

  // ── Detail View ──────────────────────────────────────────────────────────────
  const DetailView = () => {
    if (!selected) return null;
    const sm = STATUS_META[selected.status] || STATUS_META.pending;
    const idx = filtered.findIndex(p => p.path === selected.path);
    const githubUrl = GITHUB_BASE + selected.path;

    return (
      <div style={{ display: "flex", gap: 0 }}>
        {/* Mini list sidebar */}
        <div style={s.sidebar}>
          {filtered.map(p => {
            const psm = STATUS_META[p.status] || STATUS_META.pending;
            const isActive = p.path === selected.path;
            return (
              <div
                key={p.path}
                onClick={() => openPage(p)}
                style={{
                  padding: "8px 12px", cursor: "pointer", borderBottom: "1px solid #0f1d2e",
                  background: isActive ? "#0e2040" : "transparent",
                  borderRight: isActive ? "3px solid #38bdf8" : "3px solid transparent",
                }}
              >
                <div style={{ fontSize: 12, color: isActive ? "#f1f5f9" : "#94a3b8", marginBottom: 2, lineHeight: 1.3 }}>{p.title}</div>
                <div style={{ fontSize: 10, color: psm.color }}>{psm.label}</div>
              </div>
            );
          })}
        </div>

        {/* Detail main */}
        <div style={{ ...s.main, overflowY: "auto" }}>
          {/* Nav */}
          <div style={{ display: "flex", gap: 8, marginBottom: 16, alignItems: "center" }}>
            <button style={s.btn("#94a3b8", "#1e293b")} onClick={goBack}>← برگشت</button>
            <button style={s.btn("#64748b", "#1e293b")} onClick={prevPage} disabled={idx <= 0}>‹ قبلی</button>
            <span style={{ fontSize: 12, color: "#64748b" }}>{idx + 1} / {filtered.length}</span>
            <button style={s.btn("#64748b", "#1e293b")} onClick={nextPage} disabled={idx >= filtered.length - 1}>بعدی ›</button>
            <a href={githubUrl} target="_blank" rel="noopener" style={{ ...s.btn("#818cf8", "#1e1a3f"), textDecoration: "none" }}>
              ⎋ GitHub
            </a>
          </div>

          {/* Page info */}
          <div style={{ ...s.detailBox, marginBottom: 12 }}>
            <div style={{ display: "flex", gap: 8, marginBottom: 10, flexWrap: "wrap", alignItems: "center" }}>
              <span style={s.tag("#38bdf8")}>{selected.cat}</span>
              {selected.subcat && <span style={s.tag("#818cf8")}>{selected.subcat}</span>}
              <span style={s.tag(sm.color)}>{sm.label}</span>
              <span style={{ fontSize: 11, color: "#475569", marginRight: "auto" }}>
                {(selected.chars / 1000).toFixed(1)}k chars
              </span>
            </div>
            <h2 style={{ fontSize: 18, fontWeight: 700, color: "#f1f5f9", margin: "0 0 6px" }}>{selected.title}</h2>
            <div style={{ fontSize: 11, color: "#475569", marginBottom: 10, fontFamily: "monospace" }}>{selected.path}</div>
            <div style={{ fontSize: 13, color: "#94a3b8", lineHeight: 1.6, borderTop: "1px solid #1e3a5f", paddingTop: 10 }}>
              {selected.preview}
            </div>
          </div>

          {/* Actions */}
          <div style={{ ...s.detailBox, marginBottom: 12 }}>
            <div style={{ fontSize: 12, color: "#64748b", marginBottom: 10 }}>وضعیت بررسی</div>
            <div style={s.btnGroup}>
              <button
                style={{ ...s.btn("#22c55e", selected.status === "approved" ? "#052e16" : "#1e293b"), border: selected.status === "approved" ? "2px solid #22c55e" : undefined }}
                onClick={() => setStatus("approved")}
              >✓ تأیید</button>
              <button
                style={{ ...s.btn("#f59e0b", selected.status === "needs-fix" ? "#451a03" : "#1e293b"), border: selected.status === "needs-fix" ? "2px solid #f59e0b" : undefined }}
                onClick={() => setStatus("needs-fix")}
              >⚠ نیاز به اصلاح</button>
              <button
                style={{ ...s.btn("#94a3b8", selected.status === "skip" ? "#1e293b" : "#1e293b"), border: selected.status === "skip" ? "2px solid #94a3b8" : undefined }}
                onClick={() => setStatus("skip")}
              >↷ رد</button>
            </div>
          </div>

          {/* Note */}
          <div style={{ ...s.detailBox, marginBottom: 12 }}>
            <div style={{ fontSize: 12, color: "#64748b", marginBottom: 8 }}>یادداشت شخصی</div>
            <textarea
              ref={noteRef}
              style={s.textarea}
              value={noteText}
              onChange={e => setNoteText(e.target.value)}
              placeholder="یادداشت، مشکلات دیده شده، یا اقدامات لازم..."
            />
            <button style={{ ...s.btn("#38bdf8", "#0c3a5f"), marginTop: 8 }} onClick={saveNote}>ذخیره یادداشت</button>
          </div>

          {/* AI Review */}
          <div style={s.detailBox}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 10 }}>
              <div style={{ fontSize: 12, color: "#64748b" }}>بررسی هوشمند (AI)</div>
              <button style={s.btn("#a78bfa", "#1e1440")} onClick={runAI} disabled={aiLoading}>
                {aiLoading ? "⏳ در حال بررسی..." : "✦ بررسی با AI"}
              </button>
            </div>
            {aiLoading && (
              <div style={{ textAlign: "center", padding: 20, color: "#475569", fontSize: 13 }}>
                <div style={{ marginBottom: 8, fontSize: 20 }}>⚙</div>
                در حال تحلیل صفحه...
              </div>
            )}
            {aiResult && (
              <div style={s.aiBox}>
                {aiResult}
                <div style={{ marginTop: 12, paddingTop: 12, borderTop: "1px solid #1e3a5f", display: "flex", gap: 8 }}>
                  <button style={s.btn("#22c55e", "#052e16")} onClick={() => { setStatus("approved"); }}>✓ تأیید</button>
                  <button style={s.btn("#f59e0b", "#451a03")} onClick={() => { setStatus("needs-fix"); }}>⚠ اصلاح</button>
                  <button style={s.btn("#94a3b8", "#1e293b")} onClick={() => { setStatus("skip"); }}>↷ رد</button>
                </div>
              </div>
            )}
            {!aiResult && !aiLoading && (
              <div style={{ fontSize: 12, color: "#334155", padding: "10px 0" }}>
                روی «بررسی با AI» کلیک کنید تا Claude صفحه را تحلیل کند و مشکلات احتمالی را شناسایی کند.
              </div>
            )}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div style={s.app}>
      {/* Header */}
      <div style={s.header}>
        <div style={s.logo}>🐙 Ceph Review</div>
        <div style={{ ...s.progressBar, maxWidth: 200 }}><div style={s.progressFill} /></div>
        <span style={{ fontSize: 12, color: "#38bdf8", fontWeight: 700 }}>{pct}%</span>
        <div style={{ marginRight: "auto" }} />

        {/* Filters */}
        <input
          style={{ ...s.input, width: 160 }}
          placeholder="جستجوی صفحه..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
        <select style={s.select} value={filterCat} onChange={e => setFilterCat(e.target.value)}>
          {CATS.map(c => <option key={c}>{c}</option>)}
        </select>
        <select style={s.select} value={filterStatus} onChange={e => setFilterStatus(e.target.value)}>
          {STATUS_OPTS.map(s => <option key={s}>{s}</option>)}
        </select>

        <div style={{ display: "flex", gap: 6, fontSize: 11 }}>
          <span style={s.badge("#22c55e", "#052e16")}>{stats.approved} ✓</span>
          <span style={s.badge("#f59e0b", "#451a03")}>{stats.needsFix} ⚠</span>
          <span style={s.badge("#64748b", "#1e293b")}>{stats.pending} ?</span>
        </div>
      </div>

      {view === "list" ? <ListView /> : <DetailView />}
    </div>
  );
}
