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

Docker images in our Build servers::

  REPOSITORY          TAG                 IMAGE ID
  readthedocs/build   4.0                 0b13addb85cd
  readthedocs/build   latest              0b13addb85cd
  readthedocs/build   5.0rc1              4fc1878d18b1
  readthedocs/build   4.0rc1              95575448a59a
  readthedocs/build   3.0                 21110214e6a0
  readthedocs/build   stable              21110214e6a0
  readthedocs/build   2.0                 9468fcb95b87

.. warning::

   This images/hashes are not automatically updated.

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
