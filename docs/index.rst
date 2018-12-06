none-formats
============

Build the docs with ``formats: []``.

The build should succeed without problem and only HTML output has to
be built. This can be easily checked by taking a look at the output
commands from the Build itself and confirming that only one
``sphinx-build`` command was executed with the ``readthedocs``
builder.

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
