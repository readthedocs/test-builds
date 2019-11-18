htmldir
=======

Test for htmldir building in YAML file.

YAML file used to build these docs:

.. toctree::
   :glob:

   *
   folder/*

.. literalinclude:: ../.readthedocs.yml
   :language: yaml
   :linenos:

Config file used:

.. literalinclude:: conf.py
   :language: python
   :linenos:

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
