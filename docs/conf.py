# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_documents
# (startdocname, targetname, title, author, theme, toctree_only)
latex_documents = [
   ('index', 'index.tex', 'test', "author", 'manual'),
   ('index', 'index2.tex', 'test2', "author", 'manual'),
#   ('contents', 'contents.tex', "test", "author", 'howto'),
]
