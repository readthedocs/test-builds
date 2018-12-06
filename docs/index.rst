use-py2
=======

Use ``python2`` to build this docs.

Build should succeed without any problem.

YAML file used,

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
