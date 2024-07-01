sphinx context
==============

These are all the values from the Sphinx config object:

.. jinja::

   {%- for key, value in env.config.__dict__|dictsort %}
     {%- if key in ("values", "_raw_config", "overrides", "_overrides", "_options") %}
       {% continue %}
     {%- endif %}

   {{ key }}:
       .. code-block:: python

          {{ value|pprint|indent(9, True) }}

   {%- endfor %}
