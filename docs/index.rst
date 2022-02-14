Use ``build.tools`` without defining ``build.os``
=================================================

Example using ``build.tools.python`` **without**  ``build.os`` in Read the Docs config file.
As ``build.os`` is *required* we should see a good message communicating this immediately.

See https://github.com/readthedocs/readthedocs.org/issues/8912

----

Read the Docs configuration file used to build this docs (:doc:`see full file <.readthedocs.yaml>`),

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
