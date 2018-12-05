conda-env-py3.7
===============

Build docs using a ``conda`` environment.

Install all dependencies via ``conda``.

Use ``python3.7.1`` from ``conda``.

Build should success without any problem.

.. runblock:: pycon

   >>> variable = 'I want to use f-strings here'
   >>> f'Replace my {variable} here'


.. runblock:: pycon

   >>> # Python Version used
   >>> import sys
   >>> print(sys.version)


.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
