submodule-git-scheme
====================

Use a ``git@github.com:`` URL for a submodule.

This build will fail because we don't support any other URLs than HTTPS in the Community site. I **will work** in the Corporate side, though.

----

``.gitmodules`` file:

.. literalinclude:: ../.gitmodules
   :linenos:

----

Sphinx configuration file to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
