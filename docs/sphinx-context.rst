Sphinx context
==============

These are all the values injected in the ``html_context``:

.. jinja::

   {%- for key, value in env.config.__dict__.items() %}
     {%- if key in ("values", "_raw_config", "overrides") %}
       {% continue %}
     {%- endif %}

   {{ key }}:
      .. code:: python

         {{ value }}
   {%- endfor %}
