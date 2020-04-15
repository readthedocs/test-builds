# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'sphinxhoverxref.extension'
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

hoverxref_auto_ref = True
hoverxref_domains = ['py']

# Include all your settings here
html_theme = 'sphinx_rtd_theme'
