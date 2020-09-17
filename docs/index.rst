run-rust
========

Used ``build.image: testing`` to call ``cargo`` command (checking that Rust is installed).
We are expecting to have a successful build and this page should show ``cargo --version`` output.

.. runblock:: pycon

   >>> import subprocess
   >>> command = subprocess.run(['cargo', '--version'], capture_output=True)
   >>> print(command.stdout)

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
