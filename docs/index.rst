Skip a build based on command exit code
=======================================

Use ``build.jobs.post_checkout`` to execute a Git command and check if there are changes in the ``docs/`` directory.
If there aren't changes, we return 439 exit code to cancel the build immediately.

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
