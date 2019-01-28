pygments-custom-lexer-apex
==========================

Uses ``pygments-lexer-apex`` (GitHub_) package to colorize Salesforce Apex language.

.. _GitHub: https://github.com/shawalli/pygments-lexer-apex

Including ``FundController.apxc`` should show this file properly colorized by ``pygments``.


.. literalinclude:: FundController.apxc
   :language: apex
   :linenos:


----

``requirements.txt`` file to install the lexer:

.. literalinclude:: ../requirements.txt
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
