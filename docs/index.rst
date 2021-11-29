Fail the build on pip install with env variable
===============================================


What happen if the requirements URL contains a ``GITHUB_TOKEN`` environment variable and it fails?

----

Read the Docs configuration file used to build this docs (:doc:`see full file <.readthedocs.yaml>`),

.. literalinclude:: .readthedocs.yaml
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
