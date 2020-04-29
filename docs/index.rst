yaml-v2
=======

Use a YAML v2 configuration with many options.

(at this time, since V2 is not allowed to all the projects, this
project has enabled the feature ``allow_v2_config_file`` manually from
the Django shell)

YAML file used to build this docs,

.. literalinclude:: ../.readthedocs.yml
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
