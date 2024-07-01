sphinx context
==============

These are all the values injected in the Sphinx context:

.. jinja::

   {%- for key, value in env.config.__dict__.items() %}
     {%- if key in ("values", "_raw_config", "overrides", "_overrides", "_options") %}
       {% continue %}
     {%- endif %}

   {{ key }}:
       .. code-block:: python

          {{ value|pprint|indent(9, True) }}

   {%- endfor %}
