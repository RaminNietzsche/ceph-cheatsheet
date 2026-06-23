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
      <a href="#cheatsheet" class="hub-nav__link">速查表</a>
      <a href="#architecture" class="hub-nav__link">架构</a>
      <a href="#develop" class="hub-nav__link">开发</a>
      <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener" class="hub-nav__link">
        <i class="fab fa-github"></i> GitHub
      </a>
    </div>
    <div class="hub-nav__actions">
      <div class="hub-lang" role="navigation" aria-label="语言">
        <a href="/en/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <a href="/fa/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
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
  <a href="#cheatsheet" class="hub-scroll-hint" aria-label="滚动到速查表部分">
    <span aria-hidden="true">↓</span>
    <span>了解更多</span>
  </a>
</section>

<section class="hub-section" id="cheatsheet">
  <div class="hub-section__head">
    <div class="hub-section__icon">📋</div>
    <h2 class="hub-section__title">速查表</h2>
    <p class="hub-section__subtitle">CLI 命令、配置选项与日常 Ceph 运维快速参考</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">🐙</div>
      <h3 class="hub-card__title">CLI 命令</h3>
      <p class="hub-card__text">ceph、osd、mon、rgw、rbd — 数百条命令与实例</p>
      <a href="cheatsheet/cli/" class="hub-card__link">浏览 CLI 参考 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">⚙️</div>
      <h3 class="hub-card__title">配置</h3>
      <p class="hub-card__text">生产调优、扩展性、多站点与性能选项</p>
      <a href="cheatsheet/config/" class="hub-card__link">浏览配置索引 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📈</div>
      <h3 class="hub-card__title">角色与规模指南</h3>
      <p class="hub-card__text">安装、监控、备份、灾备与真实部署场景</p>
      <a href="cheatsheet/guides/" class="hub-card__link">打开指南 <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="architecture">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🏗️</div>
        <h2 class="hub-section__title">RGW 深度架构</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          请求路径、SAL、RADOS 驱动、认证、多站点与调度
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>请求流</strong><p>从 HTTP 前端到 RADOS 存储</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>多站点同步</strong><p>跨数据中心复制机制</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>认证与授权</strong><p>S3 兼容身份与 IAM</p></div></li>
        </ul>
        <a href="arch/rgw/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-layer-group"></i> 探索 RGW 内部</a>
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

<section class="hub-section" id="develop">
  <div class="hub-section__head">
    <div class="hub-section__icon">🛠️</div>
    <h2 class="hub-section__title">开发者指南</h2>
    <p class="hub-section__subtitle">工作流、规范、构建与 Ceph 贡献</p>
  </div>
  <div class="hub-develop-box">
    <div class="hub-develop-box__icon">🚀</div>
    <h3>学习程序与 Docs-as-Code</h3>
    <p>结构化学习 <code>src/rgw/</code> — 同步自 upstream docs-extended</p>
    <a href="dev/" class="hub-btn"><i class="fas fa-code"></i> 打开开发板块</a>
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
