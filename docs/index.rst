huge-build-output
=================

Generate a huge build output (~1Mb).

Build should pass. Output should be stripped to 1Mb after sending to
cold storage and a message saying this should be shown to the command
output in the build output page.

.. note::

   In case this build has been triggered multiple times, we could
   manually delete the ``Version`` to remove all this testing data.

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
