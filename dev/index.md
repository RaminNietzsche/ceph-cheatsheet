<div class="hub-page hub-page--section hub-page--dev" lang="en">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🛠️</div>
      <div>
        <p class="hub-nav__title">Develop</p>
        <p class="hub-nav__subtitle">Build &amp; contribute to RGW</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#learn" class="hub-nav__link">Learning</a>
      <a href="#conventions" class="hub-nav__link">Conventions</a>
      <a href="#workflow" class="hub-nav__link">Workflow</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="Language">
        <span class="hub-lang__item hub-lang__item--active" lang="en">EN</span>
        <a href="../fa/dev/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <a href="../zh/dev/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="../arch/rgw/learning-program/" class="hub-nav__cta"><i class="fas fa-graduation-cap"></i> Start learning</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--compact" id="top">
  <div class="hub-hero__grid hub-hero__grid--single">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        docs-extended · src/rgw/
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">Develop</span> on Ceph RGW
      </h1>
      <p class="hub-hero__lead">
        Structured path to understand and change the Object Gateway — synced from upstream docs-extended.
      </p>
      <div class="hub-hero__actions">
        <a href="../arch/rgw/learning-program/" class="hub-btn hub-btn--primary"><i class="fas fa-graduation-cap"></i> Learning program</a>
        <a href="../arch/rgw/guides/development-convention/" class="hub-btn hub-btn--outline"><i class="fas fa-file-code"></i> Conventions</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">Phases</span></div>
        <div><span class="hub-hero__stat-val">3</span><span class="hub-hero__stat-label">Dev guides</span></div>
        <div><span class="hub-hero__stat-val">↑</span><span class="hub-hero__stat-label">Upstream sync</span></div>
      </div>
    </div>
  </div>
  <a href="#learn" class="hub-scroll-hint" aria-label="Scroll to learning section">
    <span aria-hidden="true">↓</span>
    <span>Explore</span>
  </a>
</section>

<section class="hub-section" id="learn">
  <div class="hub-section__head">
    <div class="hub-section__icon">🎓</div>
    <h2 class="hub-section__title">Learning program</h2>
    <p class="hub-section__subtitle">Follow phases in order — prerequisites through multisite and subsystems</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">0️⃣</div>
      <h3 class="hub-card__title">Prerequisites</h3>
      <p class="hub-card__text">Tools, codebase layout, and baseline knowledge.</p>
      <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-card__link">Start here <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">🛤️</div>
      <h3 class="hub-card__title">Phase 0 — Request path</h3>
      <p class="hub-card__text">Trace HTTP from frontend to RADOS.</p>
      <a href="../arch/rgw/learning-program/01-phase-0-request-path/" class="hub-card__link">Phase 0 <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">✅</div>
      <h3 class="hub-card__title">Full program</h3>
      <p class="hub-card__text">All phases, checklist, progress tracker.</p>
      <a href="../arch/rgw/learning-program/" class="hub-card__link">Program index <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="conventions">
  <div class="hub-section__head">
    <div class="hub-section__icon">📐</div>
    <h2 class="hub-section__title">Conventions &amp; guides</h2>
    <p class="hub-section__subtitle">Docs-as-code, deployment notes, citing source in documentation</p>
  </div>
  <div class="hub-cards hub-cards--three">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Development convention</h3>
      <a href="../arch/rgw/guides/development-convention/" class="hub-card__link">Read <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Deployment implementation</h3>
      <a href="../arch/rgw/guides/deployment-implementation-guide/" class="hub-card__link">Read <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Source code in docs</h3>
      <a href="../arch/rgw/guides/source-code-in-docs/" class="hub-card__link">Read <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="workflow">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🔄</div>
        <h2 class="hub-section__title">Sync from upstream</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          Persian originals live in <code>dev-code/rgw/docs-extended/</code> (local clone of ceph/ceph).
        </p>
        <a href="../cheatsheet/guides/contributing/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-book-open"></i> Contributing guide</a>
      </div>
      <div class="hub-code-block">
        <pre>python3 scripts/sync-rgw-from-docs-extended.py
python3 scripts/generate-role-scale-guides.py</pre>
      </div>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🛠️</span> Develop</div>
      <p class="hub-footer__note">Independent developer portal · <a href="../">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p>Content hosted under <a href="../arch/">Architecture</a> paths</p>
    </div>
  </div>
</footer>

</div>
