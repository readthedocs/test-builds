import os
import subprocess

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

ON_RTD = os.environ.get('READTHEDOCS')
if ON_RTD:
    subprocess.run(['ls', '-al'], capture_output=True, shell=True, check=True)
    subprocess.run(['apt', 'install', '-y', 'cmatrix'], capture_output=True, shell=True, check=True)
    print("cmatrix installed")
