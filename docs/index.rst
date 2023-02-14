sphinx-hoverxref
================

Make usage of ``sphinx-hoverxref`` and test different scenarios.

Tooltips with issues on glossary
--------------------------------

* Issue: https://github.com/readthedocs/sphinx-hoverxref/issues/97

Example:

* :term:`Term 1`
* :term:`Term 2`


Reference to a title
-----------------

:ref:`conf:conf.py`


Reference to a document
------------------------

:doc:`conf`

----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
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
