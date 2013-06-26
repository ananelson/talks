========================================
Writing Reproducible Documents with Dexy
========================================

  author: Ana Nelson

Example 1
---------

{% from 'dexy.jinja' import code,codes with context -%}

First we assign variables:

{{ codes('code001.R|idio|r|pyg', 'assign-variables') }}

### Multiplication

Let's do some multiplication:

{{ codes('code001.R|idio|r|pyg', 'multiply') }}

Here's a graph:

{{ codes('code001.R|idio|r|pyg', 'graph') }}

.. image:: plot.pdf
