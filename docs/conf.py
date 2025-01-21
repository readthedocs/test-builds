import os
import sphinx

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

# Include all your settings here
html_theme = 'insipid'

html_extra_path = ['static']

templates_path = ["_templates"]


# TODO: this should be done by the theme itself
def extend_html_context(app, pagename, templatename, context, doctree):
     # Add ``sphinx_version_info`` tuple for use in Jinja templates
     context['sphinx_version_info'] = sphinx.version_info

     # Inject all the Read the Docs environment variables in the context:
     # https://docs.readthedocs.io/en/stable/reference/environment-variables.html
     context['READTHEDOCS'] = os.environ.get("READTHEDOCS", False) == "True"
     if context['READTHEDOCS']:
         for key, value in os.environ.items():
             if key.startswith("READTHEDOCS_"):
                 context[key] = value

def setup(app):
    app.connect("html-page-context", extend_html_context)
