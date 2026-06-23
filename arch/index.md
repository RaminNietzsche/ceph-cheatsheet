<div class="hub-page hub-page--section hub-page--arch" lang="en">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🏗️</div>
      <div>
        <p class="hub-nav__title">Architecture</p>
        <p class="hub-nav__subtitle">How Ceph subsystems work</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#rgw" class="hub-nav__link">RGW</a>
      <a href="#design" class="hub-nav__link">System design</a>
      <a href="#modules" class="hub-nav__link">Modules</a>
      <a href="rgw/learning-program/" class="hub-nav__link">Learning</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="Language">
        <span class="hub-lang__item hub-lang__item--active" lang="en">EN</span>
        <a href="../fa/arch/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <a href="../zh/arch/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="rgw/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-layer-group"></i> RGW overview</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--compact" id="top">
  <div class="hub-hero__grid hub-hero__grid--single">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        Deep dives · request paths · code landmarks
      </div>
      <h1 class="hub-hero__title">
        Understand <span class="hub-gradient">Ceph internals</span>
      </h1>
      <p class="hub-hero__lead">
        Subsystem architecture, storage layers, and RGW pipeline documentation synced from upstream.
      </p>
      <div class="hub-hero__actions">
        <a href="rgw/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-sitemap"></i> RGW overview</a>
        <a href="rgw/architecture/request-pipeline/" class="hub-btn hub-btn--outline"><i class="fas fa-route"></i> Request pipeline</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">RGW topics</span></div>
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">Learning phases</span></div>
        <div><span class="hub-hero__stat-val">7</span><span class="hub-hero__stat-label">Core modules</span></div>
      </div>
    </div>
  </div>
  <a href="#rgw" class="hub-scroll-hint" aria-label="Scroll to RGW section">
    <span aria-hidden="true">↓</span>
    <span>Explore</span>
  </a>
</section>

<section class="hub-section" id="rgw">
  <div class="hub-section__head">
    <div class="hub-section__icon">🌐</div>
    <h2 class="hub-section__title">RADOS Gateway (RGW)</h2>
    <p class="hub-section__subtitle">HTTP frontends, SAL, RADOS driver, auth, multisite, and scheduling</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">📖</div>
      <h3 class="hub-card__title">Overview</h3>
      <p class="hub-card__text">Entry point for RGW architecture documentation.</p>
      <a href="rgw/OVERVIEW/" class="hub-card__link">Read overview <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">🎓</div>
      <h3 class="hub-card__title">Learning program</h3>
      <p class="hub-card__text">Phased path from request path to multisite and subsystems.</p>
      <a href="rgw/learning-program/" class="hub-card__link">Start learning <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📝</div>
      <h3 class="hub-card__title">Guides</h3>
      <p class="hub-card__text">Deployment, development convention, source code in docs.</p>
      <a href="rgw/guides/development-convention/" class="hub-card__link">Open guides <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="design">
  <div class="hub-section__head">
    <div class="hub-section__icon">🔬</div>
    <h2 class="hub-section__title">System design</h2>
    <p class="hub-section__subtitle">Runtime topology, workers, scheduling, lifecycle, observability</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Request pipeline</h3>
      <a href="rgw/architecture/request-pipeline/" class="hub-card__link">View <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Runtime topology</h3>
      <a href="rgw/architecture/runtime-topology/" class="hub-card__link">View <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Multisite</h3>
      <a href="rgw/modules/multisite/" class="hub-card__link">View <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">All design docs</h3>
      <a href="rgw/architecture/system-overview/" class="hub-card__link">System overview <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="modules">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🧩</div>
        <h2 class="hub-section__title">RGW modules</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          Core request path, SAL, auth, RADOS driver, services, protocol APIs.
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>SAL layer</strong><p>Store abstraction between REST and backends</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>RADOS driver</strong><p>Metadata and data placement</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Auth</strong><p>S3-compatible identity and policies</p></div></li>
        </ul>
        <a href="rgw/modules/core-request-path/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-puzzle-piece"></i> Core request path</a>
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
      <div class="hub-footer__brand"><span>🏗️</span> Architecture</div>
      <p class="hub-footer__note">Independent architecture docs · <a href="../">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p>More subsystems (OSD, MON) may be added later</p>
    </div>
  </div>
</footer>

</div>
