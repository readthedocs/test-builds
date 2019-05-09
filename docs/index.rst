install-pytorch
===============

PyTorch_ downloads ~700Mb and requires a lot of memory to be installed.
It usually fails because it's killed by the builder (even using 2Gb of memory).

.. _PyTorch: https://pypi.org/project/torch/

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
