<div class="hub-page hub-page--section hub-page--cheatsheet" lang="zh">

<nav class="hub-nav">
  <div class="hub-nav__inner">
    <a href="." class="hub-nav__brand">
      <div class="hub-nav__logo">📋</div>
      <div>
        <p class="hub-nav__title">速查表</p>
        <p class="hub-nav__subtitle">运维参考</p>
      </div>
    </a>
    <div class="hub-nav__links">
      <a href="#guides" class="hub-nav__link">指南</a>
      <a href="#cli" class="hub-nav__link">CLI</a>
      <a href="#config" class="hub-nav__link">配置</a>
      <a href="guides/quickstart/" class="hub-nav__link">快速入门</a>
    </div>
    <div class="hub-nav__actions">
      <a href="../" class="hub-nav__hub-link" title="Ceph Docs Hub"><i class="fas fa-home"></i> Hub</a>
      <div class="hub-lang" role="navigation" aria-label="语言">
        <a href="../../cheatsheet/" class="hub-lang__item" lang="en" hreflang="en" title="English">EN</a>
        <a href="../../fa/cheatsheet/" class="hub-lang__item" lang="fa" hreflang="fa" title="فارسی">فا</a>
        <span class="hub-lang__item hub-lang__item--active" lang="zh">中文</span>
      </div>
      <a href="guides/OVERVIEW/" class="hub-nav__cta"><i class="fas fa-compass"></i> 浏览指南</a>
    </div>
  </div>
</nav>

<section class="hub-hero hub-hero--section" id="top">
  <div class="hub-hero__grid">
    <div>
      <div class="hub-hero__badge">
        <span class="hub-hero__pulse"></span>
        离线友好 · 同步自 ceph/ceph
      </div>
      <h1 class="hub-hero__title">自信<span class="hub-gradient">运维</span> Ceph</h1>
      <p class="hub-hero__lead">CLI 命令、配置项与角色/规模指南，用于日常集群管理。</p>
      <div class="hub-hero__actions">
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--primary"><i class="fas fa-terminal"></i> CLI 参考</a>
        <a href="config/OVERVIEW/" class="hub-btn hub-btn--outline"><i class="fas fa-sliders-h"></i> 配置索引</a>
      </div>
      <div class="hub-hero__stats">
        <div><span class="hub-hero__stat-val">100+</span><span class="hub-hero__stat-label">CLI 命令</span></div>
        <div><span class="hub-hero__stat-val">2122</span><span class="hub-hero__stat-label">配置项</span></div>
        <div><span class="hub-hero__stat-val">13</span><span class="hub-hero__stat-label">子系统</span></div>
      </div>
    </div>
    <div class="hub-hero__visual">
      <div class="hub-hero__glow"></div>
      <div class="hub-terminal-wrap">
        <div class="hub-float-badge hub-float-badge--top"><i class="fas fa-copy"></i> 可复制</div>
        <div class="hub-terminal">
          <div class="hub-terminal__prompt">$ ceph -s</div>
          <div class="hub-terminal__line">health: HEALTH_OK</div>
          <div class="hub-terminal__prompt">$ radosgw-admin user list</div>
          <div class="hub-terminal__line hub-terminal__ok">["admin", "s3user"]</div>
        </div>
        <div class="hub-float-badge hub-float-badge--bottom"><i class="fas fa-bolt"></i> 日常运维</div>
      </div>
    </div>
  </div>
  <a href="#quick" class="hub-scroll-hint" aria-label="滚动到快捷链接"><span aria-hidden="true">↓</span><span>探索</span></a>
</section>

<div class="hub-quick-links" id="quick">
  <a href="cli/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-terminal"></i> CLI</a>
  <a href="config/OVERVIEW/" class="hub-quick-links__item"><i class="fas fa-sliders-h"></i> 配置</a>
  <a href="guides/quickstart/" class="hub-quick-links__item"><i class="fas fa-bolt"></i> 快速入门</a>
  <a href="guides/getting-started/" class="hub-quick-links__item"><i class="fas fa-seedling"></i> 入门</a>
  <a href="guides/troubleshooting-guide/" class="hub-quick-links__item"><i class="fas fa-wrench"></i> 故障排查</a>
</div>

<section class="hub-section" id="guides">
  <div class="hub-section__head">
    <div class="hub-section__icon">📈</div>
    <h2 class="hub-section__title">按角色与规模</h2>
    <p class="hub-section__subtitle">按职责与集群规模选择文档</p>
  </div>
  <div class="hub-cards">
    <div class="hub-card"><div class="hub-card__icon">👤</div><h3 class="hub-card__title">按角色</h3><p class="hub-card__text">集群管理员、存储运维、RGW、CephFS。</p><a href="guides/OVERVIEW/#by-role" class="hub-card__link">角色指南 <i class="fas fa-arrow-right"></i></a></div>
    <div class="hub-card"><div class="hub-card__icon">📐</div><h3 class="hub-card__title">按规模</h3><p class="hub-card__text">实验室、小型/大型生产、多站点。</p><a href="guides/OVERVIEW/#by-scale" class="hub-card__link">规模指南 <i class="fas fa-arrow-right"></i></a></div>
    <div class="hub-card"><div class="hub-card__icon">⚡</div><h3 class="hub-card__title">日常运维</h3><p class="hub-card__text">快速入门、故障排查、配置查找。</p><a href="guides/quickstart/" class="hub-card__link">快速入门 <i class="fas fa-arrow-right"></i></a></div>
  </div>
</section>

<section class="hub-section hub-section--alt" id="cli">
  <div class="hub-section__inner">
    <div class="hub-split">
      <div>
        <div class="hub-section__icon">🖥️</div>
        <h2 class="hub-section__title">CLI 命令参考</h2>
        <p class="hub-section__subtitle" style="margin: 1rem 0 0; text-align: inherit;">ceph、osd、mon、rgw、rbd、cephfs、cephadm — 可复制命令与示例。</p>
        <a href="cli/OVERVIEW/" class="hub-btn hub-btn--gradient" style="margin-top: 2rem;"><i class="fas fa-terminal"></i> CLI 索引</a>
      </div>
      <div class="hub-code-block"><pre>$ ceph status
$ radosgw-admin user list
$ rbd ls</pre></div>
    </div>
  </div>
</section>

<section class="hub-section" id="config">
  <div class="hub-section__head">
    <div class="hub-section__icon">⚙️</div>
    <h2 class="hub-section__title">配置选项</h2>
    <p class="hub-section__subtitle">由 upstream YAML 生成</p>
  </div>
  <div class="hub-cards hub-cards--four">
    <div class="hub-card hub-card--compact"><h3 class="hub-card__title">global</h3><a href="config/global/INDEX/" class="hub-card__link">852 项 <i class="fas fa-arrow-right"></i></a></div>
    <div class="hub-card hub-card--compact"><h3 class="hub-card__title">rgw</h3><a href="config/rgw/INDEX/" class="hub-card__link">441 项 <i class="fas fa-arrow-right"></i></a></div>
    <div class="hub-card hub-card--compact"><h3 class="hub-card__title">osd</h3><a href="config/osd/INDEX/" class="hub-card__link">158 项 <i class="fas fa-arrow-right"></i></a></div>
    <div class="hub-card hub-card--compact"><h3 class="hub-card__title">全部</h3><a href="config/OVERVIEW/" class="hub-card__link">完整索引 <i class="fas fa-arrow-right"></i></a></div>
  </div>
</section>

<footer class="hub-footer hub-footer--section">
  <div class="hub-footer__inner">
    <div><div class="hub-footer__brand"><span>📋</span> 速查表</div><p class="hub-footer__note">独立运维参考 · <a href="../">Ceph Docs Hub</a></p></div>
  </div>
</footer>

</div>
