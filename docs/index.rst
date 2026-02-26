Profiling User Builds
=====================

This branch demonstrates how to profile Python documentation builds to identify
CPU and memory bottlenecks. Profiles can be compared between a local build and
a Read the Docs production build to spot performance differences.

Two profiling tools are used:

- `pyinstrument <https://pyinstrument.readthedocs.io/>`_ — statistical CPU profiler with interactive HTML output
- :mod:`tracemalloc` — built-in memory allocation tracker

----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

Sphinx configuration file used to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC

----

This Build's Profile
--------------------

The Sphinx build itself is profiled end-to-end using
`pyinstrument <https://pyinstrument.readthedocs.io/>`_ and
:mod:`tracemalloc`.  Three phases are measured:

- **Init** — builder initialization and config loading
- **Read sources** — parsing all RST source files
- **Write output** — rendering and writing HTML

Each phase is checked against a generous time and memory budget.
Full-page links: `phase summary <build_phases.html>`_ · `interactive profile <build_profile.html>`_

Phase timing and budget summary:

.. raw:: html

   <iframe src="build_phases.html"
           style="width:100%; height:190px; border:1px solid #ccc; border-radius:4px;">
   </iframe>

Full interactive pyinstrument profile of this build (browse the call tree, filter frames, compare runs):

.. raw:: html

   <iframe src="build_profile.html"
           style="width:100%; height:600px; border:1px solid #ccc; border-radius:4px;">
   </iframe>

----

CPU Profiling
-------------

The :func:`~profiling_examples.fibonacci` (recursive, O(2ⁿ)) and
:func:`~profiling_examples.bubble_sort` functions serve as CPU-intensive
workloads. `pyinstrument <https://pyinstrument.readthedocs.io/>`_ generates a
self-contained interactive HTML report that is embedded below.

Full-page link: `cpu_profile.html <cpu_profile.html>`_

.. raw:: html

   <iframe src="cpu_profile.html"
           style="width:100%; height:600px; border:1px solid #ccc; border-radius:4px;">
   </iframe>

----

Memory Profiling
----------------

The :func:`~profiling_examples.memory_intensive_work` function allocates
large lists, dicts, and nested structures. The profile below shows the CPU
execution path *during* those memory-intensive operations, making it easy to
spot which allocation sites dominate build time.

Full-page link: `memory_profile.html <memory_profile.html>`_

.. raw:: html

   <iframe src="memory_profile.html"
           style="width:100%; height:600px; border:1px solid #ccc; border-radius:4px;">
   </iframe>

----

Memory Usage Summary
--------------------

:mod:`tracemalloc` also reports exact current and peak heap consumption:

.. runblock:: pycon

   >>> import tracemalloc
   >>> from profiling_examples import memory_intensive_work
   >>> tracemalloc.start()
   >>> _ = memory_intensive_work()
   >>> current, peak = tracemalloc.get_traced_memory()
   >>> tracemalloc.stop()
   >>> print(f"Current memory: {current / 1024 / 1024:.2f} MB")
   >>> print(f"Peak memory:    {peak / 1024 / 1024:.2f} MB")
