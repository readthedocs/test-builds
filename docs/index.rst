pdf-build-jobs
==============

Use Read the Docs "normal workflow" to build the HTML,
but use ``build.jobs`` to create a PDF and put it on ``$READTHEDOCS_OUTPUT/pdf``
so serve it using the regular API and flyout.

----

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
