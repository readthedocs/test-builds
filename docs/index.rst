Build Sphinx Docs with Zundler builder
======================================

Check out the Sphinx documentation built with ``zundler`` at: `zundler.html <_static/zundler.html>`_.


.. seealso::

   See https://github.com/sphinx-doc/sphinx/issues/10688#issuecomment-1243012875 for more information about the process used
   to build this documentation in one single HTML file.

----

Read the Docs ``.readthedocs.yaml`` configuration file used to build this docs.

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
