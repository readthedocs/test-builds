c-dependencies
==============

Install some Python requirements that needs ``gcc`` to be built when installed as wheels.

----

.. literalinclude:: ../requirements.txt
   :language: text
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
