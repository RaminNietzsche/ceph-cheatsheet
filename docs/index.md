<div class="hub-page" lang="en">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <div class="hub-nav__brand">
      <div class="hub-nav__logo">🐙</div>
      <div>
        <p class="hub-nav__title">Ceph Docs Hub</p>
        <p class="hub-nav__subtitle">Ceph &amp; S3 documentation</p>
      </div>
    </div>
    <div class="hub-nav__links">
      <a href="#cheatsheet" class="hub-nav__link">Cheatsheet</a>
      <a href="#architecture" class="hub-nav__link">Architecture</a>
      <a href="#develop" class="hub-nav__link">Develop</a>
      <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener" class="hub-nav__link">
        <i class="fab fa-github"></i> GitHub
      </a>
    </div>
    <div class="hub-nav__actions">
      <div class="hub-lang" role="navigation" aria-label="Language">
        <span class="hub-lang__item hub-lang__item--active" lang="en">EN</span>
        <a href="fa/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <a href="zh/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="#get-started" class="hub-nav__cta"><i class="fas fa-rocket"></i> Get started</a>
    </div>
  </div>
</nav>

<section class="hub-hero" id="get-started">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        Up-to-date Ceph RGW docs
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">Build</span>, <span class="hub-gradient">operate</span>, <span class="hub-gradient">understand</span> Ceph
      </h1>
      <p class="hub-hero__lead">
        Complete cheatsheet, deep RGW architecture, and developer guides for Ceph Object Gateway (S3).
      </p>
      <div class="hub-hero__actions">
        <a href="cheatsheet/" class="hub-btn hub-btn--primary"><i class="fas fa-book"></i> Open cheatsheet</a>
        <a href="arch/" class="hub-btn hub-btn--outline"><i class="fas fa-layer-group"></i> RGW architecture</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">CLI commands</span></div>
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">RGW subsystems</span></div>
        <div><span class="hub-hero__stat-val">∞</span><span class="hub-hero__stat-label">Scalability</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-bolt"></i> High performance</div>
        <div class="hub-terminal">
          <div class="hub-terminal__prompt">$ ceph status</div>
          <div class="hub-terminal__line">cluster: ceph</div>
          <div class="hub-terminal__line">health: HEALTH_OK</div>
          <div class="hub-terminal__line">rgw: 3 daemons active</div>
          <div class="hub-terminal__line hub-terminal__warn">multisite: sync enabled</div>
        </div>
        <div class="hub-terminal__metrics">
          <div><div class="hub-terminal__metric-val">99.99</div><div class="hub-terminal__metric-label">Uptime</div></div>
          <div><div class="hub-terminal__metric-val">PB</div><div class="hub-terminal__metric-label">Storage</div></div>
          <div><div class="hub-terminal__metric-val">S3</div><div class="hub-terminal__metric-label">Compatible</div></div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-shield-alt"></i> Enterprise ready</div>
      </div>
    </div>
  </div>
  <div class="hub-scroll-hint"><span>↓</span><span>Explore more</span></div>
</section>

<section class="hub-section" id="cheatsheet">
  <div class="hub-section__head">
    <div class="hub-section__icon">📋</div>
    <h2 class="hub-section__title">Cheatsheet</h2>
    <p class="hub-section__subtitle">Fast reference for CLI commands, config options, and day-to-day Ceph operations</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">🐙</div>
      <h3 class="hub-card__title">CLI commands</h3>
      <p class="hub-card__text">ceph, osd, mon, rgw, rbd — hundreds of commands with real-world examples.</p>
      <a href="cheatsheet/cli/" class="hub-card__link">Browse CLI reference <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">⚙️</div>
      <h3 class="hub-card__title">Configuration</h3>
      <p class="hub-card__text">Production tuning, scalability, multisite, and performance options from upstream YAML.</p>
      <a href="cheatsheet/config/" class="hub-card__link">Browse config index <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📈</div>
      <h3 class="hub-card__title">Role &amp; scale guides</h3>
      <p class="hub-card__text">Install, monitoring, backup, disaster recovery, and real deployment scenarios.</p>
      <a href="cheatsheet/guides/" class="hub-card__link">Open guides <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="architecture">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🏗️</div>
        <h2 class="hub-section__title">Deep RGW architecture</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          Request path, SAL, RADOS driver, auth, multisite, and scheduling in Ceph Object Gateway.
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>Request flow</strong><p>From HTTP frontend to RADOS storage</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Multisite sync</strong><p>Cross-datacenter replication mechanics</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Auth &amp; authorization</strong><p>S3-compatible identity and IAM</p></div></li>
        </ul>
        <a href="arch/rgw/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-layer-group"></i> Explore RGW internals</a>
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
    <h2 class="hub-section__title">Developer guide</h2>
    <p class="hub-section__subtitle">Workflow, conventions, build, and contribution to Ceph RGW</p>
  </div>
  <div class="hub-develop-box">
    <div class="hub-develop-box__icon">🚀</div>
    <h3>Learning program &amp; docs-as-code</h3>
    <p>Structured path through <code>src/rgw/</code> — synced from upstream docs-extended.</p>
    <a href="dev/" class="hub-btn"><i class="fas fa-code"></i> Open develop section</a>
  </div>
</section>

<footer class="hub-footer">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🐙</span> Ceph Docs Hub</div>
      <p class="hub-footer__note">Ceph S3 technical documentation</p>
    </div>
    <div class="hub-footer__meta">
      <p>Source: ceph/ceph · src/rgw · RaminNietzsche</p>
      <div class="hub-footer__social">
        <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <p class="hub-footer__copy">Built with care for the Ceph community</p>
</footer>

</div>
