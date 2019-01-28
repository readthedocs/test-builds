# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

# Sphinx < 1.3 supports only a string
# Sphinx < 1.8 supports a list of string
# Sphinx >= 1.8 supports a dictionary mapping
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

extensions += [
    'recommonmark',
]
