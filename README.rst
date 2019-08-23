Test Builds
===========

Just testing

This repository is used internally to create different scenarios
on build configs and trigger many builds on Read the Docs productions.

Each branch should explain on it's ``docs/index.rst`` what's about and how the
QA process can be considered a success or a failure.

If we need to test a very specific use case, we create a new branch with
the issue number and the repository, like: ``issue-1234-org``, ``issue-4321-ext`` or similar.


Scenarios
---------

Each of these scenarios is a branch that can be built independenly from the others.

* `alabaster-theme <https://test-builds.readthedocs.io/en/alabaster-theme/>`_: use ``alabaster`` as theme
* `auto-wipe <https://test-builds.readthedocs.io/en/auto-wipe/>`_: used for auto wipe the environment when a config is changed
* `branch/with/slashes <https://test-builds.readthedocs.io/en/branch-with-slashes/>`_: used to check that git clones without problem
* `conda-env <https://test-builds.readthedocs.io/en/conda-env/>`_: use a simple conda environment to build the docs
* `conda-env-py3.7 <https://test-builds.readthedocs.io/en/conda-env-py3.7/>`_: use a simple conda environment to build the docs with Python 3.7
* `datetime <https://test-builds.readthedocs.io/en/datetime/>`_: shows different times (system time, build time, etc)
* `environment-variables <https://test-builds.readthedocs.io/en/environment-variables/>`_: shows all the environment variables used to build the docs
* `huge-build-output <https://test-builds.readthedocs.io/en/huge-build-output/>`_: generate megabytes of output data for commands
* `none-formats <https://test-builds.readthedocs.io/en/none-formats/>`_: use ``formats: []`` so only HTML is built
* `requirements-not-found <https://test-builds.readthedocs.io/en/requirements-not-found/>`_: use ``requirements_file: .notfound.txt``
* `robots-txt <https://test-builds.readthedocs.io/en/robots-txt/>`_: use a custom ``robots.txt`` for this project
* `search-with-old-sphinx-and-theme <https://test-builds.readthedocs.io/en/search-with-old-sphinx-and-theme/>`_: search box on old Sphinx and RTD theme version
* `timeout <https://test-builds.readthedocs.io/en/timeout/>`_: generate a timeout by sleeping 1000 seconds
* `typlog-theme <https://test-builds.readthedocs.io/en/typlog-theme/>`_: use ``typlog`` as theme
* `ŭñíč°də-branch <https://test-builds.readthedocs.io/en/ŭñíč°də-branch/>`_: the name of the branch is unicode
* `unicode-filename <https://test-builds.readthedocs.io/en/unicode-filename/>`_: has a page (rst) that its filename is unicode
* `use-py2 <https://test-builds.readthedocs.io/en/use-py2/>`_: use ``python: version: 2``
* `yaml-v2 <https://test-builds.readthedocs.io/en/yaml-v2/>`_: use a simple YAML for the V2 configuration


.. note::

  There could be more scenarios probably, but this list is not always up to date.
  Please, check `all the branches <https://github.com/rtfd/test-builds/branches/>`_ to be sure.

Tags
----

We also have some tags to have some tests around this.

* `tag-v1 <https://test-builds.readthedocs.io/en/tag-v1/>`_: points to an specific commit
* `tag-v2 <https://test-builds.readthedocs.io/en/tag-v2/>`_: points to the same commit than ``tag-v1`` (`Delete tags with same commit <https://github.com/rtfd/readthedocs.org/pull/4915>`_)


Addind a new scenario to the repository
---------------------------------------

#. Create a new branch from ``master`` using an appropiate name
#. Explain what's the use case in its ``docs/index.rst`` file

   * How to check if the QA can be considered success or failure
   * Add links to the issue tracker where there are more information
#. Add or modify the necessary files

   * Make sure that these files contains the minimum configuration needed:
   
     * remove auto generated comments
     * configs not used
#. Push your changes
#. Modify the ``README.rst`` file from ``master`` to add this new branch in the list
