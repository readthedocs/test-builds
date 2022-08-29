404 page with invalid URLs
==========================

Example showing what happens when creating a ``404.rst`` file with Sphinx *without using* ``sphinx-notfound-page``:
https://sphinx-notfound-page.readthedocs.io/

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
