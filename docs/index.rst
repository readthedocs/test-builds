Use external builders to generate different formats (``build.commands``)
========================================================================

* Use ``zundler`` to create the HTMLZip version
* Use ``SimplePDF`` to generate the PDF version
* Use regular ``sphinx-build -b epub`` to build ePUB version


.. note::

   This documentation has the flyout menu integrated even when using ``build.commands``.
   This is because the ``readthedocs-sphinx-ext`` extension was manually installed on purpose.

----

Read the Docs ``.readthedocs.yaml`` configuration file used to build this docs.

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

``requirements.txt`` used to build these docs.

.. literalinclude:: ../requirements.txt
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
