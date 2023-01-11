Modify HTML via ``build.jobs.post_build``
=========================================

Modify the content of the HTML in ``build.jobs.post_build`` by replacing some text using ``sed``.
Test case for https://github.com/readthedocs/readthedocs.org/issues/9179

.. note::

   This text should say something different than a placesholder:

   $IM_A_PLACEHOLDER


----

.. literalinclude:: .readthedocs.yaml
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
