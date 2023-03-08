import os

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

html_static_path = [
    '_static',
]
html_js_files = [
    'build-contract-data.js',
]


# We need to tell to our builder that we are building on Read the Docs
# Ideally, the theme should get this automatically from the environment
# instead of forcing us to define it on its context
if "READTHEDOCS" in os.environ:
    html_context = {
        "READTHEDOCS": True
    }
