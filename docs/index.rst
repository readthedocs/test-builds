conda-env
=========

Build docs using a ``conda`` environment.

Install all dependencies via ``conda``.

Build shouldn't fail because of ``conda.environment`` config key not defined.
It may fail for other reasons, tho.
See https://github.com/readthedocs/readthedocs.org/pull/10979#issuecomment-1896036953

.. runblock:: pycon

   >>> # Python Version used
   >>> import sys
   >>> print(sys.version)


.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
