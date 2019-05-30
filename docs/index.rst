activate-me
===========

This version/branch should be activated automatically and immediately after that it's pushed.
There is an Automation Rule ``^activate-me$`` existing for this project in the database.

To re-test this rule, first delete the branch running::

  git push origin --delete activate-me

then, re create it running::

  git push activate-me origin/activate-me

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
