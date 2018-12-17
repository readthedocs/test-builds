search-with-old-sphinx-and-theme
================================

Using old version of ``Sphinx`` and ``sphinx_rtd_theme`` search field seems to be broken when searching for some values.

With ``Sphinx==1.5.2`` and ``sphinx_rtd_theme==0.1.9``, this shows::

    ReferenceError: jquery is not defined          readthedocs-doc-embed.js:1:33742

in the Firefox console and search is completely broken.

----

``requirements.txt`` file used to build this docs,

.. literalinclude:: ../requirements.txt
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
