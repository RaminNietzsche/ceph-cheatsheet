<div class="hub-page hub-page--section hub-page--dev" lang="zh">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🛠️</div>
      <div>
        <p class="hub-nav__title">开发</p>
        <p class="hub-nav__subtitle">构建与贡献 RGW</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#learn" class="hub-nav__link">学习</a>
      <a href="#conventions" class="hub-nav__link">规范</a>
      <a href="#workflow" class="hub-nav__link">工作流</a>
    </div>
    <div class="hub-nav__actions">
      <a href="/zh/" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="语言">
        <a href="/en/dev/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <a href="/fa/dev/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <span class="hub-lang__item hub-lang__item--active" lang="zh">中文</span>
      </div>
      <a href="/zh/arch/rgw/learning-program/" class="hub-nav__cta"><i class="fas fa-graduation-cap"></i> 开始学习</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--section" id="top">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        docs-extended · src/rgw/
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">开发</span> Ceph RGW
      </h1>
      <p class="hub-hero__lead">
        理解并修改 Object Gateway 的结构化路径 — 同步自 upstream docs-extended。
      </p>
      <div class="hub-hero__actions">
        <a href="../arch/rgw/learning-program/" class="hub-btn hub-btn--primary"><i class="fas fa-graduation-cap"></i> 学习程序</a>
        <a href="../arch/rgw/guides/development-convention/" class="hub-btn hub-btn--outline"><i class="fas fa-file-code"></i> 开发规范</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">阶段</span></div>
        <div><span class="hub-hero__stat-val">3</span><span class="hub-hero__stat-label">开发指南</span></div>
        <div><span class="hub-hero__stat-val">↑</span><span class="hub-hero__stat-label">Upstream 同步</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow hub-hero__glow--dev"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fab fa-git-alt"></i> Upstream 同步</div>
        <div class="hub-terminal hub-terminal--dev">
          <div class="hub-terminal__prompt">$ python3 scripts/sync-rgw-from-docs-extended.py</div>
          <div class="hub-terminal__line hub-terminal__ok">Synced 42 arch pages</div>
          <div class="hub-terminal__prompt">$ python3 scripts/regenerate-docs.py</div>
          <div class="hub-terminal__line">fa/zh variants updated</div>
          <div class="hub-terminal__prompt">$ git diff --stat arch/rgw/</div>
          <div class="hub-terminal__line hub-terminal__warn">learning-program/ + modules/</div>
        </div>
        <div class="hub-phase-track">
          <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-phase-track__item hub-phase-track__item--done" title="前提条件">0</a>
          <a href="../arch/rgw/learning-program/01-phase-0-request-path/" class="hub-phase-track__item hub-phase-track__item--active" title="请求路径">1</a>
          <a href="../arch/rgw/learning-program/" class="hub-phase-track__item" title="完整程序">…</a>
          <a href="../arch/rgw/learning-program/10-development-checklist/" class="hub-phase-track__item" title="检查清单">✓</a>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-code-branch"></i> 贡献</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="滚动到快捷链接">
    <span aria-hidden="true">↓</span>
    <span>探索</span>
  </a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-quick-links__item"><i class="fas fa-play"></i> 前提条件</a>
  <a href="../arch/rgw/learning-program/" class="hub-quick-links__item"><i class="fas fa-list-ol"></i> 全部阶段</a>
  <a href="../arch/rgw/guides/development-convention/" class="hub-quick-links__item"><i class="fas fa-file-code"></i> 开发规范</a>
  <a href="../cheatsheet/guides/contributing/" class="hub-quick-links__item"><i class="fas fa-hand-holding-heart"></i> 贡献</a>
</div>

<section class="hub-section" id="learn">
  <div class="hub-section__head">
    <div class="hub-section__icon">🎓</div>
    <h2 class="hub-section__title">学习程序</h2>
    <p class="hub-section__subtitle">按顺序完成各阶段 — 从前提条件到多站点与子系统</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">0️⃣</div>
      <h3 class="hub-card__title">前提条件</h3>
      <p class="hub-card__text">工具、代码库布局与基础知识。</p>
      <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-card__link">从这里开始 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">🛤️</div>
      <h3 class="hub-card__title">阶段 0 — 请求路径</h3>
      <p class="hub-card__text">从前端到 RADOS 追踪 HTTP。</p>
      <a href="../arch/rgw/learning-program/01-phase-0-request-path/" class="hub-card__link">阶段 0 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">✅</div>
      <h3 class="hub-card__title">完整程序</h3>
      <p class="hub-card__text">全部阶段、检查清单与进度跟踪。</p>
      <a href="../arch/rgw/learning-program/" class="hub-card__link">程序索引 <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="conventions">
  <div class="hub-section__head">
    <div class="hub-section__icon">📐</div>
    <h2 class="hub-section__title">规范与指南</h2>
    <p class="hub-section__subtitle">文档即代码、部署说明、文档中的源码引用</p>
  </div>
  <div class="hub-cards hub-cards--three">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">开发约定</h3>
      <a href="../arch/rgw/guides/development-convention/" class="hub-card__link">阅读 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">部署实施</h3>
      <a href="../arch/rgw/guides/deployment-implementation-guide/" class="hub-card__link">阅读 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">文档中的源码</h3>
      <a href="../arch/rgw/guides/source-code-in-docs/" class="hub-card__link">阅读 <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="workflow">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🔄</div>
        <h2 class="hub-section__title">从 upstream 同步</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          波斯语原文位于 <code>dev-code/rgw/docs-extended/</code>（ceph/ceph 本地克隆）。
        </p>
        <a href="../cheatsheet/guides/contributing/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-book-open"></i> 贡献指南</a>
      </div>
      <div class="hub-code-block">
        <pre>python3 scripts/sync-rgw-from-docs-extended.py
python3 scripts/generate-role-scale-guides.py
python3 scripts/sync-i18n-pages.py</pre>
      </div>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🛠️</span> 开发</div>
      <p class="hub-footer__note">独立开发者门户 · <a href="/zh/">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p>内容托管于 <a href="../arch/">架构</a> 路径下</p>
    </div>
  </div>
</footer>

</div>
