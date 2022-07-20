Build with Poetry
=================

Build the documentation shown here with ``poetry install`` under ``build.jobs``.
It's using the official and recommended way to install Poetry on Linux.
See https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions

----

.. literalinclude:: ../pyproject.toml
   :language: toml
   :linenos:

----

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
