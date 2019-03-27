git-lfs
=======

Include an image saved with `git-lfs`_ which should display properly here:

.. _git-lfs: https://git-lfs.github.com/

.. figure:: img/git-lfs.png
   :target: https://www.flickr.com/photos/opensourceway/5009661706/

   https://www.flickr.com/photos/opensourceway/5009661706/

----

Print content of ``git-lfs.png`` file. If it's just plain text,
it means that Read the Docs is not downloading the file properly using ``git-lfs``.

.. runblock:: pycon

   >>> print(open('img/git-lfs.png').read())

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
