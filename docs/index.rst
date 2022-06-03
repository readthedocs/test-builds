Build with Poetry
=================

Build the documentation shown here with ``poetry install`` under ``build.jobs``.

----

.. literalinclude:: ../pyproject.toml
   :language: toml
   :linenos:

----

.. literalinclude:: ../.readthedocs.yaml
   :language: toml
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
