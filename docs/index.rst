submodule-https-scheme
====================

Use a ``https://`` URL for a submodule.

This build will work in both, Community and Corporate site.

----

``.gitmodules`` file:

.. literalinclude:: ../.gitmodules
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
