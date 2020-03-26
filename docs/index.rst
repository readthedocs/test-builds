.. include:: ../README.rst

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

New pages:

.. toctree::
   :maxdepth: 1
   :glob:

   *
