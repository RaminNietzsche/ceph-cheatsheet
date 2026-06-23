<div class="hub-page hub-page--section hub-page--dev" dir="rtl" lang="fa">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">🛠️</div>
      <div>
        <p class="hub-nav__title">توسعه</p>
        <p class="hub-nav__subtitle">ساخت و مشارکت در RGW</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#learn" class="hub-nav__link">یادگیری</a>
      <a href="#conventions" class="hub-nav__link">قراردادها</a>
      <a href="#workflow" class="hub-nav__link">Workflow</a>
    </div>
    <div class="hub-nav__actions">
      <a href="/fa/" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="زبان">
        <a href="/en/dev/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <span class="hub-lang__item hub-lang__item--active" lang="fa">فا</span>
        <a href="/zh/dev/" class="hub-lang__item" lang="zh" hreflang="zh" title="中文">中文</a>
      </div>
      <a href="/fa/arch/rgw/learning-program/" class="hub-nav__cta"><i class="fas fa-graduation-cap"></i> شروع یادگیری</a>
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
        روی Ceph RGW <span class="hub-gradient">توسعه دهید</span>
      </h1>
      <p class="hub-hero__lead">
        مسیر ساخت‌یافته برای درک و تغییر Object Gateway — همگام با docs-extended upstream.
      </p>
      <div class="hub-hero__actions">
        <a href="../arch/rgw/learning-program/" class="hub-btn hub-btn--primary"><i class="fas fa-graduation-cap"></i> برنامه یادگیری</a>
        <a href="../arch/rgw/guides/development-convention/" class="hub-btn hub-btn--outline"><i class="fas fa-file-code"></i> قراردادها</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">11</span><span class="hub-hero__stat-label">فاز</span></div>
        <div><span class="hub-hero__stat-val">3</span><span class="hub-hero__stat-label">راهنما</span></div>
        <div><span class="hub-hero__stat-val">↑</span><span class="hub-hero__stat-label">همگام upstream</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow hub-hero__glow--dev"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fab fa-git-alt"></i> همگام upstream</div>
        <div class="hub-terminal hub-terminal--dev">
          <div class="hub-terminal__prompt">$ python3 scripts/sync-rgw-from-docs-extended.py</div>
          <div class="hub-terminal__line hub-terminal__ok">Synced 42 arch pages</div>
          <div class="hub-terminal__prompt">$ python3 scripts/regenerate-docs.py</div>
          <div class="hub-terminal__line">fa/zh variants updated</div>
          <div class="hub-terminal__prompt">$ git diff --stat arch/rgw/</div>
          <div class="hub-terminal__line hub-terminal__warn">learning-program/ + modules/</div>
        </div>
        <div class="hub-phase-track">
          <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-phase-track__item hub-phase-track__item--done" title="پیش‌نیاز">0</a>
          <a href="../arch/rgw/learning-program/01-phase-0-request-path/" class="hub-phase-track__item hub-phase-track__item--active" title="مسیر درخواست">1</a>
          <a href="../arch/rgw/learning-program/" class="hub-phase-track__item" title="برنامه">…</a>
          <a href="../arch/rgw/learning-program/10-development-checklist/" class="hub-phase-track__item" title="چک‌لیست">✓</a>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-code-branch"></i> مشارکت</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="رفتن به لینک‌های سریع">
    <span aria-hidden="true">↓</span>
    <span>ادامه</span>
  </a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-quick-links__item"><i class="fas fa-play"></i> پیش‌نیاز</a>
  <a href="../arch/rgw/learning-program/" class="hub-quick-links__item"><i class="fas fa-list-ol"></i> همه فازها</a>
  <a href="../arch/rgw/guides/development-convention/" class="hub-quick-links__item"><i class="fas fa-file-code"></i> قراردادها</a>
  <a href="../cheatsheet/guides/contributing/" class="hub-quick-links__item"><i class="fas fa-hand-holding-heart"></i> مشارکت</a>
</div>

<section class="hub-section" id="learn">
  <div class="hub-section__head">
    <div class="hub-section__icon">🎓</div>
    <h2 class="hub-section__title">برنامه یادگیری</h2>
    <p class="hub-section__subtitle">فازها را به ترتیب دنبال کنید — از پیش‌نیاز تا multisite و زیرسیستم‌ها</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">0️⃣</div>
      <h3 class="hub-card__title">پیش‌نیازها</h3>
      <p class="hub-card__text">ابزارها، چیدمان کدبیس و دانش پایه.</p>
      <a href="../arch/rgw/learning-program/00-prerequisites/" class="hub-card__link">شروع از اینجا <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">🛤️</div>
      <h3 class="hub-card__title">فاز ۰ — مسیر درخواست</h3>
      <p class="hub-card__text">ردیابی HTTP از frontend تا RADOS.</p>
      <a href="../arch/rgw/learning-program/01-phase-0-request-path/" class="hub-card__link">فاز ۰ <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">✅</div>
      <h3 class="hub-card__title">برنامه کامل</h3>
      <p class="hub-card__text">همه فازها، چک‌لیست و پیگیری پیشرفت.</p>
      <a href="../arch/rgw/learning-program/" class="hub-card__link">فهرست برنامه <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="conventions">
  <div class="hub-section__head">
    <div class="hub-section__icon">📐</div>
    <h2 class="hub-section__title">قراردادها و راهنما</h2>
    <p class="hub-section__subtitle">docs-as-code، یادداشت‌های استقرار، استناد کد در مستندات</p>
  </div>
  <div class="hub-cards hub-cards--three">
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">قرارداد توسعه</h3>
      <a href="../arch/rgw/guides/development-convention/" class="hub-card__link">مطالعه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">پیاده‌سازی استقرار</h3>
      <a href="../arch/rgw/guides/deployment-implementation-guide/" class="hub-card__link">مطالعه <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card hub-card--compact">
      <h3 class="hub-card__title">کد در مستندات</h3>
      <a href="../arch/rgw/guides/source-code-in-docs/" class="hub-card__link">مطالعه <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section" id="workflow">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🔄</div>
        <h2 class="hub-section__title">همگام‌سازی از upstream</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          نسخه‌های فارسی اصلی در <code>dev-code/rgw/docs-extended/</code> (کلون محلی ceph/ceph).
        </p>
        <a href="../cheatsheet/guides/contributing/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-book-open"></i> راهنمای مشارکت</a>
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
      <div class="hub-footer__brand"><span>🛠️</span> توسعه</div>
      <p class="hub-footer__note">پورتال مستقل توسعه‌دهندگان · <a href="/fa/">Ceph Docs Hub</a></p>
    </div>
    <div class="hub-footer__meta">
      <p>محتوا در مسیرهای <a href="../arch/">معماری</a> میزبانی می‌شود</p>
    </div>
  </div>
</footer>

</div>
