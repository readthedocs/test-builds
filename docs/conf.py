# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = "pydata_sphinx_theme"


templates_path = ["templates"]
html_static_path = ["_static"]
html_js_files = ["js/version-selector.js"]
