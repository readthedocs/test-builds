py3.9
=====

Build the docs with Python 3.9.

.. runblock:: pycon

   >>> import sys
   >>> sys.version_info
   >>> sys.version

.. runblock:: pycon

   >>> # Use merge (|) and update (|=) on dicts
   >>> # https://www.python.org/dev/peps/pep-0584
   >>> {1: 'a'} | {2: 'b'}
   >>> d1 = {1: 'a'}
   >>> d2 = {1: 'uno'}
   >>> d1 |= d2
   >>> d1

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
