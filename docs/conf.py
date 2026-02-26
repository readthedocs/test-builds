# -*- coding: utf-8 -*-
import os
import sys

# Make modules in the docs/ directory importable from runblock directives,
# which execute in a subprocess that inherits the environment.
_docs_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHONPATH'] = _docs_dir + os.pathsep + os.environ.get('PYTHONPATH', '')

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

# Copy llms.txt to the HTML output
html_extra_path = ['../llms.txt']


def _generate_profiles(app, exception):
    """Generate interactive HTML profiles and copy them to the build output."""
    if exception or app.builder.name != 'html':
        return

    sys.path.insert(0, _docs_dir)
    from profiling_examples import cpu_intensive_work, memory_intensive_work
    from pyinstrument import Profiler

    cpu_profiler = Profiler()
    cpu_profiler.start()
    cpu_intensive_work()
    cpu_profiler.stop()

    mem_profiler = Profiler()
    mem_profiler.start()
    memory_intensive_work()
    mem_profiler.stop()

    for name, profiler in (('cpu_profile', cpu_profiler), ('memory_profile', mem_profiler)):
        path = os.path.join(app.outdir, name + '.html')
        with open(path, 'w') as fh:
            fh.write(profiler.output_html())


def setup(app):
    app.connect('build-finished', _generate_profiles)

###########################################################################
