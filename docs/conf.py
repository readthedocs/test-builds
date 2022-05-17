# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

html_static_path = ['_static']

html_js_files = ['test.js']

latex_engine = 'xelatex'  # allow us to build Unicode chars
root_doc = 'index'


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
