<div class="hub-page" dir="rtl">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <div class="hub-nav__brand">
      <div class="hub-nav__logo">🐙</div>
      <div>
        <p class="hub-nav__title">Ceph Docs Hub</p>
        <p class="hub-nav__subtitle">مستندات حرفه‌ای Ceph S3</p>
      </div>
    </div>
    <div class="hub-nav__links">
      <a href="#cheatsheet" class="hub-nav__link">Cheatsheet</a>
      <a href="#architecture" class="hub-nav__link">معماری</a>
      <a href="#develop" class="hub-nav__link">توسعه</a>
      <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener" class="hub-nav__link">
        <i class="fab fa-github"></i> گیت‌هاب
      </a>
    </div>
    <a href="#get-started" class="hub-nav__cta"><i class="fas fa-rocket"></i> شروع کنید</a>
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
        مرجع کامل Cheatsheet، معماری عمیق RGW و راهنمای توسعه‌دهندگان Ceph Object Gateway (S3)
      </p>
      <div class="hub-hero__actions">
        <a href="/cheatsheet/" class="hub-btn hub-btn--primary"><i class="fas fa-book"></i> Cheatsheet را ببینید</a>
        <a href="/arch/" class="hub-btn hub-btn--outline"><i class="fas fa-layer-group"></i> معماری RGW</a>
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
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-bolt"></i> High Performance</div>
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
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-shield-alt"></i> Enterprise Ready</div>
      </div>
    </div>
  </div>
  <div class="hub-scroll-hint"><span>↓</span><span>بیشتر بدانید</span></div>
</section>

<section class="hub-section" id="cheatsheet">
  <div class="hub-section__head">
    <div class="hub-section__icon">📋</div>
    <h2 class="hub-section__title">Cheatsheet</h2>
    <p class="hub-section__subtitle">مرجع سریع دستورات، تنظیمات و راهنماهای عملیاتی روزانه Ceph</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card">
      <div class="hub-card__icon">🐙</div>
      <h3 class="hub-card__title">دستورات CLI</h3>
      <p class="hub-card__text">ceph، osd، mon، rgw، rbd و صدها دستور کاربردی با مثال‌های واقعی</p>
      <a href="/cheatsheet/cli/" class="hub-card__link">مشاهده cheatsheet کامل <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">⚙️</div>
      <h3 class="hub-card__title">تنظیمات بهینه</h3>
      <p class="hub-card__text">بهترین تنظیمات برای production، scalability، multisite و performance</p>
      <a href="/cheatsheet/config/" class="hub-card__link">مشاهده تنظیمات <i class="fas fa-arrow-left"></i></a>
    </div>
    <div class="hub-card">
      <div class="hub-card__icon">📈</div>
      <h3 class="hub-card__title">راهنماهای مقیاس‌پذیری</h3>
      <p class="hub-card__text">نصب، مانیتورینگ، بکاپ، disaster recovery و سناریوهای واقعی</p>
      <a href="/cheatsheet/guides/" class="hub-card__link">شروع کنید <i class="fas fa-arrow-left"></i></a>
    </div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="architecture">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🏗️</div>
        <h2 class="hub-section__title">معماری عمیق RGW</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">
          درک کامل مسیر درخواست‌ها، SAL، RADOS driver، احراز هویت، multisite و scheduler در Ceph Object Gateway
        </p>
        <ul class="hub-list">
          <li><span class="hub-list__arrow">→</span><div><strong>Request Flow</strong><p>از دریافت درخواست HTTP تا ذخیره‌سازی در RADOS</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Multisite Sync</strong><p>مکانیزم همگام‌سازی بین دیتاسنترها</p></div></li>
          <li><span class="hub-list__arrow">→</span><div><strong>Authentication &amp; Authorization</strong><p>S3-compatible auth mechanisms</p></div></li>
        </ul>
        <a href="/arch/rgw/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-layer-group"></i> کاوش internals RGW</a>
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
    <h2 class="hub-section__title">راهنمای توسعه‌دهندگان</h2>
    <p class="hub-section__subtitle">Workflow، conventions، build و مشارکت در پروژه Ceph</p>
  </div>
  <div class="hub-develop-box">
    <div class="hub-develop-box__icon">🚀</div>
    <h3>برنامه یادگیری و Docs-as-Code</h3>
    <p>مسیر ساخت‌یافته در <code>src/rgw/</code> — همگام‌شده از upstream docs-extended.</p>
    <a href="/dev/" class="hub-btn"><i class="fas fa-code"></i> مشاهده بخش توسعه</a>
  </div>
</section>

<footer class="hub-footer">
  <div class="hub-footer__inner">
    <div>
      <div class="hub-footer__brand"><span>🐙</span> Ceph Docs Hub</div>
      <p class="hub-footer__note">مستندات فارسی و فنی Ceph S3</p>
    </div>
    <div class="hub-footer__meta">
      <p>منبع: ceph/ceph • src/rgw • RaminNietzsche</p>
      <div class="hub-footer__social">
        <a href="https://github.com/RaminNietzsche/ceph-cheatsheet" target="_blank" rel="noopener"><i class="fab fa-github"></i></a>
      </div>
    </div>
  </div>
  <p class="hub-footer__copy">© ۱۴۰۵ — ساخته شده با ❤️ برای جامعه Ceph فارسی</p>
</footer>

</div>
