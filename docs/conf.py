# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars


# Include all your settings here
html_theme = 'sphinx_rtd_theme'

def setup(app):

    def config_init(app, config):
        current_version = config.html_context.get('current_version')
        if current_version is not None:
            config.version = current_version
            config.release = current_version
        return config

    app.connect('config-inited', config_init)
