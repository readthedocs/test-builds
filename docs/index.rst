nbsphinx-3d-plot
================

This ``.ipynb`` file `should render properly <3D%20Plot.html>`_ and show a 3D Plot.


Reference: https://github.com/rtfd/readthedocs.org/issues/4367

----

Requirements file used (note that we need to install s specific version of ``sphinx-rtd-theme``):

.. literalinclude:: ../requirements.txt
   :language: txt
   :linenos:

----

All packages installed in the virtualenv used to generate this documentation (``pip freeze``):

.. runblock:: pycon

   >>> import os
   >>> os.system('pip freeze')

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
