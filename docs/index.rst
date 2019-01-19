custom-404-page
===============

This version uses the ``sphinx-notfound-page`` extension: https://github.com/humitos/sphinx-notfound-page

Once built, `404.html page <404.html>`_ should show

* all the CSS and Javascript properly,
* all the *internal* URLs should be absolute,
* page style should not visually break,
* all *external resources* with abasolute URLs (no modified),
* *internal* URLs must be pre-pended by ``/en/latest/`` which are the default language and default version

`Issue <https://github.com/rtfd/readthedocs.org/issues/353>`_ on Read the Docs that deal with this topic.

.. warning::

   Until Read the Docs does not implement the check for custom 404
   pages on the repository, **this branch won't shows 404
   automatically** on all 404 pages.

----

Sphinx configuration file to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
