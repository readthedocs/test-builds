c-dependencies
==============

Install some Python requirements that needs ``gcc`` to be built when installed as wheels.

I started trying with ``lxml``, ``PyPDF2`` and ``python-docx``.

I found that ``lxml==3.8.0`` (an old version) does not compile.

----

.. literalinclude:: ../requirements.txt
   :language: text
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
