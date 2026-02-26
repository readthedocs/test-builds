# -*- coding: utf-8 -*-
import os

# Make modules in the docs/ directory importable from runblock directives,
# which execute in a subprocess that inherits the environment.
_docs_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = _docs_dir + os.pathsep + os.environ.get('PYTHONPATH', '')

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

# Copy llms.txt to the HTML output
html_extra_path = ['../llms.txt']

###########################################################################
