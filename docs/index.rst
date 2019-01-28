multiple-source-suffix
======================

Use multiple values (as a dict) for ``source_suffix`` Sphinx configuration: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-source_suffix

Depending on the Sphinx version different options (str, list, dict) are supported. Read the Docs should be able to handle/accept all of them.

This build uses ``.md`` and ``.rst`` files to build its docs. Using ``recommonmark`` and ``restructuredtext``.

:Related Pull Request: https://github.com/rtfd/readthedocs.org/pull/5183

----

Sphinx configuration file to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

``requirements.txt`` file:

.. literalinclude:: ../requirements.txt
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
