<div class="hub-page hub-page--section hub-page--arch" lang="zh">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🏗️</div>
      <div>
        <p class="hub-nav__title">架构</p>
        <p class="hub-nav__subtitle">Ceph 子系统原理</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#rgw" class="hub-nav__link">RGW</a>
      <a href="#design" class="hub-nav__link">系统设计</a>
      <a href="#modules" class="hub-nav__link">模块</a>
      <a href="rgw/learning-program/" class="hub-nav__link">学习</a>
    </div>
    <div class="hub-nav__actions">
      <a href="/zh/" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="语言">
        <a href="/en/arch/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <a href="/fa/arch/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <span class="hub-lang__item hub-lang__item--active" lang="zh">中文</span>
      </div>
      <a href="rgw/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-layer-group"></i> RGW 概览</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--section" id="top">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        深度指南 · 请求路径 · 代码要点
      </div>
      <h1 class="hub-hero__title">
        理解 Ceph <span class="hub-gradient">内部原理</span>
      </h1>
      <p class="hub-hero__lead">
        子系统架构、存储层与 RGW 流水线文档，同步自 upstream。
      </p>
      <div class="hub-hero__actions">
        <a href="rgw/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-sitemap"></i> RGW 概览</a>
        <a href="rgw/architecture/request-pipeline/" class="hub-btn hub-btn--outline"><i class="fas fa-route"></i> 请求流水线</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">RGW 主题</span></div>
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">学习阶段</span></div>
        <div><span class="hub-hero__stat-val">7</span><span class="hub-hero__stat-label">核心模块</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow hub-hero__glow--arch"></div>
      <div class="hub-pipeline">
        <div class="hub-pipeline__title"><i class="fas fa-route"></i> RGW 请求路径</div>
        <div class="hub-pipeline__step hub-pipeline__step--active">
          <span class="hub-pipeline__num">1</span>
          <div><strong>HTTP Frontend</strong><span>Beast / Civetweb</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">2</span>
          <div><strong>REST → RGWOp</strong><span>操作分发</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">3</span>
          <div><strong>SAL</strong><span>存储抽象层</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">4</span>
          <div><strong>RADOS</strong><span>元数据 + 数据</span></div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-microchip"></i> SAL 架构</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="滚动到快捷链接">
    <span aria-hidden="true">↓</span>
    <span>探索</span>
  </a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="rgw/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-book"></i> RGW 概览</a>
  <a href="rgw/learning-program/" class="hub-quick-links__item"><i class="fas fa-graduation-cap"></i> 学习程序</a>
  <a href="rgw/architecture/request-pipeline/" class="hub-quick-links__item"><i class="fas fa-route"></i> 请求流水线</a>
  <a href="rgw/modules/core-request-path/" class="hub-quick-links__item"><i class="fas fa-puzzle-piece"></i> 核心路径</a>
  <a href="rgw/modules/multisite/" class="hub-quick-links__item"><i class="fas fa-globe"></i> 多站点</a>
</div>

<section class="hub-section" id="rgw">
  <div class="hub-section__head">
    <div class="hub-section__icon">🌐</div>
    <h2 class="hub-section__title">RADOS Gateway (RGW)</h2>
    <p class="hub-section__subtitle">HTTP 前端、SAL、RADOS 驱动、认证、多站点与调度</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">📖</div>
      <h3 class="hub-card__title">概览</h3>
      <p class="hub-card__text">RGW 架构文档入口。</p>
      <a href="rgw/OVERVIEW/" class="hub-card__link">阅读概览 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">🎓</div>
      <h3 class="hub-card__title">学习程序</h3>
      <p class="hub-card__text">从请求路径到多站点与子系统的分阶段路径。</p>
      <a href="rgw/learning-program/" class="hub-card__link">开始学习 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📝</div>
      <h3 class="hub-card__title">指南</h3>
      <p class="hub-card__text">部署、开发约定、文档中的源码引用。</p>
      <a href="rgw/guides/development-convention/" class="hub-card__link">打开指南 <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="design">
  <div class="hub-section__head">
    <div class="hub-section__icon">🔬</div>
    <h2 class="hub-section__title">系统设计</h2>
    <p class="hub-section__subtitle">运行时拓扑、工作线程、调度、生命周期、可观测性</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">请求流水线</h3>
      <a href="rgw/architecture/request-pipeline/" class="hub-card__link">查看 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">运行时拓扑</h3>
      <a href="rgw/architecture/runtime-topology/" class="hub-card__link">查看 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">多站点</h3>
      <a href="rgw/modules/multisite/" class="hub-card__link">查看 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">全部设计文档</h3>
      <a href="rgw/architecture/system-overview/" class="hub-card__link">系统概览 <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="modules">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🧩</div>
        <h2 class="hub-section__title">RGW 模块</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          核心请求路径、SAL、认证、RADOS 驱动、服务、协议 API。
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>SAL 层</strong><p>REST 与后端之间的存储抽象</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>RADOS 驱动</strong><p>元数据与数据放置</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>认证</strong><p>S3 兼容的身份与策略</p></div></li>
        </ul>
        <a href="rgw/modules/core-request-path/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-puzzle-piece"></i> 核心请求路径</a>
      </div>
      <div class="hub-code-block">
        <pre>RGW Request Path:
  1. Frontend (Beast/Civetweb)
  2. RGW REST → Ops
  3. SAL (Store Abstraction Layer)
  4. RADOS Backend
  5. Metadata + Data Placement</pre>
      </div>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🏗️</span> 架构</div>
      <p class="hub-footer__note">独立架构文档 · <a href="/zh/">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p>更多子系统（OSD、MON）将陆续添加</p>
    </div>
  </div>
</footer>

</div>
