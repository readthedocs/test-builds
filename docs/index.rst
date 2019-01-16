robots-txt
==========

This branch contains a ``robots.txt`` file.

When this version is configured as the *Default version* from **Admin > Advanced Settings**,
the project privacy is ``public``, the version ``public``, ``active`` and ``built``,
by hitting https://test-builds.readthedocs.io/robots.txt you should see this content:

.. literalinclude:: static/robots.txt
   :language: text
   :linenos:

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
