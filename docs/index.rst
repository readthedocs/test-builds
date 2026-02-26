Profiling User Builds
=====================

This branch demonstrates how to profile Python documentation builds to identify
CPU and memory bottlenecks. Profiles can be compared between a local build and
a Read the Docs production build to spot performance differences.

Two profiling tools are used:

- :mod:`cProfile` — built-in deterministic CPU profiler
- :mod:`tracemalloc` — built-in memory allocation tracker

The generated ``.prof`` files can be visualised interactively with
`snakeviz <https://jiffyclub.github.io/snakeviz/>`_ (included in
``requirements.txt``)::

   snakeviz cpu_profile.prof

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

CPU Profiling
-------------

The :func:`~profiling_examples.fibonacci` (recursive, O(2ⁿ)) and
:func:`~profiling_examples.bubble_sort` functions serve as CPU-intensive
workloads. :mod:`cProfile` records every function call and its cumulative
time so the hottest code paths are easy to spot.

.. runblock:: pycon

   >>> import cProfile, pstats, io
   >>> from profiling_examples import cpu_intensive_work
   >>> profiler = cProfile.Profile()
   >>> profiler.enable()
   >>> cpu_intensive_work()
   >>> profiler.disable()
   >>> profiler.dump_stats('/tmp/cpu_profile.prof')
   >>> stream = io.StringIO()
   >>> stats = pstats.Stats(profiler, stream=stream).sort_stats('cumulative')
   >>> _ = stats.print_stats(15)
   >>> print(stream.getvalue())

The ``/tmp/cpu_profile.prof`` file written above can be opened locally with
``snakeviz /tmp/cpu_profile.prof`` to explore an interactive flame graph.

----

Memory Profiling
----------------

The :func:`~profiling_examples.memory_intensive_work` function allocates
large lists, dicts, and nested structures. :mod:`tracemalloc` reports both
the current and peak heap usage so memory-heavy allocations can be tracked
across builds.

.. runblock:: pycon

   >>> import tracemalloc
   >>> from profiling_examples import memory_intensive_work
   >>> tracemalloc.start()
   >>> _ = memory_intensive_work()
   >>> current, peak = tracemalloc.get_traced_memory()
   >>> tracemalloc.stop()
   >>> print(f"Current memory: {current / 1024 / 1024:.2f} MB")
   >>> print(f"Peak memory:    {peak / 1024 / 1024:.2f} MB")
