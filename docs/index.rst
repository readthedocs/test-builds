sphinx.ext.duration
===================

Use ``sphinx.ext.duration`` extension to show how much time Sphinx spends on each file.
**Build output should show these times**.

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
