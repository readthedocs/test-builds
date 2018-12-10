environment-variables
=====================

These are the environment variables used to build this docs:

.. runblock:: pycon

   >>> import os
   >>> import pprint
   >>> pprint.pprint(dict(os.environ))


.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
