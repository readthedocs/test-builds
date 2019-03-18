japanese-pdf
============

This documentation should build properly when selecting ``Japanese``
from :guilabel:`Admin` > :guilabel:`Language`.

Here are some text in Japanese as example (using Google Translator):

これは日本語の例です。

それは成功するべきであり、エラーは報告されるべきではありません。

`The PDF can be seen here <https://readthedocs.org/projects/test-builds/downloads/pdf/japanese-pdf/>`_
and should look correct.

----

Sphinx configuration file to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :end-before: ###########################################################################
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC
