<div class="hub-page" dir="rtl" lang="fa">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <div class="hub-nav__brand">
      <div class="hub-nav__logo">🐙</div>
      <div>
        <p class="hub-nav__title">Ceph Docs Hub</p>
        <p class="hub-nav__subtitle">مستندات Ceph و S3</p>
      </div>
    </div>
    <div class="hub-nav__links">
      <a href="#portals" class="hub-nav__link">بخش‌ها</a>
      <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener" class="hub-nav__link">
        <i class="fab fa-github"></i> گیت‌هاب
      </a>
    </div>
    <div class="hub-nav__actions">
      <div class="hub-lang" role="navigation" aria-label="زبان">
        <a href="/en/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <span class="hub-lang__item hub-lang__item--active" lang="fa">فا</span>
        <a href="/zh/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="#get-started" class="hub-nav__cta"><i class="fas fa-rocket"></i> شروع کنید</a>
    </div>
  </div>
</nav>

<section class="hub-hero" id="get-started">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        مستندات به‌روز Ceph RGW
      </div>
      <h1 class="hub-hero__title">
        Ceph را <span class="hub-gradient">بسازید</span>، <span class="hub-gradient">اجرا کنید</span>، <span class="hub-gradient">درک کنید</span>
      </h1>
      <p class="hub-hero__lead">
        مرجع کامل Cheatsheet، معماری عمیق RGW و راهنمای توسعه‌دهندگان Ceph Object Gateway (S3).
      </p>
      <div class="hub-hero__actions">
        <a href="cheatsheet/" class="hub-btn hub-btn--primary"><i class="fas fa-book"></i> باز کردن Cheatsheet</a>
        <a href="arch/" class="hub-btn hub-btn--outline"><i class="fas fa-layer-group"></i> معماری RGW</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">دستور CLI</span></div>
        <div><span class="hub-hero__stat-val">15+</span><span class="hub-hero__stat-label">زیرسیستم RGW</span></div>
        <div><span class="hub-hero__stat-val">∞</span><span class="hub-hero__stat-label">مقیاس‌پذیری</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-bolt"></i> کارایی بالا</div>
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
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-shield-alt"></i> آماده enterprise</div>
      </div>
    </div>
  </div>
  <a href="#portals" class="hub-scroll-hint" aria-label="رفتن به بخش‌های مستندات">
    <span aria-hidden="true">↓</span>
    <span>یک بخش انتخاب کنید</span>
  </a>
</section>

<section class="hub-section" id="portals">
  <div class="hub-section__head">
    <div class="hub-section__icon">🧭</div>
    <h2 class="hub-section__title">سه بخش مستقل</h2>
    <p class="hub-section__subtitle">هر بخش صفحهٔ خانه، ناوبری و حوزهٔ تمرکز خود را دارد</p>
  </div>
  <div class="hub-cards hub-cards--portals">
    <a href="cheatsheet/" class="hub-card hub-card--portal hub-card--portal-cheatsheet">
      <div class="hub-card__icon">📋</div>
      <h3 class="hub-card__title">Cheatsheet</h3>
      <p class="hub-card__text">دستورات CLI، گزینه‌های config و راهنماهای نقش/مقیاس برای عملیات روزانه Ceph.</p>
      <span class="hub-card__link">ورود به Cheatsheet <i class="fas fa-arrow-left"></i></span>
    </a>
    <a href="arch/" class="hub-card hub-card--portal hub-card--portal-arch">
      <div class="hub-card__icon">🏗️</div>
      <h3 class="hub-card__title">معماری</h3>
      <p class="hub-card__text">درون‌ریزی RGW — مسیر درخواست، SAL، RADOS driver، multisite و طراحی سیستم.</p>
      <span class="hub-card__link">ورود به معماری <i class="fas fa-arrow-left"></i></span>
    </a>
    <a href="dev/" class="hub-card hub-card--portal hub-card--portal-dev">
      <div class="hub-card__icon">🛠️</div>
      <h3 class="hub-card__title">توسعه</h3>
      <p class="hub-card__text">برنامه یادگیری، قراردادهای docs-as-code و workflow همگام‌سازی upstream.</p>
      <span class="hub-card__link">ورود به توسعه <i class="fas fa-arrow-left"></i></span>
    </a>
  </div>
</section>

<footer class="hub-footer">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🐙</span> Ceph Docs Hub</div>
      <p class="hub-footer__note">مستندات فنی Ceph S3</p>
    </div>
    <div class="hub-footer__meta">
      <p>منبع: ceph/ceph · src/rgw · RaminNietzsche</p>
      <div class="hub-footer__social">
        <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <p class="hub-footer__copy">با توجه به جامعه Ceph ساخته شده</p>
</footer>

</div>
