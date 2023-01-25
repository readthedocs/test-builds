# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    # Read the Docs flyout and extras
    'readthedocs_ext.readthedocs',

    'sphinx_autorun',
    'sphinx_simplepdf',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
