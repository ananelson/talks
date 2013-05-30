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
* free-form, general-purpose authoring and automation
* multi-language, multi-format
* Open Source (MIT)
* Written in Python


Dexy Can
--------

* Run Python code
* Compile and run C code
* Run text-to-speech on a file...
* ...then make R graph a waveform of the audio.
* Convert Markdown to HTML
* Compile LaTeX to PDF
* Upload images to S3
* Post HTML to a WordPress blog
* Just about anything code can do, dexy can do.


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
- Dexy makes it easy to upgrade projects to work with available software.
- Dexy can be developed to generate full project archives including software used to generate a certain run.


Thanks
------

Should Dexy support your tool?
info@dexy.it
