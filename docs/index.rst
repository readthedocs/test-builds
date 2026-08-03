uv sync with group
==================

Reproduces `readthedocs.org#13192 <https://github.com/readthedocs/readthedocs.org/issues/13192>`_.

Read the Docs should call ``uv sync --group docs`` before the ``build.html`` job.

----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

``pyproject.toml`` defining the ``docs`` dependency group:

.. literalinclude:: ../pyproject.toml
   :language: toml
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
