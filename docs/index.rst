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

Read the Docs configuration file used to build this docs:

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


.. Sphinx 2.0.0 changes the ``master_doc`` to be ``index`` instead of ``contents``,
   so I'm adding the ``toctree`` directive here.

   https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master_doc

.. toctree::
   :glob:

   *
