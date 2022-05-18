# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'sphinx_js',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars
js_source_path = '../src/'


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
