<div class="hub-page hub-page--section hub-page--cheatsheet" lang="en">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">📋</div>
      <div>
        <p class="hub-nav__title">Cheatsheet</p>
        <p class="hub-nav__subtitle">Operations reference</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#guides" class="hub-nav__link">Guides</a>
      <a href="#cli" class="hub-nav__link">CLI</a>
      <a href="#config" class="hub-nav__link">Config</a>
      <a href="guides/quickstart/" class="hub-nav__link">Quick start</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="Language">
        <span class="hub-lang__item hub-lang__item--active" lang="en">EN</span>
        <a href="../fa/cheatsheet/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <a href="../zh/cheatsheet/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="guides/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-compass"></i> Browse guides</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--compact" id="top">
  <div class="hub-hero__grid hub-hero__grid--single">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        Offline-friendly · synced from ceph/ceph
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">Operate</span> Ceph with confidence
      </h1>
      <p class="hub-hero__lead">
        CLI commands, config options, and role/scale guides for day-to-day cluster administration.
      </p>
      <div class="hub-hero__actions">
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-terminal"></i> CLI reference</a>
        <a href="config/OVERVIEW/" class="hub-btn hub-btn--outline"><i class="fas fa-sliders-h"></i> Config index</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">CLI commands</span></div>
        <div><span class="hub-hero__stat-val">2122</span><span class="hub-hero__stat-label">Config options</span></div>
        <div><span class="hub-hero__stat-val">13</span><span class="hub-hero__stat-label">Subsystems</span></div>
      </div>
    </div>
  </div>
  <a href="#guides" class="hub-scroll-hint" aria-label="Scroll to guides section">
    <span aria-hidden="true">↓</span>
    <span>Explore</span>
  </a>
</section>

<section class="hub-section" id="guides">
  <div class="hub-section__head">
    <div class="hub-section__icon">📈</div>
    <h2 class="hub-section__title">Guides by role &amp; scale</h2>
    <p class="hub-section__subtitle">Pick documentation for your job and cluster size</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">👤</div>
      <h3 class="hub-card__title">By role</h3>
      <p class="hub-card__text">Cluster admin, storage operator, RGW admin, CephFS admin.</p>
      <a href="guides/OVERVIEW/#by-role" class="hub-card__link">Role guides <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📐</div>
      <h3 class="hub-card__title">By scale</h3>
      <p class="hub-card__text">Lab, small production, large production, multisite.</p>
      <a href="guides/OVERVIEW/#by-scale" class="hub-card__link">Scale guides <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">⚡</div>
      <h3 class="hub-card__title">Daily ops</h3>
      <p class="hub-card__text">Quick start, troubleshooting, config lookup, getting started.</p>
      <a href="guides/quickstart/" class="hub-card__link">Quick start <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="cli">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🖥️</div>
        <h2 class="hub-section__title">CLI command reference</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          ceph, osd, mon, rgw, rbd, cephfs, cephadm — copy-ready commands with examples.
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>Cluster &amp; health</strong><p>Status, auth, CRUSH, orchestrator</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>RGW / S3</strong><p>Users, buckets, multisite, quotas</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Storage</strong><p>OSD, pools, RBD, RADOS, CephFS</p></div></li>
        </ul>
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-terminal"></i> Open CLI index</a>
      </div>
      <div class="hub-code-block">
        <pre>$ ceph status
$ ceph orch ps
$ radosgw-admin user list
$ rbd ls</pre>
      </div>
    </div>
  </div>
</section>

<section class="hub-section" id="config">
  <div class="hub-section__head">
    <div class="hub-section__icon">⚙️</div>
    <h2 class="hub-section__title">Configuration options</h2>
    <p class="hub-section__subtitle">Generated from upstream YAML — global, osd, mon, mgr, mds, rgw, rbd, and more</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">global</h3>
      <a href="config/global/INDEX/" class="hub-card__link">852 options <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">rgw</h3>
      <a href="config/rgw/INDEX/" class="hub-card__link">441 options <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">osd</h3>
      <a href="config/osd/INDEX/" class="hub-card__link">158 options <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">All subsystems</h3>
      <a href="config/OVERVIEW/" class="hub-card__link">Full index <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>📋</span> Cheatsheet</div>
      <p class="hub-footer__note">Independent operations reference · <a href="../">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p><a href="../version/">Version</a> · <a href="guides/contributing/">Contributing</a></p>
    </div>
  </div>
</footer>

</div>
