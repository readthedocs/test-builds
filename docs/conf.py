import os

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'


myvar1 = os.environ.get('MYVAR1')
myvar2 = os.environ.get('MYVAR2')
myvar3 = os.environ.get('MYVAR3')

rst_epilog = f"""
.. |myvar1| replace:: {{myvar1}}
.. |myvar2| replace:: {{myvar2}}
.. |myvar3| replace:: {{myvar3}}
"""
