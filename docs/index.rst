requirements-not-found
======================

We use ``requirements_file: .notfound.txt`` in the YAML config.

Build should fail with a proper user message informing about this in a
clear way. Currently, the message says,

  Problem in your project's configuration. Invalid
  "requirements_file": path .notfound.txt does not exist

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
