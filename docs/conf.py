# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
import os
version = os.environ.get('READTHEDOCS_VERSION', '')
release = version
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
