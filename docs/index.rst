yaml-v2
=======

Use a requirements file from a submodule,
this shouldn't give an error.

YAML file used to build this docs,

.. literalinclude:: ../.readthedocs.yml
   :language: yaml
   :linenos:

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
