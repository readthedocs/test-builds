big-packages
============

Install packages like ``torch`` and ``tensorflow``.

They shouldn't fail when installing via simple ``pip`` command.

.. note::

   Keep in mind that this packages are not even used to build the documentation.
   The whole build just fail at installation time.

----

.. literalinclude:: ../requirements.txt
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
