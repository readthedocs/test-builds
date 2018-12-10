Test Builds
===========

This repository is used internally to create different scenarios
on build configs and trigger many builds on Read the Docs productions.

Each branch should explain on it's ``docs/index.rst`` what's about and how the
QA process can be considered a success or a failure.

If we need to test a very specific use case, we create a new branch with
the issue number and the repository, like: ``issue-1234-org``, ``issue-4321-ext`` or similar.


Scenarios
---------

Each of these scenarios is a branch that can be built independenly from the others.

* alabaster-theme: use ``alabaster`` as theme
* auto-wipe: used for auto wipe the environment when a config is changed
* conda-env: use a simple conda environment to build the docs
* conda-env-py3.7: use a simple conda environment to build the docs with Python 3.7
* datetime: shows different times (system time, build time, etc)
* environment-variables: shows all the environment variables used to build the docs
* huge-build-output: generate megabytes of output data for commands
* none-formats: use ``formats: []`` so only HTML is built
* requirements-not-found: use ``requirements_file: .notfound.txt``
* timeout: generate a timeout by sleeping 1000 seconds
* typlog-theme: use ``typlog`` as theme
* unicode-filename: has a page (rst) that its filename is unicode
* use-py2: use ``python: version: 2``
* yaml-v2: use a simple YAML for the V2 configuration
* ŭñíč°də-branch: the name of the branch is unicode


To be created
~~~~~~~~~~~~~

These are some branches that do not exists yet, but we want to create:

* latest-image-py3.6: use ``build: image: latest`` and ``python: version: 3.6``
* sphinx-1.8: use ``Sphinx<1.9`` as requirement

Tags
----

We also have some tags to have some tests around this.

* tag-v1: points to an specific commit
* tag-v2: points to the same commit than ``tag-v1`` (`Delete tags with same commit <https://github.com/rtfd/readthedocs.org/pull/4915>`_)


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
