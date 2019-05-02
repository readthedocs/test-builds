pypy3.5
=======

Use ``pypy3.5`` to build this docs.

----

.. literalinclude:: ../readthedocs.yml
   :language: yaml
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
