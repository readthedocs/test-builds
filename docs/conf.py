# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

# Generates a huge build output
import os
# https://docs.python.org/3/library/os.html#os.urandom
print(os.urandom(int(1 * 1024 ** 2)))
