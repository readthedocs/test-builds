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

if os.environ.get('READTHEDOCS') == 'True':
    # Building on Read the Docs
    hoverxref_api_host = 'https://readthedocs.org'
if os.environ.get('LOCAL_READTHEDOCS') == 'True':
    # Building on a local Read the Docs instance
    hoverxref_api_host = 'http://community.dev.readthedocs.io'

# Include all your settings here
html_theme = 'sphinx_rtd_theme'
