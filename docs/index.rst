build-internals
===============

This page should show and match what it's defined in out YAML file
with what it's saved into the ``readthedocs-environment.json`` file to
build the documentation.

----

Read the Docs configuration file,

.. literalinclude:: ../.readthedocs.yml
   :language: yaml
   :linenos:

----

``readthedocs-environment.json`` internal file,

.. literalinclude:: ../../../envs/build-internals/readthedocs-environment.json
   :language: json
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
