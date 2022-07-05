PR visual diff
==============

This branch shows a proof of concept for visual diff between two rendered versions: ``/en/latest/`` and current PR.

(based on this commit https://github.com/readthedocs/test-builds/commit/386db8c06f248093118a43bc824bc1681d0c77a9)

.. literalinclude:: ../app.js
   :language: javascript
   :emphasize-lines: 5
   :linenos:

----

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
