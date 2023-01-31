Sphinx PDF build with ``tectonic``
==================================

Uses ``tectonic`` to build a PDF after generating the ``.tex`` file with Sphinx
(https://tectonic-typesetting.github.io/en-US/)

See the issue https://github.com/readthedocs/readthedocs.org/issues/9598

----

Read the Docs configuration file

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
