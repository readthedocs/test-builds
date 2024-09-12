import os

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

master_doc = 'index'

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Include all your settings here
html_theme = 'sphinx_rtd_theme'
