.. include:: ../README.rst

----

Flyout placement
----------------

.. raw:: html

    <div id="readthedocs-embed-flyout">

Config
------	

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
