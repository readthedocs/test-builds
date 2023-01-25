Use external builders to generate different formats (``build.jobs``)
====================================================================

* Use ``zundler`` to create the HTMLZip version
* Use ``SimplePDF`` to generate the PDF version

----

Read the Docs ``.readthedocs.yaml`` configuration file used to build this docs.

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

``requirements.txt`` used to build these docs.

.. literalinclude:: ../requirements.txt
   :language: txt
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
