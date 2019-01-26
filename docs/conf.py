# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

extensions += [
    'nbsphinx',
    'jupyter_sphinx.embed_widgets',
]
