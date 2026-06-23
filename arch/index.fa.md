<div class="hub-page hub-page--section hub-page--arch" dir="rtl" lang="fa">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🏗️</div>
      <div>
        <p class="hub-nav__title">معماری</p>
        <p class="hub-nav__subtitle">عملکرد زیرسیستم‌های Ceph</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#rgw" class="hub-nav__link">RGW</a>
      <a href="#design" class="hub-nav__link">طراحی</a>
      <a href="#modules" class="hub-nav__link">ماژول‌ها</a>
      <a href="rgw/learning-program/" class="hub-nav__link">یادگیری</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="زبان">
        <a href="../../arch/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <span class="hub-lang__item hub-lang__item--active" lang="fa">فا</span>
        <a href="../../zh/arch/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="rgw/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-layer-group"></i> نمای RGW</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--section" id="top">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        مسیر درخواست · لایه‌ها · نقاط کد
      </div>
      <h1 class="hub-hero__title">
        <span class="hub-gradient">درون‌بنیان</span> Ceph را درک کنید
      </h1>
      <p class="hub-hero__lead">
        معماری زیرسیستم‌ها، لایه‌های ذخیره‌سازی و مستندات pipeline RGW.
      </p>
      <div class="hub-hero__actions">
        <a href="rgw/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-sitemap"></i> نمای کلی RGW</a>
        <a href="rgw/architecture/request-pipeline/" class="hub-btn hub-btn--outline"><i class="fas fa-route"></i> مسیر درخواست</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">موضوع RGW</span></div>
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">فاز یادگیری</span></div>
        <div><span class="hub-hero__stat-val">7</span><span class="hub-hero__stat-label">ماژول اصلی</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow hub-hero__glow--arch"></div>
      <div class="hub-pipeline">
        <div class="hub-pipeline__title"><i class="fas fa-route"></i> مسیر درخواست RGW</div>
        <div class="hub-pipeline__step hub-pipeline__step--active">
          <span class="hub-pipeline__num">1</span>
          <div><strong>HTTP Frontend</strong><span>Beast / Civetweb</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">2</span>
          <div><strong>REST → RGWOp</strong><span>Operation dispatch</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">3</span>
          <div><strong>SAL</strong><span>Store abstraction</span></div>
        </div>
        <div class="hub-pipeline__arrow"><i class="fas fa-chevron-down"></i></div>
        <div class="hub-pipeline__step">
          <span class="hub-pipeline__num">4</span>
          <div><strong>RADOS</strong><span>Metadata + data</span></div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-microchip"></i> معماری SAL</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="رفتن به لینک‌های سریع">
    <span aria-hidden="true">↓</span>
    <span>ادامه</span>
  </a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="rgw/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-book"></i> نمای RGW</a>
  <a href="rgw/learning-program/" class="hub-quick-links__item"><i class="fas fa-graduation-cap"></i> برنامه یادگیری</a>
  <a href="rgw/architecture/request-pipeline/" class="hub-quick-links__item"><i class="fas fa-route"></i> مسیر درخواست</a>
  <a href="rgw/modules/core-request-path/" class="hub-quick-links__item"><i class="fas fa-puzzle-piece"></i> Core path</a>
  <a href="rgw/modules/multisite/" class="hub-quick-links__item"><i class="fas fa-globe"></i> Multisite</a>
</div>

<section class="hub-section" id="rgw">
  <div class="hub-section__head">
    <div class="hub-section__icon">🌐</div>
    <h2 class="hub-section__title">RADOS Gateway</h2>
    <p class="hub-section__subtitle">Frontend، SAL، RADOS، auth، multisite</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <h3 class="hub-card__title">نمای کلی</h3>
      <a href="rgw/OVERVIEW/" class="hub-card__link">مطالعه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <h3 class="hub-card__title">برنامه یادگیری</h3>
      <a href="rgw/learning-program/" class="hub-card__link">شروع <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <h3 class="hub-card__title">راهنماها</h3>
      <a href="rgw/guides/development-convention/" class="hub-card__link">قرارداد توسعه <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="design">
  <div class="hub-section__head">
    <div class="hub-section__icon">🔬</div>
    <h2 class="hub-section__title">طراحی سیستم</h2>
    <p class="hub-section__subtitle">Topology، worker، scheduling، observability</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Request pipeline</h3>
      <a href="rgw/architecture/request-pipeline/" class="hub-card__link">مشاهده <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Runtime topology</h3>
      <a href="rgw/architecture/runtime-topology/" class="hub-card__link">مشاهده <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">Multisite</h3>
      <a href="rgw/modules/multisite/" class="hub-card__link">مشاهده <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">System overview</h3>
      <a href="rgw/architecture/system-overview/" class="hub-card__link">مشاهده <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="modules">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🧩</div>
        <h2 class="hub-section__title">ماژول‌های RGW</h2>
        <a href="rgw/modules/core-request-path/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-puzzle-piece"></i> Core request path</a>
      </div>
      <div class="hub-code-block">
        <pre>RGW Request Path:
  1. Frontend
  2. REST → Ops
  3. SAL
  4. RADOS Backend</pre>
      </div>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🏗️</span> معماری</div>
      <p class="hub-footer__note">بخش مستقل · <a href="../">Ceph Docs Hub</a></p>
    </div>
  </div>
</footer>

</div>
