# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'


# Fail the PDF build on purpose by producing a syntax error
#
# ! Undefined control sequence.
# l.71 \useage
#             [titles]{}

# ! LaTeX Error: Missing \begin{document}.
latex_elements = {
    'preamble': r'''
\useage[titles]{}
''',
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_documents
# (startdocname, targetname, title, author, theme, toctree_only)
latex_documents = [
   ('index', 'index.tex', 'Test BuildsDocumentation', 'Donald Docs', 'manual', False),
   ('conf', 'configuration.tex', "", "Donald Docs Jr", 'howto', False),
]
