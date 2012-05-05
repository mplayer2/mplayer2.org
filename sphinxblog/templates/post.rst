.. raw:: html

    <div class="full-news">

{{ post.title }}
{{ "-" * post.title|count }}

Posted by {{ post.author }} on {{ post.date }}

{{ post.abstract }}

{{ post.body }}

Comments
________

.. raw:: html

    <div id="disqus_thread"></div>
    <script type="text/javascript">
        var disqus_shortname = 'mplayer2';
        var disqus_identifier = '{{ post.url }}';
        var disqus_url = 'http://www.mplayer2.org{{ post.url }}';

        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>

    </div>

