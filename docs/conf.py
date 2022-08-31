# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'sphinx.ext.intersphinx',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

# Include all your settings here
html_theme = 'sphinx_rtd_theme'
intersphinx_mapping = {
    'mkdocstrings': ('https://mkdocstrings.github.io/', None)
}
