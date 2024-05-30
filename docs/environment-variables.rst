environment-variables
=====================

These are the environment variables used to build this docs:

.. runblock:: pycon

   >>> import os
   >>> import pprint
   >>> pprint.pprint(dict(os.environ))

There is a variable called ``SECRET_VALUE_ESCAPED`` with this content
``{1}\|\1+-(8)$`` that should be shown correctly.
