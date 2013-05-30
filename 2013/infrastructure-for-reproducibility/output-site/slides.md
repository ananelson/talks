Dexy for Reproducible Science
-----------------------------

<http://dexy.it>
<a href="http://twitter.com/dexyit">@dexyit</a>
<br />
Ana Nelson
<a href="http://twitter.com/ananelson">@ananelson</a>
ana@ananelson.com


<img src="logo.png" width="400px;" />

* document-oriented 'make'
* project automation
* code is code, prose is prose, data is data
* many-to-many relationships of prose to code/data
* document live code
* Open Source (MIT)
* Written in Python


Dexy Can
--------

* Run Python code
* Compile and run C code
* Run text-to-speech on a file...
* ...then make R graph a waveform of the audio.
* Spin up EC2 instances, run scripts via ssh.
* Convert Markdown to HTML
* Obtain data from APIs
* Publish results to APIs (WordPress)
* <http://dexy.it/filters>


Software Documentation
----------------------

You can also use Dexy to document your:

* web app (e.g. installation guide from bash script, screenshots from casper.js)
* command line tool
* library
* Desktop app via Sikuli?


Installation
------------

Python (2.6 or 2.7) &#10004;
pip (or easy\_install) &#10004;
`pip install dexy`


Write documents,
write scripts,
use dexy to tie it all together.
<br />
Example config file:

{{ d['example/dexy.yaml|pyg'] }}


Demo
----
- <a target="_new" href="/example/index.html">generated file</a>
- <a target="_new" href="/example/index.md.html">markdown source</a>
- <a target="_new" href="/example/code001.py.html">python source 1</a>
- <a target="_new" href="/example/code002.py.html">python source 2</a>
- <a target="_new" href="/example/data.csv.html">csv</a>
- Run all with: `dexy`


Capture &amp; Representation
----------------------------
- Dexy requires users to construct a reproducible workflow (using any number of command line/scriptable tools).
- Dexy's config files capture dependencies and instructions (i.e. which filters to apply to which files).


Portability
-----------

- Dexy itself is portable (in principle) to any platform which supports Python.
- Some filters will be unavailable on some platforms - if they depend on libraries/tools not supported or with different behavior.
- Dexy is flexible - we can generate portability reports or warn users.


Document Linkage
----------------

- Dexy was designed for this.
- Include whole documents, or sections of documents.
- Dexy's helper library works with variety of templating tools, including Jinja.
- Dexy is designed to work with assets in input files and those generated as side-effects of running scripts.


Archival
--------
- Dexy's minimal approach makes it easy to upgrade projects to work with currently available software.
- Dexy's working files and logs can be added to a project repository to record a snapshot of a particular run.
- Dexy is highly extensible - can generate reports/archives including software used.


Thanks
------

Should Dexy support your tool?
info@dexy.it
