shot-scraper
============

Automate screenshot generation with ``shot-scraper`` (https://shot-scraper.datasette.io/).

I used this blog post as reference
https://simonwillison.net/2022/Oct/14/automating-screenshots/

Screenshot
----------

This is an screenshot of https://datasette.io/ taken with ``shot-scraper``:

.. image:: _static/datasette.png
   :width: 80%
   :align: center

----

Read the Docs configuration file, ``.readthedocs.yaml``:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

Sphinx configuration file used to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
