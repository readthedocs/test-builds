envvar-config-file
==================

.. note::

   This is a test of https://github.com/readthedocs/readthedocs.org/issues/6311#issuecomment-1324426604
   but it seems it does not work...

Use a hacky way to define environment variables in the ``.readthedocs.yaml``.
These are the variables defined in the YAML:

:MYVAR1: |myvar1|
:MYVAR2: |myvar2|
:MYVAR3: |myvar3|


----

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
