pygments-custom-lexer-apex
==========================

Uses ``pygments-lexer-apex`` package to colorize Salesforce Apex language.


.. literalinclude:: FundController.apxc
   :language: apex
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
