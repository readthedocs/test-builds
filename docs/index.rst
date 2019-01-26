sphinx2
=======

Use Sphinx2 to build the docs and our own theme.

----

Requirements file used:

.. literalinclude:: ../requirements.txt
   :language: txt
   :linenos:

----

.. runblock:: pycon

   >>> import os
   >>> os.system('pip freeze')

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
