Private pip dependency in setup.py
==================================

Install a private pip dependency using an environment variable on ``setup.py``:

.. literalinclude:: ../setup.py
   :language: python
   :emphasize-lines: 25-29
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
