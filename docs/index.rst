Output content into ``_build/html``
===================================

Read the Docs is not using ``_build/html`` anymore.
Instead, it's using ``$READTHEDOCS_OUTPUT`` now.

Users outputting content to ``_build/html`` should be contacted and communicated about this
to avoid unexpected behavior.

We are now logging::

  Directory '_build/html' exists. This may lead to unexpected behavior.

when we detect the build is creating this directory.
We can find these logs in New Relic.


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
