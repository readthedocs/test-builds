manual-integrations
===================

Initial PoC to manually integrate all the Read the Docs features.
Context:

* https://github.com/readthedocs/readthedocs.org/pull/9755
* https://github.com/readthedocs/readthedocs.org/issues/9063
* https://github.com/readthedocs/meta/issues/71
* https://github.com/readthedocs/readthedocs.org/pull/10127
* https://github.com/humitos/readthedocs-client

Take a look at :doc:`page`.

.. raw:: html

     <script>
       let element = document.createElement("readthedocs-docdiff");
       element.setAttribute({ base-url: "http://test-builds.devthedocs.org/en/latest/" });
       document.querySelector("[role=navigation").appendChild(element);
     </script>


----

Read the Docs configuration file used to build this docs:

.. literalinclude:: ../.readthedocs.yaml
   :language: yaml
   :linenos:

----

Sphinx configuration file used to build this docs (:doc:`see full file <conf>`),

.. literalinclude:: conf.py
   :language: python
   :linenos:

----

.. runblock:: pycon

   >>> # Build at
   >>> import datetime
   >>> datetime.datetime.utcnow()  # UTC

