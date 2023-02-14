# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'hoverxref.extension',
]

hoverxref_auto_ref = True
hoverxref_roles = [
    'term',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
