Build with ``build.jobs``
=========================


This version is built with ``build.jobs``.

.. note::

   The following text should be something different than ``{ VERSION }``: {VERSION}

   We are using ``sed`` to replace the version with the value of ``READTHEDOCS_VERSION_NAME``.

----

.. literalinclude:: .readthedocs.yaml
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
