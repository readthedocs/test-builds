conda-satisfied-skip-solve
==========================

Build docs using a ``conda`` environment.

This build pins ``sphinx==1.8.1`` and the logs should show that version is installed and not updated.
The conda command should be::

  conda install --quite --satisfied-skip-solve --name ...


Related issues/prs:

* https://github.com/rtfd/readthedocs.org/pull/5631
* https://github.com/rtfd/readthedocs.org/issues/3829
* https://github.com/rtfd/readthedocs-docker-images/pull/102


.. literalinclude:: ../environment.yaml
   :language: yaml
   :linenos:


The version of Sphinx shown here should be ``1.8.1`` which is the one pinned in the conda YAML file.

.. runblock:: pycon

   >>> import sphinx
   >>> sphinx.__version__

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
