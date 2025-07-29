# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
    'notfound.extension',
    'sphinx_js',
    'sphinx_tabs.tabs',
    'sphinx_jinja2',
    'sphinx.ext.mathjax',
]

latex_engine = 'xelatex'  # allow us to build Unicode chars

autosectionlabel_prefix_document = True

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

js_source_path = '../src/'
html_extra_path = ['static']
html_context = {
    "comment": "This comment is injected manually as a test.",
}

jinja2_env_kwargs = {
    "extensions": ["jinja2.ext.loopcontrols"],
}
