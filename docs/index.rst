Intersphinx with mkdocstrings
=============================

Use the feature "Cross-references to other projects / inventories" from ``mkdocstrings``
to point directly to documentation objects.

The source project is built using Sphinx and,
the destination project is built using MkDocs + mkdocstrings' plugin.
Read more about this feature at https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories

Full documentation of ``mkdocstrings`` plugin at: https://mkdocstrings.github.io/

Examples:

* :py:class:`mkdocstrings.extension.AutoDocProcessor`
* :py:data:`mkdocstrings.plugin.RENDERING_OPTS_KEY`

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
