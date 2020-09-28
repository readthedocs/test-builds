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

Each of these scenarios is a branch that can be built independently from the others.

Please, check `all the branches <https://github.com/readthedocs/test-builds/branches/>`_ and
`all the tags <https://github.com/readthedocs/test-builds/tags/>`_ to be sure.



Adding a new scenario to the repository
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
