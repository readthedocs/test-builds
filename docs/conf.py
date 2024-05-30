# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'notfound.extension',
    'hoverxref.extension',
    'sphinx_js',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars
hoverxref_auto_ref = True

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

js_source_path = '../src/'
