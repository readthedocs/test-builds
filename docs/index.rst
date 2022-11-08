py3.11
======

Build the docs with Python 3.11.

.. runblock:: pycon

   >>> import sys
   >>> sys.version_info
   >>> sys.version

.. runblock:: pycon

   >>> # Use Structural Pattern Matching
   >>> # https://www.python.org/dev/peps/pep-0636
   >>> import random
   >>> match random.choice(['test', 'quit', 'welcome']):
   ...   case 'test':
   ...     print('TEST')
   ...   case 'quit':
   ...     print('QUIT')
   ...   case 'welcome':
   ...     print('WELCOME')
   ...

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
