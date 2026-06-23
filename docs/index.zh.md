<div class="hub-page" lang="zh">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <div class="hub-nav__brand">
      <div class="hub-nav__logo">🐙</div>
      <div>
        <p class="hub-nav__title">Ceph Docs Hub</p>
        <p class="hub-nav__subtitle">Ceph S3 技术文档</p>
      </div>
    </div>
    <div class="hub-nav__links">
      <a href="#portals" class="hub-nav__link">板块</a>
      <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener" class="hub-nav__link">
        <i class="fab fa-github"></i> GitHub
      </a>
    </div>
    <div class="hub-nav__actions">
      <div class="hub-lang" role="navigation" aria-label="语言">
        <a href="../" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <a href="../fa/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <span class="hub-lang__item hub-lang__item--active" lang="zh">中文</span>
      </div>
      <a href="#get-started" class="hub-nav__cta"><i class="fas fa-rocket"></i> 开始使用</a>
    </div>
  </div>
</nav>

<section class="hub-hero" id="get-started">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        最新 Ceph RGW 文档
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">构建</span>、<span class="hub-gradient">运维</span>、<span class="hub-gradient">理解</span> Ceph
      </h1>
      <p class="hub-hero__lead">
        完整速查表、RGW 深度架构与 Ceph Object Gateway (S3) 开发者指南
      </p>
      <div class="hub-hero__actions">
        <a href="cheatsheet/" class="hub-btn hub-btn--primary"><i class="fas fa-book"></i> 打开速查表</a>
        <a href="arch/" class="hub-btn hub-btn--outline"><i class="fas fa-layer-group"></i> RGW 架构</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">CLI 命令</span></div>
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">RGW 子系统</span></div>
        <div><span class="hub-hero__stat-val">∞</span><span class="hub-hero__stat-label">可扩展性</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-bolt"></i> 高性能</div>
        <div class="hub-terminal">
          <div class="hub-terminal__prompt">$ ceph status</div>
          <div class="hub-terminal__line">cluster: ceph</div>
          <div class="hub-terminal__line">health: HEALTH_OK</div>
          <div class="hub-terminal__line">rgw: 3 daemons active</div>
          <div class="hub-terminal__line hub-terminal__warn">multisite: sync enabled</div>
        </div>
        <div class="hub-terminal__metrics">
          <div><div class="hub-terminal__metric-val">99.99</div><div class="hub-terminal__metric-label">可用性</div></div>
          <div><div class="hub-terminal__metric-val">PB</div><div class="hub-terminal__metric-label">存储</div></div>
          <div><div class="hub-terminal__metric-val">S3</div><div class="hub-terminal__metric-label">兼容</div></div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-shield-alt"></i> 企业级</div>
      </div>
    </div>
  </div>
  <a href="#portals" class="hub-scroll-hint" aria-label="滚动到板块">
    <span aria-hidden="true">↓</span>
    <span>选择板块</span>
  </a>
</section>

<section class="hub-section" id="portals">
  <div class="hub-section__head">
    <div class="hub-section__icon">🧭</div>
    <h2 class="hub-section__title">三个独立板块</h2>
    <p class="hub-section__subtitle">每个板块有独立首页与导航</p>
  </div>
  <div class="hub-cards hub-cards--portals">
    <a href="cheatsheet/" class="hub-card hub-card--portal hub-card--portal-cheatsheet">
      <div class="hub-card__icon">📋</div>
      <h3 class="hub-card__title">速查表</h3>
      <p class="hub-card__text">CLI、配置与角色/规模指南。</p>
      <span class="hub-card__link">进入速查表 <i class="fas fa-arrow-right"></i></span>
    </a>
    <a href="arch/" class="hub-card hub-card--portal hub-card--portal-arch">
      <div class="hub-card__icon">🏗️</div>
      <h3 class="hub-card__title">架构</h3>
      <p class="hub-card__text">RGW 内部 — 请求路径、SAL、RADOS、多站点。</p>
      <span class="hub-card__link">进入架构 <i class="fas fa-arrow-right"></i></span>
    </a>
    <a href="dev/" class="hub-card hub-card--portal hub-card--portal-dev">
      <div class="hub-card__icon">🛠️</div>
      <h3 class="hub-card__title">开发</h3>
      <p class="hub-card__text">学习程序、规范与 upstream 同步。</p>
      <span class="hub-card__link">进入开发 <i class="fas fa-arrow-right"></i></span>
    </a>
  </div>
</section>

<footer class="hub-footer">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🐙</span> Ceph Docs Hub</div>
      <p class="hub-footer__note">Ceph S3 技术文档</p>
    </div>
    <div class="hub-footer__meta">
      <p>来源：ceph/ceph · src/rgw · RaminNietzsche</p>
      <div class="hub-footer__social">
        <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <p class="hub-footer__copy">为 Ceph 社区用心构建</p>
</footer>

</div>
