# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

rinoh_documents = [
    dict(
        doc='index',             # top-level file (index.rst)
        target='test-builds',    # output file (test-builds.pdf)
    ),
]
