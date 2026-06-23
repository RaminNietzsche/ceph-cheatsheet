<div class="hub-page hub-page--section hub-page--cheatsheet" dir="rtl" lang="fa">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">📋</div>
      <div>
        <p class="hub-nav__title">Cheatsheet</p>
        <p class="hub-nav__subtitle">مرجع عملیاتی</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#guides" class="hub-nav__link">راهنما</a>
      <a href="#cli" class="hub-nav__link">CLI</a>
      <a href="#config" class="hub-nav__link">Config</a>
      <a href="guides/quickstart/" class="hub-nav__link">شروع سریع</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="زبان">
        <a href="../../cheatsheet/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <span class="hub-lang__item hub-lang__item--active" lang="fa">فا</span>
        <a href="../../zh/cheatsheet/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="guides/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-compass"></i> راهنماها</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--section" id="top">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        آفلاین · همگام با ceph/ceph
      </div>
      <h1 class="hub-hero__title">
        Ceph را با <span class="hub-gradient">اطمینان</span> اجرا کنید
      </h1>
      <p class="hub-hero__lead">
        دستورات CLI، گزینه‌های پیکربندی و راهنماهای نقش/مقیاس برای مدیریت روزانه کلاستر.
      </p>
      <div class="hub-hero__actions">
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-terminal"></i> مرجع CLI</a>
        <a href="config/OVERVIEW/" class="hub-btn hub-btn--outline"><i class="fas fa-sliders-h"></i> فهرست Config</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">دستور CLI</span></div>
        <div><span class="hub-hero__stat-val">2122</span><span class="hub-hero__stat-label">گزینه Config</span></div>
        <div><span class="hub-hero__stat-val">13</span><span class="hub-hero__stat-label">زیرسیستم</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-copy"></i> آماده کپی</div>
        <div class="hub-terminal">
          <div class="hub-terminal__prompt">$ ceph -s</div>
          <div class="hub-terminal__line">health: HEALTH_OK</div>
          <div class="hub-terminal__prompt">$ radosgw-admin user list</div>
          <div class="hub-terminal__line">["admin", "s3user"]</div>
          <div class="hub-terminal__prompt">$ ./scripts/lookup-config.sh rgw_cache_enabled</div>
          <div class="hub-terminal__line hub-terminal__ok">rgw_cache_enabled = true</div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-bolt"></i> عملیات روزانه</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="رفتن به لینک‌های سریع">
    <span aria-hidden="true">↓</span>
    <span>ادامه</span>
  </a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="cli/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-terminal"></i> CLI</a>
  <a href="config/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-sliders-h"></i> Config</a>
  <a href="guides/quickstart/" class="hub-quick-links__item"><i class="fas fa-bolt"></i> شروع سریع</a>
  <a href="guides/getting-started/" class="hub-quick-links__item"><i class="fas fa-seedling"></i> شروع کار</a>
  <a href="guides/troubleshooting-guide/" class="hub-quick-links__item"><i class="fas fa-wrench"></i> عیب‌یابی</a>
</div>

<section class="hub-section" id="guides">
  <div class="hub-section__head">
    <div class="hub-section__icon">📈</div>
    <h2 class="hub-section__title">راهنما بر اساس نقش و مقیاس</h2>
    <p class="hub-section__subtitle">مستندات متناسب با شغل و اندازه کلاستر</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">👤</div>
      <h3 class="hub-card__title">بر اساس نقش</h3>
      <p class="hub-card__text">مدیر کلاستر، ذخیره‌سازی، RGW، CephFS.</p>
      <a href="guides/OVERVIEW/#by-role" class="hub-card__link">راهنمای نقش <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📐</div>
      <h3 class="hub-card__title">بر اساس مقیاس</h3>
      <p class="hub-card__text">آزمایشگاه، production کوچک/بزرگ، multisite.</p>
      <a href="guides/OVERVIEW/#by-scale" class="hub-card__link">راهنمای مقیاس <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">⚡</div>
      <h3 class="hub-card__title">عملیات روزانه</h3>
      <p class="hub-card__text">شروع سریع، عیب‌یابی، جستجوی config.</p>
      <a href="guides/quickstart/" class="hub-card__link">شروع سریع <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="cli">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🖥️</div>
        <h2 class="hub-section__title">مرجع دستورات CLI</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          ceph، osd، mon، rgw، rbd، cephfs، cephadm — دستورات آماده کپی.
        </p>
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-terminal"></i> فهرست CLI</a>
      </div>
      <div class="hub-code-block">
        <pre>$ ceph status
$ radosgw-admin user list
$ rbd ls</pre>
      </div>
    </div>
  </div>
</section>

<section class="hub-section" id="config">
  <div class="hub-section__head">
    <div class="hub-section__icon">⚙️</div>
    <h2 class="hub-section__title">گزینه‌های پیکربندی</h2>
    <p class="hub-section__subtitle">تولیدشده از YAML upstream</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">global</h3>
      <a href="config/global/INDEX/" class="hub-card__link">852 گزینه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">rgw</h3>
      <a href="config/rgw/INDEX/" class="hub-card__link">441 گزینه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">osd</h3>
      <a href="config/osd/INDEX/" class="hub-card__link">158 گزینه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">همه</h3>
      <a href="config/OVERVIEW/" class="hub-card__link">فهرست کامل <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>📋</span> Cheatsheet</div>
      <p class="hub-footer__note">بخش مستقل · <a href="../">Ceph Docs Hub</a></p>
    </div>
  </div>
</footer>

</div>
