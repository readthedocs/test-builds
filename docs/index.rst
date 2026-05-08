gVisor integration test
=======================

This branch is a smoke test for running Read the Docs builds inside a
gVisor-sandboxed runtime. If the build succeeds and the kernel string below
renders, the build environment is working.

Captured kernel string
----------------------

The ``uname -a`` output below is captured at build time, before Sphinx runs:

.. literalinclude:: uname.txt
   :language: text

How to read it
~~~~~~~~~~~~~~

* Under stock Linux (``runc``) the string looks like
  ``Linux ... #1 SMP ... x86_64 GNU/Linux``.
* Under gVisor (``runsc``) the kernel reports itself as ``gVisor`` and the
  release/version fields differ.

How to verify
-------------

The build is successful when:

* The build exits 0.
* This page renders.
* The captured ``uname -a`` line is present and non-empty.

----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:
