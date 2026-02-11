llms.txt
========

This project includes an ``llms.txt`` file in the root of the repository.

What is llms.txt?
-----------------

``llms.txt`` is a markdown file that provides a summary of project documentation
in a format optimized for Large Language Models (LLMs). It allows AI assistants
to quickly understand the purpose, structure, and key features of a project.

Purpose
-------

The ``llms.txt`` file serves several purposes:

* Provides a concise overview of the project for AI assistants
* Documents the repository structure and conventions
* Explains key features and testing scenarios
* Offers quick reference for common tasks and configurations

Content
-------

The ``llms.txt`` file in this repository includes:

* **Project description** - Overview of the test-builds repository
* **Purpose** - Why this repository exists and how it's used
* **Branch structure** - How different branches represent test scenarios
* **Features tested** - List of Read the Docs features being tested
* **Configuration** - Documentation build configuration details
* **Adding scenarios** - Guide for adding new test cases

File Location
-------------

The ``llms.txt`` file is located in the ``docs/static/`` directory and will be
served at the root URL (e.g., https://test-builds.readthedocs.io/llms.txt):

.. literalinclude:: static/llms.txt
   :language: markdown
   :caption: llms.txt
   :linenos:

Benefits
--------

Having an ``llms.txt`` file provides several benefits:

* **Faster onboarding** - New contributors can quickly understand the project
* **AI-friendly** - LLMs can efficiently parse and understand the project structure
* **Documentation hub** - Serves as a central reference point
* **Maintenance** - Easy to keep updated with key project information

Standards
---------

The ``llms.txt`` format is an emerging standard for making documentation
accessible to AI assistants. It uses markdown format for readability and
includes structured information about the project.

Learn More
----------

* The ``llms.txt`` file is automatically served at the root URL when configured
* It can be accessed alongside other static files like ``robots.txt``
* The file should be kept up-to-date as the project evolves
