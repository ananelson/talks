## FULL STACK DOCUMENTATION

A HOLISTIC APPROACH TO DOCUMENTATION, TESTING, DEVELOPMENT AND DEPLOYMENT
<p>
<http://dexy.it> <a href="http://twitter.com/dexyit">@dexyit</a>
Ana Nelson <a href="http://twitter.com/ananelson">@ananelson</a>
<http://github.com/ananelson/talks>
</p>

{% from 'dexy.jinja' import code, codes, hl with context %}

Developers Won't Write Docs.


Developers Won't Write Docs for other people in their spare time using crappy tools for free without the end result being valued and maintained.


Documentation Culture
---------------------

- Must be "we value/are willing to pay for docs" not just "we want docs".
- Docs must be maintainable (futility sucks).
- Tools must be fit for purpose.


Start With Developer Docs
-------------------------

- benefits developers AND everyone else
- allows developers to tell stories about what matters to them
- is a jumping-off point for the rest of the docs


An Example
----------

- <a href="file:///home/ana/dev/talks/2013/distill/output-site/developer.html" target="_new">Developer docs for the Django tutorial's polls app.</a>


Django. So, Python?
-------------------

- python
- html
- django templates
- bash
- sql
- javascript


![logo](logo.png)
- make-like tool
- automation, especially for documentation
- free-form, format-agnostic
- language-agnostic


dexy.yaml
---------
<p><a href="developer.rst.html" target="_new">developer.rst</a></p><br />

{{ d["dexy.yaml|idio"]['rst'] }}


dexy.yaml
---------
<br />

{{ d["dexy.yaml|idio"]['inputs'] }}


dexy.yaml
---------
<br />

{{ d["dexy.yaml|idio"]['run-casper'] }}


start server
------------
<br />

{{ d["scripts/reset-server.sh|idio|h"] }}


screenshots
-----------

- use [casper.js](http://casperjs.org) and [phantom.js](http://phantomjs.org)
- [link](screenshots.js.html)


stop server
------------
<br />

{{ d["scripts/stop-server.sh|idio|h"] }}


dexy.yaml
---------
<br />

{{ d["dexy.yaml|idio"]['run-tests'] }}


Dexy Demo
---------



What's Next?
------------

- End-User Docs
- Sysadmin Docs (s/localhost/IP-of-cloud-VM-I-just-launched/)
- Developer Tutorials
- API Docs
- Reporting


{{ d['analyze.R|idio|r|pyg']['query'] }}
![dotchart of votes](plot.png)


Automation
----------

- Maintainability
- Reusability
- Up-Front Investment, Pays Dividends


Holistic Development
--------------------

- Writing developer docs is a profoundly powerful tool for improving code.
    - Forces you to explain your code.
    - Presents your code in a new visual context.
- Automation means you don't have to flush your mental buffer mid-task.


Thank You!
----------
<p>
<http://dexy.it> <a href="http://twitter.com/dexyit">@dexyit</a>
Ana Nelson <a href="http://twitter.com/ananelson">@ananelson</a>
<http://github.com/ananelson/talks>
</p>
