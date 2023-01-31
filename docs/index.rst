Sphinx multi-page HTMLZip
=========================

Use the same output from ``StandaloneHTMLBuilder`` to generate a zipped version of it.
Expose the ``.zip`` file as downloadable content.

----

Read the Docs ``.readthedocs.yaml`` configuration file used to build this docs.

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
