Developer Docs
==============

{% from "dexy.jinja" import code, codes, ext with context %}

Docs for `mysite_com`.

This website uses Django.

Site Config
-----------

URL routing is defined in a site-wide urls.py:

{{ code("mysite_com/mysite_com/urls.py|idio") }}

And a separate urls.py in the polls app:

{{ code("mysite_com/polls/urls.py|idio") }}


Admin Interface
---------------

Django provides a ready-made admin interface. The admin interface is activated
in `settings.py` as follows:

{{ codes('/mysite_com/mysite_com/settings.py|idio', 'installed-apps') }}

The admin interface is configured in the polls app:

{{ code('mysite_com/polls/admin.py|idio') }}

The base template for the admin section is:

{{ code("mysite_com/templates/admin/base_site.html|idio") }}

Further config is attached to the `Poll` class:

{{ codes("mysite_com/polls/models.py|idio", "admin-config") }}

Here is what the main admin page looks like:

.. image:: logged-in-admin.png

Here is the polls admin:

.. image:: polls-admin.png

Let's add a new poll:

{{ codes("screenshots.js|idio", "add-new-poll") }}

.. image:: add-new-poll-filled-in.png

Here's our new poll:

.. image:: poll-added.png

User Interface
--------------

For the user interface, there is more code to show. :-)

Models
......

The `models` module is imported from django:

{{ codes("mysite_com/polls/models.py|idio", "models") }}

We define a Poll class:

{{ codes("mysite_com/polls/models.py|idio", "poll") }}

And a Choice class:

{{ codes("mysite_com/polls/models.py|idio", "choice") }}

Here are the fields defined for Poll:

{{ codes("mysite_com/polls/models.py|idio", "poll-fields") }}

And for Choice:

{{ codes("mysite_com/polls/models.py|idio", "choice-fields") }}

Each defines a descriptive `__unicode__` method:

{{ codes("mysite_com/polls/models.py|idio", "poll-unicode") }}
{{ codes("mysite_com/polls/models.py|idio", "choice-unicode") }}

We also have a `was_published_recently` method defined on Poll:

{{ codes("mysite_com/polls/models.py|idio", "recent") }}

Views
-----

{{ code("mysite_com/polls/urls.py|idio") }}

Index
.....

{{ codes("mysite_com/polls/views.py|idio", "index") }}

{{ code("mysite_com/polls/templates/polls/index.html|idio") }}

.. image:: no-polls-available.png

.. image:: index.png

Detail
......

{{ codes("mysite_com/polls/views.py|idio", "index") }}

{{ code("mysite_com/polls/templates/polls/detail.html|idio") }}

.. image:: voting.png

Results
.......

{{ codes("mysite_com/polls/views.py|idio", "results") }}

{{ code("mysite_com/polls/templates/polls/results.html|idio") }}

.. image:: voted.png

.. image:: many-votes.png
