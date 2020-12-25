<template>
<div id="app">
<router-view/>
</div>
</template>
<style lang="scss">
@font-face {
  font-family: "Noto Sans JP";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: local("Noto Sans CJK JP"), local("Noto Sans JP"),
    url(//fonts.gstatic.com/ea/notosansjp/v5/NotoSansJP-Regular.woff2)
      format("woff2"),
    url(//fonts.gstatic.com/ea/notosansjp/v5/NotoSansJP-Regular.woff)
      format("woff"),
    url(//fonts.gstatic.com/ea/notosansjp/v5/NotoSansJP-Regular.otf)
      format("opentype");
}
* :not(.v-icon) {
  font-family: "Noto Sans JP", sans-serif;
  font-feature-settings: "palt" ；;
}
</style>