Use ``build.os`` and ``build.tools``
====================================

Example using ``build.os`` and ``build.tools`` in Read the Docs config file.

----

.. runblock:: pycon

   >>> import subprocess
   >>> subprocess.run('python --version'.split())
   >>> subprocess.run('conda --version'.split())
   >>> subprocess.run('node --version'.split())
   >>> subprocess.run('cargo --version'.split())
   >>> subprocess.run('go version'.split())

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
