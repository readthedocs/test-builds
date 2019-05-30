activate-me
===========

This version/branch should be activated automatically and immediately after that it's pushed.
There is an Automation Rule ``^activate-me$`` existing for this project in the database.

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
