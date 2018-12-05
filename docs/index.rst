timeout
=======

Sleep 1000 seconds to generate a build timeout.

Build should fail and proper error should be shown to the user.

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC


.. runblock:: pycon

   >>> # Generate a timeout here
   >>> import time
   >>> time.sleep(1000)
