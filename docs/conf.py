import os

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'sphinx.ext.autosectionlabel',
    'hoverxref.extension',
]

if "LOCAL_BUILD" in os.environ:
    hoverxref_api_host = 'http://devthedocs.org'

hoverxref_auto_ref = True
hoverxref_roles = [
    'term',
]

autosectionlabel_prefix_document = True

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
