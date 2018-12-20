branch/with/slashes
===================

This is a branch (Read the Docs' Version object) that has slashes on it's name: ``branch/with/slashes``

Build should pass without problem.

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
