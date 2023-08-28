var disqus_config = function () {
    this.page.url = document.location.href;
    this.page.identifier = document.location.pathname;
  };

  (function() { 
    var d = document, s = d.createElement('script');
    s.src = '//kurakahani.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
  })();