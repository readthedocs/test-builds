datetime
========

Show different times: UTC, local time, etc

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
   >>> datetime.datetime.now()  # local time

.. runblock:: pycon

   >>> # Build at with timezones
   >>> import datetime
   >>> import pytz
   >>> from pytz import timezone
   >>> utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
   >>> utcnow.astimezone(timezone('Europe/Madrid'))  # Madrid, Spain
   >>> utcnow.astimezone(timezone('America/Los_Angeles'))  # Los Angeles, USA
   >>> utcnow.astimezone(timezone('America/Guayaquil'))  # Guayaquil, Ecuador
