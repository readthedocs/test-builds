gVisor integration test
=======================

This branch exercises a Read the Docs build under a gVisor-sandboxed runtime.
It captures a small runtime fingerprint and one network round-trip before
running Sphinx, then publishes the captured output alongside the docs.

How to verify
-------------

The build is **successful** when:

* The build exits 0.
* `probe.txt <probe.txt>`_ is published and ``/proc/version`` indicates the
  expected runtime (contains ``gVisor`` for runsc, ``Ubuntu`` for runc).
* The ``pypi.org`` probe returns ``HTTP 200``.
* ``pip install`` and the Sphinx build succeed.

The build reveals a **gVisor-specific regression** when any of the above pass
on a non-sandboxed branch (e.g. ``build-commands``) but fail here.

----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
