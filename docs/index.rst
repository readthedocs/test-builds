gVisor integration test
=======================

This branch exercises a Read the Docs build under a gVisor-sandboxed runtime
and captures runtime fingerprints that differ between gVisor (``runsc``) and
the default OCI runtime (``runc``).

The build uses ``build.commands`` to run a series of probes before invoking
Sphinx, and writes the captured output into the published HTML so a reviewer
can inspect it after the build completes.

How to verify
-------------

The build is **successful** when:

* The build exits 0.
* ``probe.txt`` and ``probe.html`` are present in the published output.
* The Sphinx-rendered ``index.html`` is present.
* Outbound HTTPS to ``pypi.org`` and ``github.com`` returns ``200``.
* ``pip install`` of ``requirements.txt`` succeeds (i.e. PyPI works through
  gVisor's netstack).

The build reveals a **gVisor-specific regression** when:

* Any probe command fails on this branch but passes on a non-sandboxed branch
  (e.g. ``build-commands``).
* DNS resolution or HTTPS to PyPI/GitHub fails or is dramatically slower.
* ``pip install`` fails with a network or syscall error that does not
  reproduce on ``runc``.
* Sphinx fails to write output, suggesting filesystem/overlay differences.

What the probe captures
-----------------------

* **Runtime fingerprint** — ``uname``, ``/proc/version``, ``dmesg``,
  ``/proc/1/comm``, ``/proc/self/status``. Under gVisor, ``/proc/version``
  contains the string ``gVisor`` and ``CapEff`` / ``Seccomp`` typically differ.
* **Mounts** — gVisor presents a different overlay layout than ``runc``.
* **CPU / memory** — ``/proc/cpuinfo`` is synthesized by the Sentry kernel
  and looks notably different from a bare-metal or runc-reported CPU.
* **Networking** — gVisor's userspace netstack has independent TCP behavior;
  we time HTTPS round-trips to PyPI and GitHub.
* **Sensitive syscalls** — ``ptrace(PTRACE_TRACEME)``, ``unshare(CLONE_NEWUSER)``,
  ``perf_event_open``. gVisor either stubs or rejects these in ways that differ
  from ``runc``.

Where to find the results
-------------------------

After the build:

* `probe.html <probe.html>`_ — the captured probe output, rendered as HTML.
* `probe.txt <probe.txt>`_ — the raw text log.

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
