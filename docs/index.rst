.. meta::
   :description: This is a meta tag added to the HTML output.

meta tags
=========

There should be some extra ``<meta>`` tags in this file.

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
