manual-integrations
===================

Initial PoC to manually integrate all the Read the Docs features.
Context:

* https://github.com/readthedocs/readthedocs.org/pull/9755
* https://github.com/readthedocs/readthedocs.org/issues/9063
* https://github.com/readthedocs/meta/issues/71


----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

Sphinx configuration file used to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC

